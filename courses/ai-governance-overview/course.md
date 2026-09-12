---
title: Overview for AI Governance

template: course
theme: corporate-clean
themes: corporate-clean,minimal-white,swiss-grid,academic-paper,course-warm
lang: en
delivery: self-paced   # presenter-led | self-paced | recorded  (gate 1)
rate: 110          # EFFECTIVE wpm, not raw reading speed — 250 x 30 = 7,500 words is far too dense for an exec module. Leaves ~40% of the time for diagrams, quiz checks and thinking. Budget ~3,300 words.
duration: 30       # minutes
accepted_hash:     # set at gate 3; a mismatch means index.html has diverged
---

# Overview for AI Governance

## Audience & outcomes

**Audience.** Business leaders — executives and senior decision-makers, not
practitioners. They approve AI spend, answer to a board, and carry the risk. They
are not lawyers and will not read a regulation.

**Jurisdiction.** Global overview, zoomed into **Singapore** and the **UK**.
Both are principles-based and regulator-led, which sets up the course's central
contrast with the EU's prescriptive risk-tier model. Teaching that contrast
explains "global" without walking through five regimes.

**Sector.** No sector constraint. **Financial services is the worked example**
of how sector supervision layers on top — MAS in Singapore, FCA and the Bank of
England in the UK give something concrete to point at.

**Delivery.** Self-paced online, 30 minutes. Narration renders **on-slide**, not
in `.notes` — nobody is speaking. Quiz checks must work.

### Outcomes

After 30 minutes, a business leader can:

1. Place their organisation's AI uses on a risk map, and say which face **binding
   obligation**, which face **supervisory expectation**, and which carry only
   reputational and operational risk. In Singapore and the UK most sit in the
   middle band, which is the point most executives get wrong.
2. Name who owns AI risk in their organisation, and what that person is
   accountable for.
3. Ask three questions of any AI proposal that expose the governance gaps.
4. Decide what to do in the next 90 days, and what can wait.

Outcome 4 is what makes this an executive course rather than a briefing. Without
it they leave informed and idle.

## Research Brief

<!-- A Finding without a traceable source is not a Finding. Claims in Narration
     must trace here or to supplied material, or be marked illustrative. -->

### Singapore  ✅ researched 2026-09-12

**SG-1 · No omnibus AI law.** AI risk is caught by existing broad statutes plus
sector guidance; targeted legislation only for specific harms.
> "many AI risks are covered by broad legislation such as the Personal Data
> Protection Act, the Workplace Fairness Act and the Broadcasting Act, and
> sector-specific guidelines in the healthcare, finance and legal sectors"
MDDI PQ response, 14 Oct 2025 · https://www.mddi.gov.sg/newsroom/mddi-s-response-to-pq-on-tackling-risk-of-agentic-ai-capable-of-autonomous-actions-and-unforeseen-emergent-behaviours/

**SG-2 · No dedicated AI regulator, by choice.**
> "We cannot adopt a one-size-fits-all approach to regulate it, nor can we
> anticipate every risk out there."
MDDI, 6 Jul 2023 · https://www.mddi.gov.sg/newsroom/pq-on-feasibility-of-regulate-artificial-intelligence/

**SG-3 · Model AI Governance Framework — 2nd ed, 21 Jan 2020. Voluntary.**
> "Adopting this voluntary Model Framework will not absolve organisations from
> compliance with current laws and regulations."
https://www.imda.gov.sg/-/media/imda/files/infocomm-media-landscape/sg-digital/tech-pillars/artificial-intelligence/second-edition-of-the-model-ai-governance-framework.pdf

**SG-4 · MGF for Generative AI — 30 May 2024. Voluntary. Nine dimensions.**
Accountability · Data · Trusted Development and Deployment · Incident Reporting ·
Testing and Assurance · Security · Content Provenance · Safety and Alignment R&D ·
AI for Public Good. (Several secondary summaries list only eight — the primary
lists nine.) https://aiverifyfoundation.sg/resources/mgf-gen-ai/

**SG-5 · MGF for AGENTIC AI — launched 22 Jan 2026, v1.5 pub 20 May 2026.**
The most significant recent change. Voluntary, living document.
> "It provides guidance to organisations on how to deploy agents responsibly …
> while emphasising that humans are ultimately accountable."
Four dimensions: bound the risks upfront · make humans meaningfully accountable ·
technical controls and processes · enable end-user responsibility.
v1.5 adds systemic/multi-agent risk and automation-bias practices (monitoring
human override rates). https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf

