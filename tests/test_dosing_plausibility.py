"""
Unit tests for the 6 dosing plausibility checks and their supporting helpers.

Run with:  python3 -m pytest tests/test_dosing_plausibility.py -v
"""

import pytest
from pipeline.validator import (
    ExtractionValidator,
    _parse_weight_range,
    _parse_dose_values,
)

# Shorthand aliases for the static check methods
_parse   = ExtractionValidator._parse_dosing_table
_contiguous = ExtractionValidator._check_weight_contiguity
_monotone   = ExtractionValidator._check_dose_monotonicity
_coverage   = ExtractionValidator._check_weight_coverage
_bounds     = ExtractionValidator._check_clinical_bounds
_combo      = ExtractionValidator._check_combination_consistency
_positive   = ExtractionValidator._check_positive_no_empty


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_table(classification, headers, rows):
    data = [dict(zip(headers, r)) if isinstance(r, (list, tuple)) else r for r in rows]
    return {"classification": classification, "headers": headers, "data": data}


def make_validator(tables):
    from pipeline.config import ExtractionConfig
    cfg = ExtractionConfig.__new__(ExtractionConfig)
    cfg.output_dir = "/tmp/test_validator"
    cfg.confidence_threshold = 0.8
    cfg.critical_content_terms = []
    ext = ExtractionValidator.__new__(ExtractionValidator)
    ext.result = {"tables": tables, "pages": [], "ocr_data": [], "cross_validation": {}}
    ext.config = cfg
    ext.reports = []
    return ext


# ---------------------------------------------------------------------------
# _parse_weight_range
# ---------------------------------------------------------------------------

class TestParseWeightRange:

    def test_simple_range(self):
        assert _parse_weight_range("5-14 kg") == (5.0, 14.0)

    def test_en_dash_range(self):
        assert _parse_weight_range("5–14 kg") == (5.0, 14.0)

    def test_less_than_upper(self):
        lo, hi = _parse_weight_range("5–<15 kg")
        assert lo == 5.0 and hi == 15.0

    def test_open_ended_ge(self):
        lo, hi = _parse_weight_range("≥35 kg")
        assert lo == 35.0 and hi is None

    def test_open_ended_gt(self):
        lo, hi = _parse_weight_range(">35 kg")
        assert lo == 35.0 and hi is None

    def test_upper_only(self):
        lo, hi = _parse_weight_range("<5 kg")
        assert lo == 0.0 and hi == 5.0

    def test_empty_returns_none(self):
        assert _parse_weight_range("") is None

    def test_no_numbers_returns_none(self):
        assert _parse_weight_range("weight") is None


# ---------------------------------------------------------------------------
# _parse_dose_values
# ---------------------------------------------------------------------------

class TestParseDoseValues:

    def test_simple_mg(self):
        assert _parse_dose_values("80 mg") == [80.0]

    def test_combination_plus(self):
        assert _parse_dose_values("80 + 480 mg") == [80.0, 480.0]

    def test_empty_returns_empty(self):
        assert _parse_dose_values("") == []

    def test_tablet_without_mg_returns_empty(self):
        assert _parse_dose_values("1 tablet") == []

    def test_decimal_dose(self):
        vals = _parse_dose_values("2.5 mg")
        assert len(vals) == 1 and abs(vals[0] - 2.5) < 0.01


# ---------------------------------------------------------------------------
# Check 1: Weight contiguity
# ---------------------------------------------------------------------------

class TestWeightContiguity:

    def test_contiguous_bands_pass(self):
        t = make_table("dosing", ["Weight", "Dose"], [
            ["5-9 kg",  "80 mg"],
            ["10-14 kg", "160 mg"],
            ["15-24 kg", "240 mg"],
        ])
        parsed = _parse(t)
        result = _contiguous(parsed)
        assert result["passed"] is True

    def test_gap_between_bands_fails(self):
        t = make_table("dosing", ["Weight", "Dose"], [
            ["5-9 kg",   "80 mg"],
            ["13-24 kg", "160 mg"],  # gap: 9→13 = 4 kg (> 1.0 kg tolerance)
        ])
        parsed = _parse(t)
        result = _contiguous(parsed)
        assert result["passed"] is False
        assert any("Gap" in issue for issue in result["issues"])

    def test_open_ended_last_passes(self):
        t = make_table("dosing", ["Weight", "Dose"], [
            ["5-14 kg",  "80 mg"],
            ["≥15 kg", "160 mg"],
        ])
        parsed = _parse(t)
        result = _contiguous(parsed)
        assert result["passed"] is True

    def test_open_ended_not_last_fails(self):
        t = make_table("dosing", ["Weight", "Dose"], [
            ["≥5 kg", "80 mg"],
            ["15-24 kg", "160 mg"],
        ])
        parsed = _parse(t)
        result = _contiguous(parsed)
        assert result["passed"] is False

    def test_single_band_skipped(self):
        t = make_table("dosing", ["Weight", "Dose"], [["5-9 kg", "80 mg"]])
        parsed = _parse(t)
        result = _contiguous(parsed)
        assert result["passed"] is True
        assert any("skipped" in i for i in result["issues"])


