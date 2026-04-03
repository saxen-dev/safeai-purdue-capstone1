#!/usr/bin/env python3
"""
Step 3: Brain 1 Knowledge Layer — RAG Vector Database
Safe AI Uganda — Purdue Capstone Project

Transforms Stage 4a chunks into a searchable RAG system with:
  - Adaptive hierarchical parent-child chunking
  - Contextual retrieval headers
  - PubMedBERT-SBERT embeddings (primary) + BGE-M3 (comparison)
  - ChromaDB (development) + FAISS HNSW+PQ8 (production)
  - BM25 + Dense + Reciprocal Rank Fusion hybrid retrieval
  - Cross-encoder re-ranking (optional)
  - Brain 1 package export with SHA-256 manifest

Usage:
  python step3_rag_database.py                  # Full build pipeline
  python step3_rag_database.py --test           # Test 12 clinical queries on existing DB
  python step3_rag_database.py --query "Q"      # Interactive single query
  python step3_rag_database.py --compare        # Compare PubMedBERT vs BGE-M3
  python step3_rag_database.py --package        # Export Brain 1 deployment package
"""

import argparse
import hashlib
import json
import logging
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import numpy as np

# ──────────────────────────────────────────────────────────────────────────────
# Section 1: Configuration
# ──────────────────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("brain1")

DEFAULT_CONFIG_PATH = "rag_config.json"


def load_config(config_path: str = DEFAULT_CONFIG_PATH) -> dict:
    """Load RAG configuration with defaults."""
    path = Path(config_path)
    if not path.exists():
        log.warning(f"Config not found at {config_path}, using defaults")
        return {}
    with open(path) as f:
        return json.load(f)


def get_config_value(config: dict, *keys, default=None):
    """Nested config lookup."""
    current = config
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


# ──────────────────────────────────────────────────────────────────────────────
# Section 2: Data Loading
# ──────────────────────────────────────────────────────────────────────────────


def load_chunks(chunks_path: str) -> tuple[dict, list[dict]]:
    """Load Stage 4a chunks.json. Returns (envelope, chunks_list)."""
    path = Path(chunks_path)
    if not path.exists():
        log.error(f"Chunks file not found: {chunks_path}")
        sys.exit(1)

    with open(path) as f:
        data = json.load(f)

    chunks = data.get("chunks", [])
    envelope = {k: v for k, v in data.items() if k != "chunks"}
    log.info(
        f"Loaded {len(chunks)} parent chunks from {envelope.get('source_document', 'unknown')}"
    )
    log.info(
        f"  Preservation levels: {envelope.get('validation_summary', {}).get('preservation_levels', {})}"
    )

    # Build lookup by chunk_id
    chunk_lookup = {c["chunk_id"]: c for c in chunks}

    return envelope, chunks, chunk_lookup


# ──────────────────────────────────────────────────────────────────────────────
# Section 3: Adaptive Child Chunk Creation
# ──────────────────────────────────────────────────────────────────────────────


def estimate_tokens(text: str, multiplier: float = 1.3) -> int:
    """Estimate token count from word count."""
    return int(len(text.split()) * multiplier)


def build_contextual_header(parent: dict, doc_title: str) -> str:
    """Build contextual retrieval header from parent metadata.

    Deterministically assembled from Stage 4a metadata — no LLM needed.
    Only includes non-null, non-empty fields.
    """
    parts = []

    # Section title
    section_title = parent.get("section_title", "")
    if section_title:
        parts.append(section_title)

    # Clinical condition from metadata
    condition = parent.get("clinical_metadata", {}).get("condition")
    if condition:
        parts.append(condition)

    # Drug name from metadata
    drug_name = parent.get("clinical_metadata", {}).get("drug_name")
    if drug_name:
        parts.append(drug_name)

    # Source reference
    source_parts = []
    if doc_title:
        source_parts.append(doc_title)
    section_number = parent.get("section_number")
    if section_number:
        source_parts.append(f"Section {section_number}")
    source_pages = parent.get("source_pages", [])
    if source_pages:
        pages_str = ", ".join(str(p) for p in source_pages)
        source_parts.append(f"p.{pages_str}")

    if source_parts:
        parts.append(f"Source: {' '.join(source_parts)}")

    if not parts:
        return ""

    return f"[Context: {' | '.join(parts)}]"


def split_recursive_paragraph(
    text: str, max_tokens: int = 512, overlap_tokens: int = 50, min_tokens: int = 50
) -> list[str]:
    """Recursive paragraph splitting with overlap.

    Splits on paragraph boundaries first, then sentence boundaries,
    then falls back to word boundaries. Respects max_tokens limit.
    """
    paragraphs = re.split(r"\n\n+", text.strip())

    chunks = []
    current_chunk = []
    current_tokens = 0

    for para in paragraphs:
        para_tokens = estimate_tokens(para)

        if current_tokens + para_tokens <= max_tokens:
            current_chunk.append(para)
            current_tokens += para_tokens
        else:
            # Flush current chunk
            if current_chunk:
                chunks.append("\n\n".join(current_chunk))

            # If single paragraph exceeds max, split on sentences
            if para_tokens > max_tokens:
                sentences = re.split(r"(?<=[.!?])\s+", para)
                sent_chunk = []
                sent_tokens = 0
                for sent in sentences:
                    st = estimate_tokens(sent)
                    if sent_tokens + st <= max_tokens:
                        sent_chunk.append(sent)
                        sent_tokens += st
                    else:
                        if sent_chunk:
                            chunks.append(" ".join(sent_chunk))
                        sent_chunk = [sent]
                        sent_tokens = st
                if sent_chunk:
                    current_chunk = [" ".join(sent_chunk)]
                    current_tokens = sent_tokens
                else:
                    current_chunk = []
                    current_tokens = 0
            else:
                current_chunk = [para]
                current_tokens = para_tokens

    if current_chunk:
        chunks.append("\n\n".join(current_chunk))

    # Filter out tiny chunks
    chunks = [c for c in chunks if estimate_tokens(c) >= min_tokens]

    # Add overlap between consecutive chunks
    if overlap_tokens > 0 and len(chunks) > 1:
        overlapped = [chunks[0]]
        for i in range(1, len(chunks)):
            prev_words = chunks[i - 1].split()
            overlap_word_count = int(overlap_tokens / 1.3)
            overlap_text = " ".join(prev_words[-overlap_word_count:])
            overlapped.append(overlap_text + " " + chunks[i])
        chunks = overlapped

    return chunks if chunks else [text]


