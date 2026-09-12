---
title: AI Value Management
series: ai-for-business-leaders

template: course
theme: corporate-clean
themes: corporate-clean,minimal-white,swiss-grid,academic-paper,course-warm
lang: en
delivery: recorded     # presenter-led | self-paced | recorded  (gate 1)
rate: 135          # EFFECTIVE wpm. Raw spoken EN is ~150, but a recorded module spends real time on diagram beats and quiz pauses that carry no words. 30 x 135 = ~4,050. Budget 4,000.
duration: 30       # minutes
accepted_hash:     # set at gate 3; a mismatch means index.html has diverged
---

# AI Value Management

Series: [`ai-for-business-leaders`](../ai-for-business-leaders.md). Audience and
terminology are inherited from there; what follows is what is specific to this
Course.

## Audience & outcomes

**Audience.** Business leaders — executives and senior decision-makers, not
practitioners. Inherited from the Series. They approve AI spend, answer to a
board, and carry the risk.

**Scope.** Why the value is not realised. The pilot-to-production gap, benefits
that never reach the P&L, and measured returns that disappoint. Diagnostic first,
then what to do about it. **Out of scope:** how to build a business case from
scratch, vendor selection, and model economics below the level of a budget line.

**Delivery.** Recorded voiceover, 30 minutes. Narration is a **script read over the slides. It does not render in the deck.** Slides carry the visual beat only,
and every quiz is a presenter beat: the narrator poses it, pauses, then answers.
Nothing on a slide has to be silently readable, and nothing in the Narration can
be assumed visible to the learner.

> This is the one input the Series does not share. `ai-governance-overview` is
> self-paced and puts its teaching content on-slide. Do not copy slide shapes
> across without re-checking where the words live.

### Outcomes

After 30 minutes, a business leader can:

1. Say **which stage** their own AI spend is stuck at, rather than that "AI is
   hard", and know that the stages fail for different reasons and take different
   fixes.
2. Explain why a model that works does not move a P&L line, and name the work in
   between: process redesign, adoption, and shutting down the path the AI
   replaced.
3. Refuse to fund a use without a **baseline** and a named **benefit owner**,
   because a benefit nobody measured beforehand cannot be claimed afterwards.
4. Decide what to stop and what to concentrate on in the next 90 days.

Outcome 4 is what makes this a course for executives rather than a briefing.
Without it they leave informed and idle. Outcome 3 will meet resistance
because it slows funding, so the Narration has to earn it.

## Research Plan

<!-- APPROVED 2026-09-12. Revised twice on Ray's direction: open on the 95%
     figure, research attribution properly, and centre the Stanford GenAI
     Playbook. Agents dispatched. -->

The Series brief covers regulation and nothing about value, so this is a full
research pass, not a gap-fill.

**Anchor text.** Ray asked for the **Stanford GenAI Playbook** as the spine, and
for worked examples drawn from it. So a Finding from the playbook outranks a
survey percentage when the two cover the same ground: a named example an
executive can picture beats a number they will forget. First research job is
establishing what the playbook actually is and what examples it carries, since
several Stanford artifacts could answer to that name. If its examples are thin
or it turns out to be advisory rather than evidenced, that constrains how much
weight it can take, and the Outline has to say so.

**The course opens on "95% of AI pilots fail" and asks why.** That is the
provocation, so the figure carries more weight than any other number here and
gets the most exacting treatment: its primary, its sample, what it actually
counted, and what its authors say the causes were. Quoting what it measured is
what lets the narration ask "why" rather than repeat a number secondhand.

### Questions

| # | Question | Why the course needs it |
|---|---|---|
| Q1 | The 95% claim: what is the primary source, what was the sample and method, and what exactly did it count as failure? | The opening beat. If the figure is softer or narrower than its reputation, the narration says so and the provocation gets sharper, not weaker |
| Q2 | **Why do they fail?** The stated causes, ranked, separating what companies self-report from what researchers observed | The course's spine. Outcome 1 is a stage diagnosis, and the stages come from here |
| Q3 | Do other primaries agree? Competing shares for production rate and for reported P&L impact | If credible surveys disagree by 40 points, that disagreement is the Finding and it is more interesting than either number |
| Q4 | **How is value credibly attributed to an AI implementation?** What methods exist (holdout groups, staged rollout, baseline before/after, task-level A/B), what each costs, and what organisations actually do | Ray's flag, and the hard one. Outcome 3 stands on it |
| Q5 | Where value is realised when it is realised: which functions, at what magnitude | Outcome 1 needs stuck-vs-working to be evidence, not assertion |
| Q6 | What organisations reporting financial impact do differently | Outcome 2's causal claim, with its limits stated |
| Q7 | Task-level productivity gains from controlled trials, and whether they aggregate to the firm | The counterweight. Some trials show gains, at least one shows a slowdown, and a course citing only the flattering ones trains over-confidence |
| Q8 | A named company quantifying an AI benefit in its own reporting, plus the cost side that benefit cases omit: integration, change management, running cost | Executives discount survey percentages and believe filings. And a benefit case with no cost case is not a case |

