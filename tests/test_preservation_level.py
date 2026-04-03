"""
Unit tests for PreservationLevel wiring in VHTResponseFormatter.

Run with:  python3 -m pytest tests/test_preservation_level.py -v
"""

import pytest
from pipeline.config import MedicalSource, PreservationLevel, TriageLevel
from pipeline.response import (
    ResponseContent,
    ResponseFormat,
    ResponseOrchestrator,
    VHTResponseFormatter,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_content(citations=None):
    return ResponseContent(
        query="What is the AL dose for a 5 kg child?",
        triage=TriageLevel.GREEN,
        triage_reasons=["Routine"],
        actions=["Check weight"],
        monitoring=[],
        referral_criteria=[],
        citations=citations or [],
    )


def make_chunk(page, heading, preservation_level, text="", nll="", tables=None):
    return {
        "page": page,
        "heading": heading,
        "preservation_level": preservation_level,
        "text": text,
        "tables": tables or (
            [{"nll": nll, "classification": "dosing"}] if nll else []
        ),
    }


def make_orchestrator():
    return ResponseOrchestrator()


# ---------------------------------------------------------------------------
# _build_citations — preservation_level forwarded
# ---------------------------------------------------------------------------

class TestBuildCitations:

    def test_verbatim_level_forwarded(self):
        orch = make_orchestrator()
        chunk = make_chunk(1, "AL Dosing", PreservationLevel.VERBATIM.value)
        cits = orch._build_citations([chunk], MedicalSource.UGANDA_CLINICAL_2023)
        assert cits[0]["preservation_level"] == PreservationLevel.VERBATIM.value

    def test_high_level_forwarded(self):
        orch = make_orchestrator()
        chunk = make_chunk(2, "Management Steps", PreservationLevel.HIGH.value)
        cits = orch._build_citations([chunk], MedicalSource.UGANDA_CLINICAL_2023)
        assert cits[0]["preservation_level"] == PreservationLevel.HIGH.value

    def test_standard_level_forwarded(self):
        orch = make_orchestrator()
        chunk = make_chunk(3, "Background", PreservationLevel.STANDARD.value)
        cits = orch._build_citations([chunk], MedicalSource.UGANDA_CLINICAL_2023)
        assert cits[0]["preservation_level"] == PreservationLevel.STANDARD.value

    def test_missing_preservation_level_defaults_to_standard(self):
        orch = make_orchestrator()
        chunk = {"page": 4, "heading": "Intro"}
        cits = orch._build_citations([chunk], MedicalSource.UGANDA_CLINICAL_2023)
        assert cits[0]["preservation_level"] == PreservationLevel.STANDARD.value

    def test_nll_from_tables_collected(self):
        orch = make_orchestrator()
        chunk = make_chunk(
            1, "AL Dosing", PreservationLevel.VERBATIM.value,
            nll="IF weight 5-9 kg, THEN artemether 20 mg.",
        )
        cits = orch._build_citations([chunk], MedicalSource.UGANDA_CLINICAL_2023)
        assert "artemether" in cits[0]["nll"]

    def test_no_nll_when_tables_empty(self):
        orch = make_orchestrator()
        chunk = make_chunk(1, "Background", PreservationLevel.STANDARD.value, text="Context text.")
        cits = orch._build_citations([chunk], MedicalSource.UGANDA_CLINICAL_2023)
        assert cits[0]["nll"] == ""

    def test_text_forwarded(self):
        orch = make_orchestrator()
        chunk = make_chunk(1, "Management", PreservationLevel.HIGH.value, text="Give IV artesunate.")
        cits = orch._build_citations([chunk], MedicalSource.UGANDA_CLINICAL_2023)
        assert cits[0]["text"] == "Give IV artesunate."

    def test_enum_instance_as_preservation_level_normalised(self):
        """Chunks could carry the enum instance rather than its string value."""
        orch = make_orchestrator()
        chunk = {
            "page": 1,
            "heading": "Dosing",
            "preservation_level": PreservationLevel.VERBATIM,  # enum instance
            "text": "",
            "tables": [],
        }
        cits = orch._build_citations([chunk], MedicalSource.UGANDA_CLINICAL_2023)
        assert cits[0]["preservation_level"] == PreservationLevel.VERBATIM.value


# ---------------------------------------------------------------------------
# _dosing_block
# ---------------------------------------------------------------------------

class TestDosingBlock:
    fmt = VHTResponseFormatter()

    def _verbatim_citation(self, nll="", text=""):
        return {
            "source": MedicalSource.UGANDA_CLINICAL_2023,
            "page": 1,
            "section": "AL Dosing",
            "preservation_level": PreservationLevel.VERBATIM.value,
            "nll": nll,
            "text": text,
        }

    def _standard_citation(self):
        return {
            "source": MedicalSource.UGANDA_CLINICAL_2023,
            "page": 2,
            "section": "Background",
            "preservation_level": PreservationLevel.STANDARD.value,
            "nll": "",
            "text": "Some context.",
        }

    def test_no_verbatim_returns_empty_string(self):
        result = self.fmt._dosing_block([self._standard_citation()])
        assert result == ""

    def test_verbatim_with_nll_shows_nll_text(self):
        nll = "IF weight 5-9 kg, THEN artemether 20 mg."
        result = self.fmt._dosing_block([self._verbatim_citation(nll=nll)])
        assert "artemether 20 mg" in result

    def test_verbatim_without_nll_falls_back_to_text(self):
        result = self.fmt._dosing_block([self._verbatim_citation(text="Dose: 20 mg artemether.")])
        assert "20 mg artemether" in result

    def test_header_included(self):
        result = self.fmt._dosing_block([self._verbatim_citation(nll="IF x, THEN y.")])
        assert "EXACT DOSING" in result

    def test_max_two_verbatim_chunks_shown(self):
        citations = [
            self._verbatim_citation(nll=f"NLL sentence {i}.") for i in range(5)
        ]
        result = self.fmt._dosing_block(citations)
        # Only two should appear
        assert result.count("NLL sentence") == 2

    def test_empty_citations_returns_empty(self):
        assert self.fmt._dosing_block([]) == ""

    def test_verbatim_with_no_content_returns_header_only(self):
        result = self.fmt._dosing_block([self._verbatim_citation()])
        # No actual dosing text to show, but also no crash
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# _citations_section — labels based on preservation level
# ---------------------------------------------------------------------------

class TestCitationsSection:
    fmt = VHTResponseFormatter()

    def _citation(self, level, section="Dosing"):
        return {
            "source": MedicalSource.UGANDA_CLINICAL_2023,
            "page": 10,
            "section": section,
            "preservation_level": level,
            "nll": "",
            "text": "",
        }

    def test_verbatim_citation_labelled(self):
        result = self.fmt._citations_section([self._citation(PreservationLevel.VERBATIM.value)])
        assert "[EXACT DOSING]" in result

    def test_high_citation_labelled(self):
        result = self.fmt._citations_section([self._citation(PreservationLevel.HIGH.value)])
        assert "[HIGH FIDELITY]" in result

    def test_standard_citation_no_label(self):
        result = self.fmt._citations_section([self._citation(PreservationLevel.STANDARD.value)])
        assert "[EXACT DOSING]" not in result
        assert "[HIGH FIDELITY]" not in result

    def test_missing_level_no_label(self):
        citation = {"source": MedicalSource.UGANDA_CLINICAL_2023, "page": 5, "section": "Intro"}
        result = self.fmt._citations_section([citation])
        assert "[EXACT DOSING]" not in result
        assert "[HIGH FIDELITY]" not in result

    def test_section_and_label_both_present(self):
        result = self.fmt._citations_section([self._citation(PreservationLevel.VERBATIM.value, section="AL Dosing")])
        assert "AL Dosing" in result
        assert "[EXACT DOSING]" in result

    def test_empty_citations_returns_fallback(self):
        result = self.fmt._citations_section([])
        assert "Refer to national" in result


# ---------------------------------------------------------------------------
# _format_standard — dosing block injected when verbatim chunks present
# ---------------------------------------------------------------------------

class TestFormatStandardDosingBlock:
    fmt = VHTResponseFormatter()

    def _make_content_with_level(self, level, nll="IF weight 5 kg, THEN AL 20 mg."):
        citations = [{
            "source": MedicalSource.UGANDA_CLINICAL_2023,
            "page": 1,
            "section": "AL Dosing",
            "preservation_level": level,
            "nll": nll if level == PreservationLevel.VERBATIM.value else "",
            "text": "",
        }]
        return make_content(citations=citations)

    def test_verbatim_chunk_injects_dosing_block(self):
        content = self._make_content_with_level(PreservationLevel.VERBATIM.value)
        output = self.fmt._format_standard(content)
        assert "EXACT DOSING" in output

    def test_standard_chunk_no_dosing_block(self):
        content = self._make_content_with_level(PreservationLevel.STANDARD.value)
        output = self.fmt._format_standard(content)
        assert "EXACT DOSING" not in output

    def test_high_chunk_no_dosing_block(self):
        content = self._make_content_with_level(PreservationLevel.HIGH.value)
        output = self.fmt._format_standard(content)
        assert "EXACT DOSING" not in output

    def test_nll_text_appears_in_output(self):
        content = self._make_content_with_level(PreservationLevel.VERBATIM.value)
        output = self.fmt._format_standard(content)
        assert "IF weight 5 kg, THEN AL 20 mg." in output

    def test_dosing_block_appears_before_citations_section(self):
        content = self._make_content_with_level(PreservationLevel.VERBATIM.value)
        output = self.fmt._format_standard(content)
        dosing_pos = output.find("EXACT DOSING")
        citations_pos = output.find("FROM THE GUIDELINES")
        assert dosing_pos < citations_pos
