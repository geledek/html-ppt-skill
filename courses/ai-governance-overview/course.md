---
title: AI Governance Overview
series: ai-for-business-leaders

template: course
theme: corporate-clean
themes: corporate-clean,minimal-white,swiss-grid,academic-paper,course-warm
lang: en
delivery: recorded     # presenter-led | self-paced | recorded  (gate 1)
rate: 130          # spoken words per minute, measured for this narrator; timings below follow it
duration: 30       # minutes
accepted_hash:     # set at gate 3; a mismatch means index.html has diverged
---

# AI Governance Overview

## Audience & outcomes

**Audience:** executives and senior decision-makers in Singapore, across sectors.
No legal or technical background is assumed. Financial services provides a
worked sector example, rather than defining the audience.

**Purpose:** an overview of the concept, scope and components of organisational
AI governance, supported by cases and an implementation roadmap.

**Coverage:** selected international approaches, with Singapore, the EU and the
UK examined together. This is not a comprehensive survey of every country's law.

**Delivery:** recorded, 30 minutes. Narration supplies the voiceover; slides keep
definitions, explanations, case backgrounds and decisions visible. They should
make sense as learning aids without reproducing every spoken sentence.

After the course, learners should be able to:

1. Explain what an AI system is and what organisational AI governance covers.
2. Identify governance components, responsibilities and lifecycle activities.
3. Distinguish applicable law, supervisory expectations and voluntary frameworks.
4. Identify a governance failure in a case and select a suitable control.
5. Assess a deployment proposal and identify the next implementation actions.

The final slide is the implementation roadmap. The opening chatbot is a clearly
labelled hypothetical example, returned to with a documented decision.

**Revision authority:** Ray requested implementation of steps 1–3 on 12 September
2026 after committing baseline `65413f3`. The proposed 30-slide revision brief is
the working specification. This authorises drafting the outline, narration and
Gate 2 sample; it does not record acceptance of the resulting artifacts.

## Research Brief

This is the active, bounded source set for the revision. The broader historical
research is preserved in Git at `65413f3`; it is not the authority for new copy.
A source's description below limits the claim that may be taught. Legal outcomes,
company reports, recommendations and hypothetical examples remain distinct.

### R00 · Illustrations and teaching synthesis

The retailer, insurance and complaints scenarios are hypothetical. The six-component
model, role table, decision record and roadmap are course teaching syntheses based
on R02–R05, not quotations or mandatory universal sequences. Their recommended
controls must not be attributed to a court or regulator as case findings.

### R01 · AI-system definition