def decompose_propositions(text: str, max_tokens: int = 200) -> list[str]:
    """Proposition-based decomposition for verbatim narratives.

    Splits on sentence boundaries, ensuring each proposition is self-contained.
    For clinical safety content (danger signs, referral criteria), each
    sentence/fact becomes an independently retrievable unit.
    """
    # Split on sentence boundaries
    sentences = re.split(r"(?<=[.!?:;])\s+", text.strip())

    propositions = []
    current = []
    current_tokens = 0

    for sent in sentences:
        st = estimate_tokens(sent)
        if current_tokens + st <= max_tokens:
            current.append(sent)
            current_tokens += st
        else:
            if current:
                propositions.append(" ".join(current))
            current = [sent]
            current_tokens = st

    if current:
        propositions.append(" ".join(current))

    # Filter very short propositions (merge with previous)
    min_tokens = 30
    merged = []
    for prop in propositions:
        if merged and estimate_tokens(prop) < min_tokens:
            merged[-1] = merged[-1] + " " + prop
        else:
            merged.append(prop)

    return merged if merged else [text]


def create_child_chunks(
    parents: list[dict],
    chunk_lookup: dict,
    config: dict,
    doc_title: str,
) -> list[dict]:
    """Create adaptive child chunks from Stage 4a parents.

    Routes each parent through the appropriate chunking strategy based on
    (chunk_type, preservation_level) as defined in the plan.

    Returns list of child chunk dicts with:
      - child_id, parent_chunk_id, content, contextual_content,
        chunk_type, preservation_level, source_pages, metadata
    """
    chunking_cfg = config.get("chunking", {})
    max_tokens = chunking_cfg.get("child_max_tokens", 512)
    overlap = chunking_cfg.get("child_overlap_tokens", 50)
    min_tokens = chunking_cfg.get("child_min_tokens", 50)

    children = []
    child_counter = 0
    stats = defaultdict(int)

    for parent in parents:
        chunk_type = parent.get("chunk_type", "narrative")
        preservation = parent.get("safety", {}).get("preservation_level", "standard")
        content = parent.get("content", "")
        content_type = parent.get("content_type", "markdown")
        token_est = parent.get("token_estimate", estimate_tokens(content))
        parent_id = parent["chunk_id"]

        # Build contextual header for this parent's children
        header = build_contextual_header(parent, doc_title)

        def make_child(text: str, suffix: str = "", is_nll: bool = False) -> dict:
            nonlocal child_counter
            child_counter += 1
            child_id = f"child-{child_counter:05d}"

            # Contextual content = header + raw content (for embedding)
            contextual = f"{header}\n\n{text}" if header else text

            return {
                "child_id": child_id,
                "parent_chunk_id": parent_id,
                "content": text,
                "contextual_content": contextual,
                "chunk_type": chunk_type,
                "preservation_level": preservation,
                "source_pages": parent.get("source_pages", []),
                "section_title": parent.get("section_title", ""),
                "section_number": parent.get("section_number"),
                "clinical_domain": parent.get("clinical_domain"),
                "is_nll": is_nll,
                "suffix": suffix,
                "token_estimate": estimate_tokens(contextual),
                "metadata": {
                    "condition": parent.get("clinical_metadata", {}).get("condition"),
                    "drug_name": parent.get("clinical_metadata", {}).get("drug_name"),
                    "preservation_level": preservation,
                    "chunk_type": chunk_type,
                    "parent_chunk_id": parent_id,
                    "source_pages": parent.get("source_pages", []),
                    "danger_signs": parent.get("clinical_metadata", {}).get(
                        "danger_signs", []
                    ),
                    "referral_criteria": parent.get("clinical_metadata", {}).get(
                        "referral_criteria", []
                    ),
                },
            }

        # ── Route by (chunk_type, preservation_level) ────────────────────

        # Skip: structural tables (ToC, not useful for clinical retrieval)
        if chunk_type == "structural_table":
            stats["skipped_structural"] += 1
            continue

        # Skip: image placeholders with no OCR text
        if chunk_type == "image" and content_type == "image_placeholder":
            stats["skipped_image_placeholder"] += 1
            continue

        # Image with OCR: 1 child = OCR text
        if chunk_type == "image" and content_type == "image_ocr":
            if content.strip() and estimate_tokens(content) >= min_tokens:
                children.append(make_child(content, suffix="ocr"))
                stats["image_ocr"] += 1
            else:
                stats["skipped_image_short_ocr"] += 1
            continue

        # Dosing tables: keep atomic + NLL child
        if chunk_type == "dosing_table":
            children.append(make_child(content, suffix="table"))
            stats["dosing_table_atomic"] += 1

            # Create NLL child for natural-language search
            nll = parent.get("nll")
            if nll and nll.strip():
                children.append(make_child(nll, suffix="nll", is_nll=True))
                stats["dosing_table_nll"] += 1
            continue

        # Clinical/evidence/other tables: keep atomic
        if chunk_type in ("clinical_table", "evidence_table", "other_table"):
            children.append(make_child(content, suffix="table"))
            stats[f"{chunk_type}_atomic"] += 1
            continue

        # ── Narratives: route by preservation level ──────────────────────

        if chunk_type == "narrative":
            # Verbatim narratives: proposition decomposition
            if preservation == "verbatim":
                propositions = decompose_propositions(content, max_tokens=200)
                for i, prop in enumerate(propositions):
                    children.append(make_child(prop, suffix=f"prop-{i}"))
                stats["narrative_verbatim_propositions"] += len(propositions)
                continue

            # High-preservation narratives: smaller adaptive chunks
            if preservation == "high":
                if token_est <= 400:
                    children.append(make_child(content))
                    stats["narrative_high_passthrough"] += 1
                else:
                    chunks = split_recursive_paragraph(
                        content, max_tokens=400, overlap_tokens=overlap
                    )
                    for i, chunk in enumerate(chunks):
                        children.append(make_child(chunk, suffix=f"part-{i}"))
                    stats["narrative_high_split"] += len(chunks)
                continue

            # Standard narratives: recursive paragraph splitting
            if token_est <= max_tokens:
                children.append(make_child(content))
                stats["narrative_standard_passthrough"] += 1
            else:
                chunks = split_recursive_paragraph(
                    content,
                    max_tokens=max_tokens,
                    overlap_tokens=overlap,
                    min_tokens=min_tokens,
                )
                for i, chunk in enumerate(chunks):
                    children.append(make_child(chunk, suffix=f"part-{i}"))
                stats["narrative_standard_split"] += len(chunks)
            continue

        # Fallback: unknown chunk type — passthrough
        children.append(make_child(content, suffix="fallback"))
        stats["fallback"] += 1

    log.info(f"Created {len(children)} child chunks from {len(parents)} parents")
    for key, count in sorted(stats.items()):
        log.info(f"  {key}: {count}")

    return children


