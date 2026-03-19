# WHO Malaria pipeline run report

- **Generated (UTC)**: 2026-03-19T23:10:31.482476+00:00
- **Preset**: who-malaria (NIH Bookshelf)
- **PDF**: `C:\temp\capstone\Bookshelf_NBK588130.pdf`
- **KB output directory**: `C:\temp\capstone\medical_kb_who_malaria`
- **Reuse KB flag**: `True`

---
## Stage 1: Multi-pass extraction

_Loaded from existing `knowledge_base.json` (pass-level log not in memory)._

| Metric | Value |
|--------|-------|
| Pages (summary) | 478 |
| Tables (summary) | 0 |
| Extraction passes (summary) | 3 |

## Stage 2: Validation

### Overall

- **Passed (threshold)**: False
- **Confidence**: -8.00%
- **Needs human review**: True

### Structure

```json
{
  "stage": "structure",
  "passed": false,
  "issues": [
    "Heading level skipped: 1 \u2192 3"
  ],
  "confidence": 0.7,
  "suggestions": [
    "Verify heading hierarchy manually"
  ],
  "metadata": {
    "pages_extracted": 478
  }
}
```

### Tables

```json
{
  "stage": "tables",
  "passed": false,
  "issues": [
    "Document estimated 1 tables but none extracted"
  ],
  "confidence": 0.3,
  "suggestions": [
    "Review tables with low confidence"
  ],
  "metadata": {
    "tables_extracted": 0,
    "valid_tables": 0
  }
}
```

### Cross

```json
{
  "stage": "cross_consistency",
  "passed": true,
  "issues": [],
  "confidence": 1.0,
  "suggestions": [],
  "metadata": {
    "consistency_score": 1.0
  }
}
```

### Medical

```json
{
  "stage": "medical_content",
  "passed": true,
  "issues": [],
  "confidence": 1.0,
  "suggestions": [],
  "metadata": {
    "terms_found": [
      "dose",
      "mg",
      "contraindication",
      "warning",
      "severe malaria",
      "artemisinin",
      "pregnancy",
      "children",
      "infant",
      "emergency"
    ],
    "terms_missing": []
  }
}
```

### Human Review

```json
{
  "stage": "human_review",
  "passed": false,
  "issues": [
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy",
    "Safety-critical information - verify accuracy"
  ],
  "confidence": -3.4000000000000004,
  "suggestions": [
    "Prioritize flagged items for manual review"
  ],
  "metadata": {
    "items_for_review": [
      {
        "type": "contraindication",
        "page": 7,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 8,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 9,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 10,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 14,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 17,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 20,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 24,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 25,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 54,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 61,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 65,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 72,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 83,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 85,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 94,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 104,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 110,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 115,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 119,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 120,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 125,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 131,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 139,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 143,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 147,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 151,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 155,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 156,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 167,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 168,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 172,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 185,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 188,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 191,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 192,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 203,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 209,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
        "type": "contraindication",
        "page": 214,
        "reason": "Safety-critical information - verify accuracy"
      },
      {
 
... (truncated)
```

## Stage 3: Chunking + BM25 index

| Metric | Value |
|--------|-------|
| Total chunks | 954 |
| Chunks with tables | 0 |

### Sample chunk headings (first 15)

- p.2 — **WHO guidelines for malaria - 13 August 2025**
- p.2 — **2025**
- p.2 — **isclaimers.**
- p.3 — **Sections**
- p.4 — **Untitled**
- p.5 — **Pyrethroid-only nets (2019)**
- p.5 — **Pyrethroid-PBO ITNs (2022)**
- p.6 — **Untitled**
- p.6 — **Pyrethroid-chlorfenapyr ITNs vs pyrethroid-PBO ITNs (2023)**
- p.6 — **Pyrethroid-pyriproxyfen ITNs vs pyrethroid-only LLINs (2023)**
- p.7 — **Insecticide-treated nets: Humanitarian emergency setting (2022)**
- p.7 — **Achieving and maintaining optimal coverage with ITNs for malaria prevention and **
- p.7 — **Management of old ITNs (2019)**
- p.8 — **Indoor residual spraying: Humanitarian emergency setting (2022)**
- p.8 — **Prioritize optimal coverage with either ITNs or IRS over combination (2019)**

## Stage 4: Guardrail brain

`MedicalGuardrailBrain` validates each composed answer: triage headings, dangerous patterns, citations vs. chunk pages.

## Stage 5: Search & Q&A (25 queries)

BM25 top-5 excerpts per query; guardrail summary below each.

### 1. Query

> What is the treatment for uncomplicated Plasmodium falciparum malaria?

**Sources (top hits)**
- Page 170: Artesunate-pyronaridine for uncomplicated malaria (2022)
- Page 17: Artesunate-pyronaridine for uncomplicated malaria (2022)
- Page 190: knowlesi
- Page 185: Justification
- Page 190: Justification

**Response**

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** What is the treatment for uncomplicated Plasmodium falciparum malaria?

### 1. Artesunate-pyronaridine for uncomplicated malaria (2022)

### Artesunate-pyronaridine for uncomplicated malaria (2022)

Artesunate-pyronaridine for uncomplicated malaria (2022)

Artesunate-pyronaridine (ASPY) is recommended as an artemisinin-based combination therapy option for the treatment of

uncomplicated P. falciparum malaria.

•

ASPY should be avoided by individuals with known liver disease (clinically apparent liver disease) because ASPY is

associated with liver transaminitis.

•

Pharmacovigilance should be strengthened where ASPY is used for...

📄 **Reference:** Page 170

### 2. Artesunate-pyronaridine for uncomplicated malaria (2022)

### Artesunate-pyronaridine for uncomplicated malaria (2022)

Artesunate-pyronaridine for uncomplicated malaria (2022)

Artesunate-pyronaridine (ASPY) is recommended as an artemisinin-based combination therapy option for the

treatment of uncomplicated P. falciparum malaria.

Remark:

•

ASPY should be avoided by individuals with known liver disease (clinically apparent liver disease) because ASPY is

associated with liver transaminitis.

•

Pharmacovigilance should be strengthened where ASPY is...

📄 **Reference:** Page 17

### 3. knowlesi

### knowlesi

5.2.1.5 Uncomplicated malaria caused by P. vivax, P. ovale, P. malariae or P.

knowlesi

