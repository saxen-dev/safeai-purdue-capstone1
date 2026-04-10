"""
Unit tests for MultiPassExtractor.pass2b_stitch_page_boundary_tables().

The method is called with a list of table dicts (as produced by pass2_table_extraction)
and a mock PDF.  We use a minimal fake extractor that skips the real PDF open/close
by monkeypatching fitz.open with a lightweight stub.

Run with:  python3 -m pytest tests/test_stitch_tables.py -v
"""

import re
import types
import pytest
from unittest.mock import MagicMock, patch

from pipeline.extractor import MultiPassExtractor
from pipeline.config import ExtractionConfig


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

def make_config(tmp_path):
    cfg = ExtractionConfig.__new__(ExtractionConfig)
    cfg.pdf_path = str(tmp_path / "dummy.pdf")
    cfg.dosing_table_keywords = []
    cfg.clinical_table_keywords = []
    return cfg


def make_extractor(tmp_path):
    cfg = make_config(tmp_path)
    ext = MultiPassExtractor.__new__(MultiPassExtractor)
    ext.config = cfg
    ext.passes = []
    return ext


def make_table(page, table_id, headers, rows, bbox, num_cols=None):
    """Build a minimal table dict as pass2_table_extraction would produce."""
    import pandas as pd
    df = pd.DataFrame(rows, columns=headers)
    return {
        "page": page,
        "table_id": table_id,
        "method": "pymupdf",
        "data": df.to_dict(orient="records"),
        "headers": headers,
        "markdown": "",
        "num_rows": len(df),
        "num_cols": num_cols if num_cols is not None else len(headers),
        "confidence": 0.9,
        "bbox": bbox,  # (x0, y0, x1, y1)
    }


def fake_doc(page_heights: dict):
    """Return a fitz.open() mock where each page[n] has rect.height from the dict."""
    doc = MagicMock()

    def getitem(idx):
        page = MagicMock()
        # idx is 0-based; page heights dict is 1-based
        page.rect.height = page_heights.get(idx + 1, 800)
        return page

    doc.__getitem__ = MagicMock(side_effect=getitem)
    doc.close = MagicMock()
    return doc


# ---------------------------------------------------------------------------
# Core stitching
# ---------------------------------------------------------------------------

class TestBasicStitch:

    def test_two_fragments_stitched(self, tmp_path):
        ext = make_extractor(tmp_path)
        PAGE_H = 800

        top = make_table(
            page=1, table_id=0,
            headers=["Weight", "Dose"],
            rows=[{"Weight": "5-9 kg", "Dose": "80 mg"},
                  {"Weight": "10-14 kg", "Dose": "160 mg"}],
            bbox=(50, 100, 400, 730),  # bottom = 730/800 = 91% → truncated
        )
        bot = make_table(
            page=2, table_id=0,
            headers=["Weight", "Dose"],
            rows=[{"Weight": "15-24 kg", "Dose": "240 mg"}],
            bbox=(50, 20, 400, 200),   # top = 20/800 = 2.5% → continuation
        )

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([top, bot])

        assert len(result) == 1
        stitched = result[0]
        assert stitched["stitched"] is True
        assert stitched["pages"] == [1, 2]
        assert stitched["num_rows"] == 3
        assert stitched["method"] == "pymupdf_stitched"

    def test_fragments_removed_from_output(self, tmp_path):
        ext = make_extractor(tmp_path)
        PAGE_H = 800

        top = make_table(1, 0, ["A", "B"], [{"A": "1", "B": "2"}], (0, 0, 100, 740))
        bot = make_table(2, 0, ["A", "B"], [{"A": "3", "B": "4"}], (0, 10, 100, 200))

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([top, bot])

        pages = [t["page"] for t in result]
        methods = [t["method"] for t in result]
        assert "pymupdf" not in methods
        assert "pymupdf_stitched" in methods

    def test_unrelated_table_preserved(self, tmp_path):
        ext = make_extractor(tmp_path)
        PAGE_H = 800

        top = make_table(1, 0, ["A", "B"], [{"A": "1", "B": "2"}], (0, 0, 100, 740))
        bot = make_table(2, 0, ["A", "B"], [{"A": "3", "B": "4"}], (0, 10, 100, 200))
        unrelated = make_table(3, 0, ["X", "Y"], [{"X": "a", "Y": "b"}], (0, 100, 100, 300))

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H, 3: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([top, bot, unrelated])

        assert len(result) == 2
        assert any(t["page"] == 3 for t in result)

    def test_pass_log_entry_added(self, tmp_path):
        ext = make_extractor(tmp_path)
        PAGE_H = 800
        top = make_table(1, 0, ["A", "B"], [{"A": "1", "B": "2"}], (0, 0, 100, 740))
        bot = make_table(2, 0, ["A", "B"], [{"A": "3", "B": "4"}], (0, 10, 100, 200))

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H})):
            ext.pass2b_stitch_page_boundary_tables([top, bot])

        log = ext.passes[-1]
        assert log["pass"] == "2b"
        assert log["stitched_count"] == 1
        assert log["fragments_removed"] == 2


# ---------------------------------------------------------------------------
# Threshold boundary conditions
# ---------------------------------------------------------------------------

