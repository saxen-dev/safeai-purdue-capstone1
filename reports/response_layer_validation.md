# Response layer validation (25 queries × 2 sources)

- **Generated (UTC)**: 2026-04-10T16:07:50.712931+00:00
- **Method**: `MedicalQASystem.answer_with_response()` after BM25 + guardrail

## Acceptance criteria

- **Guardrail**: `validation_passed == True` for all cases (required sections + triage line).
- **Triage**: `RED` if query matches danger-sign keywords; `YELLOW` for time-sensitive heuristics; else `GREEN`.
- **VHT output**: non-empty `vht_response`, `referral_note`, `quick_summary`.

Per preset: summary table (metrics only), then **full query** and **complete** formatted outputs for each of the 25 queries.

---

## Preset: `who-malaria`

- **Document**: WHO guidelines for malaria - 13 August 2025
- **Queries**: 25

### Summary table

| # | Triage | Guardrail OK | Confidence | VHT chars | Referral chars | Quick chars |
|---|--------|--------------|------------|-----------|----------------|-------------|
| 1 | GREEN | True | 0.73 | 1768 | 529 | 123 |
| 2 | GREEN | True | 0.74 | 1492 | 380 | 123 |
| 3 | GREEN | True | 0.85 | 1465 | 380 | 123 |
| 4 | GREEN | True | 0.86 | 1688 | 549 | 123 |
| 5 | GREEN | True | 0.89 | 1454 | 380 | 123 |
| 6 | GREEN | True | 0.83 | 1490 | 380 | 123 |
| 7 | GREEN | True | 0.64 | 1517 | 380 | 123 |
| 8 | GREEN | True | 0.66 | 1492 | 380 | 123 |
| 9 | GREEN | True | 0.80 | 1529 | 380 | 123 |
| 10 | GREEN | True | 0.87 | 1474 | 380 | 123 |
| 11 | GREEN | True | 0.88 | 1474 | 380 | 123 |
| 12 | GREEN | True | 0.68 | 1737 | 549 | 123 |
| 13 | GREEN | True | 0.83 | 1690 | 549 | 123 |
| 14 | GREEN | True | 0.73 | 1475 | 380 | 123 |
| 15 | GREEN | True | 0.74 | 1542 | 380 | 123 |
| 16 | GREEN | True | 0.84 | 1429 | 355 | 123 |
| 17 | GREEN | True | 0.85 | 1532 | 350 | 123 |
| 18 | GREEN | True | 0.81 | 1707 | 549 | 123 |
| 19 | GREEN | True | 0.64 | 1471 | 380 | 123 |
| 20 | GREEN | True | 0.82 | 1502 | 380 | 123 |
| 21 | GREEN | True | 0.86 | 1384 | 355 | 123 |
| 22 | GREEN | True | 0.95 | 1460 | 391 | 123 |
| 23 | GREEN | True | 0.83 | 1508 | 380 | 123 |
| 24 | GREEN | True | 0.78 | 1408 | 376 | 123 |
| 25 | GREEN | True | 0.76 | 1816 | 546 | 123 |

### Full queries and formatted outputs

#### Query 1

**Full query**

> What is the treatment for uncomplicated Plasmodium falciparum malaria?

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.73`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** How best can iCCM be implemented in emergency settings?
**Step 2:** Can mHealth applications play a role in improving the adherence of VHTs to clinical diagnostic and
**Step 3:** What treatment options are effective and safe in settings where referral is not possible?
**Step 4:** What are the elements that facilitate family members to use CCM services?
**Step 5:** Do family members follow treatment recommendations properly?

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 45: Management of illness [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 64: 4.1 References [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• How best can iCCM be implemented in emergency settings?
• Can mHealth applications play a role in improving the adherence of VHTs to clinical diagnostic and
• What treatment options are effective and safe in settings where referral is not possible?

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** What is the treatment for uncomplicated Plasmodium falciparum malaria?

### 1. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 2. Management of illness

### Management of illness

4.

How best can iCCM be implemented in emergency settings?

C. Management of illness

5.

Can mHealth applications play a role in improving the adherence of VHTs to clinical diagnostic and

treatment algorithms?

6.

What treatment options are effective and safe in settings where referral is not possible?

7.

What are the elements that facilitate family members to use CCM services?

8.

Do family members follow treatment recommendations properly?

9.

How can timely ...

📄 **Reference:** Page 45

### 3. 4.1 References

### 4.1 References

4.1 References...

📄 **Reference:** Page 64

### 4. Outcome 2

### Outcome 2

Outcome 2

61...

📄 **Reference:** Page 61

### 5. ACKNOWLEDGEMENTS

# ACKNOWLEDGEMENTS

ACKNOWLEDGEMENTS

The Ministry of Health acknowledges the efforts of many stakeholders and partners

who supported the development and update of different components of this guideline

for integrated community case management. iCCM is a key strategy to reducing child

mortality, and the iCCM TWG is commended for the successful update of the new

guidelines that build on past experiences in implementing the program in the country.

I acknowledge the following people for their ...

📄 **Reference:** Page 6


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 6, Page 10, Page 45, Page 61, Page 64

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 2

**Full query**

> Dosing artemisinin-based combination therapy in children under 5

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.74`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 36: Denominator: [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 36: Denominator: [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 35: Denominator: [HIGH FIDELITY]
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Dosing artemisinin-based combination therapy in children under 5

### 1. Denominator:

### Denominator:

Nutrition services

Numerator: Number children under five

assessed with Red MUAC  by the VHT

Denominator: Number of children under

five seen by the VHTs in the review period...

📄 **Reference:** Page 36

### 2. Denominator:

### Denominator:

Numerator: Number children under five

assessed with diarrheoa treated with

ORS/Zinc   by the VHT

Denominator: Number of children under

five seen by the VHTs with diarrheoa

HMIS 097B

Quarterly,

Anually

Program

District

Sub-County

Health Facility...

📄 **Reference:** Page 36

### 3. Denominator:

### Denominator:

Pneumonia cases

are

treated

appropriately.

Numerator: Number children under five

assessed with pneumonia/fast breathing

treated with Amoxicillin  by the VHT

Denominator: Number of children under

five seen by the VHTs with pneumonia/fast

breathing

HMIS 097B

Quarterly,

Anually

Program

District

Sub-County

Health Facility

35 | P a g e...

📄 **Reference:** Page 35

### 4. Denominator:

### Denominator:

Malaria cases are

treated

appropriately.

Numerator: Number children under five

assessed with confirmed malaria treated with

ACT  by the VHT

Denominator: Number of children under

five seen by the VHTs with malaria

HMIS 097B

Quarterly,

Anually

Program

District

Sub-County

Health Facility...

📄 **Reference:** Page 35

### 5. Denominator:

### Denominator:

iCCM

treatment

rate

Numerator: Number of treatments for

children under five provided by iCCM

conditions in twelve months in a target area

by point of treatment (Community or health

facility)

Denominator: Number of children under 5

in target areas at a given time divided by

1,000.

HMIS

UBOS

Annually

Program

District

Health Facility...

📄 **Reference:** Page 35


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 35, Page 36

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 3

**Full query**

> Severe malaria definition and management

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.85`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 61: Outcome 1 [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 6: ACKNOWLEDGEMENTS
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Severe malaria definition and management

### 1. Outcome 1

### Outcome 1

Outcome 1

Increased access to iCCM among hard to

reach communities

The proportion of newborn who receive

a home visit within 48 hours of birth by a

trained VHT administers the danger signs

checklist for the newborn and mother,

counsels, or refers as necessary.

80%

Baseline and

Activity

reports

The proportion of children with severe

malaria, pneumonia, diarrheoa, TB, and

HIV or; newborn with danger signs and

children with acute malnutrition whom

VHT promptly refers ...

📄 **Reference:** Page 61

### 2. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 3. ACKNOWLEDGEMENTS

# ACKNOWLEDGEMENTS

ACKNOWLEDGEMENTS

The Ministry of Health acknowledges the efforts of many stakeholders and partners

who supported the development and update of different components of this guideline

for integrated community case management. iCCM is a key strategy to reducing child

mortality, and the iCCM TWG is commended for the successful update of the new

guidelines that build on past experiences in implementing the program in the country.

I acknowledge the following people for their ...

📄 **Reference:** Page 6

### 4. Collection and Storage of medicines:

### Collection and Storage of medicines:

recovery, development of resistance, adverse medicine reactions, and overall failure of the program.

VHTs will be provided with training on the rational use of iCCM medicines. This will include case

definition/diagnosis, dispensing, record keeping, patient counseling, referral, patient follow-up, adverse

drug reaction monitoring (Pharmaco-vigilance), inventory management to avoid expiries and stockouts.

This will be reinforced by the use of appropria...

📄 **Reference:** Page 28

### 5. Medicines and supplies and supply chain management at the facility and community

### Medicines and supplies and supply chain management at the facility and community

STEP 3: Medicines and supplies and supply chain management at the facility and community...

📄 **Reference:** Page 23


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 6, Page 10, Page 23, Page 28, Page 61

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 4

**Full query**

> When to refer a patient with malaria to hospital?

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.86`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** To increase to at least 90% the proportion of children under-five years with malaria,
**Step 2:** To increase to at least 90% the proportion of sick children under-five years with fever and
**Step 3:** Increase to at least 90% the proportion of caregivers in hard-to-reach communities who
**Step 4:** To increase to at least 90%, the proportion of VHTs trained to manage malaria, pneumonia,

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 51: Untitled
• WHO Malaria Guidelines (NCBI Bookshelf), Page 9: BJECTIVES
• WHO Malaria Guidelines (NCBI Bookshelf), Page 61: Outcome 1 [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• To increase to at least 90% the proportion of children under-five years with malaria,
• To increase to at least 90% the proportion of sick children under-five years with fever and
• Increase to at least 90% the proportion of caregivers in hard-to-reach communities who

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** When to refer a patient with malaria to hospital?

### 1. Untitled

h) Screen children 6–59 months for moderate acute malnutrition (MAM) and severe acute malnutrition (SAM) through the use of mid-upper arm

circumference [MUAC] measurement and refer to health facility observing correct referral protocols.

i)

Conduct three postnatal home visits for both the mother and the baby on the 1st, 3rd, and 7th  day after delivery to educate and counsel the mother and

her family/spouse on recommended hygiene practices, essential newborn care practices, infant and young ...

📄 **Reference:** Page 51

### 2. BJECTIVES

### BJECTIVES

2.2 OBJECTIVES

1.

To increase to at least 90% the proportion of children under-five years with malaria,

pneumonia, and diarrhoea receiving appropriate treatment within 24 hours of the onset of

illness by 2025.

2.

To increase to at least 90% the proportion of sick children under-five years with fever and

danger signs, suspected TB, HIV, and those with severe acute malnutrition who are

identified in the community referred to health facilities.

3.

Increase to at least 90% t...

📄 **Reference:** Page 9

### 3. Outcome 1

### Outcome 1

Outcome 1

Increased access to iCCM among hard to

reach communities

The proportion of newborn who receive

a home visit within 48 hours of birth by a

trained VHT administers the danger signs

checklist for the newborn and mother,

counsels, or refers as necessary.

80%

Baseline and

Activity

reports

The proportion of children with severe

malaria, pneumonia, diarrheoa, TB, and

HIV or; newborn with danger signs and

children with acute malnutrition whom

VHT promptly refers ...

📄 **Reference:** Page 61

### 4. CTIVITIES

### CTIVITIES

5.6 VHT LEVEL ACTIVITIES

a)

Home visiting

b) Mobilization of communities for utilization of

f)

Follow up of people who have been discharged

from health facility and those on long term

treatment

g) Distribution of health commodities

h) Community information management

i)

Disease surveillance

health services

c)

Health Promotion and Education

d) Community-based case management of common

ill-health conditions

e)

Follow up of the mothers during pregnancy and

after bi...

📄 **Reference:** Page 12

### 5. S

### S

8.2 TERMS OF REFERENCE FOR ICCM VHTS

Any person serving as an iCCM service provider under the National iCCM program is expected to fulfill the following roles and responsibilities:

a) Actively participate in and potentially lead community mobilization and engagement for health. This includes participation in key community and national

health campaigns to prevent malaria, diarrheoa, pneumonia, malnutrition, and newborn illnesses.

b) Apply interpersonal communication skills to reinforce...

📄 **Reference:** Page 50


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 9, Page 12, Page 50, Page 51, Page 61

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 5

**Full query**

