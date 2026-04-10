# Safety and Guardrails

This document describes the safety measures implemented across every stage of the pipeline. Medical Q&A systems can cause real harm if they deliver incorrect dosing, miss danger signs, or present unverified information as authoritative. Our approach is defense-in-depth: multiple independent safety layers, each catching different categories of error.

## Safety by pipeline stage

### Stage 1: Extraction safety

**Preservation of exact values.** The extraction engine uses rule-based parsing (PyMuPDF + pdfplumber), never LLM-based interpretation. Cell values in dosing tables are preserved character-for-character. This eliminates the risk of an AI model "correcting" a dose that looks unusual but is clinically correct.

**Cross-validation (Pass 4).** Every page of extracted text is independently re-extracted with a second library (pdfplumber) and compared. Pages with <90% consistency are flagged, alerting downstream stages to potential extraction errors.

**Automatic PDF repair (2026-04-10).** Some PDFs produced by tools like Adobe InDesign use a non-standard internal page-tree structure that pdfminer/pdfplumber cannot traverse, causing pdfplumber to return 0 pages and the cross-consistency score to silently stay at 0% — a false failure. The extractor now detects this: if pdfplumber returns 0 pages, it automatically re-saves the PDF through PyMuPDF (`garbage=4, deflate=True, clean=True`) to a temporary file, which normalises the PDF structure to standard format. pdfplumber then runs on the repaired copy and produces correct results. The temporary file is deleted after cross-validation. This fix is transparent — no configuration change is needed — and makes cross-validation work correctly on any uploaded PDF.

**Table classification.** Tables are classified by clinical function (dosing, clinical management, evidence, structural, other). Misclassifying a dosing table as "other" could cause it to be paraphrased instead of preserved verbatim. The classification uses conservative keyword matching with domain-specific vocabularies from `configs/*.json`.

### Stage 2: Validation safety

Six independent validation stages catch different error categories:

| Stage | What it checks | Why it matters |
|---|---|---|
| Structure | Heading hierarchy, page numbering | Malformed structure = wrong section assignments |
| Tables | Column counts, numeric density | Corrupted tables = wrong dosing data |
| Cross-consistency | PyMuPDF vs pdfplumber agreement | Extraction failures = missing content |
| Medical content | Presence of critical clinical terms | Missing terms = incomplete extraction |
| Dosing plausibility | Weight bands, monotonicity, coverage, clinical bounds, combination ratios, empty cells | Implausible dosing = medication errors |
| Human review | Flags items needing physician attention | Catches what automated checks cannot |

**Dosing plausibility** is the most critical safety stage. It runs six sub-checks on every dosing-classified table:

1. **Weight contiguity** — no gaps between consecutive weight bands
2. **Dose monotonicity** — doses increase with weight (as expected clinically)
3. **Weight coverage** — table covers pediatric through adult ranges
4. **Clinical bounds** — per-kg doses fall within reference ranges for known drugs
5. **Combination consistency** — fixed-ratio drug combinations maintain stable ratios
6. **Positive/non-empty** — no missing values in dosing cells

### Stage 3: Chunking safety

**Preservation levels.** Every chunk is assigned a preservation level (`VERBATIM`, `HIGH`, `STANDARD`) based on its section type and table presence. This level travels with the chunk through retrieval and response generation, constraining how the content may be used.

**Metadata extraction.** Clinical metadata (drug names, weight ranges, contraindications) is extracted from every chunk. This enables the retriever and response layer to make safety-aware decisions — e.g., including contraindication chunks when a drug is mentioned.

**Related chunk linking.** Dosing tables are linked to their surrounding narrative context. When a dosing table is retrieved, the related narrative (which may contain contraindications or special population warnings) can be pulled in automatically.

### Stage 4: Clinical verification

**Physician review package.** The `ClinicalVerifier` generates a structured review package (`review_package.json` + `physician_review_report.md`) that a clinician can review before the knowledge base is used for patient care.

**5-tier triage classification:**

| Tier | Content type | Review priority |
|---|---|---|
| 1 | Validated dosing tables (passed Stage 2) | Mandatory — highest priority |
| 2 | Unvalidated dosing tables | Mandatory |
| 3 | Clinical management content | Mandatory |
| 4 | Evidence tables, high-preservation narrative | Recommended |
| 5 | Optional/background content | Optional |

**5 clinical verification checks per chunk:**

1. Dosage accuracy
2. Patient stratification correctness
3. Contraindication completeness
4. Conditional logic integrity
5. Source provenance

**SHA-256 audit hashes.** Every chunk gets a content hash. After physician review, the hash is re-verified to ensure no content was modified between review and deployment.

**Digital signatures.** Completed reviews include a digital signature (reviewer name, institution, timestamp, chunk ID, audit hash) for accountability.

**Deployment gate.** `passes_deployment_gate()` blocks any knowledge base from production use if mandatory-tier chunks (Tiers 1-3) have not been verified. This is a hard gate — there is no override.

### Stage 5: Response safety

**Two-brain architecture.** The response generator and the guardrail validator are separate, independent systems. The generator cannot suppress or modify guardrail findings.

**Guardrail checks:**
- Triage level must match detected danger signs
- Dangerous advice patterns are regex-detected and blocked
- All five required sections must be present
- Citations must reference real pages in the knowledge base

**Preservation-level enforcement.** VERBATIM content (dosing tables) is rendered exactly as extracted — the response formatter cannot paraphrase or summarize it.

**Confidence scoring (updated 2026-04-09).** Every response includes a numeric confidence (0.0–1.0) computed from three real retrieval signals:

```
confidence = 0.6 × retrieval_score + 0.4 × coverage − penalty
```

- **Retrieval score (60%)** — mean score of the top-3 retrieved chunks, normalized to [0,1] after RRF + cross-encoder blending
- **Coverage (40%)** — fraction of the 5 requested chunks that were actually returned
- **Guardrail penalty (subtracted)** — −0.05 per warning, −0.15 per error, −0.10 if guardrail failed

Prior to this change, the score was a hardcoded constant (0.90 for all non-RED queries) adjusted only for guardrail warnings — meaning a query backed by weak evidence received the same score as one with five highly-relevant passages. The score now carries real information about how well the retrieved evidence supports the response.

## Defense-in-depth summary

```
PDF Input
  |
  [Extraction] --- exact value preservation, no LLM interpretation
  |
  [Cross-validation] --- dual-extractor consistency check
  |
  [Validation] --- 6 stages, 6 dosing sub-checks
  |
  [Chunking] --- preservation levels, metadata extraction
  |
  [Clinical verification] --- physician review, audit hashes, deployment gate
  |
  [Retrieval] --- metadata-aware, not just embedding similarity
  |
  [Response generation] --- PDF-first content extraction, VERBATIM dosing blocks
  |
  [Guardrail validation] --- independent safety checks
  |
  [Confidence score] --- numeric safety signal to user
  |
  Response Output
```

No single layer is relied upon exclusively. Each layer catches different failure modes, and the deployment gate ensures that unverified content cannot reach patients.

See also: [Benchmarking and validation](benchmarking_and_validation.md) for quantitative safety metrics.