class TestThresholds:

    def test_table_not_near_bottom_not_stitched(self, tmp_path):
        ext = make_extractor(tmp_path)
        PAGE_H = 800

        top = make_table(1, 0, ["A", "B"], [{"A": "1", "B": "2"}], (0, 0, 100, 680))  # 85% — below threshold
        bot = make_table(2, 0, ["A", "B"], [{"A": "3", "B": "4"}], (0, 10, 100, 200))

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([top, bot])

        assert len(result) == 2  # both preserved, nothing stitched

    def test_continuation_not_near_top_not_stitched(self, tmp_path):
        ext = make_extractor(tmp_path)
        PAGE_H = 800

        top = make_table(1, 0, ["A", "B"], [{"A": "1", "B": "2"}], (0, 0, 100, 740))  # 92.5%
        bot = make_table(2, 0, ["A", "B"], [{"A": "3", "B": "4"}], (0, 100, 100, 300))  # 12.5% — above threshold

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([top, bot])

        assert len(result) == 2


# ---------------------------------------------------------------------------
# Edge cases from original stage2_cross_validation.py
# ---------------------------------------------------------------------------

class TestEdgeCases:

    def test_duplicate_header_stripped_from_continuation(self, tmp_path):
        ext = make_extractor(tmp_path)
        PAGE_H = 800

        top = make_table(
            1, 0,
            headers=["Weight", "Dose"],
            rows=[{"Weight": "5-9 kg", "Dose": "80 mg"}],
            bbox=(0, 0, 100, 740),
        )
        # Continuation starts with a duplicate header row
        bot = make_table(
            2, 0,
            headers=["Weight", "Dose"],
            rows=[{"Weight": "weight", "Dose": "dose"},  # duplicate header
                  {"Weight": "15-24 kg", "Dose": "240 mg"}],
            bbox=(0, 10, 100, 200),
        )

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([top, bot])

        assert len(result) == 1
        # Should have 2 data rows (1 from top + 1 real from bottom, header stripped)
        assert result[0]["num_rows"] == 2

    def test_zero_row_continuation(self, tmp_path):
        """PyMuPDF sometimes returns 0-row DataFrames where the data is in column headers."""
        ext = make_extractor(tmp_path)
        PAGE_H = 800

        top = make_table(
            1, 0,
            headers=["Weight", "Dose"],
            rows=[{"Weight": "5-9 kg", "Dose": "80 mg"}],
            bbox=(0, 0, 100, 740),
        )
        # 0-row continuation: data ended up in headers
        bot = {
            "page": 2,
            "table_id": 0,
            "method": "pymupdf",
            "data": [],
            "headers": ["15-24 kg", "240 mg"],
            "markdown": "",
            "num_rows": 0,
            "num_cols": 2,
            "confidence": 0.9,
            "bbox": (0, 10, 100, 100),
        }

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([top, bot])

        assert len(result) == 1
        assert result[0]["num_rows"] == 2

    def test_column_mismatch_not_stitched(self, tmp_path):
        ext = make_extractor(tmp_path)
        PAGE_H = 800

        top = make_table(1, 0, ["A", "B"], [{"A": "1", "B": "2"}], (0, 0, 100, 740))
        bot = make_table(2, 0, ["A", "B", "C"], [{"A": "3", "B": "4", "C": "5"}], (0, 10, 100, 200), num_cols=3)

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([top, bot])

        assert len(result) == 2  # no stitch

    def test_camelot_tables_passed_through(self, tmp_path):
        ext = make_extractor(tmp_path)
        PAGE_H = 800

        camelot_table = {
            "page": 1,
            "method": "camelot_lattice",
            "data": [{"A": "1"}],
            "headers": ["A"],
            "markdown": "",
            "num_rows": 1,
            "num_cols": 1,
            "confidence": 0.95,
            # No bbox key
        }

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([camelot_table])

        assert len(result) == 1
        assert result[0]["method"] == "camelot_lattice"


# ---------------------------------------------------------------------------
# Classification of stitched table
# ---------------------------------------------------------------------------

class TestStitchedClassification:

    def test_stitched_dosing_table_classified_correctly(self, tmp_path):
        ext = make_extractor(tmp_path)
        ext.config.dosing_table_keywords = ["artemether"]
        PAGE_H = 800

        top = make_table(
            1, 0,
            headers=["Body weight", "Dose"],
            rows=[{"Body weight": "5-9 kg", "Dose": "80 mg"}],
            bbox=(0, 0, 100, 740),
        )
        bot = make_table(
            2, 0,
            headers=["Body weight", "Dose"],
            rows=[{"Body weight": "10-14 kg", "Dose": "160 mg artemether"}],
            bbox=(0, 10, 100, 200),
        )

        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({1: PAGE_H, 2: PAGE_H})):
            result = ext.pass2b_stitch_page_boundary_tables([top, bot])

        assert result[0]["classification"] == "dosing"

    def test_empty_input_returns_empty(self, tmp_path):
        ext = make_extractor(tmp_path)
        with patch("pipeline.extractor.fitz.open", return_value=fake_doc({})):
            result = ext.pass2b_stitch_page_boundary_tables([])
        assert result == []
