"""
Unit tests for the Stage 4b ClinicalVerifier (P11).

Tests cover:
  - _infer_chunk_type, _get_nll, _get_source_pages
  - compute_audit_hash, compute_content_hash, compute_digital_signature
  - classify_chunk_tier
  - determine_applicable_checks
  - create_review_item
  - assemble_review_package
  - validate_completed_review
  - apply_reviews_to_chunks
  - passes_deployment_gate
  - ClinicalVerifier.generate (no file I/O)
  - ClinicalVerifier.deployment_gate_check

Run with:  python3 -m pytest tests/test_clinical_verifier.py -v
"""

import json
import pytest
from pipeline.clinical_verifier import (
    CHECK_DEFINITIONS,
    MANDATORY_TIERS,
    ClinicalVerifier,
    _infer_chunk_type,
    _get_nll,
    _get_source_pages,
    _get_preservation_level,
    apply_reviews_to_chunks,
    assemble_review_package,
    classify_chunk_tier,
    compute_audit_hash,
    compute_content_hash,
    compute_digital_signature,
    create_review_item,
    determine_applicable_checks,
    passes_deployment_gate,
    triage_all_chunks,
    validate_completed_review,
)


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

def _narrative(chunk_id="c1", text="General malaria information.",
               preservation="standard", heading="Background", page=5,
               condition="malaria", drug_name="artemether"):
    return {
        "chunk_id": chunk_id,
        "text": text,
        "page": page,
        "heading": heading,
        "section_type": "background",
        "preservation_level": preservation,
        "is_table_only": False,
        "content_type": None,
        "tables": [],
        "has_tables": False,
        "clinical_metadata": {
            "condition": condition,
            "drug_name": drug_name,
            "patient_weight_min_kg": None,
            "patient_weight_max_kg": None,
            "contraindications": [],
            "special_populations": [],
            "level_of_care": [],
            "danger_signs": [],
        },
        "related_chunks": {},
    }


def _dosing_table(chunk_id="t1", nll="IF weight 5-9 kg, THEN 20 mg.",
                  validated=False):
    base = _narrative(chunk_id, "| Weight | Dose |\n|---|---|\n| 5-9 kg | 20 mg |",
                      preservation="verbatim", heading="AL Dosing", page=12)
    base["is_table_only"] = True
    base["section_type"] = "dosing"
    base["tables"] = [{"nll": nll, "classification": "dosing"}]
    base["has_tables"] = True
    if validated:
        base["validation"] = {"status": "pass", "checks_passed": 6, "checks_total": 6}
    return base


def _clinical_table(chunk_id="ct1"):
    base = _narrative(chunk_id, "Clinical management data", heading="Clinical Mgt", page=20)
    base["is_table_only"] = True
    base["section_type"] = "clinical_management"
    base["tables"] = [{"nll": None, "classification": "clinical_management"}]
    base["has_tables"] = True
    return base


def _image_chunk(chunk_id="img1", content_type="image_ocr"):
    base = _narrative(chunk_id, "Flowchart text.", heading="Figure 1", page=7)
    base["content_type"] = content_type
    return base


def _make_review_item(chunk_id="c1", tier=3, decision="approved"):
    return {
        "chunk_id": chunk_id,
        "review_tier": tier,
        "audit_hash": compute_audit_hash("| Weight | Dose |"),
        "applicable_checks": {
            k: {"applicable": True, "guidance": "check it"} for k in CHECK_DEFINITIONS
        },
        "review": {
            "overall_decision": decision,
            "corrections": None,
            "reviewer_name": "Dr. Smith",
            "reviewer_role": "Physician",
            "institution": "IDI",
            "reviewed_at": "2026-04-03T10:00:00Z",
            "digital_signature": None,
            "checks": {k: {"status": "pass", "notes": None} for k in CHECK_DEFINITIONS},
        },
    }


# ---------------------------------------------------------------------------
# _infer_chunk_type
# ---------------------------------------------------------------------------

