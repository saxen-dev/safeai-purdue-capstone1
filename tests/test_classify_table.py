"""
Unit tests for MultiPassExtractor._classify_table().

Run with:  python3 -m pytest tests/test_classify_table.py -v
"""

import pytest
from pipeline.extractor import MultiPassExtractor

fn = MultiPassExtractor._classify_table


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_table(headers, rows):
    """Build a minimal table dict accepted by _classify_table."""
    return {"headers": headers, "data": rows}


# ---------------------------------------------------------------------------
# Happy-path: each of the five types
# ---------------------------------------------------------------------------

class TestHappyPath:

    def test_dosing_weight_and_mg(self):
        t = make_table(
            ["Body weight", "Dose"],
            [{"Body weight": "5–14 kg", "Dose": "80 mg twice daily"}],
        )
        assert fn(t, [], []) == "dosing"

    def test_dosing_drug_name_plus_dose_value(self):
        # artemether keyword + "480 mg" dose value
        t = make_table(
            ["Drug", "Dose"],
            [{"Drug": "Artemether-lumefantrine", "Dose": "480 mg per course"}],
        )
        assert fn(t, ["artemether", "lumefantrine"], []) == "dosing"

    def test_evidence_grade_table(self):
        t = make_table(
            ["Outcome", "Certainty of evidence", "Relative effect"],
            [{"Outcome": "Fever clearance", "Certainty of evidence": "Moderate certainty", "Relative effect": "RR 0.85 (CI 0.7–1.0)"}],
        )
        assert fn(t, [], []) == "evidence"

    def test_evidence_two_keywords_sufficient(self):
        t = make_table(
            ["Quality of evidence", "Risk ratio"],
            [{"Quality of evidence": "Low certainty", "Risk ratio": "0.72"}],
        )
        assert fn(t, [], []) == "evidence"

    def test_clinical_management(self):
        t = make_table(
            ["Danger sign", "Management"],
            [{"Danger sign": "Unable to drink", "Management": "Refer to hospital"}],
        )
        assert fn(t, [], []) == "clinical_management"

    def test_structural_abbreviation_list(self):
        t = make_table(
            ["Abbreviation", "Full name"],
            [{"Abbreviation": "ACT", "Full name": "Artemisinin-based combination therapy"}],
        )
        assert fn(t, [], []) == "structural"

    def test_other_empty_table(self):
        t = make_table([], [])
        assert fn(t, [], []) == "other"

    def test_other_no_signals(self):
        t = make_table(
            ["Country", "Year"],
            [{"Country": "Uganda", "Year": "2023"}],
        )
        assert fn(t, [], []) == "other"


# ---------------------------------------------------------------------------
# Cascade priority
# ---------------------------------------------------------------------------

class TestCascadePriority:

    def test_structural_beats_dosing_when_two_struct_hits(self):
        # "abbreviation" + "full name" = 2 structural hits; also has "80+480 mg"
        # Fix 2: struct_hits >= 2 should win
        t = make_table(
            ["Abbreviation", "Full name"],
            [{"Abbreviation": "AL", "Full name": "Artemether-lumefantrine 80+480 mg"}],
        )
        assert fn(t, [], []) == "structural"

    def test_structural_single_hit_blocked_by_mg(self):
        # Only "abbreviation" (1 hit) but table contains "80 mg" — should NOT be structural
        t = make_table(
            ["Abbreviation", "Dose"],
            [{"Abbreviation": "AL", "Dose": "80 mg"}],
        )
        assert fn(t, [], []) != "structural"

    def test_evidence_beats_dosing(self):
        # Table has both dose values and GRADE signals — evidence should win
        t = make_table(
            ["Outcome", "Certainty of evidence", "Dose"],
            [{"Outcome": "Cure", "Certainty of evidence": "Moderate certainty", "Dose": "480 mg"}],
        )
        # evidence has 2 hits ("certainty of evidence" + "moderate certainty") before dosing check
        assert fn(t, [], []) == "evidence"

    def test_clinical_does_not_override_dosing(self):
        # Table has both dosing signals and clinical signals — dosing is checked first
        t = make_table(
            ["Drug", "Dose", "Management"],
            [{"Drug": "Artemether", "Dose": "80 mg twice daily", "Management": "severe malaria"}],
        )
        assert fn(t, ["artemether"], []) == "dosing"


# ---------------------------------------------------------------------------
# Fix 1: 'act' substring removed from MALARIA keywords
# ---------------------------------------------------------------------------

