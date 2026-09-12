---
title: AI Governance Overview
series: ai-for-business-leaders

template: course
theme: corporate-clean
themes: corporate-clean,minimal-white,swiss-grid,academic-paper,course-warm
lang: en
delivery: recorded     # presenter-led | self-paced | recorded  (gate 1)
rate: 150          # spoken words per minute; estimated timing is recorded below
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
| S1 · The launch decision | 1–4 | 3 | Ask, reveal missing evidence, and establish the business context | revised for review | revised for review | stale |
| S2 · What AI governance covers | 5–9 | 5 | Define AI and governance; explain scope, components and roles | revised for review | revised for review | stale |
| S3 · How rules apply | 10–16 | 7 | Compare Singapore, EU and UK; distinguish legal force from harm; apply the distinction | revised for review | revised for review | stale |
| S4 · Cases and their lessons | 17–19 | 4 | Connect contestability, disclosure, customer liability and business loss to controls | revised for review | revised for review | stale |
| S5 · What sectors add | 20–23 | 4 | Explain finance as a worked example and transfer practices to other sectors | revised for review | revised for review | stale |
| S6 · Apply the controls | 24–27 | 4 | Combine questions with evidence and resolve the opening decision | revised for review | revised for review | stale |
| S7 · Implementation | 28–30 | 3 | Complete a record, prioritise a control gap and finish on the roadmap | revised for review | revised for review | stale |

**Total: 30 slides / 30 minutes.** Slide ranges and time allocations follow the
revision brief. Five assessment moments include the opening question. The former
35-slide `index.html` and its `sections/` remain the committed baseline until the
full rebuild after sample review; they are stale relative to this source.

### Proposed slide order

1. AI Governance Overview
2. Would you approve the launch?
3. At least four more things you need to know
4. AI adoption and oversight in UK financial services
5. What is an AI system?
6. What is AI governance?
7. Governance covers the AI lifecycle
8. Six components of organisational AI governance
9. Who reviews an AI proposal before launch?
10. AI governance across jurisdictions
11. Different instruments have different legal effects
12. AI Governance in Singapore
13. EU AI Act
14. AI Governance in the United Kingdom
15. Assess applicable obligations and potential harm
16. Does following a framework resolve the data issue?
17. Failure pattern: regulatory action
18. Case study: HSBC's credit-assessment disclosures
19. Failure pattern: customer claims and business losses
20. Financial Sector in Singapore
21. Financial Sector in the United Kingdom
22. Apply these governance practices in your sector
23. Who must own this before launch?
24. Three questions and the evidence to request
25. What evidence is needed before approval?
26. Would you approve the chatbot now?
27. Approve, restrict or pause?
28. Record the next decision for each priority AI use
29. Which action should come first?
30. AI Governance implementation roadmap

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

This is the full revised voiceover, organised by section and course-slide number.
Source IDs refer to the Research Brief. They are production references and are
not read aloud. Hypothetical examples and recommended controls are identified
separately from findings in a legal decision. Slide notes are generated from these
passages, not independently rewritten.

### S1 · The launch decision

#### 01 · AI Governance Overview

**Sources:** [R00]

**Narration:**
Welcome to AI Governance Overview. I am Ray Han, Chief AI Trainer at HGT Consultancy.
We will define AI governance, examine its scope and components, and compare selected regulatory approaches.
We will then use cases to connect governance responsibilities to decisions at work.
The final roadmap sets out implementation actions.

#### 02 · Would you approve the launch?

**Sources:** [R00], [R04]
**Delivery:** Allow 20 seconds to choose; reveal the answer before advancing.

**Narration:**
Consider this hypothetical proposal. A Singapore retailer wants to launch a customer-service chatbot.
The supplier says its product follows Singapore's Model AI Governance Framework.
The chatbot will answer customers' questions about products, orders and returns.
Would you approve the launch, reject it, or request more information?
Pause here and choose an answer.

Requesting more information is the best next step. The supplier's statement does not establish whether this deployment is ready.
Approval requires evidence about the proposed use and the controls around it.
Rejecting the proposal permanently also goes beyond the information available.
For now, withhold launch approval and identify what needs to be checked.
We will revisit this retailer.

#### 03 · At least four more things you need to know

**Sources:** [R00], [R04], [R05]