**SG-6 · PDPC Advisory Guidelines on Personal Data in GENERATIVE AI — 20 Jul 2026.**
Advisory, but interprets the binding PDPA. Addresses the Publicly Available
Exception for web-scraped training data, and splits PDPA responsibility across
**Model Providers / System Providers / System Deployers**.
https://www.pdpc.gov.sg/organisations/regulations-decisions/regulatory-guidance/advisory-guidelines-on-use-of-personal-data-in-generative-ai

**SG-7 · PDPC Advisory Guidelines on AI Recommendation & Decision Systems — 1 Mar 2024.**
Clarifies the Business Improvement and Research exceptions to consent.
> "The Guidelines are advisory in nature, are not legally binding … The
> provisions of the PDPA … will prevail over these Guidelines"

**SG-8 · Transparency Guidelines for GenAI Chatbots — 20 Jul 2026. Voluntary.**
> "The guidelines set out how chatbot deployers can provide meaningful
> transparency to their users through a chatbot info card, akin to a 'medical
> label'."

**SG-9 · AI Verify — voluntary testing framework + toolkit, 11 principles.**
Not a certification. GenAI-capable update 29 May 2025; crosswalked to ISO/IEC
42001 (21 Jul 2025) and NIST AI RMF. AI Verify Foundation is wholly owned by IMDA.
⚠️ Current adoption figures NOT established — only "over 90 corporate members"
(NAIS 2.0, Dec 2023) and "30 AI applications from 14 sectors" tested in the
Assurance Sandbox (19 May 2026).

**SG-10 · AI Tester Accreditation Programme (AI TAP) — expected 3Q 2026.**
Accredits *testers*, not systems. Executive-relevant caveat:
> "Accreditation does not eliminate residual risk. Procuring organisations remain
> responsible for risk acceptance, governance, and the implementation of any
> supplementary mitigations deemed necessary."

**SG-11 · Binding law is where the teeth are.** Codes of Practice under the
Online Criminal Harms Act (17 Aug 2026) require designated services to verify
advertiser identity and remove scam ads — catches AI-generated impersonation.
OSRAA's "inauthentic material abuse" (deepfake relief) is **announced with no
commencement date**. MDDI, 10 Sep 2026.

**SG-12 · AI content labelling NOT mandated.** Singapore is monitoring, not
requiring, as of 5 Aug 2026.
> "We will … assess if they should be mandated."

**SG-13 · National AI Strategy updated 20 May 2026.** ⚠️ Supersedes NAIS 2.0
(Dec 2023). **10 refreshed priorities**, not the earlier "15 Actions". A
**National AI Council chaired by PM Lawrence Wong** was established Feb 2026.
National **AI Missions** in Advanced Manufacturing, Financial Services,
Connectivity and Healthcare. Governance priority: "further strengthen layered AI
governance; deepen sector-specific risk management; and build AI testing,
assurance, and safety capabilities."
https://www.mddi.gov.sg/newsroom/update-to-singapore-s-national-ai-strategy--refreshed-priorities-to-harness-ai-for-the-public-good-factsheet/

**SG-14 · The test for when Singapore regulates.** The clearest statement of the
philosophy, and directly usable for outcome 1.
> "the need for regulation depends on how it is deployed, the nature of harm
> that may be caused, and whether existing measures are effective in addressing
> those harms."
MDDI, 7 Jul 2026 · Parliament asked three times in 2026 whether voluntary
frameworks would become mandatory. The answer each time was no:
agentic AI stays voluntary (5 Aug 2026); chatbot transparency stays a "voluntary
baseline" (8 Sep 2026, four days ago).

**SG-15 · The one hard line in the agentic framework.** Not a statute, but the
sharpest rule statement Singapore has published, and the one an executive can act on.
> "They should not allow high stakes or irreversible actions to take place
> without human review."
MDDI, 6 May 2026 · https://www.mddi.gov.sg/newsroom/mddi-s-response-to-pq-on-ensuring-meaningful-human-accountability-for-public-facing-autonomous-ai-agents-and-pathways-to-mandatory-governance-in-high-risk-sectors/