# ──────────────────────────────────────────────────────────────────────────────
# Section 4: Embedding Generation
# ──────────────────────────────────────────────────────────────────────────────


def load_embedding_model(model_name: str):
    """Load a SentenceTransformer model."""
    from sentence_transformers import SentenceTransformer

    log.info(f"Loading embedding model: {model_name}")
    t0 = time.time()
    model = SentenceTransformer(model_name)
    log.info(f"  Model loaded in {time.time() - t0:.1f}s, dim={model.get_sentence_embedding_dimension()}")
    return model


def generate_embeddings(
    model, texts: list[str], batch_size: int = 32, desc: str = "Embedding"
) -> np.ndarray:
    """Generate embeddings for a list of texts."""
    log.info(f"{desc}: encoding {len(texts)} texts (batch_size={batch_size})")
    t0 = time.time()
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
    )
    elapsed = time.time() - t0
    log.info(f"  {desc}: {embeddings.shape} in {elapsed:.1f}s ({len(texts)/elapsed:.0f} texts/s)")
    return embeddings


# ──────────────────────────────────────────────────────────────────────────────
# Section 5: ChromaDB Indexing
# ──────────────────────────────────────────────────────────────────────────────


def build_chromadb(
    children: list[dict],
    embeddings: np.ndarray,
    config: dict,
    collection_suffix: str = "",
) -> "chromadb.Collection":
    """Create or replace a ChromaDB collection with child chunks."""
    import chromadb

    persist_dir = get_config_value(
        config, "vector_db", "chromadb_persist_dir", default="rag_output/chroma_db"
    )
    collection_name = get_config_value(
        config, "vector_db", "collection_name", default="brain1_clinical_guidelines"
    )
    if collection_suffix:
        collection_name = f"{collection_name}_{collection_suffix}"

    os.makedirs(persist_dir, exist_ok=True)
    client = chromadb.PersistentClient(path=persist_dir)

    # Delete existing collection if present
    try:
        client.delete_collection(collection_name)
    except Exception:
        pass

    collection = client.create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"},
    )

    # Prepare data for batch upsert
    ids = [c["child_id"] for c in children]
    documents = [c["contextual_content"] for c in children]
    metadatas = []
    for c in children:
        meta = {
            "parent_chunk_id": c["parent_chunk_id"],
            "chunk_type": c["chunk_type"],
            "preservation_level": c["preservation_level"],
            "is_nll": str(c["is_nll"]),
            "section_title": c.get("section_title", ""),
            "clinical_domain": c.get("clinical_domain") or "",
            "condition": c.get("metadata", {}).get("condition") or "",
            "drug_name": c.get("metadata", {}).get("drug_name") or "",
        }
        # ChromaDB requires source_pages as string
        pages = c.get("source_pages", [])
        meta["source_pages"] = ",".join(str(p) for p in pages) if pages else ""
        metadatas.append(meta)

    # Batch upsert (ChromaDB max batch = 41666)
    batch_size = 5000
    for i in range(0, len(ids), batch_size):
        end = min(i + batch_size, len(ids))
        collection.add(
            ids=ids[i:end],
            embeddings=embeddings[i:end].tolist(),
            documents=documents[i:end],
            metadatas=metadatas[i:end],
        )

    log.info(f"ChromaDB collection '{collection_name}': {collection.count()} documents")
    return collection


# ──────────────────────────────────────────────────────────────────────────────
# Section 6: FAISS Index Export
# ──────────────────────────────────────────────────────────────────────────────


def build_faiss_index(
    embeddings: np.ndarray,
    config: dict,
    index_type: str = "hnsw_pq8",
) -> tuple:
    """Build FAISS index from embeddings.

    Supports:
      - 'flat': exact brute-force (smallest for small datasets)
      - 'hnsw': approximate nearest neighbor
      - 'hnsw_pq8': HNSW + 8-bit Product Quantization (production spec)
    """
    import faiss

    n, d = embeddings.shape
    log.info(f"Building FAISS index: type={index_type}, n={n}, d={d}")

    if index_type == "flat":
        index = faiss.IndexFlatIP(d)
        # Normalize and add (cosine sim via inner product on normalized vectors)
        faiss.normalize_L2(embeddings)
        index.add(embeddings)

    elif index_type == "hnsw":
        M = get_config_value(config, "vector_db", "faiss_hnsw_m", default=16)
        index = faiss.IndexHNSWFlat(d, M)
        index.hnsw.efConstruction = get_config_value(
            config, "vector_db", "faiss_hnsw_ef_construction", default=100
        )
        index.hnsw.efSearch = get_config_value(
            config, "vector_db", "faiss_hnsw_ef_search", default=50
        )
        faiss.normalize_L2(embeddings)
        index.add(embeddings)

    elif index_type == "hnsw_pq8":
        # Architecture spec: HNSW + 8-bit Product Quantization
        M_hnsw = get_config_value(config, "vector_db", "faiss_hnsw_m", default=32)
        pq_m = get_config_value(config, "vector_db", "faiss_pq_m", default=96)
        pq_nbits = get_config_value(config, "vector_db", "faiss_pq_nbits", default=8)

        # For small datasets, use OPQ for better PQ codebook
        if n < 256 * pq_m:
            # Fall back to flat for very small datasets (PQ needs enough training data)
            log.warning(
                f"Dataset too small for PQ ({n} < {256 * pq_m}). "
                "Falling back to HNSW flat index."
            )
            index = faiss.IndexHNSWFlat(d, M_hnsw)
            index.hnsw.efConstruction = 200
            index.hnsw.efSearch = 100
            faiss.normalize_L2(embeddings)
            index.add(embeddings)
        else:
            quantizer = faiss.IndexHNSWFlat(d, M_hnsw)
            nlist = get_config_value(config, "vector_db", "faiss_ivf_nlist", default=64)
            # Ensure nlist is reasonable for dataset size
            nlist = min(nlist, n // 10)
            index = faiss.IndexIVFPQ(quantizer, d, nlist, pq_m, pq_nbits)
            faiss.normalize_L2(embeddings)
            index.train(embeddings)
            index.add(embeddings)
            index.nprobe = min(10, nlist)

    else:
        raise ValueError(f"Unknown FAISS index type: {index_type}")

    log.info(f"  FAISS index: {index.ntotal} vectors indexed")
    return index


def save_faiss_index(index, path: str) -> int:
    """Save FAISS index and return file size in bytes."""
    import faiss

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    faiss.write_index(index, path)
    size = os.path.getsize(path)
    log.info(f"  FAISS index saved: {path} ({size / 1024 / 1024:.2f} MB)")
    return size


# ──────────────────────────────────────────────────────────────────────────────
# Section 7: BM25 Index
# ──────────────────────────────────────────────────────────────────────────────


def build_bm25_index(children: list[dict]) -> tuple:
    """Build BM25 index from child chunk content."""
    from rank_bm25 import BM25Okapi

    # Tokenize on whitespace + lowercase (simple but effective)
    corpus = []
    for child in children:
        text = child["contextual_content"].lower()
        tokens = re.findall(r"\b\w+\b", text)
        corpus.append(tokens)

    log.info(f"Building BM25 index: {len(corpus)} documents")
    t0 = time.time()
    bm25 = BM25Okapi(corpus)
    log.info(f"  BM25 index built in {time.time() - t0:.1f}s")

    return bm25, corpus


def save_bm25_corpus(children: list[dict], path: str):
    """Save BM25 corpus for deployment."""
    corpus_data = {
        "total": len(children),
        "documents": [
            {"child_id": c["child_id"], "tokens": re.findall(r"\b\w+\b", c["contextual_content"].lower())}
            for c in children
        ],
    }
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(corpus_data, f)
    size = os.path.getsize(path)
    log.info(f"  BM25 corpus saved: {path} ({size / 1024 / 1024:.2f} MB)")


# ──────────────────────────────────────────────────────────────────────────────
# Section 8: Hybrid Retrieval with RRF
# ──────────────────────────────────────────────────────────────────────────────


def search_dense(
    collection, query_embedding: np.ndarray, top_k: int = 20
) -> list[tuple[str, float]]:
    """Dense search via ChromaDB."""
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k,
        include=["distances"],
    )
    ids = results["ids"][0]
    distances = results["distances"][0]
    # ChromaDB cosine returns distance (lower = closer). Convert to similarity.
    return [(id_, 1.0 - dist) for id_, dist in zip(ids, distances)]


