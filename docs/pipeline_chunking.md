# Stage 3 — Semantic Chunking

**Module:** `pipeline/chunker.py` · **Class:** `SmartChunker`

## Overview

Chunking converts the extraction output into discrete, retrievable units.
Each chunk maps to a heading-bounded section of the source document.
Standalone tables that do not belong to any text section get their own chunk.

After chunking, a BM25 search index is built over all chunks for retrieval.

## Chunk schema (13 fields)

| Field | Type | Description |
|-------|------|-------------|
| `chunk_id` | `str` | Unique identifier — `chunk_NNNNNN` (text) or `chunk_table_NNNNNN` (standalone table) |
| `page` | `int` | Source page number |
| `heading` | `str` | Section heading text (`"Untitled"` if none detected) |
| `level` | `int` | Heading level (1–3); standalone tables default to 3 |
| `text` | `str` | Full chunk text, including `# heading` prefix |
| `tables` | `list` | Table records from extraction that fall on this page |
| `has_tables` | `bool` | True if `tables` is non-empty |
| `char_count` | `int` | Character length of `text` |
| `word_count` | `int` | Word count of `text` |
| `is_table_only` | `bool` | True for standalone table chunks only |
| `section_type` | `str` | Inferred content type — see table below |
| `preservation_level` | `str` | How strictly text must be reproduced in VHT responses — see table below |
| `related_chunk_ids` | `list[str]` | Related chunks (e.g. parent↔child); empty until parent-child migration (Phase 2) |

### section_type values

Inferred from heading text via keyword matching:

| Value | Heading keywords |
|-------|-----------------|
| `dosing` | dose, dosing, dosage, mg, kg, regimen, schedule, tablet |
| `diagnosis` | diagnosis, diagnostic, symptom, sign, test, laboratory, criteria |
| `treatment` | treatment, management, therapy, protocol, intervention, prophylaxis |
| `contraindication` | contraindication, warning, caution, adverse, side effect, precaution |
| `table` | standalone table chunks (`is_table_only = True`) |
| `background` | none of the above |

### preservation_level values

Mapped from `pipeline.PreservationLevel` enum:

| Value | When | Meaning |
|-------|------|---------|
| `verbatim` | `section_type` is `dosing` or `table` | Dosing quantities must be copied exactly — no paraphrasing |
| `high` | `has_tables = True` or `section_type` is `treatment` or `contraindication` | Minor rephrasing allowed but all clinical values must be preserved |
| `standard` | All other sections | May be summarised for the VHT audience while retaining clinical accuracy |

## Chunking algorithm

1. **Group by headings**: For each page, interleave headings and text blocks by `y_pos`, split into sections at each heading boundary.
2. **Build chunk**: Combine heading + text blocks into a single string. Skip if `char_count < config.min_chunk_size` and no tables.
3. **Add table chunks**: Any table not already included in a text chunk (matched by page number) gets a standalone chunk when `num_rows > 1`.
4. **Infer metadata**: Assign `section_type` and `preservation_level` for every chunk.

## BM25 index

`create_search_index()` tokenizes each chunk's text (alphanumeric tokens, length > 1) and
builds a `BM25Okapi` index. Table data is also tokenized and appended to the chunk's token
list so table content is searchable.

```python
index = {
    "bm25":        BM25Okapi,   # rank-bm25 index object
    "chunks":      list[dict],  # all chunks
    "tokenized":   list[list],  # token lists for each chunk
}
```

## Configuration

| Field | Default | Effect |
|-------|---------|--------|
| `min_chunk_size` | `500` | Minimum characters for a text chunk (standalone table chunks are exempt) |
| `max_chunk_size` | `2000` | Not currently enforced — chunks are bounded by heading sections |
| `chunk_overlap` | `200` | Not currently used — reserved for sliding-window approach (Phase 2) |

## Usage

```python
from pipeline.chunker import SmartChunker

chunker = SmartChunker(extraction_result, config)
chunks = chunker.chunk_by_headings()
index = chunker.create_search_index()
```

## Architecture note — Phase 2

The current implementation is **heading-based**: one chunk per heading section.
The `related_chunk_ids` field and `chunk_overlap` config are placeholders for
the planned **parent-child migration**, where each section (parent) is split into
fine-grained child chunks for embedding, with the parent retained for response
context. See the architecture tracker for the Phase 2 design.