**Narration:**
First, what personal data will the chatbot collect or use?
The retailer needs to understand customer inputs, retained conversations and access to order records.
Training-data provenance is another question for the supplier; it is distinct from the retailer's use of customer data.

Second, what commitments can the chatbot make to customers? An incorrect statement about refunds may affect the business financially.
Third, which jurisdictions will it serve? The retailer's location alone does not settle every applicable obligation.
Fourth, who will be accountable for its operation, including complaints and errors?

The asterisk identifies the question with direct personal-data relevance. Other questions may also involve data protection.
Singapore's Model AI Governance Framework is voluntary. Applicable obligations under the Personal Data Protection Act remain binding.
Following a framework is one input to an assessment, rather than a complete approval record.

#### 04 · AI adoption and oversight in UK financial services

**Sources:** [R06]

**Narration:**
A 2024 Bank of England and Financial Conduct Authority survey provides a useful sector example.
Seventy-five per cent of responding firms were already using AI.
Forty-six per cent reported only partial understanding of the AI technologies they used.
A third of reported AI use cases were third-party implementations.

These figures describe UK financial-services respondents and their reported uses.
These are not global findings or answers to our launch question.
They do show why procurement and oversight deserve attention alongside adoption.
An organisation may depend on a supplier's technology while still needing enough evidence to assess its own deployment.

### S2 · What AI governance covers

#### 05 · What is an AI system?

**Sources:** [R01], [R00]

**Narration:**
An AI system is a machine-based system that infers from inputs how to produce outputs.
Those outputs may be predictions, content, recommendations or decisions, and can affect physical or virtual environments.
Systems vary in their autonomy and in whether they adapt after deployment.
This is a plain-language paraphrase of the definition used by the Organisation for Economic Co-operation and Development, or OECD.

Examples include a model that estimates credit risk, a chatbot that generates replies, and an agent that acts through software tools.
For governance, examine how the system is used as well as what the model produces.
A recommendation shown to an experienced employee has a different operating context from an automatic customer decision.
A supplier's model description therefore needs to be connected to the workflow, data and people in the organisation.

#### 06 · What is AI governance?

**Sources:** [R02], [R03], [R00]

**Narration:**
In this course, AI governance means the responsibilities, policies, decision processes and controls through which an organisation oversees AI.
It covers development, procurement and use throughout the lifecycle.
Its purpose is to achieve intended benefits, meet applicable obligations and manage harm.
This is our working definition, drawing on management-system and AI risk-management approaches.

Governance determines who may approve a use, what evidence they require and when a decision must be reconsidered.
Risk management identifies and assesses possible harm, then implements and checks the response.
Compliance establishes which external requirements the organisation must meet.
These activities are connected, but meeting a legal minimum may still leave business or ethical concerns to address.

For the retailer, governance includes an accountable business owner, approved customer commitments and a process for handling failures.
It continues after the supplier completes installation.

#### 07 · Governance covers the AI lifecycle

**Sources:** [R02], [R03], [R00]

**Narration:**
Governance starts when a business identifies a proposed AI use.
The organisation should define its purpose, expected benefit, affected people and acceptable limits.
During development or procurement, it examines data, supplier dependencies and evidence about the system.
Before deployment, it tests the intended workflow and decides whether the controls justify proceeding.

Once the system is operating, people need to monitor outcomes, handle incidents and review material changes.
A new model, data source, customer group or permission can change the original risk assessment.
Retirement also needs planning: access should be removed, records handled appropriately, and dependent workflows replaced.

The same lifecycle covers predictive models, generative AI and agents.
It includes internally developed systems, purchased services and AI already being used by staff.
Policies and management oversight apply across these activities. The diagram is a repeating lifecycle, with review when circumstances change.

#### 08 · Six components of organisational AI governance

**Sources:** [R02], [R03], [R04], [R00]

**Narration:**
We will organise the course around six components. This is a teaching synthesis, not a universal six-part legal standard.

Accountability and oversight establish responsibility, approval authority and escalation.
Inventory and impact assessment identify the uses, purposes, affected people and potential consequences.
Data and supplier governance address privacy, data quality, security and third-party responsibilities.
Testing and human oversight establish whether the system performs acceptably and whether people can intervene effectively.
Transparency and recourse address what people are told and how they can raise concerns or request review.
Monitoring and improvement cover outcomes, incidents, material changes and eventual retirement.

