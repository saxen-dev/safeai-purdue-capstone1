# Stage 1 — Multi-Pass PDF Extraction

**Module:** `pipeline/extractor.py` · **Class:** `MultiPassExtractor`

## Overview

The extraction engine runs six passes over each source PDF.
The first five are numbered (0–4); a supplementary images pass runs last when
`ExtractionConfig.enable_image_extraction = True` (default).

```
Pass 0  →  Document analysis (structure profiling)
Pass 1  →  Text extraction with layout preservation
Pass 2  →  Specialized table extraction
Pass 3  →  OCR for scanned / image-heavy pages
Pass 4  →  Cross-validation (pdfplumber vs. Pass 1)
Images  →  Embedded image rasterization
```

## Pass details

| Pass | Method | What it does |
|------|--------|--------------|
| **0 – Analyze** | `analyze_document()` | Samples up to 20 pages with PyMuPDF; builds a document profile: page count, estimated heading count, estimated table count, scanned-page flags. Profile drives decisions in later passes. |
| **1 – Text** | `pass1_text_extraction()` | Extracts all text blocks and headings with `y_pos` coordinates for layout ordering. Builds per-page dicts with `headings`, `text_blocks`, `raw_text`. |
| **2 – Tables** | `pass2_table_extraction()` | Targets pages identified by Pass 0 (or all pages when `full_document_table_scan = True`). Uses PyMuPDF `find_tables()`; falls back to camelot for borderless tables. Each table record includes `headers`, `data`, `markdown`, `num_rows`, `num_cols`, `page`. |
| **3 – OCR** | `pass3_ocr_extraction()` | Runs only on pages flagged as scanned / image-heavy. Returns raw OCR text per page (placeholder — marks items `requires_manual_review` when a full OCR engine is not available). |
| **4 – Cross-validate** | `pass4_cross_validation()` | Re-extracts text with pdfplumber and computes `fuzz.ratio` similarity against Pass 1 output page-by-page. Aggregates a `consistency_score` (0–1) used by Stage 2 validation. |
| **Images** | `pass_images_extraction()` | Rasterizes embedded images to PNG under `{output_dir}/images/`; writes `image_inventory.json`. |

## Key configuration

| Field | Default | Effect |
|-------|---------|--------|
| `full_document_table_scan` | `True` | Scan every page for tables (not just the Pass-0 sample). Slower but catches tables after page ~20. |
| `enable_ocr` | `True` | Enable Pass 3. |
| `enable_image_extraction` | `True` | Enable the images pass. |
| `enable_table_detection` | `True` | Enable Pass 2. |
| `num_extraction_passes` | `5` | Informational: the 5 numbered passes (0–4). Does not gate execution. |
| `extraction_engine_version` | `2` | Bump to invalidate the pickle cache after engine changes. |

## Output structure

```python
{
    "metadata": {
        "config": { ... },
        "document_profile": { ... },
        "passes_completed": 6,
    },
    "pages": [ { "page": int, "headings": [...], "text_blocks": [...], "raw_text": str } ],
    "tables": [ { "page": int, "headers": [...], "data": [...], "markdown": str, ... } ],
    "ocr_data": [ ... ],
    "cross_validation": { "consistency_score": float, "page_matches": [...] },
    "extraction_log": [ { "pass": int|str, "strategy": str, ... } ],
    "images": [ { "page": int, "path": str, ... } ],   # written separately to image_inventory.json
}
```

## Caching

Extraction output is pickled to `{output_dir}/cache/` using a key derived from the
PDF path, file size, and `extraction_engine_version`. A cache hit skips all passes.

## Source documents

Use the factory presets for the two validated PDFs:

```python
from pipeline import extraction_config_who_malaria_nih, extraction_config_uganda_clinical_2023

cfg = extraction_config_who_malaria_nih(pdf_path="path/to/Bookshelf_NBK588130.pdf")
```

See `pipeline/config.py` for `ExtractionConfig` field definitions.
