# Response layer validation (25 queries × 2 sources)

- **Generated (UTC)**: 2026-04-01T04:59:53.311063+00:00
- **Method**: `MedicalQASystem.answer_with_response()` after BM25 + guardrail

## Acceptance criteria

- **Guardrail**: `validation_passed == True` for all cases (required sections + triage line).
- **Triage**: `RED` if query matches danger-sign keywords; `YELLOW` for time-sensitive heuristics; else `GREEN`.
- **VHT output**: non-empty `vht_response`, `referral_note`, `quick_summary`.

Per preset: summary table (metrics only), then **full query** and **complete** formatted outputs for each of the 25 queries.

---

## Preset: `who-malaria`

- **Document**: WHO Malaria Guidelines (NCBI Bookshelf)
- **Queries**: 25

### Summary table

| # | Triage | Guardrail OK | Confidence | VHT chars | Referral chars | Quick chars |
|---|--------|--------------|------------|-----------|----------------|-------------|
| 1 | GREEN | True | 0.90 | 1439 | 380 | 123 |
| 2 | GREEN | True | 0.90 | 1487 | 380 | 123 |
| 3 | GREEN | True | 0.90 | 1472 | 380 | 123 |
| 4 | GREEN | True | 0.90 | 1478 | 380 | 123 |
| 5 | GREEN | True | 0.90 | 1434 | 380 | 123 |
| 6 | GREEN | True | 0.90 | 1453 | 380 | 123 |
| 7 | GREEN | True | 0.90 | 1435 | 380 | 123 |
| 8 | GREEN | True | 0.90 | 1444 | 380 | 123 |
| 9 | GREEN | True | 0.90 | 1492 | 380 | 123 |
| 10 | GREEN | True | 0.90 | 1520 | 380 | 123 |
| 11 | GREEN | True | 0.90 | 1521 | 380 | 123 |
| 12 | GREEN | True | 0.90 | 1457 | 380 | 123 |
| 13 | GREEN | True | 0.90 | 1489 | 380 | 123 |
| 14 | GREEN | True | 0.90 | 1465 | 380 | 123 |
| 15 | GREEN | True | 0.90 | 1492 | 380 | 123 |
| 16 | GREEN | True | 0.90 | 1498 | 399 | 123 |
| 17 | GREEN | True | 0.90 | 1462 | 380 | 123 |
| 18 | GREEN | True | 0.90 | 1497 | 380 | 123 |
| 19 | GREEN | True | 0.90 | 1434 | 380 | 123 |
| 20 | GREEN | True | 0.90 | 1578 | 380 | 123 |
| 21 | GREEN | True | 0.90 | 1520 | 380 | 123 |
| 22 | GREEN | True | 0.90 | 1574 | 391 | 123 |
| 23 | GREEN | True | 0.90 | 1439 | 380 | 123 |
| 24 | GREEN | True | 0.90 | 1439 | 380 | 123 |
| 25 | GREEN | True | 0.90 | 1506 | 380 | 123 |

### Full queries and formatted outputs

#### Query 1

**Full query**

> What is the treatment for uncomplicated Plasmodium falciparum malaria?

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 437: References
• WHO Malaria Guidelines (NCBI Bookshelf), Page 308: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 435: References
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** What is the treatment for uncomplicated Plasmodium falciparum malaria?

### 1. References

### References

References

219. Pryce J, Taylor M, Fox T, Hine P. Pyronaridine-artesunate for treating uncomplicated Plasmodium falciparum malaria.

Cochrane Database Syst Rev 2022;6(6) Pubmed Journal...

📄 **Reference:** Page 437

### 2. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

220. . The effect of dosing regimens on the antimalarial efficacy of dihydroartemisinin-piperaquine: a pooled analysis of individual patient

data. PLoS medicine 2013;10(12):e1001564; discussion e1001564 Pubmed Journal

221. Graves PM, Gelband H, Garner P. Primaquine or other 8-aminoquinoline for reducing P. falciparum transmission. The Cochrane

database of systematic reviews 2014;(6):CD008152 Pubmed Journal

222. Wh...

📄 **Reference:** Page 308

### 3. References

### References

References

219. Pryce J, Taylor M, Fox T, Hine P. Pyronaridine-artesunate for treating uncomplicated Plasmodium falciparum malaria.

Cochrane Database Syst Rev 2022;6(6) Pubmed Journal...

📄 **Reference:** Page 435

### 4. knowlesi

### knowlesi

5.2.1.5 Uncomplicated malaria caused by P. vivax, P. ovale, P. malariae or P.

knowlesi

Plasmodium vivax accounts for approximately half of all malaria cases outside Africa [3][250][251]. It is prevalent in the Middle

East, Asia, the Western Pacific and Central and South America. With the exception of the Horn, it is rarer in Africa, where there

is a high prevalence of the Duffy-negative phenotype, particularly in West Africa, although cases are reported in both

Mauritania and ...

📄 **Reference:** Page 190

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

in early infancy. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America 2009;48(12):1704-12

Pubmed Journal

256. Genton B, D'Acremont V, Rare L, Baea K, Reeder JC, Alpers MP, et al. Plasmodium vivax and mixed infections are associated with

severe malaria in children: a prospective cohort study from Papua New Guinea. PLoS medicine 2008;5(6):e127 Pubmed Journal

257. Koch...

📄 **Reference:** Page 310


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 190, Page 308, Page 310, Page 435, Page 437

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 2

**Full query**

> Dosing artemisinin-based combination therapy in children under 5

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 226: Considerations in use of artemisinin-based combination therapy
• WHO Malaria Guidelines (NCBI Bookshelf), Page 443: Intervention:
• WHO Malaria Guidelines (NCBI Bookshelf), Page 443: h
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Dosing artemisinin-based combination therapy in children under 5

### 1. Considerations in use of artemisinin-based combination therapy

### Considerations in use of artemisinin-based combination therapy

Considerations in use of artemisinin-based combination therapy

Oral artemisinin and its derivatives (e.g. artesunate, artemether, dihydroartemisinin) should not be used alone. In order to simplify use,

improve adherence and minimize the availability of oral artemisinin monotherapy, fixed-dose combination ACTs are strongly preferred

to co-blistered or co-dispensed loose tablets and should be used when they are readily availabl...

📄 **Reference:** Page 226

### 2. Intervention:

### Intervention:

Intervention: Artemisinin-based combination therapy...

📄 **Reference:** Page 443

### 3. h

### h

h...

📄 **Reference:** Page 443

### 4. High

### High

High...

📄 **Reference:** Page 443

### 5. High

### High

High

1...

📄 **Reference:** Page 443


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 226, Page 443

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 3

**Full query**

> Severe malaria definition and management

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 403: Publication bias: no serious.
• WHO Malaria Guidelines (NCBI Bookshelf), Page 402: 167
• WHO Malaria Guidelines (NCBI Bookshelf), Page 404: Publication bias: no serious.
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Severe malaria definition and management

### 1. Publication bias: no serious.

### Publication bias: no serious.

children, in the 12 months following administration of the first three doses, protective efficacy against clinical (uncomplicated and

severe) malaria was 51% (95% CI 47-55) (per protocol analysis).

3. [Impact outcome] Protective efficacy (%) against clinical malaria episodes (per protocol analysis) Clinical malaria assessed with:

illness in a child brought to a study facility with a measured temperature of 37.5°C and P. falciparum asexual parasitaemia at a d...

📄 **Reference:** Page 403

### 2. 167

### 167

based

vaccination) 167

month 46.

Pilot

implementation

study 2019–2023

6 Important

1. [Impact outcome] Protective efficacy (%) against clinical malaria episodes (modified intention-to-treat analysis). Per-protocol

analysis protective efficacy 39.0% (95% CI 34.3 to 43.3). Clinical malaria assessed with: illness in a child brought to a study facility

with a measured temperature of 37.5°C and P. falciparum asexual parasitaemia at a density of > 5000 parasites per cubic millimetre o...

📄 **Reference:** Page 402

### 3. Publication bias: no serious.

### Publication bias: no serious.

defined as radiographically proven pneumonia, meningitis established by analysis of cerebrospinal fluid, sepsis (with positive blood

culture), or gastroenteritis with severe dehydration). Laboratory tests and other examinations (chest x-ray, lumbar puncture, blood

culture) to exclude co-morbidities were performed only if there was a clinical suspicion/diagnosis justifying additional investigations.

The study included 450 total participants with three study a...

📄 **Reference:** Page 404

### 4. 5.2.2 Treating severe malaria

### 5.2.2 Treating severe malaria

5.2.2 Treating severe malaria

Mortality from untreated severe malaria (particularly cerebral malaria) approaches 100%. With prompt, effective antimalarial

treatment and supportive care, the rate falls to 10–20% overall. Within the broad definition of severe malaria some syndromes are

associated with lower mortality rates (e.g. severe anaemia) and others with higher mortality rates (e.g. acidosis). The risk for death

increases in the presence of multiple com...

📄 **Reference:** Page 210

### 5. Intervention

### Intervention

Outcome

Timeframe

Study results and

Intervention

Malaria vaccination...

📄 **Reference:** Page 402


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 210, Page 402, Page 403, Page 404

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 4

**Full query**

> When to refer a patient with malaria to hospital?

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 220: Follow-on treatment
• WHO Malaria Guidelines (NCBI Bookshelf), Page 128: Research needs
• WHO Malaria Guidelines (NCBI Bookshelf), Page 163: 4. Appropriate weight-based dosing
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** When to refer a patient with malaria to hospital?

### 1. Follow-on treatment

### Follow-on treatment

Follow-on treatment

The current recommendation of experts is to give parenteral antimalarial drugs for the treatment of severe malaria for a

minimum of 24 h ounce started (irrespective of the patient’s ability to tolerate oral medication earlier) or until the patient can

tolerate oral medication, before giving the oral follow-up treatment.

After initial parenteral treatment, once the patient can tolerate oral therapy, it is essential to continue and complete treatmen...

📄 **Reference:** Page 220

### 2. Research needs

### Research needs

Research needs

The GDG identified the following evidence gaps as requiring further research. These relate to:

•

the optimal duration for PDMC in different geographical and transmission settings, and understanding of the short-, medium-

and long-term benefits of PDMC of different durations; these evaluations should recognize the underlying pattern of post-

discharge death and/or re-admission, and the higher risk of some groups dying soon after discharge; to minimize bias,...

📄 **Reference:** Page 128

### 3. 4. Appropriate weight-based dosing

### 4. Appropriate weight-based dosing

4. Appropriate weight-based dosing

To prolong their useful therapeutic life and ensure that all patients have an equal chance of being cured, the quality of antimalarial drugs

must be ensured, and antimalarial drugs must be given at optimal dosages. Treatment should maximize the likelihood of rapid clinical and

parasitological cure and minimize transmission from the treated infection. To achieve this, dosage regimens should be based on the

patient’s we...

📄 **Reference:** Page 163

### 4. 5.2.1.2 Recurrent falciparum malaria

### 5.2.1.2 Recurrent falciparum malaria

5.2.1.2 Recurrent falciparum malaria

Recurrence of P. falciparum malaria can result from re-infection or recrudescence (treatment failure). Treatment failure may

result from drug resistance or inadequate exposure to the drug due to sub-optimal dosing, poor adherence, vomiting, unusual

pharmacokinetics in an individual, or substandard medicines. It is important to determine from the patient’s history whether he

or she vomited the previous treatment or...

📄 **Reference:** Page 177

### 5. Follow-on treatment

### Follow-on treatment

Follow-on treatment

The current recommendation of experts is to give parenteral antimalarial drugs for the treatment of severe malaria for a minimum

of 24 h once started (irrespective of the patient’s ability to tolerate oral medication earlier) or until the patient can tolerate oral

medication, before giving the oral follow-up treatment.

After initial parenteral treatment, once the patient can tolerate oral therapy, it is essential to continue and complete treatment...

📄 **Reference:** Page 211


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 128, Page 163, Page 177, Page 211, Page 220

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 5

**Full query**

> Pregnancy and malaria treatment recommendations

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 185: Feasibility
• WHO Malaria Guidelines (NCBI Bookshelf), Page 302: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 30: Scope
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Pregnancy and malaria treatment recommendations

### 1. Feasibility

### Feasibility

Feasibility

One consideration in determining the feasibility of the recommendation on treatment of malaria in

the first trimester is that the existing warning against the use of artemisinin in the first trimester

implies the need to consistently screen for pregnancy among all women of childbearing potential

prior to treatment for malaria. However, pregnancy screening is rarely done prior to initiating

malaria treatment. As observed by national programmes, the contraindicati...

📄 **Reference:** Page 185

### 2. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

temperature, and relative humidity: an experimental study in rural Gambia. The Lancet Planetary Health 2018;2(11):e498-e508 Pubmed

Journal Website

114. Norms, standards and processes underpinning development of WHO recommendations on vector control. Geneva: World Health

Organization 2020. Website

115. Sicuri E, Bardají A, Nhampossa T, Maixenchs M, Nhacolo A, Nhalungo D, et al. Cost-effectiveness of intermittent pr...

📄 **Reference:** Page 302

### 3. Scope

### Scope

Scope

The consolidated WHO Guidelines for malaria bring together all recommendations for malaria, including prevention using vector control,

preventive chemotherapy and the vaccine; diagnosis, treatment and elimination strategies. The Guidelines also provide links to other

resources including unpublished evidence reviewed at the time of formulating recommendations, guidance and information on strategic

use of information to drive impact, surveillance, monitoring and evaluation, op...

📄 **Reference:** Page 30

### 4. Implementation

### Implementation

Implementation

Please refer to the WHO policy brief for the implementation of intermittent preventive treatment of malaria in pregnancy using

sulfadoxine-pyrimethamine (IPTp-SP) [128] and the WHO recommendations on antenatal care for a positive pregnancy

experience [130]. A field guide on community deployment of intermittent preventive treatment of malaria in pregnancy with

sulfadoxine-pyrimethamine was released in January 2024 [129]. A manual for subnational tailoring of...

📄 **Reference:** Page 108

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

based therapies, and in how different cultures would value the outcomes being monitored, such

as perceptions around early trimester pregnancy losses, low birthweight and anaemia. However,

artemether-lumefantrine compared to quinine is likely to be a more attractive option because of its

greater availability and the convenience of a shorter, better tolerated treatment. Policy-makers and

implementers will obviously ...

📄 **Reference:** Page 184


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 30, Page 108, Page 184, Page 185, Page 302

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 6

**Full query**

> Drug interactions with artemether lumefantrine

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 184: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 185: Acceptability
• WHO Malaria Guidelines (NCBI Bookshelf), Page 118: Antimalarial medicine
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Drug interactions with artemether lumefantrine

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

based therapies, and in how different cultures would value the outcomes being monitored, such

as perceptions around early trimester pregnancy losses, low birthweight and anaemia. However,

artemether-lumefantrine compared to quinine is likely to be a more attractive option because of its

greater availability and the convenience of a shorter, better tolerated treatment. Policy-makers and

implementers will obviously ...

📄 **Reference:** Page 184

### 2. Acceptability

### Acceptability

Acceptability

In considering the acceptability of artemether-lumefantrine versus quinine treatments, the GDG

looked to how quinine is presently being used and accepted.

Adherence to quinine is low because it is frequently associated with adverse effects, including

cinchonism, nausea and hypoglycaemia [231][243][244]. In a review of 35 national guidelines,

66% recommended oral quinine as first-line treatment for uncomplicated malaria in the first

trimester of pregnancy. O...

📄 **Reference:** Page 185

### 3. Antimalarial medicine

### Antimalarial medicine

Antimalarial medicine

Drug regimens evaluated for IPTsc and found to be effective include SP combined with an aminoquinoline (either AQ or

piperaquine), SP+AS, and artemisinin-based combination therapy including an aminoquinoline (AS-AQ or DHAP)1. SP+AQ has

been widely used for chemoprevention in West Africa and has been shown to be efficacious, safe, well tolerated, available and

inexpensive. In order to reduce the risk of drug resistance to life-saving drugs, fir...