The components overlap. Supplier evidence contributes to testing, while complaints can reveal issues that monitoring has missed.
An inventory entry should connect to an owner and a decision record, so it supports action.
For a low-impact internal use, the evidence may be brief. More consequential uses require stronger review and controls.

#### 09 · Who reviews an AI proposal before launch?

**Sources:** [R02], [R03], [R00]

**Narration:**
A business owner defines the intended use, expected benefit and acceptable outcomes.
Technical and data teams explain the system, its limitations and the results of relevant testing.
Risk, legal and compliance functions assess applicable obligations and challenge the proposed safeguards.
An accountable executive approves the deployment conditions and accepts residual risk within the organisation's authority limits.

These are illustrative responsibilities. Job titles and reporting lines will differ between organisations.
The important operational question is whether every review has an owner and a recorded conclusion.

For our retailer, customer operations can define permitted refund information and complaint handling.
The technical team can demonstrate failure handling and access controls.
The privacy function can examine collection and retention of customer conversations.
The approving executive should be able to see the unresolved issues before deciding.
The same responsibilities continue when the system changes or a significant incident occurs.

### S3 · How rules apply

#### 10 · AI governance across jurisdictions

**Sources:** [R04], [R05], [R07], [R08], [R09], [R24], [R25]
**Delivery:** Select each jurisdiction as it is named. Allow the map to settle before moving on.

**Narration:**
Your systems, your suppliers and the people affected by them can sit in different countries.
The map groups nine jurisdictions by the kind of instrument each relies on, because that difference matters more than the map's geography.
These are selected examples, not a complete list.

Three have binding AI law. The European Union's AI Act sets cross-sector requirements that depend on the system, the activity and your role.
South Korea's AI Framework Act has been in force since January 2026.
China has no single AI law, and it does enforce binding rules on generative AI and on labelling AI-generated content.

Five rely on existing law supported by guidance. Singapore combines existing legal obligations with sector supervision and voluntary frameworks.
The United Kingdom relies on its existing regulators, with policy principles supporting implementation.
Japan passed a promotion act that carries no penalties provision.
India works through sectoral regulators, and separately requires the labelling of synthetically generated content.
Malaysia has voluntary guidelines, and a governance Bill that has been drafted but not tabled.

The United States is different again. There is no federal AI statute, and state laws are now being challenged by the federal government.

Identify the use, the affected people, the locations served, and whether your organisation is a provider or a deployer.
One service can require you to consider more than one jurisdiction at the same time.

#### 11 · Different instruments have different legal effects

**Sources:** [R04], [R05], [R08], [R09], [R10]

**Narration:**
Start with the legal form of the instrument.
Acts, regulations and binding regulatory requirements create enforceable duties within their scope.
They can apply to AI-enabled activities even when written before the technology became common.

Supervisory statements and guidance require closer reading.
Some explain how a regulator interprets existing law; others set expectations for firms under its supervision.
An instrument may be non-binding in itself while influencing assessment or corrective action under the regulator's powers.
The instrument and legal authority determine consequences, including whether a penalty applies.

Voluntary frameworks provide methods and recommended practices. Contracts or policies may create additional commitments.
These categories can overlap for a single use. They are not three risk levels, and every use need not fall under all three.

#### 12 · AI Governance in Singapore

**Sources:** [R04], [R05], [R10]

**Narration:**
For a Singapore organisation, begin with the obligations attached to its activity and data.
The Personal Data Protection Act applies to relevant collection, use and disclosure of personal data, subject to its scope and exceptions.
For the retailer's chatbot, the review should examine purposes, notification, protection and retention of customer information.
Other business and customer obligations may also apply.

Singapore's Model AI Governance Framework provides voluntary guidance for responsible deployment.
Its second edition addresses internal governance, human involvement, operations management and stakeholder communication.
They do not replace applicable law.

Sector instruments add detail where the organisation conducts a regulated activity.
A financial institution therefore needs to review the relevant MAS requirements and guidance as well.
Document the source, scope and status of each instrument, including whether a cited document is a consultation proposal.

#### 13 · EU AI Act