**SG-16 · Pax Silica — a US-convened summit, not an AI regime.** Held 12 Dec 2025
in Washington DC; produced a **non-binding declaration**. Singapore signed.
> "The Summit also agreed on a non-binding Pax Silica Declaration … Other
> signatories of the Declaration were Australia, Israel, Japan, the Republic of
> Korea, the United Kingdom, and the United States of America."
MDDI, 14 Dec 2025. ⚠️ Two primary sources disagree: a 13 Jan 2026 PQ lists the
Netherlands and UAE as summit *participants*, though neither appears in the
signatory list. Participation and signature are different sets and MDDI never
reconciles them. Commits signatories to nothing enforceable.

**SG-17 · WAICO — invitation established, the body itself is NOT.**
> "Singapore has received an invitation to participate in the World AI
> Cooperation Organisation (WAICO). There is no ASEAN position on either WAICO
> or Pax Silica."
MDDI, 9 Sep 2026. ⚠️ **Bounded claim only.** WAICO's founding date, members,
secretariat and mandate could NOT be established from any primary source, and
MDDI's own page title says "Association" while the Minister says "Organisation".
Permitted in the course: *a China-linked international AI body invited Singapore
in 2026; Singapore has not decided; ASEAN has no common position.* Nothing more.

**SG-18 · The 2020 framework is still the base.** No IMDA statement says so
directly; the safe formulation is that IMDA's own June 2026 document cites it:
> "The MGF for Agentic AI builds on the responsible AI practices for
> organisations set out in MGF (2020)"

#### Singapore — open items
- MAS AI Risk Management Guidelines: **confirmed still at consultation stage as
  at 7 Jul 2026**; whether final Guidelines have since issued is unconfirmed.
  Assigned to the financial-services research.
- MAS FEAT / Veritas not yet verified against primary MAS documents.
- WAICO's own identity, founding and membership — not establishable from
  Singapore primary sources. Would need a Chinese-government or WAICO primary
  source. **Course claim is bounded to SG-17 until then.**
- MOH AI in Healthcare Guidelines (AIHGle 2.0) — named in a primary source,
  document not retrieved. Only matters if healthcare gets a mention.
- Current AI Verify adoption figures.

### United Kingdom  ✅ researched 2026-09-12

**UK-1 · No AI Act, and no government AI bill has ever been introduced.**
Verified against the Parliament Bills API, not a summary: every AI bill to date
is a Private Member's Bill and every record returns `"isAct": false`. The
Artificial Superintelligence Bill got a first reading 8 Sep 2026 — but it is a
Ten Minute Rule bill, which Parliament's own API describes as
> "often an opportunity for Members to voice an opinion … rather than a serious
> attempt to get a bill passed."
Do not overweight it.

**UK-2 · The King's Speech of 13 May 2026 contained no AI Bill.** AI appears only
as sandboxing powers inside the **Regulating for Growth Bill**, which is
*deregulatory* — powers to switch existing rules off for testing, not to impose
AI obligations. As at 2026-09-12 it had not been introduced.

**UK-3 · Regulator-led and principles-based, confirmed from the despatch box.**
> "We believe that the best way of regulating is through context-specific
> regulation, which will take into account the specific issues that arise when AI
> is adopted by particular sectors."
Baroness Lloyd, Lords, 16 Jul 2026 · https://hansard.parliament.uk/Lords/2026-07-16/debates/E7578DA3-9339-4E53-97DA-D907647C6C66/ArtificialIntelligenceLegislation

**UK-4 · Five non-statutory principles** (2023 white paper, 29 Mar 2023): safety
security and robustness · appropriate transparency and explainability · fairness ·
accountability and governance · contestability and redress.
> "We will not put these principles on a statutory footing initially."
The anticipated statutory "due regard" duty on regulators **was never enacted**.
⚠️ The white paper is a previous government's document, never formally re-adopted
by name. Safe formulation: *framework intact, branding lapsed.*

**UK-5 · DSIT was abolished on 22 July 2026.** AI strategy, public-sector AI
adoption and the AI Security Institute moved to the **Cabinet Office**; the rest
split to BIST. There is now a dedicated **Minister of State for AI**.
https://www.gov.uk/government/news/machinery-of-government-changes-fact-sheet