class TestInferChunkType:

    def test_narrative_returns_narrative(self):
        assert _infer_chunk_type(_narrative()) == "narrative"

    def test_image_ocr_returns_image(self):
        assert _infer_chunk_type(_image_chunk("i1", "image_ocr")) == "image"

    def test_image_placeholder_returns_image(self):
        assert _infer_chunk_type(_image_chunk("i1", "image_placeholder")) == "image"

    def test_dosing_section_type_returns_dosing_table(self):
        assert _infer_chunk_type(_dosing_table()) == "dosing_table"

    def test_dosing_classification_fallback(self):
        chunk = _narrative()
        chunk["is_table_only"] = True
        chunk["section_type"] = ""
        chunk["tables"] = [{"classification": "dosing", "nll": ""}]
        assert _infer_chunk_type(chunk) == "dosing_table"

    def test_clinical_management_section_type(self):
        assert _infer_chunk_type(_clinical_table()) == "clinical_table"

    def test_evidence_classification(self):
        chunk = _narrative()
        chunk["is_table_only"] = True
        chunk["section_type"] = ""
        chunk["tables"] = [{"classification": "evidence", "nll": ""}]
        assert _infer_chunk_type(chunk) == "evidence_table"

    def test_unknown_table_returns_other_table(self):
        chunk = _narrative()
        chunk["is_table_only"] = True
        chunk["section_type"] = "unknown"
        chunk["tables"] = []
        assert _infer_chunk_type(chunk) == "other_table"


# ---------------------------------------------------------------------------
# _get_nll
# ---------------------------------------------------------------------------

class TestGetNll:

    def test_returns_first_nll(self):
        chunk = _dosing_table(nll="IF 5 kg THEN 20 mg.")
        assert _get_nll(chunk) == "IF 5 kg THEN 20 mg."

    def test_returns_none_when_no_tables(self):
        assert _get_nll(_narrative()) is None

    def test_returns_none_when_nll_empty(self):
        chunk = _narrative()
        chunk["tables"] = [{"nll": ""}]
        assert _get_nll(chunk) is None

    def test_skips_empty_returns_second(self):
        chunk = _narrative()
        chunk["tables"] = [{"nll": ""}, {"nll": "IF x THEN y"}]
        assert _get_nll(chunk) == "IF x THEN y"


# ---------------------------------------------------------------------------
# _get_source_pages
# ---------------------------------------------------------------------------

class TestGetSourcePages:

    def test_returns_page_in_list(self):
        assert _get_source_pages(_narrative(page=7)) == [7]

    def test_none_page_returns_empty(self):
        chunk = _narrative()
        chunk["page"] = None
        assert _get_source_pages(chunk) == []

    def test_string_page_converted(self):
        chunk = _narrative()
        chunk["page"] = "12"
        assert _get_source_pages(chunk) == [12]


# ---------------------------------------------------------------------------
# Hash utilities
# ---------------------------------------------------------------------------

class TestHashUtilities:

    def test_audit_hash_deterministic(self):
        h1 = compute_audit_hash("hello world")
        h2 = compute_audit_hash("hello world")
        assert h1 == h2

    def test_audit_hash_different_inputs(self):
        assert compute_audit_hash("abc") != compute_audit_hash("xyz")

    def test_audit_hash_hex_length(self):
        assert len(compute_audit_hash("test")) == 64

    def test_content_hash_differs_from_audit_hash(self):
        chunk = _narrative(text="some text")
        assert compute_content_hash(chunk) != compute_audit_hash(chunk["text"])

    def test_digital_signature_deterministic(self):
        sig1 = compute_digital_signature("Dr. A", "IDI", "c1", "abc123", "2026-04-03T10:00:00Z")
        sig2 = compute_digital_signature("Dr. A", "IDI", "c1", "abc123", "2026-04-03T10:00:00Z")
        assert sig1 == sig2

    def test_digital_signature_changes_with_reviewer(self):
        sig1 = compute_digital_signature("Dr. A", "IDI", "c1", "abc", "2026-04-03T10:00:00Z")
        sig2 = compute_digital_signature("Dr. B", "IDI", "c1", "abc", "2026-04-03T10:00:00Z")
        assert sig1 != sig2


# ---------------------------------------------------------------------------
# classify_chunk_tier
# ---------------------------------------------------------------------------