**Q4 may come back empty, and that is a result.** If the honest answer is that
almost nobody attributes value rigorously and most organisations estimate, then
the Finding is the absence, and outcome 3 gets built on it directly: the reason
to demand a baseline before funding is that there is no way to reconstruct one
afterwards. I will not paper over a thin answer here with a tidy framework.

### Source kinds

**Will use.** Primary research reports that publish sample size and method
(MIT Media Lab, McKinsey Global Survey on AI, Deloitte State of Generative AI,
US Census BTOS). Peer-reviewed papers and working papers with a stated design
(NBER, arXiv, METR). Company financial disclosures and earnings transcripts.
Government statistical agencies. For Q4, also measurement and evaluation
methodology from outside AI, where the attribution problem is older and better
studied.

**Will not use.** Vendor blogs, consultancy marketing pages without a method,
and journalism restating a figure whose primary I cannot reach. If a widely
quoted statistic has no reachable primary, the Finding is that it has no
reachable primary.

### Known trap

Every headline percentage in Q1 and Q3 is repeated far more often than it is
read. The rule for all of them, including the 95%: establish the primary and what
it counted, or leave the number out. A course that opens on a misquoted figure
has lost the room before the first outcome.

## Research Brief

<!-- Findings go here as they are established, each with quote and URL. -->

### Anchor document  ✅ researched 2026-09-12

**⚠️ No Stanford artifact is titled "Stanford GenAI Playbook."** Exact-phrase
search, an hai.stanford.edu-restricted search, and the Digital Economy Lab and
Stanford Law publication indexes return nothing under that name. Three real
Stanford documents could be meant:

| | Title | Authors | Publisher | Date |
|---|---|---|---|---|
| **A** | **The Enterprise AI Playbook: Lessons from 51 Successful Deployments** | Pereira, Graylin, **Brynjolfsson** | Stanford **Digital Economy Lab** | Apr 2026 |
| B | Building for Production: A Revised Playbook for Enterprise-Ready Generative AI Solutions | Ma, Mandal | Stanford Law (CodeX) | 5 Aug 2025 |
| C | Getting Beyond the Sandbox: A Playbook for Developing Generative AI Solutions for Enterprise Applications | Mandal, Ma | Stanford Law | 28 Mar 2024 |

**A is the document.** B and C are advisory pieces for product teams building
GenAI features for external customers, with almost no data; A is empirical,
organisational, executive-facing and about why value is or is not realised.
https://digitaleconomy.stanford.edu/publication/enterprise-ai-playbook/ ·
PDF (116pp) https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf
Page numbers below are the printed footer numbers. **All ST findings are from A
unless marked.**

#### Evidence base and its limits — read before using any percentage

**ST-40 · 51 cases, 41 organisations, interview-based, selected on success.**
> "This research is based on in-depth interviews with executives and project
> leaders who have deployed AI solutions at scale. We focused exclusively on
> initiatives that have moved beyond pilot stage and are delivering measurable
> business value."
> "Our 51 case studies draw from 41 organizations, 7 countries, 5 regions,
> representing over a million employees."
One structured 60-minute interview per company minimum, plus internal metrics and
project documents. Methodology, pp.7–8.

**ST-41 · The authors disclaim representativeness in writing. Quote this if the
course cites any ST percentage.**
> "We want to be transparent that this does carry a known limitation: selection
> bias toward positive outcomes. Our findings describe what success looks like
> and what it took to get there; we don't claim to provide representative data on
> how common success is across the broader economy."
p.6. So "45% cut headcount" means 45% of 51 **successful** deployments, never 45%
of enterprises. Every ST percentage is a denominator of successes.

**ST-32 · Self-reported outcomes. No control group, no counterfactual.**
> "This research relies primarily on self-reported data from interview
> participants. While we triangulated information where possible and focused on
> mature initiatives with documented outcomes, readers should consider potential
> selection bias toward successful deployments."
Limitations, p.10.

**ST-17n · Every company is anonymised, by disclosure agreement. Unobtainable.**
> "All data was anonymized and aggregated to protect proprietary information and
> follow subject company disclosure policies. Specific company names and
> identifying details have been removed or generalized."
p.10. Named entities in the report are vendors and models only (Azure OpenAI,
GitHub Copilot, Cursor, Claude, Gemini, Bedrock, MCP). **Examples must be cited
as "a $1B+ US logistics company", never as a guess at which one.**

**ST-DISC · Author interest to disclose if the course leans on the measurement
argument.** Brynjolfsson "puts his academic insights to practical use via
Workhelix, a company he co-founded to identify and measure the benefits of AI"
(contributor bio, p.3). A measurement-vendor interest sits beside ST-29/ST-30.

**ST-42 · ⚠️ The stated data-collection window contradicts itself three ways.**
p.8 says "Aug. '25 and Feb. '26"; p.76 says "August 2024 to January 2025"; p.56
says "through early 2025". **Never put a collection window on a slide.**