**Sources:** [R07], [R08], [R00]
**Delivery:** Allow 30 seconds to read the timeline after explaining the four components.

**Narration:**
The EU AI Act contains several groups of requirements.
Prohibited practices are uses the Act disallows within its scope.
High-risk systems face requirements concerning matters such as risk management, data, documentation and human oversight.
General-purpose AI model providers have a separate set of obligations.
Transparency requirements address specified interactions and content, including informing people in relevant circumstances that they are interacting with AI.
These groups can overlap; they are not four mutually exclusive boxes for every product.

Application is phased. Prohibitions began applying in February 2025, and general-purpose AI provisions in August 2025.
The general application milestone, including Article 50 transparency, was August 2026, subject to transitional provisions.
Following the July 2026 amendment, Annex III high-risk requirements apply from 2 December 2027.
The product-related Annex I high-risk requirements apply from 2 August 2028.
Future dates are labelled explicitly on the timeline.

A non-EU organisation can also be within scope, including certain cases where system outputs are used in the Union.
Check its provider or deployer role and the relevant scope provisions before concluding that the Act does or does not apply.

#### 14 · AI Governance in the United Kingdom

**Sources:** [R09], [R11], [R12]

**Narration:**
The UK approach uses existing regulators and legal frameworks to address AI in context.
For an organisation, the review begins with the activity, affected people and applicable requirements.
Data protection, equality and sector regulation may all be relevant.
The absence of one comprehensive AI checklist does not remove these duties.

The 2023 policy framework identifies five principles: safety, security and robustness; appropriate transparency and explainability; fairness; accountability and governance; and contestability and redress.
Present these as policy principles, rather than five new statutory duties imposed on every firm.

The Information Commissioner's Office addresses data protection. Financial regulators oversee financial services.
A firm therefore needs to translate existing requirements into controls for its particular AI use.
Identify decisions requiring review, the necessary evidence and how people can seek help.

#### 15 · Assess applicable obligations and potential harm

**Sources:** [R00], [R02], [R05]

**Narration:**
Legal applicability and potential harm answer different questions.
Identify the duties and expectations relevant to the use.
Assess who could be harmed, its severity and likelihood, and whether it can be corrected.
Both assessments help determine the controls and approval authority required.

Compare two hypothetical uses within the same retailer.
An employee uses AI to draft an internal meeting summary, then checks it before circulation.
Another system automatically refuses customer refunds using order histories and complaint records.
Both can involve personal data, but their effects and operating safeguards differ.
The second use can directly affect customers and requires closer examination of the decision and review arrangements.
A voluntary framework label alone does not tell the approver which use presents the greater risk.

#### 16 · Does following a framework resolve the data issue?

**Sources:** [R00], [R04], [R05]
**Delivery:** Allow 30 seconds to choose; reveal all option explanations before advancing.

**Narration:**
Our retailer's chatbot collects contact details and purchase histories to personalise offers.
Assume the notification obligation applies and no exception removes it.
The retailer has not told customers why it collects or uses this information.
The supplier follows the Model AI Governance Framework and displays an AI label.
Does this resolve the data issue?

Option A says yes, because the supplier follows a framework. That statement does not establish that the retailer has met its notification obligation.
Option B says the retailer must address the applicable PDPA obligation before launch. This is the best answer.
Option C says an AI label alone provides the required explanation. It does not explain the data-use purposes.

### S4 · Cases and their lessons

#### 17 · Failure pattern: regulatory action

**Sources:** [R13], [R00]

**Narration:**
Foodinho, a company in the Glovo group, used a digital platform to manage delivery riders in Italy.
In November 2024, the Italian data-protection authority imposed a five-million-euro penalty for unlawful processing of riders' data.
Its notice described an automated message sent when an account was blocked or deactivated.
That message did not inform riders about contesting the decision and requesting restoration of the account.

This provides a specific example of contestability: an affected person needs a usable route to challenge an outcome.
That is different from merely receiving a description of how an algorithm works.
The enforcement covered multiple data-protection issues; the penalty should not be attributed to one missing feature alone.

For a business implementing consequential decisions, our recommended control is a documented review route with an authorised human reviewer.
Test whether customers or employees can actually find and use it.

#### 18 · Case study: HSBC's credit-assessment disclosures

**Sources:** [R14], [R00]