# ---------------------------------------------------------------------------
# Check 2: Dose monotonicity
# ---------------------------------------------------------------------------

class TestDoseMonotonicity:

    def test_monotone_doses_pass(self):
        t = make_table("dosing", ["Weight", "Dose mg"], [
            ["5-9 kg",   "80 mg"],
            ["10-14 kg", "160 mg"],
            ["15-24 kg", "240 mg"],
        ])
        result = _monotone(_parse(t))
        assert result["passed"] is True

    def test_non_monotone_doses_fail(self):
        t = make_table("dosing", ["Weight", "Dose mg"], [
            ["5-9 kg",   "160 mg"],
            ["10-14 kg", "80 mg"],   # decreases
        ])
        result = _monotone(_parse(t))
        assert result["passed"] is False

    def test_combination_drug_both_components_checked(self):
        # Component 1 ok, component 2 decreases
        t = make_table("dosing", ["Weight", "Dose mg"], [
            ["5-9 kg",   "80 + 480 mg"],
            ["10-14 kg", "160 + 240 mg"],  # second component decreases
        ])
        result = _monotone(_parse(t))
        assert result["passed"] is False

    def test_no_dose_cols_skipped(self):
        t = {"classification": "dosing", "headers": ["Weight"], "data": [{"Weight": "5-9 kg"}]}
        parsed = _parse(t)
        result = _monotone(parsed)
        assert result["passed"] is True
        assert any("skipped" in i for i in result["issues"])


# ---------------------------------------------------------------------------
# Check 3: Weight coverage
# ---------------------------------------------------------------------------

class TestWeightCoverage:

    def test_full_pediatric_adult_coverage_passes(self):
        t = make_table("dosing", ["Weight", "Dose"], [
            ["5-9 kg",   "80 mg"],
            ["10-14 kg", "160 mg"],
            ["≥35 kg", "480 mg"],
        ])
        result = _coverage(_parse(t))
        assert result["passed"] is True

    def test_missing_infant_doses_fails(self):
        t = make_table("dosing", ["Weight", "Dose"], [
            ["15-24 kg", "240 mg"],
            ["≥35 kg",   "480 mg"],
        ])
        result = _coverage(_parse(t))
        assert result["passed"] is False
        assert any("infant" in i or "start" in i for i in result["issues"])

    def test_missing_adult_doses_fails(self):
        t = make_table("dosing", ["Weight", "Dose"], [
            ["5-9 kg",   "80 mg"],
            ["10-14 kg", "160 mg"],
        ])
        result = _coverage(_parse(t))
        assert result["passed"] is False
        assert any("adult" in i for i in result["issues"])

    def test_open_ended_high_enough_passes(self):
        t = make_table("dosing", ["Weight", "Dose"], [
            ["5-9 kg",  "80 mg"],
            ["≥35 kg", "480 mg"],
        ])
        result = _coverage(_parse(t))
        assert result["passed"] is True

    def test_no_weight_bands_skipped(self):
        t = make_table("dosing", ["Drug", "Dose"], [["Artemether", "80 mg"]])
        result = _coverage(_parse(t))
        assert result["passed"] is True
        assert any("skipped" in i for i in result["issues"])


# ---------------------------------------------------------------------------
# Check 4: Clinical dose bounds
# ---------------------------------------------------------------------------

class TestClinicalBounds:

    def test_valid_artemether_dose_passes(self):
        # artemether range: (1.0, 4.0) mg/kg; tolerance 2.5×
        # 5-9 kg mid = 7 kg; 20 mg / 7 kg = 2.86 mg/kg ✓
        t = make_table("dosing", ["Weight", "artemether mg"], [
            ["5-9 kg", "20 mg"],
        ])
        result = _bounds(_parse(t))
        assert result["passed"] is True

    def test_implausibly_high_dose_fails(self):
        # artemether: bound_hi = 4.0 * 2.5 = 10 mg/kg
        # 5-9 kg mid = 7 kg; 500 mg / 7 kg = 71 mg/kg — way too high
        t = make_table("dosing", ["Weight", "artemether mg"], [
            ["5-9 kg", "500 mg"],
        ])
        result = _bounds(_parse(t))
        assert result["passed"] is False

    def test_unknown_drug_skipped(self):
        t = make_table("dosing", ["Weight", "Dose mg"], [
            ["5-9 kg", "80 mg"],
        ])
        result = _bounds(_parse(t))
        assert result["passed"] is True  # no known drug in header → skipped