**ST-43 · Much of what reads as Stanford statistics is other people's survey data,
labelled "Published Findings" per chapter.** Attribute these to their owners, not
to Stanford: Accenture "80-85% of companies are stuck in a 'Proof of Concept
Factory' stage" (p.13, 1,500 C-suite, 2019); McKinsey "55% of high performers
redesigned workflows around AI versus only 20% of other companies" (p.20);
Deloitte Jan 2026, n=3,235 director-to-C-suite, "74% of organizations hope to
grow revenue through AI, but only 20% are doing so today" and "only 6% of
organizations report EBIT impact above 5% from AI" (p.59); "62% of organizations
are experimenting with AI agents, but only 23% are scaling them" (p.68).

#### The central claim

**ST-1 · The organisation is the constraint, not the model. The course's thesis,
in the authors' words.**
> "Across 51 enterprise cases over 5 months, we found stories of transformation
> measured in weeks and others measured in years. Same technology, same use cases,
> vastly different outcomes. The difference was never the AI model. It was always
> the organization. Its readiness, its processes, its leadership, its willingness
> to change and fail."
Foreword, p.2.

**ST-4 · 77% of the hardest challenges were non-technical.**
> "77% of the hardest challenges practitioners faced were invisible costs: change
> management, data quality, and process redesign, not technical issues.
> Technology was consistently described as the easiest part."
Ch.1, p.13. Supporting, p.14: "All the hard work is in process documentation and
data architecture. If you can do those two things, everything else is quite
simple." — Executive, Telecom Company

**ST-36 · Same use case, weeks versus years. The accountability moment.**
> "A large fintech used an AI coding agent to migrate millions of lines of legacy
> extract, transform, load (ETL) code to a modern architecture. The project took
> weeks. A technology company redesigned their customer support system with AI
> and launched in six months. A major bank attempting the same customer support
> use case reports that projects take multiple years."
> "It takes us multiple years just to even stand one of these things up." —
> Executive, Financial Services
Ch.2, p.21. Accelerators, p.22: Executive Sponsorship 43% · Building on Existing
Foundation 32% · End User Willingness 25%. Delays, p.23: Learning Curve 25% ·
Data Quality 21% · Regulatory/Compliance 21% · Process Documentation Gaps 21%.

**ST-38 · Applying AI to an unfixed process is the failure mechanism.**
> "Fix the process before applying AI. AI amplifies whatever process it is
> applied to. If the process is broken, AI makes it worse faster."
p.27. And p.73: "Don't just apply AI to your existing processes. That's a
mistake. We're redesigning our workflow and that's what makes us successful." —
Head of Operations, Technology Company

#### Why efforts fail — the report's own taxonomy

**ST-35 · Six root causes, with case percentages. Note the first sentence: the
symptoms executives name are not the causes.**
> "Common symptoms like 'projects stuck in pilot' or 'inability to prove ROI'
> appeared frequently, but these are consequences, not causes."

| Root cause | % of cases |
|---|---|
| The organization wasn't ready to adopt | 35% |
| Critical knowledge was never captured or stored | 27% |
| Legal or compliance teams blocked the project | 18% |
| Technology broke or wasn't mature enough | 16% |
| Wrong problem chosen or unrealistic expectations set | 14% |
| Talent or sponsorship gap | 12% |

Appendix, pp.110–111. Remedies verbatim include "Secure visible CEO mandate tied
to OKRs", "Engage legal early as partners, not last minute gatekeepers", "Map
processes end to end and find real bottlenecks first", "Set expectations that
most AI projects fail on the first attempt".

**ST-5 · 61% of the successes sat on top of a prior failure whose cost never
entered the ROI.**
> "61% had a failed AI project before their current success […] These failed
> experiments are sunk costs that may never appear in the successful project's
> ROI but were often essential to it. The failures share a pattern: teams treated
> AI as a technology project instead of a process and change management project."
Ch.1, p.15. The Foreword gives a company-level figure alongside it: "Two thirds
of the companies we investigated had significant failed attempts prior to
achieving value creation" (p.6).

**ST-31 · The budgeting implication, stated by the authors.**
> "The implication for budgeting: the true cost of a successful AI deployment
> usually includes at least one failed attempt, and the bulk of the investment
> goes to everything except the model."
p.15. Macro basis, p.13: "for every $1 of tangible tech investment, companies
spend up to $10 on intangibles (process redesign, reskilling, organizational
transformation), initially depressing productivity before gains are realized."

**ST-9 / ST-10 · Resistance comes from staff functions, and fear of replacement
is the *least* common cause. Counterintuitive, and good for a quiz.**
> "Staff functions (Legal, HR, Risk, Compliance) were the most frequent source of
> resistance at 35%, not the AI end users." (Ch.5, p.45; p.11 adds "ahead of
> internal end-users at 23%")
> "Frontline workers fear replacement. This is the most discussed concern but
> appeared in only two cases." (p.47)
p.46 notes IT is an exception: "rather than blocking, they more often serve as
enablers."

**ST-34 · Demanding ROI proof is itself listed as a source of resistance.**
> "C-Level demands ROI proof. CFOs require clear financial justification before
> approving AI investments. The solution is measured pilots that demonstrate
> value before asking for broader investment."
p.47. Same page: "Hospital C-suite executives need direct line-item impact on
balance sheet to justify software purchases."