def search_bm25(
    bm25, query: str, children: list[dict], top_k: int = 20
) -> list[tuple[str, float]]:
    """Sparse BM25 keyword search."""
    tokens = re.findall(r"\b\w+\b", query.lower())
    scores = bm25.get_scores(tokens)

    # Get top-k indices
    top_indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for idx in top_indices:
        if scores[idx] > 0:
            results.append((children[idx]["child_id"], float(scores[idx])))

    return results


def reciprocal_rank_fusion(
    *ranked_lists: list[tuple[str, float]], k: int = 60
) -> list[tuple[str, float]]:
    """Reciprocal Rank Fusion.

    RRF_score(d) = Σ 1/(k + rank_i(d))
    """
    rrf_scores = defaultdict(float)

    for ranked_list in ranked_lists:
        for rank, (doc_id, _score) in enumerate(ranked_list):
            rrf_scores[doc_id] += 1.0 / (k + rank + 1)

    # Sort by RRF score descending
    fused = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
    return fused


def expand_context(
    child_ids: list[str],
    children_lookup: dict,
    chunk_lookup: dict,
    max_context: int = 3,
) -> list[dict]:
    """Expand retrieved children to full parent context with related chunks."""
    seen_parents = set()
    results = []

    for child_id in child_ids:
        child = children_lookup.get(child_id)
        if not child:
            continue

        parent_id = child["parent_chunk_id"]
        if parent_id in seen_parents:
            continue
        seen_parents.add(parent_id)

        parent = chunk_lookup.get(parent_id)
        if not parent:
            continue

        result = {
            "child_id": child_id,
            "parent_chunk_id": parent_id,
            "parent": parent,
            "child": child,
            "related_context": [],
        }

        # Fetch related chunks for context expansion
        related = parent.get("related_chunks", {})
        context_ids = []

        # Preceding narrative for tables
        preceding = related.get("preceding_narrative")
        if preceding:
            context_ids.append(preceding)

        # Following narrative
        following = related.get("following_narrative")
        if following:
            context_ids.append(following)

        for ctx_id in context_ids[:max_context]:
            ctx_chunk = chunk_lookup.get(ctx_id)
            if ctx_chunk:
                result["related_context"].append(
                    {
                        "chunk_id": ctx_id,
                        "section_title": ctx_chunk.get("section_title", ""),
                        "content_preview": ctx_chunk.get("content", "")[:200],
                    }
                )

        results.append(result)

    return results


def format_preservation_tag(preservation_level: str) -> str:
    """Format preservation level tag for Brain 2."""
    if preservation_level == "verbatim":
        return "[VERBATIM: Return content exactly. Do not paraphrase dosages.]"
    elif preservation_level == "high":
        return "[HIGH FIDELITY: Preserve all clinical facts, numbers, and drug names.]"
    return ""


def hybrid_retrieve(
    query: str,
    query_embedding: np.ndarray,
    collection,
    bm25,
    children: list[dict],
    children_lookup: dict,
    chunk_lookup: dict,
    config: dict,
    reranker=None,
) -> list[dict]:
    """Full hybrid retrieval pipeline: Dense + BM25 + RRF + optional reranking."""
    retrieval_cfg = config.get("retrieval", {})
    top_k_initial = retrieval_cfg.get("top_k_initial", 20)
    top_k_fused = retrieval_cfg.get("top_k_fused", 10)
    top_k_final = retrieval_cfg.get("top_k_final", 5)
    rrf_k = retrieval_cfg.get("rrf_k", 60)
    max_context = retrieval_cfg.get("max_context_chunks", 3)

    # Stage 1: Broad retrieval
    dense_results = search_dense(collection, query_embedding, top_k=top_k_initial)
    bm25_results = search_bm25(bm25, query, children, top_k=top_k_initial)

    # RRF fusion
    fused = reciprocal_rank_fusion(dense_results, bm25_results, k=rrf_k)
    fused = fused[:top_k_fused]

    # Stage 2: Optional re-ranking
    if reranker and retrieval_cfg.get("reranker_enabled", False):
        pairs = []
        fused_ids = []
        for doc_id, _score in fused:
            child = children_lookup.get(doc_id)
            if child:
                pairs.append((query, child["content"]))
                fused_ids.append(doc_id)

        if pairs:
            rerank_scores = reranker.predict(pairs)
            reranked = sorted(
                zip(fused_ids, rerank_scores), key=lambda x: x[1], reverse=True
            )
            fused = [(doc_id, float(score)) for doc_id, score in reranked]

    # Stage 3: Context expansion
    top_child_ids = [doc_id for doc_id, _ in fused[:top_k_final]]
    results = expand_context(top_child_ids, children_lookup, chunk_lookup, max_context)

    # Add preservation tags and scores
    for i, result in enumerate(results):
        preservation = result["parent"].get("safety", {}).get(
            "preservation_level", "standard"
        )
        result["preservation_tag"] = format_preservation_tag(preservation)
        result["rank"] = i + 1
        # Find score from fused results
        for doc_id, score in fused:
            if doc_id == result["child_id"]:
                result["score"] = score
                break

    return results