> Pregnancy and malaria treatment recommendations

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.89`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 61: Goal [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 12: CTIVITIES
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Pregnancy and malaria treatment recommendations

### 1. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 2. Goal

### Goal

Goal

To increase to at least 80% the proportion

of children under-five years receiving

appropriate treatment for malaria,

pneumonia, and diarrhoea within 24 hours

of the onset of illness

The proportion of children under-five

years receiving appropriate treatment for

malaria, pneumonia, and diarrhoea within

24 hours of the onset of illness

80%

Baseline

Activity

reports

MoH...

📄 **Reference:** Page 61

### 3. CTIVITIES

### CTIVITIES

5.6 VHT LEVEL ACTIVITIES

a)

Home visiting

b) Mobilization of communities for utilization of

f)

Follow up of people who have been discharged

from health facility and those on long term

treatment

g) Distribution of health commodities

h) Community information management

i)

Disease surveillance

health services

c)

Health Promotion and Education

d) Community-based case management of common

ill-health conditions

e)

Follow up of the mothers during pregnancy and

after bi...

📄 **Reference:** Page 12

### 4. S

### S

8.2 TERMS OF REFERENCE FOR ICCM VHTS

Any person serving as an iCCM service provider under the National iCCM program is expected to fulfill the following roles and responsibilities:

a) Actively participate in and potentially lead community mobilization and engagement for health. This includes participation in key community and national

health campaigns to prevent malaria, diarrheoa, pneumonia, malnutrition, and newborn illnesses.

b) Apply interpersonal communication skills to reinforce...

📄 **Reference:** Page 50

### 5. FOREWORD

# FOREWORD

FOREWORD

Integrated community case management (iCCM) of childhood infection saves lives in

hard-to-reach communities in Uganda.  The objective of this strategy is to strengthen

iCCM implementation and and set the path to institutionalizing rapid reduction in

under five mortality in the national and district health during 2020 to 2060.  The

Village health teams in remote poor urban and rural communities provide the needed

lifesaving treatments to sick children within 24 hours wi...

📄 **Reference:** Page 5


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 5, Page 10, Page 12, Page 50, Page 61

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 6

**Full query**

> Drug interactions with artemether lumefantrine

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.83`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 15: CCM [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 24: Support Supervision:
• WHO Malaria Guidelines (NCBI Bookshelf), Page 20: Pharmaco-vigilance and medicine inspection:
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Drug interactions with artemether lumefantrine

### 1. CCM

### CCM

6.1.3 MEDICINE AND COMMODITY SUPPLY MANAGEMENT FOR ICCM

Improving the supply chain for iCCM drugs and commodities constitutes one of the most critical aspects

for the performance and sustainability of the program. The medicines for iCCM include:

Artemether/Lumefantrine(20mg/120mg tablet strength), Amoxicillin 125mg dispersible tablet, Low

osmolarity ORS, Zinc 20mg tablet and rectal artesunate (50mg). Other commodities include respiratory

timers, rapid diagnostic tests, registers, m...

📄 **Reference:** Page 15

### 2. Support Supervision:

### Support Supervision:

to the VHTs will be done immediately after the training on iCCM. Subsequently, VHTs will be supplied

with commodities based on their consumption rate. The health facilities will follow proper inventory

management procedures to replenish medicine stocks to VHTs, including cross-checking VHT registers

and consumption logs to ensure appropriate accountability of the medicines. Health Facilities will also

ensure the availability of drugs and supplies to handle referred ...

📄 **Reference:** Page 24

### 3. Pharmaco-vigilance and medicine inspection:

### Pharmaco-vigilance and medicine inspection:

d) Pharmaco-vigilance and medicine inspection: Standard adverse drug forms will be used to track

adverse reactions reported by VHTs. The VHT follows up sick children per protocol, including

identifying possible adverse medicine reactions, and requests HF staff for investigation. The HF staff

investigates possible adverse medicine reactions and documents on standard Adverse Drug Reaction

Forms, reported to the DHO office and NDA Pharmaco-vigila...

📄 **Reference:** Page 20

### 4. Collection and Storage of medicines:

### Collection and Storage of medicines:

recovery, development of resistance, adverse medicine reactions, and overall failure of the program.

VHTs will be provided with training on the rational use of iCCM medicines. This will include case

definition/diagnosis, dispensing, record keeping, patient counseling, referral, patient follow-up, adverse

drug reaction monitoring (Pharmaco-vigilance), inventory management to avoid expiries and stockouts.

This will be reinforced by the use of appropria...

📄 **Reference:** Page 28

### 5. Untitled

It is the responsibility of the national level to mobilize resources, procure, stock, and supply districts with

iCCM medicines and commodities through the National Medical Stores. iCCM medicines and

commodities will be procured alongside essential medicines and health supplies for use at the health facility

and community. The routine medicine supply chain from the central to the community will be used.  For

the private sector, implementing entities will follow guidance from the MOH and Natio...

📄 **Reference:** Page 16


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 15, Page 16, Page 20, Page 24, Page 28

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 7

**Full query**

> Prophylaxis for travelers to endemic areas

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.64`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 25: Supervising VHTs in their communities ( Home Visit
• WHO Malaria Guidelines (NCBI Bookshelf), Page 4: Untitled [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 14: District pre-visit for sensitization
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Prophylaxis for travelers to endemic areas

### 1. Supervising VHTs in their communities ( Home Visit

### Supervising VHTs in their communities ( Home Visit

STEP 6: Supervising VHTs in their communities ( Home Visit

Health workers should supplement group meetings at health facilities with monthly community visits

to VHTs for at least the first three months after training to identify problems quickly and coach those

with difficulties. During these visits, the supervisors should:

 Observe the actual environment where the VHT operates, e.g., how they store medicines.

The VHT provides iCCM or...

📄 **Reference:** Page 25

### 2. Untitled

7.3

KEY NATIONAL PERFORMANCE INDICATORS ..................................................................... 33

7.4

THE M&E FRAMEWORK ................................................................................................... 38

7.5

KEY AREAS OF OPERATIONAL RESEARCH .......................................................................... 45...

📄 **Reference:** Page 4

### 3. District pre-visit for sensitization

### District pre-visit for sensitization

STEP 4: District pre-visit for sensitization

Before introducing iCCM in a district, the national task force will pre-visit districts to sensitize them on

the iCCM policy, reach a consensus on the plan to roll out iCCM in the districts, including funding sources.

The target group will be the extended district health team, including partners involved in community

mobilization activities. The following materials developed by the Ministry of Health will ...

📄 **Reference:** Page 14

### 4. Denominator:

### Denominator:

iCCM

treatment

rate

Numerator: Number of treatments for

children under five provided by iCCM

conditions in twelve months in a target area

by point of treatment (Community or health

facility)

Denominator: Number of children under 5

in target areas at a given time divided by

1,000.

HMIS

UBOS

Annually

Program

District

Health Facility...

📄 **Reference:** Page 35

### 5. Equity and Access:

### Equity and Access:



Community Ownership: The community is responsible for the selection, supervision, and support of the VHT.

The VHTs are fully accountable to the communities they operate in, and their services/ responsibilities are

community-driven.



Equity and Access:  iCCM VHT services are meant to provide family-centered integrated care and increase

access within 24 hours for all sick children under five years of the community, especially those in rural peripheral

areas or mar...

📄 **Reference:** Page 9


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 4, Page 9, Page 14, Page 25, Page 35

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 8

**Full query**

> Rapid diagnostic test interpretation false positives

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.66`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 33: If low [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 20: Pharmaco-vigilance and medicine inspection:
• WHO Malaria Guidelines (NCBI Bookshelf), Page 15: CCM [HIGH FIDELITY]
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Rapid diagnostic test interpretation false positives

### 1. If low

### If low

If low  Explore why...

📄 **Reference:** Page 33

### 2. Pharmaco-vigilance and medicine inspection:

### Pharmaco-vigilance and medicine inspection:

d) Pharmaco-vigilance and medicine inspection: Standard adverse drug forms will be used to track

adverse reactions reported by VHTs. The VHT follows up sick children per protocol, including

identifying possible adverse medicine reactions, and requests HF staff for investigation. The HF staff

investigates possible adverse medicine reactions and documents on standard Adverse Drug Reaction

Forms, reported to the DHO office and NDA Pharmaco-vigila...

📄 **Reference:** Page 20

### 3. CCM

### CCM

6.1.3 MEDICINE AND COMMODITY SUPPLY MANAGEMENT FOR ICCM

Improving the supply chain for iCCM drugs and commodities constitutes one of the most critical aspects

for the performance and sustainability of the program. The medicines for iCCM include:

Artemether/Lumefantrine(20mg/120mg tablet strength), Amoxicillin 125mg dispersible tablet, Low

osmolarity ORS, Zinc 20mg tablet and rectal artesunate (50mg). Other commodities include respiratory

timers, rapid diagnostic tests, registers, m...

📄 **Reference:** Page 15

### 4. SSUMPTIONS

### SSUMPTIONS

WHO

RISKS / ASSUMPTIONS

1 2 3 4 5...

📄 **Reference:** Page 62

### 5. RINCIPLES

### RINCIPLES

7.1.3 PRINCIPLES

1

iCCM Data is collected based on needs within the general management processes.

2

Work along the iCCM logframe measured by the corresponding indicators

3

Build iCCM M&E into the national HMIS framework so as not to overwhelm providers or make monitoring an additional activity by utilizing existing

touchpoints

4

Minimal tolerance for insufficient data by building quality assurance processes to test the data for quality and giving constant feedback on acce...

📄 **Reference:** Page 31


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 15, Page 20, Page 31, Page 33, Page 62

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 9

**Full query**

