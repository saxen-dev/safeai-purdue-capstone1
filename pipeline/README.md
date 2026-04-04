# Pipeline Developer Guide

This document is for developers who want to understand, extend, or debug the pipeline code.

For strategy/rationale docs, see the [`docs/`](../docs/) folder. For setup and usage, see [docs/setup_and_usage.md](../docs/setup_and_usage.md).

## Module map

The pipeline consists of 10 modules executed in sequence by the orchestrator:

```
cli.py               CLI entry point (argparse, preset selection)
  |
orchestrator.py      Pipeline coordinator (MedicalQASystem)
  |
  +-- config.py          Configuration dataclass + preset factories
  +-- extractor.py       Multi-pass PDF extraction (MultiPassExtractor)
  +-- validator.py       6-stage extraction validation (ExtractionValidator)
  +-- chunker.py         Semantic chunking + metadata (SmartChunker)
  +-- clinical_verifier.py  Physician review + deployment gate (ClinicalVerifier)
  +-- retriever.py       Hybrid BM25+dense+RRF retrieval (HybridRetriever)
  +-- guardrail.py       Medical safety validation (MedicalGuardrailBrain)
  +-- response.py        Structured response formatting (ResponseOrchestrator, VHTResponseFormatter)
```

### Execution flow

```python
# 1. CLI parses args, selects preset, creates ExtractionConfig
cfg = extraction_config_who_malaria_nih(pdf_path="...")

# 2. Orchestrator initializes and builds knowledge base
qa = MedicalQASystem(cfg.pdf_path, cfg.output_dir, cfg)
qa.initialize()
#    -> MultiPassExtractor.run()          # 6 passes
#    -> ExtractionValidator.validate_all() # 6 stages
#    -> SmartChunker.chunk_by_headings()   # parent chunks
#    -> SmartChunker.create_child_chunks() # child chunks
#    -> SmartChunker.create_search_index() # BM25 index
#    -> ClinicalVerifier.generate()        # review package
#    -> HybridRetriever(chunks)            # dense index
#    -> MedicalGuardrailBrain(chunks)      # guardrail init

# 3. Q&A loop
result = qa.answer(query)
#    -> HybridRetriever.retrieve(query)    # top-k chunks
#    -> MedicalGuardrailBrain.validate()   # safety check
#    -> ResponseOrchestrator.create()      # structured response
#    -> VHTResponseFormatter.format()      # output formatting
```

## Chunk schema

Every chunk is a dictionary with these fields:

```python
{
    # Core content
    "text": str,                    # Raw text content
    "page": int,                    # Source page number
    "heading": str,                 # Section heading

    # Classification
    "section_type": str,            # dosing | contraindication | diagnosis | treatment | background
    "preservation_level": str,      # VERBATIM | HIGH | STANDARD
    "content_type": str,            # narrative | table | image_ocr | image_placeholder
    "is_table_only": bool,          # True if chunk contains only table data

    # Tables
    "tables": [                     # Embedded tables (may be empty)
        {
            "classification": str,  # dosing | clinical_management | evidence | other
            "nll": str,             # Natural language description
            "headers": [str],
            "data": [dict],
            "markdown": str,
            "num_rows": int,
        }
    ],

    # Clinical metadata (17 fields)
    "clinical_metadata": {
        "condition": str | None,
        "drug_name": str | None,
        "dosage_summary": str | None,
        "patient_weight_min_kg": float | None,
        "patient_weight_max_kg": float | None,
        "patient_age_min": str | None,
        "patient_age_max": str | None,
        "route": str | None,
        "frequency": str | None,
        "duration": str | None,
        "contraindications": [str],
        "special_populations": [str],
        "level_of_care": str | None,
        "clinical_features": [str],
        "danger_signs": [str],
        "referral_criteria": [str],
        "clinical_section_type": str | None,
    },

    # Relationships
    "related_chunks": {
        "prev_sibling": int | None,
        "next_sibling": int | None,
        "preceding_narrative": int | None,
        "following_narrative": int | None,
        "context_for_tables": [int],
        "section_siblings": [int],
    },

    # Child chunk fields (only present on child chunks)
    "parent_chunk_id": int,         # Index of parent chunk
    "contextual_content": str,      # Content with metadata header prepended
    "child_strategy": str,          # proposition | recursive_paragraph | nll_child

    # Retrieval fields (added by retriever)
    "score": float,                 # Fused/reranked relevance score
    "retrieval_rank": int,          # 1-based rank in result set
}
```