**UK-6 · A STATUTORY ICO code on AI is now legally required.** The most
consequential item on the UK horizon.
> "The Commissioner must prepare an appropriate code of practice … in relation
> to— (a) developing and using artificial intelligence, and (b) automated
> decision-making."
SI 2026/425, made 16 Apr 2026, **in force 12 May 2026** ·
https://www.legislation.gov.uk/uksi/2026/425/made
ICO's own pipeline: final code **due Q1/Q2 2028**. So: legally mandated, two
years away.

**UK-7 · The automated-decision rules changed on 5 Feb 2026.** DUAA 2025 s.80
replaced UK GDPR Article 22 with Articles 22A–22D (SI 2026/82). Liberalising on
lawful basis, tightening on safeguards — a statutory four-part list: information,
representations, **human intervention**, and the right to **contest**.
> "a decision is based solely on automated processing if there is no meaningful
> human involvement in the taking of the decision"
https://www.legislation.gov.uk/ukpga/2025/18/section/80

**UK-8 · ICO AI guidance is stale and now wrong in one place.** Last updated
15 Mar 2023; still states the pre-DUAA three-gateway rule, which ceased to be the
law on 5 Feb 2026. The ICO itself says the guidance
> "is not a statutory code … There is no penalty if you fail to adopt good
> practice recommendations, as long as you find another way to comply with the law."
Binding obligation comes from UK GDPR + DPA 2018, not the guidance. **DPIAs are
the one hard requirement**: AI processing will "in the vast majority of cases"
trigger the Art 35(3)(a) legal requirement.

**UK-9 · FCA: no AI-specific rules, by explicit choice.**
> "We do not plan to introduce extra regulations for AI. Instead, we'll rely on
> existing frameworks"
FCA AI approach, updated 13 Feb 2026 · https://www.fca.org.uk/firms/innovation/ai-approach
Obligations come from SYSC 4.1.1R, SYSC 15A, PRIN 2A (Consumer Duty) and SM&CR.
The FCA and Bank considered and **rejected** a dedicated "AI Senior Manager"
function. ⚠️ The **Mills Review** (6 Jul 2026) recommends adapting the perimeter
and frameworks, which sits in tension with the February statement. The FCA has
published no reconciliation, and has not said whether it accepts the
recommendations.

**UK-10 · First binding AI-specific intervention in the UK — the CMA, 3 Jun 2026.**
Under the DMCC Act 2024, Google is
> "required to make sure that publisher content is properly attributed … in
> AI-generated search results"
with publisher opt-outs from AI Overviews. Note the shape: it arrived through
competition law, not AI law.

**UK-11 · AI Security Institute has no regulatory power.** Renamed from AI Safety
Institute on 14 Feb 2025; now part of the Cabinet Office. Frontier model testing
runs on **voluntary** company commitments. ⚠️ The only explicit "not a regulator"
statement is from Nov 2023 under the old name; no post-rename restatement found.

**UK-12 · Ofcom has an admitted gap on standalone chatbots.**
> "Because of the way the Act relates to chatbots … we are currently unable to
> investigate the creation of illegal images by the standalone Grok service"
Ofcom, 3 Feb 2026. Two regulators opened investigations into the same product in
early 2026 (Ofcom into X, 12 Jan; ICO into X/X.AI, 3 Feb). **No completed
AI-grounded ICO enforcement action in 2026.**

**UK-13 · The line that lands for executives.** There is no "UK AI compliance"
checklist. The obligations are whatever the existing sector regulator and UK GDPR
already impose. This is the same structure as Singapore, reached by a different
route, and it is the course's central point.

#### UK — open items
- Whether DUAA amended Art 35 (DPIAs) — the Art 35(3)(a) wording is the ICO's
  2023 citation. Check before asserting.
- Whether the FCA accepts the Mills Review recommendations.
- ⚠️ **EUR-Lex was blocked by a WAF for this agent — it quoted nothing from the
  EU AI Act.** All EU claims must come from the global research, not here.
### Global baseline  ✅ researched 2026-09-12