class TestClassifyChunkTier:

    def test_validated_dosing_table_is_tier1(self):
        assert classify_chunk_tier(_dosing_table(validated=True)) == 1

    def test_unvalidated_dosing_table_is_tier2(self):
        assert classify_chunk_tier(_dosing_table(validated=False)) == 2

    def test_clinical_table_is_tier3(self):
        assert classify_chunk_tier(_clinical_table()) == 3

    def test_other_table_with_loc_is_tier3(self):
        chunk = _narrative()
        chunk["is_table_only"] = True
        chunk["section_type"] = "unknown"
        chunk["clinical_metadata"]["level_of_care"] = ["HC3"]
        assert classify_chunk_tier(chunk) == 3

    def test_evidence_table_is_tier4(self):
        chunk = _narrative()
        chunk["is_table_only"] = True
        chunk["section_type"] = ""
        chunk["tables"] = [{"classification": "evidence"}]
        assert classify_chunk_tier(chunk) == 4

    def test_high_narrative_is_tier4(self):
        chunk = _narrative(preservation="high")
        assert classify_chunk_tier(chunk) == 4

    def test_verbatim_narrative_is_tier4(self):
        chunk = _narrative(preservation="verbatim")
        assert classify_chunk_tier(chunk) == 4

    def test_standard_narrative_is_tier5(self):
        chunk = _narrative(preservation="standard")
        assert classify_chunk_tier(chunk) == 5

    def test_image_standard_is_tier5(self):
        chunk = _image_chunk(content_type="image_ocr")
        chunk["preservation_level"] = "standard"
        assert classify_chunk_tier(chunk) == 5


# ---------------------------------------------------------------------------
# determine_applicable_checks
# ---------------------------------------------------------------------------

class TestDetermineApplicableChecks:

    def test_dosing_table_all_applicable(self):
        checks = determine_applicable_checks(_dosing_table())
        for key in CHECK_DEFINITIONS:
            assert checks[key]["applicable"] is True

    def test_narrative_provenance_always_applicable(self):
        checks = determine_applicable_checks(_narrative())
        assert checks["provenance"]["applicable"] is True

    def test_narrative_dosage_conditional_no_keywords(self):
        chunk = _narrative(text="General information about malaria.")
        checks = determine_applicable_checks(chunk)
        assert checks["dosage_accuracy"]["applicable"] is False

    def test_narrative_dosage_conditional_with_keyword(self):
        chunk = _narrative(text="Give 80+480 mg twice daily.")
        checks = determine_applicable_checks(chunk)
        assert checks["dosage_accuracy"]["applicable"] is True

    def test_narrative_contraindications_keyword_match(self):
        chunk = _narrative(text="Do not use in first trimester of pregnancy.")
        checks = determine_applicable_checks(chunk)
        assert checks["contraindications"]["applicable"] is True

    def test_all_checks_have_guidance(self):
        checks = determine_applicable_checks(_dosing_table())
        for key, info in checks.items():
            assert isinstance(info["guidance"], str)
            assert len(info["guidance"]) > 0

    def test_evidence_table_provenance_only(self):
        chunk = _narrative()
        chunk["is_table_only"] = True
        chunk["section_type"] = ""
        chunk["tables"] = [{"classification": "evidence"}]
        checks = determine_applicable_checks(chunk)
        assert checks["provenance"]["applicable"] is True
        assert checks["dosage_accuracy"]["applicable"] is False


# ---------------------------------------------------------------------------
# create_review_item
# ---------------------------------------------------------------------------

class TestCreateReviewItem:

    def _make(self, chunk=None, tier=2):
        chunk = chunk or _dosing_table()
        lookup = {chunk["chunk_id"]: chunk}
        checks = determine_applicable_checks(chunk)
        return create_review_item(chunk, tier, checks, lookup)

    def test_required_fields_present(self):
        item = self._make()
        for field in (
            "chunk_id", "review_priority", "review_tier", "tier_label",
            "preservation_level", "chunk_type", "source_pages", "section_title",
            "content", "audit_hash", "content_hash", "clinical_metadata",
            "validation_summary", "nll", "context", "applicable_checks", "review",
        ):
            assert field in item, f"Missing: {field}"

    def test_audit_hash_matches_content(self):
        chunk = _dosing_table()
        item = self._make(chunk)
        assert item["audit_hash"] == compute_audit_hash(chunk["text"])

    def test_nll_populated_for_dosing_table(self):
        item = self._make(_dosing_table(nll="IF 5 kg THEN 20 mg."))
        assert item["nll"] == "IF 5 kg THEN 20 mg."

    def test_nll_none_for_narrative(self):
        item = self._make(_narrative(), tier=5)
        assert item["nll"] is None

    def test_review_priority_mandatory_for_tier1(self):
        item = self._make(tier=1)
        assert item["review_priority"] == "mandatory"

    def test_review_priority_recommended_for_tier4(self):
        chunk = _narrative(preservation="high")
        item = self._make(chunk, tier=4)
        assert item["review_priority"] == "recommended"

    def test_review_slots_all_none(self):
        item = self._make()
        review = item["review"]
        assert review["overall_decision"] is None
        assert review["reviewer_name"] is None
        for check_review in review["checks"].values():
            assert check_review["status"] is None