📄 **Reference:** Page 118

### 4. Remarks

### Remarks

Remarks

Longer ACT treatment may be required to achieve > 90% cure rate in areas with artemisinin-resistant P. falciparum, but

there are insufficient trials to make definitive recommendations. A 3-day course of the artemisinin component of ACTs

covers two asexual cycles, ensuring that only a small fraction of parasites remain for clearance by the partner drug, thus

reducing the potential development of resistance to the partner drug. Shorter courses (1–2 days) are therefore not
...

📄 **Reference:** Page 173

### 5. 5.2.1.1.2 Dosing of ACTs

### 5.2.1.1.2 Dosing of ACTs

5.2.1.1.2 Dosing of ACTs

ACT regimens must ensure optimal dosing to prolong their useful therapeutic life, i.e. to maximize the likelihood of rapid

clinical and parasitological cure, minimize transmission and retard drug resistance.

It is essential to achieve effective antimalarial drug concentrations for a sufficient time (exposure) in all target populations in

order to ensure high cure rates. The dosage recommendations below are derived from understanding the ...

📄 **Reference:** Page 173


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 118, Page 173, Page 184, Page 185

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 7

**Full query**

> Prophylaxis for travelers to endemic areas

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 453: Moderate
• WHO Malaria Guidelines (NCBI Bookshelf), Page 453: Moderate
• WHO Malaria Guidelines (NCBI Bookshelf), Page 453: Untitled
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Prophylaxis for travelers to endemic areas

### 1. Moderate

### Moderate

Moderate

Due to serious...

📄 **Reference:** Page 453

### 2. Moderate

### Moderate

Moderate

Due to serious...

📄 **Reference:** Page 453

### 3. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)...

📄 **Reference:** Page 453

### 4. Intervention:

### Intervention:

Intervention: Chloroquine prophylaxis...

📄 **Reference:** Page 453

### 5. Population:

### Population:

Population: Malaria-endemic areas...

📄 **Reference:** Page 453


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 453

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 8

**Full query**

> Rapid diagnostic test interpretation false positives

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 267: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 307: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 447: Target conditions
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Rapid diagnostic test interpretation false positives

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

chemotherapy

prophylaxis

Any method of protection from or prevention of disease; when applied to chemotherapy, it is commonly

termed “chemoprophylaxis”.

prophylaxis, causal

Complete prevention of erythrocytic infection by destroying the pre-erythrocytic forms of the parasite

rapid diagnostic test

(RDT)

Immunochromatographic lateral flow device for rapid detection of malaria parasite antigens

rapid diagnostic ...

📄 **Reference:** Page 267

### 2. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

200. Malaria diagnosis: memorandum from a WHO meeting. Bulletin of the World Health Organization 1988;66(5):575-94 Pubmed

201. Malaria microscopy quality assurance manual, version 2. Geneva: World Health Organization 2016. Website

202. Kawamoto F, Billingsley PF. Rapid diagnosis of malaria by fluorescence microscopy. Parasitology today (Personal ed.)

1992;8(2):69-71 Pubmed

203. Malaria diagnosis: new perspectives....

📄 **Reference:** Page 307

### 3. Target conditions

### Target conditions

•

Patients with malaria who undergoing G6PD testing to inform treatment with primaquine or tafenoquine to prevent

relapses of P. vivax and P. ovale.

•

Index test is semi-quantitative near-patient tests for G6PD.

•

Reference standard is the quality assured G6PD spectrophotometric assay using the adjusted male median (AMM) as

the standardised metric of 100% G6PD activity. For the Standard G6PD biosensor used with the STANDARD G6PD

Analyzer (SB Biosensor, Inc) a suppl...

📄 **Reference:** Page 447

### 4. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

Qualitative FST and (d) consists of 753 participants assessed by CareStart G6PD enrolled in the Lao People’s Democratic Republic. Henriques 2018 (a) and

(c) were chosen, due to having a more complete sample size.

Bancone 2015(a)excluded from meta-analysis, because Bancone 2015 (a) and (b) use the same participants. Difference between two studies are

that(a) uses capillary blood and (b) uses venous blood samples. Ba...

📄 **Reference:** Page 447

### 5. Summary

### Summary

Summary...

📄 **Reference:** Page 447


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 267, Page 307, Page 447

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 9

**Full query**

> G6PD deficiency and primaquine

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 208: Primaquine and glucose-6-phosphate dehydrogenase deficiency
• WHO Malaria Guidelines (NCBI Bookshelf), Page 195: Practical info
• WHO Malaria Guidelines (NCBI Bookshelf), Page 199: Untitled
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** G6PD deficiency and primaquine

### 1. Primaquine and glucose-6-phosphate dehydrogenase deficiency

### Primaquine and glucose-6-phosphate dehydrogenase deficiency

Primaquine and glucose-6-phosphate dehydrogenase deficiency

Any person (male or female) with red cell G6PD activity < 30% of the normal mean has G6PD deficiency and will experience

haemolysis after primaquine. Heterozygote females with higher mean red cell activities may still show substantial haemolysis.

G6PD deficiency is an inherited sex-linked genetic disorder, which is associated with some protection against P. falciparum

...

📄 **Reference:** Page 208

### 2. Practical info

### Practical info

Practical info

Please refer to Testing for G6PD deficiency for safe use of primaquine in radical cure of P. vivax and P. ovale (Policy

brief) [264] and Guide to G6PD deficiency rapid diagnostic testing to support P. vivax radical cure [265].

If G6PD testing is not available, a decision to prescribe or withhold primaquine should be based on the balance of the

probability and benefits of preventing relapse against the risks of primaquine-induced haemolytic anaemia. This dep...

📄 **Reference:** Page 195

### 3. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

In order to prevent relapses of P. vivax and P. ovale, and when the G6PD status of the patient was previously unknown, the

following recommendations are made:

A. If only a qualitative near-patient test for G6PD deficiency is available, tafenoquine single dose treatment or high

dose primaquine (1mg/kg/day for 7 days) should not be given. If by the qualitative test the patient is classified as non-

deficient primaqu...

📄 **Reference:** Page 199

### 4. Benefits and harms

### Benefits and harms

Benefits and harms

Desirable effects:

•

There are no comparative trials of the efficacy or safety of primaquine in people with G6PD

deficiency.

Undesirable effects:

•

Primaquine is known to cause haemolysis in people with G6PD deficiency.

•

Of the 15 trials included in the systematic review, 12 explicitly excluded people with G6PD

deficiency; in three trials, it was unclear whether participants were tested for G6PD deficiency or

excluded. None of the trials rep...

📄 **Reference:** Page 208

### 5. Qualitative near-patient G6PD tests (2024)

### Qualitative near-patient G6PD tests (2024)

Qualitative near-patient G6PD tests (2024)

Qualitative near-patient tests for G6PD deficiency should be used to inform administration of specific treatment regimens to

prevent relapses of P. vivax and P. ovale. G6PD non-deficient individuals can receive 0.5 mg/kg/day primaquine for 14 days or

0.5 mg/kg/day primaquine for 7 days.

•

In males and females, <30% of normal G6PD activity is considered deficient.

•

In patients undergoing G6PD activi...

📄 **Reference:** Page 195


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 195, Page 199, Page 208

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 10

**Full query**

> Malaria vaccine recommendations RTS,S R21

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 159: Certainty of the evidence related to the safety of R21/Matrix-M
• WHO Malaria Guidelines (NCBI Bookshelf), Page 386: Systematic review summary
• WHO Malaria Guidelines (NCBI Bookshelf), Page 162: immunization systems.
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Malaria vaccine recommendations RTS,S R21

### 1. Certainty of the evidence related to the safety of R21/Matrix-M

### Certainty of the evidence related to the safety of R21/Matrix-M

Certainty of the evidence related to the safety of R21/Matrix-M ranged from LOW to MODERATE due to

few or no events, wide CIs and small sample size. While the vaccine was associated with febrile seizures at

a rate of approximately one per 2500 vaccinations, all febrile seizures resolved without sequelae. There was

no imbalance in other severe adverse events (SAEs) among children vaccinated with R21/Matrix-M or with

the cont...

📄 **Reference:** Page 159

### 2. Systematic review summary

### Systematic review summary

Systematic review summary

Six studies form the basis of these recommendations: five were individual randomized controlled trials (RCTs) and one was an open-

label extension study of an included RCT. One RCT was a multicentre study evaluating three or four doses of the RTS,S/AS01 malaria

vaccine compared to no malaria vaccination. One RCT evaluated the seasonal administration of RTS,S/AS01 malaria vaccine alone

compared to SMC alone, and also compared a combinat...

📄 **Reference:** Page 386

### 3. immunization systems.

### immunization systems.

Feasibility

Malaria vaccine introduction is feasible with good and equitable coverage, as seen through routine

immunization systems.

Administrative data from early implementing areas through 46 months of RTS,S/AS01 vaccinations under the

pilot programme showed the following:

•

About 4.2 million RTS,S/AS01 vaccine doses were administered across the three pilot countries and

more than 1.2 million children received their first dose.

•

All three countries reached ...

📄 **Reference:** Page 162

### 4. RTS,S/AS01 vs

### RTS,S/AS01 vs

RTS,S/AS01 vs...

📄 **Reference:** Page 386

### 5. Summary

### Summary

Summary...

📄 **Reference:** Page 386


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 159, Page 162, Page 386

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 11

**Full query**

> Resistance to artemisinin in Southeast Asia

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 226: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 222: Artemisinin-resistant falciparum malaria
• WHO Malaria Guidelines (NCBI Bookshelf), Page 226: Considerations in use of artemisinin-based combination therapy
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Resistance to artemisinin in Southeast Asia

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

for days or weeks after effective treatment. HRP2-detecting RDTs are not suitable for detecting treatment failure. RDTs are slightly less

sensitive for detecting P. malariae and P. ovale. The WHO Malaria RDT Product Testing programme provides comparative data on the

performance of RDT products to guide procurement. Since 2008, 210 products have been evaluated in five rounds of product

testing [207].

For the diagno...

📄 **Reference:** Page 226

### 2. Artemisinin-resistant falciparum malaria

### Artemisinin-resistant falciparum malaria

Artemisinin-resistant falciparum malaria

Artemisinin resistance in P. falciparum is now prevalent in parts of Cambodia, the Lao People’s Democratic Republic,

Myanmar, Thailand and Viet Nam. There is currently no evidence for artemisinin resistance outside these areas. The particular

advantage of artemisinins over other antimalarial drugs is that they kill circulating ring-stage parasites and thus accelerate

therapeutic responses. This is lost in ...

📄 **Reference:** Page 222

### 3. Considerations in use of artemisinin-based combination therapy

### Considerations in use of artemisinin-based combination therapy

Considerations in use of artemisinin-based combination therapy

Oral artemisinin and its derivatives (e.g. artesunate, artemether, dihydroartemisinin) should not be used alone. In order to simplify use,

improve adherence and minimize the availability of oral artemisinin monotherapy, fixed-dose combination ACTs are strongly preferred

to co-blistered or co-dispensed loose tablets and should be used when they are readily availabl...

📄 **Reference:** Page 226

### 4. P. vivax

### P. vivax

In areas with chloroquine-sensitive P. vivax

For chloroquine-sensitive vivax malaria, oral chloroquine at a total dose of 25 mg base/kg bw is effective and well tolerated.

Lower total doses are not recommended, as these encourage the emergence of resistance. Chloroquine is given at an initial

dose of 10 mg base/kg bw, followed by 10 mg/kg bw on the second day and 5 mg/kg bw on the third day. In the past, the initial

10 mg/kg bw dose was followed by 5 mg/kg bw at 6 h, 24 h and 4...

📄 **Reference:** Page 191

### 5. P. vivax

### P. vivax

In areas with chloroquine-sensitive P. vivax

For chloroquine-sensitive vivax malaria, oral chloroquine at a total dose of 25 mg base/kg bw is effective and well tolerated.

Lower total doses are not recommended, as these encourage the emergence of resistance. Chloroquine is given at an initial

dose of 10 mg base/kg bw, followed by 10 mg/kg bw on the second day and 5 mg/kg bw on the third day. In the past, the initial

10-mg/kg bw dose was followed by 5 mg/kg bw at 6 h, 24 h and 4...

📄 **Reference:** Page 192


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 191, Page 192, Page 222, Page 226

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 12

**Full query**

> Hypoglycemia in severe malaria

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 268: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 458: Population:
• WHO Malaria Guidelines (NCBI Bookshelf), Page 211: Treatment of severe malaria
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Hypoglycemia in severe malaria

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

severe anaemia

Haemoglobin concentration of < 5 g/100 mL (haematocrit < 15%)

severe falciparum

malaria

Acute falciparum malaria with signs of severe illness and/or evidence of vital organ dysfunction

single-dose regimen

Administration of a medicine as a single dose to achieve a therapeutic objective

slide positivity rate

Proportion of blood smears found to be positive for Plasmodium among all blood smears exam...

📄 **Reference:** Page 268

### 2. Population:

### Population:

Population: Children with severe malaria (malaria-endemic countries)...

📄 **Reference:** Page 458

### 3. Treatment of severe malaria

### Treatment of severe malaria

Treatment of severe malaria

It is essential that full doses of effective parenteral (or rectal) antimalarial treatment be given promptly in the initial treatment of

severe malaria. This should be followed by a full dose of effective ACT orally. Two classes of medicine are available for parenteral

treatment of severe malaria: artemisinin derivatives (artesunate or artemether) and the cinchona alkaloids (quinine and quinidine).

Parenteral artesunate is the trea...

📄 **Reference:** Page 211

### 4. Systematic review summary

### Systematic review summary

Systematic review summary

Six studies form the basis of these recommendations: five were individual randomized controlled trials (RCTs) and one was an open-

label extension study of an included RCT. One RCT was a multicentre study evaluating three or four doses of the RTS,S/AS01 malaria

vaccine compared to no malaria vaccination. One RCT evaluated the seasonal administration of RTS,S/AS01 malaria vaccine alone

compared to SMC alone, and also compared a combinat...

📄 **Reference:** Page 386

### 5. Benefits and harms

### Benefits and harms

Benefits and harms

Malaria vaccines, provided in a four-dose schedule, have been demonstrated in clinical trials to significantly

reduce clinical malaria, providing substantial added protection to that already given by existing malaria

preventive measures (i.e. ITNs and/or seasonal malaria chemoprevention (SMC)). In addition, pilot

implementation showed that the introduction of the vaccine through routine childhood immunization

programmes in Ghana, Kenya and Malawi r...

📄 **Reference:** Page 157


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 157, Page 211, Page 268, Page 386, Page 458

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 13

**Full query**

> Fluid management in severe malaria adults

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 213: Additional aspects of management
• WHO Malaria Guidelines (NCBI Bookshelf), Page 212: Management of complications
• WHO Malaria Guidelines (NCBI Bookshelf), Page 211: Clinical assessment
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Fluid management in severe malaria adults

### 1. Additional aspects of management

### Additional aspects of management

Additional aspects of management

Fluid therapy

Fluid requirements should be assessed individually. Adults with severe malaria are very vulnerable to fluid overload, while children

are more likely to be dehydrated. The fluid regimen must also be adapted to the infusion of antimalarial drugs. Rapid bolus infusion

of colloid or crystalloids is contraindicated. If available, haemofiltration should be started early for acute kidney injury or severe

metabolic...

📄 **Reference:** Page 213

### 2. Management of complications

### Management of complications

Management of complications

Severe malaria is associated with a variety of manifestations and complications, which must be recognized promptly and treated

as shown below.

Immediate clinical management of severe manifestations and complications of P. falciparum malaria...

📄 **Reference:** Page 212

### 3. Clinical assessment

### Clinical assessment

Clinical assessment

Severe malaria is a medical emergency. An open airway should be secured in unconscious patients and breathing and circulation

assessed. The patient should be weighed or body weight estimated, so that medicines, including antimalarial drugs and fluids, can

be given appropriately. An intravenous cannula should be inserted, and blood glucose (rapid test), haematocrit or haemoglobin,