**GL-1 · ⚠️ THE EU MOVED THE CLOCK. This is adopted law, not a proposal.**
**Regulation (EU) 2026/1744** ("Digital Omnibus on AI"), adopted 8 Jul 2026,
published 24 Jul 2026, **in force 27 Jul 2026**, amending the AI Act.
https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744
Stated reason (Recital 40):
> "the delayed availability of standards, common specifications, and alternative
> guidance and the delayed establishment of national competent authorities lead
> to challenges that jeopardise the effective entry into application"

**GL-2 · The amended EU timeline.** Consolidated Art. 113 (02024R1689-20260727):

| Obligation | Applies from | Status |
|---|---|---|
| Prohibitions + AI literacy | 2 Feb 2025 | IN FORCE |
| GPAI obligations, governance, penalties | 2 Aug 2025 | IN FORCE |
| General application incl. Art. 50 transparency | 2 Aug 2026 | IN FORCE |
| New prohibitions (NCII, CSAM); legacy GenAI marking | 2 Dec 2026 | dated |
| **High-risk, Annex III** | **2 Dec 2027** (was 2 Aug 2026) | **POSTPONED** |
| **High-risk embedded in products, Annex I** | **2 Aug 2028** (was 2 Aug 2027) | **POSTPONED** |
| Legacy GPAI models | 2 Aug 2027 | dated |
| Legacy high-risk, public authorities | 2 Aug 2030 | dated |

**GL-3 · What did NOT move — say this explicitly.** Prohibitions, GPAI
obligations and Art. 50 transparency were **not** delayed. Only Chapter III
high-risk Sections 1–3. Executives who hear "the EU delayed the AI Act" will
under-read their live obligations.

**GL-4 · Extraterritorial reach — Art. 2(1).** The reason a Singapore or UK firm
cares at all:
> "(c) providers and deployers of AI systems that have their place of
> establishment or are located in a third country, **where the output produced by
> the AI system is used in the Union**"

**GL-5 · Penalties (Art. 99/101).** Prohibited practices: "up to EUR 35 000 000
or … up to 7 % of its total worldwide annual turnover … whichever is higher."
Most other breaches: EUR 15m or 3%. Misleading information: EUR 7.5m or 1%.
GPAI providers fined by the Commission: EUR 15m or 3%. SMEs pay the **lower** of
the two.

**GL-6 · ISO/IEC 42001:2023** — published Dec 2023, certifiable management-system
standard, applies to "any organization, regardless of size, type and nature".
Certification bodies governed by ISO/IEC 42006:2025 (7 Jul 2025).
⚠️ **No adoption figure is obtainable.** Do not quote one. ISO moved its survey to
IAF CertSearch, and **IAF itself ceased operations 1 Jan 2026** (merged into
Global ACI).

**GL-7 · NIST AI RMF 1.0** — Jan 2023, four functions GOVERN / MAP / MEASURE /
MANAGE, Govern cross-cutting.
> "The Framework is intended to be voluntary, rights-preserving,
> non-sector-specific, and use-case agnostic"
A revision is under way under the White House AI Action Plan; scope and timetable
NOT established, and NIST's own pages conflict. **1.0 remains current.**

**GL-8 · US federal — the direction reversed.** EO 14110 (Biden) **revoked**
20 Jan 2025. EO 14179 "Removing Barriers to American Leadership in AI" in force.
**EO 14365** (11 Dec 2025) is the one executives must know:
> "the Attorney General shall establish an AI Litigation Task Force … whose sole
> responsibility shall be to challenge State AI laws"
plus BEAD funding ineligibility for states with "onerous AI laws". Carve-outs for
child safety and state procurement.

**GL-9 · ⚠️ The Colorado AI Act NEVER took effect.** Widely taught as the US
model law. SB 24-205 was delayed twice, then **repealed and reenacted** by
SB 26-189 (signed 14 May 2026) with duties starting **1 Jan 2027** — and
enforcement of the original was **enjoined** by a federal court on 27 Apr 2026
(*X.AI LLC v. Weiser*). ⚠️ Injunction sourced from the fiscal note and DOJ
release, not the docket.

**GL-10 · California is the operative US regime today.** SB 53 Transparency in
Frontier AI Act in force (>10^26 operations, >$500M revenue, $1,000,000 per
violation). AB 2013 training-data transparency in force since 1 Jan 2026. CPPA
ADMT rules phase to 1 Jan 2027. California signed more AI law **three days ago**
(SB 813, AB 1405 on AI auditors, 9 Sep 2026; child-safety chatbot laws 10 Sep).

