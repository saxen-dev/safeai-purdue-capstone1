"""
Validate the VHT response layer for the 25 evaluation queries × 2 guideline presets.

Loads existing KBs, runs answer_with_response per query. The Markdown report includes
a summary table plus per-query sections with the full query and complete formatted
outputs (VHT standard, referral note, quick summary).

Usage (repo root):
  $env:PYTHONIOENCODING='utf-8'
  python scripts/response_layer_validation_report.py
"""

from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _load_preset_meta():
    path = ROOT / "scripts" / "who_malaria_pipeline_report.py"
    spec = importlib.util.spec_from_file_location("wm_report", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.PRESET_META


def _fence(label: str, body: str) -> list[str]:
    out = [f"#### {label}", "", "```"]
    out.append(body if body else "")
    out.append("```")
    out.append("")
    return out


def main() -> None:
    from pipeline.orchestrator import MedicalQASystem

    PRESET_META = _load_preset_meta()
    reports_dir = ROOT / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    out_path = reports_dir / f"response_layer_validation_{ts}.md"
    latest = reports_dir / "response_layer_validation.md"

    lines: list[str] = [
        "# Response layer validation (25 queries × 2 sources)",
        "",
        f"- **Generated (UTC)**: {datetime.now(timezone.utc).isoformat()}",
        "- **Method**: `MedicalQASystem.answer_with_response()` after BM25 + guardrail",
        "",
        "## Acceptance criteria",
        "",
        "- **Guardrail**: `validation_passed == True` for all cases (required sections + triage line).",
        "- **Triage**: `RED` if query matches danger-sign keywords; `YELLOW` for time-sensitive heuristics; else `GREEN`.",
        "- **VHT output**: non-empty `vht_response`, `referral_note`, `quick_summary`.",
        "",
        "Per preset: summary table (metrics only), then **full query** and **complete** formatted outputs for each of the 25 queries.",
        "",
        "---",
        "",
    ]

    all_ok = True
    for preset in ("who-malaria", "uganda"):
        meta = PRESET_META[preset]
        cfg = meta["config_fn"]()
        queries = meta["queries"]
        kb_file = Path(cfg.output_dir) / "knowledge_base.json"
        if not kb_file.is_file():
            lines.append(f"## SKIP: `{preset}` — KB missing at `{kb_file}`\n\n")
            all_ok = False
            continue

        qa = MedicalQASystem(config=cfg)
        qa.initialize()

        lines.append(f"## Preset: `{preset}`")
        lines.append("")
        lines.append(f"- **Document**: {cfg.document_title}")
        lines.append(f"- **Queries**: {len(queries)}")
        lines.append("")
        lines.append("### Summary table")
        lines.append("")
        lines.append(
            "| # | Triage | Guardrail OK | Confidence | "
            "VHT chars | Referral chars | Quick chars |"
        )
        lines.append(
            "|---|--------|--------------|------------|"
            "-----------|----------------|-------------|"
        )

        results: list[tuple[int, str, dict]] = []
        for i, q in enumerate(queries, 1):
            r = qa.answer_with_response(q)
            results.append((i, q, r))
            tri = r["triage"].name
            ok = r["validation_passed"]
            conf = r["structured"].confidence_score
            vht = r.get("vht_response") or ""
            ref = r.get("referral_note") or ""
            quick = r.get("quick_summary") or ""
            lines.append(
                f"| {i} | {tri} | {ok} | {conf:.2f} | "
                f"{len(vht)} | {len(ref)} | {len(quick)} |"
            )
            if not ok:
                all_ok = False

        lines.append("")
        lines.append("### Full queries and formatted outputs")
        lines.append("")

        for i, q, r in results:
            tri = r["triage"].name
            ok = r["validation_passed"]
            conf = r["structured"].confidence_score
            vht = r.get("vht_response") or ""
            ref = r.get("referral_note") or ""
            quick = r.get("quick_summary") or ""
            evidence = r.get("response") or ""

            lines.append(f"#### Query {i}")
            lines.append("")
            lines.append("**Full query**")
            lines.append("")
            lines.append(f"> {q}")
            lines.append("")
            lines.append(
                f"**Metrics:** Triage `{tri}` | Guardrail OK `{ok}` | "
                f"Confidence `{conf:.2f}`"
            )
            lines.append("")
            lines.extend(_fence("VHT standard (`vht_response`)", vht))
            lines.extend(_fence("Referral note (`referral_note`)", ref))
            lines.extend(_fence("Quick summary (`quick_summary`)", quick))
            lines.extend(
                _fence(
                    "BM25 + guardrail evidence bundle (`response` — markdown)",
                    evidence,
                )
            )
            lines.append("---")
            lines.append("")

        lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **All guardrails passed**: {all_ok}")
    lines.append("")

    text = "\n".join(lines)
    out_path.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    print(f"Wrote {out_path}")
    print(f"Wrote {latest}")
    if not all_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
