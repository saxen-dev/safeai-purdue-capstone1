# Benchmarking and Validation

This document covers the validation stages, dosing plausibility checks, clinical verification, and end-to-end benchmarking results for both target PDFs.

## Validation framework

**Module:** `pipeline/validator.py` (880 lines) | **Class:** `ExtractionValidator`

The validator runs six stages after extraction, each producing a confidence score (0.0 to 1.0) and a pass/fail determination. The overall confidence is the mean of all stage confidences.

### Stage 1: Structure validation

Checks heading hierarchy and page numbering. A single heading-level skip (e.g., H1 to H3, common in medical PDFs) costs 10% confidence. Passing threshold: 80%.

### Stage 2: Table quality

Verifies that extracted tables have at least 2 columns and that tables containing dosing keywords have sufficient numeric values. Confidence = fraction of valid tables.

### Stage 3: Cross-consistency

Compares Pass 1 (PyMuPDF) text with Pass 4 (pdfplumber) text using fuzzy string matching. Text is normalized before comparison (whitespace collapsed, soft hyphens removed, lowercased). Passing threshold: 90%.

### Stage 4: Medical content presence

Checks that critical medical terms from the config appear in the extracted text. Confidence = fraction of terms found. Passing threshold: 80%.

### Stage 5: Human review flagging

Identifies items requiring physician attention. Only flags dosing tables that failed Stage 6 checks (not every table mentioning "mg"). Includes contraindication pages and OCR-required pages. Capped at 50 items to keep the list actionable. Confidence is proportional to the number of flagged items.

### Stage 6: Dosing plausibility

The most critical stage. Runs six sub-checks on every dosing-classified table:

#### Check 1: Weight contiguity
No gaps >1 kg between consecutive weight bands. Only fires on tables with explicit weight-band structure (header contains "weight" and at least one row parses to a weight range).

#### Check 2: Dose monotonicity
Each dose component must be non-decreasing across ascending weight bands. Only fires on tables with weight-band structure.

#### Check 3: Weight coverage
Tables should cover from pediatric (<=10 kg) through adult (>=35 kg) ranges. Only fires on tables with weight-band structure.

#### Check 4: Clinical bounds
Per-kg doses are compared against reference ranges for known drugs (artemether 1-4 mg/kg, lumefantrine 6-16 mg/kg, etc.). A 2.5x tolerance factor accommodates clinical variation.

#### Check 5: Combination consistency
For fixed-ratio combination drugs (identified by "/" or "+" in column headers), the component ratio should be stable across all weight bands. Requires at least 3 multi-component rows and a combo-drug header hint.

#### Check 6: Positive/non-empty
All weight and dose cells should be non-empty and positive. Cells containing explicit "not applicable" markers (-, --, n/a, nil, etc.) are treated as intentional rather than missing.

### Agnostic design

All checks are document-agnostic. There are no hardcoded page numbers, drug lists, or table indices. The checks work on any clinical guideline PDF — the quality of results depends on the config's `drug_keywords` and `dosing_keywords` vocabulary.

## Clinical verification

**Module:** `pipeline/clinical_verifier.py` (1,227 lines) | **Class:** `ClinicalVerifier`

### Review package generation

The verifier generates a JSON review package and a Markdown physician review report containing:

- Every chunk classified into a 5-tier priority system (Tier 1 = validated dosing, Tier 5 = optional)
- Applicable clinical verification checks for each chunk
- SHA-256 audit hashes for integrity verification
- Pre-filled review items with decision fields (verified / needs-revision / rejected)

### Physician review workflow

1. Pipeline generates `review_package.json` and `physician_review_report.md`
2. Physician reviews each item and fills in decision + notes
3. Completed review is ingested via `ClinicalVerifier.ingest()`
4. System validates: audit hash integrity, reviewer identity, ISO timestamps, mandatory decisions
5. Verified status and digital signatures are applied to chunks
6. Deployment gate check determines production readiness

### Deployment gate

`passes_deployment_gate()` requires that all mandatory-tier chunks (Tiers 1-3) have `verified_by.status == "verified"` and a valid `audit_hash`. Any unverified mandatory chunk blocks deployment.

## Raw data

The benchmark data files are tracked in the repository under [`rag_output/`](../rag_output/):