OECD: machine-based inference produces outputs that may influence environments;
autonomy and post-deployment adaptiveness vary. Use a labelled paraphrase, with the
organisation's full name. Do not claim the date/history is the definition.
[OECD explanatory memorandum, 2024](https://www.oecd.org/en/publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_623da898-en.html).
Status: primary source checked in the preceding review.

### R02 · NIST AI RMF

The voluntary AI Risk Management Framework 1.0 uses GOVERN, MAP, MEASURE and
MANAGE. GOVERN supports the other functions across the lifecycle. The course's
six-component synthesis is not a NIST enumeration.
[NIST framework](https://www.nist.gov/itl/ai-risk-management-framework),
[AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/),
[AI RMF 1.0 PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf).
Status: primary sources checked in the preceding review.

### R03 · ISO/IEC 42001:2023

A management-system standard for responsible development, provision or use of AI,
including policies, objectives and processes. Distinguish adopting management
practices from obtaining certification. No certification-adoption statistic is used.
[ISO standard overview](https://www.iso.org/standard/42001).
Status: public primary overview checked; no claim depends on unseen paywalled clauses.

### R04 · Singapore Model AI Governance Framework

The second edition (2020) is voluntary and addresses internal governance, human
involvement, operations management and stakeholder communication. It does not
replace applicable law. Keep the specific framework named.
[IMDA framework PDF](https://www.imda.gov.sg/-/media/imda/files/infocomm-media-landscape/sg-digital/tech-pillars/artificial-intelligence/second-edition-of-the-model-ai-governance-framework.pdf),
[Singapore government background](https://www.mddi.gov.sg/files/Press%20Releases%202022/annex%20b%20%20background%20on%20singapores%20ai%20governance%20work.pdf),
[Australian government comparison](https://www.industry.gov.au/news/australia-and-singapore-show-compatibility-between-ai-governance-frameworks).
Status: baseline source text plus government search evidence; direct IMDA PDF refresh
was challenged. Voluntary status is corroborated by the government comparison.

### R05 · PDPA obligations

PDPC describes accountability, notification, purpose limitation, protection,
retention and other obligations, with scope and exceptions. The quiz expressly
assumes notification applies, so its answer does not invent missing legal facts.
[PDPC obligations](https://www.pdpc.gov.sg/overview-of-pdpa/the-legislation/personal-data-protection-act/data-protection-obligations).
Status: primary source checked 12 September 2026. Do not present all obligations
as exception-free or the data-portability provision as already effective.

### R06 · UK financial-services survey

The 2024 BoE/FCA survey reports 75% adoption among responding firms, 46% partial
understanding and a third of use cases implemented by third parties. These are
sector-specific responses, not a global survey or evidence about launch votes.
[Bank of England/FCA, 21 November 2024](https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024).
Status: primary source checked in the preceding review; denominators preserved.

### R07 · EU components and territorial scope

The AI Act addresses prohibited practices, high-risk uses, general-purpose AI and
specified transparency duties. Categories can overlap. Article 2 includes certain
third-country providers/deployers where outputs are used in the Union; it is not
an unconditional rule that every overseas chatbot is covered.
[Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai),
[AI Act text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng).
Status: Commission primary explanation checked in the preceding review. Keep the
sample at overview level; no unsupported fine calculation or full scope opinion.

### R08 · EU application dates

Prohibitions: 2 February 2025; GPAI provisions: 2 August 2025; general application
including Article 50: 2 August 2026, subject to transitional provisions. The July
2026 amendment sets Annex III high-risk requirements at 2 December 2027 and
Annex I product-related high-risk requirements at 2 August 2028. Do not describe
future application as a law not yet enacted, or treat this as every exception.
[Commission July 2026 update](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force),
[Official application timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline).
Status: primary sources checked in the preceding review, dated 12 September 2026.

### R09 · UK policy framework

The 2023 white paper describes a context-specific, regulator-led approach and five
policy principles. Those principles are not themselves five new statutory duties.
[UK white paper](https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper).
Status: primary source checked 12 September 2026. Date the policy and use current
FCA material for the sector example; omit speculative institutional histories.

### R10 · Legal effect of supervisory instruments

Binding requirements and non-binding guidance must be distinguished. Guidance
can explain existing law or inform supervisory assessment; the legal basis and
instrument determine consequences. The baseline MAS extract distinguishes
non-binding guidelines from civil penalties and describes supervisory assessment.
[MAS instrument hierarchy](https://www.mas.gov.sg/regulation/mas-supervisory-approach-and-regulatory-instruments).
Status: primary refresh returns maintenance; baseline extract retained with this
limitation. The sample uses bounded distinctions, not an asserted fine, licence
outcome or unverified quotation from the March 2026 draft. Recheck before release.

### R11 · FCA approach

FCA describes reliance on existing frameworks and identifies Consumer Duty and
senior-management accountability as relevant to AI. Do not apply these UK rules
to an unspecified Singapore bank or assign every AI use automatically to one SMF.
[FCA approach, updated 13 February 2026](https://www.fca.org.uk/firms/innovation/ai-approach).
Status: primary source checked 12 September 2026.

### R12 · UK financial-services inquiry

The Treasury Committee describes regulators' reliance on existing frameworks,
while also reporting concerns and recommending clearer guidance. Do not teach
its isolated quote as proof that governance questions have all been resolved.
[Treasury Committee report, 20 January 2026](https://publications.parliament.uk/pa/cm5901/cmselect/cmtreasy/684/report.html).
Status: primary source checked. Report publication date is not assumed to be the
oral-evidence date. Narration uses a paraphrase of the regulatory explanation.

### R13 · Foodinho, 2024

The Italian authority imposed a €5 million penalty involving unlawful processing
of riders' data. Its notice describes block/deactivation messages that did not
inform riders about contesting the decision and requesting account restoration.
Multiple infringements were involved. Distinguish this from the 2021 €2.6 million
case. The Dutch and Robodebt cases do not establish an identical finding.
[Garante notice](https://www.garanteprivacy.it/home/docweb/-/docweb-display/print/10074840),
[Decision of 13 November 2024](https://garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/10074601).
Status: primary sources checked in the preceding review.

### R14 · HSBC, Singapore

The application was in 2018; the review application was in 2020; the decision was
10 March 2021. Specified evaluative opinion data could be withheld. Paragraph 19
separately commends the bank's disclosure of its policies and practices.
Do not claim the disclosures won the legal issue, accelerated the decision or
certified the bank's entire governance programme.
[PDPC decision, paragraphs 1–4 and 17–19](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/commissions-decisions/decision--hsbc-bank-singapore-limited--10032021.pdf).
Status: primary decision checked in the preceding review. Sample excerpt is short
and verbatim; background, outcome and teaching interpretation are separated.

### R15 · Air Canada

Moffatt v Air Canada, 2024 BCCRT 149, concerns misleading bereavement-fare
information supplied by a chatbot. The tribunal held the airline responsible in
that case. No claim is made that the chatbot was removed or that the case creates
an unlimited worldwide liability rule.
[CRT decision](https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do),
[CanLII copy](https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html).
Status: source and excerpt inherited from the baseline; both direct refreshes were
blocked. Amount and long quotation omitted. Recheck source before the full-deck
release. This case is not in the Gate 2 sample.

### R16 · Zillow Offers

Zillow's November 2021 filing reports a US$304.4 million inventory write-down and
cites pricing unpredictability, capacity and other operational challenges in the
wind-down decision. Do not describe this as proof that one algorithm caused the
entire failure, or claim there was no lawsuit or regulator anywhere in the history.
[Zillow Form 8-K, 2 November 2021, Item 2.05](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm).
Status: primary filing checked 12 September 2026.

### R17 · MAS FEAT

Fairness, Ethics, Accountability and Transparency principles were first published
in 2018 and are advisory. The narration does not quote an unverified provision.
[MAS FEAT document, updated 7 February 2019](https://www.mas.gov.sg/-/media/MAS/News-and-Publications/Monographs-and-Information-Papers/FEAT-Principles-Updated-7-Feb-19.pdf),
[Singapore government-hosted MAS speech, 9 October 2025](https://www.sgpc.gov.sg/api/file/getfile/Speech%20by%20Minister%20Chee%20Hong%20Tat%20at%20the%20IBF%20Distinction%20Evening.pdf?path=%2Fsgpcmedia%2Fmedia_releases%2Fmas%2Fspeech%2FS-20251009-1%2Fattachment%2FSpeech+by+Minister+Chee+Hong+Tat+at+the+IBF+Distinction+Evening.pdf).
Status: baseline document; history corroborated by official speech search evidence.
Direct MAS document refresh blocked; recheck before release.

### R18 · MAS AI Risk Management consultation

The November 2025 consultation proposed an AI inventory and lifecycle risk
management. Section 3.4 is a proposal, not presented as an issued requirement.
[MAS consultation](https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management),
[Consultation PDF](https://www.mas.gov.sg/-/media/mas-media-library/publications/consultations/bd/2025/final_consultation_paper_on_guidelines_on_ai_risk_management_forrelease.pdf).
Status: baseline source; MAS refresh returns maintenance. Current issuance status
not established. Therefore removed the old categorical “not issued” statement
and any claim that a transition clock has or has not begun.

### R19 · Agentic human oversight

The supplied Singapore government statement recommends human review for
high-stakes or irreversible actions. Preserve both conditions and advisory force.
[MDDI statement, 6 May 2026](https://www.mddi.gov.sg/newsroom/mddi-s-response-to-pq-on-ensuring-meaningful-human-accountability-for-public-facing-autonomous-ai-agents-and-pathways-to-mandatory-governance-in-high-risk-sectors/).
Status: inherited bounded source; no new quotation. Human oversight is also
supported as recommended practice by R02. This source is outside the sample.

### R20 · Singapore AI adoption (economy-wide)

Non-SME AI adoption rose from 44.0% (2023) to **62.5%** (2024); SME adoption more
than tripled from 4.2% to **14.5%**, driven by micro and small SMEs adopting
off-the-shelf generative AI tools.
[IMDA, Singapore Digital Economy Report 2025](https://www.imda.gov.sg/assets/e77d879a-6b39-4de4-b024-5e0c6da0eff3.pdf), published 6 October 2025 (data year 2024);
restated by MDDI, 21 May 2026.
⚠️ Economy-wide, not financial services. Same data year as the UK survey.
**No Singapore source publishes a percentage for board oversight of AI or for
"partial understanding".** That absence is a finding: label the UK figures as UK,
2024, financial services rather than substituting something weaker.

### R21 · MAS on banks' AI, qualitative only

MAS reports its supervisory findings qualitatively, never as survey percentages.
> "use of Generative AI in banks appears to still be at an early stage"
> "Generative AI used by banks were pre-dominantly based on pre-trained models
> from external providers. As disclosure standards relating to such AI are still
> evolving globally, banks may lack full access to essential risk management
> information"
[MAS Information Paper on AI Model Risk Management](https://www.mas.gov.sg/publications/monographs-or-information-paper/2024/artificial-intelligence-model-risk-management), 5 December 2024.

### R22 · MAS AI Risk Management Toolkit

> "MAS today announced the successful conclusion of phase two of Project
> MindForge, which culminates in the publication of an Artificial Intelligence
> (AI) Risk Management Toolkit for the financial services sector… developed
> collaboratively by a consortium of 24 leading banks, insurance companies,
> capital market firms, and other industry partners"
20 March 2026. Binding guidelines remain pending:
> "MAS is presently reviewing responses to an earlier public consultation on a set
> of Guidelines on AI Risk Management."
https://www.mas.gov.sg/news/media-releases/2026/mas-partners-industry-to-develop-ai-risk-management-toolkit-for-the-financial-sector

### R23 · UK AI Risk Management Toolkit

Voluntary guidance, **8 September 2026**, gov.uk. Helps teams "understand, assess
and manage risks when designing, procuring or delivering AI products". HTML
guidance plus a risk workbook.
https://www.gov.uk/government/publications/ai-risk-management-toolkit
⚠️ The page still attributes it to DSIT, which was abolished in July 2026. Could
not establish whether that is a stale organisation tag or a legacy badge.
**Cite it as "gov.uk, 8 September 2026" and name no department.**

### R24 · Malaysia — no binding AI law as at 13 September 2026

Three distinct things, three statuses:
- **AIGE**, National Guidelines on AI Governance and Ethics, MOSTI, 20 Sep 2024.
  Voluntary. > "The aspiration for these National Guidelines is for the voluntary adoption"
  https://mastic.mosti.gov.my/storage/2024/09/THE-NATIONAL-GUIDELINES-ON-AI-GOVERNANCE-ETHICS.pdf
- **AI Governance Bill** — public consultation 10 Jul – 1 Aug 2026, stage
  "Pre-drafting". https://upc.mpc.gov.my/view-consultation/264
- **10 Sep 2026**: the Digital Minister said the draft is complete and will go to
  Cabinet, with tabling targeted "this quarter or in the first quarter of next
  year". ⚠️ Secondary source (Malay Mail). Flag as reported, not primary.

### R25 · Japan — enacted, but no penalties

Act on Promotion of Research and Development and Utilization of AI-Related
Technologies, passed 28 May 2025; a full-text scan returns zero occurrences of
罰則 / 罰金 / 懲役. Basic AI Plan adopted by Cabinet 23 Dec 2025.
https://laws.e-gov.go.jp/law/507AC0000000053
**Must appear on any jurisdiction map.** Showing Korea as APAC's only legislated
regime while omitting Japan is misleading.

### Source corrections applied

Removed the shared explainability/contestability claim across unrelated cases;
claims that fines generally failed; the HSBC “saved by publications” inference;
universal three-layer applicability; a guarantee that a firm keeps its licence;
unqualified MAS issuance assertions; and unsupported survey generalisations.
The fine-outcome catalogue and additional countries remain outside the core
30-minute sequence. Research gaps above are authoring notes, not narration.

## Outline

**Working strategy: problem-first, followed immediately by concepts.** Retain the
chatbot question, then provide the definitions and organising model needed to
interpret laws and cases. The full draft and sample remain subject to review.

| Section | Slides | Minutes | Teaching intent | Outline | Narration | Slides |
|---|---|---:|---|---|---|---|
| S1 · The launch decision | 1–3 | 2 | Ask the decision, and reveal the evidence it needs | revised for review | revised for review | stale |
| S2 · What AI governance covers | 4–8 | 5 | Define AI and governance; explain scope, components and roles | revised for review | revised for review | stale |
| S3 · How rules apply | 9–14 | 6 | Compare Singapore and the EU; distinguish legal force from harm; apply the distinction | revised for review | revised for review | stale |
| S4 · Cases and their lessons | 15–17 | 4 | Connect contestability, disclosure, customer liability and business loss to controls | revised for review | revised for review | stale |
| S5 · What sectors add | 18–21 | 4 | Explain finance as a worked example and transfer practices to other sectors | revised for review | revised for review | stale |
| S6 · Apply the controls | 22–25 | 4 | Combine questions with evidence and resolve the opening decision | revised for review | revised for review | stale |
| S7 · Implementation | 26–28 | 3 | Complete a record, prioritise a control gap and finish on the roadmap | revised for review | revised for review | stale |

**Total: 28 slides / 28 minutes.** Slide ranges and time allocations follow the
revision brief. Five assessment moments include the opening question. The former
35-slide `index.html` and its `sections/` remain the committed baseline until the
full rebuild after sample review; they are stale relative to this source.

### Proposed slide order

1. AI Governance Overview
2. Would you approve the launch?
3. At least four more things you need to know
4. What is an AI system?
5. What is AI governance?
6. Governance covers the AI lifecycle
7. Six components of organisational AI governance
8. Who reviews an AI proposal before launch?
9. AI governance across jurisdictions
10. Different instruments have different legal effects
11. AI Governance in Singapore
12. EU AI Act
13. Assess applicable obligations and potential harm
14. Does following a framework resolve the data issue?
15. Failure pattern: regulatory action
16. Case study: HSBC's credit-assessment disclosures
17. Failure pattern: customer claims and business losses
18. Financial Sector in Singapore
19. Financial Sector in the United Kingdom
20. Apply these governance practices in your sector
21. Who must own this before launch?
22. Three questions and the evidence to request
23. What evidence is needed before approval?
24. Would you approve the chatbot now?
25. Approve, restrict or pause?
26. Record the next decision for each priority AI use
27. Which action should come first?
28. AI Governance implementation roadmap

### Gate 2 sample

Build the complete opening and fundamentals (slides 1–9), the jurisdiction map
and legal comparison (10–14), the legal quiz (16), the HSBC case (18), the return
to the chatbot (26), and the roadmap (30). These 18 selected slides test the
revised teaching foundation, reveal behaviour, longest comparison, timeline,
case layout, visual callback and closing job aid. Original course-slide numbers
remain visible in the sample so gaps are unambiguous.

This expanded representative sample is intentional: Ray's feedback affects both
the teaching foundations and multiple layout families. It is not a full rebuild.
The sample is generated to `sample.html`, with an 18-page PDF at `sample.pdf`
and its build inputs and verification record under `gate2/`. See `FEEDBACK.md`
for the disposition of each comment. Narration and sample acceptance remain pending.

## Narration

The script lives in [script.md](./script.md), one block per course slide.
It was split out when it grew to four times the length of everything else
here: this file is the brief and the outline, that file is what is read
aloud.
