"""
Unit tests for SmartChunker._extract_clinical_metadata() and helpers.

Run with:  python3 -m pytest tests/test_clinical_metadata.py -v
"""

import pytest
from pipeline.chunker import (
    SmartChunker,
    _parse_weight_range_from_cell,
    _normalize_loc,
)

fn = SmartChunker._extract_clinical_metadata
empty = SmartChunker._empty_clinical_metadata


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_chunk(text="", heading="Untitled", section_type="background", tables=None):
    return {
        "text": text,
        "heading": heading,
        "section_type": section_type,
        "tables": tables or [],
    }


def make_dosing_table(headers, rows, nll=""):
    data = [dict(zip(headers, r)) if isinstance(r, (list, tuple)) else r for r in rows]
    return {
        "classification": "dosing",
        "headers": headers,
        "data": data,
        "markdown": "",
        "nll": nll,
    }


# ---------------------------------------------------------------------------
# _parse_weight_range_from_cell
# ---------------------------------------------------------------------------

class TestParseWeightRangeFromCell:

    def test_range(self):
        assert _parse_weight_range_from_cell("5–14 kg") == (5.0, 14.0)

    def test_open_ended(self):
        lo, hi = _parse_weight_range_from_cell("≥35 kg")
        assert lo == 35.0 and hi is None

    def test_upper_only(self):
        lo, hi = _parse_weight_range_from_cell("<5 kg")
        assert lo == 0.0 and hi == 5.0

    def test_empty(self):
        assert _parse_weight_range_from_cell("") is None


# ---------------------------------------------------------------------------
# _normalize_loc
# ---------------------------------------------------------------------------

class TestNormalizeLoc:

    def test_roman_three(self):
        assert _normalize_loc("HC III") == "HC3"

    def test_roman_four(self):
        assert _normalize_loc("HC IV") == "HC4"

    def test_already_numeric(self):
        assert _normalize_loc("HC3") == "HC3"

    def test_roman_two(self):
        assert _normalize_loc("HC II") == "HC2"


# ---------------------------------------------------------------------------
# Empty metadata structure
# ---------------------------------------------------------------------------

class TestEmptyMetadata:

    def test_all_17_fields_present(self):
        m = empty()
        expected = {
            "condition", "drug_name", "dosage_summary",
            "patient_weight_min_kg", "patient_weight_max_kg",
            "patient_age_min", "patient_age_max",
            "route", "frequency", "duration",
            "contraindications", "special_populations",
            "level_of_care", "clinical_features",
            "danger_signs", "referral_criteria",
            "clinical_section_type",
        }
        assert set(m.keys()) == expected

    def test_list_fields_are_empty_lists(self):
        m = empty()
        for field in ["contraindications", "special_populations", "level_of_care",
                      "clinical_features", "danger_signs", "referral_criteria"]:
            assert m[field] == []

    def test_scalar_fields_are_none(self):
        m = empty()
        for field in ["condition", "drug_name", "dosage_summary",
                      "patient_weight_min_kg", "patient_weight_max_kg",
                      "route", "frequency", "duration", "clinical_section_type"]:
            assert m[field] is None


# ---------------------------------------------------------------------------
# condition and clinical_section_type
# ---------------------------------------------------------------------------

class TestConditionAndSectionType:

    def test_condition_from_heading(self):
        chunk = make_chunk(heading="Malaria Treatment Guidelines", section_type="treatment")
        m = fn(chunk)
        assert m["condition"] == "Malaria Treatment Guidelines"

    def test_heading_with_markdown_prefix_stripped(self):
        chunk = make_chunk(heading="## Dosing Schedule")
        m = fn(chunk)
        assert m["condition"] == "Dosing Schedule"

    def test_untitled_heading_not_set_as_condition(self):
        chunk = make_chunk(heading="Untitled")
        m = fn(chunk)
        assert m["condition"] is None

    def test_clinical_section_type_from_section_type(self):
        chunk = make_chunk(section_type="dosing")
        m = fn(chunk)
        assert m["clinical_section_type"] == "dosing"

    def test_clinical_section_type_background_default(self):
        chunk = make_chunk()
        m = fn(chunk)
        assert m["clinical_section_type"] == "background"