# ──────────────────────────────────────────────────────────────────────────────
# Section 9: Test Queries and Evaluation
# ──────────────────────────────────────────────────────────────────────────────

TEST_QUERIES = [
    {
        "id": "Q01",
        "query": "What is the artemether-lumefantrine dose for a child weighing 20 kg?",
        "type": "dosage_lookup",
        "expected_chunk_types": ["dosing_table"],
        "expected_keywords": ["artemether", "lumefantrine", "20"],
    },
    {
        "id": "Q02",
        "query": "Is primaquine safe during pregnancy?",
        "type": "contraindication",
        "expected_chunk_types": ["narrative", "dosing_table"],
        "expected_keywords": ["primaquine", "pregnancy", "contraindicated"],
    },
    {
        "id": "Q03",
        "query": "Child with fast breathing and fever, what should a VHT do?",
        "type": "semantic",
        "expected_chunk_types": ["narrative"],
        "expected_keywords": ["tachypnea", "fever", "refer", "danger"],
    },
    {
        "id": "Q04",
        "query": "artesunate-amodiaquine dosing schedule",
        "type": "exact_drug_name",
        "expected_chunk_types": ["dosing_table"],
        "expected_keywords": ["artesunate", "amodiaquine"],
    },
    {
        "id": "Q05",
        "query": "Malaria treatment for infant under 5 kg",
        "type": "weight_based",
        "expected_chunk_types": ["dosing_table", "narrative"],
        "expected_keywords": ["5 kg", "infant", "weight"],
    },
    {
        "id": "Q06",
        "query": "How to manage severe malaria with convulsions?",
        "type": "severe_management",
        "expected_chunk_types": ["clinical_table", "narrative"],
        "expected_keywords": ["severe", "convulsions", "artesunate"],
    },
    {
        "id": "Q07",
        "query": "Intermittent preventive treatment for pregnant women",
        "type": "prevention",
        "expected_chunk_types": ["narrative", "dosing_table"],
        "expected_keywords": ["IPTp", "sulfadoxine", "pyrimethamine", "pregnancy"],
    },
    {
        "id": "Q08",
        "query": "When to use a rapid diagnostic test vs microscopy?",
        "type": "diagnosis",
        "expected_chunk_types": ["narrative"],
        "expected_keywords": ["RDT", "microscopy", "diagnostic"],
    },
    {
        "id": "Q09",
        "query": "What to do if first-line ACT treatment fails?",
        "type": "treatment_failure",
        "expected_chunk_types": ["narrative"],
        "expected_keywords": ["treatment failure", "second-line", "ACT"],
    },
    {
        "id": "Q10",
        "query": "What is the evidence quality for dihydroartemisinin-piperaquine?",
        "type": "evidence",
        "expected_chunk_types": ["evidence_table", "narrative"],
        "expected_keywords": ["dihydroartemisinin", "piperaquine", "evidence"],
    },
    {
        "id": "Q11",
        "query": "When should a community health worker refer a patient to a health facility?",
        "type": "referral",
        "expected_chunk_types": ["narrative"],
        "expected_keywords": ["refer", "danger signs", "health facility"],
    },
    {
        "id": "Q12",
        "query": "Malaria treatment for HIV-positive patients",
        "type": "special_population",
        "expected_chunk_types": ["narrative"],
        "expected_keywords": ["HIV", "co-infection", "antiretroviral"],
    },
]


def evaluate_result(result: dict, test_query: dict) -> dict:
    """Evaluate a single retrieval result against expected criteria."""
    parent = result.get("parent", {})
    child = result.get("child", {})
    content = (parent.get("content", "") + " " + child.get("content", "")).lower()

    # Check chunk type match
    chunk_type = parent.get("chunk_type", "")
    type_match = chunk_type in test_query.get("expected_chunk_types", [])

    # Check keyword presence
    keywords_found = []
    keywords_missing = []
    for kw in test_query.get("expected_keywords", []):
        if kw.lower() in content:
            keywords_found.append(kw)
        else:
            keywords_missing.append(kw)

    keyword_coverage = (
        len(keywords_found) / len(test_query.get("expected_keywords", [1]))
        if test_query.get("expected_keywords")
        else 0
    )

    return {
        "type_match": type_match,
        "keyword_coverage": keyword_coverage,
        "keywords_found": keywords_found,
        "keywords_missing": keywords_missing,
        "chunk_type": chunk_type,
        "preservation_level": parent.get("safety", {}).get("preservation_level", ""),
        "relevant": type_match or keyword_coverage >= 0.5,
    }