> G6PD deficiency and primaquine

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.80`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 18: DVOCACY AND SENSITIZATION [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 26: DVOCACY AND SENSITIZATION AT THE COMMUNITY [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 33: UALITY [HIGH FIDELITY]
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** G6PD deficiency and primaquine

### 1. DVOCACY AND SENSITIZATION

### DVOCACY AND SENSITIZATION

6.2.1 ADVOCACY AND SENSITIZATION...

📄 **Reference:** Page 18

### 2. DVOCACY AND SENSITIZATION AT THE COMMUNITY

### DVOCACY AND SENSITIZATION AT THE COMMUNITY

6.3.1 ADVOCACY AND SENSITIZATION AT THE COMMUNITY...

📄 **Reference:** Page 26

### 3. UALITY

### UALITY

QUALITY

33 | P a g e...

📄 **Reference:** Page 33

### 4. Districts retain the mandate and responsibility to prepare medicines and supplies plans,

### Districts retain the mandate and responsibility to prepare medicines and supplies plans,

a) Districts retain the mandate and responsibility to prepare medicines and supplies plans, originate

orders, follow up with national medical stores, and monitor utilization (health systems). District

procurement plans (for HCIV and above ) and essential medicines kits ( HC3 and HC2) for drugs and

supplies will be prepared through the aggregation of health facility plans which should be annexed to

t...

📄 **Reference:** Page 19

### 5. TPR

### TPR

If high TPR Encourage

prevention

measures

at

different levels

If low  Maintain...

📄 **Reference:** Page 36


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 18, Page 19, Page 26, Page 33, Page 36

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 10

**Full query**

> Malaria vaccine recommendations RTS,S R21

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.87`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 3: CONTENTS [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 56: (A) [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 56: Untitled [HIGH FIDELITY]
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Malaria vaccine recommendations RTS,S R21

### 1. CONTENTS

# CONTENTS

CONTENTS...

📄 **Reference:** Page 3

### 2. (A)

### (A)

(A)...

📄 **Reference:** Page 56

### 3. Untitled

Stakeholder Matrix...

📄 **Reference:** Page 56

### 4. 5

### 5

5

CONTINUOUS SUPERVISION AND

MENTORING...

📄 **Reference:** Page 26

### 5. Development and pretesting training materials

### Development and pretesting training materials

a)

Development and pretesting training materials

The national-level team will adapt and pretest WHO generic materials by reviewing national policies,

clinical guidelines, and drug supply systems to determine the relevant recommendations to include in the

course materials for iCCM (the case management charts, modules, and other materials including

community supply chain management. They will also be required to develop refresher training mat...

📄 **Reference:** Page 15


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 3, Page 15, Page 26, Page 56

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 11

**Full query**

> Resistance to artemisinin in Southeast Asia

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.88`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 28: Collection and Storage of medicines:
• WHO Malaria Guidelines (NCBI Bookshelf), Page 5: FOREWORD
• WHO Malaria Guidelines (NCBI Bookshelf), Page 44: ORKPLAN [HIGH FIDELITY]
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Resistance to artemisinin in Southeast Asia

### 1. Collection and Storage of medicines:

### Collection and Storage of medicines:

recovery, development of resistance, adverse medicine reactions, and overall failure of the program.

VHTs will be provided with training on the rational use of iCCM medicines. This will include case

definition/diagnosis, dispensing, record keeping, patient counseling, referral, patient follow-up, adverse

drug reaction monitoring (Pharmaco-vigilance), inventory management to avoid expiries and stockouts.

This will be reinforced by the use of appropria...

📄 **Reference:** Page 28

### 2. FOREWORD

# FOREWORD

FOREWORD

Integrated community case management (iCCM) of childhood infection saves lives in

hard-to-reach communities in Uganda.  The objective of this strategy is to strengthen

iCCM implementation and and set the path to institutionalizing rapid reduction in

under five mortality in the national and district health during 2020 to 2060.  The

Village health teams in remote poor urban and rural communities provide the needed

lifesaving treatments to sick children within 24 hours wi...

📄 **Reference:** Page 5

### 3. ORKPLAN

### ORKPLAN

7.4.8 M&E WORKPLAN...

📄 **Reference:** Page 44

### 4. Integrate iCCM in the facility and VHT supervision

### Integrate iCCM in the facility and VHT supervision

community health activities for each facility.  Awareness building and mobilization of sub-county councils and other sectors to support iCCM services will

be critical.

b) Conduct integrated supportive supervision at health center III

c) Ensure the availability of appropriate IMNCI capacity at iCCM referral facilities in the HSD

d) Integrate iCCM in the facility and VHT supervision using quality audits, coaching, and mentorship mechanism...

📄 **Reference:** Page 49

### 5. location

### location

(B)

activities

location...

📄 **Reference:** Page 56


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 5, Page 28, Page 44, Page 49, Page 56

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 12

**Full query**

> Hypoglycemia in severe malaria

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.68`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** To increase to at least 90% the proportion of children under-five years with malaria,
**Step 2:** To increase to at least 90% the proportion of sick children under-five years with fever and
**Step 3:** Increase to at least 90% the proportion of caregivers in hard-to-reach communities who
**Step 4:** To increase to at least 90%, the proportion of VHTs trained to manage malaria, pneumonia,
**Step 5:** Application of iCCM job aid

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 61: Outcome 1 [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 9: BJECTIVES
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• To increase to at least 90% the proportion of children under-five years with malaria,
• To increase to at least 90% the proportion of sick children under-five years with fever and
• Increase to at least 90% the proportion of caregivers in hard-to-reach communities who

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Hypoglycemia in severe malaria

### 1. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 2. Outcome 1

### Outcome 1

Outcome 1

Increased access to iCCM among hard to

reach communities

The proportion of newborn who receive

a home visit within 48 hours of birth by a

trained VHT administers the danger signs

checklist for the newborn and mother,

counsels, or refers as necessary.

80%

Baseline and

Activity

reports

The proportion of children with severe

malaria, pneumonia, diarrheoa, TB, and

HIV or; newborn with danger signs and

children with acute malnutrition whom

VHT promptly refers ...

📄 **Reference:** Page 61

### 3. BJECTIVES

### BJECTIVES

2.2 OBJECTIVES

1.

To increase to at least 90% the proportion of children under-five years with malaria,

pneumonia, and diarrhoea receiving appropriate treatment within 24 hours of the onset of

illness by 2025.

2.

To increase to at least 90% the proportion of sick children under-five years with fever and

danger signs, suspected TB, HIV, and those with severe acute malnutrition who are

identified in the community referred to health facilities.

3.

Increase to at least 90% t...

📄 **Reference:** Page 9

### 4. delivery

### delivery

Service

delivery

for especially OVC

 Receiving facility well-stocked, sufficient staff

work.

 Timely reporting

to the health center for severe or chronic

cases.



trained in IMNCI and inpatient facilities

 Update and standardize basic iCCM training

 Develop district iCCM roll out plan

 3-day refresher training for health

 At least  HWs trained on iCCM in a standard 6-day

 At least 2 VHT per targeted village trained

materials4

 Reorient national-level master ...

📄 **Reference:** Page 46

### 5. Outcome 2

### Outcome 2

Outcome 2

61...

📄 **Reference:** Page 61


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 9, Page 10, Page 46, Page 61

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 13

**Full query**

> Fluid management in severe malaria adults

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.83`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** To increase to at least 90% the proportion of children under-five years with malaria,
**Step 2:** To increase to at least 90% the proportion of sick children under-five years with fever and
**Step 3:** Increase to at least 90% the proportion of caregivers in hard-to-reach communities who
**Step 4:** To increase to at least 90%, the proportion of VHTs trained to manage malaria, pneumonia,

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 61: Outcome 1 [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 50: S
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• To increase to at least 90% the proportion of children under-five years with malaria,
• To increase to at least 90% the proportion of sick children under-five years with fever and
• Increase to at least 90% the proportion of caregivers in hard-to-reach communities who

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Fluid management in severe malaria adults

### 1. Outcome 1

### Outcome 1

Outcome 1

Increased access to iCCM among hard to

reach communities

The proportion of newborn who receive

a home visit within 48 hours of birth by a

trained VHT administers the danger signs

checklist for the newborn and mother,

counsels, or refers as necessary.

80%

Baseline and

Activity

reports

The proportion of children with severe

malaria, pneumonia, diarrheoa, TB, and

HIV or; newborn with danger signs and

children with acute malnutrition whom

VHT promptly refers ...

📄 **Reference:** Page 61

### 2. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 3. S

### S

8.2 TERMS OF REFERENCE FOR ICCM VHTS

Any person serving as an iCCM service provider under the National iCCM program is expected to fulfill the following roles and responsibilities:

a) Actively participate in and potentially lead community mobilization and engagement for health. This includes participation in key community and national

health campaigns to prevent malaria, diarrheoa, pneumonia, malnutrition, and newborn illnesses.

b) Apply interpersonal communication skills to reinforce...

📄 **Reference:** Page 50

### 4. BJECTIVES

### BJECTIVES

2.2 OBJECTIVES

1.

To increase to at least 90% the proportion of children under-five years with malaria,

pneumonia, and diarrhoea receiving appropriate treatment within 24 hours of the onset of

illness by 2025.

2.

To increase to at least 90% the proportion of sick children under-five years with fever and

danger signs, suspected TB, HIV, and those with severe acute malnutrition who are

identified in the community referred to health facilities.

3.

Increase to at least 90% t...

📄 **Reference:** Page 9

### 5. ACKNOWLEDGEMENTS

# ACKNOWLEDGEMENTS

ACKNOWLEDGEMENTS

The Ministry of Health acknowledges the efforts of many stakeholders and partners

who supported the development and update of different components of this guideline

for integrated community case management. iCCM is a key strategy to reducing child

mortality, and the iCCM TWG is commended for the successful update of the new

guidelines that build on past experiences in implementing the program in the country.

I acknowledge the following people for their ...

📄 **Reference:** Page 6


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 6, Page 9, Page 10, Page 50, Page 61

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 14

**Full query**

> Exchange transfusion malaria criteria

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.73`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 56: (A) [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 3: CONTENTS [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 27: Selection of VHT for iCCM
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Exchange transfusion malaria criteria

### 1. (A)

### (A)

(A)...

📄 **Reference:** Page 56

### 2. CONTENTS

# CONTENTS

CONTENTS...

📄 **Reference:** Page 3

### 3. Selection of VHT for iCCM

### Selection of VHT for iCCM

aids, HMIS tools, and medicines and supplies to support the implementation of their duties.

Communities should have close linkages with facilities and should notify them on problems in

implementing iCCM, e.g., attrition, adverse reactions on use of medicines, non-performing VHTs,

a) Selection of VHT for iCCM Villages will apply the following selection criteria to propose VHT

candidates for iCCM training and implementation.  The VHT for iCCM must be:

1

exempla...

📄 **Reference:** Page 27

### 4. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 5. Outcome 2

### Outcome 2

Outcome 2

61...

📄 **Reference:** Page 61


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 3, Page 10, Page 27, Page 56, Page 61

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 15

**Full query**

> Cerebral malaria supportive care

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.74`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 50: S
• WHO Malaria Guidelines (NCBI Bookshelf), Page 13: Supportive Tool:  iCCM Benchmark tool

---
**GUARDRAIL WARNINGS:**

• Citation to page 1 not found in knowledge base
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Cerebral malaria supportive care

### 1. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 2. S

### S

8.2 TERMS OF REFERENCE FOR ICCM VHTS

Any person serving as an iCCM service provider under the National iCCM program is expected to fulfill the following roles and responsibilities:

a) Actively participate in and potentially lead community mobilization and engagement for health. This includes participation in key community and national

health campaigns to prevent malaria, diarrheoa, pneumonia, malnutrition, and newborn illnesses.

b) Apply interpersonal communication skills to reinforce...

📄 **Reference:** Page 50

### 3. Supportive Tool:  iCCM Benchmark tool

### Supportive Tool:  iCCM Benchmark tool

Step 1: Regular meetings of the National iCCM TWG

At the national level, the mandate is to ensure continuous advocacy for increased resources, partners, and

buy-in for iCCM. The national level will spearhead coordination, harmonize advocacy activities, and

disseminate policy guidelines within and outside the sector.  This step is aimed at facilitating the integration

of iCCM services with multiple national strategies, including Child Survival, IMNCI...

📄 **Reference:** Page 13

### 4. Deliver the community sensitization to improve care-seeking behaviour:

### Deliver the community sensitization to improve care-seeking behaviour:

As a hub of community-based health services, VHTs should be facilitated to transfer health literacy and

skills between individuals and families to make informed choices and decisions for behavioural change.

They should also create demand for better health services, mutual understanding, and trust among key

actors within the community. Communities should Support the VHTs to:

a) Deliver the community sensitization to i...

📄 **Reference:** Page 27

### 5. Outcome 3

### Outcome 3

Outcome 3

Increased Knowledge of and Demand for

iCCM

The proportion of caregivers and

community members have positive health

behaviors and practices (e.g., ITN use,

completed referral for pneumonia, hand-

washing, safe disposal of infant fecal

matter, exclusive breastfeeding).

80%

Evaluation

report...

📄 **Reference:** Page 62


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 10, Page 13, Page 27, Page 50, Page 62

---
**🧪 Guardrail Brain Validation:**

**⚠️ Warnings:**
• Citation to page 1 not found in knowledge base

```

---

#### Query 16

**Full query**

> Artesunate dose for severe malaria IV

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.84`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Application of iCCM job aid
**Step 2:** Filling of VHT registers and
**Step 3:** Certificates.

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 37: Rectal artesunate [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 37: Denominator: [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Application of iCCM job aid
• Filling of VHT registers and
• Certificates.

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Artesunate dose for severe malaria IV

### 1. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 2. Rectal artesunate

### Rectal artesunate

Availability

of

Rectal artesunate...

📄 **Reference:** Page 37

### 3. Denominator:

### Denominator:

Numerator: Number of villages reported

with stock out of rectal artesunate in the

review period

Denominator: Total number of villages

reporting

HMIS  097B

Quarterly

Program

District

Health Facility

37 | P a g e...

📄 **Reference:** Page 37

### 4. Untitled

catchment populations.  The maps should be the basis for prioritizing villages that need the iCCM

approach for impact.  The

HSD/in-charge

of

the

Health Centre IV takes on

the leadership role for iCCM

institutionalization

and

works with HC III and II in-

charges

and

Health

Inspector/Assistants

for

advocacy at sub-county local

governments and planning

implementation M&E of

iCCM activities.

1

VHT mapping and health

facility readiness assessment

2

iCCM case load projection

3
...

📄 **Reference:** Page 22

### 5. delivery

### delivery

Service

delivery

for especially OVC

 Receiving facility well-stocked, sufficient staff

work.

 Timely reporting

to the health center for severe or chronic

cases.



trained in IMNCI and inpatient facilities

 Update and standardize basic iCCM training

 Develop district iCCM roll out plan

 3-day refresher training for health

 At least  HWs trained on iCCM in a standard 6-day

 At least 2 VHT per targeted village trained

materials4

 Reorient national-level master ...

📄 **Reference:** Page 46


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 10, Page 22, Page 37, Page 46

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 17

**Full query**

> Rectal artesunate pre-referral children

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.85`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Video / DVD exercises
**Step 2:** VCR equipment, videotape, or DVD
**Step 3:** Flip chart
**Step 4:** Masking tape
**Step 5:** Measuring containers litre (500 ml water bottle), spoons, cups

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 37: Rectal artesunate [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 60: Additional Logistics [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Video / DVD exercises
• VCR equipment, videotape, or DVD
• Flip chart

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Rectal artesunate pre-referral children

### 1. Rectal artesunate

### Rectal artesunate

Availability

of

Rectal artesunate...

📄 **Reference:** Page 37

### 2. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 3. Additional Logistics

### Additional Logistics

Item

Number

1.

Video / DVD exercises

1 set / room

2.

VCR equipment, videotape, or DVD

1 set/room

3.

Flip chart

1 set / room

4.

Masking tape

2

5.

Markers

6

6.

Pens

One person

7.

Measuring containers litre (500 ml water bottle), spoons, cups

1 set per room

8.

Dolls

1 per room

9.

MUAC Tape

10. Timers

Medicine and supplies

11. mRDT

12. ORS sachets

3 / participant

13. Zinc tablets

Two packs /person

14. ACTs tablets(blue and yellow)

24 tabs...

📄 **Reference:** Page 60

### 4. Carry Out District Preparatory And Orientation Pre-Visit.

### Carry Out District Preparatory And Orientation Pre-Visit.

STEP 1: Carry Out District Preparatory And Orientation Pre-Visit.

The district will receive an iCCM preparatory visit from the national level. The district will mobilize the

extended DHT, CAO, ACAO Health, RDC, LCV5, Secretary for health and have them oriented on vital

components of iCCM implementation by the national task force.

 Introduce the iCCM guidelines and present a summary of the steps taken for their development.

 Br...

📄 **Reference:** Page 18

### 5. Pharmaco-vigilance and medicine inspection:

### Pharmaco-vigilance and medicine inspection:

d) Pharmaco-vigilance and medicine inspection: Standard adverse drug forms will be used to track

adverse reactions reported by VHTs. The VHT follows up sick children per protocol, including

identifying possible adverse medicine reactions, and requests HF staff for investigation. The HF staff

investigates possible adverse medicine reactions and documents on standard Adverse Drug Reaction

Forms, reported to the DHO office and NDA Pharmaco-vigila...

📄 **Reference:** Page 20


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 10, Page 18, Page 20, Page 37, Page 60

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 18

**Full query**

> Malaria in HIV coinfection

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.81`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** To increase to at least 90% the proportion of children under-five years with malaria,
**Step 2:** To increase to at least 90% the proportion of sick children under-five years with fever and
**Step 3:** Increase to at least 90% the proportion of caregivers in hard-to-reach communities who
**Step 4:** To increase to at least 90%, the proportion of VHTs trained to manage malaria, pneumonia,

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 36: Denominator: [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 6: ACKNOWLEDGEMENTS
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• To increase to at least 90% the proportion of children under-five years with malaria,
• To increase to at least 90% the proportion of sick children under-five years with fever and
• Increase to at least 90% the proportion of caregivers in hard-to-reach communities who

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Malaria in HIV coinfection

### 1. Denominator:

### Denominator:

HIV services

Numerator: Number children under five

assessed with possible exposure to HIV by the

VHT

Denominator: Number of children under

five seen by the VHTs in the review period

HMIS 097B

Quarterly,

Anually

Program

District

Sub-County

Health Facility...

📄 **Reference:** Page 36

### 2. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 3. ACKNOWLEDGEMENTS

# ACKNOWLEDGEMENTS

ACKNOWLEDGEMENTS

The Ministry of Health acknowledges the efforts of many stakeholders and partners

who supported the development and update of different components of this guideline

for integrated community case management. iCCM is a key strategy to reducing child

mortality, and the iCCM TWG is commended for the successful update of the new

guidelines that build on past experiences in implementing the program in the country.

I acknowledge the following people for their ...

📄 **Reference:** Page 6

### 4. Outcome 1

### Outcome 1

Outcome 1

Increased access to iCCM among hard to

reach communities

The proportion of newborn who receive

a home visit within 48 hours of birth by a

trained VHT administers the danger signs

checklist for the newborn and mother,

counsels, or refers as necessary.

80%

Baseline and

Activity

reports

The proportion of children with severe

malaria, pneumonia, diarrheoa, TB, and

HIV or; newborn with danger signs and

children with acute malnutrition whom

VHT promptly refers ...

📄 **Reference:** Page 61

### 5. BJECTIVES

### BJECTIVES

2.2 OBJECTIVES

1.

To increase to at least 90% the proportion of children under-five years with malaria,

pneumonia, and diarrhoea receiving appropriate treatment within 24 hours of the onset of

illness by 2025.

2.

To increase to at least 90% the proportion of sick children under-five years with fever and

danger signs, suspected TB, HIV, and those with severe acute malnutrition who are

identified in the community referred to health facilities.

3.

Increase to at least 90% t...

📄 **Reference:** Page 9


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 6, Page 9, Page 10, Page 36, Page 61

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 19

**Full query**

> Species Plasmodium vivax relapse treatment

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.64`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 62: ON [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 35: Denominator: [HIGH FIDELITY]
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Species Plasmodium vivax relapse treatment

### 1. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 2. ON

### ON

ON

Improved quality of iCCM services

The proportion of VHTs with zero

stock-outs of first-line treatment and

diagnostics for malaria, pneumonia, and

diarrheoa.

75%

Evaluation

report

The proportion of VHTs giving standard

treatment for malaria, pneumonia, and

diarrheoa.

80%

Evaluation

report

The proportion of VHTs that receive

quarterly support supervision,

mentorship, and coaching

80%

Evaluation

report

The proportion of health facilities

implementing iCCM that have ...

📄 **Reference:** Page 62

### 3. Denominator:

### Denominator:

iCCM

treatment

rate

Numerator: Number of treatments for

children under five provided by iCCM

conditions in twelve months in a target area

by point of treatment (Community or health

facility)

Denominator: Number of children under 5

in target areas at a given time divided by

1,000.

HMIS

UBOS

Annually

Program

District

Health Facility...

📄 **Reference:** Page 35

### 4. Rectal artesunate

### Rectal artesunate

Availability

of

Rectal artesunate...

📄 **Reference:** Page 37

### 5. Goal

### Goal

Goal

To increase to at least 80% the proportion

of children under-five years receiving

appropriate treatment for malaria,

pneumonia, and diarrhoea within 24 hours

of the onset of illness

The proportion of children under-five

years receiving appropriate treatment for

malaria, pneumonia, and diarrhoea within

24 hours of the onset of illness

80%

Baseline

Activity

reports

MoH...

📄 **Reference:** Page 61


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 10, Page 35, Page 37, Page 61, Page 62

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 20

**Full query**

> Monitoring after antimalarial treatment failure

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.82`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 61: Annex 8: Monitoring and Evaluation workplan [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 62: ON [HIGH FIDELITY]
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Monitoring after antimalarial treatment failure

### 1. Annex 8: Monitoring and Evaluation workplan

## Annex 8: Monitoring and Evaluation workplan

Annex 8: Monitoring and Evaluation workplan...

📄 **Reference:** Page 61

### 2. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 3. ON

### ON

ON

Improved quality of iCCM services

The proportion of VHTs with zero

stock-outs of first-line treatment and

diagnostics for malaria, pneumonia, and

diarrheoa.

75%

Evaluation

report

The proportion of VHTs giving standard

treatment for malaria, pneumonia, and

diarrheoa.

80%

Evaluation

report

The proportion of VHTs that receive

quarterly support supervision,

mentorship, and coaching

80%

Evaluation

report

The proportion of health facilities

implementing iCCM that have ...

📄 **Reference:** Page 62

### 4. ICCM MONITORING AND EVALUATION FRAMEWORK

# ICCM MONITORING AND EVALUATION FRAMEWORK

7 ICCM MONITORING AND EVALUATION FRAMEWORK...

📄 **Reference:** Page 29

### 5. Collection and Storage of medicines:

### Collection and Storage of medicines:

recovery, development of resistance, adverse medicine reactions, and overall failure of the program.

VHTs will be provided with training on the rational use of iCCM medicines. This will include case

definition/diagnosis, dispensing, record keeping, patient counseling, referral, patient follow-up, adverse

drug reaction monitoring (Pharmaco-vigilance), inventory management to avoid expiries and stockouts.

This will be reinforced by the use of appropria...

📄 **Reference:** Page 28


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 10, Page 28, Page 29, Page 61, Page 62

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 21

**Full query**

> Quality assurance microscopy

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.86`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Conducting data quality audits (DQA)
**Step 2:** Short-term M&E Technical Assistance

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 47: assurance [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 44: x [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 48: :
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Conducting data quality audits (DQA)
• Short-term M&E Technical Assistance

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Quality assurance microscopy

### 1. assurance

### assurance

Support

Supervision

and

quality

assurance

VHT

using

supervisor’s

Check-list

and

supervisor’s summary form

 Submit supervisor’s summary form to DHO

 Replenish VHW stocks as needed

 Orient all staff to support the VHTs

Coverage Chart

 the pool of trained district supervisors to

performance

and

obtain

accurate,

timely

information about cases and necessary supplies

 Developing and disseminating the guidelines for

ensure an optimal ratio of supervisors to

H...

📄 **Reference:** Page 47

### 2. x

### x

12. Conducting data quality audits (DQA)

x

x

x

x

x

iCCM TWG

DHI

Improved Data quality

Incorporated in DHI

13. Short-term M&E Technical Assistance

x

iCCM TWG

IPs

TA procured

44 | P a g e...

📄 **Reference:** Page 44

### 3. :

### :

referral and counter-referral system for iCCM. Integrate iCCM within existing quality improvement processes.

f)

Communication and social mobilization: The TWG shall develop and use a communication and social mobilization plan and strategy and materials and

messages for iCCM. The plan should also guide reporting and information flow to promote iCCM service demand, utilization, and feedback on iCCM

management and service delivery quality in the country.

g) Supervision and performance q...

📄 **Reference:** Page 48

### 4. HECKS

### HECKS

only meaningful and worthwhile if used for evidence-based decision-making from community to national

levels. To be useful, information must be based on quality data, and it also must be communicated

effectively to policymakers and other interested stakeholders. The iCCM M&E data thus needs to be

manageable and timely, reliable, and specific to the activities in question, and the results need to be well

understood. The key to effective iCCM data use involves linking the data to the...

📄 **Reference:** Page 41

### 5. RINCIPLES

### RINCIPLES

7.1.3 PRINCIPLES

1

iCCM Data is collected based on needs within the general management processes.

2

Work along the iCCM logframe measured by the corresponding indicators

3

Build iCCM M&E into the national HMIS framework so as not to overwhelm providers or make monitoring an additional activity by utilizing existing

touchpoints

4

Minimal tolerance for insufficient data by building quality assurance processes to test the data for quality and giving constant feedback on acce...

📄 **Reference:** Page 31


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 31, Page 41, Page 44, Page 47, Page 48

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 22

**Full query**

> Integrated community case management fever

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.95`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 5: FOREWORD
• WHO Malaria Guidelines (NCBI Bookshelf), Page 5: FOREWORD
• WHO Malaria Guidelines (NCBI Bookshelf), Page 6: ACKNOWLEDGEMENTS
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Integrated community case management fever

### 1. FOREWORD

expanded package to include TB and HIV assessment. This document is to guide policymakers, managers, districts, health workers, communities, NGOs, and all other stakeholders on how to implement integrated community case management (iCCM) of childhood malaria, pneumonia, and diarrheoa to reduce under mortality and take actions to introduce, implement, monitor

and evaluate iCCM at all levels of health services delivery chain. It describes activities

for sensitization and advocacy, capacity build...

📄 **Reference:** Page 5

### 2. FOREWORD

# FOREWORD

FOREWORD

Integrated community case management (iCCM) of childhood infection saves lives in

hard-to-reach communities in Uganda.  The objective of this strategy is to strengthen

iCCM implementation and and set the path to institutionalizing rapid reduction in

under five mortality in the national and district health during 2020 to 2060.  The

Village health teams in remote poor urban and rural communities provide the needed

lifesaving treatments to sick children within 24 hours wi...

📄 **Reference:** Page 5

### 3. ACKNOWLEDGEMENTS

# ACKNOWLEDGEMENTS

ACKNOWLEDGEMENTS

The Ministry of Health acknowledges the efforts of many stakeholders and partners

who supported the development and update of different components of this guideline

for integrated community case management. iCCM is a key strategy to reducing child

mortality, and the iCCM TWG is commended for the successful update of the new

guidelines that build on past experiences in implementing the program in the country.

I acknowledge the following people for their ...

📄 **Reference:** Page 6

### 4. ONTEXT

### ONTEXT

1.1 CONTEXT

Children compose 17.2% of Uganda's population but account for 40% of the disease burden in the country.

Uganda has steadily reduced child mortality rates between 1995 and 2016 from 156 to 64 per 1000 live

births. On average, about 350 children under five years of age lose their lives per day, of which a quarter die

of malaria, pneumonia, and diarrhoea. Annually, these three diseases account for half of all the under 5

OPD attendances1. and together contribute over 17...

📄 **Reference:** Page 8

### 5. Carry out Focus Group Discussion:

### Carry out Focus Group Discussion:

will be held. These will be community lead and in attendance will be the public and service

providers. The fora will be used to give feedback and accountability and develop action plans on

how to bridge gaps within the iCCM program in those respective communities. The communities

will decide who will be responsible for following up the action plans, including the timelines to do

so. On an annual basis, recurring gaps will be picked to inform iCCM planni...

📄 **Reference:** Page 27


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 5, Page 6, Page 8, Page 27

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 23

**Full query**

> Ethics of placebo-controlled malaria trials

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.83`

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 64: Activity 4.2.6 [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 10: S [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 46: SUMMARY OF ROLES AND RESPONSIBILITIES [HIGH FIDELITY]
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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Ethics of placebo-controlled malaria trials

### 1. Activity 4.2.6

### Activity 4.2.6

Activity 4.2.6 Dissemination of

implementation research findings

Number of research dissemination

meetings held

5

Meeting

proceedings

MOH...

📄 **Reference:** Page 64

### 2. S

### S

PACKAGE DELIVERED BY ICCM VHTS

PACKAGES DELIVERED BY ALL VHTS

i. Malaria diagnosis with mRDT; treatment with ACTs;

i.

Home visiting

ii.

Mobilization of communities for utilization of health

services

iii.

Health Promotion and Education

iv.

Community-based case management of common ill-

health conditions

v.

Follow up of the mothers during pregnancy and after

birth and the newborn for provision of advice,

recognition of danger signs, and referral

vi.

Follow up of people who...

📄 **Reference:** Page 10

### 3. SUMMARY OF ROLES AND RESPONSIBILITIES

# SUMMARY OF ROLES AND RESPONSIBILITIES

8 SUMMARY OF ROLES AND RESPONSIBILITIES...

📄 **Reference:** Page 46

### 4. Outcome 3

### Outcome 3

Outcome 3

Increased Knowledge of and Demand for

iCCM

The proportion of caregivers and

community members have positive health

behaviors and practices (e.g., ITN use,

completed referral for pneumonia, hand-

washing, safe disposal of infant fecal

matter, exclusive breastfeeding).

80%

Evaluation

report...

📄 **Reference:** Page 62

### 5. Outcome 2

### Outcome 2

Outcome 2

61...

📄 **Reference:** Page 61


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 10, Page 46, Page 61, Page 62, Page 64

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 24

**Full query**

> Vector control bed nets IRS

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.78`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Monitor, supervise, and evaluate national iCCM
**Step 2:** Ensure medicines and commodity security at all

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 47: Control [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 24: Support Supervision:
• WHO Malaria Guidelines (NCBI Bookshelf), Page 49: EAM
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Monitor, supervise, and evaluate national iCCM
• Ensure medicines and commodity security at all

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Vector control bed nets IRS

### 1. Control

### Control

Quality

Assurance

and Quality

Control

strictly adhered to.

 Government should ensure that policies are

adhered to.

47...

📄 **Reference:** Page 47

### 2. Support Supervision:

### Support Supervision:

to the VHTs will be done immediately after the training on iCCM. Subsequently, VHTs will be supplied

with commodities based on their consumption rate. The health facilities will follow proper inventory

management procedures to replenish medicine stocks to VHTs, including cross-checking VHT registers

and consumption logs to ensure appropriate accountability of the medicines. Health Facilities will also

ensure the availability of drugs and supplies to handle referred ...

📄 **Reference:** Page 24

### 3. EAM

### EAM

quality of iCCM service delivery. Facilitate learning across communities (village to village, Facility to Facility) to promote and scale up best practices in

iCCM

f)

Procurement and Supplies management: iCCM commodities should be integrated into existing district quantification, procurement, supply chain to the

"last mile," inventory control, resupply, and logistics management information system (LMIS). Standard operating procedures and tools should be adhered

to to support sustain...

📄 **Reference:** Page 49

### 4. VHT supervisory visit

## VHT supervisory visit

Annex 4:

VHT supervisory visit

VHTs are volunteers, so supervision should be planned when they are available.   Before a supervisory visit, a supervisor should prepare

to enable him or her to be thorough and helpful.

 Review past performance of the VHT

 Collect appropriate checklists and reporting forms to use during the supervision and the report from

the previous visit.

 Collect supplies, equipment, and/or materials that the VHT needs.

 Know dates of any r...

📄 **Reference:** Page 58

### 5. EVEL ACTIVITIES

### EVEL ACTIVITIES

5.1 NATIONAL LEVEL ACTIVITIES

Form the national iCCM Technical Working Group that will:

a)

Advocate and mobilize resources

b) Sensitize and orient districts and other stakeholders

c)

Develop and monitor implementation TORs for

the iCCM focal persons

d) Design and oversee national iCCM rollout plans

e)

Building initial capacity for district training and

supervision

f)

Monitor, supervise, and evaluate national iCCM

program

g) Utilize iCCM data for decision makin...

📄 **Reference:** Page 12


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 12, Page 24, Page 47, Page 49, Page 58

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 25

**Full query**

> Elimination strategies and surveillance

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.76`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** What are other roles that community-based health workers can play apart from managing the top
**Step 2:** What are the best ways to improve and sustain the performance of VHTs?
**Step 3:** What are the costs and performance of different training methods for (illiterate/literate) VHTs?
**Step 4:** What is the optimal number of VHTs to give near-universal coverage to a given geographic area?
**Step 5:** Which factors reduce attrition?

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

• WHO Malaria Guidelines (NCBI Bookshelf), Page 45: VHTs
• WHO Malaria Guidelines (NCBI Bookshelf), Page 63: Activity 3.1.2. [HIGH FIDELITY]
• WHO Malaria Guidelines (NCBI Bookshelf), Page 12: CTIVITIES

---
**GUARDRAIL WARNINGS:**

• Citation to page 1 not found in knowledge base
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• What are other roles that community-based health workers can play apart from managing the top
• What are the best ways to improve and sustain the performance of VHTs?
• What are the costs and performance of different training methods for (illiterate/literate) VHTs?

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
**WHO guidelines for malaria - 13 August 2025**

**Question:** Elimination strategies and surveillance

### 1. VHTs

### VHTs

A. VHTs

1.

What are other roles that community-based health workers can play apart from managing the top

killers, such as community-based surveillance, immunization, management of cholera, and preparing

families for emergencies/outbreaks?

2.

What are the best ways to improve and sustain the performance of VHTs?

3.

What are the costs and performance of different training methods for (illiterate/literate) VHTs?

4.

What is the optimal number of VHTs to give near-universal covera...

📄 **Reference:** Page 45

### 2. Activity 3.1.2.

### Activity 3.1.2.

Activity 3.1.1. Develop and disseminate an

iCCM communication strategy

Number of approved communication

strategies

1

Approved

communica

tion strategy

MOH,

Partners

To develop a strategy in

year one to be integrated

into the national

communication strategy.

Dissemination to be done

throughout the years

Activity 3.1.2. Print and disseminate

guidelines for sensitization and mobilization

for iCCM at all levels

The number of guidelines disseminated.

Activity

...

📄 **Reference:** Page 63

### 3. CTIVITIES

### CTIVITIES

5.6 VHT LEVEL ACTIVITIES

a)

Home visiting

b) Mobilization of communities for utilization of

f)

Follow up of people who have been discharged

from health facility and those on long term

treatment

g) Distribution of health commodities

h) Community information management

i)

Disease surveillance

health services

c)

Health Promotion and Education

d) Community-based case management of common

