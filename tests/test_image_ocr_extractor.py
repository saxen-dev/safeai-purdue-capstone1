"""
Unit tests for extractor.py image OCR enrichment (P12).

Tests cover:
  - _ocr_image_file: graceful fallback, pytesseract path, easyocr path
  - _extract_image_caption: spatial caption extraction via mocked fitz page
  - pass_images_extraction: inventory items carry ocr_text + caption fields
    and the pass log includes OCR stats

Run with:  python3 -m pytest tests/test_image_ocr_extractor.py -v
"""

import os
import tempfile
import types
from unittest.mock import MagicMock, patch

import pytest

import pipeline.extractor as extractor_module
from pipeline.extractor import (
    _CAPTION_PREFIX_RE,
    _extract_image_caption,
    _ocr_image_file,
)


# ---------------------------------------------------------------------------
# _CAPTION_PREFIX_RE
# ---------------------------------------------------------------------------

class TestCaptionPrefixRe:

    def test_matches_figure(self):
        assert _CAPTION_PREFIX_RE.match("Figure 1. Malaria cycle.")

    def test_matches_fig_dot(self):
        assert _CAPTION_PREFIX_RE.match("Fig. 3 treatment flow")

    def test_matches_chart(self):
        assert _CAPTION_PREFIX_RE.match("Chart 2 — dosing")

    def test_matches_diagram_no_number(self):
        assert _CAPTION_PREFIX_RE.match("Diagram overview")

    def test_does_not_match_plain_text(self):
        assert not _CAPTION_PREFIX_RE.match("Malaria is endemic in Uganda.")

    def test_case_insensitive(self):
        assert _CAPTION_PREFIX_RE.match("FIGURE 1")


# ---------------------------------------------------------------------------
# _ocr_image_file
# ---------------------------------------------------------------------------

class TestOcrImageFile:

    def test_returns_empty_when_no_engine(self):
        """When neither pytesseract nor easyocr is installed, returns ''."""
        with patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", False), \
             patch.object(extractor_module, "_EASYOCR_AVAILABLE", False):
            result = _ocr_image_file("/nonexistent/image.png")
        assert result == ""

    def test_pytesseract_path_called(self):
        """When pytesseract is available, image_to_string is called."""
        mock_img = MagicMock()
        mock_pil = MagicMock()
        mock_pil.open.return_value = mock_img
        mock_tess = MagicMock()
        mock_tess.image_to_string.return_value = "  malaria dosing  "

        with patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", True), \
             patch.object(extractor_module, "_PIL_Image", mock_pil), \
             patch.object(extractor_module, "_pytesseract", mock_tess):
            result = _ocr_image_file("/some/image.png")

        assert result == "malaria dosing"
        mock_tess.image_to_string.assert_called_once()

    def test_pytesseract_exception_falls_back_to_easyocr(self):
        """If pytesseract raises, try easyocr."""
        mock_pil = MagicMock()
        mock_pil.open.side_effect = Exception("bad image")
        mock_tess = MagicMock()
        mock_reader = MagicMock()
        mock_reader.readtext.return_value = ["give", "20mg"]
        mock_easyocr_mod = MagicMock()
        mock_easyocr_mod.Reader.return_value = mock_reader

        with patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", True), \
             patch.object(extractor_module, "_PIL_Image", mock_pil), \
             patch.object(extractor_module, "_pytesseract", mock_tess), \
             patch.object(extractor_module, "_EASYOCR_AVAILABLE", True), \
             patch.object(extractor_module, "_easyocr", mock_easyocr_mod), \
             patch.object(extractor_module, "_easyocr_reader", None):
            result = _ocr_image_file("/some/image.png")

        assert "give" in result or "20mg" in result

    def test_easyocr_path_joins_tokens(self):
        """easyocr path joins all readtext tokens into a single string."""
        mock_reader = MagicMock()
        mock_reader.readtext.return_value = ["word1", "word2", "word3"]
        mock_easyocr_mod = MagicMock()
        mock_easyocr_mod.Reader.return_value = mock_reader

        with patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", False), \
             patch.object(extractor_module, "_EASYOCR_AVAILABLE", True), \
             patch.object(extractor_module, "_easyocr", mock_easyocr_mod), \
             patch.object(extractor_module, "_easyocr_reader", None):
            result = _ocr_image_file("/some/image.png")

        assert result == "word1 word2 word3"

    def test_easyocr_exception_returns_empty(self):
        """If easyocr also fails, return ''."""
        mock_easyocr_mod = MagicMock()
        mock_easyocr_mod.Reader.side_effect = Exception("gpu error")

        with patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", False), \
             patch.object(extractor_module, "_EASYOCR_AVAILABLE", True), \
             patch.object(extractor_module, "_easyocr", mock_easyocr_mod), \
             patch.object(extractor_module, "_easyocr_reader", None):
            result = _ocr_image_file("/some/image.png")

        assert result == ""

    def test_easyocr_reader_reused_across_calls(self):
        """easyocr.Reader is constructed once and reused."""
        mock_reader = MagicMock()
        mock_reader.readtext.return_value = ["text"]
        mock_easyocr_mod = MagicMock()
        mock_easyocr_mod.Reader.return_value = mock_reader

        with patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", False), \
             patch.object(extractor_module, "_EASYOCR_AVAILABLE", True), \
             patch.object(extractor_module, "_easyocr", mock_easyocr_mod), \
             patch.object(extractor_module, "_easyocr_reader", None):
            _ocr_image_file("/a.png")
            _ocr_image_file("/b.png")

        # Reader constructor called only once
        assert mock_easyocr_mod.Reader.call_count == 1


