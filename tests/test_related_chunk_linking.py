"""
Unit tests for SmartChunker._link_related_chunks() (P8).

Run with:  python3 -m pytest tests/test_related_chunk_linking.py -v
"""

import pytest
from pipeline.chunker import SmartChunker
from pipeline.config import ExtractionConfig, PreservationLevel


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_config():
    cfg = ExtractionConfig.__new__(ExtractionConfig)
    cfg.min_chunk_size = 0
    cfg.max_chunk_size = 4000
    cfg.chunk_overlap = 200
    cfg.enable_table_detection = True
    cfg.output_dir = ""
    return cfg


def _make_chunker_with_chunks(chunks):
    """Inject a pre-built chunk list directly into a SmartChunker instance."""
    extraction = {"pages": [], "tables": []}
    chunker = SmartChunker(extraction, make_config())
    chunker.chunks = chunks
    return chunker


def _narrative(chunk_id, heading="Section A"):
    """A plain text chunk (narrative)."""
    return {
        "chunk_id": chunk_id,
        "heading": heading,
        "is_table_only": False,
        "content_type": None,
        "related_chunks": {},
        "related_chunk_ids": [],
    }


def _table_chunk(chunk_id, heading="Section A"):
    """A standalone table chunk (non-narrative)."""
    return {
        "chunk_id": chunk_id,
        "heading": heading,
        "is_table_only": True,
        "content_type": None,
        "related_chunks": {},
        "related_chunk_ids": [],
    }


def _image_chunk(chunk_id, heading="Section A", content_type="image_ocr"):
    """An image chunk (non-narrative)."""
    return {
        "chunk_id": chunk_id,
        "heading": heading,
        "is_table_only": False,
        "content_type": content_type,
        "related_chunks": {},
        "related_chunk_ids": [],
    }


# ---------------------------------------------------------------------------
# Pass 1 — sequential prev/next siblings
# ---------------------------------------------------------------------------