**GL-11 · Asia is ahead of the US on statute.**
- **Korea** — AI Framework Act **in force 22 Jan 2026**, the first comprehensive
  Asian AI statute. GenAI output labelling; fines to KRW 30m.
  ⚠️ The widely reported "one-year grace period on fines" is NOT in the Act.
- **China** — in force and already enforced. GenAI Interim Measures (Aug 2023),
  content-labelling Measures (1 Sep 2025) with a CAC enforcement sweep announced
  Nov 2025. No comprehensive AI Law published, only a legislative plan.
- **Japan** — AI promotion law (fully in force 1 Sep 2025) with **no sanctions
  chapter at all**; a full-text scan returns zero occurrences of 罰則/罰金/懲役.
- **India** — IT Amendment Rules binding from **20 Feb 2026**: mandatory labelling
  and provenance metadata for synthetic content. Separate from the non-binding
  India AI Governance Guidelines (5 Nov 2025), which state the philosophy:
  > "India's approach in general is to govern the applications of AI by
  > empowering the relevant sectoral regulators, and not to regulate the
  > underlying technology itself."
  Same philosophy as Singapore and the UK.

**GL-12 · One definition, many rulebooks — the best structural slide available.**
The OECD definition (OECD/LEGAL/0449, revised 3 May 2024) and the EU AI Act's
Art. 3(1) are near-verbatim:
> OECD: "a machine-based system that, for explicit or implicit objectives, infers,
> from the input it receives, how to generate outputs such as predictions,
> content, recommendations, or decisions that can influence physical or virtual
> environments."
The OECD Recommendation has 47 adherents and is "not legally binding … a
political commitment". Jurisdictions agree on *what AI is* and diverge entirely
on *what to do about it*.

#### Global — open items
- ISO/IEC 42001 adoption numbers — unobtainable, do not quote.
- NIST AI RMF revision scope and timetable.
- EO 14365 downstream steps (Commerce evaluation, NTIA BEAD notice, FCC
  proceeding) — no primary evidence any occurred. Do not assert they did.
- FTC preemption policy statement is **proposed only**.
### Financial services  ✅ researched 2026-09-12

**FI-1 · Neither Singapore nor the UK has a single binding AI-specific rule for
financial institutions.** Every AI instrument in both is advisory.

**FI-2 · What "non-binding guideline" actually means — the sharpest quote in the
whole brief.** MAS draft TPRM Guideline 2.5:
> "An FI should be able to demonstrate to MAS its observance of the expectations
> in these Guidelines. Where MAS is not satisfied … MAS may require the FI to
> take additional measures … which could include pre-notification of new material
> third-party arrangements. MAS may also take non-observance into account in its
> assessment of the FI … MAS may also directly communicate with the home or host
> regulators of the FI and the FI's service provider."
P004-2026, 6 Mar 2026. **Non-binding does not mean optional.** This single quote
dismantles the most common executive misreading.

**FI-3 · MAS's own instrument hierarchy.** Acts, Subsidiary Legislation,
Directions and Notices bind. Guidelines do not:
> "Contravening guidelines is not a criminal offence and does not attract civil
> penalties, but … How well an institution or person observes the guidelines may
> have an impact on MAS' overall risk assessment"
> "Circulars have no legal effect."
https://www.mas.gov.sg/regulation/mas-supervisory-approach-and-regulatory-instruments
FEAT is filed as an *Information Paper* — not even listed as a regulatory
instrument.

**FI-4 · MAS FEAT — 12 Nov 2018, advisory, still live.** 14 principles.
> "This set of Principles is not intended to be prescriptive."
Two that matter to a board:
> P8: "Firms using AIDA are accountable for both internally developed and
> externally sourced AIDA models."
> P10: "Data subjects are provided with channels to enquire about, submit appeals
> for and request reviews of AIDA-driven decisions that affect them."

**FI-5 · Veritas — concluded 26 Jun 2023.** Three phases, MAS-led consortium,
turned FEAT into per-principle assessment methodologies plus an open-source
Python toolkit. Not binding, and finished. https://www.mas.gov.sg/schemes-and-initiatives/veritas