# ---------------------------------------------------------------------------
# _extract_image_caption
# ---------------------------------------------------------------------------

def _make_mock_page(rects, blocks):
    """Build a minimal mock fitz page for caption extraction tests."""
    page = MagicMock()
    page.get_image_rects.return_value = rects
    page.get_text.return_value = blocks
    return page


def _rect(x0, y0, x1, y1):
    """Minimal fitz.Rect substitute (just needs attribute access)."""
    r = MagicMock()
    r.x0 = x0
    r.y0 = y0
    r.x1 = x1
    r.y1 = y1
    return r


class TestExtractImageCaption:

    def test_returns_empty_when_no_rects(self):
        page = _make_mock_page([], [])
        assert _extract_image_caption(page, xref=1) == ""

    def test_finds_figure_caption_below_image(self):
        img_rect = _rect(50, 100, 400, 300)
        # A block starting at y=310 (within 80pt of y1=300)
        blocks = [
            (50, 310, 400, 325, "Figure 1. Malaria treatment flowchart.", 0, 0),
        ]
        page = _make_mock_page([img_rect], blocks)
        caption = _extract_image_caption(page, xref=1)
        assert "Figure 1" in caption

    def test_ignores_block_above_image(self):
        img_rect = _rect(50, 100, 400, 300)
        # Block at y=50 (above image) — should be ignored
        blocks = [
            (50, 50, 400, 80, "Figure 1. Some caption above.", 0, 0),
        ]
        page = _make_mock_page([img_rect], blocks)
        caption = _extract_image_caption(page, xref=1)
        assert caption == ""

    def test_ignores_block_too_far_below(self):
        img_rect = _rect(50, 100, 400, 300)
        # Block at y=400 (>80pt below y1=300)
        blocks = [
            (50, 400, 400, 420, "Some paragraph far below.", 0, 0),
        ]
        page = _make_mock_page([img_rect], blocks)
        caption = _extract_image_caption(page, xref=1)
        assert caption == ""

    def test_prefers_caption_pattern_over_plain_text(self):
        img_rect = _rect(50, 100, 400, 300)
        blocks = [
            (50, 305, 400, 315, "Some generic text below.", 0, 0),
            (50, 320, 400, 335, "Fig. 2 Dosing chart by weight band.", 0, 0),
        ]
        page = _make_mock_page([img_rect], blocks)
        caption = _extract_image_caption(page, xref=1)
        assert "Fig. 2" in caption

    def test_caption_truncated_to_300_chars(self):
        img_rect = _rect(50, 100, 400, 300)
        long_text = "Figure 1. " + "x" * 400
        blocks = [(50, 305, 400, 320, long_text, 0, 0)]
        page = _make_mock_page([img_rect], blocks)
        caption = _extract_image_caption(page, xref=1)
        assert len(caption) <= 300

    def test_exception_returns_empty(self):
        """If get_image_rects raises, return '' gracefully."""
        page = MagicMock()
        page.get_image_rects.side_effect = AttributeError("not supported")
        assert _extract_image_caption(page, xref=1) == ""

    def test_empty_text_blocks_ignored(self):
        img_rect = _rect(50, 100, 400, 300)
        blocks = [(50, 305, 400, 315, "   ", 0, 0)]
        page = _make_mock_page([img_rect], blocks)
        assert _extract_image_caption(page, xref=1) == ""


