# Response Layer Strategy

**Modules:** `pipeline/response.py` (500 lines), `pipeline/guardrail.py` (145 lines) | **Classes:** `ResponseOrchestrator`, `VHTResponseFormatter`, `MedicalGuardrailBrain`

## What we built

A **two-brain response system** designed for Village Health Team (VHT) workers in low-resource clinical settings. Retrieved chunks are assembled into structured, guardrail-validated responses in multiple output formats.

```
Retrieved chunks
  |
  +---> ResponseOrchestrator
  |       - Infer triage level (RED / YELLOW / GREEN)
  |       - Select template actions, monitoring, referral criteria
  |       - Extract VERBATIM dosing blocks
  |       - Generate family education message
  |       - Calculate confidence score
  |
  +---> MedicalGuardrailBrain (validation)
  |       - Validate triage level against danger signs
  |       - Detect dangerous advice patterns
  |       - Verify citation page references
  |       - Check required response sections
  |
  +---> VHTResponseFormatter (output)
          - VHT_STANDARD: full structured response
          - VHT_QUICK: minimal triage summary
          - CLINICIAN: clinical detail focus
          - REFERRAL: structured referral note
```

### Why a two-brain architecture?

The "generating brain" (ResponseOrchestrator) assembles the response. The "validating brain" (MedicalGuardrailBrain) independently checks it for safety violations. This separation ensures that the generation logic cannot bypass safety checks — the guardrail brain has no knowledge of how the response was assembled, only whether the final output is safe.

### Triage inference

Every response starts with a triage classification:

| Level | Criteria | Response behavior |
|---|---|---|
| **RED** | Danger signs detected (convulsions, unconscious, unable to drink, severe bleeding) | Emergency header, immediate referral, no home treatment |
| **YELLOW** | Clinical concern without danger signs | Urgent actions, monitoring checklist, referral criteria |
| **GREEN** | Routine clinical question | Standard guidance, monitoring, when-to-refer list |

Triage level drives which template actions, monitoring checklists, and referral criteria are selected.

### Preservation-level-aware formatting

The response formatter respects the preservation level assigned during chunking:

- **VERBATIM** chunks (dosing tables): Rendered as exact text blocks with no modification. The `_dosing_block()` method extracts these and presents them in a clearly demarcated section.
- **HIGH** chunks (contraindications, treatment protocols): Presented with minimal formatting changes.
- **STANDARD** chunks (background, diagnosis): May be paraphrased and summarized.

This prevents the response layer from inadvertently altering dosing values — the most dangerous category of error in medical Q&A.

### Structured response sections

The VHT_STANDARD format includes:

1. **Emergency header** (RED triage only) — bold alert box
2. **Quick summary** — one-sentence triage decision
3. **Step-by-step actions** — numbered, concrete instructions
4. **Monitoring checklist** — what to watch for, when to escalate
5. **Danger signs** — when to refer immediately
6. **Family education message** — plain-language explanation for caregivers
7. **VHT reminders** — documentation, follow-up timing
8. **Dosing blocks** — VERBATIM dosing information
9. **Citations** — page references with preservation level labels

### Medical jargon translation

A built-in translation dictionary converts clinical terminology to VHT-friendly language:

```
"lethargic"  →  "very weak"
"dyspnea"    →  "difficulty breathing"
"febrile"    →  "fever"
"emesis"     →  "vomiting"
```

### Confidence scoring

Each response includes a confidence score (0.0 to 1.0):

- Base: 0.95 (RED), 0.90 (YELLOW/GREEN)
- Reduced by 0.05 per guardrail warning
- Reduced by 0.15 per guardrail error
- Floor: 0.0

## Guardrail validation

The `MedicalGuardrailBrain` runs five independent checks on every response:

### 1. Triage validation

Extracts the triage level from the response text and checks it against detected danger signs in the query. A query mentioning "convulsions" must produce a RED triage — anything else is flagged.

### 2. Dangerous advice detection

Regex patterns detect high-risk recommendations:

- Prescribing medication without mentioning referral
- Suggesting delayed referral when danger signs are present
- Recommending home treatment for emergency conditions
- Aspirin in children (Reye syndrome risk)

### 3. Required sections check

Verifies that all five required sections are present: Triage Level, Immediate Actions, Next Steps / Monitoring, When to Refer, Citations.

### 4. Citation validation

Extracts page references from the response and checks that each referenced page exists in the knowledge base.

### 5. Output structure validation

Checks that the response is non-empty and doesn't contain raw error messages or stack traces.

## Rationale

### Why template-based action selection?

For VHT workers in low-resource settings, responses must be actionable and concrete. Template-based actions ("Give oral rehydration salts", "Check temperature every 4 hours") are more useful than LLM-generated prose that might use inconsistent phrasing or miss critical steps. Templates are clinically reviewed and can be updated centrally.

### Why not use an LLM for response generation?

Several reasons specific to our use case:

1. **Hallucination risk:** An LLM might generate plausible-sounding but incorrect dosing information. Our template + VERBATIM approach never invents dosing data.
2. **Offline operation:** VHTs may work in areas without reliable internet. The pipeline runs entirely locally with no API calls.
3. **Reproducibility:** The same query with the same knowledge base always produces the same response. LLM-based generation is stochastic.
4. **Auditability:** Every piece of information in the response traces back to a specific page in the source document via citations.

### Why four output formats?

Different users need different levels of detail:

- **VHT_QUICK**: For triage decisions in the field — just the level and one action
- **VHT_STANDARD**: For full patient encounters — complete guidance
- **CLINICIAN**: For clinical officers reviewing VHT work — more technical detail
- **REFERRAL**: For handoff between care levels — structured note format

See also: [Safety and guardrails](safety_and_guardrails.md) for how safety is enforced across all pipeline stages.