**FI-6 · MAS AI Risk Management Guidelines — consulted, NOT issued.**
⚠️ Corrects the earlier premise: consultation was **13 Nov 2025** (P017-2025),
closed 31 Jan 2026, proposing a **12-month transition after issuance**. As at
2026-09-12 no Response to Feedback and no Guidelines page exist; MAS's own March
2026 TPRM paper still calls them "(proposed)". **The clock has not started.**

**FI-7 · SAFR — 3 Jul 2026.** MAS paper on governing AI agents: "defining how
agent actions are authorised, how human oversight is activated, and what is
recorded at the point of every decision." Explicitly not advice.

**FI-8 · The AI outsourcing gap.** MAS Guidelines on Outsourcing (effective
11 Dec 2024) contain **no mention of AI or machine learning**, and a GenAI API
call typically falls outside the definition of an outsourcing arrangement. The
binding layer is Notices 658/1121. Proposed TPRM Guidelines would supersede and
widen this to all third-party services — consultation closed 20 Apr 2026, not
finalised.

**FI-9 · UK FCA: "enough regulatory bite".** Jessica Rusu, FCA, to the Treasury
Committee, 20 Jan 2026: SM&CR and the Consumer Duty together give the FCA
> "enough regulatory bite that we don't need to write new rules for AI."
https://publications.parliament.uk/pa/cm5901/cmselect/cmtreasy/684/report.html

**FI-10 · SM&CR is the UK accountability mechanism, and it is binding.** AI use
falls to **SMF24** (Chief Operations) and **SMF4** (Chief Risk).
> "any use of AI in relation to an activity, business area, or management
> function of a firm would fall within the scope of a SMF manager's
> responsibilities."
There is **no AI-specific Prescribed Responsibility** and the FCA declined to
create a dedicated AI Senior Manager function. Answers outcome 2 directly:
in a UK regulated firm, AI risk already has a named owner.

**FI-11 · BoE/FCA adoption survey, 21 Nov 2024** (latest published; a 2026 wave
was fielded to 31 Jul 2026 but is unpublished):
- 75% of firms already using AI, 10% more planning to
- **46% report only "partial understanding"** of the AI they use; 34% complete
- 55% of use cases involve some automated decision-making
- **only 2% fully autonomous**
- a third of use cases are third-party implementations, up from 17% in 2022
The 46% figure is the best single slide in the deck for outcome 3.

### Enforcement and consequences  ✅ researched 2026-09-12

**EN-1 · The enforcement gap IS the finding.** Singapore's PDPC has issued **no
AI-specific enforcement decision** — no penalty against any organisation for an
AI system, algorithm or chatbot. MAS has taken **no AI or model-risk enforcement
action**. Singapore has published more AI governance material than almost any
jurisdiction and enforced none of it.

**EN-2 · Where Singapore does bite: technology governance, not models.** MAS
imposed ~**S$1.6bn** additional regulatory capital on DBS plus a **six-month
pause on non-essential IT changes** (1 Nov 2023 – 30 Apr 2024) and a ban on new
business ventures. Cited shortcomings: "system resilience; incident management;
change management; technology risk governance and oversight."
⚠️ mas.gov.sg blocks automated fetch; quotes came via Internet Archive. Verify in
a browser before shipping.

**EN-3 · The one SG decision turning on an algorithm produced no penalty.**
HSBC [2021] SGPDPC 3, 10 Mar 2021 — algorithmic output *is* personal data, but
credit scores were withholdable as evaluative opinion data.
> "I did not consider the fact that the Redacted Data was algorithmically
> generated data to be relevant in determining whether they formed part of the
> Applicant's personal data."

**EN-4 · UK ICO record is thin and unresolved.** Clearview AI £7,552,800 —
**do not say it stands.** FTT overturned it on jurisdiction (17 Oct 2023); Upper
Tribunal set that aside and remitted (6 Oct 2025); **no 2026 judgment**, verified
against the National Archives caselaw database. Four years, never adjudicated on
the merits. Serco Leisure got enforcement notices and **no fine** (23 Feb 2024).
Snap's "My AI" ended in **no action** after a fifth DPIA satisfied the ICO.
The ICO has **never** fined an AI recruitment vendor or user.