# ---------------------------------------------------------------------------
# pass_images_extraction — inventory fields
# ---------------------------------------------------------------------------

def _make_extractor_with_config(output_dir):
    """Build a MultiPassExtractor with a minimal config (no real PDF needed)."""
    from pipeline.extractor import MultiPassExtractor
    from pipeline.config import ExtractionConfig

    config = ExtractionConfig.__new__(ExtractionConfig)
    config.pdf_path = "/fake/path.pdf"
    config.output_dir = output_dir
    config.cache_dir = os.path.join(output_dir, "cache")
    config.enable_image_extraction = True
    config.enable_table_detection = True
    config.dosing_table_keywords = []
    config.clinical_table_keywords = []
    config.document_title = "Test Doc"
    config.source_label = "test"

    ext = MultiPassExtractor.__new__(MultiPassExtractor)
    ext.config = config
    ext.passes = []
    return ext


def _make_fitz_mock(pages_images):
    """
    Build a fitz.open() mock that yields pages with embedded images.

    pages_images: list of lists of image specs.
    Each spec: {"xref": int, "width": int, "height": int, "caption_blocks": [...]}
    """
    doc = MagicMock()
    doc.__len__.return_value = len(pages_images)

    page_mocks = []
    for page_idx, images in enumerate(pages_images):
        page = MagicMock()
        # get_images returns [(xref, ...), ...]
        page.get_images.return_value = [(spec["xref"],) for spec in images]

        # get_image_rects returns list with one Rect per image
        def _make_rects(spec):
            rect = _rect(10, 10, 200, 200)
            return [rect]

        # Set up get_image_rects to dispatch by xref
        def _get_image_rects(xref, _images=images):
            for spec in _images:
                if spec["xref"] == xref:
                    return [_rect(10, 10, 200, 200)]
            return []

        page.get_image_rects.side_effect = _get_image_rects
        page.get_text.return_value = []  # no captions by default
        page_mocks.append(page)

    doc.__getitem__.side_effect = lambda idx: page_mocks[idx]
    doc.close = MagicMock()
    return doc