**ST-37 · Every success was iterative. None were waterfall.**
> "Of cases where we could identify the development methodology, all used an
> iterative approach. None used traditional waterfall planning."
> "Probably 90% of the pilots and tests fail, but then we iterate on those until
> we find them and it grows and grows." — Executive, Food Delivery Company
p.24. Related, p.40: "73% of implementations started small deliberately, and 63%
framed their pilots explicitly as experiments"; "in none of the cases we examined
was anyone punished for a failed AI initiative."

#### Levers a leader actually controls

**ST-8 · Sponsorship has four levels, and only the top one produced org-wide
change.**
> "1 Passive Approval […] 2 Periodic Oversight — Monthly reviews, removes
> blockers when escalated, reactive. 3 Active Steering — Weekly check-ins,
> proactively removes blockers, involved in decisions. 4 Strategic Integration —
> AI in corporate OKRs, incentives tied to adoption, culture change."
> "the seven cases that achieved organization-wide transformation all reached
> strategic integration"
Distribution: Periodic 12% · Active Steering 58% · Strategic Integration 29%.
Ch.4, p.37. Sponsor activities, p.38: Resource Allocation 59% · Strategic
Integration 49% · Org Communication 32% · Blocker Removal 20%.

**ST-6 / ST-7 · Oversight model tracks with gain size — with the authors' own
confound attached.**
> "Escalation-based models (AI handles 80%+ autonomously, humans review
> exceptions) delivered 71% median productivity gains versus 30% for approval
> models. This may, in part, reflect different types of tasks addressed."
p.11. Definitions, p.30. By function, p.31: IT Operations/Escalation 90% ·
Customer Support/Escalation 71% · Claims Processing/Escalation 50% · Field
Service/Approval 80% · Clinical Documentation/Approval 66% · Coding/Collaboration
54%.

**ST-33 · The hedge, verbatim. Do not let the narration upgrade this to causation.**
> "This partly reflects task selection: the escalation model is typically applied
> to high volume, recoverable tasks, while approval and collaboration models serve
> regulated or high stakes work."
Ch.3, p.29.

**ST-11 · Headcount reduction is the largest single outcome but a minority.**
> "Reduction is the most common outcome at 45%, but not the majority. The combined
> alternatives (hiring avoided, no reduction, redeployment) account for 55% of
> cases in aggregate."
Ch.6, p.52. Caveat, p.56: "The 45% reduction rate we observed may represent a
floor, not a ceiling."

**ST-14 · Only 6% had AI-ready data, and that did not stop them.**
> "Only 6% of implementations had data that was fully ready for AI. But in the
> majority of cases where data challenges existed, LLMs were part of the solution
> […] Models unlocked previously inaccessible data in 88% of cases"
Ch.9, p.79. p.82: "59% had data scattered across multiple systems owned by
different teams. Only 16% had fully centralized data. Yet success did not require
centralization. It required access."

#### Measurement — the spine of outcome 3

**ST-12 · Revenue gains are rare, and the binding constraint is measurement, not
capability.**
> "What distinguishes these cases is not the technology. It is that someone
> measured the revenue side, not just the cost side."
Ch.7, p.60. p.62: "What these cases share is not a common technology stack or
industry. It is that someone asked a question beyond 'how do we reduce cost?' and
measured the answer."

**ST-29 · KPIs before deployment, and the trap of measuring only headcount.**
> "Organizations that define clear KPIs before deployment are significantly more
> likely to demonstrate value and secure continued investment. Yet many teams
> default to a narrow set of efficiency-focused metrics — often measured by
> headcount reduction — while overlooking indicators of quality, customer value,
> and revenue growth that often prove more sustainable and impactful over time.
> We all know the saying, you get what you measure, and with AI enabled projects,
> this is especially true."
Appendix, p.108.

**ST-30 · A function-by-function KPI menu. The most directly usable executive
asset in the document.**
> "These are not theoretical frameworks. Every KPI and every failure mode below
> was reported by at least one of the 51 implementations in our sample."
Thirteen functions, pp.108–109. Verbatim examples: Customer Support —
"Self-Service Resolution Rate — Share of AI-deflected interactions that are
actually resolved, not just deflected"; Engineering — "New Product Offerings —
New or unplanned products that emerge from AI implementations"; IT Operations —
"Staff-to-System Ratio — Number of humans required to manage AI-automated systems
or robots"; Healthcare — "Coding Accuracy Rate — Agreement between AI-suggested
billing codes and doctor-approved codes."

**ST-3 · The report's five imperatives, under its own heading "The playbook that
emerges from data."**
> "Start with the invisible and intangible work. Process documentation, data
> access layers, and change management are not overhead tacked on to the real
> work. They often are the real work. […] Invest in measurement. Clear KPIs
> should be identified before deployment. […] Save everything. […] Build a
> multi-model architecture from day one. […] Plan for agentic AI."
Conclusion, pp.106–107.

**ST-2 · There is no staged maturity model in this document.** The structure is
11 diagnostic questions, one per chapter (Contents, p.4), including "Why do AI
business cases underestimate real investment?", "How to cross the valley of death
between deployment and ROI?", "What separates sponsors who drive results from
those who just approve budgets?", "Where does fatal resistance come from?".
**If the Outline uses stages, they are ours, built from ST-35, and must be
labelled as ours.**

