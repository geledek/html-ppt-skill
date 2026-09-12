---
title: Overview for AI Governance
series: ai-for-business-leaders

template: course
theme: corporate-clean
themes: corporate-clean,minimal-white,swiss-grid,academic-paper,course-warm
lang: en
delivery: recorded     # presenter-led | self-paced | recorded  (gate 1)
rate: 150          # spoken wpm. Narration is a VOICEOVER SCRIPT, not on-slide prose. 30 min of runtime = ~21 min of script plus quizzes, transitions and pauses.
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

**Delivery.** Recorded, 30 minutes, watched at the learner's own pace.

A voiceover is recorded from the Narration below, so the Narration is a **script
to be read aloud** and does not appear on the slide. Slides carry the headline
and the visual — a table, the layer stack, the figures — and nothing the voice is
already saying. Printing the script on screen while someone reads it aloud is the
worst way to present either.

In the built deck the script lives in each slide's `<div class="notes">`, hidden
from the audience view and readable by pressing `S`.

Quiz checks are interactive: the learner clicks, or the answer reveals when the
recording advances.

### Outcomes

After 30 minutes, a business leader can:

1. Sort their organisation's AI uses by which rules actually apply in Singapore —
   binding law, supervisory expectation, or voluntary guidance — and recognise
   where other jurisdictions differ.
2. Designate an accountable owner for each consequential AI use, and in a
   regulated firm, identify who already holds it.
3. Interrogate any AI proposal with a short set of questions that expose
   governance gaps before approval.
4. Leave with an actionable AI governance roadmap: what to do in the next 90
   days, and what follows.

Outcome 4 is what makes this an executive course rather than a briefing. Without
it they leave informed and idle. The course therefore ends on a **one-page
roadmap** the learner can screenshot or print, not on a closing sentence.

Three phrases were cut from an earlier draft of these outcomes and should stay
cut. **"Risk map"** promised an artefact the course never shows. **"Middle band"**
was jargon from the three-tier framing, used before the learner has seen it. And
**"the point most executives get wrong"** had no source — the 46% figure is about
understanding AI systems, not about understanding which rules apply — so it broke
the course's own provenance rule.

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

**SG-19 · "AI inventory" is MAS's own term — use it, not "registry".** Named
section heading in the draft Guidelines (P017-2025, 13 Nov 2025):
> "**AI Inventory** — 3.4 An FI should establish and maintain an accurate and
> up-to-date **inventory** of AI use cases, systems or models across the FI to
> support governance and oversight, as well as risk management, throughout the
> AI lifecycle."
And it ties the inventory to ownership, which is outcome 2:
> "3.7 The FI should assign clear roles and responsibilities for the
> **inventorisation** of AI, including the designation of a control function to
> be responsible for the AI inventory"
https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management
MAS never uses "register" or "registry" for this.

⚠️ **"Register" is not a synonym, and using it would mislead.** In the EU AI Act
"registration" means filing a high-risk system in a **public EU database run by
the Commission** (Arts. 49 and 71) — an external, provider-side obligation. Put
"AI register" on a Singapore slide and you imply a regulator-facing filing that
does not exist here. Note also that the AI Act imposes **no general obligation on
a private-sector deployer** to keep an internal record: Art. 26(6) requires
retaining automatically generated **logs** for at least six months, and Art. 26(8)
extends registration only to *public-authority* deployers.

⚠️ **Do NOT attribute "inventory" to ISO/IEC 42001.** Its nearest Annex A control
is titled **"A.4.2 Resource documentation"**. The standard is paywalled and its
body text could not be verified from a primary source, so "ISO requires an AI
inventory" is unverified and should not be said.

**SG-19b · Corroboration outside Singapore.** NIST AI RMF GOVERN 1.6, verified
from the PDF: "Mechanisms are in place to inventory AI systems and are resourced
according to organizational risk priorities." The ICO uses "AI inventory" in its
own internal AI use policy (Aug 2025). IMDA uses neither term anywhere — the
agentic framework's nearest concept is that agent identities should be
"catalogued and centrally managed". The FCA has published no term at all.

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

