"""
Unit tests for SmartChunker image OCR enrichment (P7).

Run with:  python3 -m pytest tests/test_image_ocr_enrichment.py -v
"""

import json
import pathlib
import tempfile

import pytest
from pipeline.chunker import SmartChunker
from pipeline.config import ExtractionConfig, PreservationLevel


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_config(output_dir=None):
    cfg = ExtractionConfig.__new__(ExtractionConfig)
    cfg.min_chunk_size = 0
    cfg.max_chunk_size = 4000
    cfg.chunk_overlap = 200
    cfg.enable_table_detection = True
    cfg.output_dir = output_dir or ""
    return cfg


def make_extraction(pages=None, tables=None, image_inventory=None):
    result = {
        "pages": pages or [],
        "tables": tables or [],
    }
    if image_inventory is not None:
        result["image_inventory"] = image_inventory
    return result


def make_page(page_num, text="Some content."):
    return {
        "page": page_num,
        "headings": [{"text": "Section", "level": 2, "y_pos": 0}],
        "text_blocks": [{"text": text, "y_pos": 10}],
    }


def make_image_data(page_no, ocr_text="", caption="", saved_path=""):
    return {
        "page_no": page_no,
        "ocr_text": ocr_text,
        "caption": caption,
        "saved_path": saved_path,
    }


def make_chunker(pages=None, image_inventory=None, output_dir=None):
    extraction = make_extraction(
        pages=pages or [make_page(1)],
        image_inventory=image_inventory,
    )
    cfg = make_config(output_dir=output_dir)
    return SmartChunker(extraction, cfg)


# ---------------------------------------------------------------------------
# _load_image_inventory — sources
# ---------------------------------------------------------------------------

class TestLoadImageInventory:

    def test_loads_from_extraction_dict(self):
        img = make_image_data(1, ocr_text="Flowchart text")
        chunker = make_chunker(image_inventory=[img])
        assert 1 in chunker._image_by_page
        assert chunker._image_by_page[1][0]["ocr_text"] == "Flowchart text"

    def test_empty_when_no_inventory(self):
        chunker = make_chunker(image_inventory=None)
        assert chunker._image_by_page == {}

    def test_loads_from_file_when_not_in_extraction(self):
        with tempfile.TemporaryDirectory() as tmp:
            inv = [make_image_data(2, ocr_text="File-loaded OCR")]
            path = pathlib.Path(tmp) / "image_inventory.json"
            path.write_text(json.dumps(inv), encoding="utf-8")
            chunker = make_chunker(image_inventory=None, output_dir=tmp)
            assert 2 in chunker._image_by_page
            assert "File-loaded OCR" in chunker._image_by_page[2][0]["ocr_text"]

    def test_extraction_dict_takes_priority_over_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            file_inv = [make_image_data(1, ocr_text="from file")]
            path = pathlib.Path(tmp) / "image_inventory.json"
            path.write_text(json.dumps(file_inv), encoding="utf-8")
            dict_inv = [make_image_data(1, ocr_text="from dict")]
            chunker = make_chunker(image_inventory=dict_inv, output_dir=tmp)
            assert chunker._image_by_page[1][0]["ocr_text"] == "from dict"

    def test_multiple_images_same_page_all_stored(self):
        imgs = [
            make_image_data(3, ocr_text="Fig 1"),
            make_image_data(3, ocr_text="Fig 2"),
        ]
        chunker = make_chunker(image_inventory=imgs)
        assert len(chunker._image_by_page[3]) == 2

    def test_page_no_as_string_normalised_to_int(self):
        img = {"page_no": "4", "ocr_text": "str page key", "caption": "", "saved_path": ""}
        chunker = make_chunker(image_inventory=[img])
        assert 4 in chunker._image_by_page

    def test_missing_page_no_skipped(self):
        img = {"ocr_text": "no page", "caption": "", "saved_path": ""}
        chunker = make_chunker(image_inventory=[img])
        assert chunker._image_by_page == {}


# ---------------------------------------------------------------------------
# _build_image_chunk
# ---------------------------------------------------------------------------