**Narration:**
In 2018, an unsuccessful credit-card applicant asked HSBC Singapore for its internal evaluation report.
The bank provided a report with some information redacted.
The applicant sought access to the remaining information, and the dispute reached the Personal Data Protection Commission.

In its March 2021 decision, the Commission accepted that specified information could be withheld under the evaluative-purpose exception.
The decision also considered HSBC's explanations of how it used data and technology for credit assessments.
HSBC provided its Principle for the Ethical Use of Big Data and AI and its Credit Decisioning Policy Statement.
The Commissioner commented favourably on accountability and disclosure.

The legal exception supported withholding the specified data. The disclosure documents served a separate explanatory purpose.
Our governance lesson is to prepare accurate explanations of data use and decision processes, while applying the relevant access rights and exceptions.
This was not certification of HSBC's entire AI governance programme.

#### 19 · Failure pattern: customer claims and business losses

**Sources:** [R15], [R16], [R00]

**Narration:**
Two other examples show why the consequence of poor deployment is broader than a regulatory fine.
Air Canada's chatbot gave a customer incorrect information about bereavement fares.
The British Columbia Civil Resolution Tribunal held the airline responsible for the misleading information in that case.
For a customer-facing service, test policy answers and provide a route to resolve errors.

Zillow's 2021 filing reported a three-hundred-and-four-point-four-million-US-dollar inventory write-down associated with Zillow Offers.
The company cited home-pricing unpredictability, capacity constraints and other operational challenges when it decided to wind down the business.
It would be inaccurate to reduce that business outcome to one defective algorithm.
The deployment lesson is to examine forecasting uncertainty, operational capacity and financial exposure together.

These are different mechanisms: a customer claim in one case and an inventory loss in the other.
A governance review should consider both legal exposure and the organisation's ability to absorb or reverse an error.

### S5 · What sectors add

#### 20 · Financial Sector in Singapore

**Sources:** [R10], [R17], [R18]

**Narration:**
MAS's FEAT principles address Fairness, Ethics, Accountability and Transparency in the use of AI and data analytics.
They are advisory principles, first published in 2018.
They provide a useful way to examine fair outcomes, responsibility and communication in financial services.

A separate November 2025 consultation proposed Guidelines on AI Risk Management.
The proposal includes maintaining an AI inventory and proportionate risk management across the lifecycle.
We are discussing that consultation document as a proposal, not presenting it as an issued rule.
An organisation using a consultation proposal should check the current issued requirements before relying on it.

For a financial institution, the practical task is to connect AI controls to its existing governance, risk and compliance arrangements.
The review should distinguish binding requirements, advisory principles and proposals, rather than treat every MAS publication as having the same legal effect.

#### 21 · Financial Sector in the United Kingdom

**Sources:** [R11], [R12], [R00]

**Narration:**
The FCA explains that its existing frameworks apply to firms' use of AI.
Its approach identifies the Consumer Duty and senior-management accountability as relevant foundations.
The regulator can use its existing supervisory and enforcement powers where a firm's use of AI breaches the relevant financial regulatory requirements.

Responsibilities should follow the firm's activities and its documented management arrangements.
A business decision, a technology system and a risk control may involve different people, but their responsibilities must connect.
Avoid assigning all AI risk automatically to the chief technology officer or creating a new title without decision authority.

For a credit-decisioning tool, the firm should establish who owns the lending use, who challenges the risk assessment and who authorises deployment.
Supplier testing can contribute evidence. It does not remove the firm's responsibility for how the tool is used.

#### 22 · Apply these governance practices in your sector

**Sources:** [R00], [R02], [R03]

**Narration:**
The transferable practices are to map obligations, assign responsibility and retain evidence.
Start with the activity your organisation performs and identify the requirements already attached to it.
Then assign an accountable owner and an appropriate independent review.
Keep evidence of testing, decisions and monitoring so management can understand whether controls are working.

For a retailer, this may involve customer communications, personal data and refund decisions.
For an employer, it may involve recruitment, employee information and review of consequential decisions.
These are examples of questions to investigate, not a statement that identical duties apply to both.
Financial-services regulation does not automatically apply to another sector.
The useful lesson is how a regulated organisation connects its obligations to owners, controls and evidence.

#### 23 · Who must own this before launch?