# ---------------------------------------------------------------------------
# assemble_review_package
# ---------------------------------------------------------------------------

class TestAssembleReviewPackage:

    def _make_package(self, chunks=None):
        if chunks is None:
            chunks = [_dosing_table("t1"), _dosing_table("t2", validated=True), _clinical_table()]
        chunk_lookup = {c["chunk_id"]: c for c in chunks}
        tier_groups, _ = triage_all_chunks(chunks)
        return assemble_review_package(
            chunks, chunk_lookup, tier_groups, "Uganda 2023", "file.pdf"
        )

    def test_package_has_required_keys(self):
        pkg = self._make_package()
        for key in ("pipeline_version", "source_document", "generated_at",
                    "review_workflow", "summary", "review_items"):
            assert key in pkg

    def test_review_items_excludes_tier5(self):
        chunks = [_narrative(), _dosing_table("t1")]
        pkg = self._make_package(chunks)
        tiers = {item["review_tier"] for item in pkg["review_items"]}
        assert 5 not in tiers

    def test_summary_counts_match_chunks(self):
        chunks = [_dosing_table("t1"), _dosing_table("t2", validated=True), _clinical_table()]
        pkg = self._make_package(chunks)
        assert pkg["summary"]["total_chunks_in_pipeline"] == 3

    def test_source_document_set(self):
        pkg = self._make_package()
        assert pkg["source_document"] == "Uganda 2023"

    def test_safety_rule_in_workflow(self):
        pkg = self._make_package()
        rule = pkg["review_workflow"]["safety_rule"]
        assert "verified_by" in rule and "audit_hash" in rule


# ---------------------------------------------------------------------------
# validate_completed_review
# ---------------------------------------------------------------------------

class TestValidateCompletedReview:

    def _completed(self, items):
        return {"review_items": items}

    def test_valid_approved_review_passes(self):
        chunk = _dosing_table("t1", nll="IF 5 kg THEN 20 mg.")
        item = _make_review_item("t1", tier=2, decision="approved")
        item["audit_hash"] = compute_audit_hash(chunk["text"])
        is_valid, issues, stats = validate_completed_review(
            self._completed([item]), [chunk]
        )
        assert is_valid
        assert stats["approved"] == 1

    def test_mandatory_no_decision_fails(self):
        chunk = _dosing_table("t1")
        item = _make_review_item("t1", tier=2, decision=None)
        is_valid, issues, stats = validate_completed_review(
            self._completed([item]), [chunk]
        )
        assert not is_valid
        assert stats["unreviewed_mandatory"] == 1

    def test_hash_mismatch_fails(self):
        chunk = _dosing_table("t1")
        item = _make_review_item("t1", tier=2, decision="approved")
        item["audit_hash"] = "aaaaaa"  # wrong hash
        is_valid, issues, stats = validate_completed_review(
            self._completed([item]), [chunk]
        )
        assert not is_valid
        assert stats["hash_mismatches"] == 1

    def test_missing_reviewer_name_fails(self):
        chunk = _dosing_table("t1")
        item = _make_review_item("t1", tier=2, decision="approved")
        item["audit_hash"] = compute_audit_hash(chunk["text"])
        item["review"]["reviewer_name"] = None
        is_valid, issues, stats = validate_completed_review(
            self._completed([item]), [chunk]
        )
        assert not is_valid
        assert stats["missing_identity"] == 1

    def test_flagged_without_notes_recorded(self):
        chunk = _dosing_table("t1")
        item = _make_review_item("t1", tier=2, decision="flagged")
        item["audit_hash"] = compute_audit_hash(chunk["text"])
        item["review"]["corrections"] = None
        for k in item["review"]["checks"]:
            item["review"]["checks"][k]["notes"] = None
        _, issues, stats = validate_completed_review(
            self._completed([item]), [chunk]
        )
        assert stats["missing_notes_on_flags"] == 1

    def test_optional_tier_unreviewed_still_valid(self):
        chunk = _narrative("c1")
        item = _make_review_item("c1", tier=5, decision=None)
        is_valid, issues, stats = validate_completed_review(
            self._completed([item]), [chunk]
        )
        assert is_valid


