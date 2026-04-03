"""
Stage 4b — Clinical Verification Framework.

Generates a physician review package from Stage 4a chunks so an IDI
physician can verify safety-critical content against the source PDF.

Two modes:
  Generate:  ClinicalVerifier(chunks, config).generate(output_dir)
      → review_package.json
      → physician_review_report.md

  Ingest:    ClinicalVerifier(chunks, config).ingest(completed_review_path, output_dir)
      → validates completed review, computes digital signatures,
        returns chunks updated with verified_by fields.

Safety rule: No content proceeds to Phase B (Deployment) without
a verified_by signature and audit_hash.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MANDATORY_TIERS = [1, 2, 3]
RECOMMENDED_TIERS = [4]
OPTIONAL_TIERS = [5]

DECISIONS = ["approved", "flagged", "corrected"]
CHECK_STATUSES = ["pass", "fail", "not_applicable", "corrected"]

CHECK_DEFINITIONS: Dict[str, Dict[str, Any]] = {
    "dosage_accuracy": {
        "name": "Dosage Accuracy",
        "description": (
            "Dose values match source PDF exactly (e.g., '80+480 mg', '1 tablet')."
        ),
        "check_number": 1,
    },
    "stratification": {
        "name": "Stratification",
        "description": (
            "Age/weight ranges are preserved — no merged or missing rows."
        ),
        "check_number": 2,
    },
    "contraindications": {
        "name": "Contraindications",
        "description": (
            "Warnings are present (e.g., 'Do not use in first trimester')."
        ),
        "check_number": 3,
    },
    "conditional_logic": {
        "name": "Conditional Logic",
        "description": (
            "IF/THEN referral logic is intact "
            "(e.g., NLL dosing rules, danger sign criteria)."
        ),
        "check_number": 4,
    },
    "provenance": {
        "name": "Provenance",
        "description": (
            "Source page number and section citation are correctly cited."
        ),
        "check_number": 5,
    },
}

# Applicability by chunk_type.  True = always applicable, "conditional" = keyword-gated.
CHECK_APPLICABILITY: Dict[str, Dict[str, Any]] = {
    "dosing_table": {
        "dosage_accuracy": True,
        "stratification": True,
        "contraindications": True,
        "conditional_logic": True,
        "provenance": True,
    },
    "clinical_table": {
        "dosage_accuracy": True,
        "stratification": True,
        "contraindications": True,
        "conditional_logic": True,
        "provenance": True,
    },
    "evidence_table": {
        "dosage_accuracy": False,
        "stratification": False,
        "contraindications": False,
        "conditional_logic": False,
        "provenance": True,
    },
    "narrative": {
        "dosage_accuracy": "conditional",
        "stratification": "conditional",
        "contraindications": "conditional",
        "conditional_logic": "conditional",
        "provenance": True,
    },
    "image": {
        "dosage_accuracy": "conditional",
        "stratification": "conditional",
        "contraindications": "conditional",
        "conditional_logic": "conditional",
        "provenance": True,
    },
}

TIER_DEFINITIONS: Dict[int, Dict[str, Any]] = {
    1: {
        "label": "Validated dosing tables",
        "review_requirement": "mandatory",
        "description": (
            "Passed all 6 Stage 3 automated plausibility checks. "
            "Physician confirms extraction accuracy."
        ),
        "est_minutes_per_chunk": 2,
    },
    2: {
        "label": "Unvalidated dosing tables",
        "review_requirement": "mandatory",
        "description": (
            "NOT validated by Stage 3 automated checks "
            "(no weight column or skipped). Extra care required."
        ),
        "est_minutes_per_chunk": 2,
    },
    3: {
        "label": "Clinical management tables",
        "review_requirement": "mandatory",
        "description": (
            "Safety-critical clinical management content. "
            "Full manual review required."
        ),
        "est_minutes_per_chunk": 2,
    },
    4: {
        "label": "Evidence tables + high-priority narratives",
        "review_requirement": "recommended",
        "description": (
            "Contains clinical thresholds, dosing keywords, or "
            "contraindication information."
        ),
        "est_minutes_per_chunk": 0.5,
    },
    5: {
        "label": "Standard chunks",
        "review_requirement": "optional",
        "description": (
            "General narrative, structural tables, images. "
            "No safety-critical content."
        ),
        "est_minutes_per_chunk": 0,
    },
}

CONTEXT_PREVIEW_CHARS = 500

# Keyword patterns for conditional check applicability on narratives / images
_DOSAGE_KW = re.compile(
    r"mg/kg|mg\s*/\s*kg|tablet|dose|dosing|dosage|\d+\s*\+\s*\d+\s*mg",
    re.IGNORECASE,
)
_STRATIFICATION_KW = re.compile(
    r"weight|kg|age|year|month|infant|child|adult|pediatric|neonate",
    re.IGNORECASE,
)
_CONTRAINDICATION_KW = re.compile(
    r"contraindicated|do not use|avoid|not recommended|caution|warning|"
    r"first trimester|pregnancy|G6PD|hypersensitivity",
    re.IGNORECASE,
)
_CONDITIONAL_LOGIC_KW = re.compile(
    r"\bif\b.*\bthen\b|refer|danger sign|emergency|severe|failure|"
    r"switch to|escalate|hospitalize",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Chunk schema adapters
# ---------------------------------------------------------------------------

def _infer_chunk_type(chunk: Dict[str, Any]) -> str:
    """Map pipeline chunk fields to a review chunk_type string.

    Pipeline uses section_type + is_table_only + content_type.
    This function translates to the 5-way type expected by the verifier.
    """
    content_type = chunk.get("content_type") or ""
    if content_type in ("image_ocr", "image_placeholder"):
        return "image"

    if not chunk.get("is_table_only", False):
        return "narrative"

    # For table chunks: check section_type first, then table-level classification.
    section_type = (chunk.get("section_type") or "").lower()
    if section_type in ("dosing", "dosing_table"):
        return "dosing_table"
    if section_type in ("clinical_management", "clinical_table"):
        return "clinical_table"

    for t in chunk.get("tables", []):
        cls = (t.get("classification") or "").lower()
        if cls == "dosing":
            return "dosing_table"
        if cls == "clinical_management":
            return "clinical_table"
        if cls == "evidence":
            return "evidence_table"

    return "other_table"


def _get_nll(chunk: Dict[str, Any]) -> Optional[str]:
    """Return the first non-empty NLL string from the chunk's tables list."""
    for t in chunk.get("tables", []):
        nll = (t.get("nll") or "").strip()
        if nll:
            return nll
    return None