**EN-3b · What SAVED HSBC — the most actionable finding in the brief.** The
Deputy Commissioner credited HSBC's *published* governance:
> "Even though HSBC was entitled to decline providing access to the Redacted
> Data, it had acted reasonably by providing information about how it uses data
> and technology to conduct credit facility assessments. From the perspective of
> accountability and disclosure of policies and practices, HSBC had acquitted
> itself."
HSBC had published a "Principle for the Ethical Use of Big Data and AI" and a
"Credit Decisioning Policy Statement". Governance documentation is not
bureaucracy here; it is what a regulator credited. Feeds outcome 4 directly.

**EN-4 · UK ICO record is thin and unresolved.** Clearview AI £7,552,800 —
**do not say it stands.** FTT overturned it on jurisdiction (17 Oct 2023); Upper
Tribunal set that aside and remitted (6 Oct 2025); **no 2026 judgment**, verified
against the National Archives caselaw database. Four years, never adjudicated on
the merits. Serco Leisure got enforcement notices and **no fine** (23 Feb 2024).
Snap's "My AI" ended in **no action** after a fifth DPIA satisfied the ICO.
The ICO has **never** fined an AI recruitment vendor or user.

**EN-4b · The most common outcome is not a fine — the sanction is the
investigation.** Serco: notice, no fine. Snap "My AI": preliminary notice, five
DPIA revisions, then **no action**. HSBC Singapore: the bank won. Pieces
Technologies: disclosure obligations, no penalty. The cost is the investigation,
the remediation and the public record.
> Stephen Almond, ICO, on Snap: "Our investigation into 'My AI' should act as a
> warning shot for industry."

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
Damages: CAD **812.02** ($650.88 + $36.14 interest + $125 fees). Trivial award,
load-bearing principle. Also usable:
> "it does not explain why customers should have to double-check information
> found in one part of its website on another part of its website."
⚠️ **Do NOT say Air Canada disabled the chatbot** — no primary source. Air Canada
did not appeal.

**EN-7b · NYC "MyCity" chatbot — the refusal to withdraw is the lesson.**
The Markup, 29 Mar 2024: the city's small-business chatbot advised that a
landlord could refuse a housing-voucher tenant, that "There are no restrictions
on the amount of rent that you can charge a residential tenant", and that an
employer could take a cut of workers' tips. The city's response was that it had
"already provided thousands of people with timely, accurate answers" and would
"continue to focus on upgrading this tool". **It was not taken down.**
⚠️ Journalism, not a regulator finding. Frame as reported.

**EN-8 · Zillow Offers — no regulator, no lawsuit, a quarter of the company.**
~**$304m** Q3 2021 inventory write-down, $240–265m further expected, Homes
segment pre-tax loss **$(421.6)m**, and a workforce cut of "approximately 25%"
after a pricing model was confidently wrong. ⚠️ The company gave only the
percentage; the widely quoted ~2,000 headcount is media arithmetic.
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

**EN-10b · The sharpest sentence any regulator wrote — but it is withdrawn.**
CFPB Circular, on adverse-action reasons from opaque models:
> "A creditor's lack of understanding of its own methods is therefore not a
> cognizable defense against liability"
⚠️ **Withdrawn 12 May 2025** in a sweep of 67 guidance documents. Quote it as a
standard a regulator once articulated, never as live guidance. ECOA §1691(d) and
Reg B §1002.9 still bind regardless of the withdrawal.

**EN-10c · Apple Card / Goldman Sachs — the regulator found NO discrimination.**
NYDFS reviewed ~400,000 New York applications and found neither disparate
treatment nor disparate impact. The lesson is reputational, not legal: a viral
thread triggered a state investigation the bank won and still lost.
⚠️ **Do not say "DFS called it a black box."** DFS attributes that characterisation
to the complaining consumer, and records that Goldman *could* explain every
complainant's decision when asked. NYDFS went further than its own finding:
> "even the exclusive consideration of such financial characteristics does not
> prevent that history of discrimination from affecting credit scores."

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
- **UnitedHealth "nH Predict" / Cigna "PXDX" claim-denial litigation — NOT
  researched.** Flagged as likely the most powerful financial-services-adjacent
  case available. Search budget ran out. Decide whether the course needs it.
