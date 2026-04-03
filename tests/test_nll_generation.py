"""
Unit tests for MultiPassExtractor._generate_nll() and _write_nll_file().

Run with:  python3 -m pytest tests/test_nll_generation.py -v
"""

import os
import pytest
from pipeline.extractor import MultiPassExtractor

fn = MultiPassExtractor._generate_nll


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_table(classification, headers, rows):
    return {
        "classification": classification,
        "headers": headers,
        "data": [dict(zip(headers, r)) if isinstance(r, (list, tuple)) else r for r in rows],
    }


# ---------------------------------------------------------------------------
# Core NLL output
# ---------------------------------------------------------------------------

class TestNLLOutput:

    def test_dosing_table_produces_sentences(self):
        t = make_table(
            "dosing",
            ["Body weight", "Dose", "Frequency", "Duration"],
            [["5–<15 kg", "1 tablet", "twice daily", "3 days"]],
        )
        nll = fn(t)
        assert nll != ""
        assert "IF Body weight is 5–<15 kg" in nll
        assert "THEN" in nll
        assert "Dose is 1 tablet" in nll
        assert "Frequency is twice daily" in nll
        assert "Duration is 3 days" in nll

    def test_clinical_management_table_produces_sentences(self):
        t = make_table(
            "clinical_management",
            ["Danger sign", "Action"],
            [["Unable to drink", "Refer immediately"]],
        )
        nll = fn(t)
        assert "IF Danger sign is Unable to drink" in nll
        assert "THEN Action is Refer immediately" in nll

    def test_each_row_becomes_one_sentence(self):
        t = make_table(
            "dosing",
            ["Weight", "Dose"],
            [["5-9 kg", "80 mg"], ["10-14 kg", "160 mg"], ["15-24 kg", "240 mg"]],
        )
        nll = fn(t)
        sentences = [s for s in nll.split("\n") if s.strip()]
        assert len(sentences) == 3

    def test_sentence_ends_with_period(self):
        t = make_table("dosing", ["Weight", "Dose"], [["5-9 kg", "80 mg"]])
        nll = fn(t)
        assert nll.strip().endswith(".")

    def test_single_column_no_then_clause(self):
        t = make_table("dosing", ["Weight"], [["5-9 kg"]])
        nll = fn(t)
        assert "IF Weight is 5-9 kg." in nll
        assert "THEN" not in nll


# ---------------------------------------------------------------------------
# NLL suppressed for non-dosing/clinical types
# ---------------------------------------------------------------------------

class TestNLLSuppressed:

    def test_evidence_table_returns_empty(self):
        t = make_table(
            "evidence",
            ["Outcome", "Certainty"],
            [["Fever clearance", "Moderate"]],
        )
        assert fn(t) == ""

    def test_structural_table_returns_empty(self):
        t = make_table(
            "structural",
            ["Abbreviation", "Full name"],
            [["AL", "Artemether-lumefantrine"]],
        )
        assert fn(t) == ""

    def test_other_table_returns_empty(self):
        t = make_table("other", ["A", "B"], [["1", "2"]])
        assert fn(t) == ""


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------

class TestNLLEdgeCases:

    def test_empty_data_returns_empty(self):
        t = make_table("dosing", ["Weight", "Dose"], [])
        assert fn(t) == ""

    def test_empty_headers_returns_empty(self):
        t = {"classification": "dosing", "headers": [], "data": [{"A": "1"}]}
        assert fn(t) == ""

    def test_missing_classification_returns_empty(self):
        t = {"headers": ["Weight", "Dose"], "data": [{"Weight": "5 kg", "Dose": "80 mg"}]}
        assert fn(t) == ""

    def test_row_with_all_empty_values_skipped(self):
        t = make_table(
            "dosing",
            ["Weight", "Dose"],
            [["5-9 kg", "80 mg"], ["", ""]],
        )
        sentences = [s for s in fn(t).split("\n") if s.strip()]
        assert len(sentences) == 1

    def test_row_with_partial_empty_values(self):
        # Only non-empty (header, value) pairs are included
        t = make_table(
            "dosing",
            ["Weight", "Dose", "Notes"],
            [["5-9 kg", "80 mg", ""]],
        )
        nll = fn(t)
        assert "Notes" not in nll
        assert "Dose is 80 mg" in nll

    def test_list_rows_handled(self):
        # data as list of lists (not dicts)
        t = {
            "classification": "dosing",
            "headers": ["Weight", "Dose"],
            "data": [["5-9 kg", "80 mg"]],
        }
        nll = fn(t)
        assert "IF Weight is 5-9 kg" in nll

    def test_dict_rows_handled(self):
        t = {
            "classification": "dosing",
            "headers": ["Weight", "Dose"],
            "data": [{"Weight": "5-9 kg", "Dose": "80 mg"}],
        }
        nll = fn(t)
        assert "IF Weight is 5-9 kg" in nll

    def test_multirow_output_joined_by_newlines(self):
        t = make_table(
            "dosing",
            ["Weight", "Dose"],
            [["5-9 kg", "80 mg"], ["10-14 kg", "160 mg"]],
        )
        nll = fn(t)
        lines = nll.split("\n")
        assert len(lines) == 2
        assert all(line.startswith("IF") for line in lines)


# ---------------------------------------------------------------------------
# _write_nll_file integration
# ---------------------------------------------------------------------------

class TestWriteNLLFile:

    def _make_extractor(self, tmp_path):
        from pipeline.config import ExtractionConfig
        cfg = ExtractionConfig.__new__(ExtractionConfig)
        cfg.output_dir = str(tmp_path)
        ext = MultiPassExtractor.__new__(MultiPassExtractor)
        ext.config = cfg
        return ext

    def test_nll_file_created_for_dosing_tables(self, tmp_path):
        ext = self._make_extractor(tmp_path)
        tables = [
            {**make_table("dosing", ["Weight", "Dose"], [["5-9 kg", "80 mg"]]),
             "page": 3, "nll": fn(make_table("dosing", ["Weight", "Dose"], [["5-9 kg", "80 mg"]]))},
        ]
        ext._write_nll_file(tables)
        nll_path = tmp_path / "tables_nll.txt"
        assert nll_path.exists()
        content = nll_path.read_text()
        assert "IF Weight is 5-9 kg" in content

    def test_nll_file_not_created_when_no_nll_tables(self, tmp_path):
        ext = self._make_extractor(tmp_path)
        tables = [
            {**make_table("evidence", ["Outcome", "Certainty"], [["Fever", "Moderate"]]),
             "page": 1, "nll": ""},
        ]
        ext._write_nll_file(tables)
        assert not (tmp_path / "tables_nll.txt").exists()

    def test_nll_file_contains_page_and_classification(self, tmp_path):
        ext = self._make_extractor(tmp_path)
        t = make_table("dosing", ["Weight", "Dose"], [["5-9 kg", "80 mg"]])
        t["page"] = 5
        t["nll"] = fn(t)
        ext._write_nll_file([t])
        content = (tmp_path / "tables_nll.txt").read_text()
        assert "dosing" in content
        assert "5" in content  # page number

    def test_nll_file_contains_multiple_tables(self, tmp_path):
        ext = self._make_extractor(tmp_path)
        tables = []
        for i, w in enumerate(["5-9 kg", "10-14 kg"]):
            t = make_table("dosing", ["Weight", "Dose"], [[w, "80 mg"]])
            t["page"] = i + 1
            t["nll"] = fn(t)
            tables.append(t)
        ext._write_nll_file(tables)
        content = (tmp_path / "tables_nll.txt").read_text()
        assert "Table 1" in content
        assert "Table 2" in content
