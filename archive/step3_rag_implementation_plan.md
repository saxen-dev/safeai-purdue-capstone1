# Step 3: Stand Up a RAG Vector Database — Implementation Plan

**Safe AI Uganda — Purdue Capstone Project**
**Prepared:** 06.03.2026
**Status:** Proposed — pending team review

---

## Context

Stages 1–4b of the extraction pipeline are complete and merged to main. Stage 4a produced `chunks.json` with 1,478 metadata-rich chunks (preservation levels, clinical metadata, related-chunk links, NLL, verified_by placeholders). Step 3 transforms these chunks into a searchable Brain 1 Knowledge Layer — the RAG vector database that the entire Safe AI system depends on.

**Current environment:** Python 3.12.10, torch 2.2.2 + transformers 4.40.2 already installed, 17 GB RAM, 28 GB free disk. No RAG packages installed yet (no sentence-transformers, chromadb, faiss, rank-bm25). No `requirements.txt` exists.

**Go/No-Go Gate:** Brain 1 must successfully return relevant results before proceeding to Step 4 (Brain 2). If retrieval fails, the entire Two-Brain architecture fails.

---

## Key Design Decisions

### 1. Parent-Child Chunking (not re-chunking from scratch)

Stage 4a already produced semantically meaningful chunks with rich metadata (preservation levels, clinical metadata, related-chunk links, physician review templates). **Re-chunking from scratch would destroy all of this.**

Instead:
- **Parent chunks** = Stage 4a's 1,478 chunks (source of truth with all metadata)
- **Child search chunks** = Derived from parents for embedding:
  - Parent ≤512 tokens → 1 child = parent content (1,283 chunks)
  - Parent >512 tokens (narrative) → split on paragraph boundaries, ~400 tokens, 50-token overlap (~280 children from 139 parents)
  - Parent >512 tokens (table) → split on row boundaries (~100 children from 54 parents)
  - Dosing tables with NLL → additional NLL-text child for natural-language search (~25 extra)
  - Image chunks (35) → skipped (no embeddable text)
- **Search on children, retrieve parents** with full metadata
- **Estimated total children: ~1,650–1,700**

This approach gives us the spec-recommended hierarchical parent-child chunking (400–512 tokens with overlap) while preserving Stage 4a's metadata-rich parent chunks as the authoritative source of truth.

### 2. Vector Database: ChromaDB (prototype) + FAISS (production export)

- **ChromaDB** for development: built-in metadata filtering (preservation_level, condition, drug_name), persistence, easy API
- **FAISS with HNSW** for production mobile deployment: <50 MB index target
- Both use the same embeddings; FAISS index exported from ChromaDB vectors
- For ~1,700 vectors × 768 dims, FAISS HNSW index ≈ 15 MB (well under 50 MB even without Product Quantization)

### 3. Embedding Model: PubMedBERT-SBERT

- **Primary:** `pritamdeka/S-PubMedBert-MS-MARCO` (768-dim, clinical domain, retrieval-tuned)
- **Baseline comparison:** `sentence-transformers/all-MiniLM-L6-v2` (384-dim, general purpose)
- Both models run on the same 12 test queries; we document which performs better for clinical retrieval and why

### 4. Hybrid Retrieval: Dense + BM25 + Reciprocal Rank Fusion

- **Dense:** ChromaDB cosine similarity on child embeddings (handles semantic matching — e.g., "fast breathing" → "tachypnea")
- **Sparse:** BM25 keyword matching (critical for exact drug names like "artemether-lumefantrine" and dosage values like "80+480 mg")
- **Fusion:** Reciprocal Rank Fusion (k=60) merges both ranked lists
- **Context expansion:** After top-K children retrieved, map to parents → fetch preceding/following narratives via `related_chunks` links

### 5. Preservation Level Enforcement

When returning results, tag each chunk for downstream Brain 2:
- `verbatim` (31 chunks): `[VERBATIM: Return content exactly. Do not paraphrase dosages.]`
- `high` (325 chunks): `[HIGH FIDELITY: Preserve all clinical facts, numbers, and drug names.]`
- `standard` (1,122 chunks): no tag — paraphrasing acceptable

---

## Deliverables

### Files to Create

| File | Description |
|---|---|
| `requirements.txt` | Dependency management (sentence-transformers, chromadb, faiss-cpu, rank-bm25) |
| `rag_config.json` | All tunable parameters (embedding model, chunk sizes, FAISS params, retrieval config) |
| `step3_rag_database.py` | Main RAG pipeline script (~1,100 lines) — build, test, and query modes |
| `step3_technology_rationale.md` | Why ChromaDB + FAISS, PubMedBERT, BM25+RRF, parent-child chunking |
| `step3_rag_summary.md` | 2-page summary (tech choices, config, performance, architecture decisions) |
| `step3_retrieval_test_results.md` | 12 test queries with per-query results + aggregate metrics |
| `step3_setup_instructions.md` | Reproduction instructions for successor team |