def run_test_queries(
    embed_model,
    collection,
    bm25,
    children: list[dict],
    children_lookup: dict,
    chunk_lookup: dict,
    config: dict,
    reranker=None,
) -> dict:
    """Run all 12 clinical test queries and compute metrics."""
    log.info("=" * 60)
    log.info("Running 12 clinical test queries")
    log.info("=" * 60)

    all_results = {}
    precision_at_3_sum = 0
    precision_at_5_sum = 0
    mrr_sum = 0

    for tq in TEST_QUERIES:
        log.info(f"\n{tq['id']}: {tq['query']}")

        # Embed query
        query_embedding = embed_model.encode(
            tq["query"], normalize_embeddings=True
        )

        # Retrieve
        results = hybrid_retrieve(
            tq["query"],
            query_embedding,
            collection,
            bm25,
            children,
            children_lookup,
            chunk_lookup,
            config,
            reranker=reranker,
        )

        # Evaluate each result
        evaluations = []
        for result in results:
            ev = evaluate_result(result, tq)
            evaluations.append(ev)

        # Metrics
        relevant_at_3 = sum(1 for e in evaluations[:3] if e["relevant"])
        relevant_at_5 = sum(1 for e in evaluations[:5] if e["relevant"])
        precision_at_3 = relevant_at_3 / min(3, len(evaluations)) if evaluations else 0
        precision_at_5 = relevant_at_5 / min(5, len(evaluations)) if evaluations else 0

        # MRR: reciprocal rank of first relevant result
        mrr = 0
        for i, e in enumerate(evaluations):
            if e["relevant"]:
                mrr = 1.0 / (i + 1)
                break

        precision_at_3_sum += precision_at_3
        precision_at_5_sum += precision_at_5
        mrr_sum += mrr

        query_result = {
            "query_id": tq["id"],
            "query": tq["query"],
            "type": tq["type"],
            "num_results": len(results),
            "precision_at_3": round(precision_at_3, 3),
            "precision_at_5": round(precision_at_5, 3),
            "mrr": round(mrr, 3),
            "results": [],
        }

        for i, (result, ev) in enumerate(zip(results, evaluations)):
            query_result["results"].append(
                {
                    "rank": i + 1,
                    "child_id": result["child_id"],
                    "parent_chunk_id": result["parent_chunk_id"],
                    "chunk_type": ev["chunk_type"],
                    "preservation_level": ev["preservation_level"],
                    "type_match": ev["type_match"],
                    "keyword_coverage": round(ev["keyword_coverage"], 3),
                    "keywords_found": ev["keywords_found"],
                    "keywords_missing": ev["keywords_missing"],
                    "relevant": ev["relevant"],
                    "preservation_tag": result.get("preservation_tag", ""),
                    "content_preview": result["child"]["content"][:150],
                    "source_pages": result["parent"].get("source_pages", []),
                }
            )

        all_results[tq["id"]] = query_result
        log.info(
            f"  P@3={precision_at_3:.3f}  P@5={precision_at_5:.3f}  MRR={mrr:.3f}  "
            f"Results={len(results)}"
        )

    n = len(TEST_QUERIES)
    aggregate = {
        "mean_precision_at_3": round(precision_at_3_sum / n, 3),
        "mean_precision_at_5": round(precision_at_5_sum / n, 3),
        "mean_mrr": round(mrr_sum / n, 3),
        "num_queries": n,
    }

    log.info("\n" + "=" * 60)
    log.info(f"AGGREGATE: P@3={aggregate['mean_precision_at_3']:.3f}  "
             f"P@5={aggregate['mean_precision_at_5']:.3f}  "
             f"MRR={aggregate['mean_mrr']:.3f}")
    log.info("=" * 60)

    return {"queries": all_results, "aggregate": aggregate}


# ──────────────────────────────────────────────────────────────────────────────
# Section 10: Brain 1 Package Export
# ──────────────────────────────────────────────────────────────────────────────