parasitaemia and, in adults, renal function should be measured immed...

📄 **Reference:** Page 211

### 4. Benefits and harms

### Benefits and harms

Benefits and harms

Is parenteral artesunate superior to parenteral quinine in preventing death from severe malaria?

Desirable effects:

•

In children > 12 years and adults, parenteral artesunate probably prevents more deaths than

intramuscular artemether (moderate-quality evidence).

•

No randomized controlled trials have been conducted in children aged ≤ 12 years.

--

Is intramuscular artemether superior to parenteral quinine in preventing death from severe malaria...

📄 **Reference:** Page 218

### 5. Publication bias: no serious.

### Publication bias: no serious.

defined as radiographically proven pneumonia, meningitis established by analysis of cerebrospinal fluid, sepsis (with positive blood

culture), or gastroenteritis with severe dehydration). Laboratory tests and other examinations (chest x-ray, lumbar puncture, blood

culture) to exclude co-morbidities were performed only if there was a clinical suspicion/diagnosis justifying additional investigations.

The study included 450 total participants with three study a...

📄 **Reference:** Page 404


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 211, Page 212, Page 213, Page 218, Page 404

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 14

**Full query**

> Exchange transfusion malaria criteria

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 213: Additional aspects of management
• WHO Malaria Guidelines (NCBI Bookshelf), Page 128: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 235: Research needs
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Exchange transfusion malaria criteria

### 1. Additional aspects of management

### Additional aspects of management

Additional aspects of management

Fluid therapy

Fluid requirements should be assessed individually. Adults with severe malaria are very vulnerable to fluid overload, while children

are more likely to be dehydrated. The fluid regimen must also be adapted to the infusion of antimalarial drugs. Rapid bolus infusion

of colloid or crystalloids is contraindicated. If available, haemofiltration should be started early for acute kidney injury or severe

metabolic...

📄 **Reference:** Page 213

### 2. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

post-discharge. The main outcomes of interest were the impact of PDMC on re-admission (all-cause and severe anaemia),

mortality (all-cause), severe anaemia, and blood transfusion. Other outcomes of interest included confirmed clinical malaria,

severe malaria, anaemia, adverse events, and parasite prevalence. Three randomized double-blind placebo-controlled trials were

included in the review. All the trials were con...

📄 **Reference:** Page 128

### 3. Research needs

### Research needs

Research needs

•

Further evidence is needed on the impact (prevalence and incidence of malaria infection at the community level ) and

potential harms/unintended consequences of TDA for malaria in very low to low transmission or post-elimination settings.

•

