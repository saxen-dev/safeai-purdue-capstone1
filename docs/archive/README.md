# Archive

These documents describe planned or aspirational pipeline designs that **do not match the current codebase**.
They are kept here for reference and will be rewritten to reflect actual implementations in a follow-up PR.

| File | Why archived |
|------|--------------|
| `extraction_pipeline_overview.md` | References non-existent scripts and wrong config approach |
| `stage1_primary_extraction_strategy.md` | Describes Docling-based extraction; actual code uses PyMuPDF + pdfplumber |
| `stage2_cross_validation_strategy.md` | Describes independent re-extraction stage; actual cross-validation is pass 4 inside extractor.py |
| `stage3_automated_checks_strategy.md` | Describes 6 dosing plausibility checks; actual validator.py has 5 different validation stages |
| `stage4a_chunking_strategy.md` | Describes 17-field parent-child chunking schema; actual chunker.py has 10-field heading-based schema |
| `stage4b_clinical_verification_strategy.md` | Describes physician review + SHA-256 audit; not yet implemented |

See `pipeline/README.md` for accurate documentation of what is currently built.
