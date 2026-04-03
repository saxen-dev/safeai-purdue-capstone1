"""
Unit tests for SmartChunker parent-child chunking (P10).

Tests cover:
  - Module-level helpers: _estimate_tokens, _split_recursive_paragraph, _decompose_propositions
  - SmartChunker._build_contextual_header
  - SmartChunker.create_child_chunks (routing, field presence, NLL children)
  - HybridRetriever._chunk_text with contextual_content

Run with:  python3 -m pytest tests/test_parent_child_chunking.py -v
"""

import pytest
from pipeline.chunker import (
    SmartChunker,
    _estimate_tokens,
    _split_recursive_paragraph,
    _decompose_propositions,
    _CHILD_MAX_TOKENS,
    _CHILD_MIN_TOKENS,
)
from pipeline.config import ExtractionConfig, PreservationLevel
from pipeline.retriever import HybridRetriever


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


def make_chunker(chunks):
    extraction = {"pages": [], "tables": []}
    c = SmartChunker(extraction, make_config())
    c.chunks = list(chunks)
    return c


def narrative_chunk(chunk_id, text, preservation=PreservationLevel.STANDARD.value,
                    heading="Malaria Treatment", page=1):
    return {
        "chunk_id": chunk_id,
        "text": text,
        "page": page,
        "heading": heading,
        "section_type": "treatment",
        "preservation_level": preservation,
        "tables": [],
        "has_tables": False,
        "is_table_only": False,
        "content_type": None,
        "image_path": "",
        "clinical_metadata": {
            "condition": "malaria",
            "drug_name": "artemether",
            "dosage_summary": None,
            "patient_weight_min_kg": None,
            "patient_weight_max_kg": None,
            "patient_age_min": None,
            "patient_age_max": None,
            "route": None,
            "frequency": None,
            "duration": None,
            "contraindications": [],
            "special_populations": [],
            "level_of_care": [],
            "clinical_features": [],
            "danger_signs": [],
            "referral_criteria": [],
            "clinical_section_type": "treatment",
        },
        "related_chunk_ids": [],
        "related_chunks": {},
    }


def table_chunk(chunk_id, text="| Weight | Dose |\n|---|---|\n| 5-9 kg | 20 mg |",
                nll="IF weight 5-9 kg, THEN artemether 20 mg.", heading="AL Dosing",
                section_type="table"):
    base = narrative_chunk(chunk_id, text, PreservationLevel.VERBATIM.value, heading)
    base["is_table_only"] = True
    base["section_type"] = section_type
    base["tables"] = [{"nll": nll, "classification": "dosing"}]
    base["has_tables"] = True
    return base


def image_chunk(chunk_id, content_type="image_ocr",
                text="Clinical flowchart text.", heading="Figure 1"):
    base = narrative_chunk(chunk_id, text, PreservationLevel.STANDARD.value, heading)
    base["content_type"] = content_type
    base["image_path"] = "/img/fig1.png"
    return base


# ---------------------------------------------------------------------------
# _estimate_tokens
# ---------------------------------------------------------------------------

class TestEstimateTokens:

    def test_empty_string(self):
        assert _estimate_tokens("") == 0

    def test_single_word(self):
        assert _estimate_tokens("hello") == int(1 * 1.3)

    def test_ten_words(self):
        text = "one two three four five six seven eight nine ten"
        assert _estimate_tokens(text) == int(10 * 1.3)

    def test_proportional(self):
        t20 = _estimate_tokens(" ".join(["word"] * 20))
        t10 = _estimate_tokens(" ".join(["word"] * 10))
        assert t20 == 2 * t10


# ---------------------------------------------------------------------------
# _split_recursive_paragraph
# ---------------------------------------------------------------------------

class TestSplitRecursiveParagraph:

    def _long_text(self, n_paragraphs=6, words_per_para=120):
        paras = [" ".join([f"word{i}" for i in range(words_per_para)])]
        return "\n\n".join(paras * n_paragraphs)

    def test_short_text_returned_as_single_chunk(self):
        text = "Short paragraph."
        chunks = _split_recursive_paragraph(text, max_tokens=512)
        assert len(chunks) == 1
        assert chunks[0].strip() == text.strip()

    def test_long_text_split_into_multiple_chunks(self):
        text = self._long_text(4, 100)
        chunks = _split_recursive_paragraph(text, max_tokens=100)
        assert len(chunks) > 1

    def test_each_chunk_within_token_budget(self):
        # Use text with real sentence breaks so the sentence-splitting path fires.
        sentences = [f"Sentence {i} contains some words about malaria treatment." for i in range(30)]
        text = " ".join(sentences)
        budget = 100
        chunks = _split_recursive_paragraph(text, max_tokens=budget, overlap_tokens=0)
        for c in chunks:
            # With overlap=0, each chunk should not exceed budget by much.
            assert _estimate_tokens(c) <= budget + 30

    def test_empty_string_returns_single_empty(self):
        chunks = _split_recursive_paragraph("", max_tokens=512)
        assert len(chunks) >= 1

    def test_overlap_prefix_present_in_second_chunk(self):
        # Use two long paragraphs so they split
        para = " ".join(["alpha"] * 60 + ["beta"] * 60)
        text = para + "\n\n" + para
        chunks = _split_recursive_paragraph(text, max_tokens=80, overlap_tokens=20)
        if len(chunks) > 1:
            # Second chunk should start with words from first chunk's tail
            first_words = set(chunks[0].split()[-15:])
            second_start = set(chunks[1].split()[:15])
            assert first_words & second_start  # overlap exists