## Adding a new preset

1. Create a JSON config in `configs/` (see [configs/README.md](../configs/README.md))
2. Add a factory function in `config.py`:

```python
def extraction_config_my_guideline(
    pdf_path: Optional[str] = None,
    output_dir: Optional[str] = None,
) -> ExtractionConfig:
    json_cfg = _load_json_config(_CONFIGS_DIR / "my_guideline.json")
    # ... merge keywords, set defaults
    return ExtractionConfig(...)
```

3. Register in `cli.py`:

```python
if args.preset == "my-guideline":
    cfg = extraction_config_my_guideline(pdf_path=args.pdf, output_dir=args.output_dir)
```

## Adding a new validation check

1. Add a static method to `ExtractionValidator` in `validator.py`
2. Call it from `_validate_dosing_plausibility()` or create a new stage in `validate_all()`
3. Add tests in `tests/test_dosing_plausibility.py`

## Key constants

| Constant | Location | Value | Purpose |
|---|---|---|---|
| `_CHILD_MAX_TOKENS` | chunker.py | 512 | Max child chunk size (STANDARD) |
| `_CHILD_OVERLAP_TOKENS` | chunker.py | 50 | Overlap between consecutive children |
| `_RRF_K_DEFAULT` | retriever.py | 60 | RRF fusion constant |
| `_DRUG_MATCH_BOOST` | retriever.py | 1.35 | Score multiplier for drug-name match |
| `_DOSING_TYPE_BOOST` | retriever.py | 1.25 | Score multiplier for dosing_table in dosing queries |
| `_NLL_BOOST` | retriever.py | 1.15 | Score multiplier for NLL children in dosing queries |
| `_EVIDENCE_TABLE_DEMOTE` | retriever.py | 0.85 | Score demote for evidence_table in dosing queries |
| `_CONDITION_MATCH_BOOST` | retriever.py | 1.20 | Score multiplier for condition metadata match |
| `_DOMAIN_MATCH_BOOST` | retriever.py | 1.10 | Score multiplier for clinical_domain match |
| `_RATIO_TOLERANCE` | validator.py | 0.35 | Max combo drug ratio deviation |
| `_COVERAGE_PEDIATRIC_LOW` | validator.py | 10.0 kg | Expected minimum weight coverage |
| `_COVERAGE_ADULT_HIGH` | validator.py | 35.0 kg | Expected minimum adult coverage |
| `_DOSE_BOUNDS_TOLERANCE` | validator.py | 2.5x | Clinical bounds tolerance factor |

## RAG output artifacts

The retrieval benchmark results and deployable mobile package are tracked in [`rag_output/`](../rag_output/). Key files: `retrieval_test_results.json` (12-query benchmark), `build_report.json` (corpus stats and metrics), `child_chunks.json` (1,695 chunks), and `brain1_package/` (24 MB mobile export). Binary indices (FAISS, numpy) are gitignored and regenerated by `retriever.py`. See [`rag_output/README.md`](../rag_output/README.md) for details.

## Testing

```bash
# All tests
python -m pytest tests/ -q

# Specific module
python -m pytest tests/test_dosing_plausibility.py -v

# With output
python -m pytest tests/ -v --tb=short
```

Tests use `unittest.mock` extensively to avoid requiring real PDFs, OCR engines, or embedding models.