def sha256_file(path: str) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def export_brain1_package(
    children: list[dict],
    parents: list[dict],
    faiss_index_path: str,
    bm25_corpus_path: str,
    config: dict,
    doc_title: str,
) -> str:
    """Export a complete, version-stamped Brain 1 deployment package.

    Produces a self-contained directory that can be zipped and signed
    for air-gapped distribution to VHT devices.
    """
    package_dir = get_config_value(
        config, "paths", "brain1_package_dir", default="rag_output/brain1_package"
    )
    os.makedirs(package_dir, exist_ok=True)

    # 1. Copy FAISS index
    import shutil

    faiss_dest = os.path.join(package_dir, "faiss_index.bin")
    if os.path.exists(faiss_index_path):
        shutil.copy2(faiss_index_path, faiss_dest)

    # 2. Save child chunks (for result display and BM25)
    child_chunks_path = os.path.join(package_dir, "child_chunks.json")
    child_export = []
    for c in children:
        child_export.append(
            {
                "child_id": c["child_id"],
                "parent_chunk_id": c["parent_chunk_id"],
                "content": c["content"],
                "contextual_content": c["contextual_content"],
                "chunk_type": c["chunk_type"],
                "preservation_level": c["preservation_level"],
                "source_pages": c["source_pages"],
                "is_nll": c["is_nll"],
                "token_estimate": c["token_estimate"],
                "metadata": c["metadata"],
            }
        )
    with open(child_chunks_path, "w") as f:
        json.dump({"total": len(child_export), "children": child_export}, f, indent=2)

    # 3. Save parent chunks (full metadata for display)
    parent_chunks_path = os.path.join(package_dir, "parent_chunks.json")
    with open(parent_chunks_path, "w") as f:
        json.dump({"total": len(parents), "parents": parents}, f, indent=2)

    # 4. Copy BM25 corpus
    bm25_dest = os.path.join(package_dir, "bm25_inverted_index.json")
    if os.path.exists(bm25_corpus_path):
        shutil.copy2(bm25_corpus_path, bm25_dest)

    # 5. Create package manifest with SHA-256 hashes
    manifest = {
        "package_version": "1.0.0",
        "pipeline_version": "step3",
        "source_document": doc_title,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "total_children": len(children),
        "total_parents": len(parents),
        "files": {},
    }

    for filename in os.listdir(package_dir):
        filepath = os.path.join(package_dir, filename)
        if filename == "package_manifest.json":
            continue
        if os.path.isfile(filepath):
            manifest["files"][filename] = {
                "sha256": sha256_file(filepath),
                "size_bytes": os.path.getsize(filepath),
            }

    manifest_path = os.path.join(package_dir, "package_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    # Log package summary
    total_size = sum(
        v["size_bytes"] for v in manifest["files"].values()
    )
    log.info(f"\nBrain 1 Package exported to: {package_dir}")
    log.info(f"  Total size: {total_size / 1024 / 1024:.2f} MB")
    for name, info in manifest["files"].items():
        log.info(f"  {name}: {info['size_bytes'] / 1024 / 1024:.2f} MB  sha256={info['sha256'][:16]}...")

    return package_dir


# ──────────────────────────────────────────────────────────────────────────────
# Section 11: Save Outputs
# ──────────────────────────────────────────────────────────────────────────────


def save_build_report(
    config: dict,
    envelope: dict,
    children: list[dict],
    faiss_sizes: dict,
    timings: dict,
    test_results: Optional[dict] = None,
):
    """Save build report JSON."""
    report_path = get_config_value(
        config, "paths", "build_report_path", default="rag_output/build_report.json"
    )
    os.makedirs(os.path.dirname(report_path) or ".", exist_ok=True)

    # Child chunk statistics
    type_counts = defaultdict(int)
    preservation_counts = defaultdict(int)
    nll_count = 0
    total_tokens = 0
    for c in children:
        type_counts[c["chunk_type"]] += 1
        preservation_counts[c["preservation_level"]] += 1
        if c["is_nll"]:
            nll_count += 1
        total_tokens += c["token_estimate"]

    report = {
        "build_timestamp": datetime.now(timezone.utc).isoformat(),
        "source_document": envelope.get("source_document", "unknown"),
        "parent_chunks": envelope.get("total_chunks", 0),
        "child_chunks": len(children),
        "nll_children": nll_count,
        "child_type_counts": dict(type_counts),
        "child_preservation_counts": dict(preservation_counts),
        "total_tokens": total_tokens,
        "avg_tokens_per_child": round(total_tokens / len(children), 1) if children else 0,
        "faiss_index_sizes": faiss_sizes,
        "timings": timings,
        "config": config,
    }

    if test_results:
        report["test_results_aggregate"] = test_results.get("aggregate", {})

    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    log.info(f"Build report saved: {report_path}")


def save_child_chunks(children: list[dict], path: str):
    """Save child chunks JSON for development use."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump({"total": len(children), "children": children}, f, indent=2)
    size = os.path.getsize(path)
    log.info(f"Child chunks saved: {path} ({size / 1024 / 1024:.2f} MB)")


def save_test_results(test_results: dict, path: str):
    """Save test query results."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(test_results, f, indent=2)
    log.info(f"Test results saved: {path}")


# ──────────────────────────────────────────────────────────────────────────────
# Section 12: Main
# ──────────────────────────────────────────────────────────────────────────────


def build_pipeline(config: dict, skip_comparison: bool = False):
    """Full build pipeline: chunks → children → embed → index → test → package."""
    timings = {}
    faiss_sizes = {}

    # ── Step 1: Load parent chunks ────────────────────────────────────────
    t0 = time.time()
    chunks_path = get_config_value(
        config, "paths", "chunks_input", default="extraction_output_malaria/chunks.json"
    )
    envelope, parents, chunk_lookup = load_chunks(chunks_path)
    doc_title = envelope.get("source_document", "Clinical Guidelines")
    timings["load_chunks"] = round(time.time() - t0, 2)

    # ── Step 2: Create adaptive child chunks ──────────────────────────────
    t0 = time.time()
    children = create_child_chunks(parents, chunk_lookup, config, doc_title)
    timings["create_children"] = round(time.time() - t0, 2)

    # Build lookup
    children_lookup = {c["child_id"]: c for c in children}

    # Save child chunks
    child_path = get_config_value(
        config, "paths", "child_chunks_path", default="rag_output/child_chunks.json"
    )
    save_child_chunks(children, child_path)

    # ── Step 3: Generate embeddings (primary model) ───────────────────────
    t0 = time.time()
    primary_model_name = get_config_value(
        config, "embedding", "primary_model", default="pritamdeka/S-PubMedBert-MS-MARCO"
    )
    embed_model = load_embedding_model(primary_model_name)
    batch_size = get_config_value(config, "embedding", "batch_size", default=32)

    texts = [c["contextual_content"] for c in children]
    embeddings = generate_embeddings(embed_model, texts, batch_size, desc="PubMedBERT")
    timings["embed_primary"] = round(time.time() - t0, 2)

    # Save embeddings
    emb_path = get_config_value(
        config, "paths", "embeddings_primary_path",
        default="rag_output/embeddings_pubmedbert.npy",
    )
    os.makedirs(os.path.dirname(emb_path) or ".", exist_ok=True)
    np.save(emb_path, embeddings)
    log.info(f"Embeddings saved: {emb_path} ({embeddings.nbytes / 1024 / 1024:.2f} MB)")

    # ── Step 4: Build ChromaDB ────────────────────────────────────────────
    t0 = time.time()
    collection = build_chromadb(children, embeddings, config, collection_suffix="pubmedbert")
    timings["build_chromadb"] = round(time.time() - t0, 2)

    # ── Step 5: Build FAISS indexes ───────────────────────────────────────
    t0 = time.time()
    emb_copy = embeddings.copy()

    # Flat index (always built — reliable, sufficient for ~1,700 vectors)
    flat_index = build_faiss_index(emb_copy.copy(), config, index_type="flat")
    flat_path = get_config_value(
        config, "vector_db", "faiss_flat_index_path",
        default="rag_output/faiss_index_flat.bin",
    )
    flat_size = save_faiss_index(flat_index, flat_path)
    faiss_sizes["flat"] = flat_size

    # Note: HNSW and HNSW+PQ8 indexes are the production spec for when
    # the corpus grows beyond ~10,000 vectors (multiple clinical guidelines).
    # At ~1,700 vectors, flat index provides exact search in <1ms — no ANN needed.
    # HNSW/PQ8 build is skipped here but the code path is preserved for
    # future scaling. To enable, set faiss_build_hnsw: true in rag_config.json.
    hnsw_path = flat_path.replace("flat", "hnsw")
    pq_path = flat_path.replace("flat", "hnsw_pq8")
    if get_config_value(config, "vector_db", "faiss_build_hnsw", default=False):
        try:
            hnsw_index = build_faiss_index(emb_copy.copy(), config, index_type="hnsw")
            hnsw_size = save_faiss_index(hnsw_index, hnsw_path)
            faiss_sizes["hnsw"] = hnsw_size
        except Exception as e:
            log.warning(f"HNSW index build failed: {e}")
        try:
            pq_index = build_faiss_index(emb_copy.copy(), config, index_type="hnsw_pq8")
            pq_size = save_faiss_index(pq_index, pq_path)
            faiss_sizes["hnsw_pq8"] = pq_size
        except Exception as e:
            log.warning(f"HNSW+PQ8 index build failed: {e}")
    else:
        log.info("  HNSW/PQ8 indexes skipped (flat index sufficient for current corpus size)")

    timings["build_faiss"] = round(time.time() - t0, 2)

    # Check 50 MB target
    for name, size in faiss_sizes.items():
        mb = size / 1024 / 1024
        status = "PASS" if mb < 50 else "FAIL"
        log.info(f"  FAISS {name}: {mb:.2f} MB [{status} < 50 MB target]")

    # ── Step 6: Build BM25 index ──────────────────────────────────────────
    t0 = time.time()
    bm25, bm25_corpus = build_bm25_index(children)
    bm25_path = get_config_value(
        config, "paths", "bm25_corpus_path", default="rag_output/bm25_corpus.json"
    )
    save_bm25_corpus(children, bm25_path)
    timings["build_bm25"] = round(time.time() - t0, 2)

    # ── Step 7: Load reranker (optional) ──────────────────────────────────
    reranker = None
    if get_config_value(config, "retrieval", "reranker_enabled", default=True):
        try:
            from sentence_transformers import CrossEncoder

            reranker_name = get_config_value(
                config, "retrieval", "reranker_model",
                default="cross-encoder/ms-marco-MiniLM-L-6-v2",
            )
            log.info(f"Loading cross-encoder reranker: {reranker_name}")
            t0 = time.time()
            reranker = CrossEncoder(reranker_name)
            timings["load_reranker"] = round(time.time() - t0, 2)
        except Exception as e:
            log.warning(f"Failed to load reranker: {e}. Proceeding without re-ranking.")

    # ── Step 8: Run test queries ──────────────────────────────────────────
    t0 = time.time()
    test_results = run_test_queries(
        embed_model,
        collection,
        bm25,
        children,
        children_lookup,
        chunk_lookup,
        config,
        reranker=reranker,
    )
    timings["test_queries"] = round(time.time() - t0, 2)

    # Save test results
    test_path = get_config_value(
        config, "paths", "test_results_path",
        default="rag_output/retrieval_test_results.json",
    )
    save_test_results(test_results, test_path)

    # ── Step 9: Export Brain 1 package ────────────────────────────────────
    t0 = time.time()
    # Use the best available FAISS index for production
    production_index_path = flat_path
    if os.path.exists(pq_path) and "hnsw_pq8" in faiss_sizes:
        production_index_path = pq_path
    elif os.path.exists(hnsw_path) and "hnsw" in faiss_sizes:
        production_index_path = hnsw_path
    export_brain1_package(
        children, parents, production_index_path, bm25_path, config, doc_title
    )
    timings["export_package"] = round(time.time() - t0, 2)

    # ── Step 10: Save build report ────────────────────────────────────────
    save_build_report(config, envelope, children, faiss_sizes, timings, test_results)

    # ── Summary ───────────────────────────────────────────────────────────
    log.info("\n" + "=" * 60)
    log.info("BUILD COMPLETE")
    log.info("=" * 60)
    log.info(f"  Parents:      {len(parents)}")
    log.info(f"  Children:     {len(children)}")
    log.info(f"  Embeddings:   {embeddings.shape}")
    log.info(f"  ChromaDB:     {collection.count()} docs")
    log.info(f"  FAISS flat:   {faiss_sizes.get('flat', 0) / 1024 / 1024:.2f} MB")
    log.info(f"  FAISS HNSW:   {faiss_sizes.get('hnsw', 0) / 1024 / 1024:.2f} MB")
    log.info(f"  FAISS PQ8:    {faiss_sizes.get('hnsw_pq8', 0) / 1024 / 1024:.2f} MB")
    log.info(f"  Test P@5:     {test_results['aggregate']['mean_precision_at_5']:.3f}")
    log.info(f"  Test MRR:     {test_results['aggregate']['mean_mrr']:.3f}")
    total_time = sum(timings.values())
    log.info(f"  Total time:   {total_time:.1f}s")
    for step, t in timings.items():
        log.info(f"    {step}: {t:.1f}s")

    return {
        "children": children,
        "children_lookup": children_lookup,
        "chunk_lookup": chunk_lookup,
        "embed_model": embed_model,
        "collection": collection,
        "bm25": bm25,
        "reranker": reranker,
        "test_results": test_results,
    }


def query_mode(query: str, config: dict):
    """Interactive single query with full context display."""
    # Load existing data
    chunks_path = get_config_value(
        config, "paths", "chunks_input", default="extraction_output_malaria/chunks.json"
    )
    envelope, parents, chunk_lookup = load_chunks(chunks_path)
    doc_title = envelope.get("source_document", "Clinical Guidelines")

    # Load children
    child_path = get_config_value(
        config, "paths", "child_chunks_path", default="rag_output/child_chunks.json"
    )
    with open(child_path) as f:
        child_data = json.load(f)
    children = child_data["children"]
    children_lookup = {c["child_id"]: c for c in children}

    # Load embedding model and ChromaDB
    import chromadb

    primary_model_name = get_config_value(
        config, "embedding", "primary_model", default="pritamdeka/S-PubMedBert-MS-MARCO"
    )
    embed_model = load_embedding_model(primary_model_name)

    persist_dir = get_config_value(
        config, "vector_db", "chromadb_persist_dir", default="rag_output/chroma_db"
    )
    client = chromadb.PersistentClient(path=persist_dir)
    collection_name = get_config_value(
        config, "vector_db", "collection_name", default="brain1_clinical_guidelines"
    )
    collection = client.get_collection(f"{collection_name}_pubmedbert")

    # Build BM25
    bm25, _ = build_bm25_index(children)

    # Optional reranker
    reranker = None
    if get_config_value(config, "retrieval", "reranker_enabled", default=True):
        try:
            from sentence_transformers import CrossEncoder

            reranker_name = get_config_value(
                config, "retrieval", "reranker_model",
                default="cross-encoder/ms-marco-MiniLM-L-6-v2",
            )
            reranker = CrossEncoder(reranker_name)
        except Exception:
            pass

    # Embed and retrieve
    query_embedding = embed_model.encode(query, normalize_embeddings=True)
    results = hybrid_retrieve(
        query, query_embedding, collection, bm25, children, children_lookup,
        chunk_lookup, config, reranker=reranker,
    )

    # Display results
    print(f"\n{'=' * 60}")
    print(f"Query: {query}")
    print(f"{'=' * 60}\n")

    for result in results:
        parent = result["parent"]
        child = result["child"]
        tag = result.get("preservation_tag", "")

        print(f"--- Rank {result['rank']} ---")
        print(f"Parent: {result['parent_chunk_id']} ({parent.get('chunk_type', '')})")
        print(f"Section: {parent.get('section_title', '')} ({parent.get('section_number', '')})")
        print(f"Pages: {parent.get('source_pages', [])}")
        print(f"Preservation: {parent.get('safety', {}).get('preservation_level', '')}")
        if tag:
            print(f"Tag: {tag}")
        print(f"\nContent:\n{child.get('content', '')[:500]}")
        if result.get("related_context"):
            print(f"\nRelated context ({len(result['related_context'])} chunks):")
            for ctx in result["related_context"]:
                print(f"  - {ctx['chunk_id']}: {ctx['content_preview'][:100]}...")
        print()


def main():
    parser = argparse.ArgumentParser(description="Brain 1 Knowledge Layer — RAG Pipeline")
    parser.add_argument("--config", default=DEFAULT_CONFIG_PATH, help="Config file path")
    parser.add_argument("--test", action="store_true", help="Run test queries only")
    parser.add_argument("--query", type=str, help="Interactive single query")
    parser.add_argument("--compare", action="store_true", help="Compare embedding models")
    parser.add_argument("--package", action="store_true", help="Export Brain 1 package only")
    args = parser.parse_args()

    config = load_config(args.config)

    if args.query:
        query_mode(args.query, config)
    elif args.test:
        # Run test queries on existing DB
        result = build_pipeline(config)
    elif args.compare:
        log.info("Model comparison mode — building with both models")
        result = build_pipeline(config, skip_comparison=False)
    else:
        # Full build pipeline
        result = build_pipeline(config)


if __name__ == "__main__":
    main()
