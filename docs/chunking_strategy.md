# Chunking Strategy

**Module:** `pipeline/chunker.py` (923 lines) | **Class:** `SmartChunker`

## What we built

A **hierarchical parent-child chunking system** with clinical metadata extraction, preservation-level-aware splitting, and multi-pass related-chunk linking.

```
Extracted content
  -> Parent chunks (semantic, heading-based)
     -> Clinical metadata extraction (17 fields)
     -> Section type + preservation level inference
     -> Child chunks (sized for dense embedding retrieval)
        -> Contextual headers prepended
     -> Related chunk linking (3 passes)
```

### Parent chunking

Content is grouped into parent chunks by document headings. Each heading starts a new chunk that includes all text blocks and tables until the next heading of equal or higher level. This respects the document's own organizational structure rather than imposing arbitrary token windows.

Standalone tables that don't fall under any narrative section get their own dedicated chunks so dosing tables are never merged into unrelated narrative.

### Section type detection

Each chunk is classified by its heading text using keyword matching:

| Section type | Keywords | Example heading |
|---|---|---|
| `dosing` | dose, dosing, dosage, regimen, mg, kg | "Dosing recommendations" |
| `contraindication` | contraindication, warning, adverse, precaution | "Contraindications and warnings" |
| `diagnosis` | diagnosis, symptom, sign, test, laboratory | "Diagnostic criteria" |
| `treatment` | treatment, management, therapy, protocol | "Management of severe malaria" |
| `background` | (default) | "Introduction" |

### Preservation level

Section type and table presence determine how strictly content must be preserved during retrieval and response generation:

| Level | When assigned | Constraint |
|---|---|---|
| `VERBATIM` | Dosing tables, table-only chunks | Exact text — no paraphrasing allowed |
| `HIGH` | Contraindications, treatment with tables | High-fidelity paraphrasing only |
| `STANDARD` | Background, diagnosis, general narrative | Standard paraphrasing acceptable |

### Clinical metadata extraction

Every chunk gets a 17-field clinical metadata dictionary extracted from its content:

- **Drug identification:** name, dosage summary, route, frequency, duration
- **Patient population:** weight range (min/max kg), age range (min/max)
- **Clinical context:** condition, contraindications, special populations
- **Care setting:** level of care (HC2, HC3, hospital), danger signs, referral criteria, clinical features, clinical section type

Metadata is extracted using regex patterns and keyword matching against the chunk's text, table headers, and natural language table descriptions (NLL).

### Child chunking

Parent chunks are split into smaller child chunks sized for dense embedding retrieval. The splitting strategy is preservation-level-aware:

| Preservation | Max tokens | Strategy |
|---|---|---|
| `VERBATIM` | 200 | Proposition decomposition (sentence-level) |
| `HIGH` | 400 | Recursive paragraph splitting with overlap |
| `STANDARD` | 512 | Recursive paragraph splitting with overlap |

Each child chunk gets a **contextual header** prepended:

```
[Context: Dosing recommendations | Malaria | Artemether-lumefantrine |
Source: WHO Guidelines for Malaria, Page 173]
```

This header ensures the dense embedding captures both the metadata context and the raw content in a single vector, improving retrieval relevance.

Dosing tables additionally generate an **NLL child** — a natural language description of the table that enables semantic search to find tables even when the query uses different wording than the table headers.

### Related chunk linking

After all chunks are built, three linking passes connect them:

1. **Sequential siblings:** Each chunk gets `prev_sibling` and `next_sibling` pointers
2. **Table-narrative proximity:** Tables are linked to the nearest preceding and following narrative chunks, and vice versa via `context_for_tables`
3. **Section siblings:** Chunks under the same heading are linked as `section_siblings`

These links enable the retriever and response layer to pull in surrounding context when a single chunk isn't sufficient.

## Alternatives we considered

### Fixed-size token windows (rejected)

The simplest chunking approach: split text into 512-token windows with 50-token overlap. We rejected this because:
- It splits dosing tables mid-row, making the top half meaningless without the bottom
- It ignores document structure, merging the end of one section with the start of the next
- There is no natural boundary for metadata extraction

### Single-level chunking (rejected)

Using only parent chunks (heading-based) without child splitting. This produces chunks that are too large for dense embedding (some sections are 2,000+ tokens). Dense retrieval quality degrades sharply above ~512 tokens because the embedding must compress too much content into a single vector. The parent-child hierarchy gives us semantic boundaries (parents) AND embedding-friendly sizes (children).

### LLM-based proposition decomposition for all content (rejected)

Academic research (e.g., "Dense X Retrieval" by Chen et al.) suggests decomposing all text into atomic propositions. We adopted this only for `VERBATIM` content (dosing tables) where every sentence is safety-critical. For `STANDARD` content, recursive paragraph splitting is cheaper and produces comparable retrieval quality. Running an LLM over 3,800+ chunks would add significant cost and latency.

### Overlapping sliding windows with no structure awareness (rejected)

Sliding windows with overlap ensure no content falls in a gap, but they produce many redundant chunks and don't respect section boundaries. Our heading-based parents avoid redundancy, and the 50-token overlap in child splitting handles boundary content.

### No metadata extraction (rejected)

Some RAG systems rely entirely on the embedding model to understand content. We found that explicit metadata extraction (drug names, weight ranges, conditions) dramatically improves both retrieval precision and response quality. When a user asks "What is the dose of artemether for children under 5 kg?", the metadata enables exact matching on drug name and weight range before the embedding similarity even runs.

## Output

The chunker produces a list of chunk dictionaries, each containing: `text`, `page`, `heading`, `section_type`, `preservation_level`, `clinical_metadata`, `tables`, `related_chunks`, and (for child chunks) `contextual_content` and `parent_chunk_id`.

See also: [Retrieval strategy](retrieval_strategy.md) for how chunks are indexed and searched.