class TestPassImagesInventoryFields:

    def _run(self, output_dir, doc_mock, images_per_page=None):
        """Run pass_images_extraction with a mocked fitz.open()."""
        from pipeline.extractor import MultiPassExtractor
        ext = _make_extractor_with_config(output_dir)

        pix_mock = MagicMock()
        pix_mock.width = 100
        pix_mock.height = 100
        pix_mock.n = 3
        pix_mock.alpha = 0
        pix_mock.save = MagicMock()

        with patch("pipeline.extractor.fitz.open", return_value=doc_mock), \
             patch("pipeline.extractor.fitz.Pixmap", return_value=pix_mock), \
             patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", False), \
             patch.object(extractor_module, "_EASYOCR_AVAILABLE", False):
            inventory = ext.pass_images_extraction()

        return inventory

    def test_inventory_items_have_ocr_text_field(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = _make_fitz_mock([[{"xref": 1, "width": 100, "height": 100}]])
            inventory = self._run(tmp, doc)
            assert len(inventory) == 1
            assert "ocr_text" in inventory[0]

    def test_inventory_items_have_caption_field(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = _make_fitz_mock([[{"xref": 1, "width": 100, "height": 100}]])
            inventory = self._run(tmp, doc)
            assert "caption" in inventory[0]

    def test_ocr_text_empty_when_no_engine(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = _make_fitz_mock([[{"xref": 1, "width": 100, "height": 100}]])
            inventory = self._run(tmp, doc)
            assert inventory[0]["ocr_text"] == ""

    def test_caption_empty_when_no_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = _make_fitz_mock([[{"xref": 1, "width": 100, "height": 100}]])
            inventory = self._run(tmp, doc)
            assert inventory[0]["caption"] == ""

    def test_pass_log_has_ocr_engine_field(self):
        with tempfile.TemporaryDirectory() as tmp:
            from pipeline.extractor import MultiPassExtractor
            ext = _make_extractor_with_config(tmp)
            pix_mock = MagicMock()
            pix_mock.width = 100
            pix_mock.height = 100
            pix_mock.n = 3
            pix_mock.alpha = 0
            doc = _make_fitz_mock([[{"xref": 1, "width": 100, "height": 100}]])
            with patch("pipeline.extractor.fitz.open", return_value=doc), \
                 patch("pipeline.extractor.fitz.Pixmap", return_value=pix_mock), \
                 patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", False), \
                 patch.object(extractor_module, "_EASYOCR_AVAILABLE", False):
                ext.pass_images_extraction()
            log = ext.passes[-1]
            assert "ocr_engine" in log
            assert log["ocr_engine"] == "none"

    def test_pass_log_ocr_engine_pytesseract_when_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            from pipeline.extractor import MultiPassExtractor
            ext = _make_extractor_with_config(tmp)
            pix_mock = MagicMock()
            pix_mock.width = 100
            pix_mock.height = 100
            pix_mock.n = 3
            pix_mock.alpha = 0
            doc = _make_fitz_mock([[{"xref": 1, "width": 100, "height": 100}]])
            mock_pil = MagicMock()
            mock_tess = MagicMock()
            mock_tess.image_to_string.return_value = "ocr result"
            with patch("pipeline.extractor.fitz.open", return_value=doc), \
                 patch("pipeline.extractor.fitz.Pixmap", return_value=pix_mock), \
                 patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", True), \
                 patch.object(extractor_module, "_PIL_Image", mock_pil), \
                 patch.object(extractor_module, "_pytesseract", mock_tess):
                ext.pass_images_extraction()
            log = ext.passes[-1]
            assert log["ocr_engine"] == "pytesseract"

    def test_ocr_text_populated_when_pytesseract_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            from pipeline.extractor import MultiPassExtractor
            ext = _make_extractor_with_config(tmp)
            pix_mock = MagicMock()
            pix_mock.width = 100
            pix_mock.height = 100
            pix_mock.n = 3
            pix_mock.alpha = 0
            doc = _make_fitz_mock([[{"xref": 1, "width": 100, "height": 100}]])
            mock_pil = MagicMock()
            mock_tess = MagicMock()
            mock_tess.image_to_string.return_value = "  dosing chart  "
            with patch("pipeline.extractor.fitz.open", return_value=doc), \
                 patch("pipeline.extractor.fitz.Pixmap", return_value=pix_mock), \
                 patch.object(extractor_module, "_PYTESSERACT_AVAILABLE", True), \
                 patch.object(extractor_module, "_PIL_Image", mock_pil), \
                 patch.object(extractor_module, "_pytesseract", mock_tess):
                inventory = ext.pass_images_extraction()
            assert inventory[0]["ocr_text"] == "dosing chart"