Plasmodium vivax accounts for approximately half of all malaria cases outside Africa [3][250][251]. It is prevalent in the Middle

East, Asia, the Western Pacific and Central and South America. With the exception of the Horn, it is rarer in Africa, where there

is a high prevalence of the Duffy-negative phenotype, particularly in West Africa, although cases are reported in both

Mauritania and ...

📄 **Reference:** Page 190

### 4. Justification

### Justification

Justification

The GDG reached a consensus on a strong recommendation for artemether-lumefantrine as the preferred treatment of

uncomplicated Plasmodium falciparum malaria during the first trimester of pregnancy, despite the low certainty of evidence

because:

•

there was a large magnitude of beneficial effect of treatment on efficacy (demonstrated in the second and third

trimesters of pregnancy), specifically a six-fold reduction in treatment failures following artemether...

📄 **Reference:** Page 185

### 5. Justification

### Justification

Justification

In falciparum malaria, the risk for progression to severe malaria with vital organ dysfunction increases at higher parasite

densities. In low-transmission settings, mortality begins to increase when the parasite density exceeds 100 000/µL (~2%

parasitaemia). On the north-west border of Thailand, before the general introduction of ACT, parasitaemia > 4% without

signs of severity was associated with a 3% mortality rate (about 30-times higher than from uncomplic...

📄 **Reference:** Page 190


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 17, Page 170, Page 185, Page 190

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 2. Query

> Dosing artemisinin-based combination therapy in children under 5

**Sources (top hits)**
- Page 226: Considerations in use of artemisinin-based combination therapy
- Page 168: Artemisinin-based combination therapy (2015)
- Page 3: Sections
- Page 170: Untitled
- Page 203: Tafenoquine as anti-relapse therapy (2024)

**Response**

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

### 2. Artemisinin-based combination therapy (2015)

### Artemisinin-based combination therapy (2015)

Artemisinin-based combination therapy (2015)

Children and adults with uncomplicated P. falciparum malaria should be treated with one of the following ACTs*:

•

artemether-lumefantrine (AL)

•

artesunate-amodiaquine (AS+AQ)

•

artesunate-mefloquine (ASMQ)

•

dihydroartemisinin-piperaquine (DHAP)

•

artesunate + sulfadoxine-pyrimethamine (AS+SP)

•

artesunate-pyronaridine (ASPY) (2022)

*Artesunate + sulfadoxine-pyrimethamine and artesunate-...

📄 **Reference:** Page 168

### 3. Sections

## Sections

Sections

Summary of recommendations ........................................................................................................................................................................ 5

1. Abbreviations.............................................................................................................................................................................................. 27

2. Executive summary .................................................

📄 **Reference:** Page 3

### 4. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

The Guideline Development Group decided to recommend a “menu” of approved combinations from which countries can select

first- and second- line therapies. Modelling studies suggest that having multiple first-line ACTs available for use may help to

prevent or delay the development of resistance.

Recommendation: Dihydroartemisinin + piperaquine is recommended for general use.

A systematic review showed that the dosin...

📄 **Reference:** Page 170

### 5. Tafenoquine as anti-relapse therapy (2024)

### Tafenoquine as anti-relapse therapy (2024)

Tafenoquine as anti-relapse therapy (2024)

Tafenoquine is recommended as an alternative to primaquine (3.5 mg/kg total dose) for preventing relapses of P. vivax in

patients ≥ 2years of age, who have ≥ 70% G6PD activity and who receive chloroquine treatment.

•

These recommendations pertain only to South America.

•

Quantitative or semi-quantitative determination of G6PD activity must be done before tafenoquine administration.

•

Tafenoquine is...

📄 **Reference:** Page 203


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 3, Page 168, Page 170, Page 203, Page 226

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 3. Query

> Severe malaria definition and management

**Sources (top hits)**
- Page 403: Publication bias: no serious.
- Page 210: 5.2.2 Treating severe malaria
- Page 402: 167
- Page 214: malaria
- Page 404: Publication bias: no serious.

**Response**

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

### 2. 5.2.2 Treating severe malaria

### 5.2.2 Treating severe malaria

5.2.2 Treating severe malaria

Mortality from untreated severe malaria (particularly cerebral malaria) approaches 100%. With prompt, effective antimalarial

treatment and supportive care, the rate falls to 10–20% overall. Within the broad definition of severe malaria some syndromes are

associated with lower mortality rates (e.g. severe anaemia) and others with higher mortality rates (e.g. acidosis). The risk for death

increases in the presence of multiple com...

📄 **Reference:** Page 210

### 3. 167

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

### 4. malaria

### malaria

Treatment of severe P. vivax malaria

Although P. vivax malaria is considered to be benign, with a low case-fatality rate, it may cause a debilitating febrile illness with

progressive anaemia and can also occasionally cause severe disease, as in P. falciparum malaria. Reported manifestations of

severe P. vivax malaria include severe anaemia, thrombocytopenia, acute pulmonary oedema and, less commonly, cerebral

malaria, pancytopenia, jaundice, splenic rupture, haemoglobinuria, acu...

📄 **Reference:** Page 214

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

Citations: Page 210, Page 214, Page 402, Page 403, Page 404

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 4. Query

> When to refer a patient with malaria to hospital?

**Sources (top hits)**
- Page 220: Follow-on treatment
- Page 128: Research needs
- Page 211: Therapeutic objectives
- Page 163: 4. Appropriate weight-based dosing
- Page 177: 5.2.1.2 Recurrent falciparum malaria

**Response**

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

### 3. Therapeutic objectives

### Therapeutic objectives

Therapeutic objectives

The main objective of the treatment of severe malaria is to prevent the patient from dying. Secondary objectives are prevention of

disabilities and prevention of recrudescent infection.

Death from severe malaria often occurs within hours of admission to a hospital or clinic, so it is essential that therapeutic

concentrations of a highly effective antimalarial drug be achieved as soon as possible. Management of severe malaria comprises

mainl...

📄 **Reference:** Page 211

### 4. 4. Appropriate weight-based dosing

### 4. Appropriate weight-based dosing

4. Appropriate weight-based dosing

To prolong their useful therapeutic life and ensure that all patients have an equal chance of being cured, the quality of antimalarial drugs

must be ensured, and antimalarial drugs must be given at optimal dosages. Treatment should maximize the likelihood of rapid clinical and

parasitological cure and minimize transmission from the treated infection. To achieve this, dosage regimens should be based on the

patient’s we...

📄 **Reference:** Page 163

### 5. 5.2.1.2 Recurrent falciparum malaria

### 5.2.1.2 Recurrent falciparum malaria

5.2.1.2 Recurrent falciparum malaria

Recurrence of P. falciparum malaria can result from re-infection or recrudescence (treatment failure). Treatment failure may

result from drug resistance or inadequate exposure to the drug due to sub-optimal dosing, poor adherence, vomiting, unusual

pharmacokinetics in an individual, or substandard medicines. It is important to determine from the patient’s history whether he

or she vomited the previous treatment or...

📄 **Reference:** Page 177


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 128, Page 163, Page 177, Page 211, Page 220

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 5. Query

> Pregnancy and malaria treatment recommendations

**Sources (top hits)**
- Page 108: Implementation
- Page 185: Feasibility
- Page 184: Untitled
- Page 30: Scope
- Page 302: Untitled

**Response**

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Pregnancy and malaria treatment recommendations

### 1. Implementation

### Implementation

Implementation

Please refer to the WHO policy brief for the implementation of intermittent preventive treatment of malaria in pregnancy using

sulfadoxine-pyrimethamine (IPTp-SP) [128] and the WHO recommendations on antenatal care for a positive pregnancy

experience [130]. A field guide on community deployment of intermittent preventive treatment of malaria in pregnancy with

sulfadoxine-pyrimethamine was released in January 2024 [129]. A manual for subnational tailoring of...

📄 **Reference:** Page 108

### 2. Feasibility

### Feasibility

Feasibility

One consideration in determining the feasibility of the recommendation on treatment of malaria in

the first trimester is that the existing warning against the use of artemisinin in the first trimester

implies the need to consistently screen for pregnancy among all women of childbearing potential

prior to treatment for malaria. However, pregnancy screening is rarely done prior to initiating

malaria treatment. As observed by national programmes, the contraindicati...

📄 **Reference:** Page 185

### 3. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

based therapies, and in how different cultures would value the outcomes being monitored, such

as perceptions around early trimester pregnancy losses, low birthweight and anaemia. However,

artemether-lumefantrine compared to quinine is likely to be a more attractive option because of its

greater availability and the convenience of a shorter, better tolerated treatment. Policy-makers and

implementers will obviously ...

📄 **Reference:** Page 184

### 4. Scope

### Scope

Scope

The consolidated WHO Guidelines for malaria bring together all recommendations for malaria, including prevention using vector control,

preventive chemotherapy and the vaccine; diagnosis, treatment and elimination strategies. The Guidelines also provide links to other

resources including unpublished evidence reviewed at the time of formulating recommendations, guidance and information on strategic

use of information to drive impact, surveillance, monitoring and evaluation, op...

📄 **Reference:** Page 30

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

temperature, and relative humidity: an experimental study in rural Gambia. The Lancet Planetary Health 2018;2(11):e498-e508 Pubmed

Journal Website

114. Norms, standards and processes underpinning development of WHO recommendations on vector control. Geneva: World Health

Organization 2020. Website

115. Sicuri E, Bardají A, Nhampossa T, Maixenchs M, Nhacolo A, Nhalungo D, et al. Cost-effectiveness of intermittent pr...

📄 **Reference:** Page 302


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 30, Page 108, Page 184, Page 185, Page 302

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 6. Query

> Drug interactions with artemether lumefantrine

**Sources (top hits)**
- Page 184: Untitled
- Page 185: Acceptability
- Page 186: Untitled
- Page 185: Justification
- Page 181: Dosing in pregnancy

**Response**

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

### 3. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

outcomes in the first trimester of pregnancy;

•

artemether-lumefantrine had much better tolerability compared to quinine-based therapies; and

•

there is probably increased equity, acceptability and feasibility, resulting from better access to artemether-lumefantrine

and more efficient implementation of ACTs compared to quinine-based treatments.

Despite limited exposures to other ACTs (artesunate-amodiaquine, art...

📄 **Reference:** Page 186

### 4. Justification

### Justification

Justification

The GDG reached a consensus on a strong recommendation for artemether-lumefantrine as the preferred treatment of

uncomplicated Plasmodium falciparum malaria during the first trimester of pregnancy, despite the low certainty of evidence

because:

•

there was a large magnitude of beneficial effect of treatment on efficacy (demonstrated in the second and third

trimesters of pregnancy), specifically a six-fold reduction in treatment failures following artemether...

📄 **Reference:** Page 185

### 5. Dosing in pregnancy

### Dosing in pregnancy

Dosing in pregnancy

Data on the pharmacokinetics of antimalarial agents used during pregnancy are limited. Those available indicate that

pharmacokinetic properties are often altered during pregnancy but that the alterations are insufficient to warrant dose

modifications at this time. With quinine, no significant differences in exposure have been seen during pregnancy. Studies

of the pharmacokinetics of SP used in IPTp in many sites show significantly decreased exposu...

📄 **Reference:** Page 181


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 181, Page 184, Page 185, Page 186

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 7. Query

> Prophylaxis for travelers to endemic areas

**Sources (top hits)**
- Page 103: Untitled
- Page 102: Protection for travellers to malaria-endemic areas
- Page 120: Untitled
- Page 189: 5.2.1.4.4 Non-immune travellers
- Page 146: Practical info

**Response**

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Prophylaxis for travelers to endemic areas

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

In summary, travellers should start chemoprophylaxis before entering an endemic area, to assess tolerability and, for slowly eliminated

drugs, to build up therapeutic concentrations. Malaria may be prevented by taking drugs that inhibit liver-stage (pre-erythrocytic)

development (causal prophylaxis) or drugs that kill asexual blood stages (suppressive prophylaxis). Causal prophylactics (atovaquone

+ proguanil) can ...

📄 **Reference:** Page 103

### 2. Protection for travellers to malaria-endemic areas

### Protection for travellers to malaria-endemic areas

Protection for travellers to malaria-endemic areas

The primary target for these guidelines is people living in endemic areas and no formal recommendations regarding preventive

chemotherapy are currently included for non-immune people travelling to malaria endemic regions.

People growing up in endemic countries will increasingly be non-immune as malaria control improves. However, epidemiological

changes will be heterogeneous and future g...

📄 **Reference:** Page 102

### 3. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

IPTsc can be safely given with other medicines and whether there are any additional contraindications as a result. Additionally,

there is a need to consider how to include girls of reproductive age who should not be given certain antimalarials for prophylaxis

without first confirming that they are not pregnant (see "Age group' above for further information).

IPTsc is not recommended in children with severe acute il...

📄 **Reference:** Page 120

### 4. 5.2.1.4.4 Non-immune travellers

### 5.2.1.4.4 Non-immune travellers

5.2.1.4.4 Non-immune travellers

Travellers who acquire malaria are often non-immune people living in cities in endemic countries with little or no

transmission or are visitors from non-endemic countries travelling to areas with malaria transmission. Both are at higher

risk for severe malaria. In a malaria-endemic country, they should be treated according to national policy, provided the

treatment recommended has a recent proven cure rate > 90%. Travellers...

📄 **Reference:** Page 189

### 5. Practical info

### Practical info

Practical info

MDA without an 8-aminoquinoline medicine may have a short-term (1–3 months) impact on P. vivax transmission. For MDA to

contribute meaningfully towards achievement of malaria elimination, activities must already be in place to capitalize on the

reduction in transmission achieved through the strategy. For that reason, MDA should be implemented as a component of a

robust malaria elimination programme that includes, at minimum, good coverage of case-based surv...

📄 **Reference:** Page 146


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 102, Page 103, Page 120, Page 146, Page 189

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 8. Query

> Rapid diagnostic test interpretation false positives

**Sources (top hits)**
- Page 447: Target conditions
- Page 446: Target condition
- Page 267: Untitled
- Page 201: preferences
- Page 307: Untitled

**Response**

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Rapid diagnostic test interpretation false positives

### 1. Target conditions

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

### 2. Target condition

### Target condition

•

Patients with confirmed P. vivax or P. ovale malaria undergoing G6PD testing to inform treatment with primaquine to

prevent relapses.

•

Index test is qualitative near-patient tests for G6PD.

•

Reference standard is quality assured spectrophotometric assay for G6PD. The reference standard value for the studies

included in the systematic review was based on the adjusted male median (AMM) G6PD activity (100% G6PD activity)

calculated for each G6PD spectrophotometric ...

📄 **Reference:** Page 446

### 3. Untitled

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

### 4. preferences

### preferences

Values and

preferences

The contextual factors review included 10 studies on values, mainly for quantitative tests. These

studies found that there is a variation between health care workers in how they value the outcomes of

interest (true and false positive and negative test results plus the subsequent consequences thereof).

Still, governments ask for evidence regarding the value of G6PD testing as a way to prevent

haemolysis cases while still being able to treat patients f...

📄 **Reference:** Page 201

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

Citations: Page 201, Page 267, Page 307, Page 446, Page 447

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 9. Query

> G6PD deficiency and primaquine

**Sources (top hits)**
- Page 208: Primaquine and glucose-6-phosphate dehydrogenase deficiency
- Page 195: Practical info
- Page 208: Benefits and harms
- Page 199: Untitled
- Page 195: Qualitative near-patient G6PD tests (2024)

**Response**

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

### 3. Benefits and harms

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

### 4. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

In order to prevent relapses of P. vivax and P. ovale, and when the G6PD status of the patient was previously unknown, the

following recommendations are made:

A. If only a qualitative near-patient test for G6PD deficiency is available, tafenoquine single dose treatment or high

dose primaquine (1mg/kg/day for 7 days) should not be given. If by the qualitative test the patient is classified as non-

deficient primaqu...

📄 **Reference:** Page 199

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

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 10. Query

> Malaria vaccine recommendations RTS,S R21

**Sources (top hits)**
- Page 159: Certainty of the evidence related to the safety of R21/Matrix-M
- Page 162: immunization systems.
- Page 386: Systematic review summary
- Page 160: The resources required are likely to be comparable to other new vaccine introductions.
- Page 158: Untitled

**Response**

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

### 2. immunization systems.

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

### 3. Systematic review summary

### Systematic review summary

Systematic review summary

Six studies form the basis of these recommendations: five were individual randomized controlled trials (RCTs) and one was an open-

label extension study of an included RCT. One RCT was a multicentre study evaluating three or four doses of the RTS,S/AS01 malaria

vaccine compared to no malaria vaccination. One RCT evaluated the seasonal administration of RTS,S/AS01 malaria vaccine alone

compared to SMC alone, and also compared a combinat...

📄 **Reference:** Page 386

### 4. The resources required are likely to be comparable to other new vaccine introductions.

### The resources required are likely to be comparable to other new vaccine introductions.

Resources

The resources required are likely to be comparable to other new vaccine introductions.

Mathematical models examined the addition of the vaccine to existing malaria control interventions and

treatment (Full evidence report on the RTS,S/AS01 malaria vaccine, unpublished evidence) [184].

At an assumed RTS,S/AS01 vaccine price of US$ 5 per dose and PfPR2-10 of 10–50%, two different malaria

mode...

📄 **Reference:** Page 160

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

◦

Among children who received a combination of RTS,S/AS01 seasonal vaccination and SMC, there

was a substantially greater reduction in clinical malaria (72%; 95% CI: 64–78), compared to SMC

alone, during 12 months of follow-up after the third dose. Results were similar after three years of

follow-up, with significant reductions in clinical malaria (63%; 95% CI: 58–67), hospital admissions

with severe malaria (71%...

📄 **Reference:** Page 158


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 158, Page 159, Page 160, Page 162, Page 386

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 11. Query

> Resistance to artemisinin in Southeast Asia

**Sources (top hits)**
- Page 222: Artemisinin-resistant falciparum malaria
- Page 226: Untitled
- Page 226: Considerations in use of artemisinin-based combination therapy
- Page 192: P. vivax
- Page 191: P. vivax

**Response**

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Resistance to artemisinin in Southeast Asia

### 1. Artemisinin-resistant falciparum malaria

### Artemisinin-resistant falciparum malaria

Artemisinin-resistant falciparum malaria

Artemisinin resistance in P. falciparum is now prevalent in parts of Cambodia, the Lao People’s Democratic Republic,

Myanmar, Thailand and Viet Nam. There is currently no evidence for artemisinin resistance outside these areas. The particular

advantage of artemisinins over other antimalarial drugs is that they kill circulating ring-stage parasites and thus accelerate

therapeutic responses. This is lost in ...

📄 **Reference:** Page 222

### 2. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

for days or weeks after effective treatment. HRP2-detecting RDTs are not suitable for detecting treatment failure. RDTs are slightly less

sensitive for detecting P. malariae and P. ovale. The WHO Malaria RDT Product Testing programme provides comparative data on the

performance of RDT products to guide procurement. Since 2008, 210 products have been evaluated in five rounds of product

testing [207].

For the diagno...

📄 **Reference:** Page 226

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

10-mg/kg bw dose was followed by 5 mg/kg bw at 6 h, 24 h and 4...

📄 **Reference:** Page 192

### 5. P. vivax

### P. vivax

In areas with chloroquine-sensitive P. vivax

For chloroquine-sensitive vivax malaria, oral chloroquine at a total dose of 25 mg base/kg bw is effective and well tolerated.

Lower total doses are not recommended, as these encourage the emergence of resistance. Chloroquine is given at an initial

dose of 10 mg base/kg bw, followed by 10 mg/kg bw on the second day and 5 mg/kg bw on the third day. In the past, the initial

10 mg/kg bw dose was followed by 5 mg/kg bw at 6 h, 24 h and 4...

📄 **Reference:** Page 191


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 191, Page 192, Page 222, Page 226

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 12. Query

> Hypoglycemia in severe malaria

**Sources (top hits)**
- Page 211: Treatment of severe malaria
- Page 214: malaria
- Page 214: Treatment of severe malaria during pregnancy
- Page 157: Benefits and harms
- Page 215: GRADE

**Response**

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Hypoglycemia in severe malaria

### 1. Treatment of severe malaria

### Treatment of severe malaria

Treatment of severe malaria

It is essential that full doses of effective parenteral (or rectal) antimalarial treatment be given promptly in the initial treatment of

severe malaria. This should be followed by a full dose of effective ACT orally. Two classes of medicine are available for parenteral

treatment of severe malaria: artemisinin derivatives (artesunate or artemether) and the cinchona alkaloids (quinine and quinidine).

Parenteral artesunate is the trea...

📄 **Reference:** Page 211

### 2. malaria

### malaria

Treatment of severe P. vivax malaria

Although P. vivax malaria is considered to be benign, with a low case-fatality rate, it may cause a debilitating febrile illness with

progressive anaemia and can also occasionally cause severe disease, as in P. falciparum malaria. Reported manifestations of

severe P. vivax malaria include severe anaemia, thrombocytopenia, acute pulmonary oedema and, less commonly, cerebral

malaria, pancytopenia, jaundice, splenic rupture, haemoglobinuria, acu...

📄 **Reference:** Page 214

### 3. Treatment of severe malaria during pregnancy

### Treatment of severe malaria during pregnancy

Treatment of severe malaria during pregnancy

Women in the second and third trimesters of pregnancy are more likely to have severe malaria than other adults, and, in low-

transmission settings, this is often complicated by pulmonary oedema and hypoglycaemia. Maternal mortality is approximately

50%, which is higher than in non-pregnant adults. Fetal death and premature labour are common.

Parenteral antimalarial drugs should be given to pregnant...

📄 **Reference:** Page 214

### 4. Benefits and harms

### Benefits and harms

Benefits and harms

Malaria vaccines, provided in a four-dose schedule, have been demonstrated in clinical trials to significantly

reduce clinical malaria, providing substantial added protection to that already given by existing malaria

preventive measures (i.e. ITNs and/or seasonal malaria chemoprevention (SMC)). In addition, pilot

implementation showed that the introduction of the vaccine through routine childhood immunization

programmes in Ghana, Kenya and Malawi r...

📄 **Reference:** Page 157

### 5. GRADE

### GRADE

GRADE

In a systematic review of artesunate for severe malaria [281], eight randomized controlled trials with a total of 1664 adults and

5765 children, directly compared parenteral artesunate with parenteral quinine. The trials were conducted in various African

and Asian countries between 1989 and 2010.

In comparison with quinine, parenteral artesunate:

•

reduced mortality from severe malaria by about 40% in adults (RR, 0.61; 95% CI, 0.50–0.75, five trials, 1664 participants,

hi...

📄 **Reference:** Page 215


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 157, Page 211, Page 214, Page 215

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 13. Query

> Fluid management in severe malaria adults

**Sources (top hits)**
- Page 213: Additional aspects of management
- Page 218: Benefits and harms
- Page 211: Clinical assessment
- Page 215: GRADE
- Page 404: Publication bias: no serious.

**Response**

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

### 2. Benefits and harms

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

### 3. Clinical assessment

### Clinical assessment

Clinical assessment

Severe malaria is a medical emergency. An open airway should be secured in unconscious patients and breathing and circulation

assessed. The patient should be weighed or body weight estimated, so that medicines, including antimalarial drugs and fluids, can

be given appropriately. An intravenous cannula should be inserted, and blood glucose (rapid test), haematocrit or haemoglobin,

parasitaemia and, in adults, renal function should be measured immed...

📄 **Reference:** Page 211

### 4. GRADE

### GRADE

GRADE

In a systematic review of artesunate for severe malaria [281], eight randomized controlled trials with a total of 1664 adults and

5765 children, directly compared parenteral artesunate with parenteral quinine. The trials were conducted in various African

and Asian countries between 1989 and 2010.

In comparison with quinine, parenteral artesunate:

•

reduced mortality from severe malaria by about 40% in adults (RR, 0.61; 95% CI, 0.50–0.75, five trials, 1664 participants,

hi...

📄 **Reference:** Page 215

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

Citations: Page 211, Page 213, Page 215, Page 218, Page 404

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 14. Query

> Exchange transfusion malaria criteria

**Sources (top hits)**
- Page 213: Additional aspects of management
- Page 128: Untitled
- Page 120: mortality
- Page 235: Research needs
- Page 114: Seasonal malaria chemoprevention (2022)

**Response**

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

### 3. mortality

### mortality

None of the studies that met the inclusion criteria for the review systematically collected data on school

attendance, severe malaria, hospital admissions (all-cause and malaria-specific), or mortality (all-

cause and malaria-specific)2.

More information on the evidence can be found in the systematic review [145].

1 Adjusted for age, sex and transmission intensity.

2 School achievement was not ranked by the GDG as a critical outcome and therefore was not considered. However, ...

📄 **Reference:** Page 120

### 4. Research needs

### Research needs

Research needs

•

Further evidence is needed on the impact (prevalence and incidence of malaria infection at the community level ) and

potential harms/unintended consequences of TDA for malaria in very low to low transmission or post-elimination settings.

•

Evidence is needed on the acceptability, feasibility, impact (prevalence and incidence of malaria infection at the community

level) and potential harms/unintended consequences (death, hospital admission, severe anaemi...

📄 **Reference:** Page 235

### 5. Seasonal malaria chemoprevention (2022)

### Seasonal malaria chemoprevention (2022)

Seasonal malaria chemoprevention (2022)

In areas of seasonal malaria transmission, children belonging to age groups at high risk of severe malaria should be given

antimalarial medicines during peak malaria transmission seasons to reduce disease burden.

•

Eligibility for seasonal malaria chemoprevention (SMC) is defined by the seasonality of malaria transmission and age groups

at risk of severe malaria. Thresholds for assessing these criteria chan...

📄 **Reference:** Page 114


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 114, Page 120, Page 128, Page 213, Page 235

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 15. Query

> Cerebral malaria supportive care

**Sources (top hits)**
- Page 210: 5.2.2 Treating severe malaria
- Page 220: Continuing supportive care
- Page 211: Therapeutic objectives
- Page 411: Publication bias: no serious.
- Page 167: Management of seizures

**Response**

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

as possible and should include monitoring of vital signs, coma score and urine

output. Blood glucose should be monitored every 4 h, if possible, particularly in unconscious patients.

Please refer to The use of rectal artesunate as a pre-referral treatment for severe Plas...

📄 **Reference:** Page 220

### 3. Therapeutic objectives

### Therapeutic objectives

Therapeutic objectives

The main objective of the treatment of severe malaria is to prevent the patient from dying. Secondary objectives are prevention of

disabilities and prevention of recrudescent infection.

Death from severe malaria often occurs within hours of admission to a hospital or clinic, so it is essential that therapeutic

concentrations of a highly effective antimalarial drug be achieved as soon as possible. Management of severe malaria comprises

mainl...

📄 **Reference:** Page 211

### 4. Publication bias: no serious.

### Publication bias: no serious.

142. Inconsistency: no serious. Indirectness: no serious. Imprecision: serious. Downgraded two levels for imprecision: zero

events in the control group. Publication bias: no serious.

143. [Safety outcome] Cerebral malaria assessed with positive P. falciparum rapid diagnostic test or by microscopy, with impaired

consciousness (Glasgow coma score <11 or Blantyre coma score <3 or assessed as P or U on the AVPU scale (“Alert, Voice, Pain,

Unresponsive”). Pilot ...

📄 **Reference:** Page 411

### 5. Management of seizures

### Management of seizures

Management of seizures

Generalized seizures are more common in children with P. falciparum malaria than in those with malaria due to other species. This

suggests an overlap between the cerebral pathology resulting from falciparum malaria and febrile convulsions. As seizures may

be a prodrome of cerebral malaria, patients who have more than two seizures within a 24 h period should be treated as for severe

malaria. If the seizures continue, the airways should be mai...

📄 **Reference:** Page 167


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 167, Page 210, Page 211, Page 220, Page 411

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 16. Query

> Artesunate dose for severe malaria IV

**Sources (top hits)**
- Page 211: Treatment of severe malaria
- Page 155: Schedule
- Page 22: Untitled
- Page 220: Pre-referral treatment options (2015)
- Page 311: Untitled

**Response**

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Artesunate dose for severe malaria IV

### 1. Treatment of severe malaria

### Treatment of severe malaria

Treatment of severe malaria

It is essential that full doses of effective parenteral (or rectal) antimalarial treatment be given promptly in the initial treatment of

severe malaria. This should be followed by a full dose of effective ACT orally. Two classes of medicine are available for parenteral

treatment of severe malaria: artemisinin derivatives (artesunate or artemether) and the cinchona alkaloids (quinine and quinidine).

Parenteral artesunate is the trea...

📄 **Reference:** Page 211

### 2. Schedule

### Schedule

Schedule

Malaria vaccines should be provided in a four-dose schedule in children from 5 months of age for the reduction of malaria disease and

burden. Countries may choose to give the first vaccine dose earlier than 5 months of age on the basis of operational considerations, to

increase coverage or impact.[iv]

The minimum interval between any doses is four weeks; however, to achieve prolonged protection, the fourth dose should be given

6–18 months after the third dose. To impr...

📄 **Reference:** Page 155

### 3. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

Where complete treatment of severe malaria is not possible, but injections are available, adults and children

should be given a single intramuscular dose of artesunate, and referred to an appropriate facility for further care.

Where intramuscular artesunate is not available, intramuscular artemether or, if that is not available,

intramuscular quinine should be used.

Where intramuscular injection of artesunate is n...

📄 **Reference:** Page 22

### 4. Pre-referral treatment options (2015)

### Pre-referral treatment options (2015)

Pre-referral treatment options (2015)

Where complete treatment of severe malaria is not possible, but injections are available, adults and children should be given a

single intramuscular dose of artesunate, and referred to an appropriate facility for further care. Where intramuscular artesunate

is not available, intramuscular artemether or, if that is not available, intramuscular quinine should be used.

Where intramuscular injection of artesunate is...

📄 **Reference:** Page 220

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

272. Verma R, Commons RJ, Gupta A, Rahi M, Nitika, Bharti PK, et al. Safety and efficacy of primaquine in patients with Plasmodium

vivax malaria from South Asia: a systematic review and individual patient data meta-analysis. BMJ global health 2023;8(12) Pubmed

Journal

273. Mehdipour P, Rajasekhar M, Dini S, Zaloumis S, Abreha T, Adam I, et al. Effect of adherence to primaquine on the risk of

Plasmodium vivax recur...

📄 **Reference:** Page 311


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 22, Page 155, Page 211, Page 220, Page 311

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 17. Query

> Rectal artesunate pre-referral children

**Sources (top hits)**
- Page 219: 5.2.2.3 Pre-referral treatment options
- Page 221: GRADE
- Page 220: Pre-referral treatment options (2015)
- Page 221: Other considerations
- Page 187: Untitled

**Response**

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

### 3. Pre-referral treatment options (2015)

### Pre-referral treatment options (2015)

Pre-referral treatment options (2015)

Where complete treatment of severe malaria is not possible, but injections are available, adults and children should be given a

single intramuscular dose of artesunate, and referred to an appropriate facility for further care. Where intramuscular artesunate

is not available, intramuscular artemether or, if that is not available, intramuscular quinine should be used.

Where intramuscular injection of artesunate is...

📄 **Reference:** Page 220

### 4. Other considerations

### Other considerations

Other considerations

The guideline development group could find no plausible explanation for the finding of increased mortality among older

children and adults in Asia who received rectal artesunate, which may be due to chance. Further trials would provide

clarification but are unlikely to be done. The group was therefore unable to recommend its use in older children and adults.

In the absence of direct evaluations of parenteral antimalarial drugs for pre- referral ...

📄 **Reference:** Page 221

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

exposure in this vulnerable population. The available evidence for artemether + lumefantrine, SP and chloroquine does not

indicate dose modification at this time, but young children should be closely monitored, as reduced drug exposure may

increase the risk for treatment failure. Limited studies of amodiaquine and mefloquine showed no significant effect of age

on plasma concentration profiles.

In community situati...

📄 **Reference:** Page 187


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 187, Page 219, Page 220, Page 221

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 18. Query

> Malaria in HIV coinfection

**Sources (top hits)**
- Page 188: 5.2.1.4.3 Patients co-infected with HIV
- Page 156: Vaccination of special populations
- Page 164: Diagnosis of malaria
- Page 230: Acceptability
- Page 3: Sections

**Response**

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

### 3. Diagnosis of malaria

### Diagnosis of malaria

Diagnosis of malaria

In patients with suspected severe malaria and in other high-risk groups, such as patients living with HIV/AIDS, absence or delay of

parasitological diagnosis should not delay an immediate start of antimalarial treatment.

At present, molecular diagnostic tools based on nucleic-acid amplification techniques (e.g. loop-mediated isothermal amplification or

polymerase chain reaction [PCR]) do not have a role in the clinical management of malaria.

Wh...

📄 **Reference:** Page 164

### 4. Acceptability

### Acceptability

Acceptability

The acceptability of MTaT was reported in three qualitative studies identified by the systematic review

(Bhamani et al unpublished evidence). One study in western Kenya found that the community engaged in

an MTaT intervention reported concerns over testing in the absence of symptoms. These concerns were

mostly related to the fear of covert HIV testing and some lack of understanding of the possibility of

asymptomatic malaria. Other issues related to acceptabi...

📄 **Reference:** Page 230

### 5. Sections

## Sections

Sections

Summary of recommendations ........................................................................................................................................................................ 5

1. Abbreviations.............................................................................................................................................................................................. 27

2. Executive summary .................................................

📄 **Reference:** Page 3


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 3, Page 156, Page 164, Page 188, Page 230

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 19. Query

> Species Plasmodium vivax relapse treatment

**Sources (top hits)**
- Page 190: knowlesi
- Page 34: Etiology
- Page 310: Untitled
- Page 311: Untitled
- Page 153: Malaria vaccine pipeline

**Response**

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

### 2. Etiology

### Etiology

Etiology

Malaria is a life-threatening disease caused by the infection of red blood cells with protozoan parasites of the genus Plasmodium that are

transmitted to people through the bites of infected female Anopheles mosquitoes. Four species of Plasmodium (P. falciparum, P. vivax, P.

malariae and P. ovale) most commonly infect humans. P. falciparum and P. vivax are the most prevalent species and P. falciparum is the

most dangerous. A fifth species, P. knowlesi (a species of Pla...

📄 **Reference:** Page 34

### 3. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

in early infancy. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America 2009;48(12):1704-12

Pubmed Journal

256. Genton B, D'Acremont V, Rare L, Baea K, Reeder JC, Alpers MP, et al. Plasmodium vivax and mixed infections are associated with

severe malaria in children: a prospective cohort study from Papua New Guinea. PLoS medicine 2008;5(6):e127 Pubmed Journal

257. Koch...

📄 **Reference:** Page 310

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

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 20. Query

> Monitoring after antimalarial treatment failure

**Sources (top hits)**
- Page 224: Therapeutic efficacy
- Page 22: Monitoring efficacy and safety of antimalarial drugs and resistance (2010)
- Page 224: Monitoring efficacy and safety of antimalarial drugs and resistance (2010)
- Page 22: National adaptation and implementation (2010)
- Page 227: National adaptation and implementation (2010)

**Response**

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

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 21. Query

> Quality assurance microscopy

**Sources (top hits)**
- Page 165: Untitled
- Page 225: General guiding principles for choosing a case management strategy and tools
- Page 164: Parasitological diagnosis
- Page 196: Guidance
- Page 200: Practical info

**Response**

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

### 5. Practical info

### Practical info

Practical info

Although it may be important to know whether a female has an intermediate G6PD activity,

programmatically it may not be feasible to tailor the treatments for women differently than for men.

Practical guidance should cover all aspects of safe implementation of a new diagnostic test e.g.

implementation plan, clear national guidelines, quality assurance/prequalification of tests, training of

users, quality assurance of testing, and the type of health care fac...

📄 **Reference:** Page 200


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 164, Page 165, Page 196, Page 200, Page 225

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 22. Query

> Integrated community case management fever

**Sources (top hits)**
- Page 164: Untitled
- Page 227: Other operational issues in managing effective treatment
- Page 225: General guiding principles for choosing a case management strategy and tools
- Page 260: Untitled
- Page 37: Global vector control response 2017–2030

**Response**

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

### 4. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

available

antimalarial medicine

A pharmaceutical product used in humans for the prevention, treatment or reduction of transmission of

malaria

artemisinin-based

combination therapy

A combination of an artemisinin derivative with a longer-acting antimalarial drug that has a different mode of

action

basic reproduction

number

The number of secondary cases that a single infection (index case) would generate in a ...

📄 **Reference:** Page 260

### 5. Global vector control response 2017–2030

### Global vector control response 2017–2030

Global vector control response 2017–2030

The vision of WHO and the broader infectious diseases community is a world free of human suffering from vector-borne diseases. In

2017, the World Health Assembly welcomed the Global vector control response 2017–2030 [16] (GVCR) and adopted a resolution to

promote an integrated approach to the control of vector-borne diseases. The approach builds on the concept of integrated vector

management (IVM), but wit...

📄 **Reference:** Page 37


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 37, Page 164, Page 225, Page 227, Page 260

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 23. Query

> Ethics of placebo-controlled malaria trials

**Sources (top hits)**
- Page 108: Untitled
- Page 221: GRADE
- Page 128: Untitled
- Page 105: Maternal death
- Page 208: GRADE

**Response**

```
**WHO Malaria Guidelines (NCBI Bookshelf)**

**Question:** Ethics of placebo-controlled malaria trials

### 1. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

supplemented by a cross-cutting review on chemoprevention and drug resistance (Plowe unpublished evidence), a civil society

consultation report on chemoprevention (CS4ME unpublished evidence) and contributions from the GDG membership, which

included former and current national malaria programme representatives. The GDG was supported by a Steering Group, which

included representatives from the WHO Departments for Se...

📄 **Reference:** Page 108

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

post-discharge. The main outcomes of interest were the impact of PDMC on re-admission (all-cause and severe anaemia),

mortality (all-cause), severe anaemia, and blood transfusion. Other outcomes of interest included confirmed clinical malaria,

severe malaria, anaemia, adverse events, and parasite prevalence. Three randomized double-blind placebo-controlled trials were

included in the review. All the trials were con...

📄 **Reference:** Page 128

### 4. Maternal death

### Maternal death

variable (risk ratio for maternal malaria: 0.73; 95% CI: 0.53–1.01; and for placental malaria: 0.89;

95% CI: 0.68–1.15).

•

Adverse events: IPTp-SP had a pooled prevalence of serious adverse events of 3.84% (95% CI:

2.20–5.88%) and a pooled prevalence of adverse events of 14.3% (95% CI: 4.9–27.5%). In two trials

comparing IPTp-SP to placebo or case management, the pooled risk ratio showed that IPTp-SP may

reduce maternal adverse events (risk ratio: 0.56; 95% CI: 0.30–1.0...

📄 **Reference:** Page 105

### 5. GRADE

### GRADE

GRADE

In a systematic review of primaquine for radical cure of P. vivax malaria [276], 14 days of primaquine was compared with

placebo or no treatment in 10 trials, and 14 days was compared with 7 days in one trial. The trials were conducted in

Colombia, Ethiopia, India, Pakistan and Thailand between 1992 and 2006.

In comparison with placebo or no primaquine:

14 days of primaquine (0.25 mg/kg bw per day) reduced relapses during 15 months of follow-up by about 40% (RR, 0.60; 95%

...

📄 **Reference:** Page 208


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 105, Page 108, Page 128, Page 208, Page 221

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 24. Query

> Vector control bed nets IRS

**Sources (top hits)**
- Page 297: Untitled
- Page 298: Untitled
- Page 68: Acceptability
- Page 276: Untitled
- Page 66: Untitled

**Response**

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

### 3. Acceptability

### Acceptability

Acceptability

The systematic review reported that wall decolourization, bad smell, an increase in bed bug nuisance,

and contamination of food grains were reported by study participants in India after spraying with

DDT [78]. However, these factors may depend on the insecticide and formulation used. In another study

conducted in Pakistan [56], no persistent odour or residue was reported after spraying with the pyrethroid

insecticide alpha-cypermethrin. In this same study, i...

📄 **Reference:** Page 68

### 4. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

Charles Wondji declared receiving research support, including grants, collaborations, sponsorships, and other funding from the

Innovative Vector Control Consortium (IVCC) exceeding US$ 5000. Ongoing studies aim to evaluate the entomological impact

of more recently developed indoor residual spraying (IRS) products, dual active ingredient nets and pyrethroid-PBO nets

against insecticide-resistant mosquitoes.

Josh Yu...

📄 **Reference:** Page 276

### 5. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

individual studies reported an RR of malaria infection of 0.70 (95% CI: 0.65–0.75) one month after

application and of 0.68 (95% CI: 0.66–0.70) one year after deployment, compared to no IRS.

The systematic review excluded studies in which other vector control interventions were being used,

including insecticide-treated nets (ITNs). A separate systematic review investigating the impact of co-

deploying IRS and ITNs ...

📄 **Reference:** Page 66


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 66, Page 68, Page 276, Page 297, Page 298

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---

### 25. Query

> Elimination strategies and surveillance

**Sources (top hits)**
- Page 228: 6. Interventions in the final phase of elimination and prevention of re-establishment
- Page 26: Untitled
- Page 253: 7. Surveillance
- Page 245: Reactive case detection and treatment to reduce transmission of malaria (2022)
- Page 146: (2022)

**Response**

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

### 2. Untitled

WHO guidelines for malaria - 13 August 2025 - World Health Organization (WHO)

Remark:

Until an area is nearing elimination or is post-elimination, it is unlikely that reactive case detection and treatment (RACDT) will

have any effect on malaria transmission. However, RACDT becomes an essential component of surveillance when countries are

nearing interruption of transmission to monitor progress towards elimination. When countries are post-elimination and working

towards certification, RACDT ...

📄 **Reference:** Page 26

### 3. 7. Surveillance

### 7. Surveillance

7. Surveillance

Surveillance is “the continuous and systematic collection, analysis and interpretation of disease-specific data, and the use of that data in

the planning, implementation and evaluation of public health practice” [300].

Pillar 3 of the Global technical strategy for malaria 2016–2030 [4] is to transform malaria surveillance into a key intervention in all malaria-

endemic countries and in those countries that have eliminated malaria but remain susceptible to...

📄 **Reference:** Page 253

### 4. Reactive case detection and treatment to reduce transmission of malaria (2022)

### Reactive case detection and treatment to reduce transmission of malaria (2022)

Reactive case detection and treatment to reduce transmission of malaria (2022)

In areas approaching elimination or post-elimination settings preventing re-establishment of transmission, all people residing with

or near a confirmed malaria case and all people who share the same risk of infection (e.g. co-travellers and co-workers) can be

tested for malaria and treated if positive.

Until an area is nearing elim...

📄 **Reference:** Page 245

### 5. (2022)

### (2022)

MDA to reduce transmission of P. vivax (2022)

In areas with P. vivax transmission, antimalarial medicine can be given as chemoprevention through mass drug administration

(MDA) to reduce transmission.

•

MDA may quickly reduce transmission of P. vivax, but the effect wanes within 1–3 months. Therefore, if MDA is

implemented, it should be one of several components of a robust malaria elimination programme (including, at minimum,

good coverage of case-based surveillance with parasi...

📄 **Reference:** Page 146


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 26, Page 146, Page 228, Page 245, Page 253

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

**Guardrail**: passed=`True` | errors=0 | warnings=0

---