# ---------------------------------------------------------------------------
# apply_reviews_to_chunks
# ---------------------------------------------------------------------------

class TestApplyReviewsToChunks:

    def _apply(self, decision="approved"):
        chunk = _dosing_table("t1", nll="IF x THEN y.")
        item = _make_review_item("t1", tier=2, decision=decision)
        item["audit_hash"] = compute_audit_hash(chunk["text"])
        completed = {"review_items": [item]}
        updated, stats = apply_reviews_to_chunks(completed, [chunk])
        return updated[0], stats

    def test_approved_chunk_gets_verified_status(self):
        chunk, _ = self._apply("approved")
        assert chunk["verified_by"]["status"] == "verified"

    def test_flagged_chunk_gets_flagged_status(self):
        chunk, _ = self._apply("flagged")
        assert chunk["verified_by"]["status"] == "flagged"

    def test_digital_signature_present(self):
        chunk, _ = self._apply()
        assert len(chunk["verified_by"]["digital_signature"]) == 64

    def test_audit_hash_set_on_chunk(self):
        chunk, _ = self._apply()
        assert "audit_hash" in chunk
        assert len(chunk["audit_hash"]) == 64

    def test_clinical_verification_checks_set(self):
        chunk, _ = self._apply()
        assert "clinical_verification_checks" in chunk
        assert set(chunk["clinical_verification_checks"].keys()) == set(CHECK_DEFINITIONS)

    def test_stats_applied_count(self):
        _, stats = self._apply()
        assert stats["applied"] == 1

    def test_unreviewd_chunk_skipped(self):
        chunk1 = _dosing_table("t1")
        chunk2 = _dosing_table("t2")
        item = _make_review_item("t1", tier=2, decision="approved")
        item["audit_hash"] = compute_audit_hash(chunk1["text"])
        completed = {"review_items": [item]}
        updated, stats = apply_reviews_to_chunks(completed, [chunk1, chunk2])
        assert stats["applied"] == 1
        assert stats["skipped"] == 1
        assert "verified_by" not in updated[1]


# ---------------------------------------------------------------------------
# passes_deployment_gate
# ---------------------------------------------------------------------------

class TestPassesDeploymentGate:

    def test_no_chunks_passes(self):
        passes, unverified = passes_deployment_gate([])
        assert passes
        assert unverified == []

    def test_unverified_mandatory_blocks(self):
        chunk = _dosing_table("t1")
        passes, unverified = passes_deployment_gate([chunk])
        assert not passes
        assert "t1" in unverified

    def test_verified_mandatory_passes(self):
        chunk = _dosing_table("t1")
        chunk["verified_by"] = {"status": "verified"}
        chunk["audit_hash"] = compute_audit_hash(chunk["text"])
        passes, unverified = passes_deployment_gate([chunk])
        assert passes
        assert unverified == []

    def test_optional_tier_unverified_still_passes(self):
        chunk = _narrative("c1", preservation="standard")
        # tier 5, no verified_by
        passes, unverified = passes_deployment_gate([chunk])
        assert passes


# ---------------------------------------------------------------------------
# ClinicalVerifier class
# ---------------------------------------------------------------------------

class TestClinicalVerifier:

    def test_generate_returns_package_dict(self):
        chunks = [_dosing_table("t1"), _clinical_table()]
        verifier = ClinicalVerifier(chunks)
        package = verifier.generate()
        assert "review_items" in package
        assert "summary" in package

    def test_generate_sets_doc_title(self):
        verifier = ClinicalVerifier([_dosing_table()])
        package = verifier.generate(doc_title="Uganda 2023")
        assert package["source_document"] == "Uganda 2023"

    def test_deployment_gate_check_static(self):
        chunk = _dosing_table("t1")
        chunk["verified_by"] = {"status": "verified"}
        chunk["audit_hash"] = compute_audit_hash(chunk["text"])
        passes, unverified = ClinicalVerifier.deployment_gate_check([chunk])
        assert passes