**EN-5 · Where algorithmic enforcement actually stuck — labour and public sector.**
- Deliveroo Italy **€2.5m** (2 Aug 2021), Foodinho/Glovo **€2.6m** (2021) and
  **€5m** (13 Nov 2024) — rider management algorithms, no route to contest.
- **Netherlands Belastingdienst** — the strongest case in the set. Two separate
  fines: €2.75m (nationality as a risk-classification indicator, found
  *discriminatory*) and €3.7m (the FSV fraud blacklist). At least 244,273 people
  and 30,000 businesses affected. **The Rutte III cabinet resigned, 15 Jan 2021.**
  Over 43,000 recognised victims, each receiving at least €30,000.
- **Robodebt** (Australia) — $1.763bn unlawfully asserted against ~433,000
  people, $751m recovered from ~381,000 and refunded.
  > "a crude and cruel mechanism, neither fair nor legal"

**EN-6 · Frontier-AI enforcement has mostly FAILED — the honest counterweight.**
- OpenAI's €15m Garante fine **annulled** by the Tribunale di Roma, 18 Mar 2026,
  on jurisdiction. The substantive AI findings were never examined.
- Clearview's Italian **€20m never collected**. A €20m headline that produced €0.
- NYC Local Law 144: one compliance issue found across 32 companies, **no
  penalties** two and a half years in (NY Comptroller audit, 2 Dec 2025).
- CFPB Circulars 2022-03 and 2023-03 **withdrawn** 12 May 2025.

**EN-7 · Moffatt v. Air Canada, 2024 BCCRT 149, 14 Feb 2024 — you own what your
system says.** The simplest principle in the deck.
> "Air Canada suggests the chatbot is a separate legal entity that is responsible
> for its own actions. This is a remarkable submission. … It should be obvious to
> Air Canada that it is responsible for all the information on its website."
Damages: CAD 812.02. The number is the point — trivial award, total principle.

**EN-8 · Zillow Offers — no regulator, no lawsuit, a quarter of the company.**
~**$304m** Q3 2021 inventory write-down, $240–265m further expected, ~**25%** of
staff cut, after a pricing model was confidently wrong.
> "the unpredictability in forecasting home prices far exceeds what we
> anticipated"
SEC filing, 2 Nov 2021. Best case in the set for a CFO audience.

**EN-9 · Mobley v. Workday — the AI vendor in the dock, live now.** Nationwide
age-discrimination collective certified against the *vendor*, not employers
(N.D. Cal., 16 May 2025). Active as of Sept 2026, not settled.
⚠️ The 2026 procedural history is law-firm sourced, not order PDFs.

**EN-10 · Regulators police AI *claims* most easily of all.** SEC "AI washing"
settlements (Delphia $225k, Global Predictions $175k, 18 Mar 2024); FTC
Operation AI Comply (25 Sep 2024); FTC v. Rite Aid five-year facial recognition
ban (19 Dec 2023). Saying it does more than it does is the cheapest case to bring.

**EN-11 · Do NOT use.** Amazon's scrapped recruiting tool is **journalism only**
(Reuters, 2018, five anonymous sources, no regulator finding) — say "reported",
never "found". TikTok's £12.7m is not AI enforcement; it concerns under-13s'
consent with no finding about the recommender.

#### Enforcement — verification gaps before shipping
- MAS and ICO press-release wording is secondary (both sites block automated
  fetch). Tribunal judgments are verbatim and solid.
- Marina Bay Sands S$315,000 — no verbatim quote obtained.
- Mobley 2026 procedural history — law-firm reporting.
- MAS AIRM issuance date — no primary source. **Do not repeat secondary
  speculation**, including a reported Aug 2026 statement that could not be traced.

## Outline

<!-- Approved at gate 1, together with the Research Brief above.
     Strategy: concept-first | example-first | problem-first -->

| # | Section | Min | Teaching intent | Findings | Outline | Narration | Slides |
|---|---------|-----|-----------------|----------|---------|-----------|--------|
| 1 |         |     |                 |          | pending | pending   | pending |

<!-- Per-Section status is the gate. A gate passes when every Section has passed
     it. Changing a Section's outline marks that Section's narration and slides
     stale — and nothing else. -->

## Narration

<!-- One script for the whole course, organised by Section, written against the
     minute budgets above. Edit directly; hand-edits are detected by hash. -->

### 1.

