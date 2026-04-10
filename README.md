# SafeAI Medical Guidelines Pipeline

A production-grade pipeline for extracting, validating, chunking, and querying clinical guideline PDFs — built for Village Health Team (VHT) workers in low-resource settings.

Given a medical guideline PDF (WHO Malaria Guidelines, Uganda Clinical Guidelines 2023, or any clinical document), the pipeline:

1. **Extracts** text, tables, and images across 6 specialized passes
2. **Validates** extraction quality with 6 independent stages including dosing plausibility checks
3. **Chunks** content into semantically coherent units with 17-field clinical metadata
4. **Generates** a physician review package with SHA-256 audit hashes and a deployment gate
5. **Indexes** chunks for hybrid BM25 + dense retrieval with reciprocal rank fusion
6. **Answers** clinical questions with guardrail-validated, triage-aware structured responses

## Quick start

```bash
# Install
pip install -r requirements-pipeline.txt

# Optional: install Docling for transformer-based table extraction (recommended)
pip install 'docling>=2.64.0'

# Run with WHO Malaria preset
python run_pipeline.py --preset who-malaria --pdf /path/to/Bookshelf_NBK588130.pdf

# Run with Uganda Clinical Guidelines preset
python run_pipeline.py --preset uganda --pdf /path/to/Uganda_Clinical_Guidelines_2023.pdf

# Run with any clinical PDF (no preset)
python run_pipeline.py --pdf /path/to/any_guideline.pdf

# Query a processed knowledge base (verbatim retrieval, no LLM)
python query.py "What is the treatment for malaria in children?"
python query.py "ACT dosing by weight" --top-k 3 --kb ./medical_kb_who_malaria
```

After processing, the system drops into an interactive Q&A session in your terminal. `query.py` provides a separate verbatim query interface that returns exact source passages with no LLM synthesis. See [docs/setup_and_usage.md](docs/setup_and_usage.md) for full installation and usage instructions.

## Pipeline architecture

```
PDF Input
  |
  [Stage 1] Multi-pass extraction     pipeline/extractor.py
  |           Pass 0: Document profiling
  |           Pass 1: Text + headings (PyMuPDF)
  |           Pass 2: Table extraction + page-boundary stitching
  |           Pass 4: Cross-validation (pdfplumber)
  |           Pass images: OCR + caption extraction
  |
  [Stage 2] 6-stage validation         pipeline/validator.py
  |           Structure, tables, cross-consistency,
  |           medical content, dosing plausibility (6 checks),
  |           human review flagging
  |
  [Stage 3] Semantic chunking           pipeline/chunker.py
  |           Parent chunks (heading-based)
  |           -> Child chunks (preservation-level-aware splitting)
  |           -> Clinical metadata extraction (17 fields)
  |           -> Related chunk linking (3 passes)
  |
  [Stage 4] Clinical verification       pipeline/clinical_verifier.py
  |           5-tier triage, 5 verification checks,
  |           SHA-256 audit hashes, deployment gate
  |
  [Stage 5] Hybrid retrieval            pipeline/retriever.py
  |           BM25 + FAISS dense + RRF fusion
  |           + optional cross-encoder reranking
  |
  [Stage 6] Guardrail + Response        pipeline/guardrail.py
              Two-brain validation        pipeline/response.py
              Triage-aware VHT formatting
              4 output formats (VHT, Quick, Clinician, Referral)
```

## Folder layout

