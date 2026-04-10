# Step 3: Technology Rationale — Brain 1 Knowledge Layer

**Safe AI Uganda — Purdue Capstone Project**
**Date:** 2026-03-14
**Pipeline Version:** step3 v1.0.0

---

## 1. Chunking Strategy: Adaptive Hierarchical with Contextual Retrieval

### Decision: 3-Layer Hybrid (Parent-Child + Adaptive + Contextual Headers)

**Why not re-chunk from scratch?** Stage 4a already produced 1,478 semantically meaningful chunks with 20 metadata fields, preservation levels, physician review templates, and inter-chunk navigation links. Re-chunking would destroy this rich metadata.

**Layer 1 — Hierarchical Parent-Child:** Parents (Stage 4a chunks) are the source of truth. Children (~1,695) are derived for embedding. Search returns children; display returns parents with full clinical metadata.

**Layer 2 — Adaptive by content type and safety level:**

| Content Type | Strategy | Rationale |
|---|---|---|
| Dosing tables (verbatim) | Atomic + NLL child | Tables cannot be split without dosing error risk |
| Clinical/evidence tables | Atomic | GRADE evidence and LOC routing must stay intact |
| Verbatim narratives (danger signs) | Proposition decomposition | Each clinical fact must be independently retrievable |
| High-preservation narratives | Smaller chunks (~300-400 tokens) | Dense clinical content needs precise retrieval |
| Standard narratives (>512 tokens) | Recursive paragraph splitting | Default approach with 50-token overlap |
| Standard narratives (<=512 tokens) | Passthrough (1 child = parent) | No splitting needed |
| Images (OCR) | Passthrough | OCR text is typically short |
| Structural tables | Skip | Table of contents not useful for retrieval |

**Layer 3 — Contextual headers:** Every child chunk gets a metadata header prepended before embedding:
```
[Context: {section_title} | {condition} | {drug_name} | Source: {doc} Section {num}, p.{pages}]
```
This is deterministically assembled from Stage 4a metadata (no LLM needed). Research shows up to 49% error reduction in retrieval failure rates with contextual enrichment.

### Strategies Evaluated and Rejected

| Strategy | Why Rejected |
|---|---|
| Fixed-size (512 tokens) | Would split dosing tables mid-row — patient safety risk |
| Semantic chunking | 3-5x compute cost for marginal benefit; WHO section hierarchy already provides semantic boundaries |
| Late chunking (jina-embeddings-v2) | Requires long-context model incompatible with PubMedBERT-SBERT |
| LLM-based/agentic chunking | Highest compute cost, experimental; our structured WHO content doesn't need autonomous decisions |
| Mix-of-granularity | Requires training a query router; incompatible with offline mobile deployment |
| Page-based chunking | Clinical concepts span pages; tables get split; page size varies wildly |

---

## 2. Embedding Model: PubMedBERT-SBERT

### Decision: `pritamdeka/S-PubMedBert-MS-MARCO` (768-dim)

**Why this model:**
- Medical domain pre-training (PubMed corpus) + MS-MARCO retrieval fine-tuning
- 78.1% exact match on clinical ICD-10 semantic search (Excoffier et al., 2024)
- 512-token context window aligns with our 400-512 token child chunks
- 768-dimensional embeddings — good balance of quality and index size
- Runs locally with no API dependency — critical for offline deployment
- ~420 MB model size, embeds 1,695 children in ~9 minutes on CPU

**Comparison baseline:** The plan recommends BGE-M3 instead of the original MiniLM baseline, for Phase 2 multilingual readiness evaluation.

### Models Evaluated

| Model | Clinical Match | Recommendation |
|---|---|---|
| PubMedBERT-SBERT | 78.1% | Primary (Phase 1) |
| BGE-M3 | SOTA multilingual | Comparison + Phase 2 candidate |
| jina-embeddings-v2 | 84.0% | Not recommended (late chunking incompatible with parent-child architecture) |
| E5-Instruct | 81.3% | Not recommended (no unique niche vs PubMedBERT + BGE-M3) |
| text-embedding-3-large | 54.9% MIRACL | Not recommended (requires API, incompatible with offline) |