- **[`retrieval_test_results.json`](../rag_output/retrieval_test_results.json)** — per-query results for all 12 clinical test queries (P@3, P@5, MRR, per-result relevance, source pages, content previews)
- **[`build_report.json`](../rag_output/build_report.json)** — corpus stats, timing, aggregate metrics, model configuration
- **[`brain1_package/`](../rag_output/brain1_package/)** — the deployable mobile package (24.11 MB)

See [`rag_output/README.md`](../rag_output/README.md) for the full directory guide.

## Benchmark results

### WHO Malaria Guidelines (478 pages, 203 tables)

| Stage | Score | Status |
|---|---|---|
| 1. Structure | 80% | PASS |
| 2. Tables | 100% | PASS |
| 3. Cross-consistency | 83% | FAIL (below 90% threshold) |
| 4. Medical content | 100% | PASS |
| 6. Dosing plausibility | 42% (8/19 tables) | FAIL |
| 5. Human review | 50 items flagged | — |
| **Overall confidence** | **~68%** | |

**Stage 3 analysis:** The 83% cross-consistency score reflects genuine text divergence on the malaria PDF's dense evidence tables (pages 314-476), where PyMuPDF and pdfplumber render complex multi-column layouts differently. The clinical content on these pages is still correctly extracted — the divergence is in formatting, not substance.

**Stage 6 analysis:** 11 of 19 dosing tables fail because the WHO malaria guidelines deliberately use non-contiguous weight bands for some drugs (e.g., separate tables for infants and adults) and include evidence comparison tables that are classified as "dosing" due to drug name mentions.

### Uganda Clinical Guidelines (1,161 pages, 950 tables)

| Stage | Score | Status |
|---|---|---|
| 1. Structure | 80% | PASS |
| 2. Tables | 100% | PASS |
| 3. Cross-consistency | 94% | PASS |
| 4. Medical content | 100% | PASS |
| 6. Dosing plausibility | 97% (495/509 tables) | PASS |
| 5. Human review | 43 items flagged | — |
| **Overall confidence** | **~79%** | |

The Uganda PDF performs significantly better because:
- Its table layouts are more uniform (consistent 2-3 column structures)
- Its 212 drug keywords provide richer classification vocabulary
- Its dosing tables use standard weight-band formats

### Response layer validation

Both presets were tested with 25 queries each (50 total):

| Metric | WHO Malaria | Uganda |
|---|---|---|
| Queries tested | 25 | 25 |
| Guardrail pass rate | 100% | 100% |
| Triage level consistency | All GREEN | All GREEN |
| Response confidence | 0.90 (all) | 0.90 (all) |
| VHT response length | 1,439-1,578 chars | 1,422-1,597 chars |

All 50 queries passed guardrail validation with no warnings or errors.

## Test suite

417 unit tests cover all pipeline modules:

| Test file | Tests | Coverage |
|---|---|---|
| `test_classify_table.py` | Table classification taxonomy | 244 lines |
| `test_clinical_metadata.py` | Metadata extraction | 366 lines |
| `test_clinical_verifier.py` | Review package, deployment gate | 609 lines |
| `test_config_presets.py` | Config factory functions | 324 lines |
| `test_dosing_plausibility.py` | All 6 dosing checks | 391 lines |
| `test_hybrid_retriever.py` | BM25 + dense + RRF | 257 lines |
| `test_image_ocr_enrichment.py` | Image OCR in chunker | 267 lines |
| `test_image_ocr_extractor.py` | Image extraction + OCR | 407 lines |
| `test_nll_generation.py` | Natural language table descriptions | 230 lines |
| `test_parent_child_chunking.py` | Parent-child splitting | 420 lines |
| `test_preservation_level.py` | Preservation level inference | 264 lines |
| `test_related_chunk_linking.py` | Related chunk linking | 312 lines |
| `test_stitch_tables.py` | Page-boundary table stitching | 313 lines |

Run the full suite:

```bash
python -m pytest tests/ -q
# 417 passed in ~25s
```

See also:
- [Safety and guardrails](safety_and_guardrails.md) for how these validation results enforce safety decisions
- [`rag_output/README.md`](../rag_output/README.md) for cross-referencing benchmark results against the source PDFs
