# Guideline Configuration Files

Each JSON file in this folder defines the vocabulary, ground-truth references, and document metadata for a specific clinical guideline PDF. The pipeline's preset factory functions (`extraction_config_who_malaria_nih`, `extraction_config_uganda_clinical_2023` in `pipeline/config.py`) load these files and merge their keywords with built-in constants.

## Included configs

| File | Guideline | Drug keywords | Dosing keywords |
|---|---|---|---|
| `malaria_who_2025.json` | WHO Guidelines for Malaria (2025) | 12 | 9 |
| `uganda_clinical_2023.json` | Uganda Clinical Guidelines (MoH 2023) | 212 | 12 |

## JSON schema

```jsonc
{
  // Where raw extraction output is written (relative to project root)
  "output_dir": "extraction_output_malaria",

  // Document metadata
  "document": {
    "pdf_path": "B09514-eng.pdf",       // default filename (overridden by --pdf)
    "title": "WHO guidelines for malaria - 13 August 2025",
    "short_name": "WHO-Malaria-2025",
    "page_count": 478
  },

  // Optional processing hints
  "processing": {
    "benchmark_pages": [173, 212],       // pages used for quick extraction checks
    "page_range": null,                  // restrict extraction to a page range
    "max_pages_per_batch": null          // batch size for large documents
  },

  // Ground-truth assertions used by validation
  "ground_truth": [
    { "page": 173, "type": "text",
      "must_contain": ["weight-based dosage recommendations", "artemether"] }
  ],

  // Keywords for table classification and dosing detection
  "drug_keywords":    ["artemether", "lumefantrine", ...],
  "dosing_keywords":  ["body weight", "mg/kg", ...],

  // Per-drug reference dose ranges [mg/kg] for plausibility checks
  "dose_reference_ranges": {
    "artemether": [1.0, 4.0],
    "lumefantrine": [6.0, 16.0]
  },

  // Domain-specific terminology for metadata extraction
  "domain_keywords": {
    "conditions":                 ["malaria", "severe malaria", ...],
    "biomarkers":                 ["parasitaemia", "G6PD", ...],
    "contraindication_terms":     ["allergy", "first trimester", ...],
    "high_preservation_keywords": ["dosage", "contraindication", ...]
  },

  // Section-type detection keywords (Uganda-specific)
  "clinical_section_keywords": ["clinical_features", "management", ...],

  // Level-of-care keywords (e.g. "HC2", "HC3", "hospital")
  "loc_keywords": ["HC2", "HC3", "HC4", "hospital", ...],

  // Keywords that identify clinical management tables (vs. dosing/evidence)
  "clinical_table_keywords": ["manifestation", "differential", ...],

  // Pages used for targeted cross-validation
  "cross_validation": {
    "dosing_pages":               [173, 174, 175],
    "severe_pages":               [212, 213],
    "clinical_assessment_pages":  [256, 257]
  }
}
```

## Adding a new guideline

1. Copy an existing config and rename it (e.g. `ethiopia_std_treatment_2024.json`).
2. Fill in `document`, `drug_keywords`, `dosing_keywords`, and at least a few `ground_truth` entries.
3. Add a new preset factory function in `pipeline/config.py` following the pattern of the existing presets.
4. Register the new preset name in `pipeline/cli.py` so it can be used with `--preset`.

See [docs/setup_and_usage.md](../docs/setup_and_usage.md) for running the pipeline with a preset.