**Sources:** [R00], [R11], [R12]
**Delivery:** Allow 30 seconds to choose; reveal before advancing.

**Narration:**
A UK-regulated bank is preparing a vendor-built credit-decisioning tool.
Its documented management responsibilities place this lending activity with an existing senior manager.
The vendor says it tests the model, but the bank's risk function has not reviewed the deployment.
Who needs to act before launch?

Option A leaves accountability with the vendor. Supplier responsibilities remain important, but do not replace the bank's own obligations.
Option B requires the responsible senior manager to ensure the bank completes its review before approval. This is the best answer.
Option C waits for an AI-specific job title. The FCA's approach relies on existing frameworks and accountability arrangements.
The bank should document both its own responsibilities and what evidence or support the supplier must provide.

### S6 · Apply the controls

#### 24 · Three questions and the evidence to request

**Sources:** [R00], [R13], [R14], [R11]

**Narration:**
Three questions help a business leader examine a proposal.
Who is accountable for this use? Request a named owner, a decision authority and an escalation route.
How can an affected person challenge an outcome? Request the review procedure and evidence that someone can change the decision.
What have we told people about the system? Request accurate explanations of its purpose, limitations and use of data.

Foodinho illustrates the importance of a usable challenge route. HSBC illustrates disclosure alongside legal access limits.
These cases support different lessons, rather than one universal explainability requirement.
The questions address responsibility, recourse and communication. The approval decision also needs evidence about performance and operating controls.

#### 25 · What evidence is needed before approval?

**Sources:** [R00], [R02], [R03], [R19]

**Narration:**
Ask for testing in the intended setting, including relevant users and foreseeable failure conditions.
Confirm that a person can intervene and has the authority, information and time to do so.
Identify what production monitoring will detect, who receives alerts and when escalation is required.
Finally, examine a tested way to stop, restrict or roll back the system.

Singapore's agentic guidance recommends human review for high-stakes or irreversible actions.
This is voluntary guidance; it should not be described as a general statutory prohibition.
For any proposed use, connect oversight to the consequence of an error and the permissions the system holds.
An approval record should identify the evidence reviewed, unresolved limitations, deployment conditions and the next review trigger.

#### 26 · Would you approve the chatbot now?

**Sources:** [R00], [R02], [R05]

**Narration:**
Return to the retailer introduced at the start. In this hypothetical continuation, the team now supplies four items of evidence.
The Head of Customer Operations owns the use. Customers can reach a human reviewer who can correct an outcome.
The proposed disclosures describe data use and the chatbot's limits.
A supervised trial has tested the permitted questions, escalation and shutdown process.

One limitation remains: refund-policy answers have not passed the retailer's acceptance tests.
The appropriate decision in this example is to restrict the pilot to product information and order status.
Keep refund decisions with staff until testing and controls justify expanding the scope.
Monitoring, access limits and a tested stop process must operate during the pilot.
The decision is now connected to evidence and restrictions, with the owner responsible for reassessment.

#### 27 · Approve, restrict or pause?

**Sources:** [R00], [R02], [R03]
**Delivery:** Allow 30 seconds to choose; reveal all feedback.

**Narration:**
An insurance tool flags claims for manual review. It has an owner, a review procedure and accurate customer information.
Testing has used only a supplier benchmark. There is no production monitoring or rollback process.
Should the organisation approve production use, run an unrestricted pilot, or pause production and establish safeguards?

Pausing production and establishing safeguards is the best answer.
A bounded pilot may then be appropriate, with suitable testing, monitoring, human review and rollback in place.
Approving production would leave the stated gaps unresolved. Calling a deployment a pilot does not resolve them either.
Manual referral can still cause harm through delay, bias or excessive reliance on automated recommendations.
Assess the actual workflow before deciding how much control is needed.

### S7 · Implementation

#### 28 · Record the next decision for each priority AI use

**Sources:** [R00], [R02], [R03]

**Narration:**
A short decision record makes the next action explicit.
Use five fields: the use case, accountable owner, review route, evidence and next decision with a date.
For a hypothetical complaints-triage tool, the owner is the Head of Customer Operations.
The record shows that some escalated complaints are closed without human review and testing uses only supplier data.
The next decision is whether a controlled pilot can proceed after those gaps are addressed.