def _get_source_pages(chunk: Dict[str, Any]) -> List[int]:
    """Return [page] as a list (pipeline uses a single integer)."""
    page = chunk.get("page")
    if page is not None:
        try:
            return [int(page)]
        except (TypeError, ValueError):
            pass
    return []


def _get_preservation_level(chunk: Dict[str, Any]) -> str:
    return (chunk.get("preservation_level") or "standard").lower()


# ---------------------------------------------------------------------------
# Hash / signature utilities
# ---------------------------------------------------------------------------

def compute_audit_hash(content: str) -> str:
    """SHA-256 of the chunk's text content.

    Locks the extraction text so any post-extraction tampering is detectable.
    """
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def compute_content_hash(chunk: Dict[str, Any]) -> str:
    """SHA-256 of the full chunk JSON (all metadata included)."""
    serialized = json.dumps(chunk, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def compute_digital_signature(
    reviewer_name: str,
    institution: str,
    chunk_id: str,
    audit_hash: str,
    reviewed_at: str,
) -> str:
    """Tamper-evident digital signature.

    SHA-256 of (reviewer_name | institution | chunk_id | audit_hash | reviewed_at).
    """
    payload = "|".join(
        [reviewer_name, institution, chunk_id, audit_hash, reviewed_at]
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Triage
# ---------------------------------------------------------------------------

def classify_chunk_tier(chunk: Dict[str, Any]) -> int:
    """Assign a review tier (1–5) to a pipeline chunk.

    Tier 1: Dosing table — Stage 3 validation passed
    Tier 2: Dosing table — not validated / skipped
    Tier 3: Clinical management table (safety-critical)
    Tier 4: Evidence table OR high/verbatim-preservation narrative/image
    Tier 5: Everything else
    """
    ct = _infer_chunk_type(chunk)
    preservation = _get_preservation_level(chunk)

    # Pipeline validator operates at the document level; per-chunk validation
    # status is not stored.  Dosing tables without a status slot into Tier 2.
    if ct == "dosing_table":
        validation = chunk.get("validation") or {}
        if validation.get("status") == "pass":
            return 1
        return 2

    if ct == "clinical_table":
        return 3

    if ct == "other_table":
        cm = chunk.get("clinical_metadata") or {}
        if cm.get("level_of_care") or cm.get("danger_signs"):
            return 3

    if ct == "evidence_table":
        return 4

    if ct in ("narrative", "image") and preservation in ("high", "verbatim"):
        return 4

    return 5


def triage_all_chunks(
    chunks: List[Dict[str, Any]],
) -> Tuple[Dict[int, List[str]], Dict[str, int]]:
    """Classify all chunks into tiers.

    Returns:
        tier_groups: {tier_number: [chunk_ids]}
        chunk_tiers: {chunk_id: tier_number}
    """
    tier_groups: Dict[int, List[str]] = {1: [], 2: [], 3: [], 4: [], 5: []}
    chunk_tiers: Dict[str, int] = {}
    for chunk in chunks:
        tier = classify_chunk_tier(chunk)
        tier_groups[tier].append(chunk["chunk_id"])
        chunk_tiers[chunk["chunk_id"]] = tier
    return tier_groups, chunk_tiers


# ---------------------------------------------------------------------------
# Check applicability
# ---------------------------------------------------------------------------

def _build_guidance(
    check_key: str,
    chunk_type: str,
    page_str: str,
    section_str: str,
    drug_name: str,
    chunk: Dict[str, Any],
) -> str:
    drug_ref = f" for {drug_name}" if drug_name else ""

    if check_key == "dosage_accuracy":
        if chunk_type == "dosing_table":
            return (
                f"Verify each weight band's dose{drug_ref} matches "
                f"source PDF page {page_str}."
            )
        return f"Verify any dose values mentioned match source PDF page {page_str}."

    if check_key == "stratification":
        if chunk_type == "dosing_table":
            cm = chunk.get("clinical_metadata") or {}
            w_min = cm.get("patient_weight_min_kg")
            w_max = cm.get("patient_weight_max_kg")
            weight_ref = ""
            if w_min is not None or w_max is not None:
                weight_ref = f" (extracted range: {w_min}–{w_max} kg)"
            return (
                f"Confirm weight/age bands cover the full intended "
                f"population{weight_ref}; no merged or missing rows."
            )
        return (
            "Confirm any age/weight stratifications mentioned are "
            "correctly preserved."
        )

    if check_key == "contraindications":
        cm = chunk.get("clinical_metadata") or {}
        existing = cm.get("contraindications", [])
        sp = cm.get("special_populations", [])
        dangers = cm.get("danger_signs", [])
        hints = []
        if existing:
            hints.append(f"Extracted contraindications: {', '.join(existing)}")
        if sp:
            hints.append(f"Special populations: {', '.join(sp)}")
        if dangers:
            hints.append(
                f"Danger signs: {', '.join(d[:60] for d in dangers[:3])}"
            )
        base = "Check for warnings, danger signs, and referral criteria."
        if hints:
            base += " " + "; ".join(hints) + "."
        return base

    if check_key == "conditional_logic":
        nll = _get_nll(chunk)
        cm = chunk.get("clinical_metadata") or {}
        loc = cm.get("level_of_care", [])
        if nll:
            return (
                "Verify that the NLL (Natural Language Logic) correctly "
                "represents the weight→dose mapping from the table."
            )
        if loc:
            return (
                f"Verify Level of Care assignments ({', '.join(loc)}) match "
                "the source PDF. Confirm referral pathways are intact."
            )
        return (
            "Verify any IF/THEN logic, referral criteria, or decision "
            "pathways are intact."
        )

    if check_key == "provenance":
        return (
            f"Confirm source page {page_str} and section '{section_str}' "
            "match the source document."
        )

    return "Review this check against the source PDF."


def determine_applicable_checks(
    chunk: Dict[str, Any],
) -> Dict[str, Dict[str, Any]]:
    """Determine which of the 5 checks apply to this chunk.

    Returns {check_key: {"applicable": bool, "guidance": str}}.
    """
    ct = _infer_chunk_type(chunk)
    content = chunk.get("text", "")
    pages = _get_source_pages(chunk)
    section_title = chunk.get("heading", "")
    drug_name = (chunk.get("clinical_metadata") or {}).get("drug_name", "")
    page_str = ", ".join(str(p) for p in pages) if pages else "unknown"
    section_str = section_title or "unknown section"

    base = CHECK_APPLICABILITY.get(ct, CHECK_APPLICABILITY["narrative"])

    result: Dict[str, Dict[str, Any]] = {}
    for check_key, check_def in CHECK_DEFINITIONS.items():
        base_val = base.get(check_key, False)

        if base_val == "conditional":
            if check_key == "dosage_accuracy":
                applicable = bool(_DOSAGE_KW.search(content))
            elif check_key == "stratification":
                applicable = bool(_STRATIFICATION_KW.search(content))
            elif check_key == "contraindications":
                applicable = bool(_CONTRAINDICATION_KW.search(content))
            elif check_key == "conditional_logic":
                applicable = bool(_CONDITIONAL_LOGIC_KW.search(content))
            else:
                applicable = False
        else:
            applicable = bool(base_val)

        if applicable:
            guidance = _build_guidance(
                check_key, ct, page_str, section_str, drug_name, chunk
            )
        else:
            guidance = "Not applicable for this chunk type/content."

        result[check_key] = {"applicable": applicable, "guidance": guidance}

    return result


# ---------------------------------------------------------------------------
# Review item creation
# ---------------------------------------------------------------------------

def _format_validation_summary(validation: Optional[Dict]) -> str:
    if not validation:
        return "No validation data"
    status = validation.get("status", "unknown")
    if status == "pass":
        return (
            f"Pass ({validation.get('checks_passed', '?')}/"
            f"{validation.get('checks_total', '?')} automated checks, "
            f"{validation.get('weight_bands', '?')} weight bands)"
        )
    if status == "skipped":
        return f"Skipped ({validation.get('reason', 'unknown reason')})"
    if status == "fail":
        issues = validation.get("issues", [])
        issue_str = "; ".join(issues[:3]) if issues else "see details"
        return (
            f"Fail ({validation.get('checks_passed', '?')}/"
            f"{validation.get('checks_total', '?')} checks; {issue_str})"
        )
    if status == "not_applicable":
        return "Not applicable (non-weight-based table)"
    return f"Unknown ({status})"


def _get_context_preview(
    chunk: Dict[str, Any],
    chunk_lookup: Dict[str, Dict],
    max_chars: int = CONTEXT_PREVIEW_CHARS,
) -> Dict[str, Optional[str]]:
    related = chunk.get("related_chunks") or {}
    result: Dict[str, Optional[str]] = {
        "preceding_narrative_id": None,
        "preceding_narrative_preview": None,
        "following_narrative_id": None,
        "following_narrative_preview": None,
    }
    prec_id = related.get("preceding_narrative")
    if prec_id and prec_id in chunk_lookup:
        result["preceding_narrative_id"] = prec_id
        result["preceding_narrative_preview"] = (
            chunk_lookup[prec_id].get("text", "")[:max_chars].strip()
        )
    foll_id = related.get("following_narrative")
    if foll_id and foll_id in chunk_lookup:
        result["following_narrative_id"] = foll_id
        result["following_narrative_preview"] = (
            chunk_lookup[foll_id].get("text", "")[:max_chars].strip()
        )
    return result


def create_review_item(
    chunk: Dict[str, Any],
    tier: int,
    applicable_checks: Dict[str, Any],
    chunk_lookup: Dict[str, Dict],
) -> Dict[str, Any]:
    """Create a single review item with all context for physician review."""
    tier_def = TIER_DEFINITIONS[tier]
    cm = chunk.get("clinical_metadata") or {}
    text = chunk.get("text", "")
    audit_hash = compute_audit_hash(text)
    content_hash = compute_content_hash(chunk)
    context = _get_context_preview(chunk, chunk_lookup)

    tier_labels = {
        1: lambda v: (
            f"Validated dosing table (Stage 3: "
            f"{(v or {}).get('checks_passed', '?')}/"
            f"{(v or {}).get('checks_total', '?')} checks pass)"
        ),
        2: lambda _: "Unvalidated dosing table (Stage 3 skipped — no automated validation)",
        3: lambda _: "Clinical management table — safety-critical content",
    }
    if tier in tier_labels:
        tier_label = tier_labels[tier](chunk.get("validation"))
    elif tier == 4:
        ct = _infer_chunk_type(chunk)
        if ct == "evidence_table":
            tier_label = "Evidence table — clinical facts must be preserved"
        else:
            tier_label = "High-priority narrative — contains dosing or contraindication information"
    else:
        tier_label = "Standard chunk — general content"

    review_priority = (
        "mandatory"
        if tier in MANDATORY_TIERS
        else ("recommended" if tier in RECOMMENDED_TIERS else "optional")
    )

    return {
        "chunk_id": chunk["chunk_id"],
        "review_priority": review_priority,
        "review_tier": tier,
        "tier_label": tier_label,
        "preservation_level": _get_preservation_level(chunk),
        "chunk_type": _infer_chunk_type(chunk),
        "source_pages": _get_source_pages(chunk),
        "section_title": chunk.get("heading", ""),
        "content": text,
        "audit_hash": audit_hash,
        "content_hash": content_hash,
        "clinical_metadata": cm,
        "validation_summary": _format_validation_summary(chunk.get("validation")),
        "nll": _get_nll(chunk),
        "context": context,
        "applicable_checks": applicable_checks,
        "review": {
            "checks": {
                key: {"status": None, "notes": None}
                for key in CHECK_DEFINITIONS
            },
            "overall_decision": None,
            "corrections": None,
            "reviewer_name": None,
            "reviewer_role": None,
            "institution": None,
            "reviewed_at": None,
            "digital_signature": None,
        },
    }


# ---------------------------------------------------------------------------
# Package assembly
# ---------------------------------------------------------------------------

def assemble_review_package(
    chunks: List[Dict[str, Any]],
    chunk_lookup: Dict[str, Dict],
    tier_groups: Dict[int, List[str]],
    doc_title: str = "",
    source_pdf: str = "",
) -> Dict[str, Any]:
    """Assemble the complete review package JSON."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    review_items: List[Dict[str, Any]] = []
    for tier in [1, 2, 3, 4]:
        for cid in tier_groups[tier]:
            chunk = chunk_lookup[cid]
            checks = determine_applicable_checks(chunk)
            item = create_review_item(chunk, tier, checks, chunk_lookup)
            review_items.append(item)

    tier_counts = {t: len(ids) for t, ids in tier_groups.items()}
    mandatory_count = sum(tier_counts.get(t, 0) for t in MANDATORY_TIERS)
    recommended_count = sum(tier_counts.get(t, 0) for t in RECOMMENDED_TIERS)
    est_minutes = sum(
        tier_counts.get(t, 0) * TIER_DEFINITIONS[t]["est_minutes_per_chunk"]
        for t in [1, 2, 3, 4]
    )

    return {
        "pipeline_version": "4b",
        "source_document": doc_title,
        "source_pdf": source_pdf,
        "generated_at": now,
        "review_workflow": {
            "decisions": DECISIONS,
            "check_statuses": CHECK_STATUSES,
            "checks": {
                key: {
                    "check_number": defn["check_number"],
                    "name": defn["name"],
                    "description": defn["description"],
                }
                for key, defn in CHECK_DEFINITIONS.items()
            },
            "safety_rule": (
                "No content proceeds to Phase B (Deployment) without "
                "a verified_by signature and audit_hash."
            ),
        },
        "summary": {
            "total_chunks_in_pipeline": len(chunks),
            "total_review_items": len(review_items),
            "mandatory_review": mandatory_count,
            "recommended_review": recommended_count,
            "not_included_optional": tier_counts.get(5, 0),
            "estimated_review_time_minutes": round(est_minutes, 1),
            "by_tier": {
                str(t): {
                    "count": tier_counts.get(t, 0),
                    "label": TIER_DEFINITIONS[t]["label"],
                    "requirement": TIER_DEFINITIONS[t]["review_requirement"],
                }
                for t in [1, 2, 3, 4, 5]
            },
        },
        "review_items": review_items,
    }


# ---------------------------------------------------------------------------
# Physician-readable markdown report
# ---------------------------------------------------------------------------

def _format_review_item_markdown(item: Dict[str, Any], item_number: int) -> str:
    lines = []
    cid = item["chunk_id"]
    pages = item["source_pages"]
    page_str = ", ".join(str(p) for p in pages) if pages else "?"
    section_title = item.get("section_title", "")
    cm = item.get("clinical_metadata") or {}
    drug = cm.get("drug_name", "")
    nll = item.get("nll")
    val_summary = item.get("validation_summary", "")
    context = item.get("context", {})

    header = f"### {item_number}. {cid}"
    if drug:
        header += f" — {drug}"
    lines.append(header)

    meta_parts = [f"**Pages:** {page_str}"]
    if section_title:
        meta_parts.append(f"**Section:** {section_title}")
    lines.append(" | ".join(meta_parts))

    detail_parts = []
    if val_summary:
        emoji = "✅" if "Pass" in val_summary else ("❌" if "Fail" in val_summary else "⚠️")
        detail_parts.append(f"**Validation:** {emoji} {val_summary}")
    condition = cm.get("condition", "")
    if condition:
        detail_parts.append(f"**Condition:** {condition}")
    w_min = cm.get("patient_weight_min_kg")
    w_max = cm.get("patient_weight_max_kg")
    if w_min is not None or w_max is not None:
        w_str = f"{w_min}–{w_max} kg" if w_max else f"{w_min}+ kg"
        detail_parts.append(f"**Weight range:** {w_str}")
    if detail_parts:
        lines.append(" | ".join(detail_parts))

    lines.append("")
    lines.append(f"**Audit hash:** `{item['audit_hash'][:16]}...`")
    lines.append("")
    lines.append("#### Extracted Content")
    lines.append("```")
    lines.append(item["content"])
    lines.append("```")
    lines.append("")

    if nll:
        lines.append("#### Natural Language Logic (NLL)")
        lines.append("```")
        lines.append(nll)
        lines.append("```")
        lines.append("")

    prec_preview = context.get("preceding_narrative_preview")
    foll_preview = context.get("following_narrative_preview")
    if prec_preview or foll_preview:
        lines.append("#### Clinical Context")
        if prec_preview:
            prec_id = context.get("preceding_narrative_id", "")
            lines.append(f"> **Before this item** ({prec_id}): {prec_preview}")
            lines.append(">")
        if foll_preview:
            foll_id = context.get("following_narrative_id", "")
            lines.append(f"> **After this item** ({foll_id}): {foll_preview}")
        lines.append("")

    contras = cm.get("contraindications", [])
    specials = cm.get("special_populations", [])
    if contras or specials:
        lines.append("#### Extracted Clinical Flags")
        if contras:
            lines.append(f"- **Contraindications:** {', '.join(contras)}")
        if specials:
            lines.append(f"- **Special populations:** {', '.join(specials)}")
        lines.append("")

    lines.append("#### Verification Checklist")
    applicable = item.get("applicable_checks", {})
    for check_key, check_def in CHECK_DEFINITIONS.items():
        check_info = applicable.get(check_key, {})
        if check_info.get("applicable", False):
            guidance = check_info.get("guidance", "")
            lines.append(f"- [ ] **{check_def['name']}** — {guidance}")
        else:
            lines.append(f"- ~~**{check_def['name']}**~~ — Not applicable")
    lines.append("")
    lines.append("**Decision:** ☐ Approved  ☐ Flagged  ☐ Corrected")
    lines.append("")
    lines.append("**Reviewer notes:** _____")
    lines.append("")
    lines.append("**Corrections (if any):** _____")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def generate_physician_report(package: Dict[str, Any]) -> str:
    """Generate the complete physician-readable markdown review report."""
    lines = []
    summary = package["summary"]
    source_pdf = package.get("source_pdf", "")

    lines.append("# Clinical Verification Report")
    lines.append("## Stage 4b: Physician Review Package")
    lines.append("")
    lines.append(
        f"**Generated:** {package['generated_at']} | **Pipeline version:** 4b"
    )
    if source_pdf:
        lines.append(f"**Source:** {source_pdf}")
    lines.append(
        "**Safety rule:** No content proceeds to deployment without "
        "`verified_by` signature + `audit_hash`."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## How to Use This Document")
    lines.append("")
    lines.append("1. Review each item against the **5 Clinical Verification Checks**:")
    for check_key, check_def in CHECK_DEFINITIONS.items():
        lines.append(f"   - **{check_def['name']}**: {check_def['description']}")
    lines.append(
        "2. For each check, mark: ✅ Pass | ❌ Fail | ⚠️ Corrected | — Not applicable"
    )
    lines.append(
        "3. Record your **overall decision**: Approved / Flagged / Corrected"
    )
    lines.append(
        "4. Enter corrections in the notes field if flagging or correcting"
    )
    lines.append(
        "5. Fill in your reviewer details (name, role, institution, date)"
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Review Summary")
    lines.append("")
    lines.append("| Tier | Description | Chunks | Priority | Est. Time |")
    lines.append("|---|---|---|---|---|")
    for t in [1, 2, 3, 4]:
        td = TIER_DEFINITIONS[t]
        count = summary["by_tier"][str(t)]["count"]
        est = count * td["est_minutes_per_chunk"]
        time_str = f"~{est/60:.1f} hrs" if est >= 60 else f"~{est:.0f} min"
        desc = td["description"]
        desc_short = desc[:60] + "..." if len(desc) > 60 else desc
        lines.append(
            f"| {t}. {td['label']} | {desc_short} "
            f"| {count} | {td['review_requirement'].capitalize()} | {time_str} |"
        )
    mandatory_est = sum(
        summary["by_tier"][str(t)]["count"] * TIER_DEFINITIONS[t]["est_minutes_per_chunk"]
        for t in MANDATORY_TIERS
    )
    lines.append(
        f"| **Total mandatory** | | **{summary['mandatory_review']}** | "
        f"| **~{mandatory_est:.0f} min** |"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    items_by_tier: Dict[int, List[Dict]] = {1: [], 2: [], 3: [], 4: []}
    for item in package["review_items"]:
        t = item["review_tier"]
        if t in items_by_tier:
            items_by_tier[t].append(item)

    tier_headings = {
        1: "TIER 1 — Validated Dosing Tables",
        2: "TIER 2 — Unvalidated Dosing Tables",
        3: "TIER 3 — Clinical Management Tables",
        4: "TIER 4 — Evidence Tables + High-Priority Narratives",
    }
    tier_notes = {
        1: (
            "> These tables passed all 6 automated plausibility checks. "
            "The physician confirms extraction accuracy against the source PDF."
        ),
        2: (
            "> ⚠️ These tables were NOT validated by Stage 3 automated checks. "
            "Extra care required — verify all values against the source PDF."
        ),
        3: (
            "> Safety-critical clinical management content. "
            "Full manual review required."
        ),
        4: (
            "> Contains clinical thresholds, dosing keywords, or contraindication "
            "information. Recommended for additional clinical safety assurance."
        ),
    }
    tier_requirements = {1: "MANDATORY", 2: "MANDATORY", 3: "MANDATORY", 4: "RECOMMENDED"}

    offset = 0
    for t in [1, 2, 3, 4]:
        tier_items = items_by_tier[t]
        if not tier_items:
            continue
        req = tier_requirements[t]
        lines.append(
            f"## {tier_headings[t]} ({len(tier_items)} chunks) — {req} REVIEW"
        )
        lines.append("")
        lines.append(tier_notes[t])
        lines.append("")
        for i, item in enumerate(tier_items, offset + 1):
            lines.append(_format_review_item_markdown(item, i))
        offset += len(tier_items)

    lines.append("---")
    lines.append("")
    lines.append("## Appendix: Reviewer Sign-Off")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    for field in ["Reviewer name", "Reviewer role", "Institution", "Date", "Signature"]:
        lines.append(f"| **{field}** | _____ |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Appendix: Glossary")
    lines.append("")
    lines.append("| Term | Meaning |")
    lines.append("|---|---|")
    for term, meaning in [
        ("ACT", "Artemisinin-based combination therapy"),
        ("NLL", "Natural Language Logic — human-readable representation of table logic"),
        ("Audit hash", "SHA-256 hash of extracted content; ensures tamper detection"),
        (
            "Preservation level",
            "Controls whether RAG/LLM may paraphrase: verbatim (no), high (minimal), standard (yes)",
        ),
        ("Tier 1", "Dosing tables that passed all 6 automated plausibility checks"),
        ("Tier 2", "Dosing tables that were not validated by automated checks"),
        ("Tier 3", "Clinical management tables (safety-critical)"),
        ("Tier 4", "Evidence tables and narratives containing dosing/contraindication keywords"),
        (
            "G6PD",
            "Glucose-6-phosphate dehydrogenase (enzyme deficiency relevant to antimalarial safety)",
        ),
    ]:
        lines.append(f"| **{term}** | {meaning} |")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Review ingestion / validation
# ---------------------------------------------------------------------------

def validate_completed_review(
    completed: Dict[str, Any],
    chunks: List[Dict[str, Any]],
) -> Tuple[bool, List[str], Dict[str, Any]]:
    """Validate a completed review package.

    Returns (is_valid, issues, stats).
    Six validation checks:
      1. All mandatory chunks have overall_decision set
      2. All applicable checks have status set
      3. Audit hashes match (content wasn't tampered with)
      4. Reviewer identity filled for all reviewed items
      5. reviewed_at is a valid ISO datetime
      6. Flagged/corrected items have notes or corrections
    """
    issues: List[str] = []
    stats: Dict[str, Any] = {
        "total_reviewed": 0,
        "approved": 0,
        "flagged": 0,
        "corrected": 0,
        "unreviewed_mandatory": 0,
        "hash_mismatches": 0,
        "missing_identity": 0,
        "missing_datetime": 0,
        "missing_notes_on_flags": 0,
        "missing_check_statuses": 0,
    }

    chunk_lookup = {c["chunk_id"]: c for c in chunks}
    review_items = completed.get("review_items", [])

    for item in review_items:
        cid = item["chunk_id"]
        review = item.get("review", {})
        decision = review.get("overall_decision")
        tier = item.get("review_tier", 5)

        # Check 1
        if tier in MANDATORY_TIERS and not decision:
            stats["unreviewed_mandatory"] += 1
            issues.append(
                f"Mandatory chunk {cid} (tier {tier}) has no decision"
            )
            continue

        if not decision:
            continue  # unreviewed recommended/optional — OK

        stats["total_reviewed"] += 1
        if decision in ("approved", "flagged", "corrected"):
            stats[decision] += 1

        # Check 2
        applicable = item.get("applicable_checks", {})
        checks = review.get("checks", {})
        for check_key, check_info in applicable.items():
            if check_info.get("applicable", False):
                if not (checks.get(check_key) or {}).get("status"):
                    stats["missing_check_statuses"] += 1
                    issues.append(
                        f"{cid}: check '{check_key}' is applicable but has no status"
                    )

        # Check 3
        if cid in chunk_lookup:
            expected = compute_audit_hash(chunk_lookup[cid].get("text", ""))
            if item.get("audit_hash") != expected:
                stats["hash_mismatches"] += 1
                issues.append(
                    f"{cid}: audit_hash MISMATCH — content may have been altered"
                )

        # Check 4
        if not review.get("reviewer_name") or not review.get("institution"):
            stats["missing_identity"] += 1
            issues.append(f"{cid}: missing reviewer_name or institution")

        # Check 5
        reviewed_at = review.get("reviewed_at")
        if not reviewed_at:
            stats["missing_datetime"] += 1
            issues.append(f"{cid}: missing reviewed_at timestamp")
        else:
            try:
                datetime.fromisoformat(reviewed_at.replace("Z", "+00:00"))
            except (ValueError, AttributeError):
                stats["missing_datetime"] += 1
                issues.append(
                    f"{cid}: reviewed_at '{reviewed_at}' is not valid ISO datetime"
                )

        # Check 6
        if decision in ("flagged", "corrected"):
            has_notes = bool(review.get("corrections"))
            has_check_notes = any(
                (checks.get(k) or {}).get("notes") for k in checks
            )
            if not has_notes and not has_check_notes:
                stats["missing_notes_on_flags"] += 1
                issues.append(
                    f"{cid}: decision is '{decision}' but no corrections or notes provided"
                )

    is_valid = (
        stats["unreviewed_mandatory"] == 0
        and stats["hash_mismatches"] == 0
        and stats["missing_identity"] == 0
        and stats["missing_datetime"] == 0
    )
    return is_valid, issues, stats


def apply_reviews_to_chunks(
    completed: Dict[str, Any],
    chunks: List[Dict[str, Any]],
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Apply completed reviews to chunks, updating verified_by fields.

    Returns (updated_chunks, application_stats).
    """
    chunk_lookup = {c["chunk_id"]: c for c in chunks}
    review_lookup = {
        item["chunk_id"]: item
        for item in completed.get("review_items", [])
        if (item.get("review") or {}).get("overall_decision")
    }
    applied = 0
    skipped = 0

    for chunk in chunks:
        cid = chunk["chunk_id"]
        if cid not in review_lookup:
            skipped += 1
            continue

        item = review_lookup[cid]
        review = item["review"]
        decision = review["overall_decision"]

        status_map = {"approved": "verified", "flagged": "flagged", "corrected": "flagged"}
        status = status_map.get(decision, "unverified")

        audit_hash = compute_audit_hash(chunk.get("text", ""))
        sig = compute_digital_signature(
            reviewer_name=review.get("reviewer_name", ""),
            institution=review.get("institution", ""),
            chunk_id=cid,
            audit_hash=audit_hash,
            reviewed_at=review.get("reviewed_at", ""),
        )

        # Collect comments
        parts = []
        if review.get("corrections"):
            parts.append(f"Corrections: {review['corrections']}")
        for check_key, check_review in (review.get("checks") or {}).items():
            if (check_review or {}).get("notes"):
                check_name = CHECK_DEFINITIONS.get(check_key, {}).get("name", check_key)
                parts.append(f"{check_name}: {check_review['notes']}")
        comments = "; ".join(parts) if parts else None

        chunk["verified_by"] = {
            "status": status,
            "reviewer_name": review.get("reviewer_name"),
            "reviewer_role": review.get("reviewer_role"),
            "institution": review.get("institution"),
            "digital_signature": sig,
            "verified_at": review.get("reviewed_at"),
            "comments": comments,
        }
        chunk["audit_hash"] = audit_hash
        chunk["clinical_verification_checks"] = {
            check_key: {
                "status": (review.get("checks") or {}).get(check_key, {}).get("status"),
                "notes": (review.get("checks") or {}).get(check_key, {}).get("notes"),
            }
            for check_key in CHECK_DEFINITIONS
        }
        applied += 1

    return chunks, {"applied": applied, "skipped": skipped, "total": len(chunks)}


# ---------------------------------------------------------------------------
# Deployment gate
# ---------------------------------------------------------------------------

def passes_deployment_gate(chunks: List[Dict[str, Any]]) -> Tuple[bool, List[str]]:
    """Check whether every mandatory-tier chunk has a verified_by signature.

    Returns (passes, list_of_unverified_chunk_ids).
    Safety rule: No content proceeds to Phase B without verified_by + audit_hash.
    """
    _, chunk_tiers = triage_all_chunks(chunks)
    unverified = []
    for chunk in chunks:
        cid = chunk["chunk_id"]
        tier = chunk_tiers.get(cid, 5)
        if tier in MANDATORY_TIERS:
            vb = chunk.get("verified_by") or {}
            if vb.get("status") not in ("verified",) or not chunk.get("audit_hash"):
                unverified.append(cid)
    return len(unverified) == 0, unverified


# ---------------------------------------------------------------------------
# ClinicalVerifier — main class
# ---------------------------------------------------------------------------

class ClinicalVerifier:
    """Stage 4b: generate review packages and ingest completed reviews.

    Usage::

        verifier = ClinicalVerifier(chunks, config)

        # Generate
        package = verifier.generate(output_dir="./out", doc_title="Uganda 2023")

        # Ingest (after physician fills in the review package JSON)
        ok, issues, updated = verifier.ingest("completed_review.json", "./out")
        passes, unverified = verifier.deployment_gate_check(updated)
    """

    def __init__(
        self,
        chunks: List[Dict[str, Any]],
        config: Any = None,
    ):
        self.chunks = chunks
        self.config = config

    def generate(
        self,
        output_dir: Optional[str] = None,
        doc_title: str = "",
        source_pdf: str = "",
    ) -> Dict[str, Any]:
        """Build and optionally save the review package + physician report.

        Returns the review package dict.
        """
        chunk_lookup = {c["chunk_id"]: c for c in self.chunks}
        tier_groups, _ = triage_all_chunks(self.chunks)
        package = assemble_review_package(
            self.chunks, chunk_lookup, tier_groups,
            doc_title=doc_title, source_pdf=source_pdf,
        )
        if output_dir:
            out = Path(output_dir)
            out.mkdir(parents=True, exist_ok=True)
            pkg_path = out / "review_package.json"
            with open(pkg_path, "w", encoding="utf-8") as f:
                json.dump(package, f, indent=2, ensure_ascii=False)
            report = generate_physician_report(package)
            rpt_path = out / "physician_review_report.md"
            with open(rpt_path, "w", encoding="utf-8") as f:
                f.write(report)
        return package

    def ingest(
        self,
        completed_review_path: str,
        output_dir: Optional[str] = None,
    ) -> Tuple[bool, List[str], List[Dict[str, Any]]]:
        """Validate and apply a completed physician review.

        Returns (is_valid, issues, updated_chunks).
        Updated chunks have verified_by + audit_hash + clinical_verification_checks.
        Optionally writes updated chunks.json to output_dir.
        """
        with open(completed_review_path, "r", encoding="utf-8") as f:
            completed = json.load(f)

        is_valid, issues, _ = validate_completed_review(completed, self.chunks)
        if not is_valid:
            return is_valid, issues, self.chunks

        updated, _ = apply_reviews_to_chunks(completed, self.chunks)
        if output_dir:
            out = Path(output_dir)
            out.mkdir(parents=True, exist_ok=True)
            chunks_path = out / "chunks.json"
            with open(chunks_path, "w", encoding="utf-8") as f:
                json.dump(updated, f, indent=2, ensure_ascii=False)
        return is_valid, issues, updated

    @staticmethod
    def deployment_gate_check(
        chunks: List[Dict[str, Any]],
    ) -> Tuple[bool, List[str]]:
        """Return (passes, unverified_chunk_ids) for the mandatory-tier chunks."""
        return passes_deployment_gate(chunks)