### Files to Modify

| File | Change |
|---|---|
| `.gitignore` | Add `rag_output/` (regenerated, not committed) |
| `extraction_pipeline_overview.md` | Add Step 3 section showing RAG integration |

**No changes to any extraction pipeline scripts (Stages 1–4b).**

---

## Script Design: `step3_rag_database.py`

### Modes of Operation

```
python step3_rag_database.py              # Build: create children → embed → index → test → report
python step3_rag_database.py --test       # Test only: run 12 queries on existing DB
python step3_rag_database.py --query "Q"  # Interactive: single query with full context
python step3_rag_database.py --compare    # Compare PubMedBERT vs MiniLM on test queries
```

### Section Breakdown

| Section | Purpose | Est. Lines |
|---|---|---|
| 1. Imports | sentence_transformers, chromadb, faiss, rank_bm25, numpy, json, argparse | ~20 |
| 2. Configuration | Load from rag_config.json with defaults. Constants for chunking, retrieval, paths | ~40 |
| 3. Data Loading | Load chunks.json, build chunk lookup dict | ~60 |
| 4. Child Chunk Creation | Parent-child hierarchy: split large chunks, create NLL children for dosing tables | ~200 |
| 5. Embedding Generation | Load SentenceTransformer model, batch encode all children, save to .npy | ~80 |
| 6. ChromaDB Indexing | Init persistent ChromaDB, upsert children with embeddings + metadata | ~100 |
| 7. FAISS Index Export | Build HNSW index from embeddings, report size vs 50 MB target | ~80 |
| 8. BM25 Index | Tokenize children, build BM25Okapi index, save corpus | ~60 |
| 9. Hybrid Retrieval | Dense + sparse search, RRF fusion, parent expansion, context expansion | ~150 |
| 10. Test Queries | 12 clinical queries, relevance scoring, metrics (precision@k, MRR) | ~200 |
| 11. Save Outputs | Build report JSON, retrieval test results JSON | ~80 |
| 12. Main | argparse, 9-step build mode, test mode, query mode, scorecard | ~120 |
| **Total** | | **~1,100** |

---

## 12 Clinical Test Queries

| # | Query | Type | What It Tests |
|---|---|---|---|
| Q01 | "What is the artemether-lumefantrine dose for a child weighing 20 kg?" | Dosage lookup | Dense + BM25 drug name match; NLL child retrieval |
| Q02 | "Is primaquine safe during pregnancy?" | Contraindication | Semantic + keyword match on contraindication text |
| Q03 | "Child with fast breathing and fever, what should a VHT do?" | Semantic | Pure dense (no exact medical terms) |
| Q04 | "artesunate-amodiaquine dosing schedule" | Exact drug name | BM25 critical for exact drug name variant |
| Q05 | "Malaria treatment for infant under 5 kg" | Weight-based | Weight range matching in clinical metadata |
| Q06 | "How to manage severe malaria with convulsions?" | Severe malaria | Clinical management table retrieval |
| Q07 | "Intermittent preventive treatment for pregnant women" | Prevention | IPTp guidance from prevention sections |
| Q08 | "When to use a rapid diagnostic test vs microscopy?" | Diagnosis | Diagnostic section retrieval |
| Q09 | "What to do if first-line ACT treatment fails?" | Treatment failure | Second-line treatment guidance |
| Q10 | "What is the evidence quality for dihydroartemisinin-piperaquine?" | Evidence | Evidence table retrieval |
| Q11 | "When should a community health worker refer a patient to a health facility?" | Referral | Danger signs, referral criteria |
| Q12 | "Malaria treatment for HIV-positive patients" | Special population | HIV co-infection guidance |

**Metrics per query:** precision@3, precision@5, MRR (mean reciprocal rank). Compare dense vs sparse vs hybrid. Compare PubMedBERT vs MiniLM.

---

## Configuration: `rag_config.json`

```json
{
  "embedding": {
    "primary_model": "pritamdeka/S-PubMedBert-MS-MARCO",
    "baseline_model": "sentence-transformers/all-MiniLM-L6-v2",
    "primary_dim": 768,
    "baseline_dim": 384,
    "batch_size": 32
  },
  "chunking": {
    "child_max_tokens": 512,
    "child_overlap_tokens": 50,
    "child_min_tokens": 50,
    "tables_keep_atomic": true,
    "create_nll_children": true,
    "token_multiplier": 1.3
  },
  "vector_db": {
    "chromadb_persist_dir": "rag_output/chroma_db",
    "faiss_index_path": "rag_output/faiss_index.bin",
    "collection_name": "who_malaria_guidelines",
    "faiss_hnsw_m": 32,
    "faiss_hnsw_ef_construction": 200,
    "faiss_hnsw_ef_search": 100
  },
  "retrieval": {
    "top_k": 5,
    "rrf_k": 60,
    "expand_context": true,
    "max_context_chunks": 3
  }
}
```

---

## Dependencies: `requirements.txt`

