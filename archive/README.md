# Archive

This folder contains the **original standalone scripts** that were developed during early prototyping. Every file here has been fully replaced by modules in the `pipeline/` package.

They are kept for reference only and are **not used** by the current pipeline.

| Archived file | Replaced by | Purpose |
|---|---|---|
| `extraction_mvp_v2.py` | `pipeline/extractor.py` | Multi-pass PDF extraction |
| `stage2_cross_validation.py` | `pipeline/extractor.py` (Pass 4) | PyMuPDF vs pdfplumber consistency |
| `stage3_automated_checks.py` | `pipeline/validator.py` | 6-stage validation |
| `stage4a_chunking.py` | `pipeline/chunker.py` | Semantic chunking + metadata |
| `stage4b_review_package.py` | `pipeline/clinical_verifier.py` | Physician review + deployment gate |
| `step3_rag_database.py` | `pipeline/retriever.py` | Hybrid BM25 + dense retrieval |
| `config_generator.py` | `pipeline/config.py` + `configs/*.json` | Preset configuration factory |
| `pipeline_config.py` | `pipeline/config.py` | Extraction config dataclass |
| `rag_config.json` | `configs/*.json` | RAG configuration |
| `requirements-rag.txt` | `requirements-pipeline.txt` | Deps (merged into pipeline reqs) |
| `step3_rag_implementation_plan.md` | `docs/retrieval_strategy.md` | RAG design plan |
| `step3_technology_rationale.md` | `docs/retrieval_strategy.md` | Technology selection rationale |