ill-health conditions

e)

Follow up of the mothers during pregnancy and

after bi...

📄 **Reference:** Page 12

### 4. Supportive Tool:  iCCM Benchmark tool

### Supportive Tool:  iCCM Benchmark tool

Step 1: Regular meetings of the National iCCM TWG

At the national level, the mandate is to ensure continuous advocacy for increased resources, partners, and

buy-in for iCCM. The national level will spearhead coordination, harmonize advocacy activities, and

disseminate policy guidelines within and outside the sector.  This step is aimed at facilitating the integration

of iCCM services with multiple national strategies, including Child Survival, IMNCI...

📄 **Reference:** Page 13

### 5. Activity 3.1.3.

### Activity 3.1.3.

Activity 3.1.3. Conduct sensitization

meetings for traditional and civic leaders

regarding iCCM

Number of sensitization meetings

conducted

1,920

Activity

reports

MOH,

Partners

20 leaders per district...

📄 **Reference:** Page 63


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 12, Page 13, Page 45, Page 63

---
**🧪 Guardrail Brain Validation:**

**⚠️ Warnings:**
• Citation to page 1 not found in knowledge base

```

---


## Preset: `uganda`

- **Document**: Uganda Clinical Guidelines 2023
- **Queries**: 25

### Summary table

| # | Triage | Guardrail OK | Confidence | VHT chars | Referral chars | Quick chars |
|---|--------|--------------|------------|-----------|----------------|-------------|
| 1 | GREEN | True | 0.84 | 1495 | 380 | 123 |
| 2 | GREEN | True | 0.95 | 1653 | 439 | 123 |
| 3 | GREEN | True | 1.00 | 2234 | 565 | 123 |
| 4 | GREEN | True | 0.89 | 1586 | 404 | 123 |
| 5 | GREEN | True | 0.93 | 1488 | 378 | 123 |
| 6 | GREEN | True | 0.93 | 1717 | 448 | 123 |
| 7 | GREEN | True | 0.79 | 1455 | 380 | 123 |
| 8 | GREEN | True | 0.90 | 1425 | 379 | 123 |
| 9 | GREEN | True | 0.97 | 1586 | 374 | 123 |
| 10 | GREEN | True | 0.94 | 1562 | 388 | 123 |
| 11 | GREEN | True | 0.88 | 1567 | 380 | 123 |
| 12 | GREEN | True | 0.89 | 1395 | 339 | 123 |
| 13 | GREEN | True | 0.91 | 2948 | 438 | 123 |
| 14 | GREEN | True | 0.95 | 1417 | 333 | 123 |
| 15 | GREEN | True | 0.95 | 1641 | 406 | 123 |
| 16 | GREEN | True | 0.68 | 1420 | 377 | 123 |
| 17 | GREEN | True | 0.90 | 1599 | 390 | 123 |
| 18 | GREEN | True | 0.65 | 1590 | 331 | 123 |
| 19 | GREEN | True | 0.87 | 1729 | 484 | 123 |
| 20 | GREEN | True | 0.91 | 1647 | 396 | 123 |
| 21 | GREEN | True | 0.83 | 1529 | 379 | 123 |
| 22 | GREEN | True | 0.81 | 1381 | 297 | 123 |
| 23 | GREEN | True | 0.89 | 1559 | 398 | 123 |
| 24 | GREEN | True | 0.96 | 1647 | 435 | 123 |
| 25 | GREEN | True | 0.92 | 1448 | 350 | 123 |

### Full queries and formatted outputs

#### Query 1

**Full query**

> Integrated management of childhood illness pneumonia classification

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.84`

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