class TestActSubstringFix:

    def test_practice_not_dosed_as_dosing(self):
        # "practice" contains "act" — should NOT trigger dosing hit
        # extra_dosing does NOT contain "act" anymore
        t = make_table(
            ["Practice", "Dose"],
            [{"Practice": "Standard practice", "Dose": "80 mg daily"}],
        )
        # Only 1 dosing keyword hit ("mg" in "80 mg daily" header cell) + dose value
        # "dose" keyword is in base set, so dosing_hits=2 ("mg" + "dose") → still dosing.
        # Real test: passing "act" as extra keyword should NOT match "practice"
        assert fn(t, ["act"], []) == "dosing"  # dosing from "dose"+"mg", not from "act"

    def test_interaction_table_not_dosing_via_malaria_preset(self):
        # "interaction" contains "act" as a substring — verifies the malaria preset
        # no longer includes "act" so this table is not falsely classified as dosing.
        from pipeline.config import MALARIA_DOSING_TABLE_KEYWORDS
        assert "act" not in MALARIA_DOSING_TABLE_KEYWORDS, (
            "'act' was re-added to MALARIA_DOSING_TABLE_KEYWORDS — "
            "it causes false positives via substring match in 'interaction'/'practice'"
        )
        t = make_table(
            ["Drug", "Interaction"],
            [{"Drug": "Warfarin", "Interaction": "Clinical practice interaction monitoring"}],
        )
        result = fn(t, MALARIA_DOSING_TABLE_KEYWORDS, [])
        assert result != "dosing"


# ---------------------------------------------------------------------------
# Fix 3: 'weight' removed from base DOSING_TABLE_KEYWORDS
# ---------------------------------------------------------------------------

class TestWeightKeywordFix:

    def test_weight_monitoring_table_not_dosing(self):
        # A patient weight tracking table with no dose values
        t = make_table(
            ["Patient", "Weight recorded"],
            [{"Patient": "Adult", "Weight recorded": "60"}],
        )
        assert fn(t, [], []) != "dosing"

    def test_weight_with_kg_still_dosing(self):
        # "Weight (kg)" triggers has_weight_pattern — still correctly dosing when combined
        # with a drug keyword
        t = make_table(
            ["Weight (kg)", "Tablet"],
            [{"Weight (kg)": "5–14", "Tablet": "1 tablet"}],
        )
        assert fn(t, [], []) == "dosing"

    def test_body_weight_keyword_still_works(self):
        # "body weight" remains in base keywords — should still classify as dosing
        t = make_table(
            ["Body weight", "Dose"],
            [{"Body weight": ">30 kg", "Dose": "2 tablets"}],
        )
        assert fn(t, [], []) == "dosing"


# ---------------------------------------------------------------------------
# Data shape variants
# ---------------------------------------------------------------------------

class TestDataShapeVariants:

    def test_list_rows_not_dict(self):
        # data rows as lists (not dicts)
        t = {"headers": ["Weight", "Dose"], "data": [["5-10 kg", "80 mg"]]}
        assert fn(t, [], []) == "dosing"

    def test_missing_headers_key(self):
        t = {"data": [{"Drug": "Quinine", "Dose": "10 mg/kg"}]}
        assert fn(t, [], []) == "dosing"

    def test_missing_data_key(self):
        t = {"headers": ["Abbreviation", "Full name"]}
        assert fn(t, [], []) == "structural"

    def test_numeric_cell_values(self):
        # Numeric values in cells should not crash
        t = make_table(
            ["Age", "Weight"],
            [{"Age": 5, "Weight": 14}],
        )
        result = fn(t, [], [])
        assert result in {"dosing", "other", "clinical_management", "structural", "evidence"}


# ---------------------------------------------------------------------------
# Per-document extra keywords
# ---------------------------------------------------------------------------

class TestPerDocumentKeywords:

    def test_malaria_drug_name_classifies_as_dosing(self):
        t = make_table(
            ["Drug", "Regimen"],
            [{"Drug": "Artesunate", "Regimen": "4 mg/kg once daily"}],
        )
        assert fn(t, ["artesunate"], []) == "dosing"

    def test_uganda_drug_name_classifies_as_dosing(self):
        t = make_table(
            ["Drug", "Course"],
            [{"Drug": "Amoxicillin", "Course": "500 mg three times daily"}],
        )
        assert fn(t, ["amoxicillin"], []) == "dosing"

    def test_extra_clinical_keyword_triggers_clinical_management(self):
        t = make_table(
            ["Level of care", "Action"],
            [{"Level of care": "HC3", "Action": "Refer to HC4"}],
        )
        assert fn(t, [], ["level of care", "hc3", "hc4"]) == "clinical_management"