# ---------------------------------------------------------------------------
# _decompose_propositions
# ---------------------------------------------------------------------------

class TestDecomposePropositions:

    def test_single_short_sentence_unchanged(self):
        text = "Give artemether 20 mg twice daily."
        props = _decompose_propositions(text, max_tokens=200)
        assert len(props) >= 1
        assert "artemether" in props[0]

    def test_long_text_split_into_multiple_propositions(self):
        sentences = [f"Sentence {i} with some clinical content." for i in range(20)]
        text = " ".join(sentences)
        props = _decompose_propositions(text, max_tokens=50)
        assert len(props) > 1

    def test_each_proposition_within_budget(self):
        sentences = [f"Sentence {i} repeating words." for i in range(30)]
        text = " ".join(sentences)
        props = _decompose_propositions(text, max_tokens=100)
        for p in props:
            assert _estimate_tokens(p) <= 100 + 50  # allow small overage for merging

    def test_empty_string_returns_single_element(self):
        props = _decompose_propositions("")
        assert len(props) >= 1


# ---------------------------------------------------------------------------
# _build_contextual_header
# ---------------------------------------------------------------------------

class TestBuildContextualHeader:

    def test_heading_included(self):
        chunk = narrative_chunk("c1", "text", heading="AL Dosing")
        header = SmartChunker._build_contextual_header(chunk, "Uganda Guidelines")
        assert "AL Dosing" in header

    def test_condition_included_when_different_from_heading(self):
        chunk = narrative_chunk("c1", "text", heading="Treatment")
        header = SmartChunker._build_contextual_header(chunk)
        assert "malaria" in header

    def test_drug_name_included(self):
        chunk = narrative_chunk("c1", "text")
        header = SmartChunker._build_contextual_header(chunk)
        assert "artemether" in header

    def test_doc_title_included(self):
        chunk = narrative_chunk("c1", "text", page=5)
        header = SmartChunker._build_contextual_header(chunk, "Uganda Clinical 2023")
        assert "Uganda Clinical 2023" in header

    def test_page_number_included(self):
        chunk = narrative_chunk("c1", "text", page=42)
        header = SmartChunker._build_contextual_header(chunk)
        assert "42" in header

    def test_wrapped_in_context_tag(self):
        chunk = narrative_chunk("c1", "text")
        header = SmartChunker._build_contextual_header(chunk)
        assert header.startswith("[Context:")

    def test_empty_chunk_returns_empty_string(self):
        chunk = {"chunk_id": "c1", "text": "", "heading": "", "page": None,
                 "clinical_metadata": {}}
        header = SmartChunker._build_contextual_header(chunk)
        assert header == ""


# ---------------------------------------------------------------------------
# create_child_chunks — routing
# ---------------------------------------------------------------------------