```
safeai-purdue-capstone/
|
|-- run_pipeline.py              Entry point (delegates to pipeline/cli.py)
|-- requirements-pipeline.txt    All Python dependencies (numpy<2 pinned)
|-- .gitignore                   Ignores PDFs, output dirs, venvs
|
|-- query.py                     Verbatim query CLI (no LLM, exact source text)
|-- pipeline/                    Core pipeline package (12 modules, ~7,000 lines)
|   |-- __init__.py              Lazy exports for all public classes
|   |-- __main__.py              Enables `python -m pipeline`
|   |-- cli.py                   CLI argument parsing, preset selection
|   |-- config.py                ExtractionConfig dataclass, preset factories
|   |-- extractor.py             Multi-pass PDF extraction engine
|   |-- docling_table_extractor.py  Optional Docling+TableFormer table extraction
|   |-- colpali_retriever.py     Optional ColPali v1.2 visual retrieval (MaxSim)
|   |-- validator.py             6-stage extraction validation
|   |-- chunker.py               Semantic chunking + clinical metadata
|   |-- clinical_verifier.py     Physician review package + deployment gate
|   |-- retriever.py             Hybrid BM25 + dense + RRF retrieval
|   |-- guardrail.py             Medical safety guardrail brain
|   |-- response.py              VHT response formatting + triage
|   +-- README.md                Developer guide (module map, chunk schema)
|
|-- configs/                     JSON config files for guideline presets
|   |-- malaria_who_2025.json    WHO Malaria (12 drug keywords)
|   |-- uganda_clinical_2023.json Uganda Clinical (212 drug keywords)
|   +-- README.md                Config file format + how to add a new guideline
|
|-- tests/                       444 unit tests
|   |-- test_classify_table.py       Table classification taxonomy
|   |-- test_clinical_metadata.py    Metadata extraction
|   |-- test_clinical_verifier.py    Review package + deployment gate
|   |-- test_config_presets.py       Config factory functions
|   |-- test_dosing_plausibility.py  6 dosing plausibility checks
|   |-- test_hybrid_retriever.py     BM25 + dense + RRF retrieval
|   |-- test_image_ocr_enrichment.py Image OCR in chunker
|   |-- test_image_ocr_extractor.py  Image extraction + OCR
|   |-- test_nll_generation.py       Natural language table descriptions
|   |-- test_parent_child_chunking.py Parent-child chunk splitting
|   |-- test_preservation_level.py   Preservation level inference
|   |-- test_related_chunk_linking.py Related chunk linking
|   +-- test_stitch_tables.py        Page-boundary table stitching
|
|-- docs/                        Strategy, rationale, and reference docs
|   |-- setup_and_usage.md       Full setup, CLI walkthrough, troubleshooting
|   |-- extraction_strategy.md   Multi-pass extraction + alternatives considered
|   |-- chunking_strategy.md     Hierarchical chunking + alternatives considered
|   |-- retrieval_strategy.md    Hybrid retrieval + alternatives considered
|   |-- response_layer.md        Two-brain response architecture + rationale
|   |-- safety_and_guardrails.md Safety measures across all pipeline stages
|   +-- benchmarking_and_validation.md  Validation stages, test results, metrics
|
|-- scripts/                     Report generation and index-building scripts
|   |-- build_colpali_index.py              Build ColPali visual retrieval index
|   |-- who_malaria_pipeline_report.py      Full pipeline report (25 queries)
|   +-- response_layer_validation_report.py Response layer validation (50 queries)
|
|-- reports/                     Generated benchmark reports
|   |-- who_malaria_pipeline_report.md
|   |-- uganda_clinical_pipeline_report.md
|   +-- response_layer_validation.md
|
+-- archive/                     Original standalone scripts (replaced by pipeline/)
    |-- README.md                What each file was and what replaced it
    +-- (12 archived files)
```

## Documentation

### Getting started
- **[Setup and usage guide](docs/setup_and_usage.md)** — Installation, running the pipeline, CLI walkthrough, troubleshooting

### Design strategy and rationale
- **[Extraction strategy](docs/extraction_strategy.md)** — Multi-pass extraction design, why PyMuPDF, Docling+TableFormer integration, alternatives considered
- **[Chunking strategy](docs/chunking_strategy.md)** — Hierarchical parent-child chunking, preservation levels, metadata extraction, alternatives rejected (fixed-size windows, LLM propositions)
- **[Retrieval strategy](docs/retrieval_strategy.md)** — Hybrid BM25 + dense + RRF + reranking, spelling normalization, heading weighting, alternatives rejected
- **[Response layer](docs/response_layer.md)** — Two-brain architecture, VHT formatting, triage inference, PDF-first content extraction with template fallback
- **[Safety and guardrails](docs/safety_and_guardrails.md)** — Defense-in-depth safety across all 6 stages

### Testing and benchmarks
- **[Benchmarking and validation](docs/benchmarking_and_validation.md)** — 6-stage validation, dosing plausibility, clinical verification, test results for both PDFs