**ST-39 · The 95% figure is MIT NANDA's, cited by the playbook as its
motivation. The two sources fit together; the attribution must be right.**
> "Despite billions in enterprise AI spending, a 2025 study from MIT's NANDA
> initiative concluded that 95% of generative AI pilot programs fail to produce
> measurable financial impact. [7] They argued that the failures stem not from
> model quality but from poor workflow integration and misaligned organizational
> incentives."
p.6; endnote [7], p.115: MIT NANDA Initiative, "The GenAI Divide: State of AI in
Business 2025," July 2025. **Never attribute the 95% to Stanford.**

#### The 95% figure  ✅ researched 2026-09-12

The opener. Every claim here is load-bearing, so the whole audit is recorded.

**F-1 · The primary exists and is identified.** *The GenAI Divide: STATE OF AI IN
BUSINESS 2025*, MIT NANDA — Challapally, Pease, Raskar, Chari. July 2025.
Research period January–June 2025. 26 pages.
Archived canonical: http://web.archive.org/web/20250818145714if_/https://nanda.media.mit.edu/ai_report_2025.pdf
Verified mirror: https://cloudelligent.com/wp-content/uploads/2026/02/v0.1_State_of_AI_in_Business_2025_Report.pdf
Both were text-extracted and matched on distinctive strings; the mirror is
faithful. PDF metadata: created by Aditya Challapally, 13 July 2025.

**F-2 · ⚠️ The canonical MIT URL no longer serves the report.**
`https://nanda.media.mit.edu/ai_report_2025.pdf` returns `302 Found` to
https://www.media.mit.edu/groups/nanda/overview/ — a sponsorship page that does
not mention "The GenAI Divide" or "State of AI in Business 2025" anywhere.
Distribution is now via a Google Form. Verified 12 Sep 2026. **The most-cited
enterprise-AI statistic of 2025–26 has no live citable primary at its publisher.**
It survives as archive snapshots and third-party mirrors.

**F-5 · What it actually measured: 95% of ORGANISATIONS get zero return. Not 95%
of pilots.**
> "Despite $30–40 billion in enterprise investment into GenAI, this report
> uncovers a surprising result in that 95% of organizations are getting zero
> return. Just 5% of integrated AI pilots are extracting millions in value, while
> the vast majority remain stuck with no measurable P&L impact."
The funnel for task-specific GenAI: **Investigated 60% → Piloted 20% →
Successfully Implemented 5%.**
> "Sixty percent of organizations evaluated such tools, but only 20 percent
> reached pilot stage and just 5 percent reached production."

**F-5b · On the report's own numbers the pilot failure rate is 75%, not 95%.**
5 of 20 that piloted reached production. The 95% denominator is all
organisations. The report's general-purpose LLM funnel runs 80% → 50% → 40% and
it concedes "Generic LLM chatbots appear to show high pilot-to-implementation
rates (~83%)". **Arithmetic, not a claim the report makes.** Mark as derived.

**F-6 · The misquote starts inside the primary.** Immediately after the funnel:
> "The 95% failure rate for enterprise AI solutions represents the clearest
> manifestation of the GenAI Divide."
So the slide from "95% of organisations get zero return" to "95% failure rate"
originates in the document, not only in the press.

**F-3 · Sample: a convenience sample with no frame.**
> "This report is based on a multi-method research design that includes a
> systematic review of over 300 publicly disclosed AI initiatives, structured
> interviews with representatives from 52 organizations, and survey responses
> from 153 senior leaders collected across four major industry conferences."
No frame, no response rate, no weighting. The four conferences are never named.
Its own stated limits:
> "Organizations willing to discuss AI implementation challenges may
> systematically differ from those declining participation, potentially creating
> bias toward either more experimental or more cautious adopters"
> "Six-month observation period may be insufficient to fully assess 'successful
> deployment' for complex enterprise systems, potentially understating success
> rates for longer-term implementations"

**F-4 · Two incompatible definitions of success, and the looser one governs the
95%.**
> A (research note under the funnel, the one that produces the figure): "We
> define successfully implemented for task-specific GenAI tools as ones users or
> executives have remarked as causing a marked and sustained productivity and/or
> P&L impact"
> B (appendix 8.2): "Success defined as deployment beyond pilot phase with
> measurable KPIs."
A turns on whether somebody *remarked*. B turns on measured KPIs.

**F-9 · Self-labelled preliminary, with MIT institutional backing disclaimed.**
> "Preliminary Findings from AI Implementation Research from Project NANDA"
> "Disclaimer: The views expressed in this report are solely those of the authors
> and reviewers and do not reflect the positions of any affiliated employers."
No peer review, journal or DOI claimed anywhere.

**F-7 · The best-known write-up misstates the method.** Fortune, 18 Aug 2025,
headline "MIT report: 95% of generative AI pilots at companies are failing",
describes the research as
> "based on 150 interviews with leaders, a survey of 350 employees, and an
> analysis of 300 public AI deployments."
The report says 52 organisations and 153 **senior leaders**. "150 interviews" and
"350 employees" appear nowhere in it.
https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
**Three separate errors in the popular framing:** denominator (organisations, not
pilots) · unit (zero measurable P&L return, not "failed") · the circulating
method description is wrong about n and about who was asked.