Link the record to the relevant inventory entry and assessment.
When a field is incomplete, record the action, responsible person and deadline for resolving it.
This gives management a specific issue to review and a way to follow up.

#### 29 · Which action should come first?

**Sources:** [R00], [R02], [R03]
**Delivery:** Allow 20 seconds to choose; reveal before the roadmap.

**Narration:**
A firm has completed its AI inventory. Next week it plans to activate a tool that automatically declines insurance claims.
There is no appeals route or production monitoring. The board has also asked about ISO certification.
Which action should come first?

Pause the launch and establish the missing controls before deployment.
Starting certification does not resolve next week's control gap. Expanding the inventory also does not address this known exposure.
The organisation can pursue those activities alongside the urgent work, with clear ownership and priorities.
Certification may provide useful assurance, but it is separate from deciding whether this particular system is ready to operate.

#### 30 · AI Governance implementation roadmap

**Sources:** [R00], [R02], [R03], [R04], [R18]
**Delivery:** Hold the final roadmap for 20 seconds so learners can read or capture it.

**Narration:**
Begin with the foundation: create an AI inventory and assign responsibility for keeping it current.
Record each use's purpose, owner, users, data, supplier and deployment status.
Address urgent known risks while the wider inventory is being completed.

Assess the uses and establish controls. Identify applicable obligations, approval authority, testing, human review, disclosures and supplier requirements.
Then operate and improve the programme through monitoring, complaints, incident response, change review and tested rollback or retirement.

Use NIST, ISO and Singapore's governance guidance to support this work, with sector-specific sources where relevant.
The MAS inventory reference shown here comes from a consultation proposal for financial institutions.
Add assurance tools, dedicated resources or certification when risk, scale or contractual needs justify them.
Select one priority use, name its owner and record the next decision and date.

## Production review · 12 September 2026

Steps 1–3 are drafted and checked: revised 30-slide outline, complete source
narration, and an 18-slide representative Gate 2 sample. The earlier full deck
is preserved pending sample review. No acceptance hash has been set.

### Estimated recording duration

Counts include only spoken narration, excluding headings, references and delivery
instructions. At 150 words per minute, the spoken estimate below leaves time for
learner response, diagram reading, case reflection and transitions. This is a
production budget, not a measured recording. Rehearse before final recording.

| Section | Spoken words | Spoken minutes | Non-spoken allowance (seconds) | Total minutes |
|---|---:|---:|---:|---:|
| S1 | 395 | 2.63 | 22 | 3 |
| S2 | 701 | 4.67 | 20 | 5 |
| S3 | 900 | 6.00 | 60 | 7 |
| S4 | 442 | 2.95 | 63 | 4 |
| S5 | 515 | 3.43 | 34 | 4 |
| S6 | 478 | 3.19 | 49 | 4 |
| S7 | 347 | 2.31 | 41 | 3 |

Total: **3,778 spoken words**, approximately
**25.19 spoken minutes**, with planned holds
and transitions bringing the course to **30 minutes**.

Use S1's allowance for the opening response; S2's for the lifecycle and role
diagrams; S3's for the EU timeline and legal quiz; S4's for reflection on the
three cases; S5's for the ownership quiz; S6's for the callback and deployment
quiz; S7's for the priority question and final roadmap. Individual delivery
notes indicate the principal holds. Adjust pace and holds after rehearsal.

### Language and visual review

Applied no-ai-slop first, then sg-english, to the rewritten source and extracted
sample copy. Removed vague slogans, unfinished transitions and the survey-to-quiz
comparison. Expanded unfamiliar acronyms; used Singapore/British spelling;
preserved legal scope, conditions and distinctions. Ray's requested learner
question headings take precedence over generic style restrictions.

All 18 sample slides and both quiz reveal states passed the 1920×1080 text-bounds
and layout-stability checks and were visually inspected. Keyboard reveal/advance
and all three map controls passed. The PDF contains 18 landscape 16:9 pages,
with revealed answers, complete map, readable case attribution and no visible
clipping. Source limitations remain explicitly recorded in the Research Brief.

Detailed artifacts and remaining review decisions: `gate2/README.md`,
`gate2/checks.json`, `gate2/REVIEW.md`, and `FEEDBACK.md`.