- Robodebt: the settlement was **$112m inclusive of costs**. $1.763bn is debts
  *withdrawn* and $751m *refunded* (a subset). "$1.872 billion" is unverified.
- Post Office Horizon: cite **[2019] EWHC 3408 (QB)**, not TCC. ~1,000 people
  prosecuted. On the 13 deaths Sir Wyn **declines a causal finding** — "I cannot
  make a definitive finding … I do not rule it out as a real possibility."
  At least 59 contemplated suicide, ten attempted.
- Air India or any airline/bank withdrawing an AI product: **not found**. Leave out.
- AI hallucination case counts (~1,668 by Jul 2026) and *Couvrette v. Wisnovsky*:
  database blocked, **unverified**. No number on a slide without re-checking.
- France/CNIL: recommend dropping entirely — CNIL de-publishes sanctions and no
  live page backs the Clearview €20m.

## Outline

**Teaching Strategy: problem-first.** ✅ **Gate 1 approved 2026-09-12** (Research
Brief + Outline together). Revised after an external review; see "Review
corrections" below.

**Failure mode of this strategy:** problem-first frustrates beginners, and
self-paced is where that bites hardest — no presenter is there to recover a
learner who bounces off the opening. Mitigated by making the opening a bounded
scenario with immediate corrective feedback, not an open-ended audit.

**Running example:** a Singapore business wants to launch a customer chatbot; the
supplier says it follows the Model AI Governance Framework. Introduced in S1,
revisited in S3, S6 and S7.

| # | Section | Min | Words | Teaching intent | Findings | Outline | Narration | Slides |
|---|---------|-----|-------|-----------------|----------|---------|-----------|--------|
| 1 | Is that enough to approve launch? | 2 | 220 | Create the gap with a bounded, answerable decision; correct it immediately | SG-3, FI-11 | approved | drafted | pending |
| 2 | One definition, many rulebooks | 2 | 220 | Reframe "is AI regulated?" into "which use, where, judged by whom?" | GL-12, GL-11 | approved | drafted | pending |
| 3 | The three tiers of legal force · **quiz** | 6 | 660 | Outcome 1. Legal force is a separate axis from severity of harm | SG-1/3/14, FI-2/3, UK-3/13, GL-2/3/4 | approved | drafted | **built — REPRESENTATIVE** |
| 4 | Where enforcement actually is · **quiz** | 4 | 440 | Accuracy alone does not establish lawful deployment | EN-1/2/5/6/7/8 | approved | drafted | pending |
| 5 | The sector layer: financial services · **quiz** | 4 | 440 | Outcome 2. Responsibility maps to an existing owner | FI-4/6/9/10 | approved | drafted | pending |
| 6 | Three questions + the decision rule · **quiz** | 5 | 550 | Outcome 3, applied to the running example | EN-3b/7/10c, FI-4, SG-15, FI-7 | approved | drafted | pending |
| 7 | Your next 90 days · **quiz** | 7 | 770 | Outcome 4. A prioritisation decision, not a checklist | EN-3b, SG-15 | approved | drafted | pending |

Total 30 min · 3,300 words · ~26 slides · 4 quizzes.
Quiz stems, options and per-option feedback **count inside** each section's word
budget. The 110 wpm effective rate already discounts for thinking time — do not
add a second interaction allowance on top.

### Review corrections applied at gate 1

An external review (codex, high reasoning effort) checked the outline against this
brief. Accepted and folded in:

1. **Outcome 1 conflated two axes.** "Binding obligation / supervisory expectation
   / reputational risk only" mixes *legal force* with *severity of harm*. All
   three layers can apply to one use at once, and a voluntary framework does not
   move an activity into a reputational-only bucket. Teach: tag the applicable
   layers, then assess consequence and urgency separately.
2. **Rebalanced from orientation to application.** S1-S5 had 23 of 30 minutes.
   Now 2/2/6/4/4/5/7.
3. **Opening replaced.** The original bundled "list your uses" with "classify
   their legal status", assumed learners could not, and resolved with a statistic
   that normalises the wrong gap — understanding an AI system is not the same as
   understanding its legal obligations. Replaced with the bounded chatbot
   scenario. FI-11's 46% demoted to dated context.
