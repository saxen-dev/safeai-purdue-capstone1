"""
Hybrid retrieval: dense (FAISS) + sparse (BM25) + RRF + optional cross-encoder.

Falls back gracefully to BM25-only when sentence-transformers or faiss are
not installed.
"""

from __future__ import annotations

import re
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from rank_bm25 import BM25Okapi

# Optional heavy dependencies — graceful fallback when not installed.
try:
    from sentence_transformers import SentenceTransformer
    _SBERT_AVAILABLE = True
except ImportError:
    _SBERT_AVAILABLE = False

try:
    import faiss
    _FAISS_AVAILABLE = True
except ImportError:
    _FAISS_AVAILABLE = False

try:
    from sentence_transformers import CrossEncoder
    _CROSS_ENCODER_AVAILABLE = True
except ImportError:
    _CROSS_ENCODER_AVAILABLE = False


DEFAULT_EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
_RRF_K_DEFAULT = 60


def reciprocal_rank_fusion(
    *ranked_lists: List[Tuple[str, float]],
    k: int = _RRF_K_DEFAULT,
) -> List[Tuple[str, float]]:
    """
    Fuse multiple ranked lists with Reciprocal Rank Fusion.

        RRF(d) = Σ  1 / (k + rank_i(d))

    Returns a new ranked list sorted by fused score descending.
    """
    rrf_scores: Dict[str, float] = defaultdict(float)
    for ranked in ranked_lists:
        for rank, (doc_id, _) in enumerate(ranked):
            rrf_scores[doc_id] += 1.0 / (k + rank + 1)
    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)