# ---------------------------------------------------------------------------
# Dosing table fields
# ---------------------------------------------------------------------------

class TestDosingTableFields:

    def test_drug_name_from_table_header(self):
        t = make_dosing_table(["Body weight", "artemether mg"], [["5-9 kg", "20 mg"]])
        chunk = make_chunk(tables=[t])
        m = fn(chunk)
        assert m["drug_name"] == "artemether"

    def test_drug_name_from_nll(self):
        t = make_dosing_table(
            ["Weight", "Dose"],
            [["5-9 kg", "80 mg"]],
            nll="IF weight is 5-9 kg, THEN lumefantrine dose is 480 mg.",
        )
        chunk = make_chunk(tables=[t])
        m = fn(chunk)
        assert m["drug_name"] == "lumefantrine"

    def test_weight_min_max_extracted(self):
        t = make_dosing_table(
            ["Body weight", "Dose"],
            [["5-9 kg", "80 mg"], ["10-14 kg", "160 mg"], ["≥35 kg", "480 mg"]],
        )
        chunk = make_chunk(tables=[t])
        m = fn(chunk)
        assert m["patient_weight_min_kg"] == 5.0
        assert m["patient_weight_max_kg"] == 14.0  # max of finite hi values

    def test_route_defaults_to_oral_for_dosing_table(self):
        t = make_dosing_table(["Weight", "Dose"], [["5-9 kg", "80 mg"]])
        chunk = make_chunk(tables=[t])
        m = fn(chunk)
        assert m["route"] == "oral"

    def test_non_dosing_table_no_drug_name(self):
        t = {
            "classification": "evidence",
            "headers": ["Outcome", "artemether effect"],
            "data": [],
            "markdown": "",
            "nll": "",
        }
        chunk = make_chunk(tables=[t])
        m = fn(chunk)
        assert m["drug_name"] is None


# ---------------------------------------------------------------------------
# Frequency, duration, dosage_summary
# ---------------------------------------------------------------------------

class TestFrequencyDuration:

    def test_frequency_extracted_from_text(self):
        chunk = make_chunk(text="Give twice daily for 3 days.")
        m = fn(chunk)
        assert "twice" in m["frequency"]

    def test_duration_extracted_from_text(self):
        chunk = make_chunk(text="Treatment for 3 days.")
        m = fn(chunk)
        assert m["duration"] == "for 3 days"

    def test_dosage_summary_combines_both(self):
        chunk = make_chunk(text="Give once daily for 5 days.")
        m = fn(chunk)
        assert m["dosage_summary"] is not None
        assert "once" in m["dosage_summary"]
        assert "5 days" in m["dosage_summary"]

    def test_frequency_from_table_markdown(self):
        t = make_dosing_table(["Weight", "Dose"], [["5-9 kg", "80 mg"]])
        t["markdown"] = "| Weight | Dose |\n| 5-9 kg | 80 mg twice daily |"
        chunk = make_chunk(tables=[t])
        m = fn(chunk)
        assert m["frequency"] is not None


# ---------------------------------------------------------------------------
# Route
# ---------------------------------------------------------------------------

class TestRoute:

    def test_oral_explicit(self):
        chunk = make_chunk(text="Administer orally with food.")
        m = fn(chunk)
        assert "oral" in m["route"]

    def test_iv_detected(self):
        chunk = make_chunk(text="Give IV artesunate for severe malaria.")
        m = fn(chunk)
        assert m["route"] is not None and "iv" in m["route"].lower()


# ---------------------------------------------------------------------------
# Level of care
# ---------------------------------------------------------------------------