class TestCreateChildChunksRouting:

    def test_narrative_standard_produces_children(self):
        c = make_chunker([narrative_chunk("p1", "Give the drug once daily for three days.")])
        children = c.create_child_chunks()
        assert len(children) >= 1

    def test_narrative_verbatim_uses_propositions(self):
        # 60 sentences × ~7 tokens each ≈ 420 tokens total, well above the
        # 200-token proposition cap → must produce multiple children.
        sentences = [f"Danger sign {i}: refer the patient immediately to hospital." for i in range(60)]
        text = " ".join(sentences)
        chunk = narrative_chunk("p1", text, PreservationLevel.VERBATIM.value)
        c = make_chunker([chunk])
        children = c.create_child_chunks()
        assert len(children) >= 2

    def test_narrative_high_passthrough_short(self):
        chunk = narrative_chunk("p1", "Short high-preservation text.", PreservationLevel.HIGH.value)
        c = make_chunker([chunk])
        children = c.create_child_chunks()
        assert len(children) == 1

    def test_table_chunk_produces_atomic_child(self):
        c = make_chunker([table_chunk("p1")])
        children = c.create_child_chunks()
        table_children = [ch for ch in children if not ch["is_nll"]]
        assert len(table_children) >= 1

    def test_dosing_table_produces_nll_child(self):
        c = make_chunker([table_chunk("p1")])
        children = c.create_child_chunks()
        nll_children = [ch for ch in children if ch["is_nll"]]
        assert len(nll_children) == 1

    def test_nll_child_contains_nll_text(self):
        c = make_chunker([table_chunk("p1", nll="IF weight 5 kg, THEN 20 mg.")])
        children = c.create_child_chunks()
        nll_child = next(ch for ch in children if ch["is_nll"])
        assert "20 mg" in nll_child["text"]

    def test_image_placeholder_skipped(self):
        c = make_chunker([image_chunk("p1", content_type="image_placeholder")])
        children = c.create_child_chunks()
        assert len(children) == 0

    def test_image_ocr_produces_one_child(self):
        # Text must be ≥ _CHILD_MIN_TOKENS (50 tokens ≈ 39 words) to pass the filter.
        long_text = " ".join(["malaria flowchart treatment pathway step"] * 10)
        c = make_chunker([image_chunk("p1", content_type="image_ocr", text=long_text)])
        children = c.create_child_chunks()
        assert len(children) == 1

    def test_empty_parent_list_returns_empty(self):
        c = make_chunker([])
        children = c.create_child_chunks()
        assert children == []


# ---------------------------------------------------------------------------
# create_child_chunks — field schema
# ---------------------------------------------------------------------------

class TestCreateChildChunksFields:

    REQUIRED = (
        "chunk_id", "parent_chunk_id", "text", "contextual_content",
        "page", "heading", "section_type", "preservation_level",
        "tables", "has_tables", "is_nll", "clinical_metadata",
        "related_chunk_ids", "word_count", "char_count",
    )

    def _first_child(self):
        c = make_chunker([narrative_chunk("p1", "Give medicine once daily.", page=7)])
        return c.create_child_chunks()[0]

    def test_all_required_fields_present(self):
        child = self._first_child()
        for field in self.REQUIRED:
            assert field in child, f"Missing field: {field}"

    def test_parent_chunk_id_matches_parent(self):
        child = self._first_child()
        assert child["parent_chunk_id"] == "p1"

    def test_chunk_id_starts_with_child_prefix(self):
        child = self._first_child()
        assert child["chunk_id"].startswith("child_p1_")

    def test_contextual_content_contains_text(self):
        child = self._first_child()
        assert "once daily" in child["contextual_content"]

    def test_contextual_content_contains_header(self):
        c = make_chunker([narrative_chunk("p1", "text", page=7)])
        child = c.create_child_chunks("Uganda Handbook")[0]
        assert "Uganda Handbook" in child["contextual_content"]

    def test_page_inherited_from_parent(self):
        child = self._first_child()
        assert child["page"] == 7

    def test_tables_is_empty_list(self):
        child = self._first_child()
        assert child["tables"] == []

    def test_has_tables_is_false(self):
        child = self._first_child()
        assert child["has_tables"] is False

    def test_clinical_metadata_inherited(self):
        child = self._first_child()
        assert child["clinical_metadata"]["condition"] == "malaria"

    def test_word_count_matches_text(self):
        child = self._first_child()
        assert child["word_count"] == len(child["text"].split())


# ---------------------------------------------------------------------------
# create_child_chunks — self.children populated
# ---------------------------------------------------------------------------

class TestChildrenProperty:

    def test_self_children_populated_after_create(self):
        c = make_chunker([narrative_chunk("p1", "Some text here.")])
        c.create_child_chunks()
        assert len(c.children) >= 1

    def test_self_children_same_as_return_value(self):
        c = make_chunker([narrative_chunk("p1", "text")])
        returned = c.create_child_chunks()
        assert c.children is returned


# ---------------------------------------------------------------------------
# HybridRetriever._chunk_text with contextual_content
# ---------------------------------------------------------------------------

class TestRetrieverChunkText:

    def test_contextual_content_preferred_over_text(self):
        chunk = {
            "chunk_id": "c1",
            "text": "raw text only",
            "contextual_content": "[Context: ...]\n\nfull enriched content",
            "tables": [],
        }
        result = HybridRetriever._chunk_text(chunk)
        assert "enriched content" in result
        assert "raw text only" not in result

    def test_falls_back_to_text_when_no_contextual_content(self):
        chunk = {
            "chunk_id": "c1",
            "text": "fallback text",
            "tables": [],
        }
        result = HybridRetriever._chunk_text(chunk)
        assert "fallback text" in result

    def test_empty_contextual_content_falls_back_to_text(self):
        chunk = {
            "chunk_id": "c1",
            "text": "plain text",
            "contextual_content": "",
            "tables": [],
        }
        result = HybridRetriever._chunk_text(chunk)
        assert "plain text" in result