class HybridRetriever:
    """
    Hybrid retrieval over a flat chunk list.

    Dense path   : SentenceTransformer embeddings + FAISS IndexFlatIP.
    Sparse path  : BM25Okapi over chunk text + table NLL.
    Fusion       : Reciprocal Rank Fusion.
    Reranking    : optional CrossEncoder (ms-marco-MiniLM-L-6-v2 default).

    When sentence-transformers or faiss are not installed the retriever
    operates in BM25-only mode — callers can check ``dense_available``.
    """

    def __init__(
        self,
        chunks: List[Dict[str, Any]],
        *,
        embed_model_name: str = DEFAULT_EMBED_MODEL,
        rerank_model_name: Optional[str] = DEFAULT_RERANK_MODEL,
        enable_reranking: bool = True,
        top_k_initial: int = 20,
        top_k_fused: int = 10,
        rrf_k: int = _RRF_K_DEFAULT,
    ):
        self.chunks = chunks
        self.top_k_initial = top_k_initial
        self.top_k_fused = top_k_fused
        self.rrf_k = rrf_k

        # Sparse index — always built (None when corpus is empty).
        self._corpus_tokens: List[List[str]]
        self._bm25: Optional[BM25Okapi]
        self._corpus_tokens, self._bm25 = self._build_bm25(chunks)

        # Dense index — only when deps are available.
        self._embed_model: Optional[Any] = None
        self._faiss_index: Optional[Any] = None
        if _SBERT_AVAILABLE and _FAISS_AVAILABLE:
            self._embed_model = SentenceTransformer(embed_model_name)
            self._faiss_index = self._build_faiss(chunks, self._embed_model)

        # Cross-encoder reranker — only when deps are available.
        self._reranker: Optional[Any] = None
        if enable_reranking and _CROSS_ENCODER_AVAILABLE and rerank_model_name:
            try:
                self._reranker = CrossEncoder(rerank_model_name)
            except Exception:
                pass  # non-fatal — fall back to no reranking

    # ------------------------------------------------------------------
    # Index-building helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _chunk_text(chunk: Dict[str, Any]) -> str:
        """
        Return the text to index/embed for a chunk.

        Child chunks (from parent-child Phase 2) carry a ``contextual_content``
        field that prepends a metadata header — use it when present so the
        retriever sees both context and content in a single unit.  Parent chunks
        fall back to text + table NLL concatenation.
        """
        cc = chunk.get("contextual_content", "")
        if cc:
            return cc
        parts = [chunk.get("text", "")]
        for t in chunk.get("tables", []):
            nll = t.get("nll", "")
            if nll:
                parts.append(nll)
        return " ".join(parts)

    @staticmethod
    def _build_bm25(
        chunks: List[Dict[str, Any]],
    ) -> Tuple[List[List[str]], Optional[BM25Okapi]]:
        corpus_tokens: List[List[str]] = []
        for chunk in chunks:
            text = HybridRetriever._chunk_text(chunk).lower()
            tokens = [t for t in re.findall(r"[a-zA-Z0-9]+", text) if len(t) > 1]
            corpus_tokens.append(tokens)
        if not corpus_tokens:
            return corpus_tokens, None
        return corpus_tokens, BM25Okapi(corpus_tokens)

    @staticmethod
    def _build_faiss(
        chunks: List[Dict[str, Any]],
        embed_model: Any,
    ) -> Any:
        texts = [HybridRetriever._chunk_text(c) for c in chunks]
        embeddings = embed_model.encode(
            texts,
            batch_size=32,
            normalize_embeddings=True,
            show_progress_bar=False,
        ).astype(np.float32)
        if embeddings.ndim < 2 or embeddings.shape[0] == 0:
            # Empty chunk list: build a zero-vector index with the model's dimension
            d = embed_model.get_sentence_embedding_dimension() or 768
            index = faiss.IndexFlatIP(d)
            return index
        d = embeddings.shape[1]
        index = faiss.IndexFlatIP(d)
        index.add(embeddings)
        return index

    # ------------------------------------------------------------------
    # Single-modality search
    # ------------------------------------------------------------------

    def _search_dense(self, query: str, k: int) -> List[Tuple[str, float]]:
        if self._embed_model is None or self._faiss_index is None:
            return []
        q_emb = self._embed_model.encode(
            [query], normalize_embeddings=True, show_progress_bar=False
        ).astype(np.float32)
        n = min(k, self._faiss_index.ntotal)
        scores, indices = self._faiss_index.search(q_emb, n)
        return [
            (self.chunks[int(idx)]["chunk_id"], float(score))
            for score, idx in zip(scores[0], indices[0])
            if idx >= 0
        ]

    def _search_bm25(self, query: str, k: int) -> List[Tuple[str, float]]:
        if self._bm25 is None or not self.chunks:
            return []
        tokens = [
            t for t in re.findall(r"[a-zA-Z0-9]+", query.lower()) if len(t) > 1
        ]
        scores = self._bm25.get_scores(tokens)
        top_indices = np.argsort(scores)[::-1][:k]
        # Include all top-k results regardless of score — BM25 already ranks by
        # relevance; the caller's k limit handles the rest.  Filtering > 0 would
        # silently drop results when the IDF formula returns 0 for common terms
        # in small corpora (a known artefact of some rank_bm25 versions).
        return [
            (self.chunks[int(i)]["chunk_id"], float(scores[i]))
            for i in top_indices
        ]

    # ------------------------------------------------------------------
    # Public retrieval
    # ------------------------------------------------------------------

    def retrieve(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """
        Return up to k chunks ranked by hybrid score.

        Each returned chunk dict is a shallow copy of the original with two
        extra fields added:
          score          — fused (or reranked) relevance score
          retrieval_rank — 1-based rank in this result set
        """
        k_init = max(k, self.top_k_initial)
        id_to_chunk = {c["chunk_id"]: c for c in self.chunks}

        dense = self._search_dense(query, k_init)
        sparse = self._search_bm25(query, k_init)

        # Fuse: if both paths returned results use RRF; otherwise keep whichever did.
        if dense and sparse:
            fused: List[Tuple[str, float]] = reciprocal_rank_fusion(
                dense, sparse, k=self.rrf_k
            )
        elif dense:
            fused = dense
        else:
            fused = sparse

        fused = fused[: self.top_k_fused]

        # Optional cross-encoder reranking.
        if self._reranker and fused:
            valid_ids: List[str] = []
            pairs: List[Tuple[str, str]] = []
            for doc_id, _ in fused:
                chunk = id_to_chunk.get(doc_id)
                if chunk:
                    pairs.append((query, chunk.get("text", "")[:512]))
                    valid_ids.append(doc_id)
            if pairs:
                rerank_scores = self._reranker.predict(pairs)
                fused = sorted(
                    zip(valid_ids, map(float, rerank_scores)),
                    key=lambda x: x[1],
                    reverse=True,
                )

        # Assemble final result list.
        results: List[Dict[str, Any]] = []
        seen: set = set()
        for doc_id, score in fused[:k]:
            if doc_id in seen:
                continue
            seen.add(doc_id)
            chunk = id_to_chunk.get(doc_id)
            if chunk:
                out = dict(chunk)
                out["score"] = float(score)
                out["retrieval_rank"] = len(results) + 1
                results.append(out)

        return results

    # ------------------------------------------------------------------
    # Capability flags
    # ------------------------------------------------------------------

    @property
    def dense_available(self) -> bool:
        """True when FAISS + sentence-transformers are installed and indexed."""
        return self._faiss_index is not None

    @property
    def reranking_available(self) -> bool:
        """True when a cross-encoder reranker is loaded."""
        return self._reranker is not None