4. **"None was about model accuracy" is false inside its own section.** Zillow
   *was* a forecasting failure; Air Canada *was* wrong information. Correct claim:
   **accuracy alone does not establish lawful or responsible deployment.**
5. **FI-2 must carry its provenance** — draft TPRM guidelines, March 2026, not an
   issued AI guideline.
6. **S4 quiz key was unsupported.** EN-5 evidences no contest route for the
   *rider* cases. It does not establish that as the common factual finding across
   the Dutch and Robodebt cases. Rewritten as a judgement question.
7. **"Frontier cases that failed" groups four different outcomes** — annulment on
   jurisdiction, non-collection, unadjudicated merits, few violations detected.
   Label them individually. Say Clearview **Italy** €20m; say the UK case is
   unadjudicated **on the merits**.
8. **EN-1 needs scope and date**: "as at 12 Sep 2026 this research found no
   AI-specific PDPC enforcement decision", and distinguish decisions,
   investigations and penalties.
9. **SMF24/SMF4 are examples, not a universal rule.** The FCA's words say
   responsibility follows the relevant activity, business area or function.
10. **HSBC lesson narrowed.** The decision also holds HSBC was *entitled* to
    withhold. Publication did not win the case; it was credited on accountability
    and disclosure.
11. **India is not purely principles-based** — binding synthetic-content rules
    since 20 Feb 2026 (GL-11). **China has no comprehensive AI law**; Korea has a
    framework act.
12. **Apple Card stays reputational.** NYDFS found no discrimination, so it is not
    evidence of deceptive claims.
13. **All four quizzes become judgement, not recall**, each with explanatory
    feedback on *every* option.