```
sentence-transformers>=2.2.0
chromadb>=0.4.0
faiss-cpu>=1.7.0
rank-bm25>=0.2.2
numpy>=1.24.0
```

Note: torch 2.2.2 and transformers 4.40.2 are already installed in the venv. Not pinning them avoids conflicts. Estimated additional disk: ~200 MB (packages) + ~2 GB (PubMedBERT model cache).

---

## Output Directory (added to .gitignore — regenerated, not committed)

```
rag_output/
├── chroma_db/                     # ChromaDB persistent storage (~20–50 MB)
├── faiss_index_pubmedbert.bin     # FAISS HNSW index (~15 MB)
├── faiss_index_minilm.bin         # FAISS HNSW index (~8 MB)
├── embeddings_pubmedbert.npy      # Raw vectors (1700×768, ~5 MB)
├── embeddings_minilm.npy          # Raw vectors (1700×384, ~3 MB)
├── child_chunks.json              # Parent-to-child mapping (~12 MB)
├── bm25_corpus.json               # BM25 tokenized corpus (~3 MB)
├── retrieval_test_results.json    # Test query results
└── build_report.json              # Build stats (timing, counts, sizes)
```

---

## Milestone Mapping

| Milestone | Deliverables | Validation Criteria |
|---|---|---|
| **M3.1: Tech Selected** | `requirements.txt`, `rag_config.json`, `step3_technology_rationale.md` | All imports succeed; config loads cleanly; rationale documented |
| **M3.2: Content Loaded** | `step3_rag_database.py` (build pipeline), working ChromaDB + FAISS + BM25 | ChromaDB has ~1,650–1,700 children; FAISS index <50 MB; all 1,443 non-image parents represented |
| **M3.3: Retrieval Validated** | Complete script + `step3_retrieval_test_results.md` + `step3_rag_summary.md` + `step3_setup_instructions.md` | 12 queries tested; precision@5 >0.6 for clinical queries; hybrid beats pure dense on drug-name queries |

---

## Implementation Sequence

| Step | Action | Output | Milestone |
|---|---|---|---|
| 1 | Create `requirements.txt` + install dependencies | Dependencies ready | |
| 2 | Create `rag_config.json` | Configuration ready | |
| 3 | Write `step3_technology_rationale.md` | Rationale documented | **M3.1** |
| 4 | Write `step3_rag_database.py` sections 1–8 (build pipeline) | Build pipeline ready | |
| 5 | Run build pipeline, verify ChromaDB + FAISS + BM25 | Database populated | **M3.2** |
| 6 | Write sections 9–12 (retrieval + test queries + main) | Full script complete | |
| 7 | Run full pipeline with 12 test queries | Test results generated | |
| 8 | Write `step3_retrieval_test_results.md` | Query results documented | |
| 9 | Write `step3_rag_summary.md` | 2-page summary | |
| 10 | Write `step3_setup_instructions.md` | Reproduction docs | |
| 11 | Update `.gitignore` + `extraction_pipeline_overview.md` | Integration documented | |
| 12 | Branch + commit + PR + merge | All on main | **M3.3** |

---

## Verification Checklist

1. `pip install -r requirements.txt` completes without errors
2. `python step3_rag_database.py` completes in <5 minutes
3. ChromaDB collection count ≈ 1,650–1,700 (all non-image parents represented)
4. FAISS index size <50 MB
5. `python step3_rag_database.py --test` — all 12 queries return results
6. Precision@5 >0.6 for clinical queries (Q01, Q02, Q04, Q06)
7. Hybrid outperforms pure dense on exact drug-name queries (Q01, Q04)
8. Verbatim chunks appear with preservation tags in results
9. Parent-child expansion works (child → parent with full metadata)
10. Context expansion follows related_chunks links (preceding/following narratives)
11. NLL children improve dosing table retrieval (compare Q01 with/without NLL)
12. `python step3_rag_database.py --query "artemether dose for 25 kg child"` returns relevant dosing table

---

## How This Connects to the Larger System

```
Extraction Pipeline (Stages 1–4b)     ←── COMPLETE
        │
        ▼
   chunks.json (1,478 chunks)
        │
        ▼
┌─────────────────────────────┐
│  Step 3: RAG Vector Database │  ←── THIS PLAN
│  (Brain 1: Knowledge Layer)  │
│                             │
│  ChromaDB (prototype)       │
│  FAISS (production export)  │
│  PubMedBERT embeddings      │
│  BM25 + RRF hybrid search   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Deployment Gate             │
│  verified_by + audit_hash    │
│  (Layer 1 Guardrail)        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Step 4: Brain 2             │
│  (Reasoning Layer — LLM)     │
│  + 7-Layer Guardrails        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  VHT Mobile Application      │
│  (Field deployment, Uganda)  │
└─────────────────────────────┘
```

**Repository:** [github.com/rajbagchi/safeai-purdue-capstone](https://github.com/rajbagchi/safeai-purdue-capstone)