class TestBuildImageChunk:

    def setup_method(self):
        self.chunker = make_chunker()

    def test_ocr_text_becomes_chunk_text(self):
        img = make_image_data(1, ocr_text="Treatment pathway for malaria.")
        chunk = self.chunker._build_image_chunk(1, img)
        assert "Treatment pathway for malaria" in chunk["text"]

    def test_caption_prepended_as_label(self):
        img = make_image_data(1, ocr_text="Steps A B C", caption="Figure 2")
        chunk = self.chunker._build_image_chunk(1, img)
        assert "[Image caption: Figure 2]" in chunk["text"]
        assert "Steps A B C" in chunk["text"]

    def test_content_type_image_ocr_when_text_present(self):
        img = make_image_data(1, ocr_text="Some OCR text")
        chunk = self.chunker._build_image_chunk(1, img)
        assert chunk["content_type"] == "image_ocr"

    def test_content_type_image_placeholder_when_no_text(self):
        img = make_image_data(1, ocr_text="", caption="")
        chunk = self.chunker._build_image_chunk(1, img)
        assert chunk["content_type"] == "image_placeholder"
        assert chunk["text"] == "<!-- image -->"

    def test_caption_only_is_image_ocr(self):
        img = make_image_data(1, ocr_text="", caption="Figure 1: Malaria pathway")
        chunk = self.chunker._build_image_chunk(1, img)
        assert chunk["content_type"] == "image_ocr"

    def test_image_path_stored(self):
        img = make_image_data(1, ocr_text="x", saved_path="/out/img_001.png")
        chunk = self.chunker._build_image_chunk(1, img)
        assert chunk["image_path"] == "/out/img_001.png"

    def test_page_number_stored(self):
        img = make_image_data(7, ocr_text="content")
        chunk = self.chunker._build_image_chunk(7, img)
        assert chunk["page"] == 7

    def test_preservation_level_is_standard(self):
        img = make_image_data(1, ocr_text="content")
        chunk = self.chunker._build_image_chunk(1, img)
        assert chunk["preservation_level"] == PreservationLevel.STANDARD.value

    def test_chunk_id_prefix(self):
        img = make_image_data(1, ocr_text="content")
        chunk = self.chunker._build_image_chunk(1, img)
        assert chunk["chunk_id"].startswith("chunk_image_")

    def test_clinical_metadata_present_when_ocr(self):
        img = make_image_data(1, ocr_text="Manage at HC III. Danger signs: fever.")
        chunk = self.chunker._build_image_chunk(1, img)
        assert "clinical_metadata" in chunk
        assert set(chunk["clinical_metadata"].keys()) == set(
            SmartChunker._empty_clinical_metadata().keys()
        )

    def test_clinical_metadata_empty_when_placeholder(self):
        img = make_image_data(1, ocr_text="", caption="")
        chunk = self.chunker._build_image_chunk(1, img)
        assert chunk["clinical_metadata"] == SmartChunker._empty_clinical_metadata()

    def test_ocr_clinical_metadata_populated(self):
        img = make_image_data(1, ocr_text="Danger signs: convulsions, cannot drink.")
        chunk = self.chunker._build_image_chunk(1, img)
        assert len(chunk["clinical_metadata"]["danger_signs"]) >= 1

    def test_tables_is_empty_list(self):
        img = make_image_data(1, ocr_text="x")
        chunk = self.chunker._build_image_chunk(1, img)
        assert chunk["tables"] == []

    def test_has_tables_is_false(self):
        img = make_image_data(1, ocr_text="x")
        chunk = self.chunker._build_image_chunk(1, img)
        assert chunk["has_tables"] is False


# ---------------------------------------------------------------------------
# chunk_by_headings — integration
# ---------------------------------------------------------------------------

class TestChunkByHeadingsImages:

    def test_image_chunk_produced_for_page_with_image(self):
        extraction = make_extraction(
            pages=[make_page(1)],
            image_inventory=[make_image_data(1, ocr_text="Clinical flowchart text")],
        )
        chunker = SmartChunker(extraction, make_config())
        chunks = chunker.chunk_by_headings()
        image_chunks = [c for c in chunks if c.get("content_type") in ("image_ocr", "image_placeholder")]
        assert len(image_chunks) == 1

    def test_no_image_chunks_when_no_inventory(self):
        extraction = make_extraction(pages=[make_page(1)])
        chunker = SmartChunker(extraction, make_config())
        chunks = chunker.chunk_by_headings()
        image_chunks = [c for c in chunks if c.get("content_type") in ("image_ocr", "image_placeholder")]
        assert len(image_chunks) == 0

    def test_two_images_same_page_produce_two_chunks(self):
        imgs = [
            make_image_data(1, ocr_text="Fig 1 text"),
            make_image_data(1, ocr_text="Fig 2 text"),
        ]
        extraction = make_extraction(pages=[make_page(1)], image_inventory=imgs)
        chunker = SmartChunker(extraction, make_config())
        chunks = chunker.chunk_by_headings()
        image_chunks = [c for c in chunks if "content_type" in c]
        assert len(image_chunks) == 2

    def test_image_on_different_page_not_included_for_other_page(self):
        imgs = [make_image_data(2, ocr_text="Page 2 image")]
        extraction = make_extraction(
            pages=[make_page(1), make_page(2)],
            image_inventory=imgs,
        )
        chunker = SmartChunker(extraction, make_config())
        chunks = chunker.chunk_by_headings()
        img_chunks = [c for c in chunks if "content_type" in c]
        assert len(img_chunks) == 1
        assert img_chunks[0]["page"] == 2

    def test_image_chunk_has_all_required_fields(self):
        imgs = [make_image_data(1, ocr_text="Some text", caption="Fig 1")]
        extraction = make_extraction(pages=[make_page(1)], image_inventory=imgs)
        chunker = SmartChunker(extraction, make_config())
        chunks = chunker.chunk_by_headings()
        img_chunk = next(c for c in chunks if "content_type" in c)
        for field in ("chunk_id", "page", "text", "tables", "clinical_metadata",
                      "preservation_level", "section_type", "content_type", "image_path"):
            assert field in img_chunk, f"Missing field: {field}"

    def test_placeholder_image_has_empty_clinical_metadata(self):
        imgs = [make_image_data(1, ocr_text="", caption="")]
        extraction = make_extraction(pages=[make_page(1)], image_inventory=imgs)
        chunker = SmartChunker(extraction, make_config())
        chunks = chunker.chunk_by_headings()
        img_chunk = next(c for c in chunks if "content_type" in c)
        assert img_chunk["content_type"] == "image_placeholder"
        assert img_chunk["clinical_metadata"] == SmartChunker._empty_clinical_metadata()