14. **NEW — the missing executive decision.** The three questions can all be
    answered satisfactorily while approving a system with no evidence it works.
    S6 adds a deployment decision rule: what evidence justifies approve, restrict
    or stop. Anchored on SG-15 ("should not allow high stakes or irreversible
    actions to take place without human review") and FI-7.
15. **DBS still needs browser verification** before it ships (EN-2).

Rejected: cutting S4 to 3 minutes. The Dutch childcare case is the only item in
the brief where an algorithm brought down a government; it earns its minute, taken
from S6.

Deferred as out of scope: piloting the module with representative executives and
measuring section completion.

## Representative Section — S3

Chosen as the **most demanding** section: the widest table (two jurisdictions ×
three tiers), the most blockquotes, the EU timeline, and a quiz. Six slides. It
stresses more layout components than any other section, which is what a design
sample has to do. S7 is marginally longer in words (689 vs 629) but is mostly
prose and a list, so it would prove less.

Rendered to `sample.html` and reviewed live at gate 2.

## Narration

Delivery is **recorded**, so this text is a **voiceover script**. It does NOT
appear on the slide — it lives in each slide's `<div class="notes">`, hidden from
the audience view and readable with `S`. Slide numbers below (1.2, 3.4 …) are
Section.Slide.

Edited through the `no-ai-slop` skill; zero banned words remain.

**Measured at 150 spoken wpm:**

| S | Script words | Min spoken |
|---|---|---|
| 1 | 200 | 1.3 |
| 2 | 204 | 1.4 |
| 3 | 619 | 4.1 |
| 4 | 451 | 3.0 |
| 5 | 438 | 2.9 |
| 6 | 539 | 3.6 |
| 7 | 683 | 4.6 |
| **Total** | **3134** | **20.9** |

Script runs 21 minutes. The remaining ~9 minutes of the 30-minute runtime are the
four quiz pauses, transitions, and time on the roadmap one-pager. If the recorded
cut comes in short, S7 has the most room to grow — it carries the roadmap.

### S1 · Is that enough to approve launch?  (2 min · target 220)

**1.2 — The decision**
A Singapore business wants to launch a customer service chatbot. The supplier
says its product follows Singapore's Model AI Governance Framework. You are
asked to approve the launch.

Is that enough?  ( Yes · No · Need more information )

**1.3 — What you are missing**
Need more information is the right answer. "No" is also reasonable. "Yes" is not.

IMDA wrote the Model Framework, and says in the framework itself that adopting
it "will not absolve organisations from compliance with current laws and
regulations." The framework is voluntary. The Personal Data Protection Act is not.

Four things you still do not know: what data the chatbot collects and what it was
trained on; what it can tell a customer that costs you money; where your
customers are sitting when they use it; and who in your organisation answers for
it when it is wrong.

Those four gaps are the next 28 minutes. None of them is answered by a framework,
and all of them are answerable by you.

If you picked Yes, you have company. In the Bank of England and FCA survey of UK
financial firms, 46% of those using AI reported only partial understanding of the
AI they use.

### S2 · One definition, many rulebooks  (2 min · target 220)

**2.1 — The agreement**
Forty-seven countries have adhered to the same definition of an AI system. The
OECD wrote it in 2019 and revised it in 2024. The EU copied it almost word for
word into Article 3(1) of the AI Act.

Agreement stops there.

**2.2 — The divergence**
The EU sets risk tiers in law, with fines reaching 7% of worldwide turnover.

Singapore and the UK hand the job to the regulators that already exist, and
publish guidance rather than rules. India says the same thing about philosophy, but has
binding rules on labelling synthetic content in force since February 2026.

Korea passed a framework act, in force January 2026. China has no comprehensive
AI law, and binding rules on generative AI and content labelling that it already
enforces.

The United States reversed direction in 2025 and is now litigating against its
own states.

**2.3 — The reframe**
So "is AI regulated?" has no answer. The word covers a Korean statute, a Chinese
labelling rule, a Singapore guideline and an American lawsuit against a state.

"Which of my uses, where, judged by whom?" does have an answer, and you can work
it out in an afternoon. That question is the shape of everything that follows.

### S3 · The three tiers of legal force  (6 min · target 660)

**3.1 — Three layers, all at once**
Every jurisdiction in this course has three layers, and all three apply to the
same system at the same time.

Binding law that was not written about AI, and binds anyway.
Supervisory expectation. Not law. Not optional either.
Voluntary frameworks. Genuinely voluntary.

The common mistake is reading these as a ranking, where satisfying the top one
excuses the others. They are not a ranking, and satisfying one says nothing about
the other two.

**3.2 — Singapore and the UK**
[ table: Singapore | UK across the three tiers ]

Neither country has an AI Act, and both have said why. Singapore: "We cannot
adopt a one-size-fits-all approach to regulate it, nor can we anticipate every
risk out there." The UK, from the despatch box in July 2026: "the best way of
regulating is through context-specific regulation."

**3.3 — What the middle tier actually costs**
This is where executives misjudge, in both directions. Some treat guidance as
law. Others treat it as decoration.

MAS spelled out the cost of ignoring a non-binding guideline in its draft
third-party risk management guidelines, published March 2026. Where MAS is not
satisfied with a firm's observance, it "may require the FI to take additional
measures", will "take non-observance into account in its assessment of the FI",
and "may also directly communicate with the home or host regulators of the FI and
the FI's service provider."

Supervision enforces that guidance, rather than penalties. A firm that ignores it
keeps its licence and loses the benefit of the doubt.

**3.4 — Legal force is not severity**
Two dimensions, and mixing them is the most expensive error in this course.

Legal force asks which layers apply. Consequence asks how bad it is when this is
wrong. They are independent.

A use can sit under binding law and be trivial. A use can sit under nothing but
voluntary guidance and be the one that ends up in the newspaper. Adopting a
framework does not move an activity into a low-risk bucket; it does not move it
at all.

Tag the layers. Then rank by consequence. Separately, and in that order, because
the layers tell you who asks the questions and the consequence tells you how fast
you need an answer.

**3.5 — The EU AI Act is partially live**
You are not in the EU. You may still be in scope. Article 2(1)(c) reaches
providers and deployers in a third country "where the output produced by the AI
system is used in the Union."

Some obligations were postponed. Regulation (EU) 2026/1744, in force 27 July
2026, moved the high-risk obligations to December 2027 and August 2028.

Others are already in force: prohibitions since February 2025, general-purpose AI
obligations since August 2025, and Article 50 transparency since August 2026.

Penalties reach 35 million euro or 7% of worldwide turnover, whichever is higher.

**3.6 — Quiz**
A Singapore retailer launches a chatbot that collects customer contact details
and purchase history to personalise offers. The vendor's product follows the
Model AI Governance Framework and displays an AI info card. The retailer has
published nothing about how it uses customer data. Where is the exposure?

A. Covered. The Model Framework and the info card address transparency.
   → Both are voluntary. IMDA's own framework says adopting it "will not absolve
   organisations from compliance with current laws and regulations."
B. ✓ The PDPA applies regardless, and voluntary measures do not discharge it.
   → The PDPA is binding law. PDPC's advisory guidelines interpret it. The Model
   Framework sits in a different tier and does not displace either.
C. Reputational only, since Singapore has no AI statute.
   → Singapore has no AI statute, and that changes nothing here. The PDPA binds
   whether or not AI is involved.

### S4 · Where enforcement actually is  (4 min · target 440)

**4.1 — What produced real consequences**
The Dutch tax authority used nationality as an indicator in a risk-classification
model. The regulator found that unlawful and discriminatory, and fined it 2.75
million euros. At least 244,273 people were affected. More than 43,000 are now
recognised as victims, each receiving at least 30,000 euros. The cabinet resigned
in January 2021.

Australia's Robodebt scheme asserted 1.763 billion Australian dollars of debt
against roughly 433,000 people. A judge called it "a massive failure of public
administration."

Italy fined Deliveroo 2.5 million euro and Glovo 5 million over rider-management
algorithms, where a suspended rider "received an automatic message without any
possibility of providing explanations or contesting the decision."

None of these turned on how accurate the model was. All three turned on whether a
person could argue with the decision.

**4.2 — The headline AI fines mostly did not survive**
Italy fined OpenAI 15 million euro; a Rome court annulled it in March 2026 on
jurisdiction, without examining the substance. Italy fined Clearview AI 20
million euro, never collected. The UK fined Clearview 7.55 million pounds in
2022, still unadjudicated on the merits four years later. New York City's
hiring-audit law turned up one compliance issue across 32 companies surveyed.

Annulled, uncollected, undecided, barely detected. Plan against the pattern in
4.1, not against the headlines.

**4.3 — And the ones with no regulator at all**
Air Canada's chatbot gave a passenger the wrong advice on bereavement fares. The
airline argued that the chatbot was "a separate legal entity that is responsible
for its own actions." The tribunal called that "a remarkable submission." It
awarded 812 Canadian dollars. The sum is small. The principle is not.

Zillow's home-pricing model was confidently wrong. The company wrote down 304
million United States dollars in a single quarter and cut roughly 25% of its
staff. No regulator was involved.

Accuracy is not irrelevant. Zillow was a forecasting failure and Air Canada was
wrong information. It is just never the whole question.

**4.4 — Quiz**
A rider-management algorithm assigns shifts. An audit shows it is accurate and
well calibrated. Suspended riders receive an automated message. They can appeal,
and the appeal re-runs the same algorithm. Which change addresses the governance
gap?

A. Improve the model's accuracy further.
   → Accuracy was not the finding in the Italian rider cases. A well-calibrated
   model that cannot be contested still fails.
B. Publish a fuller explanation of how the algorithm works.
   → Explanation helps, and it is not what was missing. The finding turned on the
   absence of any route to contest. An explanation a rider cannot act on is not
   a route.
C. ✓ Give a person the authority to overturn the decision.
   → Foodinho's riders got "an automatic message without any possibility of
   providing explanations or contesting the decision." An appeal that re-runs the
   same algorithm is not a review.

### S5 · The sector layer: financial services  (4 min · target 440)

**5.1 — Sectors add a layer**
Everything so far applies whatever business you are in. Your sector adds to it.

In Singapore, MAS published FEAT in 2018: fourteen principles on fairness,
ethics, accountability and transparency. It is advisory. MAS files it as an
Information Paper, which its own hierarchy does not list as a regulatory
instrument at all.

MAS consulted on Guidelines on AI Risk Management in November 2025 and proposed a
twelve-month transition after issuance. As at September 2026 they have not been
issued, so the transition has not started.

**5.2 — The UK answered the same question differently, and arrived at the same place**
The FCA was asked whether it would write AI rules. It said no. Its Chief Data,
Information and Intelligence Officer told the Treasury Committee in January 2026
that the Senior Managers regime and the Consumer Duty together give the regulator
"enough regulatory bite that we don't need to write new rules for AI."

So who owns AI risk in a UK regulated firm? Somebody already does. Responsibility
follows the activity, business area or function: technology systems normally sit
with the Chief Operations function, risk controls with the Chief Risk function.

The FCA considered creating a dedicated AI Senior Manager and decided against it,
on the basis that existing governance already reached the problem.

**5.3 — What travels beyond finance**
Your sector regulator probably already has a view, and it probably is not written
in a document with "AI" in the title.

And the absence of an AI-specific rule does not create an absence of an owner. If
nobody in your organisation can be named, that is a finding about your
organisation rather than about the regulation.

**5.4 — Quiz**
A bank is launching a credit-decisioning tool built by a vendor. The vendor says
the model is tested and monitored. The business sponsor says the vendor is
accountable for model performance. The risk function says nobody has asked it to
review anything. Who must own this before launch?

A. The vendor. It built the model and monitors it.
   → FEAT Principle 8: firms are "accountable for both internally developed and
   externally sourced AIDA models." Outsourcing the build does not outsource the
   accountability.
B. ✓ A named senior manager inside the bank, with the risk function's review done.
   → Responsibility follows the activity and the function. The FCA declined to
   create an AI-specific role precisely because an existing owner already holds it.
C. Nobody yet. No AI-specific rule requires an owner before launch.
   → The absence of an AI rule is not an absence of an owner. FEAT, the Senior
   Managers regime and the Consumer Duty all attach to the firm regardless.

### S6 · Three questions, and the one that decides  (5 min · target 550)

**6.1 — Three questions**
Few executives have time to assess every AI proposal properly. Most have time for
three questions.

Who is accountable when this is wrong, and what is their name?
How does a person affected by this contest what it decided?
What have we told customers this does?

**6.2 — Where each one comes from**
Each comes from a case you just saw.

Accountability: FEAT Principle 8 makes firms accountable for externally sourced
models as well as their own. A third of AI use cases in UK financial services
arrive through third parties.

Contestability: the Dutch, Deliveroo and Foodinho findings all turned on whether
a person could argue with a decision.

Disclosure comes from Air Canada, and from the first AI-washing settlements
brought by the SEC in 2024. Two advisers paid 400,000 United States dollars
between them for claiming to use AI that they were not using.

One caution on the third. A New York regulator reviewed roughly 400,000 Apple
Card applications. It found no discrimination by Goldman Sachs or Apple, and both
could explain every complainant's decision when asked. The public criticism
continued anyway. Being able to explain a decision will protect a firm in a
regulator's assessment. On its own, it will not protect its reputation.

**6.3 — The question that actually decides**
A firm can obtain satisfactory answers to all three and still approve a system
with no evidence that it works.

A fourth question closes that gap. What evidence would justify approving this,
restricting it, or stopping it?

Four things make up that evidence. It has been tested in the setting where it
will run, not on the vendor's benchmark. A person can intervene, and has the
authority to overrule it. Monitoring would show if it had drifted. And a stop or
rollback exists that somebody has actually tried.

Singapore's agentic AI framework states the hard line: systems "should not allow
high stakes or irreversible actions to take place without human review."

Note what that does and does not say. It does not prohibit autonomy. It prohibits
autonomy where the action cannot be undone.

**6.4 — Back to the chatbot**
Return to the decision put to you 25 minutes ago.

The supplier follows a voluntary framework. That answers none of the four
questions. Ask these instead. Whose name is on this? How does a customer dispute
what it told them? What does your marketing claim it can do? And what happens
when it is confidently wrong at two in the morning on a Saturday?

**6.5 — Quiz**
An AI tool flags insurance claims for manual review. It has a named accountable
owner, a published appeals process, and accurate marketing copy. It has been
tested on the vendor's benchmark dataset. There is no monitoring in production
and no rollback plan. Approve, restrict, or stop?

A. Approve. Accountability, contestability and disclosure are all in place.
   → Those three are necessary and not sufficient. None of them tells you whether
   it works in your setting.
B. ✓ Restrict. A limited pilot with monitoring and a rollback, then reassess.
   → The gap is evidence, not governance paperwork. A bounded pilot produces what
   a vendor benchmark cannot.
C. Stop. It cannot be deployed without production monitoring.
   → Defensible, and disproportionate here. The action is a flag for human
   review, which is neither high-stakes nor irreversible. Reserve stopping for
   decisions that are.

### S7 · Your next 90 days  (7 min · target 770)

**7.1 — The one case that ended well**
In 2021 a rejected credit-card applicant asked HSBC Singapore for the
algorithmically generated scores behind the refusal. HSBC declined. Singapore's
Deputy Commissioner agreed the bank was entitled to decline, because the scores
were evaluative opinion data. The law settled that.

Then he went further than he needed to. HSBC "had acted reasonably by providing
information about how it uses data and technology to conduct credit facility
assessments. From the perspective of accountability and disclosure of policies
and practices, HSBC had acquitted itself."

He was pointing at two documents HSBC had published: a Principle for the Ethical
Use of Big Data and AI, and a Credit Decisioning Policy Statement.

Read that precisely. The publications did not win the case. What they did was let
a regulator satisfy itself quickly that the organisation was in control. It is
the cheapest item on the next slide, and the only one with a regulator's
endorsement attached.

**7.2 — Four things, in this order**
Inventory. You cannot govern what you cannot list, and the list should include
what people are already using without asking.

Name an owner for each consequential use. A person, not a committee, not a
vendor.

Build a contest path for anything that affects a customer or an employee. A route
to a human with authority to overturn the outcome.

Put AI terms into procurement. A third of use cases arrive through suppliers, and
FEAT Principle 8 makes you accountable for those too.

**7.3 — Write it down as five fields**
A list of four good intentions is not a plan. Pick your highest-consequence use
and fill in five fields. If you cannot fill them, that is the output.

Use case. Accountable owner, by name. What a person affected can do about it.
What evidence says it works here. Next decision, and by when.

Worked example. Automated triage of customer complaints.
Owner: the Head of Customer Operations, named, not the vendor.
Contest path: none today; complaints escalated by the tool are never re-read by a
person before closure.
Evidence: vendor benchmark only; never tested on our complaint mix.
Next decision: whether to restrict to a pilot, by the end of this month.

That record took four lines and produced two findings and a deadline. Do it for
your top three uses and you have the foundation of your governance programme.

**7.4 — What can usually wait**
Usually secondary to closing a live control gap: ISO 42001 certification,
assurance tooling, and a dedicated AI function or Head of AI Governance.

"Usually" is carrying weight there. Certification becomes urgent when a customer
contract requires it, when a procurement process scores it, or when your
organisation is large enough that ad-hoc ownership stops scaling. These are
contextual choices, not permanently wrong ones.

One caution. No public figure exists for how many organisations hold ISO 42001.
The body that compiled certification statistics ceased operations in January
2026. If a vendor quotes you an adoption number, ask where it came from.

**7.5 — Quiz**
A firm finished its AI inventory last month: 31 use cases, with named owners for
the 6 it considers consequential. Next week it plans to switch on a tool that
automatically declines low-value insurance claims. No appeals route has been
designed and there is no monitoring. The board has asked about ISO 42001
certification. What comes first?

A. Start ISO 42001 certification. It answers the board and reassures customers.
   → Certification is usually secondary to closing a live control gap, and it
   takes months. The deployment is next week.
B. ✓ Design the appeals route and the monitoring before the tool goes live.
   → An automatic decline affecting customers with no route to contest is the
   pattern behind the Dutch, Deliveroo and Foodinho findings. The inventory is
   done; this is the gap it revealed.
C. Extend the inventory to name owners for all 31 use cases.
   → Worth doing, and not what is about to go wrong next week. The inventory has
   already surfaced the thing that needs attention.

**7.6 — Start here**
Start with the inventory. Everything else on the list depends on knowing what you
have.