Evidence is needed on the acceptability, feasibility, impact (prevalence and incidence of malaria infection at the community

level) and potential harms/unintended consequences (death, hospital admission, severe anaemi...

📄 **Reference:** Page 235

### 4. Research needs

### Research needs

Research needs

•

Further evidence is needed on the impact (prevalence and incidence of malaria infection at the community level) and potential

harms/unintended consequences of RDA.

•

Evidence is needed on the acceptability, feasibility, impact (prevalence and incidence of malaria infection at the community

level) and potential harms/unintended consequences (death, hospital admission, severe anaemia or any severe adverse

event) of safe provision (including testing for G...

📄 **Reference:** Page 245

### 5. Research needs

### Research needs

Research needs

•

Further evidence is needed on the impact (incidence or prevalence of malaria infection at the community level) and

potential harms/ unintended consequences of MDA for P. vivax.

•

Evidence is needed on the acceptability, feasibility, impact (incidence or prevalence of malaria infection at the community

level) and potential harms/unintended consequences (death, hospital admission, severe anaemia or any severe adverse

event) of safe provision (including t...

📄 **Reference:** Page 150


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 128, Page 150, Page 213, Page 235, Page 245

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 15

**Full query**

> Cerebral malaria supportive care

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 210: 5.2.2 Treating severe malaria
• WHO Malaria Guidelines (NCBI Bookshelf), Page 212: Continuing supportive care
• WHO Malaria Guidelines (NCBI Bookshelf), Page 220: Continuing supportive care
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Cerebral malaria supportive care

### 1. 5.2.2 Treating severe malaria

### 5.2.2 Treating severe malaria

5.2.2 Treating severe malaria

Mortality from untreated severe malaria (particularly cerebral malaria) approaches 100%. With prompt, effective antimalarial

treatment and supportive care, the rate falls to 10–20% overall. Within the broad definition of severe malaria some syndromes are

associated with lower mortality rates (e.g. severe anaemia) and others with higher mortality rates (e.g. acidosis). The risk for death

increases in the presence of multiple com...

📄 **Reference:** Page 210

### 2. Continuing supportive care

### Continuing supportive care

Continuing supportive care

Patients with severe malaria require intensive nursing care, preferably in an intensive care unit where possible. Clinical

observations should be made as frequently

as possible and should include monitoring of vital signs, coma score and urine output.

Blood glucose should be monitored every 4 h, if possible, particularly in unconscious patients....

📄 **Reference:** Page 212

### 3. Continuing supportive care

### Continuing supportive care

Continuing supportive care

Patients with severe malaria require intensive nursing care, preferably in an intensive care unit where possible. Clinical

observations should be made as frequently

as possible and should include monitoring of vital signs, coma score and urine

output. Blood glucose should be monitored every 4 h, if possible, particularly in unconscious patients.

Please refer to The use of rectal artesunate as a pre-referral treatment for severe Plas...

📄 **Reference:** Page 220

### 4. Therapeutic objectives

### Therapeutic objectives

Therapeutic objectives

The main objective of the treatment of severe malaria is to prevent the patient from dying. Secondary objectives are prevention of

disabilities and prevention of recrudescent infection.

Death from severe malaria often occurs within hours of admission to a hospital or clinic, so it is essential that therapeutic

concentrations of a highly effective antimalarial drug be achieved as soon as possible. Management of severe malaria comprises

mainl...

📄 **Reference:** Page 211

### 5. Publication bias: no serious.

### Publication bias: no serious.

142. Inconsistency: no serious. Indirectness: no serious. Imprecision: serious. Downgraded two levels for imprecision: zero

events in the control group. Publication bias: no serious.

143. [Safety outcome] Cerebral malaria assessed with positive P. falciparum rapid diagnostic test or by microscopy, with impaired

consciousness (Glasgow coma score <11 or Blantyre coma score <3 or assessed as P or U on the AVPU scale (“Alert, Voice, Pain,

Unresponsive”). Pilot ...

📄 **Reference:** Page 411


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 210, Page 211, Page 212, Page 220, Page 411

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 16

**Full query**

> Artesunate dose for severe malaria IV

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Confirm patient weight before calculating dose
**Step 2:** Explain dosing schedule to caregiver
**Step 3:** Observe first dose if possible
**Step 4:** Complete full course even if symptoms improve

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 155: Schedule
• WHO Malaria Guidelines (NCBI Bookshelf), Page 211: Treatment of severe malaria
• WHO Malaria Guidelines (NCBI Bookshelf), Page 22: Untitled
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Confirm patient weight before calculating dose
• Explain dosing schedule to caregiver
• Observe first dose if possible

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Artesunate dose for severe malaria IV

### 1. Schedule

### Schedule

Schedule

Malaria vaccines should be provided in a four-dose schedule in children from 5 months of age for the reduction of malaria disease and

burden. Countries may choose to give the first vaccine dose earlier than 5 months of age on the basis of operational considerations, to

increase coverage or impact.[iv]

The minimum interval between any doses is four weeks; however, to achieve prolonged protection, the fourth dose should be given

6–18 months after the third dose. To impr...

📄 **Reference:** Page 155

### 2. Treatment of severe malaria

### Treatment of severe malaria

Treatment of severe malaria

It is essential that full doses of effective parenteral (or rectal) antimalarial treatment be given promptly in the initial treatment of

severe malaria. This should be followed by a full dose of effective ACT orally. Two classes of medicine are available for parenteral

treatment of severe malaria: artemisinin derivatives (artesunate or artemether) and the cinchona alkaloids (quinine and quinidine).

Parenteral artesunate is the trea...

📄 **Reference:** Page 211

### 3. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

Where complete treatment of severe malaria is not possible, but injections are available, adults and children

should be given a single intramuscular dose of artesunate, and referred to an appropriate facility for further care.

Where intramuscular artesunate is not available, intramuscular artemether or, if that is not available,

intramuscular quinine should be used.

Where intramuscular injection of artesunate is n...

📄 **Reference:** Page 22

### 4. Artemether

### Artemether

Artemether

Artemether is two to three times less active than its main metabolite dihydroartemisinin. Artemether can be given as an oil-

based intramuscular injection or orally. In severe falciparum malaria, the concentration of the parent compound predominates

after intramuscular injection, whereas parenteral artesunate is hydrolysed rapidly and almost completely to dihydroartemisinin.

Given intramuscularly, artemether may be absorbed more slowly and more erratically than wat...

📄 **Reference:** Page 217

### 5. Pre-referral treatment options (2015)

### Pre-referral treatment options (2015)

Pre-referral treatment options (2015)

Where complete treatment of severe malaria is not possible, but injections are available, adults and children should be given a

single intramuscular dose of artesunate, and referred to an appropriate facility for further care. Where intramuscular artesunate

is not available, intramuscular artemether or, if that is not available, intramuscular quinine should be used.

Where intramuscular injection of artesunate is...

📄 **Reference:** Page 220


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 22, Page 155, Page 211, Page 217, Page 220

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 17

**Full query**

> Rectal artesunate pre-referral children

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 219: 5.2.2.3 Pre-referral treatment options
• WHO Malaria Guidelines (NCBI Bookshelf), Page 221: GRADE
• WHO Malaria Guidelines (NCBI Bookshelf), Page 187: Untitled
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Rectal artesunate pre-referral children

### 1. 5.2.2.3 Pre-referral treatment options

### 5.2.2.3 Pre-referral treatment options

5.2.2.3 Pre-referral treatment options

The risk for death from severe malaria is greatest in the first 24 h, yet, in most malaria-endemic countries, the transit time

between referral and arrival at a health facility where intravenous treatment can be administered is usually long, thus delaying

the start of appropriate antimalarial treatment. During this time, the patient may deteriorate or die. It is therefore recommended

that patients, particularl...

📄 **Reference:** Page 219

### 2. GRADE

### GRADE

GRADE

In a systematic review of pre-referral treatment for suspected severe malaria, in a single large randomized controlled trial of 17

826 children and adults in Bangladesh, Ghana and the United Republic of Tanzania, pre-referral rectal artesunate was

compared with placebo [286].

In comparison with placebo:

•

Rectal artesunate reduced mortality by about 25% in children < 6 years (RR, 0.74; 95% CI, 0.59–0.93; one trial, 8050

participants, moderate- quality evidence).

•

Recta...

📄 **Reference:** Page 221

### 3. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

exposure in this vulnerable population. The available evidence for artemether + lumefantrine, SP and chloroquine does not

indicate dose modification at this time, but young children should be closely monitored, as reduced drug exposure may

increase the risk for treatment failure. Limited studies of amodiaquine and mefloquine showed no significant effect of age

on plasma concentration profiles.

In community situati...

📄 **Reference:** Page 187

### 4. Pre-referral treatment options (2015)

### Pre-referral treatment options (2015)

Pre-referral treatment options (2015)

Where complete treatment of severe malaria is not possible, but injections are available, adults and children should be given a

single intramuscular dose of artesunate, and referred to an appropriate facility for further care. Where intramuscular artesunate

is not available, intramuscular artemether or, if that is not available, intramuscular quinine should be used.

Where intramuscular injection of artesunate is...

📄 **Reference:** Page 220

### 5. Other considerations

### Other considerations

Other considerations

The guideline development group could find no plausible explanation for the finding of increased mortality among older

children and adults in Asia who received rectal artesunate, which may be due to chance. Further trials would provide

clarification but are unlikely to be done. The group was therefore unable to recommend its use in older children and adults.

In the absence of direct evaluations of parenteral antimalarial drugs for pre- referral ...

📄 **Reference:** Page 221


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 187, Page 219, Page 220, Page 221

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 18

**Full query**

> Malaria in HIV coinfection

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 188: 5.2.1.4.3 Patients co-infected with HIV
• WHO Malaria Guidelines (NCBI Bookshelf), Page 156: Vaccination of special populations
• WHO Malaria Guidelines (NCBI Bookshelf), Page 230: Acceptability
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Malaria in HIV coinfection

### 1. 5.2.1.4.3 Patients co-infected with HIV

### 5.2.1.4.3 Patients co-infected with HIV

5.2.1.4.3 Patients co-infected with HIV

There is considerable geographical overlap between malaria and HIV infection, and many people are co-infected.

Worsening HIV-related immunosuppression may lead to more severe manifestations of malaria. In HIV-infected pregnant

women, the adverse effects of placental malaria on birth weight are increased. In areas of stable endemic malaria, HIV-

infected patients who are partially immune to malaria may have m...

📄 **Reference:** Page 188

### 2. Vaccination of special populations

### Vaccination of special populations

Vaccination of special populations

Malnourished children may be at particular risk of malaria infection and can be vaccinated with either vaccine. RTS,S/AS01 can be

given to children with HIV infection.

RTS,S/AS01 has been evaluated in infants with a history of preterm birth (before 37 weeks’ gestation) and/or low birth weight, in HIV-

exposed or in HIV-infected infants and children, and in malnourished infants and children. The vaccine was found to be...

📄 **Reference:** Page 156

### 3. Acceptability

### Acceptability

Acceptability

The acceptability of MTaT was reported in three qualitative studies identified by the systematic review

(Bhamani et al unpublished evidence). One study in western Kenya found that the community engaged in

an MTaT intervention reported concerns over testing in the absence of symptoms. These concerns were

mostly related to the fear of covert HIV testing and some lack of understanding of the possibility of

asymptomatic malaria. Other issues related to acceptabi...

📄 **Reference:** Page 230

### 4. 5.2.1.4.3. Patients co-infected with HIV

### 5.2.1.4.3. Patients co-infected with HIV

5.2.1.4.3. Patients co-infected with HIV...

📄 **Reference:** Page 443

### 5. Diagnosis of malaria

### Diagnosis of malaria

Diagnosis of malaria

In patients with suspected severe malaria and in other high-risk groups, such as patients living with HIV/AIDS, absence or delay of

parasitological diagnosis should not delay an immediate start of antimalarial treatment.

At present, molecular diagnostic tools based on nucleic-acid amplification techniques (e.g. loop-mediated isothermal amplification or

polymerase chain reaction [PCR]) do not have a role in the clinical management of malaria.

Wh...

📄 **Reference:** Page 164


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 156, Page 164, Page 188, Page 230, Page 443

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 19

**Full query**

> Species Plasmodium vivax relapse treatment

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 190: knowlesi
• WHO Malaria Guidelines (NCBI Bookshelf), Page 310: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 34: Etiology
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Species Plasmodium vivax relapse treatment

### 1. knowlesi

### knowlesi

5.2.1.5 Uncomplicated malaria caused by P. vivax, P. ovale, P. malariae or P.

knowlesi

Plasmodium vivax accounts for approximately half of all malaria cases outside Africa [3][250][251]. It is prevalent in the Middle

East, Asia, the Western Pacific and Central and South America. With the exception of the Horn, it is rarer in Africa, where there

is a high prevalence of the Duffy-negative phenotype, particularly in West Africa, although cases are reported in both

Mauritania and ...

📄 **Reference:** Page 190

### 2. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

in early infancy. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America 2009;48(12):1704-12

Pubmed Journal

256. Genton B, D'Acremont V, Rare L, Baea K, Reeder JC, Alpers MP, et al. Plasmodium vivax and mixed infections are associated with

severe malaria in children: a prospective cohort study from Papua New Guinea. PLoS medicine 2008;5(6):e127 Pubmed Journal

257. Koch...

📄 **Reference:** Page 310

### 3. Etiology

### Etiology

Etiology

Malaria is a life-threatening disease caused by the infection of red blood cells with protozoan parasites of the genus Plasmodium that are

transmitted to people through the bites of infected female Anopheles mosquitoes. Four species of Plasmodium (P. falciparum, P. vivax, P.

malariae and P. ovale) most commonly infect humans. P. falciparum and P. vivax are the most prevalent species and P. falciparum is the

most dangerous. A fifth species, P. knowlesi (a species of Pla...

📄 **Reference:** Page 34

### 4. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

272. Verma R, Commons RJ, Gupta A, Rahi M, Nitika, Bharti PK, et al. Safety and efficacy of primaquine in patients with Plasmodium

vivax malaria from South Asia: a systematic review and individual patient data meta-analysis. BMJ global health 2023;8(12) Pubmed

Journal

273. Mehdipour P, Rajasekhar M, Dini S, Zaloumis S, Abreha T, Adam I, et al. Effect of adherence to primaquine on the risk of

Plasmodium vivax recur...

📄 **Reference:** Page 311

### 5. Malaria vaccine pipeline

### Malaria vaccine pipeline

Malaria vaccine pipeline

Two malaria vaccines are WHO-prequalified and recommended for use: RTS,S/AS01 and R21/Matrix-M. Both are pre-erythrocytic

vaccines that prevent P. falciparum infection and subsequent illness and death in children; the vaccines are not designed to interrupt

malaria transmission. The recommended malaria vaccines prevent P. falciparum malaria. There is no known cross-protection with

other Plasmodium species. However, in areas where P. falci...

📄 **Reference:** Page 153


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 34, Page 153, Page 190, Page 310, Page 311

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 20

**Full query**

> Monitoring after antimalarial treatment failure

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 224: Therapeutic efficacy
• WHO Malaria Guidelines (NCBI Bookshelf), Page 22: Monitoring efficacy and safety of antimalarial drugs and resistance (2010)
• WHO Malaria Guidelines (NCBI Bookshelf), Page 224: Monitoring efficacy and safety of antimalarial drugs and resistance (2010)
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Monitoring after antimalarial treatment failure

### 1. Therapeutic efficacy

### Therapeutic efficacy

Therapeutic efficacy

Monitoring of therapeutic efficacy in falciparum malaria involves assessing clinical and parasitological outcomes of treatment

for at least 28 days after the start of adequate treatment and monitoring for the reappearance of parasites in blood. The exact

duration of post-treatment follow-up is based on the elimination half- life of the partner drug in the ACT being evaluated. Tools

for monitoring antimalaria drug efficacy can be found on the WHO...

📄 **Reference:** Page 224

### 2. Monitoring efficacy and safety of antimalarial drugs and resistance (2010)

### Monitoring efficacy and safety of antimalarial drugs and resistance (2010)

Monitoring efficacy and safety of antimalarial drugs and resistance (2010)

All malaria programmes should regularly monitor the therapeutic efficacy of antimalarial drugs using the standard

WHO protocols.

An antimalarial medicine that is recommended in the national malaria treatment policy should be changed if the

total treatment failure proportion is ≥ 10%, as assessed in vivo by monitoring therapeutic efficacy.
...

📄 **Reference:** Page 22

### 3. Monitoring efficacy and safety of antimalarial drugs and resistance (2010)

### Monitoring efficacy and safety of antimalarial drugs and resistance (2010)

Monitoring efficacy and safety of antimalarial drugs and resistance (2010)

All malaria programmes should regularly monitor the therapeutic efficacy of antimalarial drugs using the standard WHO

protocols.

An antimalarial medicine that is recommended in the national malaria treatment policy should be changed if the total treatment

failure proportion is ≥ 10%, as assessed in vivo by monitoring therapeutic efficacy.
...

📄 **Reference:** Page 224

### 4. National adaptation and implementation (2010)

### National adaptation and implementation (2010)

National adaptation and implementation (2010)

The choice of ACTs in a country or region should be based on optimal efficacy, safety and adherence.

An antimalarial medicine that is recommended in the national malaria treatment policy should be changed if the total

treatment failure proportion is ≥ 10%, as assessed in vivo by monitoring therapeutic efficacy.

Introduction of a new antimalarial medicine in the national treatment policy should be...

📄 **Reference:** Page 22

### 5. National adaptation and implementation (2010)

### National adaptation and implementation (2010)

National adaptation and implementation (2010)

The choice of ACTs in a country or region should be based on optimal efficacy, safety and adherence.

An antimalarial medicine that is recommended in the national malaria treatment policy should be changed if the total treatment failure

proportion is ≥ 10%, as assessed in vivo by monitoring therapeutic efficacy.

Introduction of a new antimalarial medicine in the national treatment policy should be...

📄 **Reference:** Page 227


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 22, Page 224, Page 227

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 21

**Full query**

> Quality assurance microscopy

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 165: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 225: General guiding principles for choosing a case management strategy and tools
• WHO Malaria Guidelines (NCBI Bookshelf), Page 164: Parasitological diagnosis
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Quality assurance microscopy

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

•

high sensitivity, if the performance of microscopy is high;

•

differentiation of Plasmodia species;

•

determination of parasite densities – notably identification of hyperparasitaemia;

•

detection of gametocytaemia;

•

allows monitoring of responses to therapy and

•

can be used to diagnose many other conditions.

Good performance of microscopy can be difficult to maintain, because of the requirements for a...

📄 **Reference:** Page 165

### 2. General guiding principles for choosing a case management strategy and tools

### General guiding principles for choosing a case management strategy and tools

General guiding principles for choosing a case management strategy and tools

Choosing a diagnostic strategy

The two methods currently considered suitable for routine patient management are light microscopy and RDTs. Different strategies

may be adopted in different health care settings. The choice between RDTs and microscopy depends on local circumstances,

including the skills available, the patient case-load, t...

📄 **Reference:** Page 225

### 3. Parasitological diagnosis

### Parasitological diagnosis

Parasitological diagnosis

The benefit of parasitological diagnosis relies entirely on an appropriate management response of health care providers. The two

methods used routinely for parasitological diagnosis of malaria are light microscopy and immunochromatographic RDTs. The latter

detect parasite-specific antigens or enzymes that are either genus or species specific.

Both microscopy and RDTs must be supported by a quality assurance programme. Antimalarial trea...

📄 **Reference:** Page 164

### 4. Guidance

### Guidance

Guidance

The practical guidance on the use of qualitative near-patient tests for G6PD deficiency should include

all aspects of safe implementation of a new diagnostic test e.g. implementation plan, clear national

guidelines, quality assurance and prequalification of tests, training of users, quality assurance of

testing, and selection of the type of health services where these tests should be deployed. In addition

the guidance should also include specific information on the an...

📄 **Reference:** Page 196

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

200. Malaria diagnosis: memorandum from a WHO meeting. Bulletin of the World Health Organization 1988;66(5):575-94 Pubmed

201. Malaria microscopy quality assurance manual, version 2. Geneva: World Health Organization 2016. Website

202. Kawamoto F, Billingsley PF. Rapid diagnosis of malaria by fluorescence microscopy. Parasitology today (Personal ed.)

1992;8(2):69-71 Pubmed

203. Malaria diagnosis: new perspectives....

📄 **Reference:** Page 307


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 164, Page 165, Page 196, Page 225, Page 307

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 22

**Full query**

> Integrated community case management fever

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Check temperature – feel child's body, hot to touch?
**Step 2:** Remove extra clothing
**Step 3:** Wipe with cool (not cold) cloth
**Step 4:** Offer frequent small drinks if able to swallow
**Step 5:** Continue breastfeeding if baby

**MONITORING:**

• Check temperature every 4 hours
• Watch for danger signs (cannot drink, convulsions, lethargy)
• If fever >3 days → refer immediately

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 164: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 227: Other operational issues in managing effective treatment
• WHO Malaria Guidelines (NCBI Bookshelf), Page 225: General guiding principles for choosing a case management strategy and tools
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Check temperature – feel child's body, hot to touch?
• Remove extra clothing
• Wipe with cool (not cold) cloth

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Integrated community case management fever

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

In malaria-endemic areas, malaria should be suspected in any patient presenting with a history of fever or temperature ≥ 37.5 °C and

no other obvious cause. In areas in which malaria transmission is stable (or during the high-transmission period of seasonal malaria),

malaria should also be suspected in children with palmar pallor or a haemoglobin concentration of < 8 g/dL. High-transmission settings

include many pa...

📄 **Reference:** Page 164

### 2. Other operational issues in managing effective treatment

### Other operational issues in managing effective treatment

Other operational issues in managing effective treatment

Individual patients derive the maximum benefit from an ACT if they can access it within 24–48 h of the onset of malaria symptoms.

The impact in reducing transmission at a population level depends on high coverage rates and the transmission intensity. Thus, to

optimize the benefits of deploying ACTs, they should be available in the public health delivery system, the private se...

📄 **Reference:** Page 227

### 3. General guiding principles for choosing a case management strategy and tools

### General guiding principles for choosing a case management strategy and tools

General guiding principles for choosing a case management strategy and tools

Choosing a diagnostic strategy

The two methods currently considered suitable for routine patient management are light microscopy and RDTs. Different strategies

may be adopted in different health care settings. The choice between RDTs and microscopy depends on local circumstances,

including the skills available, the patient case-load, t...

📄 **Reference:** Page 225

### 4. Global vector control response 2017–2030

### Global vector control response 2017–2030

Global vector control response 2017–2030

The vision of WHO and the broader infectious diseases community is a world free of human suffering from vector-borne diseases. In

2017, the World Health Assembly welcomed the Global vector control response 2017–2030 [16] (GVCR) and adopted a resolution to

promote an integrated approach to the control of vector-borne diseases. The approach builds on the concept of integrated vector

management (IVM), but wit...

📄 **Reference:** Page 37

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

G6PD

glucose-6-phosphate dehydrogenase

HBHI

High burden to high impact approach

HFCA

health-facility catchment area

HRP2

histidine-rich protein 2

ICER

incremental cost-effectiveness ratio

IHR

International Health Regulation

IPTi

intermittent preventive treatment in infants, now referred to as perennial malaria chemoprevention (PMC)

IPTp

intermittent preventive treatment in pregnancy

IPTsc

intermittent...

📄 **Reference:** Page 28


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 28, Page 37, Page 164, Page 225, Page 227

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 23

**Full query**

> Ethics of placebo-controlled malaria trials

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 280: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 108: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 453: parasitaemia
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Ethics of placebo-controlled malaria trials

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

•

Dr Anna Maria van Eijk, Liverpool School of Tropical Medicine, Liverpool, United Kingdom of Great Britain and Northern Ireland

Perennial Malaria Chemoprevention (PMC) (formerly Intermittent Preventive Treatment in infants or IPTi)

•

Dr Christina Carlson, Division of Parasitic Diseases and Malaria, Centers for Disease Control and Prevention, Atlanta, United

States of America

•

Dr Laura Steinhardt, Malaria Bran...

📄 **Reference:** Page 280

### 2. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

supplemented by a cross-cutting review on chemoprevention and drug resistance (Plowe unpublished evidence), a civil society

consultation report on chemoprevention (CS4ME unpublished evidence) and contributions from the GDG membership, which

included former and current national malaria programme representatives. The GDG was supported by a Steering Group, which

included representatives from the WHO Departments for Se...

📄 **Reference:** Page 108

### 3. parasitaemia

### parasitaemia

P. vivax

parasitaemia

Relative risk 0.02

(CI 95% 0 — 0.26)

Based on data from 951

participants in 1 studies.

(Randomized controlled)...

📄 **Reference:** Page 453

### 4. Anaemia in third

### Anaemia in third

Anaemia in third

Relative risk 0.95

(CI 95% 0.9 — 1.01)

Based on data from 951

participants in 1 studies.

(Randomized controlled)...

📄 **Reference:** Page 453

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

post-discharge. The main outcomes of interest were the impact of PDMC on re-admission (all-cause and severe anaemia),

mortality (all-cause), severe anaemia, and blood transfusion. Other outcomes of interest included confirmed clinical malaria,

severe malaria, anaemia, adverse events, and parasite prevalence. Three randomized double-blind placebo-controlled trials were

included in the review. All the trials were con...

📄 **Reference:** Page 128


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 108, Page 128, Page 280, Page 453

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 24

**Full query**

> Vector control bed nets IRS

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 297: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 298: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 338: measurements
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Vector control bed nets IRS

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

26. REX Consortium. Heterogeneity of selection and the evolution of resistance. Trends in ecology & evolution 2013;28(2):110-8 Pubmed

Journal

27. Sternberg ED, Thomas MB. Insights from agriculture for the management of insecticide resistance in disease vectors. Evolutionary

applications 2018;11(4):404-414 Pubmed Journal

28. Huijben S, Paaijmans KP. Putting evolution in elimination: Winning our ongoing battle with ...

📄 **Reference:** Page 297

### 2. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

44. Snow RW, Lindsay SW, Hayes RJ, Greenwood BM. Permethrin-treated bed nets (mosquito nets) prevent malaria in Gambian children.

Transactions of The Royal Society of Tropical Medicine and Hygiene 1988;82(6):838-842 Pubmed Journal Website

45. Russell TL, Lwetoijera DW, Maliti D, Chipwaza B, Kihonda J, Charlwood JD, et al. Impact of promoting longer-lasting insecticide

treatment of bed nets upon malaria transmission...

📄 **Reference:** Page 298

### 3. measurements

### measurements

measurements

IRS

IRS

0.01) in intervention villages. (Data on

numbers of participants at follow-up not

provided)...

📄 **Reference:** Page 338

### 4. Acceptability

### Acceptability

Acceptability

The systematic review reported that wall decolourization, bad smell, an increase in bed bug nuisance,

and contamination of food grains were reported by study participants in India after spraying with

DDT [78]. However, these factors may depend on the insecticide and formulation used. In another study

conducted in Pakistan [56], no persistent odour or residue was reported after spraying with the pyrethroid

insecticide alpha-cypermethrin. In this same study, i...

📄 **Reference:** Page 68

### 5. 4.1.1 Interventions recommended for large-scale deployment

### 4.1.1 Interventions recommended for large-scale deployment

4.1.1 Interventions recommended for large-scale deployment

Interventions that are recommended for large-scale deployment in terms of malaria vector control are those that have proven

protective efficacy to reduce or prevent infection and/or disease in humans and are broadly applicable for populations at risk of

malaria in most epidemiological and ecological settings.

Vector control interventions applicable for all populations at...

📄 **Reference:** Page 41


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 41, Page 68, Page 297, Page 298, Page 338

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 25

**Full query**

> Elimination strategies and surveillance

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• WHO Malaria Guidelines (NCBI Bookshelf), Page 228: 6. Interventions in the final phase of elimination and prevention of re-establishment
• WHO Malaria Guidelines (NCBI Bookshelf), Page 30: Scope
• WHO Malaria Guidelines (NCBI Bookshelf), Page 146: (2022)
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Elimination strategies and surveillance

### 1. 6. Interventions in the final phase of elimination and prevention of re-establishment

### 6. Interventions in the final phase of elimination and prevention of re-establishment

6. Interventions in the final phase of elimination and prevention of re-establishment

The Global technical strategy for malaria 2016-2030 [4] urges all malaria-endemic countries to accelerate towards elimination and

attainment of malaria-free status. WHO recommends that all countries ensure access to malaria prevention, diagnosis and treatment as

part of universal health coverage; recommendations relate...

📄 **Reference:** Page 228

### 2. Scope

### Scope

Scope

The consolidated WHO Guidelines for malaria bring together all recommendations for malaria, including prevention using vector control,

preventive chemotherapy and the vaccine; diagnosis, treatment and elimination strategies. The Guidelines also provide links to other

resources including unpublished evidence reviewed at the time of formulating recommendations, guidance and information on strategic

use of information to drive impact, surveillance, monitoring and evaluation, op...

📄 **Reference:** Page 30

### 3. (2022)

### (2022)

MDA to reduce transmission of P. vivax (2022)

In areas with P. vivax transmission, antimalarial medicine can be given as chemoprevention through mass drug administration

(MDA) to reduce transmission.

•

MDA may quickly reduce transmission of P. vivax, but the effect wanes within 1–3 months. Therefore, if MDA is

implemented, it should be one of several components of a robust malaria elimination programme (including, at minimum,

good coverage of case-based surveillance with parasi...

📄 **Reference:** Page 146

### 4. (2022)

### (2022)

MDA to reduce transmission of P. vivax (2022)

In areas with P. vivax transmission, antimalarial medicine can be given as chemoprevention through mass drug

administration (MDA) to reduce transmission.

Remark:

•

MDA may quickly reduce transmission of P. vivax, but the effect wanes within 1–3 months. Therefore, if MDA is

implemented, it should be one of several components of a robust malaria elimination programme (including, at

minimum, good coverage of case-based surveillance wi...

📄 **Reference:** Page 15

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

problem-solving approach using local data to identify recommendations that are relevant at a country level and based on local

context, defining stratum-specific packages of interventions that optimize impact and are prioritized for resource allocation. This shift

moves away from overly prescriptive recommendations and will clearly distinguish evidence-informed recommendations from contextual

considerations. The con...

📄 **Reference:** Page 36


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 15, Page 30, Page 36, Page 146, Page 228

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---


## Preset: `uganda`

- **Document**: Uganda Clinical Guidelines 2023
- **Queries**: 25

### Summary table

| # | Triage | Guardrail OK | Confidence | VHT chars | Referral chars | Quick chars |
|---|--------|--------------|------------|-----------|----------------|-------------|
| 1 | GREEN | True | 0.90 | 1448 | 380 | 123 |
| 2 | GREEN | True | 0.90 | 1456 | 380 | 123 |
| 3 | GREEN | True | 0.90 | 1452 | 380 | 123 |
| 4 | GREEN | True | 0.90 | 1455 | 380 | 123 |
| 5 | GREEN | True | 0.90 | 1476 | 380 | 123 |
| 6 | GREEN | True | 0.90 | 1467 | 380 | 123 |
| 7 | GREEN | True | 0.90 | 1508 | 380 | 123 |
| 8 | GREEN | True | 0.90 | 1432 | 380 | 123 |
| 9 | GREEN | True | 0.90 | 1440 | 380 | 123 |
| 10 | GREEN | True | 0.90 | 1471 | 380 | 123 |
| 11 | GREEN | True | 0.90 | 1519 | 380 | 123 |
| 12 | GREEN | True | 0.90 | 1460 | 380 | 123 |
| 13 | GREEN | True | 0.90 | 1555 | 380 | 123 |
| 14 | GREEN | True | 0.90 | 1597 | 380 | 123 |
| 15 | GREEN | True | 0.90 | 1458 | 380 | 123 |
| 16 | GREEN | True | 0.90 | 1477 | 380 | 123 |
| 17 | GREEN | True | 0.90 | 1453 | 380 | 123 |
| 18 | GREEN | True | 0.90 | 1456 | 380 | 123 |
| 19 | GREEN | True | 0.90 | 1499 | 380 | 123 |
| 20 | GREEN | True | 0.90 | 1473 | 380 | 123 |
| 21 | GREEN | True | 0.90 | 1422 | 380 | 123 |
| 22 | GREEN | True | 0.90 | 1546 | 380 | 123 |
| 23 | GREEN | True | 0.90 | 1468 | 380 | 123 |
| 24 | GREEN | True | 0.90 | 1436 | 380 | 123 |
| 25 | GREEN | True | 0.90 | 1428 | 380 | 123 |

### Full queries and formatted outputs

#### Query 1

**Full query**

> Integrated management of childhood illness pneumonia classification

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 37: IPT
• Uganda Clinical Guidelines 2023, Page 932: 17.4  INTEGRATED COMMUNITY CASE MANAGEMENT
• Uganda Clinical Guidelines 2023, Page 878: Childhood Illness
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Integrated management of childhood illness pneumonia classification

### 1. IPT

### IPT

HBV

Hepatitis B Virus

HC

Health Centre

Hct/Ht

Haematocrit

HCW

Health Care Worker

HDU

High Dependency Unit

HE

Hepatic Encephalopathy

HepB

Hepatitis B

HHS

Hyperosmolar Hyperglycaemic State

Hib

Haemophilus Influenzae Type B

HIV

Human Immunodeficiency Virus

HPV

Human Papilloma Virus

HR

Heart Rate

HRP

High-Risk Pregnancy

HRS

Hepatorenal Syndrome

HSV

Herpes Simplex Virus

HVS

High Vaginal  Swab

ICCM

Integrated Community Case Management

ICU

Intensive Care  Uni...

📄 **Reference:** Page 37

### 2. 17.4  INTEGRATED COMMUNITY CASE MANAGEMENT

### 17.4  INTEGRATED COMMUNITY CASE MANAGEMENT

17.4  INTEGRATED COMMUNITY CASE MANAGEMENT

Integrated Community Case Management (iCCM) of malaria, pneumo­

nia and diarrhoea is a recently adopted strategy for the treatment of

common childhood illness at community level by trained Community

Health Workers since 2010. It addresses a gap in delivery of curative

services to children below 5 years allowing:



prompt and accessible treatment of uncomplicated malaria, pneu­

monia and diarrhoea

...

📄 **Reference:** Page 932

### 3. Childhood Illness

### Childhood Illness

Uganda Clinical Guidelines 2023

CHAPTER 17: Childhood Illness

-

Pinch the skin of the

abdomen. Does it go

back

-

Very slowly? (takes >2

seconds)

-

Slowly? (up to 2 seconds)...

📄 **Reference:** Page 878

### 4. Childhood Illness

### Childhood Illness

Uganda Clinical Guidelines 2023

CHAPTER 17: Childhood Illness

CLINICAL FEATURES

CLASSIFY AS

MANAGEMENT

~

Sunken

eyes



FOLLOW UP in 2 days:...

📄 **Reference:** Page 879

### 5. Childhood Illness

### Childhood Illness

Uganda Clinical Guidelines 2023

CHAPTER 17: Childhood Illness...

📄 **Reference:** Page 897


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 37, Page 878, Page 879, Page 897, Page 932

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 2

**Full query**

> Diarrhea dehydration ORS zinc treatment plan

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 75: Plan A (No dehydration and for prevention)
• Uganda Clinical Guidelines 2023, Page 77: Plan C (Severe dehydration)
• Uganda Clinical Guidelines 2023, Page 75: ORS
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Diarrhea dehydration ORS zinc treatment plan

### 1. Plan A (No dehydration and for prevention)

### Plan A (No dehydration and for prevention)

Plan A (No dehydration and for prevention)

TREATMENT

LOC



Counsel the mother on the 4 rules of home treatment:

extra fluids (ORS), continue feeding, zinc supplemen­

tation, when to return

HC2



Give extra fluids: as much as the child will take

- If child exclusively breastfed, give ORS or safe...

📄 **Reference:** Page 75

### 2. Plan C (Severe dehydration)

### Plan C (Severe dehydration)

Plan C (Severe dehydration)

TREATMENT

LOC...

📄 **Reference:** Page 77

### 3. ORS

### ORS

- In addition to the usual fluid intake, give ORS after

each loose stool or episode of vomiting Child <2

years: 50-100 ml

Child 2-5 years: 100-200 ml

- Give the mother 2 packets to use at home

- Giving ORS is especially important if the child

has been treated with Plan B or Plan C during

current visit

- Give frequent small sips from a cup



Advice the mother to continue or increase breastfeeding.

If child vomits, wait 10 minutes, then give more slowly

- In a child with high ...

📄 **Reference:** Page 75

### 4. Emergencies and Trauma

### Emergencies and Trauma

Uganda Clinical Guidelines 2023

CHAPTER 1: Emergencies and Trauma

TREATMENT

LOC

If mother must leave before completing the child’s treatment



Show her how to prepare ORS at home and how much

ORS to give to finish the 4-hour treatment

- Give her enough packets to complete this and 2

more to complete Plan A at home



Counsel mother on the 4 rules of home treatment: extra

fluids, continue feeding, zinc, when to return...

📄 **Reference:** Page 77

### 5. Management

### Management

Management...

📄 **Reference:** Page 75


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 75, Page 77

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 3

**Full query**

> HIV antiretroviral therapy first-line regimen adults

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 444: ment regimen
• Uganda Clinical Guidelines 2023, Page 444: Important:
• Uganda Clinical Guidelines 2023, Page 444: Susceptible TB: 1st line treatment regimens
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** HIV antiretroviral therapy first-line regimen adults

### 1. ment regimen

### ment regimen

Alternative 1st-line treat­

ment regimen

All forms of TB in children

(2 months to 16 years) with

non-severe disease

2 HRE(Z)

2RH

G e n e r a l

Hospital and

above

All forms of TB in adults

above 12 years, weight

>40 Kgs, if HIV positive

CD4>100 cells/L

2 HPMZ

2HPM

378...

📄 **Reference:** Page 444

### 2. Important:

### Important:

Important: The choice of regimen now depends on rifampicin

sensitivity and not on the previous history of treatment:



All patients without rifampicin resistance (either new or re-treat­

ments) are treated with 1st line regimen.



Patients with rifampicin resistance (either new or re- treatments)

are treated with second line medication in a designated MDR-TB

treatment facility....

📄 **Reference:** Page 444

### 3. Susceptible TB: 1st line treatment regimens

### Susceptible TB: 1st line treatment regimens

Susceptible TB: 1st line treatment regimens

For patients without rifampicin resistance to  Gene Xpert MTB/Rif (both

new and re-treatment cases).

New cases not belonging to priority (risk) groups and in which diagnosis

was done by sputum examination will also be treated with this regimen....

📄 **Reference:** Page 444

### 4. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections

orATV/r

All third line regimens

to be guided by HIV

the table to guide the

drug resistance test­

In case of suscepti­

preferred or alterna­

regimens1,2

to all drugs, use

line regimen

Third line

tive choices.

bility

ing....

📄 **Reference:** Page 289

### 5. Principles of ART

### Principles of ART

Principles of ART

~

Antiretroviral therapy is part of comprehensive HIV care.

The guiding principles of good ART include:

~

Efficacy and durability of the chosen medicine regimens

~

Freedom from serious adverse effects; low toxicity

~

Ease of administration including no food restrictions, better

palatability, and lower pill burden

~

Affordability and availability of medicines and medicine com­

binations

~

Organised sequencing – spares other available formula...

📄 **Reference:** Page 268


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 268, Page 289, Page 444

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 4

**Full query**

> Tuberculosis treatment regimen and contact investigation

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 166: Investigation
• Uganda Clinical Guidelines 2023, Page 497: Investigation
• Uganda Clinical Guidelines 2023, Page 452: 5.3.2.3	 Tuberculosis Preventive Treatment
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Tuberculosis treatment regimen and contact investigation

### 1. Investigation

### Investigation

Investigation...

📄 **Reference:** Page 166

### 2. Investigation

### Investigation

Investigation...

📄 **Reference:** Page 497

### 3. 5.3.2.3	 Tuberculosis Preventive Treatment

### 5.3.2.3	 Tuberculosis Preventive Treatment

5.3.2.3	 Tuberculosis Preventive Treatment

Tuberculosis preventive treatment is recommended to prevent the

development of active TB disease in an individual who has latent TB

infection (LTBI).

Uganda  guidelines for programmatic management of Latent TB infection

recommend TB preventive treatment (TPT ) in the following categories

of people:

- Persons living with HIV

- Child & adult contacts of pulmonary TB patients

Do not use TPT in cases ...

📄 **Reference:** Page 452

### 4. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections

ARV regimen substitution for patients initiating TB treatment while on ART

Age Group

Regimen When Di­

agnosed With Tb

Recommended Action/ Sub­

stitution

Adults, Preg­

n a n t  a n d

Breastfeeding

Women and

Adolescents

If on LPV/r based

regimen

Continue the same regimen but

double the dose of DTG (give

DTG twice daily)

If on ATV/r based

regim...

📄 **Reference:** Page 320

### 5. Contact tracing

### Contact tracing

Contact tracing

~

Tracing of contacts of TB patients

~

Routine screening of health workers for latent & active TB...

📄 **Reference:** Page 451


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 166, Page 320, Page 451, Page 452, Page 497

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 5

**Full query**

> Malaria uncomplicated case management ACT dosing children

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 235: Treatment of uncomplicated malaria
• Uganda Clinical Guidelines 2023, Page 235: Management of Malaria
• Uganda Clinical Guidelines 2023, Page 775: Management of Malaria in Pregnancy
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Malaria uncomplicated case management ACT dosing children

### 1. Treatment of uncomplicated malaria

### Treatment of uncomplicated malaria

Treatment of uncomplicated malaria

The following tables contain dosages for medicines used in treatment of

uncomplicated malaria.

169...

📄 **Reference:** Page 235

### 2. Management of Malaria

### Management of Malaria

Management of Malaria

NATIONAL MALARIA TREATMENT POLICY

Uncomplicated Malaria

All patients: including children

<4 months of age and pregnant

women

in 2nd and 3rd trimesters

First line medicine

Artemether/Lumefantrine

First line alternative

Artesunate/Amodiaquine

Second line medicine

Dihydroartemisin/ Piperaquine

If not available: quinine tablets

Pregnant women 1st trimester

ACT currently used

Severe Malaria

All age groups or patient categories First li...

📄 **Reference:** Page 235

### 3. Management of Malaria in Pregnancy

### Management of Malaria in Pregnancy

Management of Malaria in Pregnancy

APPROACH

MANAGEMENT

LOC

Prophylaxis All

pregnant mothers

Wexcept those

with HIV on

cotrimoxazole

prophylaxis



Intermittent Preventive Treatment

(IPTp) with Sulphadoxine/ pyrimeth­

amine (SP) once a month starting

at 13 weeks until delivery

HC2



Quinine oral 600 mg 8 hourly for 7

days (if Quinine not available, ACT

may be used)

Treatment of

Uncomplicated

malaria in 1st

trimester

HC2

709...

📄 **Reference:** Page 775

### 4. Infectious Diseases

### Infectious Diseases

Uganda Clinical Guidelines 2023

CHAPTER 2: Infectious Diseases...

📄 **Reference:** Page 235

### 5. 17.4  INTEGRATED COMMUNITY CASE MANAGEMENT

### 17.4  INTEGRATED COMMUNITY CASE MANAGEMENT

17.4  INTEGRATED COMMUNITY CASE MANAGEMENT

Integrated Community Case Management (iCCM) of malaria, pneumo­

nia and diarrhoea is a recently adopted strategy for the treatment of

common childhood illness at community level by trained Community

Health Workers since 2010. It addresses a gap in delivery of curative

services to children below 5 years allowing:



prompt and accessible treatment of uncomplicated malaria, pneu­

monia and diarrhoea

...

📄 **Reference:** Page 932


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 235, Page 775, Page 932

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 6

**Full query**

> Postpartum hemorrhage emergency management oxytocin

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 789: and no signs of infection
• Uganda Clinical Guidelines 2023, Page 812: 16.4.6 Postpartum Haemorrhage (PPH)
• Uganda Clinical Guidelines 2023, Page 789: Obstetric Conditions
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Postpartum hemorrhage emergency management oxytocin

### 1. and no signs of infection

### and no signs of infection

If the membranes have been ruptured for >18 hours

and no signs of infection



Give prophylactic antibiotics until delivery to help reduce

neonatal group B streptococcus infection: Ampicillin 2

g IV every 6 hours or benzylpenicillin 2 MU IV every

6 hours

HC4



Assess the cervix



Refer to HC4 or above (with facilities for emergency

obstetric management) for induction with oxytocin (see

section 16.4.2)...

📄 **Reference:** Page 789

### 2. 16.4.6 Postpartum Haemorrhage (PPH)

### 16.4.6 Postpartum Haemorrhage (PPH)

16.4.6 Postpartum Haemorrhage (PPH)    ICD10 CODE: O72

Vaginal bleeding of more than 500 mL after vaginal delivery or >1000

mL after caesarean section.

746...

📄 **Reference:** Page 812

### 3. Obstetric Conditions

### Obstetric Conditions

Uganda Clinical Guidelines 2023

CHAPTER 16: Obstetric Conditions

MANAGEMENT

LOC



Refer all patients to hospital and keep in hospital until

delivery

HC4...

📄 **Reference:** Page 789

### 4. Check for vaginal bleeding and possible uterine/urinary tract or febrile infection

### Check for vaginal bleeding and possible uterine/urinary tract or febrile infection

Check for vaginal bleeding and possible uterine/urinary tract or febrile infection

otics

months

Postpartum

Postpartum

Moderate

No Anae­

6 weeks

minutes

bleeing

delivery

soaked

1 pad

bleeding



More

than

after

in 5



Still



Hb 7-11



Hb >11

g/dL or



Palmar

juctival­

or con­

pallor

pallor

g/dL



No



Heavy vaginal

vaginal bleed­



Heavy/ light

ing after 6



Look for

...

📄 **Reference:** Page 837

### 5. Cervix not favourable

### Cervix not favourable

Cervix not favourable



Ripen cervix using either



Misoprostol 25 micrograms inserted vaginally every

6 hours for 2 doses, if no response increase to 50

micrograms every 6 hours, max 200 micrograms in

24 hours – stop when in established labour



Or misoprostol 20 micrograms orally (dissolve 1 200

microgram tablet in 200 mL of water and give 20 mL)

every 2 hours until labour starts or max 24 hours



Or Foley catheter: insert Foley catheter through internal...

📄 **Reference:** Page 807


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 789, Page 807, Page 812, Page 837

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 7

**Full query**

> Family planning contraceptive counseling methods

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 751: Family Planning (FP)
• Uganda Clinical Guidelines 2023, Page 725: 15.1.10  Summary of Medical Eligibility for Contraceptives
• Uganda Clinical Guidelines 2023, Page 730: 15.2  Overview Of Key Contraceptive Methods
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Family planning contraceptive counseling methods

### 1. Family Planning (FP)

### Family Planning (FP)

Uganda Clinical Guidelines 2023

CHAPTER 15: Family Planning (FP)

INSTRUCTIONS

LOC...

📄 **Reference:** Page 751

### 2. 15.1.10  Summary of Medical Eligibility for Contraceptives

### 15.1.10  Summary of Medical Eligibility for Contraceptives

15.1.10  Summary of Medical Eligibility for Contraceptives

The tables below contain a ummarized version of the medical eligibility

criteria for initiating a patient on contraceptive methods, based on the

MOH (2016) and WHO (2020) Medical Eligibility Criteria for Contracep­

tive Use. It guides family planning providers in recommending safe and

effective contraception methods for women with medical conditions or

medially-relevan...

📄 **Reference:** Page 725

### 3. 15.2  Overview Of Key Contraceptive Methods

### 15.2  Overview Of Key Contraceptive Methods

15.2  Overview Of Key Contraceptive Methods

The following sections contain an overview of mainstream contraceptive

methods and how to manage side effects

of each (in case they occur). Side effects are one of most common reasons

why women stop using contraception, and the health worker should

be able to counsel the patient and address her concerns appropriately....

📄 **Reference:** Page 730

### 4. Methods all couples (except a few) can safely use

### Methods all couples (except a few) can safely use

Methods all couples (except a few) can safely use

Emergency contraceptive pill (for emergency use only) Bilateral Tubal

Ligation (BTL) and Vasectomy

Barrier methods (condoms, diaphragm) Lactational amenorrhoea

method (LAM)

Fertility awareness (FAM) and Standard days methods...

📄 **Reference:** Page 730

### 5. Oral contraceptives

### Oral contraceptives

Oral contraceptives



Combined oral contraceptive (see Family Planning,

section 15.2.3)...

📄 **Reference:** Page 1062


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 725, Page 730, Page 751, Page 1062

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 8

**Full query**

> Hypertension diagnosis and management primary care

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 54: Chronic Care
• Uganda Clinical Guidelines 2023, Page 830: Postpartum care services
• Uganda Clinical Guidelines 2023, Page 296: Management
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Hypertension diagnosis and management primary care

### 1. Chronic Care

### Chronic Care

Chronic Care

~

Health workers are faced with an increasing number of

chronic diseases and conditions that require additional at­

tention, such as hypertension, chronic heart problems, dia­

betes, cancers, mental conditions, HIV/AIDS, and TB.

~

Communication is even more important to:

~

Find out the duration of the symptoms, previous diagnosis,

previous or current treatments and impact on daily life

~

Explain the nature and management of the condition to the

patient...

📄 **Reference:** Page 54

### 2. Postpartum care services

### Postpartum care services

Postpartum care services

The mother and baby should be seen at 6 hours after birth and again

before discharge if in a health facility (and anytime the mother reports

concern about herself and her baby) or approximately 6 hours after

delivery at home.

The routine follow-up visits are at 6 days and 6 weeks, and have the

following components:



Counselling



Assessment and management of observed or reported prob­

lems. Check for hypertension, anaemia, vagina...

📄 **Reference:** Page 830

### 3. Management

### Management

Management

All HIV services for pregnant mothers are offered in the MCH clinic.

After delivery, mother and baby will remain in the MCH postnatal clinic

till HIV status of the child is

confirmed, then they will be transferred to the general ART clinic.

The current policy aims at elimination of Mother-to-Child Transmission

(eMTCT) through provision of a continuum of care with the following

elements:

- Primary HIV prevention for men, women and adolescents

- Prevention of un...

📄 **Reference:** Page 296

### 4. Differential diagnosis

### Differential diagnosis

Differential diagnosis

~

Aphthous ulcer

~

Other causes of genital sores, e.g., syphilis

~

Other causes of meningoencephalitis...

📄 **Reference:** Page 1046

### 5. Management

### Management



Investigation of uveitis is broad and requires a high index of

suspicion



Diagnosis of uveitis requires expertise and can only be confirmed

by slit lamp examinations

Management

TREATMENT

LOC

If at HC2 and HC3...

📄 **Reference:** Page 995


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 54, Page 296, Page 830, Page 995, Page 1046

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 9

**Full query**

> Diabetes mellitus type 2 glycemic targets

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 778: Therapeutic targets
• Uganda Clinical Guidelines 2023, Page 537: Diabetes Mellitus
• Uganda Clinical Guidelines 2023, Page 541: Treatment targets
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Diabetes mellitus type 2 glycemic targets

### 1. Therapeutic targets

### Therapeutic targets

Therapeutic targets

~

Pre prandial blood glucose <5.3 mmol/L

~

1-hour postprandial glucose <7.8 mmol/L

~

2-hour postprandial glucose <6.4 mmol/L...

📄 **Reference:** Page 778

### 2. Diabetes Mellitus

### Diabetes Mellitus

8.1.3

Diabetes Mellitus

ICD10 CODE: E08-E13

Metabolic disease resulting from insulin insufficiency or ineffectiveness,

due to decreased insulin secretion, or peripheral resistance to the action

of insulin, or a combination of the two....

📄 **Reference:** Page 537

### 3. Treatment targets

### Treatment targets

Treatment targets

- Fasting blood sugar <7 mmol/l

- Postprandial sugar <10 mmol/l

- HbA1c <7% (7.5 % for elderly)

Elderly people are at higher risk of hypoglycaemia. Monitor carefully,

and do not aim at very strict control of blood sugar.

Management of Type 1 Diabetes

Insulin SC: 0.6 -1.5 IU/kg/day HC4 Children <5 years: start with 0.5

IU/Kg/day, and refer to a paediatrician

Type of

Usual

Action

Onset

Peak

Duration

Insulin

Protocol

Insulin short

acting, r...

📄 **Reference:** Page 541

### 4. 15.1.6  Obtain and Record Client History

### 15.1.6  Obtain and Record Client History

15.1.6  Obtain and Record Client History

The primary objectives are:

~

To obtain client’s personal and social data and information

on health status

~

To identify abnormalities/problems requiring treatment or

referral

For FP clients, it is important to pay particular attention to information

outlined in the table below:

HISTORY

INFORMATION NEEDED

Social History

~

Smoking? How many ummarized per

day?

~

Drinking? How much alcohol per da...

📄 **Reference:** Page 721

### 5. 8 ENDOCRINE AND METABOLIC DISEASES..................................468

### 8 ENDOCRINE AND METABOLIC DISEASES..................................468

8 ENDOCRINE AND METABOLIC DISEASES..................................468

8.1.1 Addison’s Disease..........................................................................................468

8.1.2 Cushing’s Syndrome.......................................................................................470

8.1.3 Diabetes Mellitus............................................................................................4...

📄 **Reference:** Page 10


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 10, Page 537, Page 541, Page 721, Page 778

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 10

**Full query**

> Acute stroke referral and supportive care

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 394: If stroke clinically haemorrhagic
• Uganda Clinical Guidelines 2023, Page 394: Chronic care of ischaemic stroke
• Uganda Clinical Guidelines 2023, Page 394: If ischaemic stroke
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Acute stroke referral and supportive care

### 1. If stroke clinically haemorrhagic

### If stroke clinically haemorrhagic

If stroke clinically haemorrhagic



Supportive care as above



Refer for CT scan and neurosurgical evaluation...

📄 **Reference:** Page 394

### 2. Chronic care of ischaemic stroke

### Chronic care of ischaemic stroke

Chronic care of ischaemic stroke



Early mobilization and physiotherapy f Aspirin 75-100

mg once daily for life f Atorvastatin 40 mg daily for life



Control of risk factors

328...

📄 **Reference:** Page 394

### 3. If ischaemic stroke

### If ischaemic stroke

If ischaemic stroke

H



Aspirin 150-300 mg every 24 hours



In the acute phase, treat hypertension only if extreme

(more than 220/120) or if there are other complications

(pulmonary oedema, angina, etc), otherwise re-start

antihypertensive 24 hours after the event and reduce

blood pressure slowly



Consider DVT prophylaxis with enoxaparin 40 mg

SC daily...

📄 **Reference:** Page 394

### 4. Cardiovascular Diseases

### Cardiovascular Diseases

Uganda Clinical Guidelines 2023

CHAPTER 4: Cardiovascular Diseases...

📄 **Reference:** Page 394

### 5. Management of stable angina

### Management of stable angina

Management of stable angina

TREATMENT

LOC...

📄 **Reference:** Page 394


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 394

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 11

**Full query**

> Syndromic management sexually transmitted infections

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 343: HIV/AIDS and Sexually Transmitted Infections
• Uganda Clinical Guidelines 2023, Page 317: HIV/AIDS and Sexually Transmitted Infections
• Uganda Clinical Guidelines 2023, Page 349: HIV/AIDS and Sexually Transmitted Infections
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Syndromic management sexually transmitted infections

### 1. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections...

📄 **Reference:** Page 343

### 2. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections...

📄 **Reference:** Page 317

### 3. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections

TREATMENT

LOC...

📄 **Reference:** Page 349

### 4. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections

Candida vaginitis and bacterial vaginosis are NOT sexually transmitted

diseases, even though sexual activity is a risk factor.

~

Gonorrhoea causes cervicitis and rarely vaginitis. Thereis a

purulent thin mucoid slightly yellow pus discharge with no

smell and non-itchy

~

Chlamydia causes cervicitis which may present with a non-

itchy, thin, colourless...

📄 **Reference:** Page 346

### 5. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections

TREATMENT

LOC...

📄 **Reference:** Page 356


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 317, Page 343, Page 346, Page 349, Page 356

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 12

**Full query**

> Cervical cancer screening VIA HPV

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 677: Screening for Cervical Cancer
• Uganda Clinical Guidelines 2023, Page 675: Prevention of Infections
• Uganda Clinical Guidelines 2023, Page 674: Oncogenic Infections
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Cervical cancer screening VIA HPV

### 1. Screening for Cervical Cancer

### Screening for Cervical Cancer

Screening for Cervical Cancer

This aims to detect pre-cancerous lesions that are then treated to prevent

progression to invasive cancer. The following methods are recommended:

Visual Inspection with Acetic Acid (VIA): involves applying 3-5% freshly

prepared acetic acid to the cervix and observing results after one minute.

 The VIA results are generally categorized into 3 subsets:

suspicious for cancer, VIA negative and VIA positive

 It uses readily ava...

📄 **Reference:** Page 677

### 2. Prevention of Infections

### Prevention of Infections

Prevention of Infections

The following infections are associated with causing certain types of

cancer:

~

Viral Hepatitis B/C: cancer of the liver

~

Human Papilloma Virus (HPV): cervical cancer

~

Helicobacter Pylori: stomach cancer

HIV/AIDS: aggressive lymphoma subtypes, Kaposi’s sarcoma, anorectal

cancer, cervical cancer, etc

~

Schistosomiasis: increases risk of bladder cancer

~

Liver Fluke: increases risk of cholangio-carcinoma

~

Preventative measur...

📄 **Reference:** Page 675

### 3. Oncogenic Infections

### Oncogenic Infections

Oncogenic Infections

The following infections are associated with causing certain types of

cancer:

 Viral Hepatitis B/C: cancer of the liver

 Human Papilloma Virus (HPV): cervical, oral, anal, and cancer

 Helicobacter Pylori: Gastric (stomach) cancer

 HIV/AIDS: aggressive lymphoma subtypes, Kaposi’s sarcoma,

anorectal cancer, cervical cancer, etc.

 Schistosomiasis: increases risk of bladder cancer

 Liver Fluke: increases risk of cholangio-carcinoma

 Pre...

📄 **Reference:** Page 674

### 4. owing if using VIA as a screening method:

### owing if using VIA as a screening method:

Consider the following if using VIA as a screening method:

 Women <25 years of age should be screened only if they are

at high risk for disease: HIV positive, early sexual exposure,

multiple partners, previous abnormal screening results, cervical

intraepithelial neoplasia (CIN)

 VIA is not appropriate for women >50 years

 Screening is advised every 3-5 years in case of normal results,

but after 1 years in case of abnormal results and treat...

📄 **Reference:** Page 677

### 5. Oncology

### Oncology

Uganda Clinical Guidelines 2023

CHAPTER 12: Oncology

ing, early diagnosis, pre-cancer treatment or cancer management, and

referral to avoid or reduce complications associated with the cancer.

Secondary prevention strategies relate to the discovery and control of

cancerous or pre-cancerous lesions.

Early detection of cancer greatly increases the chances for successful

treatment and cure. It comprises of:

~

Early diagnosis in symptomatic populations

~

Screening in asymptom...

📄 **Reference:** Page 676


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 674, Page 675, Page 676, Page 677

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 13

**Full query**

> Routine immunization schedule infants Uganda

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 16: 18.1  Routine Childhood Vaccination...............................................875
• Uganda Clinical Guidelines 2023, Page 305: HIV/AIDS and Sexually Transmitted Infections
• Uganda Clinical Guidelines 2023, Page 305: 3.1.9.2 HIV-exposed infant care services
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Routine immunization schedule infants Uganda

### 1. 18.1  Routine Childhood Vaccination...............................................875

### 18.1  Routine Childhood Vaccination...............................................875

18 IMMUNIZATION......................................................................875

18.1  Routine Childhood Vaccination...............................................875

18.1.1   National Immunization Schedule.................................................................875

18.1.2  Hepatitis B Vaccination...............................................................................881

18.1.3  ...

📄 **Reference:** Page 16

### 2. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections

Service

Description

• 8 ANC visits

• Two weeks after

initiating ART

• Synchronize ART

refills and adherence

support with the ANC

visits

• After that, monthly

until delivery

• Follow routine

MCH schedule after

delivery together

with the exposed

infant visit schedule...

📄 **Reference:** Page 305

### 3. 3.1.9.2 HIV-exposed infant care services

### 3.1.9.2 HIV-exposed infant care services

3.1.9.2 HIV-exposed infant care services

Service

Description

Identification of

HIV-exposed in­

fants

• Identify all HIV-exposed infants; document the

HIV status of the mother in the child card and

mothers’ passport. Infants whose HIV status

is not documented or is unknown should be

offered rapid HIV testing; including those whose

mothers did not receive eMTCT services or have

become newly infected after pregnancy. Rapid

diagnostic tests ...

📄 **Reference:** Page 305

### 4. Check immunization card and classify

### Check immunization card and classify

Check immunization card and classify

~

Imuniza­

tion not

up to date

according

~

to national

schedule

(see chap­

ter 18)

~

Give all missed

doses on this

visit (Include sick

infants unless

being referred)

Infant Not

Immunized

as per

Schedule

~

Immuniza­

tion upto

date as per

national

schedule

~

Advise caretaker

when to return

for the next

dose

Infant Im­

munized as

Per Sched­

ule...

📄 **Reference:** Page 889

### 5. Prevention

### Prevention

Prevention

~

Educate parents on the importance of following the routine

childhood immunisation schedule:

~

Ensure good nutrition

~

Avoid overcrowding

~

Booster doses of vaccine in exposed infants...

📄 **Reference:** Page 423


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 16, Page 305, Page 423, Page 889

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 14

**Full query**

> Severe acute malnutrition inpatient management

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 17: 19.2  Malnutrition.........................................................................890
• Uganda Clinical Guidelines 2023, Page 959: 19.2.1.2  Assessing Malnutrition in Children 6 months to 5 years
• Uganda Clinical Guidelines 2023, Page 963: 19.2.2   Management of Acute Malnutrition in Children
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Severe acute malnutrition inpatient management

### 1. 19.2  Malnutrition.........................................................................890

### 19.2  Malnutrition.........................................................................890

19.2  Malnutrition.........................................................................890

19.2.1  Introduction on Malnutrition........................................................................890

19.2.1.1 Classification of Malnutrition......................................................................892

19.2.1.2 Assessing Malnutrition in Children 6 months to 5 years.................

📄 **Reference:** Page 17

### 2. 19.2.1.2  Assessing Malnutrition in Children 6 months to 5 years

### 19.2.1.2  Assessing Malnutrition in Children 6 months to 5 years

19.2.1.2  Assessing Malnutrition in Children 6 months to 5 years

The 4 key features used to diagnose acute malnutrition are:



Weight-for-Height/Length (WFH/L) using WHO growth standards

charts (see section 15.5). It is the best indicator for diagnosing

acute malnutrition.



Mean Upper Arm Circumference (MUAC) in mm using a measuring

tape (see section 17.5)



Oedema of both feet (kwashiorkor with or without severe wa...

📄 **Reference:** Page 959

### 3. 19.2.2   Management of Acute Malnutrition in Children

### 19.2.2   Management of Acute Malnutrition in Children

19.2.2   Management of Acute Malnutrition in Children...

📄 **Reference:** Page 963

### 4. Weight for-Height/Length

### Weight for-Height/Length

Weight for-Height/Length

r

Used to diagnose acute malnutrition

r

The cut-off for severe acute malnutrition is -3 z-scores and be­

low. These children are at a high risk of mortality, but respond

quickly and safely to re-feeding using therapeutic foods following

recommended guidelines.

r

The cut-off for moderate acute malnutrition is -2 to -3 z-scores

below.

868...

📄 **Reference:** Page 934

### 5. 19.2.2.1   Management of Moderate Acute Malnutrition

### 19.2.2.1   Management of Moderate Acute Malnutrition

19.2.2.1   Management of Moderate Acute Malnutrition

TREATMENT

LOC



Assess the child’s feeding and counsel the mother on

the feeding recommendations



If child has any feeding problem, counsel and follow up

in 7 days (see section 17.3.12.4)...

📄 **Reference:** Page 963


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 17, Page 934, Page 959, Page 963

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 15

**Full query**

> Tuberculosis preventive therapy isoniazid

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 37: IPT
• Uganda Clinical Guidelines 2023, Page 316: TB preventive therapy (TPT)
• Uganda Clinical Guidelines 2023, Page 452: 5.3.2.3	 Tuberculosis Preventive Treatment
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Tuberculosis preventive therapy isoniazid

### 1. IPT

### IPT

HBV

Hepatitis B Virus

HC

Health Centre

Hct/Ht

Haematocrit

HCW

Health Care Worker

HDU

High Dependency Unit

HE

Hepatic Encephalopathy

HepB

Hepatitis B

HHS

Hyperosmolar Hyperglycaemic State

Hib

Haemophilus Influenzae Type B

HIV

Human Immunodeficiency Virus

HPV

Human Papilloma Virus

HR

Heart Rate

HRP

High-Risk Pregnancy

HRS

Hepatorenal Syndrome

HSV

Herpes Simplex Virus

HVS

High Vaginal  Swab

ICCM

Integrated Community Case Management

ICU

Intensive Care  Uni...

📄 **Reference:** Page 37

### 2. TB preventive therapy (TPT)

### TB preventive therapy (TPT)

TB preventive therapy (TPT)



Give INH for six months to HIV-exposed infant who

are exposed to TB (close contact with PTB case) after

excluding TB disease (see section 5.3.2.3)



Dose: Isoniazid 10 mg/kg + pyridoxine 25 mg daily



For newborn infants, if the mother has TB disease and

has been on anti-TB drugs for at least two weeks before

delivery, INH prophylaxis is not required.

250...

📄 **Reference:** Page 316

### 3. 5.3.2.3	 Tuberculosis Preventive Treatment

### 5.3.2.3	 Tuberculosis Preventive Treatment

5.3.2.3	 Tuberculosis Preventive Treatment

Tuberculosis preventive treatment is recommended to prevent the

development of active TB disease in an individual who has latent TB

infection (LTBI).

Uganda  guidelines for programmatic management of Latent TB infection

recommend TB preventive treatment (TPT ) in the following categories

of people:

- Persons living with HIV

- Child & adult contacts of pulmonary TB patients

Do not use TPT in cases ...

📄 **Reference:** Page 452

### 4. 5.3.2.5	 TB Preventive Treatment Dosing Chart

### 5.3.2.5	 TB Preventive Treatment Dosing Chart

5.3.2.5	 TB Preventive Treatment Dosing Chart

Medicine frequency

& duration

Formulation

Dose of TPT

medicine

(mgs)

Dose/

weight

Recom

3HP (once weekly

rifapentine plus isoni­

azid for 3 months)

Fixed Doze

Combination

(FDC) Tablet

Rifapentine

300mg/ Iso­

niazid 300mg

3–5.9

Single medicine

Pyridoxine

25mg/day

tablet

6H (daily isoniazid

for 6 months)

3–5.9

kgs

Isoniazid 100

mg

<10 years

0.5

Single medicine

10mg/kg

...

📄 **Reference:** Page 454

### 5. TPT (TB Preventive treatment)

### TPT (TB Preventive treatment)

TPT (TB Preventive treatment)

HC3



such as;   isoniazid + rifapentine(3HP)  weekly for 3

months in all adults, adolescents and children >12

months living with HIV and in whom TB disease has

been excluded (other medications for TPT refer to the

current HIV/TB guidelines)



If child <12 months, give only if history of contact with

TB case and no active disease (one-month daily rifap­

entine and isoniazid (1HP).)

– Dose:  (see section 5.3.2.1 )...

📄 **Reference:** Page 264


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 37, Page 264, Page 316, Page 452, Page 454

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 16

**Full query**

> Depression screening and management primary care

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 719: ceive
• Uganda Clinical Guidelines 2023, Page 676: Screening for Breast Cancer
• Uganda Clinical Guidelines 2023, Page 214: COVID-19 screening and triage process at health facilities
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Depression screening and management primary care

### 1. ceive

### ceive

ceive

Pre-conception care discussion topics for clients who desire to conceive

include:

~

Pregnancy planning and appropriate contraception

~

Folic acid supplementation 3 months preceeding concep­

tion

~

Good diet, risk assessment and management of pre exist­

ing conditions and risk factors

~

Benefits of preconception care (e.g., prevention of unin­

tended pregnancies, good maternal and foetal outcomes)

~

Screening for hereditary diseases e.g., sickle cell disease

~

Sc...

📄 **Reference:** Page 719

### 2. Screening for Breast Cancer

### Screening for Breast Cancer

Screening for Breast Cancer

Screening / health checkup for breast cancer involves:

Breast Self-Examination (BSE): a simple, quick examination done by the

client herself, aimed at early detection of lumps. Regular (monthly-not

during menstruation, at least seven days after ending the menstruation)

and correct technique of breast examination is important and easy to

teach and administer. Health workers should note that BSE is not a

standard screening test fo...

📄 **Reference:** Page 676

### 3. COVID-19 screening and triage process at health facilities

### COVID-19 screening and triage process at health facilities

COVID-19 screening and triage process at health facilities

~

COVID-19 triage aims to flag suspected patients at first

point of contact within the healthcare system in order to

~

protect other patients and staff from potential exposure.

~

identify and rapidly address severe symptoms, rule out oth­

er conditions with features similar to COVID-19, ascertain

if suspect case definition is met

~

All suspected patients should be...

📄 **Reference:** Page 214

### 4. Investigations

### Investigations

Investigations



Non-treponemal antibody tests (VDRL and RPR)

- Positive 4-6 weeks after infection

- Used as screening test

- Possibility of false positive

- Remains positive 6-12 months after treatment



Treponemal antibody tests (TPHA): very sensitive, used to confirm

a positive non-treponemal test. Remains positive for long even

after treatment so its positivity may not indicate active disease....

📄 **Reference:** Page 357

### 5. 16.1  ANTENATAL CARE (ANC)

### 16.1  ANTENATAL CARE (ANC)

16.1  ANTENATAL CARE (ANC)     ICD10 CODE: Z36

Antenatal care is a planned programme of medical care offered to

pregnant women by a skilled birth attendant, from the time of con­

ception to delivery, aimed at ensuring a safe and satisfying pregnancy

and birth outcome.

The main objective of antenatal care is to give information on:

~

Screening, prevention, and treatment of complications

~

Emergency preparedness

~

Birth planning

~

Satisfying any unmet n...

📄 **Reference:** Page 759


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 214, Page 357, Page 676, Page 719, Page 759

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 17

**Full query**

> Asthma chronic management inhaler technique

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 403: Chronic Asthma
• Uganda Clinical Guidelines 2023, Page 403: General principles of management
• Uganda Clinical Guidelines 2023, Page 402: Respiratory Diseases
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Asthma chronic management inhaler technique

### 1. Chronic Asthma

### Chronic Asthma

5.1.1.2	 Chronic Asthma...

📄 **Reference:** Page 403

### 2. General principles of management

### General principles of management

General principles of management

~

Follow a stepped approach



Before initiating a new drug, check that diagnosis is correct, compli­

ance and inhaler technique are correct and eliminate trigger factors

for acute exacerbations

~

Start at the step most appropriate to initial severity

~

Rescue course



Give a 3-5 days “rescue course” of prednisolone at any step and

at any time as required to control acute exacerbations of asthma

at a dose of:

Ch...

📄 **Reference:** Page 403

### 3. Respiratory Diseases

### Respiratory Diseases

Uganda Clinical Guidelines 2023

CHAPTER 5: Respiratory Diseases

PRIMARY CARE - Patient presents with

acute or sub-acute asthma exacerbation

ASSESS the PATIENT - Is it asthma? Risk factor

for asthma related death? Severity of exacerbation

MILD OR MODER­

ATE Talks in phrases,

prefers sitting not

lying, not agitated.

Respiratory rate

increased Accessory

muscles not used

SEVERE Talks in words,

sits hunched forwards,

agitated Respiratory

rate >30/min Accessor...

📄 **Reference:** Page 402

### 4. STEP 1: Intermittent asthma

### STEP 1: Intermittent asthma

STEP 1: Intermittent asthma

~

Intermittent symptoms (< once/week)

HC3

~

Night time symptoms < twice/month

~

Normal physical activity...

📄 **Reference:** Page 403

### 5. Caution

### Caution

Caution

 Do not give medicines such as morphine, propranolol, or

other B-blockers to patients with asthma as they worsen

respiratory problems

 Do not give sedatives to children with asthma, even if they

are restless

339...

📄 **Reference:** Page 405


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 402, Page 403, Page 405

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 18

**Full query**

> Chronic kidney disease staging referral

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 516: Chronic Kidney Disease (CKD)
• Uganda Clinical Guidelines 2023, Page 253: 3.1.1 Clinical Features of HIV
• Uganda Clinical Guidelines 2023, Page 382: Risk Factor
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Chronic kidney disease staging referral

### 1. Chronic Kidney Disease (CKD)

### Chronic Kidney Disease (CKD)

7.1.2

Chronic Kidney Disease (CKD)      ICD10 CODE: N18

Chronic impairment of kidney function...

📄 **Reference:** Page 516

### 2. 3.1.1 Clinical Features of HIV

### 3.1.1 Clinical Features of HIV

3.1.1 Clinical Features of HIV

The WHO Clinical Staging of HIV for adults and children in the tables

below shows the typical clinical features of HIV infection. The staging is

based on demonstration of one or more opportunistic infections or key

findings and correlates with disease progression and prognosis. Clinical

staging should be performed at HIV diagnosis, on entry into HIV care,

at ART initiation and at every visit hereafter to help guide patient ...

📄 **Reference:** Page 253

### 3. Risk Factor

### Risk Factor

Risk Factor

Heart failure

Post myocardial infarction

Angina

Diabetes

Mild/moderate kidney disease

Advanced chronic kidney disease

Stroke

Carvedilol or Bisoprolol  only...

📄 **Reference:** Page 382

### 4. Surgery, Radiology and Anaesthesia

### Surgery, Radiology and Anaesthesia

Uganda Clinical Guidelines 2023

CHAPTER 24 : Surgery, Radiology and Anaesthesia

~

Hepatomegaly or cirrhosis (fibrotic

~

Gut perforation: Free air below the

~

Kidney diseases (cancer, chronic

hemidiaphgram on the CXR indi­

~

Liver/spleen rupture/ haematoma

pyelonephritis, hydronephrosis)

Ultrasound

~

Fluids (blood) in peritoneum

~

Renal trauma/haematoma

cate pneumoperitoneum

disease

Ultrasound

~

Gallstones, cholecystitis

~

Liver masse...

📄 **Reference:** Page 1120

### 5. 7.1 Renal Diseases........................................................................448

### 7.1 Renal Diseases........................................................................448

7.1 Renal Diseases........................................................................448

7.1.1 Acute Renal Failure........................................................................................448

7.1.2 Chronic Kidney Disease (CKD)........................................................................450

7.1.3 Use of Drugs in Renal Failure.............................................

📄 **Reference:** Page 10


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 10, Page 253, Page 382, Page 516, Page 1120

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 19

**Full query**

> Exclusive breastfeeding six months

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 317: Counselling on infant feeding choice
• Uganda Clinical Guidelines 2023, Page 317: If mother chooses breastfeeding
• Uganda Clinical Guidelines 2023, Page 953: 19.1.1  Infant and Young Child Feeding (IYCF)
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Exclusive breastfeeding six months

### 1. Counselling on infant feeding choice

### Counselling on infant feeding choice

Counselling on infant feeding choice

- Explain the risks of HIV transmission by breastfeeding (15%)

and other risks of not breastfeeding (malnutrition, diarrhoea)

- Mixed feeding may also increase risk of HIV transmission

- and diarrhoea

- Tell her about options for feeding, advantages, and risks

- Help her to assess choices, decide on the best option, and

then support her choice

- Feeding options

- Recommended

option:

Exclusive

breastfeeding...

📄 **Reference:** Page 317

### 2. If mother chooses breastfeeding

### If mother chooses breastfeeding

If mother chooses breastfeeding

- The risk may be reduced by keeping the breasts healthy

(mastitis and cracked nipples raise HIV infection risk)

- Advise exclusive breastfeeding for 3-6 months

251...

📄 **Reference:** Page 317

### 3. 19.1.1  Infant and Young Child Feeding (IYCF)

### 19.1.1  Infant and Young Child Feeding (IYCF)

19.1.1  Infant and Young Child Feeding (IYCF)

1.	 Counsel and support all mothers to initiate breastfeeding within an

hour of delivery and exclusively breastfeed their infants for the first

six months of life, unless medically contraindicated.

2.	 Teach mother correct positioning and attachment for breastfeeding,

how to express and store breast milk hygienically, and how to feed

the child by a cup.

3.	 Counsel and support parents to intro...

📄 **Reference:** Page 953

### 4. If breastfeeding difficult:

### If breastfeeding difficult:

Support exclusive breast­

feeding

on demand, day and night,

whenever baby wants

If breastfeeding difficult:

Help mother to position and

attach the baby

If breastfeeding not possible:

Advise on safe replacement feed­

ing (AFASS)

759...

📄 **Reference:** Page 825

### 5. HC2

### HC2

HC2

Routine deworming

every six months...

📄 **Reference:** Page 920


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 317, Page 825, Page 920, Page 953

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 20

**Full query**

> Pre-eclampsia severe features magnesium sulfate

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 795: Clinical features of severe pre-eclampsia
• Uganda Clinical Guidelines 2023, Page 795: 16.3.7      Pre-Eclampsia
• Uganda Clinical Guidelines 2023, Page 835: Obstetric Conditions
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Pre-eclampsia severe features magnesium sulfate

### 1. Clinical features of severe pre-eclampsia

### Clinical features of severe pre-eclampsia

Clinical features of severe pre-eclampsia



Headache, blurring of vision of new onset



Epigastric or right upper quadrant pain, vomiting

729...

📄 **Reference:** Page 795

### 2. 16.3.7      Pre-Eclampsia

### 16.3.7      Pre-Eclampsia

16.3.7      Pre-Eclampsia	                     ICD10 CODE: O14

Pre-eclampsia is a hypertensive condition of pregnancy usually diag­

nosed after 20 weeks of gestation and can present as late as 4-6 weeks

postpartum.

It is haracterized with hypertension, proteinuria with or without oedema

and, may result into maternal fits if not managed appropriately.

It may also be superimposed on chronic hypertension. It is classified as

mild to severe pre-eclampsia.

TYPE ...

📄 **Reference:** Page 795

### 3. Obstetric Conditions

### Obstetric Conditions

Uganda Clinical Guidelines 2023

CHAPTER 16: Obstetric Conditions

as in non-pregnant women (see)



If no pre-eclampsia, give/contin­

ue appropriate antihypertensive

Severe Hypertension



Assess and treat for pre-eclamp­

sive as in non-pregnant women

tinue appropriate antihyperten­



If not pre-eclampsia, give/con­

sia (section 16.3.7). Refer to

tension



Assess for pre-eclampsia

Normal



No additional treatment



Review in one week

(section 4.1.6)

...

📄 **Reference:** Page 835

### 4. Mild to moderate pre-eclampsia

### Mild to moderate pre-eclampsia

Mild to moderate pre-eclampsia



Based on BP response



Methyldopa, oral, 250 mg every 8 hours as a starting

dose, increase to 500 mg 6 hourly according to response,

Max dose 2 g daily

AND/OR

HC3



Nifedipine 20-40 mg every 12 hours

Severe pre-eclampsia (hypertensive emergency)

To prevent convulsions

HC3



Give IV fluids (Normal saline) very slowly (1 L in 6-8

hours max)



Give IV loading dose of magnesium sulphate injection

(4 g of MgSO4)

...

📄 **Reference:** Page 797

### 5. Blood pressure

### Blood pressure

Blood pressure



History of

eclampsia

or pre-ec­

an hour

lampsia

769...

📄 **Reference:** Page 835


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 795, Page 797, Page 835

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 21

**Full query**

> Sepsis empirical antibiotics adults

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 792: Newborn
• Uganda Clinical Guidelines 2023, Page 701: Medicines
• Uganda Clinical Guidelines 2023, Page 785: Post-abortal Sepsis
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Sepsis empirical antibiotics adults

### 1. Newborn

### Newborn

Newborn

H



Examine the neonate for suspected sepsis before

discharge



If newborn sepsis is suspected manage as in section

2.1.7.1



Advise the mother on how to recognize danger signs

(see section 17.1.1)...

📄 **Reference:** Page 792

### 2. Medicines

### Medicines

Medicines



Give antibiotics if there is evidence of surrounding cellulitis (see

section 22.1.3)



Control pain



Control odour with topical metronidazole



powder or gel until there is no foul smell



If patient has sepsis, give parenteral antibiotics (see section 2.1.7

for treatment of sepsis)...

📄 **Reference:** Page 701

### 3. Post-abortal Sepsis

### Post-abortal Sepsis

Post-abortal Sepsis

Patient has signs and symptoms

of sepsis following an abortion,

but there are no products of

conception in the uterus



Give IV antibiotics cef­

triaxone 2 g + metroni­

dazole 500



mg IV 8 hourly for

48 hours, until fever

has disappeared, then

switch to oral treatment

as for septic abortion

HC4



Refer to hospital for

evacuation...

📄 **Reference:** Page 785

### 4. 16.3.6       Antepartum Haemorrhage (APH) – Abruptio Placentae

### 16.3.6       Antepartum Haemorrhage (APH) – Abruptio Placentae

16.3.6       Antepartum Haemorrhage (APH) – Abruptio Placentae...

📄 **Reference:** Page 792

### 5. If the woman has a Caesarean section

### If the woman has a Caesarean section

If the woman has a Caesarean section



Continue the above antibiotics, and add metronidazole

500 mg IV every 8 hours

-

Continue until 48 hours after fever has gone...

📄 **Reference:** Page 792


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 701, Page 785, Page 792

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 22

**Full query**

> Rabies post-exposure prophylaxis dog bite

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 102: 1.2.1.4  Rabies Post Exposure Prophylaxis
• Uganda Clinical Guidelines 2023, Page 4: 1.2 Trauma and Injuries..................................................................26
• Uganda Clinical Guidelines 2023, Page 205: Caution: the patient may bite
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Rabies post-exposure prophylaxis dog bite

### 1. 1.2.1.4  Rabies Post Exposure Prophylaxis

### 1.2.1.4  Rabies Post Exposure Prophylaxis

1.2.1.4  Rabies Post Exposure Prophylaxis           ICD10 CODE:

Z20.3, Z23...

📄 **Reference:** Page 102

### 2. 1.2 Trauma and Injuries..................................................................26

### 1.2 Trauma and Injuries..................................................................26

1.2 Trauma and Injuries..................................................................26

1.2.1 Bites and Stings..............................................................................................26

1.2.1.1  Snakebites.........................................................................................28

1.2.1.2 Insect Bites & Stings....................................................

📄 **Reference:** Page 4

### 3. Caution: the patient may bite

### Caution: the patient may bite

Caution: the patient may bite



Counsel caregivers on rabies and consequences

139...

📄 **Reference:** Page 205

### 4. 2.3.5 Rabies

### 2.3.5 Rabies

2.3.5 Rabies

ICD10 CODE: A82

Rabies is a viral infection of wild and domestic animals, transmitted to

humans by saliva of infected animals through bites, scratches or licks

on broken skin or mucuos membranes. Once symptoms develop, rabies

presents as a fatal encephalitis: there is no cure and treatment is palliative.

Before symptomatic disease has developed, rabies can effectively be

prevented by post-exposure prophylaxis....

📄 **Reference:** Page 204

### 5. Unit, Community Health Dept, Ministry of Health, September 2001

### Unit, Community Health Dept, Ministry of Health, September 2001

Post exposure prophylaxis effectively prevents the development of rabies

after the contact with saliva of infected animals, through bites, scratches,

licks on broken skin or mucous membranes. For further details refer to

Rabies Post-Exposure Treatment Guidelines, Veterinary Public Health

Unit, Community Health Dept, Ministry of Health, September 2001...

📄 **Reference:** Page 102


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 4, Page 102, Page 204, Page 205

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 23

**Full query**

> Burns initial wound care and referral

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 112: 2nd Degree burns or Partial thickness burns
• Uganda Clinical Guidelines 2023, Page 112: Emergencies and Trauma
• Uganda Clinical Guidelines 2023, Page 112: 4th Degree burns
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Burns initial wound care and referral

### 1. 2nd Degree burns or Partial thickness burns

### 2nd Degree burns or Partial thickness burns

2nd Degree burns or Partial thickness burns

It is a dermal injury that is sub-classified as

superficial and deep 2nd degree burns. In su­

perficial 2nd degree burns, blisters result, the

pink moist wound is painful. A thin eschar is

formed. Heals in 10-14 days.

In deep 2nd degree burns, blisters are lacking,

the wound is pale, moderately painful, a thick

escar is formed. Heals in

>1 month, requiring surgical debridement...

📄 **Reference:** Page 112

### 2. Emergencies and Trauma

### Emergencies and Trauma

Uganda Clinical Guidelines 2023

CHAPTER 1: Emergencies and Trauma

CRITERIA

LEVEL...

📄 **Reference:** Page 112

### 3. 4th Degree burns

### 4th Degree burns

3rd Degree burns

Full thickness skin destruction, leather- like

rigid eschar. Painless on palpation or pinprick.

Requires skin graft.

4th Degree burns

Full thickness skin and fascia, muscles, or bone

destruction. Lifeless body part

Percentage of total

body surface area

(TBSA)

Small areas are estimated using the open palm

of the patient to represent 1% TBSA. Large

areas estimated using the “rules of nines” or

a Lund-Browder chart. Count all areas except

the one...

📄 **Reference:** Page 112

### 4. Severe burns

### Severe burns

Severe burns



First aid and wound management as above PLUS



Give IV fluid replacement in a total volume per 24 hours

according to the calculation in the box below (use crystal­

loids, i.e., Ringer’s lactate, or normal saline)



If patient in shock, run the IV fluids fast until BP improves

(see section 1.1.2)

HC4



Manage pain as necessary



Refer for admission



Monitor vital signs and urine output



Use antibiotics if there are systemic signs of infection:
...

📄 **Reference:** Page 116

### 5. At health facility

### At health facility

At health facility

HC2



Give oral or IV analgesics as required



If TBSA <10% and patient able to drink, give oral fluids

otherwise consider IV



Give TT if not fully immunised



Leave small blisters alone, drain large blisters and dress

if closed dressing method is being used the urine output.

The normal urine output is: Children (<30 kg) 1-2 ml/kg/

hour and adults 0.5 ml/kg/hour (30-50 ml /hour)



Dress with silver sulphadiazine cream 1%, add saline

moi...

📄 **Reference:** Page 115


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 112, Page 115, Page 116

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 24

**Full query**

> Snake bite envenomation hospital referral

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 96: without envenomation
• Uganda Clinical Guidelines 2023, Page 96: Management
• Uganda Clinical Guidelines 2023, Page 96: Emergencies and Trauma
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Snake bite envenomation hospital referral

### 1. without envenomation

### without envenomation

If no signs and symptoms for 6-8 hours: most likely bite

without envenomation

~

Observation for 12-24 hours recommended

~

Tetanus toxoid (TT) IM 0.5 ml if not previously

immunised in the last 10 years...

📄 **Reference:** Page 96

### 2. Management

### Management

Management

What to do

What not to do

 Do not panic

 Reassure the patient to

 Do not lay the patient on

stay calm

 Lay the patient on the

their back as it may block

airways

 Do not apply a tourniquet

side to avoid movement

of affected areas

 Remove all tight items

 Do not squeeze or incise the

wound

 Do not attempt to suck the

around the affected area

 Leave the wound/bite

venom out

 Do not try to kill or attack

area alone

 Immobilize the patient

...

📄 **Reference:** Page 96

### 3. Emergencies and Trauma

### Emergencies and Trauma

Uganda Clinical Guidelines 2023

CHAPTER 1: Emergencies and Trauma...

📄 **Reference:** Page 96

### 4. If local necrosis develops

### If local necrosis develops

If local necrosis develops

~

Remove blisters, clean and dress daily, debride

after lesions stabilise (minimum 15 days)

30...

📄 **Reference:** Page 96

### 5. If signs of fang penetration

### If signs of fang penetration

If signs of fang penetration

~

Immobilise limb with a splint

~

Analgesic e.g. paracetamol (avoid NSAIDS like

aspirin, diclofenac, ibuprofen)...

📄 **Reference:** Page 96


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 96

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 25

**Full query**

> Neonatal sepsis danger signs referral

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.90`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess patient carefully
**Step 2:** Check for danger signs (see below)
**Step 3:** If unsure, refer to health facility
**Step 4:** Record all findings

**MONITORING:**

• Check if patient can drink normally
• Watch for convulsions or shaking
• Monitor breathing – is it fast or difficult?
• Check if patient is awake and alert
• Look for pale or yellow skin/eyes

**DANGER SIGNS - STOP AND REFER IF YOU SEE:**

• Cannot drink or breastfeed
• Very weak, cannot sit up or wake up
• Shaking/fitting (convulsions)
• Vomiting everything
• Difficulty breathing
• Pale or yellow skin/eyes
• Bleeding from any place

**WHAT TO TELL THE FAMILY:**

The symptoms can be managed at home with guidance. Follow the advice you were given. Come back if symptoms get worse.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 792: Newborn
• Uganda Clinical Guidelines 2023, Page 153: Causes
• Uganda Clinical Guidelines 2023, Page 183: 2.1.7.1 Neonatal Septicaemia
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess patient carefully
• Check for danger signs (see below)
• If unsure, refer to health facility

**Referral completed:** [ ]
**Health worker received:** [ ]

---
_This is a VHT referral. Please assess patient promptly._
```

#### Quick summary (`quick_summary`)

```
MANAGE AT HOME
Reason: Routine evidence retrieval from national guidelines
Action: Follow advice below, monitor for changes
```

#### BM25 + guardrail evidence bundle (`response` — markdown)

```
**Uganda Clinical Guidelines 2023**

**Question:** Neonatal sepsis danger signs referral

### 1. Newborn

### Newborn

Newborn

H



Examine the neonate for suspected sepsis before

discharge



If newborn sepsis is suspected manage as in section

2.1.7.1



Advise the mother on how to recognize danger signs

(see section 17.1.1)...

📄 **Reference:** Page 792

### 2. Causes

### Causes

Causes

~

Surgical causes.

- Head Injury, Chest trauma

~

Medical Causes

- Severe Asthma, Pneumonia, Sepsis, Shock, Malaria,

Covid-19, Heart Failure, Cardiac arrest, Upper airway

obstruction, Severe anaemia, Pertussis, Carbon Monoxide

poisoning.

~

Obstetric, gynaecological, and perioperative causes.

- Obstructed labour, Ruptured uterus, Pre-eclampsia and

eclampsia, Post caesarean section,

~

Neonatal causes

- Transient tachypnoea of the new-born, Hypoxic Ischaemic

encep...

📄 **Reference:** Page 153

### 3. 2.1.7.1 Neonatal Septicaemia

### 2.1.7.1 Neonatal Septicaemia

2.1.7.1 Neonatal Septicaemia

Organisms causing neonatal septicemia are similar to the ones causing

neonatal pneumonia and meningitis. Refer to hospital after pre-referral

dose of antibiotics....

📄 **Reference:** Page 183

### 4. If danger signs present, treat as below

### If danger signs present, treat as below

If danger signs present, treat as below

pustules and apply Gentian



If referral not possible continue

every 12 hours plus gentamicin

gentamicin 5-7 mg/Kg every



Give ampicillin 50 mg/kg IM



Clean infected umbilicus and

Kg IV/IM every 6 hours and

5 mg/kg every 24 hours (4

tion, give cloxacillin 50 mg/



If risk of staphylococcus infec­



Refer baby to hospital

treatment for 7 days

mg/kg if preterm)



Keep baby warm

24 hours

Vio...

📄 **Reference:** Page 863

### 5. 17.3.21   Check for General Danger Signs

### 17.3.21   Check for General Danger Signs

17.3.21   Check for General Danger Signs...

📄 **Reference:** Page 892


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 153, Page 183, Page 792, Page 863, Page 892

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---


## Summary

- **All guardrails passed**: True