# ---------------------------------------------------------------------------
# Check 5: Combination consistency
# ---------------------------------------------------------------------------

class TestCombinationConsistency:

    def test_stable_ratio_passes(self):
        # AL ratio ~1:6 throughout
        t = make_table("dosing", ["Weight", "Dose mg"], [
            ["5-9 kg",   "20 + 120 mg"],
            ["10-14 kg", "40 + 240 mg"],
            ["15-24 kg", "60 + 360 mg"],
        ])
        result = _combo(_parse(t))
        assert result["passed"] is True

    def test_unstable_ratio_fails(self):
        # Header must contain a combo hint (e.g. '/') for the check to fire
        t = make_table("dosing", ["Weight", "Artemether/Lumefantrine mg"], [
            ["5-9 kg",   "20 + 120 mg"],   # ratio 6.0
            ["10-14 kg", "40 + 240 mg"],   # ratio 6.0
            ["15-24 kg", "60 + 60 mg"],    # ratio 1.0 — very different
        ])
        result = _combo(_parse(t))
        assert result["passed"] is False

    def test_single_component_skipped(self):
        t = make_table("dosing", ["Weight", "Dose mg"], [
            ["5-9 kg", "80 mg"],
            ["10-14 kg", "160 mg"],
        ])
        result = _combo(_parse(t))
        assert result["passed"] is True  # no multi-component rows


# ---------------------------------------------------------------------------
# Check 6: Positive values and no empty cells
# ---------------------------------------------------------------------------

class TestPositiveNoEmpty:

    def test_valid_table_passes(self):
        t = make_table("dosing", ["Weight", "Dose"], [
            ["5-9 kg", "80 mg"],
            ["10-14 kg", "160 mg"],
        ])
        result = _positive(_parse(t))
        assert result["passed"] is True

    def test_empty_weight_cell_fails(self):
        # Needs ≥2 weight-band rows so has_weight_bands=True and the check fires
        t = make_table("dosing", ["Weight", "Dose"], [
            ["5-9 kg", "80 mg"],
            ["", "160 mg"],          # second row has empty weight cell
        ])
        result = _positive(_parse(t))
        assert result["passed"] is False
        assert any("empty weight" in i for i in result["issues"])

    def test_empty_dose_cell_fails(self):
        # Needs ≥2 weight-band rows so has_weight_bands=True and the check fires
        t = make_table("dosing", ["Weight", "Dose"], [
            ["5-9 kg", "80 mg"],
            ["10-14 kg", ""],        # second row has truly empty dose cell
        ])
        result = _positive(_parse(t))
        assert result["passed"] is False
        assert any("empty dose" in i for i in result["issues"])


# ---------------------------------------------------------------------------
# _validate_dosing_plausibility integration
# ---------------------------------------------------------------------------

class TestValidateDosingPlausibility:

    def test_no_dosing_tables_skipped(self):
        v = make_validator([
            make_table("evidence", ["Outcome", "Effect"], [["Fever", "RR 0.85"]]),
        ])
        result = v._validate_dosing_plausibility()
        assert result.passed is True
        assert any("skipped" in i for i in result.issues)

    def test_clean_dosing_table_passes(self):
        t = make_table("dosing", ["Body weight", "Dose mg"], [
            ["5-9 kg",   "80 mg"],
            ["10-14 kg", "160 mg"],
            ["≥35 kg",   "480 mg"],
        ])
        v = make_validator([t])
        result = v._validate_dosing_plausibility()
        assert result.metadata["dosing_tables"] == 1

    def test_result_contains_per_table_checks(self):
        t = make_table("dosing", ["Body weight", "Dose mg"], [
            ["5-9 kg", "80 mg"],
        ])
        v = make_validator([t])
        result = v._validate_dosing_plausibility()
        table_result = result.metadata["table_results"][0]
        assert "weight_contiguity" in table_result["checks"]
        assert "dose_monotonicity" in table_result["checks"]
        assert "weight_coverage" in table_result["checks"]
        assert "clinical_bounds" in table_result["checks"]
        assert "combination_consistency" in table_result["checks"]
        assert "positive_no_empty" in table_result["checks"]

    def test_non_dosing_tables_excluded(self):
        tables = [
            make_table("dosing",   ["Body weight", "Dose"], [["5-9 kg", "80 mg"]]),
            make_table("evidence", ["Outcome", "Effect"],   [["Fever",  "RR 0.85"]]),
        ]
        v = make_validator(tables)
        result = v._validate_dosing_plausibility()
        assert result.metadata["dosing_tables"] == 1