class TestPass1Sequential:

    def test_middle_chunk_has_prev_and_next(self):
        chunks = [_narrative("a"), _narrative("b"), _narrative("c")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[1]["related_chunks"]["prev_sibling"] == "a"
        assert c.chunks[1]["related_chunks"]["next_sibling"] == "c"

    def test_first_chunk_no_prev(self):
        chunks = [_narrative("a"), _narrative("b")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[0]["related_chunks"]["prev_sibling"] is None

    def test_last_chunk_no_next(self):
        chunks = [_narrative("a"), _narrative("b")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[-1]["related_chunks"]["next_sibling"] is None

    def test_single_chunk_both_none(self):
        chunks = [_narrative("solo")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[0]["related_chunks"]["prev_sibling"] is None
        assert c.chunks[0]["related_chunks"]["next_sibling"] is None

    def test_empty_chunks_no_error(self):
        c = _make_chunker_with_chunks([])
        c._link_related_chunks()  # must not raise


# ---------------------------------------------------------------------------
# Pass 2 — table/image ↔ narrative proximity
# ---------------------------------------------------------------------------

class TestPass2TableNarrativeProximity:

    def test_table_gets_preceding_narrative(self):
        chunks = [_narrative("narr1"), _table_chunk("tbl1")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[1]["related_chunks"]["preceding_narrative"] == "narr1"

    def test_table_gets_following_narrative(self):
        chunks = [_table_chunk("tbl1"), _narrative("narr1")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[0]["related_chunks"]["following_narrative"] == "narr1"

    def test_narrative_gets_context_for_tables(self):
        chunks = [_narrative("narr1"), _table_chunk("tbl1")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert "tbl1" in c.chunks[0]["related_chunks"]["context_for_tables"]

    def test_multiple_tables_each_get_same_preceding_narrative(self):
        chunks = [_narrative("narr1"), _table_chunk("tbl1"), _table_chunk("tbl2")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[1]["related_chunks"]["preceding_narrative"] == "narr1"
        assert c.chunks[2]["related_chunks"]["preceding_narrative"] == "narr1"
        assert "tbl1" in c.chunks[0]["related_chunks"]["context_for_tables"]
        assert "tbl2" in c.chunks[0]["related_chunks"]["context_for_tables"]

    def test_narrative_between_two_tables_gets_both_in_context(self):
        chunks = [_narrative("narr1"), _table_chunk("tbl1"), _narrative("narr2"), _table_chunk("tbl2")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert "tbl1" in c.chunks[0]["related_chunks"]["context_for_tables"]
        assert "tbl2" in c.chunks[2]["related_chunks"]["context_for_tables"]

    def test_image_ocr_chunk_treated_as_non_narrative(self):
        chunks = [_narrative("narr1"), _image_chunk("img1", content_type="image_ocr")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[1]["related_chunks"]["preceding_narrative"] == "narr1"
        assert "img1" in c.chunks[0]["related_chunks"]["context_for_tables"]

    def test_image_placeholder_chunk_treated_as_non_narrative(self):
        chunks = [_narrative("narr1"), _image_chunk("img1", content_type="image_placeholder")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[1]["related_chunks"]["preceding_narrative"] == "narr1"

    def test_table_at_start_has_no_preceding_narrative(self):
        chunks = [_table_chunk("tbl1"), _narrative("narr1")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[0]["related_chunks"]["preceding_narrative"] is None

    def test_table_at_end_has_no_following_narrative(self):
        chunks = [_narrative("narr1"), _table_chunk("tbl1")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[1]["related_chunks"]["following_narrative"] is None

    def test_narrative_chunks_have_empty_preceding_narrative(self):
        chunks = [_narrative("narr1"), _narrative("narr2")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[0]["related_chunks"]["preceding_narrative"] is None
        assert c.chunks[1]["related_chunks"]["preceding_narrative"] is None


# ---------------------------------------------------------------------------
# Pass 3 — section siblings
# ---------------------------------------------------------------------------

class TestPass3SectionSiblings:

    def test_same_heading_chunks_are_siblings(self):
        chunks = [
            _narrative("a", heading="Malaria"),
            _narrative("b", heading="Malaria"),
            _narrative("c", heading="Malaria"),
        ]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert set(c.chunks[0]["related_chunks"]["section_siblings"]) == {"b", "c"}
        assert set(c.chunks[1]["related_chunks"]["section_siblings"]) == {"a", "c"}

    def test_different_headings_not_siblings(self):
        chunks = [
            _narrative("a", heading="Malaria"),
            _narrative("b", heading="Tuberculosis"),
        ]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[0]["related_chunks"]["section_siblings"] == []
        assert c.chunks[1]["related_chunks"]["section_siblings"] == []

    def test_chunk_not_its_own_sibling(self):
        chunks = [_narrative("a", heading="X"), _narrative("b", heading="X")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert "a" not in c.chunks[0]["related_chunks"]["section_siblings"]
        assert "b" not in c.chunks[1]["related_chunks"]["section_siblings"]

    def test_single_chunk_in_section_has_empty_siblings(self):
        chunks = [_narrative("solo", heading="Unique")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert c.chunks[0]["related_chunks"]["section_siblings"] == []


# ---------------------------------------------------------------------------
# related_chunk_ids flat list
# ---------------------------------------------------------------------------

class TestRelatedChunkIds:

    def test_flat_list_contains_prev_and_next(self):
        chunks = [_narrative("a"), _narrative("b"), _narrative("c")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        ids = c.chunks[1]["related_chunk_ids"]
        assert "a" in ids
        assert "c" in ids

    def test_flat_list_contains_preceding_narrative(self):
        chunks = [_narrative("narr1"), _table_chunk("tbl1")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert "narr1" in c.chunks[1]["related_chunk_ids"]

    def test_flat_list_contains_context_for_tables(self):
        chunks = [_narrative("narr1"), _table_chunk("tbl1")]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert "tbl1" in c.chunks[0]["related_chunk_ids"]

    def test_flat_list_contains_section_siblings(self):
        chunks = [
            _narrative("a", heading="X"),
            _narrative("b", heading="X"),
        ]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        assert "b" in c.chunks[0]["related_chunk_ids"]
        assert "a" in c.chunks[1]["related_chunk_ids"]

    def test_flat_list_no_duplicates(self):
        # prev_sibling and section_sibling could both be "a"
        chunks = [
            _narrative("a", heading="X"),
            _narrative("b", heading="X"),
        ]
        c = _make_chunker_with_chunks(chunks)
        c._link_related_chunks()
        ids = c.chunks[1]["related_chunk_ids"]
        assert len(ids) == len(set(ids))


# ---------------------------------------------------------------------------
# Integration: chunk_by_headings populates linking
# ---------------------------------------------------------------------------

class TestChunkByHeadingsLinking:

    def _make_extraction(self):
        return {
            "pages": [
                {
                    "page": 1,
                    "headings": [{"text": "Treatment", "level": 2, "y_pos": 0}],
                    "text_blocks": [{"text": "Give twice daily.", "y_pos": 10}],
                },
                {
                    "page": 2,
                    "headings": [{"text": "Dosing", "level": 2, "y_pos": 0}],
                    "text_blocks": [{"text": "Body weight matters.", "y_pos": 10}],
                },
            ],
            "tables": [],
        }

    def test_chunks_have_related_chunks_dict(self):
        chunker = SmartChunker(self._make_extraction(), make_config())
        chunks = chunker.chunk_by_headings()
        for chunk in chunks:
            assert "related_chunks" in chunk

    def test_sequential_linking_in_output(self):
        chunker = SmartChunker(self._make_extraction(), make_config())
        chunks = chunker.chunk_by_headings()
        if len(chunks) >= 2:
            # First chunk should point to second
            assert chunks[0]["related_chunks"]["next_sibling"] == chunks[1]["chunk_id"]
            # Second chunk should point back
            assert chunks[1]["related_chunks"]["prev_sibling"] == chunks[0]["chunk_id"]

    def test_related_chunk_ids_populated(self):
        chunker = SmartChunker(self._make_extraction(), make_config())
        chunks = chunker.chunk_by_headings()
        # At least some chunks should have non-empty related_chunk_ids
        any_linked = any(len(c["related_chunk_ids"]) > 0 for c in chunks)
        assert any_linked