**F-8 · What the report says the cause was — a learning gap, not the usual
suspects.** Directly usable, and it agrees with ST-1.
> "The core barrier to scaling is not infrastructure, regulation, or talent. It is
> learning. Most GenAI systems do not retain feedback, adapt to context, or
> improve over time."
> "Most fail due to brittle workflows, lack of contextual learning, and
> misalignment with day-to-day operations."
Its four patterns: "Only 2 of 8 major sectors show meaningful structural change" ·
"Big firms lead in pilot volume but lag in scale-up" · "Budgets favor visible,
top-line functions over high-ROI back office" · "External partnerships see twice
the success rate of internal builds".
Barriers were **scored, not measured**:
> "Research Note: These scores reflect reported frequency rather than objective
> measurement of barrier impact"
Ranked most to least frequent: unwillingness to adopt new tools · model output
quality · poor user experience · lack of executive sponsorship · change
management. Budget skew, from a hypothetical $100 allocation exercise: "Sales and
marketing functions captured approximately 70 percent" — though the section
takeaway says 50%, an internal inconsistency. On build-vs-buy the report warns
against the causal reading it is usually quoted for:
> "The correlation between external partnerships and success does not
> necessarily prove causation."

### Rival primaries  ✅ researched 2026-09-12

**F-10 · McKinsey 2026 · n=1,719 · 37% report any EBIT impact, ~6% are high
performers, and the number has not moved.** *The state of AI in 2026: On the road
to ROI*, 25 Aug 2026, field 4 May–8 Jun 2026.
https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
> "Thirty-seven percent of respondents attribute at least some EBIT impact to AI
> use (about the same share as last year). And the proportion of AI high
> performers (those who attribute at least 5 percent of EBIT to their use of AI
> and describe the technology's impact as 'significant') has remained flat at
> about 6 percent of all respondents."
> "44 percent now report that AI is scaling across their enterprise, up from 38
> percent a year ago"
**The individual/enterprise gap — the single best quote for outcome 2:**
> "At the individual level, AI is clearly a boon: 80 percent of survey
> respondents say it has improved their productivity and half say it helps them
> make better decisions. Yet, only 37 percent of organizations report any
> positive EBIT contribution, essentially flat compared with last year."
Weighting caveat: "the data are weighted by the contribution of each respondent's
nation to global GDP" — geography only, not business population.

**F-11 · McKinsey 2025 · n=1,993 · 39% any EBIT, two-thirds not scaling.** Field
25 Jun–29 Jul 2025.
> "Nearly two-thirds of respondents say their organizations have not yet begun
> scaling AI across the enterprise."
> "Thirty-nine percent of respondents attribute any level of EBIT impact to AI,
> and most of those respondents say that less than 5 percent of their
> organization's EBIT is attributable to AI use."
⚠️ McKinsey's 2026 text calls 37% "about the same share as last year" when the
2025 published figure was 39%.

**F-12 · Deloitte 2026 · n=3,235 · 25% moved 40%+ of pilots to production. A
threshold statistic, not a production rate.** *The State of AI in the
Enterprise: The Untapped Edge*, 7th ed. Field **Aug–Sep 2025** — older field data
than McKinsey 2026 despite the newer title.
https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
> "only 25% of respondents have moved 40% or more of their AI pilots into
> production. However, the pathway to value appears to be clear and achievable
> for those respondents, with 54% expecting to reach that level in the next three
> to six months."
> "only 30% of organizations are redesigning key processes around AI and 37%
> report only using AI at a surface level with little or no change to underlying
> business processes"
> "74% of organizations hoping to grow revenue through their AI initiatives in
> the future compared to just 20% that are already doing so"
Also: 25% report a "transformative effect", "more than double from a year ago";
66% report productivity/efficiency gains. **The 25% is the share of respondents
clearing a 40% conversion threshold. It cannot be read as a production rate.**

**F-13 / F-14 · US Census BTOS · the only figure with a real sampling frame ·
19.8% of US businesses used AI, as of 3 May 2026.**
https://www.census.gov/library/stories/2026/05/ai-use-businesses.html
> "The BTOS data (December 2025 to May 2026) show that overall AI usage hovered
> between 17% and 20%"
> "As of May 3, 2026, the AI use rates in the Information (39.7%) and Finance and
> Insurance (33.9%) sectors were both higher than the national rate (19.8%)"
Size gradient: 37% at 250+ employees · 32% at 100–249 · "Less than 20% of firms
with four or fewer employees". Method: ~1.2M businesses sampled annually from the
2023 Business Register, six biweekly panels, nonresponse-weighted (NAF1/NAF2).
⚠️ Two caveats Census states itself: "the BTOS response data are not subjected to
editing", and BTOS is filed under **Experimental Data Products**.
⚠️ **A wording change breaks the series.** On 17 Nov 2025 the question moved from
AI use "in producing goods or services" to "in any business function". Pre- and
post-Nov-2025 figures are not measuring the same thing.

**F-15 · S&P Global / 451 Research · n=1,006 · 42% abandoned the majority of AI
initiatives, up from 17% year over year; 46% of projects scrapped.** *VotE: AI &
Machine Learning, Use Cases 2025*, 30 May 2025.
https://www.spglobal.com/market-intelligence/en/news-insights/research/ai-experiences-rapid-adoption-but-with-mixed-outcomes-highlights-from-vote-ai-machine-learning
> "The percentage of companies abandoning the majority of their AI initiatives
> before they reach production has surged from 17% to 42% year over year, with
> organizations on average reporting that 46% of projects are scrapped between
> proof of concept and broad adoption."
> "46% reported that no single enterprise objective had seen a 'strong positive
> impact' from that investment"
⚠️ Internal tension in one survey: 46% report no *strong* positive impact on any
objective, yet 76% report positive impact on revenue-growth objectives.
"Positive" and "strong positive" are different bars.

**F-16 · Why the numbers disagree: unit substitution, not measurement error.**

| Figure | Unit of analysis | Source |
|---|---|---|
| 95% zero return | **organisations** | NANDA |
| 75% pilot failure | **pilots** (derived, 5 of 20) | NANDA funnel arithmetic |
| 42% abandoned majority | **companies** | S&P |
| 46% scrapped | **projects** — the only project-level figure here | S&P |
| 25% | **respondents clearing a 40% threshold** | Deloitte |
| 63% not scaling | **stage of maturity**, not failure | McKinsey 2026 |

**The defensible executive claim is not "95% of pilots fail."** It is that only
single-digit to low-double-digit percentages of organisations can evidence
material bottom-line impact, and that has not moved in a year: McKinsey 37% any
EBIT and ~6% at 5%+ of EBIT; Deloitte 20% already growing revenue; S&P 46% with
no strong positive impact on any objective. **This is where four independent
primaries with different methods actually converge**, and it is a stronger
opening than the headline number it replaces.

On adoption the spread is ~70 points (BTOS 19.8% vs McKinsey "nearly nine in
ten"), and that is population, not error. BTOS counts businesses including
millions of firms with four or fewer employees; McKinsey and Deloitte count
professionals who answered a survey about AI, Deloitte's screened for "direct
involvement in their companies' AI initiatives". BTOS reproduces the gap
internally: 19.8% nationally, 37% at 250+ employees.

**F-NM · ⚠️ Every figure above is a self-report, BTOS included.** No primary
located audits financial statements or deployment inventories. **This is the
bridge into outcome 3** — the measurement problem is not only inside companies,
it is in the evidence base the whole debate runs on.

#### NOT ESTABLISHED — 95% and rivals

1. The four industry conferences behind NANDA's 153 responses. Never named.
2. NANDA's response rate, geography, or industry composition.
3. The 300+ public initiatives NANDA reviewed. No appendix, no criteria.
4. NANDA's bootstrap confidence intervals — claimed in the appendix, never reported.
5. A live publisher-hosted copy of the NANDA report (verified 12 Sep 2026).
6. Any MIT institutional statement, retraction or revision. Only "v0.1" located.
7. Whether NANDA's 5% denominator is all organisations or the 60% that evaluated.
   The report never states it explicitly.
8. BTOS unit response rates for the AI-supplement periods.
9. Deloitte's exact publication date (campaign parameters suggest Davos, 21 Jan 2026).
10. Deloitte's underlying project-level pilot-to-production distribution.
11. S&P's field dates and verbatim question wording.
12. **Any primary reporting a *measured* rather than self-reported production or
    financial-impact rate.** Searched; none found.

### Worked examples — all anonymised, all with before/after numbers

**ST-17 · Invoice processing · $1B+ US logistics company** (pp.16–18). Fleet of
refrigerated trailers, 100k+ invoices a year, seven FTEs. Pre-work quote: "the
750 templates don't make any sense and most of them are repetitive."
> "Headcount 7 → 2 full-time equivalents (FTEs) · Accuracy 85% · Processing time
> < 24 hours · Time to production 8 weeks · Value created > $1M"
Executive line, p.18: "Look guys, 80% is perfect for us… What we care is
immediate cost saving and getting rid of these backlogs." — President

**ST-21 · Security operations · technology services company** (pp.48–50).
Six-person SOC, ~1,500 alerts/month.
> "Alerts processed 1,500 → 40,000/mo · Alert coverage High-priority → 100% ·
> Team capacity required 6 → 1.5 FTEs · Freed capacity redeployed 4.5 FTEs"
> "No one was laid off. The 4.5 FTEs of freed capacity were redeployed to threat
> hunting, security architecture, and capability development."
Reframe, p.49: "AI is not replacing the person you have. AI is replacing the
person you don't need to hire."

**ST-23 · Procurement · regional supermarket chain** (pp.74–76). ~24 stores, "at
roughly half the industry benchmark" margin. AI "replaced the human procurement
function entirely."
> "Waste reduction 40% · Stockout reduction 80% · EBITDA margin Doubled"

**ST-24 · Procurement · construction services company** (pp.84–85). **The only
case with an investment figure and an explicit ROI claim.**
> "Investment $500K - $1M · Productivity gain (projected over 3–5 years) 30% ·
> Expected ROI 10x over 3 years"
Note "projected" and "expected" — not measured.

**ST-20 · Field service · semiconductor manufacturer** (pp.41–43). Data across
"five or six different repositories owned by different teams"; "The service-level
agreement (SLA) for data gathering alone was 40 hours."
> "Data gathering time 40+ hours → < 1 hour · Issues with complete data 0% →
> 95%+ · Product testing cycle 20% reduction"
Key line, p.43: "AI is a mindset change, it's nothing more than that. It is
actually completely change-management driven."

**ST-19 · Marketing content · financial services company** (pp.33–34). Agency
workflow "took seven weeks per campaign"; deliberate 80/20 human split.
> "Time to market 7 weeks → 6 hours · Click through rate 2x improvement ·
> Production efficiency >80% reduction in time"

**ST-18 · Recruiting · translation services company** (pp.25–27). Second attempt
after a failure: "they did not account for bias… and they assumed AI would fix
broken processes."
> "Time to build ~1 month · Time per role 3 hrs → 3 min · Intake efficiency +83%
> · Screening efficiency +79% · Candidate conversion +75%"
Demand test, p.26: "This was a painkiller for those guys. It wasn't 'Hey, this
would be great.' It was 'I'm drowning.'"

**ST-22 · Engineering · education technology company** (pp.55–57). 200+ in tech,
100+ engineers; six-month Copilot/Cursor pilot. The internal politics are
explicit and usable: "The CEO and COO, under PE pressure to show returns, leaned
toward cost reduction. The CFO was initially unconvinced that AI would generate
net savings. The CTO argued for acceleration." (p.56)
> "Engineering productivity 20-30% time saved · Development costs Millions in
> savings · Engineering headcount No reduction · Savings reinvested in AI
> development"

**ST-25 · Customer support · communications technology company** (pp.103–104).
Multi-LLM gateway routing on "cost, latency, relevance, and accuracy."
> "Ticket deflection 82% · Resolution rate 71% · Agent productivity 40%+
> improvement · Support headcount 32% reduction"

**ST-27 · Customer-facing AI · large US retail bank** (pp.92–93). Four-component
PII architecture. "Channel cost Lowest to serve · Call containment 48-72hr
reduction." Key line: "Risk-averse culture is the hardest barrier."

**ST-26 · ⚠️ Call-centre-as-a-service company** (pp.65–67). **Internally
inconsistent — do not use the number.** Results box says "New project wins 20+
attributed to AI"; the prose says "Thirty new projects were won not because the
company was cheaper, but because it was more capable" (p.66) and "thirty new
projects later" (p.67).

**ST-28 · Further prose examples with numbers.** Retail personalised email, p.60:
"In the first month, they measured a 40% increase in purchase intent and a 20%
increase in actual purchases" — with the line "The only thing this did was it
gave them better emails to send." · Fintech >100M customers, p.63: legacy
migration "traditional estimate was 18 months with over 1,000 engineers. With AI
coding agents, business units began completing migrations in weeks." · Insurance
rewrite, p.63: "originally quoted at 5,000 hours with a team of seven, scheduled
for completion in 2027, was finished in 600 hours with a team of three." ·
PE-owned company, p.54: "an 88% productivity gain in coding led to reducing the
development team from seven to three." · Semiconductor shadow AI, p.89: "the
company staff are using 1,500 or 1,600 different AI tools." · Enterprise content
platform, p.60: "200% increase in click through rates."

#### From B and C, if needed

**ST-46 · B's critique of how GenAI quality gets measured.** Useful support for
outcome 3 beyond the cost/revenue split.
> "These evaluations tend to measure simplistic metrics like accuracy,
> hallucination rates, or the recall of specific court opinions. While these
> benchmarks provide a metric, our research argues their actual usefulness is
> uncertain."
> "Without a clear understanding of what 'good' looks like, it is impossible to
> establish trust in AI systems or determine the appropriate division of labor
> between humans and machines."
pp.11–12 · https://law.stanford.edu/wp-content/uploads/2025/08/Building-for-Production_-A-Revised-Playbook-for-Enterprise-Ready-Generative-AI-Solutions_MA-MANDAL.pdf
Its blind-evaluation pilot, p.12: "reviewing partners did not favor the most
comprehensive outputs. Instead, they consistently preferred work products that
were clear, concise, and precise." **Sample size not stated — NOT ESTABLISHED.**

#### NOT ESTABLISHED

1. Any Stanford document titled "Stanford GenAI Playbook". The name is informal.
2. Named companies behind any case study. Removal is stated policy; unobtainable.
3. The report's true data-collection window (three inconsistent statements).
4. Whether the call-centre case won 20+ or 30 projects.
5. An aggregate dollar value across the 51 cases — only per-case figures exist.
6. Sample size of B's lawyer blind-evaluation pilot.

## Outline

<!-- Written after the Research Brief. Up to three Outlines differing on
     Teaching Strategy, outcomes and duration held constant. -->

_Pending._

| # | Section | Min | Words | Teaching intent | Findings | Outline | Narration | Slides |
|---|---------|-----|-------|-----------------|----------|---------|-----------|--------|
| 1 |         |     |       |                 |          | pending | pending   | pending |

## Narration

_Pending gate 1 approval._