• Uganda Clinical Guidelines 2023, Page 893: Childhood Illness
• Uganda Clinical Guidelines 2023, Page 929: 17.4  INTEGRATED COMMUNITY CASE MANAGEMENT [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 876: Childhood Illness [HIGH FIDELITY]
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

### 1. Childhood Illness

### Childhood Illness

Uganda Clinical Guidelines 2023

CHAPTER 17: Childhood Illness

CLINICAL FEATURES

CLASSIFY AS

MANAGEMENT

No signs of

severe disease

or pneumonia



If wheezing give an inhaled

bronchodilator (salbutamol

inhaler every 3-4 hours as

necessary) for 5 days

Cough or

Cold (No

pneumo­

nia)

Most likely

viral so no

antibiotics

needed



Soothe throat/relieve

cough with safe remedy



If coughing for more

than 14 days or recurrent

wheezing, refer for possible

T...

📄 **Reference:** Page 893

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

📄 **Reference:** Page 929

### 3. Childhood Illness

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

📄 **Reference:** Page 876

### 4. Childhood Illness

### Childhood Illness

Uganda Clinical Guidelines 2023

CHAPTER 17: Childhood Illness

CLINICAL FEATURES

CLASSIFY AS

MANAGEMENT

~

Or very

low

weight

for age



a child aged 6 months

or more...

📄 **Reference:** Page 907

### 5. 17.4  Integrated Community Case Management................................863

### 17.4  Integrated Community Case Management................................863

17.4  Integrated Community Case Management................................863...

📄 **Reference:** Page 16


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 16, Page 876, Page 893, Page 907, Page 929

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 2

**Full query**

> Diarrhea dehydration ORS zinc treatment plan

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.95`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Give zinc for 10 days: Child < 6 months: 10 mg per day;
**Step 2:** If child exclusively breastfed, give ORS or safe
**Step 3:** Give extra fluids: as much as the child will take
**Step 4:** In addition to the usual fluid intake, give ORS after
**Step 5:** Give the mother 2 packets to use at home

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

• Uganda Clinical Guidelines 2023, Page 897: Note: [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 75: Plan A (No dehydration and for prevention) [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 77: Plan C (Severe dehydration) [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Give zinc for 10 days: Child < 6 months: 10 mg per day;
• If child exclusively breastfed, give ORS or safe
• Give extra fluids: as much as the child will take

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

### 1. Note:

### Note:

Note:

 The current recommendation for treatment of diarrhoea is

oral rehydration salts (ORS) and zinc salts (Zn sulphate, Zn

gluconate or Zn acetate).

- Give zinc for 10 days: Child < 6 months: 10 mg per day;

Child > 6 months: 20 mg per day...

📄 **Reference:** Page 897

### 2. Plan A (No dehydration and for prevention)

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

### 3. Plan C (Severe dehydration)

### Plan C (Severe dehydration)

Plan C (Severe dehydration)

TREATMENT

LOC...

📄 **Reference:** Page 77

### 4. ORS

### ORS

Zinc Tablets and

ORS

Diarrhoea

Zinc

< 14 days without

blood

2-6 months: ½ tab once a day

for 10 days

6 months to 5 years: 1 tab

once a day for 10 days ORS

As much as the chid wants but

at least ½ cup after each loose

stool

864...

📄 **Reference:** Page 930

### 5. ORS

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


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 75, Page 77, Page 897, Page 930

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 3

**Full query**

> HIV antiretroviral therapy first-line regimen adults

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `1.00`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** For recipients of care on  NNRTI-based First Line regimen whose VL is not suppressed, switch
**Step 2:** All PLHIV should receive resistance testing to inform the prescription of 2ndand 3rd-line medicines.
**Step 3:** Since all 3rd-line PLHIV will have prior PI Exposure, DRV/r will be taken twice a day.
**Step 4:** For all PLHIV failing first-line ART, optimize the second-line ART using HIVDR test

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

inform the prescription of 2ndand 3rd-line medicines.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**EXACT DOSING (copy from guidelines — do not change numbers):**

### 3.1.5 Recommended First Line Regimens in Adults, Adolescents,

3.1.5 Recommended First Line Regimens in Adults, Adolescents,

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

377

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 272: 3.1.5 Recommended First Line Regimens in Adults, Adolescents, [EXACT DOSING]
• Uganda Clinical Guidelines 2023, Page 443: ment regimen [EXACT DOSING]
• Uganda Clinical Guidelines 2023, Page 290: HIV/AIDS and Sexually Transmitted Infections [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• For recipients of care on  NNRTI-based First Line regimen whose VL is not suppressed, switch
• All PLHIV should receive resistance testing to inform the prescription of 2ndand 3rd-line medicines.
• Since all 3rd-line PLHIV will have prior PI Exposure, DRV/r will be taken twice a day.

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

### 1. 3.1.5 Recommended First Line Regimens in Adults, Adolescents,

### 3.1.5 Recommended First Line Regimens in Adults, Adolescents,

3.1.5 Recommended First Line Regimens in Adults, Adolescents,...

📄 **Reference:** Page 272

### 2. ment regimen

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

377...

📄 **Reference:** Page 443

### 3. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections

•	 For recipients of care on  NNRTI-based First Line regimen whose VL is not suppressed, switch

without a second VL but conduct IAC to improve adherence to new regimen.

•	 All PLHIV should receive resistance testing to inform the prescription of 2ndand 3rd-line medicines.

+ FTC + LPV/r

NOTE: For details

implementat ion

on the third-line

Please see the...

📄 **Reference:** Page 290

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

Citations: Page 268, Page 272, Page 289, Page 290, Page 443

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 4

**Full query**

> Tuberculosis treatment regimen and contact investigation

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.89`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Persons living with HIV
**Step 2:** Child & adult contacts of pulmonary TB patients
**Step 3:** Assess for cough, fever, weight loss and nights
**Step 4:** If any of the TB symptoms are present, do
**Step 5:** evaluation for TB

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

• Uganda Clinical Guidelines 2023, Page 451: 5.3.2.3	 Tuberculosis Preventive Treatment [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 9: Untitled [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 318: 3.1.10.1	 Tuberculosis and HIV Co-Infection
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Persons living with HIV
• Child & adult contacts of pulmonary TB patients
• Assess for cough, fever, weight loss and nights

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

### 1. 5.3.2.3	 Tuberculosis Preventive Treatment

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

📄 **Reference:** Page 451

### 2. Untitled

Uganda Clinical Guidelines 2023

5.3.2.1 Anti-TB Drugs Side Effects..........................................................................381

5.3.2.2 Prevention and Infection Control of TB........................................................384

5.3.2.3 Tuberculosis Preventive Treatment................................................................385

5.3.2.5 TB Preventive Treatment Dosing Chart........................................................386...

📄 **Reference:** Page 9

### 3. 3.1.10.1	 Tuberculosis and HIV Co-Infection

### 3.1.10.1	 Tuberculosis and HIV Co-Infection

3.1.10.1	 Tuberculosis and HIV Co-Infection

Active TB may be present when ART needs to be initiated or it may

develop during treatment.

TB and HIV care for co-infected patients should be provided in an

integrated manner under one roof by one care team (one-stop-shop).

Co-management of TB and HIV is complicated by:

~

Drug interactions between rifampicin and both the NNRTI

and PI classes

~

Immune reconstitution inflammatory syndrome (IRIS)...

📄 **Reference:** Page 318

### 4. 5.3 Tuberculosis (Tb).....................................................................366

### 5.3 Tuberculosis (Tb).....................................................................366

5.3 Tuberculosis (Tb).....................................................................366

5.3.1Definition, Clinical Features and Diagnosis of TB..............................................366

5.3.1.1Tuberculosis in Children and adolescents.......................................................372

5.3.1.2Drug-Resistant TB.........................................................................

📄 **Reference:** Page 8

### 5. Contact tracing

### Contact tracing

Contact tracing

~

Tracing of contacts of TB patients

~

Routine screening of health workers for latent & active TB...

📄 **Reference:** Page 450


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 8, Page 9, Page 318, Page 450, Page 451

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 5

**Full query**

> Malaria uncomplicated case management ACT dosing children

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.93`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Give paracetamol 1 g every 6 hours Child: 10 mg/
**Step 2:** Give diazepam 0.2 mg/kg (max 10 mg) slow IV or

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

• Uganda Clinical Guidelines 2023, Page 235: Management of Malaria [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 235: Treatment of uncomplicated malaria [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 929: 17.4  INTEGRATED COMMUNITY CASE MANAGEMENT [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Give paracetamol 1 g every 6 hours Child: 10 mg/
• Give diazepam 0.2 mg/kg (max 10 mg) slow IV or

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

### 1. Management of Malaria

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

### 2. Treatment of uncomplicated malaria

### Treatment of uncomplicated malaria

Treatment of uncomplicated malaria

The following tables contain dosages for medicines used in treatment of

uncomplicated malaria.

169...

📄 **Reference:** Page 235

### 3. 17.4  INTEGRATED COMMUNITY CASE MANAGEMENT

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

📄 **Reference:** Page 929

### 4. Management of Malaria in Pregnancy

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

706...

📄 **Reference:** Page 772

### 5. 2.5.3.3 Management of Complications of Severe Malaria

### 2.5.3.3 Management of Complications of Severe Malaria

2.5.3.3 Management of Complications of Severe Malaria

Dosage of IM artemether

COMPLICATION

TREATMENT

Hyperpyrexia

Give paracetamol 1 g every 6 hours Child: 10 mg/

kg + tepid sponging + fanning

Convulsions

Give diazepam 0.2 mg/kg (max 10 mg) slow IV or

(in adults) IM or 0.5 mg/kg rectally...

📄 **Reference:** Page 241


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 235, Page 241, Page 772, Page 929

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 6

**Full query**

> Postpartum hemorrhage emergency management oxytocin

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.93`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Resuscitation and management of obstetric haemorrhage and
**Step 2:** Identification and management of underlying causes
**Step 3:** Check uterus to see if contracted f Massage uterus (to
**Step 4:** Start IV fluids (normal saline) using 2 IV lines using
**Step 5:** Give prophylactic antibiotics until delivery to help reduce

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

• Uganda Clinical Guidelines 2023, Page 809: 16.4.6 Postpartum Haemorrhage (PPH) [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 811: Management [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 789: 16.3.6       Antepartum Haemorrhage (APH) – Abruptio Placentae [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Resuscitation and management of obstetric haemorrhage and
• Identification and management of underlying causes
• Check uterus to see if contracted f Massage uterus (to

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

### 1. 16.4.6 Postpartum Haemorrhage (PPH)

### 16.4.6 Postpartum Haemorrhage (PPH)

16.4.6 Postpartum Haemorrhage (PPH)    ICD10 CODE: O72

Vaginal bleeding of more than 500 mL after vaginal delivery or >1000

mL after caesarean section.

743...

📄 **Reference:** Page 809

### 2. Management

### Management

Management

The principles of management include two major components:

1.

Resuscitation and management of obstetric haemorrhage and

possibly hypovolemic shock

2.

Identification and management of underlying causes

TREATMENT

LOC

First aid

HC3



Check uterus to see if contracted f Massage uterus (to

expel clots) f Give oxytocin 10 IU IM or IV slowly Give

tranexamic acid 1gm IV slowly over 10 mins but within

3 hours after delivery of the baby



Empty the bladder



S...

📄 **Reference:** Page 811

### 3. 16.3.6       Antepartum Haemorrhage (APH) – Abruptio Placentae

### 16.3.6       Antepartum Haemorrhage (APH) – Abruptio Placentae

16.3.6       Antepartum Haemorrhage (APH) – Abruptio Placentae...

📄 **Reference:** Page 789

### 4. Postpartum care services

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

📄 **Reference:** Page 827

### 5. and no signs of infection

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

📄 **Reference:** Page 786


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 786, Page 789, Page 809, Page 811, Page 827

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 7

**Full query**

> Family planning contraceptive counseling methods

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.79`

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

counsel the patient and address her concerns appropriately.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 727: 15.2  Overview Of Key Contraceptive Methods [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 726: Family Planning (FP) [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 265: Family planning [HIGH FIDELITY]
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

### 1. 15.2  Overview Of Key Contraceptive Methods

### 15.2  Overview Of Key Contraceptive Methods

15.2  Overview Of Key Contraceptive Methods

The following sections contain an overview of mainstream contraceptive

methods and how to manage side effects

of each (in case they occur). Side effects are one of most common reasons

why women stop using contraception, and the health worker should

be able to counsel the patient and address her concerns appropriately....

📄 **Reference:** Page 727

### 2. Family Planning (FP)

### Family Planning (FP)

Uganda Clinical Guidelines 2023

CHAPTER 15: Family Planning (FP)

Contraceptives

Coc

Pop

Poi

Poim

Cuiud

Peurperal sepsis

Y

Y

Y

Y

N

Age And Pregnancy History (Parity)

Adolescents (menarche

to age < 18 years)

Condition

Y

Y

Y

Y

Y

Nulliparity

Y

Y

Y

Y

Y

Parous

Y

Y

Y

Y

Y

Pregnancy

NA

NA

NA

NA

NA...

📄 **Reference:** Page 726

### 3. Family planning

### Family planning

Family planning

Encourage PLHIV to discuss their

reproductive choices and support

them to adopt those which do not

compromise their health. For women

who choose to conceive, link them

to eMTCT services....

📄 **Reference:** Page 265

### 4. 15.1.10  Summary of Medical Eligibility for Contraceptives

### 15.1.10  Summary of Medical Eligibility for Contraceptives

15.1.10  Summary of Medical Eligibility for Contraceptives

The tables below contain a ummarized version of the medical eligibility

criteria for initiating a patient on contraceptive methods, based on the

MOH (2016) and WHO (2020) Medical Eligibility Criteria for Contracep­

tive Use. It guides family planning providers in recommending safe and

effective contraception methods for women with medical conditions or

medially-relevan...

📄 **Reference:** Page 722

### 5. Family Planning (FP)

### Family Planning (FP)

Uganda Clinical Guidelines 2023

CHAPTER 15: Family Planning (FP)

INSTRUCTIONS

LOC



Supply at least 40 female condoms to each client

per month



Advise client to return for more before they are finished



In case of hypersensitivity, avoid use and change to

another FP method

HC2...

📄 **Reference:** Page 730


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 265, Page 722, Page 726, Page 727, Page 730

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

**Step 1:** Diastolic of 90 mmHg and systolic of 140 mmHg
**Step 2:** Ensure adequate depth of anaesthesia and analgesia

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

• Uganda Clinical Guidelines 2023, Page 378: Management of hypertension [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 372: Prevention [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 1106: Hypertension
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Diastolic of 90 mmHg and systolic of 140 mmHg
• Ensure adequate depth of anaesthesia and analgesia

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

### 1. Management of hypertension

### Management of hypertension

Management of hypertension...

📄 **Reference:** Page 378

### 2. Prevention

### Prevention

Prevention

 Management of risk factors

 Early diagnosis and treatment of the cause (e.g. hypertension)

 Treatment adherence...

📄 **Reference:** Page 372

### 3. Hypertension

### Hypertension

Hypertension

- Diastolic of 90 mmHg and systolic of 140 mmHg

are acceptable

- If

hypertension

not

adequately

controlled,

there is risk of vasoconstriction, hypovolaemia,

exaggerated

vasoactive

response

to

stress

leading to hypo or hypertension, hypertensive

complications during anaesthesia



Control hypertension pre-operatively



Patient should take antihypertensive medicines on schedule

even on the day of operation



General anaesthesia technique is prefe...

📄 **Reference:** Page 1106

### 4. Classify and treat as directed below Check for hypertension

### Classify and treat as directed below Check for hypertension

Classify and treat as directed below Check for hypertension

Blood Pressure



Diastolic



Diastolic



Diastolic

readings

mmHg

mmHg



2 read­

mmHg

on 2



110



<90

ings



90

BP

BP

BP

on

repeat after



Diastolic BP



90 mmHg,...

📄 **Reference:** Page 832

### 5. Chronic Care

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


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 54, Page 372, Page 378, Page 832, Page 1106

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 9

**Full query**

> Diabetes mellitus type 2 glycemic targets

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.97`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Fasting blood sugar <7 mmol/l
**Step 2:** Postprandial sugar <10 mmol/l
**Step 3:** HbA1c <7% (7.5 % for elderly)
**Step 4:** DKA is characterized by ketosis, acidosis, and hyperglycaemia.
**Step 5:** HHS is characterized by hyperglycaemia, severe

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

• Uganda Clinical Guidelines 2023, Page 539: Treatment targets [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 542: glycaemic State (HHS) [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 535: Diabetes Mellitus [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Fasting blood sugar <7 mmol/l
• Postprandial sugar <10 mmol/l
• HbA1c <7% (7.5 % for elderly)

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

### 1. Treatment targets

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

📄 **Reference:** Page 539

### 2. glycaemic State (HHS)

### glycaemic State (HHS)

8.1.4

Diabetic Ketoacidosis (DKA) and Hyperosmolar Hyper­

glycaemic State (HHS)    ICD10 CODE: E10.1 AND E11.0

Acute metabolic complications of diabetes mellitus:

- DKA is characterized by ketosis, acidosis, and hyperglycaemia.

It is more common in type 1 diabetes.

- HHS is characterized by hyperglycaemia, severe

- dehydration and hypovolemia, but no ketosis and acidosis. It

is more common in type 2 diabetes.

476...

📄 **Reference:** Page 542

### 3. Diabetes Mellitus

### Diabetes Mellitus

8.1.3

Diabetes Mellitus

ICD10 CODE: E08-E13

Metabolic disease resulting from insulin insufficiency or ineffectiveness,

due to decreased insulin secretion, or peripheral resistance to the action

of insulin, or a combination of the two....

📄 **Reference:** Page 535

### 4. Note

### Note

Note

 Look out for diabetes mellitus as a consequence of damage

to the pancreas

397...

📄 **Reference:** Page 463

### 5. Caution

### Caution

Caution

 Oral antidiabetic medicines are NOT used in type 1.

Metformin can be used but only under specialist advice

Management of Type 2 Diabetes

TREATMENT

LOC...

📄 **Reference:** Page 541


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 463, Page 535, Page 539, Page 541, Page 542

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 10

**Full query**

> Acute stroke referral and supportive care

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.94`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Sodium bicarbonate 1 mEq/kg bolus followed by
**Step 2:** Refer for ventilatory support if necessary
**Step 3:** Keep baby warm
**Step 4:** Give analgesics prn
**Step 5:** Refer for radiotherapy at national referral hospital for se­

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

• Uganda Clinical Guidelines 2023, Page 1033: Supportive care [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 145: Supportive care [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 183: Supportive care [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Sodium bicarbonate 1 mEq/kg bolus followed by
• Refer for ventilatory support if necessary
• Keep baby warm

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

### 1. Supportive care

### Supportive care

Supportive care...

📄 **Reference:** Page 1033

### 2. Supportive care

### Supportive care

Supportive care

H



Oxygen therapy



IV fluids for hypotension



Charcoal may be useful but only if given within 1 hour

from ingestion and if the patient is not drowsy (risk of

inhalation)



Refer for ventilatory support if necessary



Alkalinisation to increase renal excretion

- Sodium bicarbonate 1 mEq/kg bolus followed by

RR

infusion (specialist only)...

📄 **Reference:** Page 145

### 3. Supportive care

### Supportive care

Supportive care

H



Keep baby warm

117...

📄 **Reference:** Page 183

### 4. Supportive therapy

### Supportive therapy

Supportive therapy



Treat anaphylactic shock (see section 1.1.1)



Treat swelling if significant as necessary, using ice packs

or cold compresses



Give analgesics prn



Reassure and immobilise the patient

HC3...

📄 **Reference:** Page 93

### 5. Referral criteria

### Referral criteria

Referral criteria

~

If pain does not respond to above measures, refer to pal­

liative care specialist

~

Refer for radiotherapy at national referral hospital for se­

vere bone pain not responding to above medications

~

Refer for surgery if the cause of pain is amenable to sur­

gery...

📄 **Reference:** Page 694


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 93, Page 145, Page 183, Page 694, Page 1033

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 11

**Full query**

> Syndromic management sexually transmitted infections

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.88`

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

• Uganda Clinical Guidelines 2023, Page 362: HIV/AIDS and Sexually Transmitted Infections [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 297: HIV/AIDS and Sexually Transmitted Infections [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 361: HIV/AIDS and Sexually Transmitted Infections [HIGH FIDELITY]
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

📄 **Reference:** Page 362

### 2. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections...

📄 **Reference:** Page 297

### 3. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections...

📄 **Reference:** Page 361

### 4. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections...

📄 **Reference:** Page 329

### 5. HIV/AIDS and Sexually Transmitted Infections

### HIV/AIDS and Sexually Transmitted Infections

Uganda Clinical Guidelines 2023

CHAPTER 3: HIV/AIDS and Sexually Transmitted Infections...

📄 **Reference:** Page 284


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 284, Page 297, Page 329, Page 361, Page 362

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 12

**Full query**

> Cervical cancer screening VIA HPV

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.89`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Consider the following if using VIA as a screening method:

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

• Uganda Clinical Guidelines 2023, Page 674: Screening for Cervical Cancer
• Uganda Clinical Guidelines 2023, Page 674: owing if using VIA as a screening method:
• Uganda Clinical Guidelines 2023, Page 679: Cervical Cancer [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Consider the following if using VIA as a screening method:

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

📄 **Reference:** Page 674

### 2. owing if using VIA as a screening method:

### owing if using VIA as a screening method:

Consider the following if using VIA as a screening method:

 Women <25 years of age should be screened only if they are

at high risk for disease: HIV positive, early sexual exposure,

multiple partners, previous abnormal screening results, cervical

intraepithelial neoplasia (CIN)

 VIA is not appropriate for women >50 years

 Screening is advised every 3-5 years in case of normal results,

but after 1 years in case of abnormal results and treat...

📄 **Reference:** Page 674

### 3. Cervical Cancer

### Cervical Cancer

Cervical Cancer...

📄 **Reference:** Page 679

### 4. Oncogenic Infections

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

📄 **Reference:** Page 671

### 5. Screening for Breast Cancer

### Screening for Breast Cancer

Screening for Breast Cancer

Screening / health checkup for breast cancer involves:

Breast Self-Examination (BSE): a simple, quick examination done by the

client herself, aimed at early detection of lumps. Regular (monthly-not

during menstruation, at least seven days after ending the menstruation)

and correct technique of breast examination is important and easy to

teach and administer. Health workers should note that BSE is not a

standard screening test fo...

📄 **Reference:** Page 673


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 671, Page 673, Page 674, Page 679

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 13

**Full query**

> Routine immunization schedule infants Uganda

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.91`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Give this as early as possible in life, preferably at birth
**Step 2:** Do NOT give BCG vaccine to any child with clinical signs
**Step 3:** Check immunization card and classify
**Step 4:** Give all missed

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

**EXACT DOSING (copy from guidelines — do not change numbers):**

### 18.1.1   National Immunization Schedule

18.1.1   National Immunization Schedule

Adapted from the UNEPI/MOH Immunization Schedule, 2022

Vaccine Or

Antigen

Age

Dose & Mode Of

Administration

Mode Of Ad­

ministration

Site Of Ad­

ministration

BCG

At birth

(or first

contact)

0-11 months: 0.05 mL

Above 11

months: 0.1 mL

Intradermally Right Up­

per Arm

Hepatitis

B

At

birth(first

contact

within

the first

7 days of

life)

0.5 ml IM

Intramus­

cular

Outer

aspect of

left thigh

Oral Polio

4 doses: at birth,

6,

10, and

14 weeks

2 drops

Orally

Mouth

Inactivat­

ed Polio

Vaccine

(IPV)

2 doses: At 6 and

14

Weeks of

age

0.5 mL

Intramus­

cular

Outer

aspect of

right thigh; 2.5 cm

away from

PCV site

872

### Routine TT vaccine schedule and the period of protection

Routine TT vaccine schedule and the period of protection

TT DOSE

WHEN GIVEN

DURATION AND

LEVELS

OF PROTECTION

Td1

At first contact with woman of childbearing

age or as early as possible during pregnancy

None

Td2

At least 4 weeks after Td1

3 years; 80% protection

Td3

At least 6 months after Td2

5 years; 95% protection

Td4

At least 1 year after Td3

10 years; 99% protection

Td5

At least 1 year after Td4

30 years; 99% protection

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 939: General principles of routine childhood immunization [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 886: Check immunization card and classify [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 938: 18.1.1   National Immunization Schedule [EXACT DOSING]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Give this as early as possible in life, preferably at birth
• Do NOT give BCG vaccine to any child with clinical signs
• Check immunization card and classify

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

### 1. General principles of routine childhood immunization

### General principles of routine childhood immunization

General principles of routine childhood immunization

~

The aim is to ensure that all target age groups complete

their immunization schedule as above

~

Age for vaccinations: Give each vaccine at the recom­

mended age or if this is not possible, at any first contact

with the child after this age

~

BCG vaccination

- Give this as early as possible in life, preferably at birth

- Do NOT give BCG vaccine to any child with clinical sig...

📄 **Reference:** Page 939

### 2. Check immunization card and classify

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

📄 **Reference:** Page 886

### 3. 18.1.1   National Immunization Schedule

### 18.1.1   National Immunization Schedule

18.1.1   National Immunization Schedule

Adapted from the UNEPI/MOH Immunization Schedule, 2022

Vaccine Or

Antigen

Age

Dose & Mode Of

Administration

Mode Of Ad­

ministration

Site Of Ad­

ministration

BCG

At birth

(or first

contact)

0-11 months: 0.05 mL

Above 11

months: 0.1 mL

Intradermally Right Up­

per Arm

Hepatitis

B

At

birth(first

contact

within

the first

7 days of

life)

0.5 ml IM

Intramus­

cular

Outer

aspect of

left...

📄 **Reference:** Page 938

### 4. Routine TT vaccine schedule and the period of protection

### Routine TT vaccine schedule and the period of protection

Routine TT vaccine schedule and the period of protection

TT DOSE

WHEN GIVEN

DURATION AND

LEVELS

OF PROTECTION

Td1

At first contact with woman of childbearing

age or as early as possible during pregnancy

None

Td2

At least 4 weeks after Td1

3 years; 80% protection

Td3

At least 6 months after Td2

5 years; 95% protection

Td4

At least 1 year after Td3

10 years; 99% protection

Td5

At least 1 year after Td4

30 years; 99%...

📄 **Reference:** Page 946

### 5. 18.1  Routine Childhood Vaccination...............................................872

### 18.1  Routine Childhood Vaccination...............................................872

18 IMMUNIZATION......................................................................872

18.1  Routine Childhood Vaccination...............................................872

18.1.1   National Immunization Schedule.................................................................872

18.1.2  Hepatitis B Vaccination...............................................................................878

18.1.3  ...

📄 **Reference:** Page 16


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 16, Page 886, Page 938, Page 939, Page 946

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 14

**Full query**

> Severe acute malnutrition inpatient management

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.95`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Assess the child’s feeding and counsel the mother on

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

Advise the mother to continue RUTF.

**REMEMBER AS A VHT:**

• Always check for danger signs first
• If you are unsure, it is better to refer
• Record all patients you see
• Keep your VHT kit and referral forms ready

**FROM THE GUIDELINES:**

• Uganda Clinical Guidelines 2023, Page 962: 19.2.2.3  Management of Complicated Severe Acute Malnutri­ [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 960: 19.2.2   Management of Acute Malnutrition in Children [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 960: 19.2.2.1   Management of Moderate Acute Malnutrition [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Assess the child’s feeding and counsel the mother on

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

### 1. 19.2.2.3  Management of Complicated Severe Acute Malnutri­

### 19.2.2.3  Management of Complicated Severe Acute Malnutri­

19.2.2.3  Management of Complicated Severe Acute Malnutri­...

📄 **Reference:** Page 962

### 2. 19.2.2   Management of Acute Malnutrition in Children

### 19.2.2   Management of Acute Malnutrition in Children

19.2.2   Management of Acute Malnutrition in Children...

📄 **Reference:** Page 960

### 3. 19.2.2.1   Management of Moderate Acute Malnutrition

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

📄 **Reference:** Page 960

### 4. If the child has moderate acute malnutrition:

### If the child has moderate acute malnutrition:

If the child has moderate acute malnutrition:



Advise the mother to continue RUTF. Counsel her

to start other foods according to the age appropriate

feeding recommendations (see section 17.3.12.3)



Tell her to return in 14 days. Continue to see the

child every 14 days until the child has no more acute

malnutrition...

📄 **Reference:** Page 962

### 5. Malnutrition

### Malnutrition

Moderate Acute

Malnutrition

~

WFH/L between -3 and -2 z-scores

~

Or MUAC 115 up to 125 mm

~

Or low weight for age...

📄 **Reference:** Page 957


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 957, Page 960, Page 962

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 15

**Full query**

> Tuberculosis preventive therapy isoniazid

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.95`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Give INH for six months to HIV-exposed infant who
**Step 2:** Persons living with HIV
**Step 3:** Child & adult contacts of pulmonary TB patients
**Step 4:** Assess for cough, fever, weight loss and nights
**Step 5:** If any of the TB symptoms are present, do

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

• Uganda Clinical Guidelines 2023, Page 316: TB preventive therapy (TPT) [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 264: TPT (TB Preventive treatment) [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 451: 5.3.2.3	 Tuberculosis Preventive Treatment [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Give INH for six months to HIV-exposed infant who
• Persons living with HIV
• Child & adult contacts of pulmonary TB patients

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

### 1. TB preventive therapy (TPT)

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

### 2. TPT (TB Preventive treatment)

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

📄 **Reference:** Page 451

### 4. Untitled

Uganda Clinical Guidelines 2023

5.3.2.1 Anti-TB Drugs Side Effects..........................................................................381

5.3.2.2 Prevention and Infection Control of TB........................................................384

5.3.2.3 Tuberculosis Preventive Treatment................................................................385

5.3.2.5 TB Preventive Treatment Dosing Chart........................................................386...

📄 **Reference:** Page 9

### 5. Isoniazid

### Isoniazid

Isoniazid

Hepatitis, peripheral neuropathy...

📄 **Reference:** Page 447


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 9, Page 264, Page 316, Page 447, Page 451

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 16

**Full query**

> Depression screening and management primary care

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.68`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Symptom screening or CXR
**Step 2:** All individuals seeking health care should be screened for TB at each

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

• Uganda Clinical Guidelines 2023, Page 590: Depression [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 845: Management [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 580: Depression [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Symptom screening or CXR
• All individuals seeking health care should be screened for TB at each

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

### 1. Depression

### Depression

9.2.2

Depression

ICD10 CODE: F32, F33

A common disorder characterised by low mood, loss of interest and

enjoyment and reduced energy leading to diminished activity and in

severe forms, difficult day-to-day functioning.

524...

📄 **Reference:** Page 590

### 2. Management

### Management

Management

TREATMENT

LOC



Routine assessment for depressive symptoms during post

natal visits or at least once at 6 weeks



Counselling and reassurance at first contact and review

after 2 weeks



If persisting, refer for specialized treatment...

📄 **Reference:** Page 845

### 3. Depression

### Depression

Depression

~

As for depression described above, but with a history of

manic episode

~

High index of suspicion for bipolar in early onset depres­

sion with family history of bipolar illness

~

Differential diagnosis

~

Organic mental states e.g. drug or alcohol intoxication, de­

lirium

~

Chronic Psychosis...

📄 **Reference:** Page 580

### 4. TB screening approaches:

### TB screening approaches:

TB screening approaches:

•	Symptom screening or CXR

•	All individuals seeking health care should be screened for TB at each

visit...

📄 **Reference:** Page 437

### 5. ceive

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

📄 **Reference:** Page 716


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 437, Page 580, Page 590, Page 716, Page 845

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

**Step 1:** Inhaler 2-10 puffs via a large volume spacer
**Step 2:** Give salbutamol
**Step 3:** Assess after 1 month and adjust the dose prn
**Step 4:** Higher dose may be needed initially to gain
**Step 5:** Doubling of the regular dose may be useful to

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

• Uganda Clinical Guidelines 2023, Page 397: Management of asthma attacks [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 402: Chronic Asthma [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 403: STEP 2: Mild persistent asthma [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Inhaler 2-10 puffs via a large volume spacer
• Give salbutamol
• Assess after 1 month and adjust the dose prn

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

### 1. Management of asthma attacks

### Management of asthma attacks

Management of asthma attacks

TREATMENT

LOC

Mild to moderate

HC3



Treat as an out-patient

HC3



Reassure patient; place him in a ½ sitting position

HC3



Give salbutamol

- Inhaler 2-10 puffs via a large volume spacer

331...

📄 **Reference:** Page 397

### 2. Chronic Asthma

### Chronic Asthma

5.1.1.2	 Chronic Asthma...

📄 **Reference:** Page 402

### 3. STEP 2: Mild persistent asthma

### STEP 2: Mild persistent asthma

STEP 2: Mild persistent asthma

~

Symptoms > once/week, but < once/day

~

Night time symptoms > twice/month

~

Symptoms may affect activity

HC3

HC4

Regular inhaled preventer therapy



Salbutamol inhaler 1-2 puffs prn



Plus regular standard-dose inhaled

corticosteroid, e.g. beclomethasone 100-400 micrograms

every 12 hours (children: 100-200 micrograms every 12 hours)

- Assess after 1 month and adjust the dose prn

- Higher dose may be needed initi...

📄 **Reference:** Page 403

### 4. General principles of management

### General principles of management



Chest X-ray



Blood: complete blood count

General principles of management

The four essential components of Asthma Management: Patient edu­

cation, control of asthma triggers, monitoring for changes in symptoms

or lung function, and pharmacologic therapy.

~

Inhalation route is always preferred as it delivers the med­

icines directly to the airways; the dose required is smaller,

the side-effects are reduced



E.g., nebuliser solutions for acute...

📄 **Reference:** Page 395

### 5. General principles of management

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

📄 **Reference:** Page 402


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 395, Page 397, Page 402, Page 403

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 18

**Full query**

> Chronic kidney disease staging referral

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.65`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Refer for specialist management including possible

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

• Uganda Clinical Guidelines 2023, Page 514: Chronic Kidney Disease (CKD) [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 514: Renal and Urinary Diseases [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 243: Criteria for referral to regional/tertiary hospital [HIGH FIDELITY]

---
**GUARDRAIL WARNINGS:**

• Contraindication warning: 'any drugs which may make kidney damage worse e' — patient context 'renal' detected in query
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Refer for specialist management including possible

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

📄 **Reference:** Page 514

### 2. Renal and Urinary Diseases

### Renal and Urinary Diseases

Uganda Clinical Guidelines 2023

CHAPTER 7: Renal and Urinary Diseases

TREATMENT

LOC



Refer for specialist management including possible

dialysis as soon as possible and before the patient’s

condition becomes critical

HC4...

📄 **Reference:** Page 514

### 3. Criteria for referral to regional/tertiary hospital

### Criteria for referral to regional/tertiary hospital

Criteria for referral to regional/tertiary hospital

~

Persistent renal failure needing dialysis

~

Any complication that cannot be managed locally...

📄 **Reference:** Page 243

### 4. 7.1 Renal Diseases........................................................................446

### 7.1 Renal Diseases........................................................................446

7.1 Renal Diseases........................................................................446

7.1.1 Acute Renal Failure........................................................................................446

7.1.2 Chronic Kidney Disease (CKD)........................................................................448

7.1.3 Use of Drugs in Renal Failure.............................................

📄 **Reference:** Page 10

### 5. Chronic stage

### Chronic stage

Chronic stage



Encourage active use of the limb to restore muscle

function/physiotherapy



In event of severe contractures, refer for corrective

surgery...

📄 **Reference:** Page 204


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 10, Page 204, Page 243, Page 514

---
**🧪 Guardrail Brain Validation:**

**⚠️ Warnings:**
• Contraindication warning: 'any drugs which may make kidney damage worse e' — patient context 'renal' detected in query

```

---

#### Query 19

**Full query**

> Exclusive breastfeeding six months

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.87`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Counsel and support all mothers to initiate breastfeeding within an
**Step 2:** Teach mother correct positioning and attachment for breastfeeding,
**Step 3:** Counsel and support parents to introduce adequate, safe, and ap­
**Step 4:** A good diet should be adequate in quantity and include an energy-rich
**Step 5:** Pregnant women and lactating mothers should consume adequate

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

• Uganda Clinical Guidelines 2023, Page 950: 19.1.1  Infant and Young Child Feeding (IYCF)
• Uganda Clinical Guidelines 2023, Page 822: If breastfeeding difficult: [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 730: Indications [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Counsel and support all mothers to initiate breastfeeding within an
• Teach mother correct positioning and attachment for breastfeeding,
• Counsel and support parents to introduce adequate, safe, and ap­

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

### 1. 19.1.1  Infant and Young Child Feeding (IYCF)

### 19.1.1  Infant and Young Child Feeding (IYCF)

19.1.1  Infant and Young Child Feeding (IYCF)

1.	 Counsel and support all mothers to initiate breastfeeding within an

hour of delivery and exclusively breastfeed their infants for the first

six months of life, unless medically contraindicated.

2.	 Teach mother correct positioning and attachment for breastfeeding,

how to express and store breast milk hygienically, and how to feed

the child by a cup.

3.	 Counsel and support parents to intro...

📄 **Reference:** Page 950

### 2. If breastfeeding difficult:

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

756...

📄 **Reference:** Page 822

### 3. Indications

### Indications

Indications

~

Women <35 years needing highly effective FP method

~

Non-breastfeeding clients, or breastfeeding clients after 6

months postpartum

~

Clients with dysmenorrhoea

~

Clients with heavy periods or ovulation pain

~

Clients concerned by irregular menstrual cycles...

📄 **Reference:** Page 730

### 4. Counselling on infant feeding choice

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

### 5. Breastfeeding

### Breastfeeding

Breastfeeding...

📄 **Reference:** Page 927


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 317, Page 730, Page 822, Page 927, Page 950

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 20

**Full query**

> Pre-eclampsia severe features magnesium sulfate

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.91`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Draw 8 mL of a 50% MgSO4 and add 12 mL
**Step 2:** Give the solution as a slow IV bolus over 20
**Step 3:** minutes (the 20-20-20 rule)
**Step 4:** Give IV fluids (Normal saline) very slowly (1 L in 6-8
**Step 5:** Give IV loading dose of magnesium sulphate injection

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

• Uganda Clinical Guidelines 2023, Page 792: Clinical features of severe pre-eclampsia [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 794: Mild to moderate pre-eclampsia [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 792: 16.3.7      Pre-Eclampsia [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Draw 8 mL of a 50% MgSO4 and add 12 mL
• Give the solution as a slow IV bolus over 20
• minutes (the 20-20-20 rule)

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

726...

📄 **Reference:** Page 792

### 2. Mild to moderate pre-eclampsia

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

📄 **Reference:** Page 794

### 3. 16.3.7      Pre-Eclampsia

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

📄 **Reference:** Page 792

### 4. Deliver baby

### Deliver baby

Deliver baby

H



Women with severe pre-eclampsia should be delivered

urgently (vaginally or C/S) regardless of gestational age

in the following situations:

- Non-reassuring foetal heart

- Ruptured membranes

- Uncontrolled BP

- Oligohydramnious

- Features of IUGR

- Oliguria of <500 mL/24 hours

- Pulmonary Oedema...

📄 **Reference:** Page 795

### 5. Obstetric Conditions

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

📄 **Reference:** Page 832


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 792, Page 794, Page 795, Page 832

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 21

**Full query**

> Sepsis empirical antibiotics adults

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.83`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Give IV antibiotics cef­
**Step 2:** Refer to hospital for
**Step 3:** Moderate to severe wounds with extensive tissue
**Step 4:** Very contaminated wounds
**Step 5:** Deep puncture wounds (especially by cats)

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

• Uganda Clinical Guidelines 2023, Page 782: Post-abortal Sepsis [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 789: Newborn [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 93: Antibiotics [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Give IV antibiotics cef­
• Refer to hospital for
• Moderate to severe wounds with extensive tissue

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

### 1. Post-abortal Sepsis

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

📄 **Reference:** Page 782

### 2. Newborn

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

📄 **Reference:** Page 789

### 3. Antibiotics

### Antibiotics

Antibiotics



Give only for infected or high-risk wounds including:

- Moderate to severe wounds with extensive tissue

- damage

- Very contaminated wounds

- Deep puncture wounds (especially by cats)

- Wounds on hands, feet, genitalia or face

- Wounds with underlying structures involved

- Wounds in immunocompromised patients



See next sections on wound management, human and

animal bites for more details...

📄 **Reference:** Page 93

### 4. 1. At Emergency Unit

### 1. At Emergency Unit

1. At Emergency Unit

 Early recognition and resuscitation with iv crystalloids Or Blood

 Empirical Broad spectrum antibiotics Treatment:

 Early and adequate broad-spectrum antibiotics

 Intravenous access. Administer 30ml/kg of crystalloids. A large

bore cannula, in an adult (gauge 16) is preferred.

 Urinary catheterization: UOP in an adult is 0.5ml/kg/hr or

more, an equivalent of 30-50mls/hr.

 Transfer for management to ICU if not responding to

resuscitat...

📄 **Reference:** Page 184

### 5. Management

### Management

Management

TREATMENT

LOC

Bed rest

Treat complications e.g. heart failure Initial empirical

antibiotic therapy

H

Benzylpenicillin 5 MU IV every 6 hours for 4 weeks

Child: Benzylpenicillin 50,000 IU/kg every 6 hours for

4 weeks

Plus gentamicin 1 mg/kg IV every 8 hours for 2 weeks

If staphylococcus suspected, (acute onset) add:

Cloxacillin IV 3 g every 6 hours

Child: 50 mg/kg every 6 hours for 4 weeks

If MRSA (Multi-Resistant Staphylococcus aureus)

RR

Vancomycin 500 ...

📄 **Reference:** Page 369


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 93, Page 184, Page 369, Page 782, Page 789

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 22

**Full query**

> Rabies post-exposure prophylaxis dog bite

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.81`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Do not vaccinate

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

• Uganda Clinical Guidelines 2023, Page 204: 2.3.5 Rabies [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 205: Caution: the patient may bite [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 335: 3.1.11.2 Pre-Exposure Prophylaxis (PrEP) [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Do not vaccinate

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

### 1. 2.3.5 Rabies

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

### 2. Caution: the patient may bite

### Caution: the patient may bite

Caution: the patient may bite



Counsel caregivers on rabies and consequences

139...

📄 **Reference:** Page 205

### 3. 3.1.11.2 Pre-Exposure Prophylaxis (PrEP)

### 3.1.11.2 Pre-Exposure Prophylaxis (PrEP)

3.1.11.2 Pre-Exposure Prophylaxis (PrEP)...

📄 **Reference:** Page 335

### 4. Recommendations for Rabies Vaccination/Serum

### Recommendations for Rabies Vaccination/Serum

Recommendations for Rabies Vaccination/Serum

Condition Of Animal

Nature Of

Exposure

At Time Of

Exposure

10 Days

Later

Recommended

Action

Saliva in contact

with skin but no

skin lesion

Healthy

Healthy

Do not vaccinate

Rabid

Vaccinate

Suspect/

Unknown

Healthy

Do not vaccinate

Rabid

Vaccinate

Unknown

Vaccinate

Saliva in

contact with

skin that has

lesions, minor

bites on trunk

or proximal

limbs

Healthy

Healthy

Do no...

📄 **Reference:** Page 104

### 5. References

### References

References

Ministry of Health Uganda, National Tuberculosis and Leprosy Pro­

gramme, 2016. Tuberculosis and Leprosy Manual, 3rd Edition

Ministry of Health Uganda, Makerere Palliative Care Unit, 2014.

Palliative Care Guidelines

World Health Organisation, 2010. WHO guide for Rabies Pre and

Post-Exposure Prophylaxis in Humans. http://www. who.int/rabies/

PEP_prophylaxis_guidelines_June10.pdf Accessed on 25/11/2016

Ministry of Health Uganda, 2013. Uganda National Infection Pr...

📄 **Reference:** Page 1154


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 104, Page 204, Page 205, Page 335, Page 1154

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 23

**Full query**

> Burns initial wound care and referral

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.89`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Give IV fluid replacement in a total volume per 24 hours
**Step 2:** Refer for admission
**Step 3:** Monitor vital signs and urine output
**Step 4:** Stop the burning process and move the patient to safety

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

• Uganda Clinical Guidelines 2023, Page 116: Severe burns
• Uganda Clinical Guidelines 2023, Page 114: Mild/moderate burns – First aid [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 112: 2nd Degree burns or Partial thickness burns [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Give IV fluid replacement in a total volume per 24 hours
• Refer for admission
• Monitor vital signs and urine output

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

### 1. Severe burns

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

### 2. Mild/moderate burns – First aid

### Mild/moderate burns – First aid

Mild/moderate burns – First aid

HC1



Stop the burning process and move the patient to safety



Roll on the ground if clothing is on fire

48...

📄 **Reference:** Page 114

### 3. 2nd Degree burns or Partial thickness burns

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

### 4. Burns

### Burns

Burns



Reassurance that healing will occur without scarring



Topical anaesthetic lidocaine 2% may help...

📄 **Reference:** Page 1097

### 5. 4th Degree burns

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


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 112, Page 114, Page 116, Page 1097

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 24

**Full query**

> Snake bite envenomation hospital referral

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.96`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Swelling of hand or foot (site of most bites) within 1 hour of
**Step 2:** Swelling of elbow or knee within 3 hours of bite
**Step 3:** Swelling of groin or chest at any time
**Step 4:** Significant swelling of head or neck
**Step 5:** Check package insert for IV dosage details. Ensure the

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

• Uganda Clinical Guidelines 2023, Page 94: 1.2.1.1  Snakebites [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 97: Criteria for referral for administration of antivenom
• Uganda Clinical Guidelines 2023, Page 96: without envenomation [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Swelling of hand or foot (site of most bites) within 1 hour of
• Swelling of elbow or knee within 3 hours of bite
• Swelling of groin or chest at any time

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

### 1. 1.2.1.1  Snakebites

### 1.2.1.1  Snakebites

1.2.1.1  Snakebites

Snakebites can cause both local and systemic effects. Non-venomous

snakes cause local effects (swelling, redness, laceration) and venomous

snakes cause both local and systemic effects due to envenomation.  Over

70% of snakes in Uganda are non-venomous and most bites are from

non-venomous snakes. Of the venomous snakes, more than 50% of

bites are “dry” i.e. no envenomation occurs. In the event that venom is

injected, the effect of the venom depe...

📄 **Reference:** Page 94

### 2. Criteria for referral for administration of antivenom

### Criteria for referral for administration of antivenom

Criteria for referral for administration of antivenom

~

Signs of systemic envenoming (paralysis, respiratory dif­

ficulty, bleeding)

~

Spreading local damage:

- Swelling of hand or foot (site of most bites) within 1 hour of

bite

- Swelling of elbow or knee within 3 hours of bite

- Swelling of groin or chest at any time

- Significant swelling of head or neck



Antivenom sera polyvalent (Africa)

- Check package insert for IV d...

📄 **Reference:** Page 97

### 3. without envenomation

### without envenomation

If no signs and symptoms for 6-8 hours: most likely bite

without envenomation

~

Observation for 12-24 hours recommended

~

Tetanus toxoid (TT) IM 0.5 ml if not previously

immunised in the last 10 years...

📄 **Reference:** Page 96

### 4. Emergencies and Trauma

### Emergencies and Trauma

Uganda Clinical Guidelines 2023

CHAPTER 1: Emergencies and Trauma

Battersby’s green snake (Philothamnus battersbyi)  Olive House Snake (Lycodonomorphis inornatus)...

📄 **Reference:** Page 99

### 5. Caution: the patient may bite

### Caution: the patient may bite

Caution: the patient may bite



Counsel caregivers on rabies and consequences

139...

📄 **Reference:** Page 205


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 94, Page 96, Page 97, Page 99, Page 205

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---

#### Query 25

**Full query**

> Neonatal sepsis danger signs referral

**Metrics:** Triage `GREEN` | Guardrail OK `True` | Confidence `0.92`

#### VHT standard (`vht_response`)

```
**QUICK SUMMARY: GREEN (Manage at Community Level)**

• What I see: Routine evidence retrieval from national guidelines
• What to do: Follow advice below, monitor for changes
• What NOT to do: Do NOT give medicine at home for danger signs

**WHAT TO DO (step by step):**

**Step 1:** Give ampicillin 50 mg/kg IM
**Step 2:** Refer baby to hospital
**Step 3:** Keep baby warm

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

• Uganda Clinical Guidelines 2023, Page 789: Newborn [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 183: 2.1.7.1 Neonatal Septicaemia [HIGH FIDELITY]
• Uganda Clinical Guidelines 2023, Page 859: 17.1.1  Newborn Examination/Danger Signs [HIGH FIDELITY]
```

#### Referral note (`referral_note`)

```
**VHT REFERRAL NOTE**

**Triage:** 🟢 GREEN (Manage at Community Level)
**Reason:** Routine evidence retrieval from national guidelines

**Actions taken:**
• Give ampicillin 50 mg/kg IM
• Refer baby to hospital
• Keep baby warm

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

📄 **Reference:** Page 789

### 2. 2.1.7.1 Neonatal Septicaemia

### 2.1.7.1 Neonatal Septicaemia

2.1.7.1 Neonatal Septicaemia

Organisms causing neonatal septicemia are similar to the ones causing

neonatal pneumonia and meningitis. Refer to hospital after pre-referral

dose of antibiotics....

📄 **Reference:** Page 183

### 3. 17.1.1  Newborn Examination/Danger Signs

### 17.1.1  Newborn Examination/Danger Signs

17.1.1  Newborn Examination/Danger Signs

Use the following procedures to examine all newborn babies after delivery,

before discharge or if baby is seen as an outpatient for routine, FOLLOW

UP, or sick newborn visit during first week of life....

📄 **Reference:** Page 859

### 4. Danger signs

### Danger signs

Danger signs

Sign Or Symptom

Possible Cause

Recent trauma to the

head

Intracranial bleeding

Head injury

High fever

Malaria Meningitis

Other infections

Acute onset, severe

Intracranial bleeding

Chronic worsening

headache

Tumours, hypertension

Altered consciousness

and/or focal neurolog­

ical symptoms and/or

seizure

Tumour, intracranial bleeding, intracranial

infection

495...

📄 **Reference:** Page 561

### 5. If danger signs present, treat as below

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

📄 **Reference:** Page 860


---

Triage Level: GREEN (evidence retrieval summary — not a substitute for bedside assessment; follow local protocols)

Immediate Actions: Review the guideline excerpts above; align actions with national/WHO guidance and qualified supervision.

Next Steps / Monitoring: Consult the full source guideline or a clinician for patient-specific decisions.

When to Refer: Per excerpts and national guidance; seek urgent care if danger signs, severe disease, or instability is suspected.

Citations: Page 183, Page 561, Page 789, Page 859, Page 860

---
**🧪 Guardrail Brain Validation:** ✅ Passed

```

---


## Summary

- **All guardrails passed**: True