class TestLevelOfCare:

    def test_hc3_extracted(self):
        chunk = make_chunk(text="Manage at HC III or higher.")
        m = fn(chunk)
        assert "HC3" in m["level_of_care"]

    def test_multiple_locs_extracted(self):
        chunk = make_chunk(text="Refer from HC II to HC IV for surgery.")
        m = fn(chunk)
        assert "HC2" in m["level_of_care"]
        assert "HC4" in m["level_of_care"]

    def test_deduplicated(self):
        chunk = make_chunk(text="HC III guidelines. Follow HC III protocol.")
        m = fn(chunk)
        assert m["level_of_care"].count("HC3") == 1


# ---------------------------------------------------------------------------
# Safety-critical fields
# ---------------------------------------------------------------------------

class TestSafetyCritical:

    def test_contraindication_extracted(self):
        chunk = make_chunk(text="Quinine is contraindicated in pregnancy.")
        m = fn(chunk)
        assert any("pregnanc" in c.lower() for c in m["contraindications"])

    def test_do_not_give_extracted(self):
        chunk = make_chunk(text="Do not give to children under 5 years.")
        m = fn(chunk)
        assert len(m["contraindications"]) >= 1

    def test_danger_signs_extracted(self):
        chunk = make_chunk(text="Danger signs: convulsions, unable to drink, severe anaemia.")
        m = fn(chunk)
        assert len(m["danger_signs"]) >= 1
        assert any("convulsion" in d.lower() for d in m["danger_signs"])

    def test_referral_criteria_extracted(self):
        chunk = make_chunk(text="Refer immediately if the patient cannot stand.")
        m = fn(chunk)
        assert len(m["referral_criteria"]) >= 1

    def test_clinical_features_extracted(self):
        chunk = make_chunk(text="Clinical features: fever, chills, rigors, headache.")
        m = fn(chunk)
        assert len(m["clinical_features"]) >= 1

    def test_special_populations_pregnant_extracted(self):
        chunk = make_chunk(text="Use with caution in pregnant women and infants.")
        m = fn(chunk)
        assert any("pregnant" in p.lower() for p in m["special_populations"])


# ---------------------------------------------------------------------------
# Age fields
# ---------------------------------------------------------------------------

class TestAgeFields:

    def test_age_max_children(self):
        chunk = make_chunk(text="For children under 5 years of age.")
        m = fn(chunk)
        assert m["patient_age_max"] is not None
        assert "5" in m["patient_age_max"]

    def test_age_min_adults(self):
        chunk = make_chunk(text="Adults ≥ 18 years should receive standard dose.")
        m = fn(chunk)
        assert m["patient_age_min"] is not None
        assert "18" in m["patient_age_min"]


# ---------------------------------------------------------------------------
# Integration: all 17 fields present on extracted metadata
# ---------------------------------------------------------------------------

class TestIntegration:

    def test_metadata_has_all_17_fields(self):
        t = make_dosing_table(["Body weight", "artemether mg"], [["5-9 kg", "20 mg"]])
        chunk = make_chunk(
            text="Give twice daily for 3 days. Contraindicated in severe liver failure.",
            heading="Artemether-Lumefantrine Dosing",
            section_type="dosing",
            tables=[t],
        )
        m = fn(chunk)
        assert set(m.keys()) == set(empty().keys())

    def test_chunk_by_headings_stamps_clinical_metadata(self):
        """_build_chunk must attach clinical_metadata to every produced chunk."""
        from pipeline.config import ExtractionConfig
        cfg = ExtractionConfig.__new__(ExtractionConfig)
        cfg.min_chunk_size = 0
        cfg.max_chunk_size = 4000
        cfg.chunk_overlap = 200
        cfg.enable_table_detection = True

        extraction = {
            "pages": [{
                "page": 1,
                "headings": [{"text": "Treatment", "level": 2, "y_pos": 10}],
                "text_blocks": [{"text": "Give twice daily for 3 days.", "y_pos": 20}],
            }],
            "tables": [],
        }
        chunker = SmartChunker(extraction, cfg)
        chunks = chunker.chunk_by_headings()
        assert len(chunks) > 0
        for chunk in chunks:
            assert "clinical_metadata" in chunk
            assert set(chunk["clinical_metadata"].keys()) == set(empty().keys())
