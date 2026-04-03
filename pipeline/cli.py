"""CLI entry point for the medical pipeline."""

import argparse
import os
from pathlib import Path

from .config import (
    DEFAULT_UGANDA_CLINICAL_2023_PDF,
    DEFAULT_WHO_MALARIA_NIH_PDF,
    ExtractionConfig,
    extraction_config_uganda_clinical_2023,
    extraction_config_who_malaria_nih,
)
from .orchestrator import MedicalQASystem

_PRESET_ENV_HINTS = {
    "who-malaria": (
        "  Set MALARIA_PDF=/path/to/Bookshelf_NBK588130.pdf   (once, in your shell profile)\n"
        "  or pass: python run_pipeline.py --preset who-malaria --pdf /path/to/file.pdf"
    ),
    "uganda": (
        "  Set UGANDA_PDF=/path/to/Uganda_Clinical_Guidelines_2023.pdf   (once, in your shell profile)\n"
        "  or pass: python run_pipeline.py --preset uganda --pdf /path/to/file.pdf"
    ),
}


def main() -> None:
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Medical Q&A pipeline (WHO Malaria or Uganda Clinical Guidelines)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python run_pipeline.py --preset who-malaria --pdf /data/Bookshelf_NBK588130.pdf\n"
            "  python run_pipeline.py --preset uganda --pdf /data/Uganda_Clinical_Guidelines_2023.pdf\n"
            "  python run_pipeline.py --pdf /data/my_guideline.pdf --output-dir ./kb\n\n"
            "Env vars (avoids --pdf on every run):\n"
            "  MALARIA_PDF   — path to the WHO malaria guidelines PDF\n"
            "  UGANDA_PDF    — path to the Uganda Clinical Guidelines 2023 PDF\n"
        ),
    )
    parser.add_argument(
        "--preset",
        choices=("who-malaria", "uganda"),
        default=None,
        help="Use document-specific vocabularies for WHO Malaria or Uganda Clinical Guidelines",
    )
    parser.add_argument(
        "--pdf",
        default=None,
        help="Path to the PDF file (overrides default / env var; required when no preset is set)",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory for chunks, knowledge base, and review package",
    )
    args = parser.parse_args()

    # --- Build ExtractionConfig ---
    if args.preset == "who-malaria":
        cfg = extraction_config_who_malaria_nih(
            pdf_path=args.pdf or DEFAULT_WHO_MALARIA_NIH_PDF,
            output_dir=args.output_dir,
        )
    elif args.preset == "uganda":
        cfg = extraction_config_uganda_clinical_2023(
            pdf_path=args.pdf or DEFAULT_UGANDA_CLINICAL_2023_PDF,
            output_dir=args.output_dir,
        )
    elif args.pdf:
        # Custom PDF without a preset: use a generic config.
        # Pass --preset who-malaria or --preset uganda for document-tuned vocabularies.
        pdf = Path(args.pdf).expanduser()
        output_dir = args.output_dir or str(pdf.parent / "medical_knowledge_base")
        cfg = ExtractionConfig(
            pdf_path=str(pdf),
            output_dir=output_dir,
            document_title=pdf.stem.replace("_", " ").replace("-", " "),
        )
    else:
        # No args: default to WHO malaria preset using env var or legacy Windows path.
        cfg = extraction_config_who_malaria_nih(output_dir=args.output_dir)

    # --- Validate PDF exists ---
    if not os.path.exists(cfg.pdf_path):
        print(f"❌ PDF not found: {cfg.pdf_path}")
        if args.preset in _PRESET_ENV_HINTS:
            print(_PRESET_ENV_HINTS[args.preset])
        else:
            print("  Pass --pdf /path/to/your_guideline.pdf")
        return

    qa = MedicalQASystem(config=cfg)
    qa.initialize()

    print("\n" + "=" * 70)
    print("INTERACTIVE Q&A MODE")
    print("Type 'quit' to exit, 'status' for system status")
    print("=" * 70)

    while True:
        print("\n" + "-" * 50)
        query = input("Your question: ").strip()

        if query.lower() in ("quit", "exit", "q"):
            break
        if query.lower() == "status":
            print("\n📊 System Status:")
            print(f"  • Chunks: {len(qa.chunks)}")
            if qa.validation_result and "overall" in qa.validation_result:
                overall = qa.validation_result["overall"]
                print(f"  • Validation confidence: {overall.get('confidence', 0):.1%}")
                print(f"  • Needs human review: {overall.get('needs_human_review', False)}")
            continue
        if not query:
            continue

        result = qa.answer(query)

        print("\n" + "=" * 70)
        print(result["response"])
        print("=" * 70)

        if not result["validation_passed"]:
            print("\n⚠️  This response has safety warnings - verify before use")
