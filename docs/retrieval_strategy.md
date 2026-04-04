# Retrieval Strategy

**Module:** `pipeline/retriever.py` (279 lines) | **Class:** `HybridRetriever`

## What we built

A **hybrid retrieval system** combining sparse keyword search (BM25), dense semantic search (FAISS + sentence-transformers), reciprocal rank fusion (RRF), and optional cross-encoder reranking.

```
User query
  |
  +---> BM25 (sparse)     ---> top-20 by keyword match
  |                              |
  +---> FAISS (dense)     ---> top-20 by embedding similarity
  |                              |
  +--- Reciprocal Rank Fusion ---+---> top-10 fused results
  |
  +---> Cross-encoder reranking ---> top-5 final results
```

### Why hybrid?

Neither sparse nor dense retrieval alone is sufficient for medical Q&A:

- **BM25** excels at exact drug name matches ("artemether-lumefantrine") but fails on semantic paraphrases ("anti-malarial combination therapy").
- **Dense retrieval** captures semantic similarity but can miss exact dosing values — a query for "5 mg/kg" may retrieve content about "weight-based dosing" that mentions different doses.

Combining both modalities with rank fusion consistently outperforms either alone in our testing.

### BM25 (sparse search)

The BM25Okapi index is built over tokenized chunk text. Tokenization strips non-alphanumeric characters, lowercases, and removes single-character tokens. The index searches over the `contextual_content` field of child chunks, which includes the metadata header.

### Dense search (FAISS)

Chunks are embedded using `sentence-transformers/all-MiniLM-L6-v2` (384-dimensional embeddings, ~90 MB model). The FAISS `IndexFlatIP` (inner product) index stores normalized embeddings for exact cosine similarity search. The text sent to the encoder is the `contextual_content` field — the child chunk's content with its metadata header prepended — so the embedding captures both context and content.

### Reciprocal Rank Fusion (RRF)

RRF merges the BM25 and dense ranked lists using:

```
RRF_score(doc) = sum( 1 / (k + rank_i(doc)) )  for each ranked list i
```

With `k=60` (standard), this gives balanced weight to both modalities. A document ranked #1 in both lists gets score `2/61 = 0.033`; a document ranked #1 in one and #20 in the other gets `1/61 + 1/80 = 0.029`. The gap is small, which is intentional — we want documents that appear in both lists to rank highest, not just documents that dominate one list.

### Cross-encoder reranking (optional)

The top-10 fused results are re-scored using `cross-encoder/ms-marco-MiniLM-L-6-v2`. Unlike bi-encoder similarity (where query and document are embedded independently), the cross-encoder processes the query-document pair jointly, enabling deeper semantic matching. This is expensive per-pair but only runs on 10 candidates.

Reranking is non-fatal: if the cross-encoder model fails to load (e.g., no internet on first run), the system falls back to RRF-only results with a warning.

### Graceful degradation

The retriever adapts to available dependencies:

| Available | Behavior |
|---|---|
| BM25 + FAISS + cross-encoder | Full hybrid + reranking |
| BM25 + FAISS | Hybrid with RRF, no reranking |
| BM25 only | Sparse keyword search only |

This means the pipeline works on machines without GPU or without `sentence-transformers` / `faiss-cpu` installed — it just falls back to BM25.

## Alternatives we considered

### Dense-only retrieval (rejected)

Using only embedding similarity (no BM25). We tested this and found it frequently missed exact drug name matches. A query for "primaquine dosing" would retrieve general "anti-malarial dosing" content instead of the specific primaquine table. BM25's exact keyword matching catches these cases reliably.

### BM25-only retrieval (rejected as default)

BM25 is fast and requires no model download, but it fails on semantic queries. "How should I treat a child who can't keep medicine down?" has no keyword overlap with "vomiting within 30 minutes of oral dose — repeat administration" — yet this is exactly the relevant content. Dense retrieval captures this semantic bridge.

### ChromaDB as the vector store (rejected)

ChromaDB provides a managed vector store with built-in embedding and persistence. We tested it but found that for our corpus size (3,800-4,000 chunks), FAISS `IndexFlatIP` is faster, uses less memory, and has no external process dependency. ChromaDB's advantages (persistence, filtering, multi-tenancy) don't apply to our single-document, in-memory use case.

### HNSW approximate search (rejected)

FAISS supports approximate nearest-neighbor search via HNSW or IVF indexes, which trade accuracy for speed. With only ~4,000 vectors, exact search (`IndexFlatIP`) completes in <1ms per query. There is no performance justification for approximate search at this scale.

### ColBERT / late-interaction models (rejected)

ColBERT stores per-token embeddings and computes fine-grained query-document interaction at search time. This provides better relevance than bi-encoder similarity but requires significantly more storage (384 dims x ~100 tokens per chunk vs. 384 dims x 1 embedding) and slower query time. For our corpus size and latency requirements, the bi-encoder + cross-encoder reranker achieves comparable quality at lower cost.

### Query expansion / HyDE (rejected)

Hypothetical Document Embeddings (HyDE) generates a synthetic answer to the query and uses its embedding for retrieval. This requires an LLM call per query, adding latency and cost. Our hybrid BM25 + dense approach already handles the vocabulary mismatch that HyDE addresses, without the LLM dependency.

## Parameters

| Parameter | Default | Purpose |
|---|---|---|
| `top_k_initial` | 20 | Candidates per modality before fusion |
| `top_k_fused` | 10 | Candidates after RRF before reranking |
| `rrf_k` | 60 | RRF fusion constant |
| `enable_reranking` | True | Enable cross-encoder reranking |

## Output

The retriever returns a list of chunk dictionaries enriched with `score` (fused/reranked relevance) and `retrieval_rank` (1-based position). These feed into the [response layer](response_layer.md) for answer generation.

## Benchmark data

The retrieval benchmark artifacts are tracked in [`rag_output/`](../rag_output/):

- **[`retrieval_test_results.json`](../rag_output/retrieval_test_results.json)** — 12-query clinical benchmark with per-result relevance, rankings, and source pages
- **[`build_report.json`](../rag_output/build_report.json)** — aggregate metrics (P@3 = 0.944, P@5 = 0.967, MRR = 0.944), corpus stats, and model configuration
- **[`child_chunks.json`](../rag_output/child_chunks.json)** — all 1,695 child chunks used for retrieval
- **[`brain1_package/`](../rag_output/brain1_package/)** — mobile-ready export (24.11 MB)

See [`rag_output/README.md`](../rag_output/README.md) for the full directory guide and how to cross-reference results against the source PDFs.

See also: [Chunking strategy](chunking_strategy.md) for how chunks are prepared for retrieval.
