"""
Complete production pipeline for medical guidelines (WHO Malaria, Uganda Clinical
Guidelines 2023, or any arbitrary PDF) with multi-pass extraction, validation,
chunking, dense retrieval, clinical verification, and two-brain Q&A.

Entry point: run from project root with:
  python run_pipeline.py --preset who-malaria --pdf /path/to/Bookshelf_NBK588130.pdf
  python run_pipeline.py --preset uganda --pdf /path/to/Uganda_Clinical_Guidelines_2023.pdf
  python run_pipeline.py --pdf /path/to/any_guideline.pdf
  python -m pipeline   # alternative
"""

import warnings
warnings.filterwarnings("ignore")

from pipeline.cli import main

if __name__ == "__main__":
    main()
