"""
Extraction validation: structure, tables, cross-consistency, medical content.
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

import numpy as np
from dataclasses import asdict

from .config import (
    ExtractionConfig,
    GENERAL_CLINICAL_CRITICAL_TERMS,
    ValidationReport,
)

# ---------------------------------------------------------------------------
# Dosing plausibility constants
# ---------------------------------------------------------------------------

# Weight-band population coverage thresholds (kg)
_COVERAGE_PEDIATRIC_LOW: float = 10.0   # table should start at or below this
_COVERAGE_ADULT_HIGH: float = 35.0      # table should reach at or above this

# Multiplicative tolerance for clinical dose bounds (2.5× either side)
_DOSE_BOUNDS_TOLERANCE: float = 2.5

# Maximum fractional deviation from median ratio in combination drugs (35%)
_RATIO_TOLERANCE: float = 0.35

# Cell values treated as "not applicable" rather than missing in dosing tables.
# Truly empty strings are NOT included — those are still flagged as missing.
_NA_CELL_VALUES: frozenset = frozenset({
    "-", "--", "---", "—", "–", "n/a", "na", "nil", "none",
    "not applicable", "not used", "n.a.", "n.a", ".", "/",
})

# Reference per-kg dose ranges for key guideline drugs [mg/kg, per single dose]
# Sources: WHO malaria guidelines; Uganda Clinical Guidelines 2023
_DRUG_DOSE_RANGES: Dict[str, Tuple[float, float]] = {
    # WHO malaria ACT components
    "artemether":       (1.0,  4.0),
    "lumefantrine":     (6.0, 16.0),
    "artesunate":       (2.0,  4.0),
    "amodiaquine":      (7.5, 15.0),
    "mefloquine":       (8.0, 25.0),
    "sulfadoxine":      (20.0, 30.0),
    "pyrimethamine":    (1.0,  2.0),
    "primaquine":       (0.25, 0.75),
    "dihydroartemisinin": (2.0, 4.0),
    "piperaquine":      (15.0, 27.0),
    "quinine":          (8.0, 15.0),
    "chloroquine":      (5.0, 10.0),
    # Uganda broad guideline common drugs
    "amoxicillin":      (12.5, 25.0),
    "cotrimoxazole":    (6.0, 12.0),
    "metronidazole":    (7.5, 15.0),
    "ciprofloxacin":    (10.0, 20.0),
    "paracetamol":      (10.0, 15.0),
}


# ---------------------------------------------------------------------------
# Module-level parsing helpers
# ---------------------------------------------------------------------------

def _parse_weight_range(cell: str) -> Optional[Tuple[float, Optional[float]]]:
    """Extract (lo_kg, hi_kg) from a weight cell string.

    hi_kg is None for open-ended bands (≥ / > patterns).
    Returns None if no weight values can be parsed.
    """
    cell = cell.strip()

    # Open-ended upper band: ">35 kg", "≥35", ">=35"
    m = re.search(r'[>≥]\s*=?\s*(\d+\.?\d*)', cell)
    if m:
        return (float(m.group(1)), None)

    # Range with explicit bounds: "5–14 kg", "5-<15 kg", "10 to 24 kg"
    m = re.search(r'(\d+\.?\d*)\s*[-–to<≤]+\s*<?(\d+\.?\d*)', cell)
    if m:
        return (float(m.group(1)), float(m.group(2)))

    # Upper-only: "<5 kg" → (0, 5)
    m = re.search(r'^[<≤]\s*(\d+\.?\d*)', cell)
    if m:
        return (0.0, float(m.group(1)))

    return None


def _parse_dose_values(cell: str) -> List[float]:
    """Extract numeric mg values from a dose cell.

    Returns [] for pure tablet-count cells without mg values.
    Handles combination patterns like "80 + 480 mg" → [80.0, 480.0].
    """
    if not cell.strip():
        return []

    # Pure tablet count with no mg value — skip (can't compute per-kg dose)
    if "tablet" in cell.lower() and "mg" not in cell.lower():
        return []

    # Combination pattern: numbers separated by +
    combo = re.findall(r'(\d+\.?\d*)\s*\+\s*(\d+\.?\d*)', cell)
    if combo:
        vals: List[float] = []
        for pair in combo:
            vals.extend(float(x) for x in pair)
        return vals

    # All standalone numbers — filter to plausible mg range
    numbers = re.findall(r'\d+\.?\d*', cell)
    result: List[float] = []
    for n in numbers:
        val = float(n)
        if 1.0 <= val <= 5000.0:
            result.append(val)
    return result


class ExtractionValidator:
    """
    Comprehensive validation of extracted content.
    Implements multi-stage validation from CDSS architecture.
    """

    def __init__(self, extraction_result: Dict, config: ExtractionConfig):
        self.result = extraction_result
        self.config = config
        self.reports: List[ValidationReport] = []

    def validate_all(self) -> Dict:
        """Run all validation stages."""
        print("\n🔍 Running comprehensive validation...")

        validation_results: Dict[str, Any] = {}

        validation_results["structure"] = self._validate_structure()
        print(
            f"  Stage 1 (Structure): {'✅' if validation_results['structure'].passed else '❌'} "
            f"conf={validation_results['structure'].confidence:.0%}"
        )

        validation_results["tables"] = self._validate_tables()
        print(
            f"  Stage 2 (Tables): {'✅' if validation_results['tables'].passed else '❌'} "
            f"conf={validation_results['tables'].confidence:.0%}"
        )

        validation_results["cross"] = self._validate_cross_consistency()
        print(
            f"  Stage 3 (Cross): {'✅' if validation_results['cross'].passed else '❌'} "
            f"conf={validation_results['cross'].confidence:.0%}"
        )

        validation_results["medical"] = self._validate_medical_content()
        print(
            f"  Stage 4 (Medical): {'✅' if validation_results['medical'].passed else '❌'} "
            f"conf={validation_results['medical'].confidence:.0%}"
        )

        validation_results["dosing_plausibility"] = self._validate_dosing_plausibility()
        print(
            f"  Stage 6 (Dosing Plausibility): "
            f"{'✅' if validation_results['dosing_plausibility'].passed else '❌'} "
            f"conf={validation_results['dosing_plausibility'].confidence:.0%}"
        )

        validation_results["human_review"] = self._flag_for_human_review(
            dosing_report=validation_results.get("dosing_plausibility")
        )
        print(
            f"  Stage 5 (Human Review): flagged {len(validation_results['human_review'].issues)} items"
        )

        confidences = [
            r.confidence
            for r in validation_results.values()
            if hasattr(r, "confidence")
        ]
        overall_confidence = float(np.mean(confidences)) if confidences else 0.0

        validation_results["overall"] = {
            "confidence": overall_confidence,
            "passed": overall_confidence >= self.config.confidence_threshold,
            "needs_human_review": len(validation_results["human_review"].issues) > 0,
        }

        report_file = os.path.join(
            self.config.output_dir,
            "validation",
            f"validation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        )
        os.makedirs(os.path.dirname(report_file), exist_ok=True)

        with open(report_file, "w") as f:
            json.dump(
                {
                    k: asdict(v) if hasattr(v, "__dataclass_fields__") else v
                    for k, v in validation_results.items()
                },
                f,
                indent=2,
                default=str,
            )

        return validation_results

    def _validate_structure(self) -> ValidationReport:
        """Validate document structure preservation."""
        issues: List[str] = []
        pages = self.result.get("pages", [])

        if not pages:
            issues.append("No pages extracted")
            return ValidationReport(
                stage="structure",
                passed=False,
                issues=issues,
                confidence=0.0,
                suggestions=["Check PDF accessibility"],
                metadata={},
            )

        page_numbers = [p["page"] for p in pages]
        expected_pages = list(range(1, len(page_numbers) + 1))
        if page_numbers != expected_pages:
            issues.append(
                f"Page numbering inconsistent: {page_numbers[:5]}..."
            )

        heading_levels = []
        for page in pages[:10]:
            for h in page.get("headings", []):
                heading_levels.append(h.get("level", 0))

        if heading_levels:
            for i in range(len(heading_levels) - 1):
                if heading_levels[i + 1] > heading_levels[i] + 1:
                    issues.append(
                        f"Heading level skipped: {heading_levels[i]} → {heading_levels[i+1]}"
                    )

        # Proportional: each issue costs 0.1, floor at 0.6 so a single
        # heading-level skip (common in medical PDFs) still passes at 0.8.
        confidence = max(0.6, 0.9 - 0.1 * len(issues))

        return ValidationReport(
            stage="structure",
            passed=confidence >= 0.8,
            issues=issues,
            confidence=confidence,
            suggestions=(
                ["Verify heading hierarchy manually"] if issues else []
            ),
            metadata={"pages_extracted": len(pages)},
        )

    def _validate_tables(self) -> ValidationReport:
        """Validate table extraction quality."""
        issues: List[str] = []
        tables = self.result.get("tables", [])

        if not tables:
            profile = self.result.get("metadata", {}).get("document_profile", {})
            if profile.get("estimated_tables", 0) > 0:
                issues.append(
                    f"Document estimated {profile['estimated_tables']} tables but none extracted"
                )
                confidence = 0.3
            else:
                confidence = 1.0
        else:
            valid_tables = 0
            for table in tables:
                if table.get("num_cols", 0) < 2:
                    issues.append(
                        f"Table on page {table['page']} has only {table.get('num_cols', 0)} columns"
                    )
                else:
                    valid_tables += 1

                data = str(table.get("data", ""))
                if "dose" in data.lower() or "mg" in data.lower():
                    numbers = re.findall(r"\d+\.?\d*", data)
                    if len(numbers) < 3:
                        issues.append(
                            f"Possible dosing table on page {table['page']} has few numeric values"
                        )

            confidence = valid_tables / len(tables) if tables else 0.0

        return ValidationReport(
            stage="tables",
            passed=confidence >= 0.8,
            issues=issues,
            confidence=confidence,
            suggestions=(
                ["Review tables with low confidence"] if confidence < 0.8 else []
            ),
            metadata={
                "tables_extracted": len(tables),
                "valid_tables": valid_tables if tables else 0,
            },
        )

    def _validate_cross_consistency(self) -> ValidationReport:
        """Validate consistency across extraction passes."""
        issues: List[str] = []
        cross_val = self.result.get("cross_validation", {})
        consistency = cross_val.get("consistency_score", 1.0)

        if consistency < 0.9:
            issues.append(
                f"Low cross-validation consistency: {consistency:.1%}"
            )

        return ValidationReport(
            stage="cross_consistency",
            passed=consistency >= 0.9,
            issues=issues,
            confidence=consistency,
            suggestions=(
                ["Review pages with low consistency scores"]
                if consistency < 0.9
                else []
            ),
            metadata={"consistency_score": consistency},
        )

    def _validate_medical_content(self) -> ValidationReport:
        """Validate presence of critical medical content."""
        issues: List[str] = []
        all_text = ""
        for page in self.result.get("pages", []):
            for block in page.get("text_blocks", []):
                all_text += block.get("text", "") + " "

        critical_terms = (
            self.config.critical_content_terms
            if self.config.critical_content_terms
            else GENERAL_CLINICAL_CRITICAL_TERMS
        )

        found_terms: List[str] = []
        missing_terms: List[str] = []

        for term in critical_terms:
            if term.lower() in all_text.lower():
                found_terms.append(term)
            else:
                missing_terms.append(term)

        if len(missing_terms) > len(critical_terms) * 0.3:
            issues.append(
                f"Many critical medical terms missing: {missing_terms[:5]}"
            )

        confidence = 1.0 - (len(missing_terms) / len(critical_terms))

        return ValidationReport(
            stage="medical_content",
            passed=confidence >= 0.8,
            issues=issues,
            confidence=confidence,
            suggestions=(
                ["Verify medical terminology extraction"]
                if confidence < 0.8
                else []
            ),
            metadata={
                "terms_found": found_terms,
                "terms_missing": missing_terms,
            },
        )

    # ------------------------------------------------------------------
    # Dosing plausibility — table parsing helper
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_dosing_table(table: Dict) -> Dict:
        """Parse a dosing table dict into structured weight bands and dose columns.

        Returns:
          {
            "headers": [str, ...],
            "weight_col": int | None,
            "dose_cols": [int, ...],
            "rows": [
              {"weight_cell": str, "weight_range": (lo, hi)|None,
               "dose_cells": [str, ...], "dose_values": [[float, ...], ...]},
              ...
            ]
          }
        """
        headers = [str(h).strip() for h in table.get("headers", [])]
        data = table.get("data", [])

        weight_col: Optional[int] = None
        dose_cols: List[int] = []

        for ci, h in enumerate(headers):
            h_lower = h.lower()
            if weight_col is None and any(
                kw in h_lower for kw in ["body weight", "weight"]
            ):
                weight_col = ci
            elif any(kw in h_lower for kw in ["dose", "mg", "tablet"] + list(_DRUG_DOSE_RANGES)):
                dose_cols.append(ci)

        # Track whether weight/dose cols were explicitly identified
        explicit_weight_col = weight_col
        using_fallback_cols = not dose_cols and bool(headers)

        # Fallback: treat first col as weight, rest as dose
        if not dose_cols and headers:
            weight_col = weight_col if weight_col is not None else 0
            dose_cols = [i for i in range(len(headers)) if i != weight_col]

        rows: List[Dict] = []
        for row in data:
            if isinstance(row, dict):
                cells = [str(row.get(h, "")).strip() for h in headers]
            else:
                cells = [str(v).strip() for v in row]

            weight_cell = (
                cells[weight_col]
                if weight_col is not None and weight_col < len(cells)
                else ""
            )
            weight_range = _parse_weight_range(weight_cell) if weight_cell else None

            dose_cells: List[str] = []
            dose_values: List[List[float]] = []
            for dc in dose_cols:
                if dc < len(cells):
                    dose_cells.append(cells[dc])
                    dose_values.append(_parse_dose_values(cells[dc]))
                else:
                    dose_cells.append("")
                    dose_values.append([])

            rows.append({
                "weight_cell": weight_cell,
                "weight_range": weight_range,
                "dose_cells": dose_cells,
                "dose_values": dose_values,
            })

        weight_band_count = sum(1 for r in rows if r["weight_range"] is not None)
        # ≥1 parsed weight range is enough to confirm the table has weight-band
        # structure; the individual checks that need ≥2 bands guard themselves.
        has_weight_bands = explicit_weight_col is not None and weight_band_count >= 1

        return {
            "headers": headers,
            "weight_col": weight_col,
            "dose_cols": dose_cols,
            "rows": rows,
            "has_weight_bands": has_weight_bands,
            "using_fallback_cols": using_fallback_cols,
        }

    # ------------------------------------------------------------------
    # Dosing plausibility — six checks
    # ------------------------------------------------------------------

    @staticmethod
    def _check_weight_contiguity(parsed: Dict) -> Dict:
        """Check 1: No gaps between consecutive weight bands."""
        issues: List[str] = []

        if not parsed.get("has_weight_bands"):
            return {"passed": True, "issues": ["no weight-band structure — skipped"]}

        weight_ranges = [r["weight_range"] for r in parsed["rows"] if r["weight_range"]]

        if len(weight_ranges) < 2:
            return {"passed": True, "issues": ["<2 weight bands — skipped"]}

        for i in range(len(weight_ranges) - 1):
            lo_cur, hi_cur = weight_ranges[i]
            lo_next, _ = weight_ranges[i + 1]

            if hi_cur is None:
                issues.append(
                    f"Open-ended band (≥{lo_cur} kg) is not the last row"
                )
                continue

            if lo_next is not None and abs(hi_cur - lo_next) > 1.0:
                issues.append(
                    f"Gap between band {i+1} ({hi_cur} kg) and band {i+2} "
                    f"({lo_next} kg) — {abs(hi_cur - lo_next):.1f} kg"
                )

        return {"passed": len(issues) == 0, "issues": issues}

    @staticmethod
    def _check_dose_monotonicity(parsed: Dict) -> Dict:
        """Check 2: Each dose component must be non-decreasing across weight bands."""
        issues: List[str] = []

        if not parsed.get("has_weight_bands"):
            return {"passed": True, "issues": ["no weight-band structure — skipped"]}

        if not parsed["dose_cols"]:
            return {"passed": True, "issues": ["No dose columns found — skipped"]}

        for dc_idx in range(len(parsed["dose_cols"])):
            header = (
                parsed["headers"][parsed["dose_cols"][dc_idx]]
                if dc_idx < len(parsed["dose_cols"]) and parsed["dose_cols"][dc_idx] < len(parsed["headers"])
                else f"Col {dc_idx}"
            )
            col_vals = [
                row["dose_values"][dc_idx]
                if dc_idx < len(row["dose_values"]) else []
                for row in parsed["rows"]
            ]
            max_comp = max((len(v) for v in col_vals), default=0)

            for comp_idx in range(max_comp):
                prev: Optional[float] = None
                for r_i, vals in enumerate(col_vals):
                    if comp_idx < len(vals):
                        curr = vals[comp_idx]
                        if prev is not None and curr < prev:
                            comp_label = f" component {comp_idx+1}" if max_comp > 1 else ""
                            issues.append(
                                f"{header}{comp_label}: row {r_i+1} = {curr} < "
                                f"row {r_i} = {prev} (not monotonic)"
                            )
                        prev = curr

        return {"passed": len(issues) == 0, "issues": issues}

    @staticmethod
    def _check_weight_coverage(parsed: Dict) -> Dict:
        """Check 3: Table covers from pediatric through adult weight bands."""
        issues: List[str] = []

        if not parsed.get("has_weight_bands"):
            return {"passed": True, "issues": ["no weight-band structure — skipped"],
                    "range_low": None, "range_high": None}

        weight_ranges = [r["weight_range"] for r in parsed["rows"] if r["weight_range"]]

        if not weight_ranges:
            return {
                "passed": True,
                "issues": ["No weight bands found — skipped"],
                "range_low": None,
                "range_high": None,
            }

        range_low = weight_ranges[0][0]
        range_high = weight_ranges[-1][1]
        last_open_low = weight_ranges[-1][0]

        if range_low > _COVERAGE_PEDIATRIC_LOW:
            issues.append(
                f"Table starts at {range_low} kg — may be missing infant doses "
                f"(expected ≤ {_COVERAGE_PEDIATRIC_LOW} kg)"
            )

        if range_high is not None and range_high < _COVERAGE_ADULT_HIGH:
            issues.append(
                f"Table ends at {range_high} kg — may be missing adult doses "
                f"(expected ≥ {_COVERAGE_ADULT_HIGH} kg or open-ended)"
            )
        elif range_high is None and last_open_low < _COVERAGE_ADULT_HIGH * 0.5:
            issues.append(
                f"Open-ended band starts at {last_open_low} kg — "
                f"unusually low for adult dosing"
            )

        return {
            "passed": len(issues) == 0,
            "issues": issues,
            "range_low": range_low,
            "range_high": range_high,
        }

    @staticmethod
    def _check_clinical_bounds(parsed: Dict) -> Dict:
        """Check 4: Per-kg dose falls within plausible clinical reference ranges."""
        issues: List[str] = []

        for dc_idx, dc in enumerate(parsed["dose_cols"]):
            header = parsed["headers"][dc] if dc < len(parsed["headers"]) else ""
            h_lower = header.lower()
            drugs = [drug for drug in _DRUG_DOSE_RANGES if drug in h_lower]

            if not drugs:
                continue

            for r_i, row in enumerate(parsed["rows"]):
                wr = row["weight_range"]
                if wr is None:
                    continue

                lo, hi = wr
                mid_weight = lo + 20.0 if hi is None else (lo + hi) / 2.0
                if mid_weight <= 0:
                    continue

                dose_vals = row["dose_values"][dc_idx] if dc_idx < len(row["dose_values"]) else []

                for drug, dose_val in zip(drugs, dose_vals):
                    if dose_val <= 0:
                        continue
                    per_kg = dose_val / mid_weight
                    ref_lo, ref_hi = _DRUG_DOSE_RANGES[drug]
                    bound_lo = ref_lo / _DOSE_BOUNDS_TOLERANCE
                    bound_hi = ref_hi * _DOSE_BOUNDS_TOLERANCE
                    if per_kg < bound_lo or per_kg > bound_hi:
                        issues.append(
                            f"Row {r_i+1} ({row['weight_cell']}): {drug} "
                            f"{dose_val} mg / {mid_weight:.0f} kg = {per_kg:.2f} mg/kg — "
                            f"outside [{bound_lo:.2f}–{bound_hi:.1f}] mg/kg"
                        )

        return {"passed": len(issues) == 0, "issues": issues}

    @staticmethod
    def _check_combination_consistency(parsed: Dict) -> Dict:
        """Check 5: Component ratios in combination drugs are stable across rows.

        Only fires when the column header explicitly suggests a fixed-ratio
        combination drug (e.g. contains '/', '+', or 'co-').  Generic dose
        columns with multiple numeric values (e.g. two unrelated drugs listed
        in one row) are skipped to avoid false positives.
        """
        issues: List[str] = []

        # Keywords that indicate a genuine fixed-ratio combination product
        _COMBO_HINTS = ("/", "+", " co-", "coartem", "co-artemether",
                        "combined", "combination", "compound")

        for dc_idx in range(len(parsed["dose_cols"])):
            col_i = parsed["dose_cols"][dc_idx]
            header = (
                parsed["headers"][col_i].lower()
                if col_i < len(parsed["headers"]) else ""
            )

            # Skip columns whose header doesn't look like a combo product
            if not any(hint in header for hint in _COMBO_HINTS):
                continue

            multi_rows = [
                (r_i, row["dose_values"][dc_idx])
                for r_i, row in enumerate(parsed["rows"])
                if dc_idx < len(row["dose_values"]) and len(row["dose_values"][dc_idx]) >= 2
            ]

            # Need at least 3 multi-component rows to establish a reliable ratio
            if len(multi_rows) < 3:
                continue

            ratios = [vals[1] / vals[0] for _, vals in multi_rows if vals[0] > 0]
            if not ratios:
                continue

            median_ratio = sorted(ratios)[len(ratios) // 2]
            if median_ratio <= 0:
                continue

            for (r_i, _), ratio in zip(multi_rows, ratios):
                deviation = abs(ratio - median_ratio) / median_ratio
                if deviation > _RATIO_TOLERANCE:
                    row = parsed["rows"][r_i]
                    issues.append(
                        f"Row {r_i+1} ({row.get('weight_cell', '?')}): ratio = "
                        f"{ratio:.2f} vs median {median_ratio:.2f} "
                        f"(deviation {deviation*100:.0f}% > {_RATIO_TOLERANCE*100:.0f}%)"
                    )

        return {"passed": len(issues) == 0, "issues": issues}

    @staticmethod
    def _check_positive_no_empty(parsed: Dict) -> Dict:
        """Check 6: All weight and dose cells are non-empty; all dose values > 0."""
        issues: List[str] = []

        # Skip empty-cell check when columns were inferred via fallback — the
        # first column may not be a weight column at all (e.g. drug name lists).
        if parsed.get("using_fallback_cols") and not parsed.get("has_weight_bands"):
            return {"passed": True, "issues": ["no explicit dose columns — skipped"]}

        for r_i, row in enumerate(parsed["rows"]):
            weight_norm = row["weight_cell"].strip().lower()
            if weight_norm in _NA_CELL_VALUES:
                continue  # intentionally blank / not-applicable weight row

            if not weight_norm and parsed.get("has_weight_bands"):
                issues.append(f"Row {r_i+1}: empty weight cell")

            for dc_idx, dose_cell in enumerate(row["dose_cells"]):
                cell_norm = dose_cell.strip().lower()
                if cell_norm in _NA_CELL_VALUES:
                    continue  # intentionally blank / not-applicable cell
                if not cell_norm:
                    issues.append(f"Row {r_i+1}, dose col {dc_idx+1}: empty dose cell")
                    continue
                for comp_idx, val in enumerate(
                    row["dose_values"][dc_idx] if dc_idx < len(row["dose_values"]) else []
                ):
                    if val <= 0:
                        issues.append(
                            f"Row {r_i+1}, dose col {dc_idx+1}, "
                            f"component {comp_idx+1}: non-positive value {val}"
                        )

        return {"passed": len(issues) == 0, "issues": issues}

    # ------------------------------------------------------------------
    # Dosing plausibility — orchestrator
    # ------------------------------------------------------------------

    def _validate_dosing_plausibility(self) -> ValidationReport:
        """Stage 6: Run all six plausibility checks on every dosing-classified table."""
        dosing_tables = [
            t for t in self.result.get("tables", [])
            if t.get("classification") == "dosing"
        ]

        if not dosing_tables:
            return ValidationReport(
                stage="dosing_plausibility",
                passed=True,
                issues=["No dosing-classified tables found — skipped"],
                confidence=1.0,
                suggestions=[],
                metadata={"dosing_tables": 0},
            )

        all_issues: List[str] = []
        table_results: List[Dict] = []
        passed_count = 0

        for i, table in enumerate(dosing_tables):
            pages = table.get("pages", [table.get("page", "?")])
            parsed = self._parse_dosing_table(table)

            checks = {
                "weight_contiguity":       self._check_weight_contiguity(parsed),
                "dose_monotonicity":       self._check_dose_monotonicity(parsed),
                "weight_coverage":         self._check_weight_coverage(parsed),
                "clinical_bounds":         self._check_clinical_bounds(parsed),
                "combination_consistency": self._check_combination_consistency(parsed),
                "positive_no_empty":       self._check_positive_no_empty(parsed),
            }

            table_passed = all(c["passed"] for c in checks.values())
            if table_passed:
                passed_count += 1

            table_issues = [
                f"[table {i+1} p{pages} / {name}] {issue}"
                for name, check in checks.items()
                for issue in check["issues"]
                if issue and "skipped" not in issue
            ]
            all_issues.extend(table_issues)

            table_results.append({
                "table_index": i + 1,
                "pages": pages,
                "classification": table.get("classification"),
                "num_rows": table.get("num_rows", 0),
                "overall_passed": table_passed,
                "checks": checks,
            })

        confidence = passed_count / len(dosing_tables)

        print(
            f"  Stage 6 (Dosing Plausibility): "
            f"{passed_count}/{len(dosing_tables)} tables passed"
        )

        return ValidationReport(
            stage="dosing_plausibility",
            passed=confidence >= 0.8,
            issues=all_issues,
            confidence=confidence,
            suggestions=(
                ["Review flagged dosing tables before deployment"]
                if all_issues else []
            ),
            metadata={
                "dosing_tables": len(dosing_tables),
                "passed": passed_count,
                "table_results": table_results,
            },
        )

    def _flag_for_human_review(
        self,
        dosing_report: Optional[Any] = None,
    ) -> ValidationReport:
        """Flag sections needing human verification.

        Only dosing tables that *failed* Stage 6 checks are flagged as needing
        dosing review — not every table that mentions "mg".  Contraindication
        pages and OCR pages are always included.  Total items are capped at 50
        to keep the list actionable.
        """
        _MAX_ITEMS = 50
        priority_items: List[Dict[str, Any]] = []

        # Build a set of page numbers for dosing tables that failed Stage 6
        failed_dosing_pages: set = set()
        if dosing_report is not None:
            for tr in dosing_report.metadata.get("table_results", []):
                if not tr.get("overall_passed"):
                    for pg in (tr.get("pages") or [tr.get("page")]):
                        if pg is not None:
                            failed_dosing_pages.add(pg)

        # If no Stage 6 data available, fall back to all dosing-classified tables
        if dosing_report is None:
            for table in self.result.get("tables", []):
                if table.get("classification") == "dosing":
                    priority_items.append({
                        "type": "dosing_table",
                        "page": table.get("page"),
                        "reason": "Dosing accuracy critical - requires human verification",
                    })
        else:
            for page_num in sorted(failed_dosing_pages):
                priority_items.append({
                    "type": "dosing_table",
                    "page": page_num,
                    "reason": "Dosing accuracy critical - requires human verification",
                })

        # Always include contraindication pages
        for page in self.result.get("pages", []):
            for block in page.get("text_blocks", []):
                text = block.get("text", "").lower()
                if "contraindication" in text or "not recommended" in text:
                    priority_items.append({
                        "type": "contraindication",
                        "page": page.get("page"),
                        "reason": "Safety-critical information - verify accuracy",
                    })
                    break

        # Always include OCR pages
        for ocr_item in self.result.get("ocr_data", []):
            if ocr_item.get("status") == "requires_manual_review":
                priority_items.append({
                    "type": "scanned_page",
                    "page": ocr_item.get("page"),
                    "reason": "OCR required - manual transcription needed",
                })

        # Cap to keep the list actionable
        priority_items = priority_items[:_MAX_ITEMS]

        hr_conf = max(0.0, min(1.0, 1.0 - (len(priority_items) * 0.02)))
        return ValidationReport(
            stage="human_review",
            passed=len(priority_items) == 0,
            issues=[item["reason"] for item in priority_items],
            confidence=hr_conf,
            suggestions=["Prioritize flagged items for manual review"],
            metadata={"items_for_review": priority_items},
        )