---

## 3. Vector Database: ChromaDB + FAISS

### Decision: Dual-database architecture

**ChromaDB** (development): High-level API, built-in metadata filtering (`where={"preservation_level": "verbatim"}`), SQLite persistence. Used for prototyping and test queries.

**FAISS** (production): In-process C++ library, compilable for Android NDK. Flat index at 4.97 MB for 1,695 vectors — well under 50 MB target.

**Why not HNSW+PQ8?** At only 1,695 vectors, brute-force flat search provides exact results in <1ms on mobile CPU. HNSW+PQ8 is the production spec for when the corpus grows beyond ~10,000 vectors (multiple clinical guidelines). The code path is preserved but not needed at current scale.

### Databases Eliminated

| Database | Why Not |
|---|---|
| Pinecone | Cloud-only; no offline capability |
| Weaviate | Requires server process; too heavy for mobile |
| Milvus | Requires cluster; overengineered for ~1,700 vectors |
| Qdrant | Requires server process |

---

## 4. Retrieval: Hybrid Dense + BM25 + RRF + Cross-Encoder

### Decision: 3-Stage retrieval pipeline

**Stage 1 — Broad retrieval:**
- Dense: ChromaDB cosine similarity on PubMedBERT embeddings → top-20
- Sparse: BM25 keyword matching on contextual child text → top-20
- Fusion: Reciprocal Rank Fusion (k=60) → top-10

**Stage 2 — Re-ranking:**
- Cross-encoder: `cross-encoder/ms-marco-MiniLM-L-6-v2` (22M params)
- Re-ranks top-10 → top-5 based on (query, chunk) pair scoring

**Stage 3 — Context expansion:**
- Child → Parent mapping (full metadata recovery)
- Related chunks via `preceding_narrative`/`following_narrative` links
- Preservation tags added: `[VERBATIM]` or `[HIGH FIDELITY]`

### Why Hybrid (Not Pure Dense or Sparse)

| Query Type | Dense Wins | Sparse Wins |
|---|---|---|
| "fast breathing and fever" | Yes (semantic → tachypnea) | No |
| "artemether-lumefantrine dose" | No | Yes (exact drug name) |
| "80+480 mg for 25-35 kg" | No | Yes (exact numbers) |
| "when to refer severe malaria" | Yes (semantic referral) | Partial |

### Why RRF Over Other Fusion Methods
- Score-agnostic (no normalization between BM25 and cosine scales)
- Rank-based (only relative ordering matters)
- No training required
- k=60 is the established default

---

## 5. Performance Results

### Aggregate Metrics (12 Clinical Test Queries)

| Metric | Value |
|---|---|
| **Mean Precision@3** | **0.944** |
| **Mean Precision@5** | **0.967** |
| **Mean MRR** | **0.944** |
| Queries with perfect retrieval (P@3 = 1.0) | 11/12 |

### Brain 1 Package Size

| Component | Size |
|---|---|
| FAISS flat index | 4.97 MB |
| Child chunks JSON | 5.50 MB |
| Parent chunks JSON | 10.80 MB |
| BM25 inverted index | 2.85 MB |
| **Total package** | **24.11 MB** |
| 50 MB target | **PASS** |

### Build Timing (CPU, ~9.5 minutes total)

| Step | Time |
|---|---|
| Load chunks | 0.1s |
| Create children | 0.1s |
| PubMedBERT embedding | 551.2s |
| ChromaDB indexing | 5.1s |
| FAISS index | 0.1s |
| BM25 index | 0.5s |
| Load reranker | 2.9s |
| Test queries | 15.3s |
| Package export | 0.6s |

---

## 6. Sources

- Excoffier et al. (2024). "Generalist vs Specialist Clinical Embeddings." arXiv:2401.01943
- EHR Retrieval Comparison (2024). arXiv:2409.15163
- Anthropic (2024). "Contextual Retrieval." anthropic.com/news/contextual-retrieval
- BGE-M3 Paper (2024). arXiv:2402.03216
- FAISS Wiki. "Guidelines to Choose an Index." github.com/facebookresearch/faiss
