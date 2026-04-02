# Stage 2 — Extraction Validation

**Module:** `pipeline/validator.py` · **Class:** `ExtractionValidator`

## Overview

Validation runs after extraction and before chunking.
It checks five things about the extracted content and writes a timestamped JSON
report to `{output_dir}/validation/`.

```
Stage 1  →  Structure integrity
Stage 2  →  Table quality
Stage 3  →  Cross-pass consistency
Stage 4  →  Medical content completeness
Stage 5  →  Human-review flagging
```

Each stage returns a `ValidationReport` dataclass
(`stage`, `passed`, `issues`, `confidence`, `suggestions`, `metadata`).
The overall confidence is the mean of stages 1–5.
Extraction is considered validated when `overall.confidence >= config.confidence_threshold` (default 0.8).

## Stage details

### Stage 1 — Structure (`_validate_structure`)

Checks that pages were extracted and that the heading hierarchy has no skipped levels.

| Check | Pass condition |
|-------|----------------|
| Pages extracted | At least 1 page |
| Page numbering | Sequential starting at 1 |
| Heading levels (first 10 pages) | No level skips (e.g. H1 → H3 without H2) |

Confidence: **0.9** (no issues) / **0.7** (any issue)

---

### Stage 2 — Tables (`_validate_tables`)

| Check | Pass condition |
|-------|----------------|
| Tables found | At least as many as `document_profile.estimated_tables` |
| Column count | Each table has ≥ 2 columns |
| Dosing tables | Tables with "dose" / "mg" in data have ≥ 3 numeric values |

Confidence: `valid_tables / total_tables`

---

### Stage 3 — Cross-consistency (`_validate_cross_consistency`)

Uses the `consistency_score` produced by Pass 4 (pdfplumber vs. PyMuPDF text similarity).

| Score | Outcome |
|-------|---------|
| ≥ 0.9 | Passes — text agreement is high |
| < 0.9 | Fails — flags pages for review |

Confidence: equals `consistency_score` directly.

---

### Stage 4 — Medical content (`_validate_medical_content`)

Checks that critical clinical terms appear in the extracted text.
The term list is source-specific:

| Source | Term list |
|--------|-----------|
| WHO Malaria | `MALARIA_GUIDELINE_CRITICAL_TERMS` (dose, artemisinin, pregnancy, …) |
| Uganda CG 2023 | `UGANDA_CLINICAL_CRITICAL_TERMS` (dose, diagnosis, referral, hospital, …) |
| Generic | `GENERAL_CLINICAL_CRITICAL_TERMS` (dose, treatment, patient, …) |

Fails if more than 30% of critical terms are absent.
Confidence: `1 - (missing_count / total_terms)`

---

### Stage 5 — Human-review flagging (`_flag_for_human_review`)

Does **not** affect the pass/fail decision. Flags three types of content for manual inspection:

| Flag type | Trigger |
|-----------|---------|
| `dosing_table` | Table data contains "dose", "mg", "tablet", or "administration" |
| `contraindication` | Page text contains "contraindication" or "not recommended" |
| `scanned_page` | OCR result has `status == "requires_manual_review"` |

Flagged items are written to `validation_report_*.json` under `metadata.items_for_review`.

## Output

```python
{
    "structure":     ValidationReport(...),
    "tables":        ValidationReport(...),
    "cross":         ValidationReport(...),
    "medical":       ValidationReport(...),
    "human_review":  ValidationReport(...),
    "overall": {
        "confidence":         float,   # mean of stages 1-5
        "passed":             bool,    # confidence >= config.confidence_threshold
        "needs_human_review": bool,    # any human-review flags raised
    }
}
```

## Usage

```python
from pipeline.validator import ExtractionValidator

validator = ExtractionValidator(extraction_result, config)
validation = validator.validate_all()
print(validation["overall"]["confidence"])
```