### Developer reference
- **[Pipeline developer guide](pipeline/README.md)** — Module map, chunk schema, execution flow, how to extend
- **[Config file format](configs/README.md)** — JSON schema, how to add a new guideline
- **[Archive](archive/README.md)** — What the original standalone scripts were and what replaced them

## Benchmark results

Tested on two clinical guideline PDFs:

| Metric | WHO Malaria (478 pages) | Uganda Clinical (1,161 pages) |
|---|---|---|
| Tables extracted | 201 *(+Docling)* | 950 |
| Tables stitched across pages | 77 | 170 |
| Images extracted | 2 | 43 |
| Semantic chunks created | 5,538 *(+Docling)* | 3,753 |
| Child chunks for retrieval | 1,695 | 3,754 |
| Validation: Structure | PASS | 80% PASS |
| Validation: Tables | 100% PASS | 100% PASS |
| Validation: Cross-consistency | 83% | 94% PASS |
| Validation: Medical content | 100% PASS | 100% PASS |
| Validation: Dosing plausibility | 62.5% (10/16) *(+Docling)* | 99% PASS (479/484) |
| Retrieval P@3 (30 queries) | 0.489 | — |
| Retrieval MRR (30 queries) | 0.686 | — |
| Guardrail pass rate (25 queries) | 100% | 100% |
| Response confidence (mean, 25 queries) | *Re-run required (WHO Malaria KB not built)* | 0.89 (range: 0.68–1.00) |

*Docling + TableFormer ACCURATE was used for WHO Malaria extraction — requires `pip install 'docling>=2.64.0'`.*
*ColPali v1.2 visual retrieval is integrated but requires ≥16 GB RAM to run inference; index building tested on hardware with sufficient memory.*

## Running tests

```bash
python -m pytest tests/ -q
# 444 passed in ~55s
```

## Changelog

### 2026-04-09 — Response layer accuracy improvements (`pipeline/response.py`)

#### 1. Confidence score — was hardcoded, now computed from retrieval signals

**What changed:** `_calculate_confidence()` previously used a fixed baseline of `0.95` (RED triage) or `0.90` (all other queries), adjusted only for guardrail warnings. The benchmark table showed `0.90` as a result for both PDFs, but this was not a measured value — it was the hardcoded constant.

**Why it was wrong:** A query that retrieved weakly-matched chunks received exactly the same confidence score as a query backed by five highly-relevant guideline passages. The score carried no real information.

**What it does now:** Three real signals are combined:
- **Retrieval quality (60%)** — mean score of the top-3 retrieved chunks. Scores are normalized to [0, 1] by the hybrid retriever after RRF + cross-encoder blending.
- **Coverage (40%)** — fraction of the 5 requested chunks that were actually found.
- **Guardrail penalty (subtracted)** — −0.05 per warning, −0.15 per error, −0.10 if guardrail failed.

`confidence = 0.6 × retrieval_score + 0.4 × coverage − penalty`, clamped to [0.0, 1.0].

#### 2. Actions, monitoring, referral criteria — were hardcoded templates, now PDF-first

**What changed:** `_select_actions()`, `_select_monitoring()`, and `_select_referral_criteria()` previously returned hardcoded text lists selected by keyword-matching on the query string. There were only ~5 possible action sequences and ~2 monitoring/referral templates regardless of which guideline was loaded.

**Why it was wrong:** The response content did not reflect the actual loaded PDF. A document-specific instruction (e.g. "Complete 3-day ACT course even if fever resolves on day 1") would never appear in the output. The same fixed text was returned for any guideline document.

**What it does now:**
- **Actions** — `_extract_list_items_from_chunks()` scans retrieved chunk text for bullet-point and numbered-list items using regex. Items are taken verbatim from the PDF and deduplicated (up to 6 returned).
- **Monitoring** — `_collect_metadata_field(..., "danger_signs")` reads `danger_signs` extracted from chunk `clinical_metadata` by the chunker's `_DANGER_SIGN_RE` regex, formatted as "Watch for: …".
- **Referral criteria** — `_collect_metadata_field(..., "referral_criteria")` reads referral conditions extracted from chunk `clinical_metadata` by `_REFERRAL_RE`.

All three methods fall back to the hardcoded templates only when the PDF chunks contain no extractable list items or metadata. This preserves backward compatibility for edge cases while grounding responses in the actual source document by default.

## License

Purdue University Capstone Project — SafeAI Team.
