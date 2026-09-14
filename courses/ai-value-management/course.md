---
title: AI Value Management
series: ai-for-business-leaders

template: course
theme: corporate-clean
themes: corporate-clean,minimal-white,swiss-grid,academic-paper,course-warm
lang: en
delivery: recorded     # presenter-led | self-paced | recorded  (gate 1)
rate: 117          # EFFECTIVE wpm, measured: 3,512 words / 30 min. Raw speech is 23.4 min at 150 wpm; the balance is quiz pauses and visual beats.
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

By the end of this session, participants will be able to:

1. Identify the stage at which an AI initiative has stalled, and distinguish the
   causes and remedies that apply to each stage.
2. Explain why a technically effective AI system does not by itself improve
   financial performance, and identify the organisational changes required to
   realise its value.
3. Specify the evidence required before approving investment in an AI
   initiative, including a pre-deployment baseline and an accountable benefit
   owner, and assess whether a reported benefit is a verified saving or an
   estimate.
4. Determine which AI initiatives to discontinue and which to prioritise over the
   next 90 days.

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

One `### Rnn` entry per source, each with the claim, a direct quote, the URL and
the date. **A slide may only cite source IDs its narration block declares.**
Caveats, discarded figures and arithmetic are in `## Evidence audit` below; read
the audit entry before citing any Rnn on a slide.

### R00 · Illustrations and teaching synthesis

The four-stage diagnosis in S4 and the decision rule in S8. Built from R08, R06,
R12 and R03, and identified on the slide as the course's own structure. **No
source stages the whole funnel** — see the audit. Not attributed to any
researcher.

### R01 · MIT NANDA — the 95% figure

*The GenAI Divide: State of AI in Business 2025.* Challapally, Pease, Raskar,
Chari. July 2025. Research period January to June 2025.
> "Despite $30–40 billion in enterprise investment into GenAI, this report
> uncovers a surprising result in that 95% of organizations are getting zero
> return."
> "Sixty percent of organizations evaluated such tools, but only 20 percent
> reached pilot stage and just 5 percent reached production."
> "The 95% failure rate for enterprise AI solutions represents the clearest
> manifestation of the GenAI Divide."
http://web.archive.org/web/20250818145714if_/https://nanda.media.mit.edu/ai_report_2025.pdf
⚠️ The canonical MIT URL now redirects to a sponsorship page. Cite the archive.

### R02 · MIT NANDA — method and its own limits

Same document.
> "structured interviews with representatives from 52 organizations, and survey
> responses from 153 senior leaders collected across four major industry
> conferences."
> "We define successfully implemented for task-specific GenAI tools as ones users
> or executives have remarked as causing a marked and sustained productivity
> and/or P&L impact"
> "These figures are directionally accurate based on individual interviews rather
> than official company reporting."
> "Preliminary Findings from AI Implementation Research from Project NANDA"
> "The views expressed in this report are solely those of the authors and reviewers
> and do not reflect the positions of any affiliated employers."

### R03 · McKinsey — state of AI 2026

25 August 2026. Field 4 May to 8 June 2026. n=1,719 in 97 nations, GDP-weighted.
> "Thirty-seven percent of respondents attribute at least some EBIT impact to AI
> use (about the same share as last year). And the proportion of AI high
> performers … has remained flat at about 6 percent of all respondents."
> "At the individual level, AI is clearly a boon: 80 percent of survey respondents
> say it has improved their productivity and half say it helps them make better
> decisions. Yet, only 37 percent of organizations report any positive EBIT
> contribution, essentially flat compared with last year."
> "One in five respondents says their organization is limiting AI use because of
> operating costs"
> "Just 14 percent of respondents from organizations using AI report that AI
> contributed to an overall decline in workforce size in the past year—less than
> half the 32 percent who, in last year's survey, expected workforce reductions"
https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

### R04 · McKinsey — workflow redesign and its R²

*The state of AI: How organizations are rewiring to capture value*, March 2025.
n=1,491, field 16 to 31 July 2024.
> "out of 25 attributes tested for organizations of all sizes, the redesign of
> workflows has the biggest effect on an organization's ability to see EBIT impact
> from its use of gen AI."
> Footnote 1: "The correlation analyses considered 25 attributes and the reported
> effect of gen AI use on organizations' EBIT, and using the Johnson's Relative
> Weights regression analysis yielded an R-squared of 0.20."
> "less than one in five saying their organizations are tracking KPIs for gen AI
> solutions."
**Correlation, not causation. Both variables self-reported by one respondent.**

### R05 · Deloitte — benefits achieved against benefits hoped for

*State of AI in the Enterprise: The Untapped Edge*, January 2026. Field August to
September 2025. n=3,235, director to C-suite, 24 countries.
> "revenue growth largely remains an aspiration, with 74% of organizations hoping
> to grow revenue through their AI initiatives in the future compared to just 20%
> that are already doing so"
Achieving today against hope to achieve: efficiency and productivity 66/60;
reduce costs 40/65; **increase revenue 20/74**.
⚠️ Frame is purposive: "organizations on the leading edge of AI". Not a
population estimate.

### R06 · S&P Global / 451 Research — abandonment

*Voice of the Enterprise: AI & Machine Learning, Use Cases 2025*, 30 May 2025.
n=1,006, North America and Europe.
> "The percentage of companies abandoning the majority of their AI initiatives
> before they reach production has surged from 17% to 42% year over year, with
> organizations on average reporting that 46% of projects are scrapped between
> proof of concept and broad adoption."
⚠️ Field dates and question wording not published. The 46% is the only
project-level figure in the brief.

### R07 · US Census BTOS — adoption, with a real sampling frame

*Large Firms With at Least 20 Employees Biggest AI Users*, 26 May 2026.
~1.2 million businesses sampled annually from the 2023 Business Register.
> "As of May 3, 2026, the AI use rates in the Information (39.7%) and Finance and
> Insurance (33.9%) sectors were both higher than the national rate (19.8%)"
> "Less than 20% of firms with four or fewer employees reported using AI."
https://www.census.gov/library/stories/2026/05/ai-use-businesses.html
⚠️ Filed under Experimental Data Products. A November 2025 question change breaks
the series.

### R08 · US Census — the complementary work is not being done

Bonney, Breaux, Dinlersoz, Foster, Haltiwanger & Pande, *The Microstructure of AI
Diffusion*, CES-WP-26-25, April 2026. **>117,000 distinct firms, nationally
representative, survey-weighted.** The strongest sample in the brief.
> "over half of AI-using businesses (64%) report no institutional adjustments …
> The most common adjustments are training staff and developing new workflows –
> each applicable to about 15% of AI-using firms."
> "the most common barrier is that AI is not applicable to the business (65% of
> firms, firm-weighted)"
> "57% of users integrate AI in three or fewer business functions, most commonly
> Sales and Marketing (52%)"
> "Most users (66%) rely on AI solely to augment tasks, while AI-related
> employment decreases are rare, occurring in only 2% of firms."
> "We underscore that these associations are descriptive and do not imply causal
> relationships … reverse causality remains a concern"
https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-25.pdf

### R09 · Stanford Digital Economy Lab — the Enterprise AI Playbook

*The Enterprise AI Playbook: Lessons from 51 Successful Deployments.* Pereira,
Graylin, Brynjolfsson. April 2026. 51 cases, 41 organisations, interview-based.
> "Same technology, same use cases, vastly different outcomes. The difference was
> never the AI model. It was always the organization." (p.2)
> "77% of the hardest challenges practitioners faced were invisible costs: change
> management, data quality, and process redesign, not technical issues. Technology
> was consistently described as the easiest part." (p.13)
> "Common symptoms like 'projects stuck in pilot' or 'inability to prove ROI'
> appeared frequently, but these are consequences, not causes." (p.110)
> Six root causes: organisation not ready to adopt 35%; knowledge never captured
> 27%; legal or compliance blocked 18%; technology not mature 16%; wrong problem
> 14%; talent or sponsorship gap 12%. (p.111)
> "61% had a failed AI project before their current success" (p.15)
> "Fix the process before applying AI. AI amplifies whatever process it is applied
> to. If the process is broken, AI makes it worse faster." (p.27)
> "We want to be transparent that this does carry a known limitation: selection
> bias toward positive outcomes … we don't claim to provide representative data on
> how common success is across the broader economy." (p.6)
https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf
⚠️ **Every percentage has a denominator of successes.** Every company anonymised.
⚠️ **Disclose (Ray's instruction):** Brynjolfsson "puts his academic insights to
practical use via Workhelix, a company he co-founded to identify and measure the
benefits of AI" (p.3).

### R10 · RAND — root causes of AI project failure

RR-A2680-1, 13 August 2024. 65 semi-structured interviews, 50 industry and 15
academic, August to December 2023.
> "Eighty-four percent of our interviewees cited one or more of these root causes
> as the primary reason that AI projects would fail."
> "the most common root cause of failure was the business leadership of the
> organization misunderstanding how to set the project on a pathway to success."
> "because the majority of our interviewees were nonmanagerial engineers instead
> of business executives, the results may disproportionately reflect the
> perspective of individuals who do not hold leadership positions. Thus, the
> results may be skewed toward identifying leadership failures."
https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2600/RRA2680-1/RAND_RRA2680-1.pdf
⚠️ **RAND's own "80% of AI projects fail" line is a citation to journalism, not a
RAND finding. The course must not repeat it.**

### R11 · Dillon, Jaffe, Immorlica & Stanton — time saved, nothing else moved

*Shifting Work Patterns with Generative AI*, arXiv:2504.11436v4, 13 November
2025; NBER WP 33795. Randomised, **66 firms, 7,137 knowledge workers, 6 months.**
> "the 80% of treated workers who used this tool spent two fewer hours on email
> each week and reduced their time working outside of regular hours. Apart from
> these individual time savings, we do not detect shifts in the quantity or
> composition of workers' tasks resulting from individual-level AI provision."
> "treated and control workers replied to the same number of email threads,
> participated in the same number of Teams meetings, and completed the same number
> of Word documents."
> "we do not observe the content of any work nor any measures of productivity or
> performance evaluation."
https://arxiv.org/abs/2504.11436

### R12 · Humlum & Vestergaard — a measured null, and where the work goes

*Still Waters, Rapid Currents*, RFBerlin DP 078/26, 13 March 2026; NBER WP 33777.
~25,000 Danish worker responses per round linked to administrative records,
difference-in-differences, 11 exposed occupations.
> "most employers in exposed occupations have adopted chatbot initiatives, workers
> report productivity benefits, and new AI-related tasks are widespread. Yet these
> currents have not broken the surface: using difference-in-differences, we
> estimate precise null effects on earnings and recorded hours at both the worker
> and workplace levels, ruling out effects larger than 2% two years after the
> launch of ChatGPT."
> "only 41% of new tasks focus on 'productive AI use' … while the remaining 59%
> relate to 'AI implementation and oversight'"
> "about 25% spend more time on the same tasks they initially saved time on."
> "take-up rates almost double in workplaces with active employer initiatives."
> adopters "report savings of about 3% of their work hours"; "the large majority
> (85%) of chatbot users reallocate saved time to other job tasks."
https://www.rfberlin.com/wp-content/uploads/2026/03/26078.pdf
⚠️ "RFBerlin Discussion Papers … have not been peer-reviewed."

### R13 · Cui et al. — lab to field attenuation

Three firm RCTs at Microsoft, Accenture and a Fortune 100 company. n=4,867
developers, 2 to 8 months. *Management Science*.
> "a 26.08% increase (SE: 10.3%) in completed tasks among developers using the AI
> tool"
> "this estimate is substantially smaller than the 58% decrease Peng et al. (2023)
> find for the time to complete a software engineering task in the lab …
> Additionally, coding is only part of a software developer's job, so only some of
> the time saved on coding tasks may be spent on additional coding."
> "Though each experiment is noisy"; "only the effect on the number of pull
> requests is statistically significant at conventional significance levels."
https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf
⚠️ Outcomes are pull requests, commits and builds. Activity counts, not value.

### R14 · METR 2025 — the forecast, the belief and the measurement

arXiv:2507.09089, 12 July 2025. Task-randomised. **n=16 developers, 246 tasks** in
repositories they maintain.
> "Before starting tasks, developers forecast that allowing AI will reduce
> completion time by 24%. After completing the study, developers estimate that
> allowing AI reduced completion time by 20%. Surprisingly, we find that allowing
> AI actually increases completion time by 19%"
> "We do not claim that our developers or repositories represent a majority or
> plurality of software development work"
https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
⚠️ Confidence interval +2% to +39%. **Superseded by R15.**

### R15 · METR 2026 — the slowdown is gone, and the design abandoned

*We are Changing our Developer Productivity Experiment Design*, 24 February 2026.
57 developers, 143 repositories, 800+ tasks.
> "we now estimate a speedup of -18% with a confidence interval between -38% and
> +9%. Among newly-recruited developers the estimated speedup is -4%, with a
> confidence interval between -15% and +9%."
> "30% to 50% of developers told us that they were choosing not to submit some
> tasks because they did not want to do them without AI. This implies we are
> systematically missing tasks which have high expected uplift from AI."
> "Wider adoption of AI has made it more difficult to measure task-level
> productivity"
> "it is likely a bad proxy for the real productivity impact of AI tools"
https://metr.org/blog/2026-02-24-uplift-update/
**Both new intervals cross zero. Anyone citing the 19% slowdown today is a year
out of date.**

### R16 · Brynjolfsson, Li & Raymond — gains concentrate in novices

*Generative AI at Work*, *Quarterly Journal of Economics* 140(2), 2025. Staggered
rollout, difference-in-differences, n=5,172 customer-support agents, GPT-3 era.
> "increases worker productivity, as measured by issues resolved per hour, by 15%
> on average, with substantial heterogeneity across workers."
> "a 30% increase in the number of issues resolved per hour" for less skilled
> workers; "we find evidence that AI assistance leads to a small decrease in the
> quality of conversations conducted by the most skilled agents."
https://danielle-li.github.io/assets/docs/GenerativeAIatWork.pdf
⚠️ **Published figure is 15%, not the 14% usually quoted. A staggered rollout, not
an RCT.**

### R17 · Dell'Acqua et al. — the jagged frontier

SSRN 4573321, revised 17 March 2026; *Organization Science*. **Pre-registered
RCT, n=758.**
> "subjects using AI outperformed those not using AI, completing 12.2% more tasks
> and completing them 25.1% more quickly on average"
> "for a complex managerial task selected to be outside the frontier, subjects
> using AI were 19% less likely to produce correct solutions"
⚠️ **The paper's body says 19 percentage points; the abstract says 19%. Use
percentage points.** Conducted with Boston Consulting Group, with BCG-affiliated
co-authors. Disclose.

### R18 · Acemoglu — the only attempt at the whole chain

*The Simple Macroeconomics of AI*, NBER WP 32487, 2024; *Economic Policy* 2025.
> "these macroeconomic effects appear nontrivial but modest—no more than a 0.66%
> increase in total factor productivity (TFP) over 10 years."
> "even these estimates could be exaggerated … predicted TFP gains over the next
> 10 years are even more modest and are predicted to be less than 0.53%."
**A model calibrated on other people's task-level estimates. Not a measurement.**

### R19 · Bick, Blandin & Deming — the self-reported bridge

St. Louis Fed, 13 November 2025; survey NBER WP 32966.
> "Workers report generative AI time savings equivalent to 1.6% of all work hours"
> "This suggests that generative AI may have increased labor productivity by up to
> 1.3% since the introduction of ChatGPT."
> "increased productivity by workers in some tasks will not increase measured
> productivity by as much if workers apply their saved time to less-productive
> activities"

### R20 · US Bureau of Labor Statistics — AI is not measured separately

*Productivity and Artificial Intelligence*, page dated 8 June 2026.
> "BLS implicitly captures AI use through its capital measure of software used in
> production."
https://www.bls.gov/productivity/articles-and-research/ai-and-productivity/home.htm

### R21 · Brynjolfsson, Rock & Syverson — the paradox and its mechanism

NBER WP 24001, November 2017.
> "We describe four potential explanations for this clash of expectations and
> statistics: false hopes, mismeasurement, redistribution, and implementation
> lags. While a case can be made for each, we argue that lags have likely been the
> biggest contributor to the paradox."
> "their full effects won't be realized until waves of complementary innovations
> are developed and implemented. The required adjustment costs, organizational
> changes, and new skills can be modeled as a kind of intangible capital."

### R22 · Klarna Form 20-F FY2025 — the audited record

> "Our AI assistant has handled 80% of customer service chats in the year ended
> December 31, 2025 (according to our service chat log data), with no drop in
> consumer satisfaction levels since its introduction (according to internal
> consumer satisfaction surveys)."
> "Customer service and operations expenses for the year ended December 31, 2025
> increased by $4 million, or 2%, compared to the year ended December 31, 2024.
> Cost increased at a slower pace than volumes, with volumes up 32% year-over-year
> and transactions up 25% year-over-year, indicating continued operating leverage."
> Prior year decrease: "primarily driven by a decrease in customer service costs
> as we continued to make significant efforts to optimize and manage such costs."
> "dual-track approach of combining broad and continuing implementation of scalable
> AI in customer service with high-quality human support."
Audited line: 2023 US$240m; 2024 US$203m; 2025 US$207m.
https://www.sec.gov/Archives/edgar/data/2003292/000200329226000007/klar-20251231.htm

### R23 · Klarna Q3 2025 earnings call — the unaudited claim

Sebastian Siemiatkowski, 18 November 2025.
> "it used to do about 700 full-time jobs. Now it is doing about 853 full-time jobs
> of a saving of $60 million."
**No baseline, no definition of a full-time job, no derivation.**

### R24 · Presto Automation — a denominator that excluded the work

10-K FY2023, 11 October 2023:
> "Presto Voice currently achieves an 85% non-intervention rate on average,
> meaning that restaurant staff does not need to intervene in 85% of the orders
> placed"
> "Our systems currently use a human agent (located offsite of the restaurant) to
> enter, review, validate and correct orders received by Presto Voice"
> "we had 137 full-time employees … and 149 contractors, consisting primarily of
> human agents supporting our HITL approach"
10-Q, 21 February 2024:
> "locations that use our AI technology currently use human agent intervention,
> including entering the order, in all instances."
> "the SEC had commenced a formal investigation into disclosures that the Company
> had made regarding certain aspects of its AI technology."
https://www.sec.gov/Archives/edgar/data/1822145/000155837023016336/prst-20230630x10k.htm

### R25 · Commonwealth Bank of Australia — a defined metric

FY2026 Full Year Results Presentation, year ended 30 June 2026.
> "Agentic messaging resolve rate¹ … 86% … FY26
> ¹ Percentage of customer conversations initiated through the agentic chatbot
> channel that are successfully resolved without a human assisted servicing
> pathway."
https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Presentation.pdf
**Use as the counter-example: a defined denominator in an investor document.**

### R26 · IBM — a self-reported gain, and a figure that changes shape

Q4 2025 earnings call, 28 January 2026.
> "We have more than 20,000 IBMers that are using Project Bob, reporting
> productivity gains averaging 45%"
Annual Report: "approximately $4.5 billion in productivity savings since the
beginning of 2023." Same quarter's call: "exiting 2025 with $4.5 billion of
annual run rate savings."
FY2025 10-K: "IBM's drive for greater agility, productivity, flexibility and cost
savings by continuously transforming with the use of AI may not yield intended
gains."
**Cumulative and annual run-rate are different quantities. The 10-K carries the
figure nowhere.**

### R27 · World Bank — the counterfactual requirement

Gertler, Martinez, Premand, Rawlings & Vermeersch, *Impact Evaluation in
Practice*, 2nd ed., World Bank and IDB, 13 September 2016.
> "without a comparison group that yields an accurate estimate of the
> counterfactual, the true impact of a program cannot be established."
> "the baseline outcome is almost never a good estimate of the counterfactual.
> That is why we consider it a counterfeit estimate of the counterfactual."
https://openknowledge.worldbank.org/handle/10986/25030

### R28 · Gordon et al. — 416% claimed, 77% real

*A Comparison of Approaches to Advertising Measurement: Evidence from Big Field
Experiments at Facebook*, MSI WP 18-113, 2018; *Marketing Science* 38(2), 2019.
15 experiments.
> "the observational methods overestimate ad effectiveness relative to the RCT…
> The bias can be large: in half of our studies, the estimated percentage increase
> in purchase outcomes is off by a factor of three across all methods."
> "When we naively compared exposed to unexposed users, we estimated an ad lift of
> 416%. … Matching the groups based on their propensity score … gave us a lift of
> 102%. Compared to the starting point, we have gotten much closer to the true RCT
> lift of 77%."
https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_18-113.pdf

### R29 · Lewis & Rao — the arithmetic ceiling

*The Unfavorable Economics of Measuring the Returns to Advertising*, *Quarterly
Journal of Economics* 130(4), 2015. 25 large field experiments.
> "The median confidence interval on return on investment is over 100 percentage
> points wide."
> "Achieving more standard tolerances for investment decisions, such as a 10% ROI
> difference, requires the median campaign to be 62 times larger to possess
> adequate power—nearly impossible for a campaign of any realistic size."

### R30 · UK cashable savings — the four-line test

Cabinet Office and HM Treasury, *Government efficiency savings technical note*.
> "Cashable savings are those which lead to a direct reduction (all other things
> being equal) in a department budget."
> "The savings are defined as: ● Release of cash that relates to an activity that
> has already happened ● Not just relocating or deferring costs ● Fairly calculated
> and clearly positioned ● Captured in year and accrue within period ● Net of any
> double counting ● Understood and seen as reasonable by an impartial third party."
https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1064110/government-efficiency-savings-technical-note.pdf

### R31 · HM Treasury Green Book — additionality

*The Green Book: UK Government Guidance on Appraisal 2026.*
> "Deadweight: Outcomes that would have taken place without any intervention."
> "Additionality: Outcomes that take place as a result of the intervention."

### R32 · HM Treasury Magenta Book — baseline timing

*Central Government guidance on evaluation*, March 2020.
> "The intervention effect is sufficiently large to be distinguished from expected
> 'noise' in the data."
> "baseline data – data collected before the intervention – will need to be
> collected early … Without appropriate data collection or data access planning an
> evaluation may be impossible, severely limited, or unnecessarily expensive."

### R33 · BCG — most firms track no financial KPI

*AI Radar: From Potential to Profit*, January 2025. n=1,803 C-level.
> "60% of companies are failing to define and monitor any financial KPIs related
> to AI value creation"
> "We drew insights on AI maturity and value from self-reported data provided by
> the respondents."

### R34 · IBM Institute for Business Value — starting what cannot be assessed

*Solving the AI ROI puzzle*, 13 July 2025. n=624, 22 countries.
> "72% of CAIOs say their organizations risk falling behind without AI impact
> measurement. But 68% initiate AI projects even if they can't assess their
> impact—because the most promising AI opportunities are often the most difficult
> to measure."
2025 CEO Study, n=2,000: "CEOs say only 25% of AI initiatives have delivered
expected ROI—and only 16% have scaled enterprise-wide."

### R35 · Kohavi et al. — why before-and-after fails in industry

*Online Controlled Experiments at Large Scale*, KDD 2013.
> "The most common question we get as an organization learns about controlled
> experiments is 'why not measure the metric of interest, ship the feature, and
> then look at the delta?'"
> "Our experience is that external variations overwhelm the effects we are trying
> to detect."
> "Only one third of the ideas tested at Microsoft improved the metric(s) they were
> designed to improve."

### R36 · Sculley et al. — the model is a small part of the system

*Hidden Technical Debt in Machine Learning Systems*, NeurIPS 2015.
> "only a tiny fraction of the code in many ML systems is actually devoted to
> learning or prediction … much of the remainder may be described as 'plumbing'."
> "developing and deploying ML systems is relatively fast and cheap, but
> maintaining them over time is difficult and expensive."
⚠️ The 5%/95% figure is an estimate, not a measurement. Quote as expert testimony.

### R37 · MIT — a withdrawn result, disavowed

arXiv:2412.17866, administrative note on v2, 20 May 2025:
> "Withdrawn by arXiv administrators due to concerns about the validity of the
> data and incomplete Institutional Review Board requirements"
Acemoglu & Autor, MIT Department of Economics, 16 May 2025:
> "we want to be clear that we have no confidence in the provenance, reliability
> or validity of the data and in the veracity of the research."
> "the findings reported in this paper should not be relied on"
https://economics.mit.edu/news/assuring-accurate-research-record

### R38 · Brynjolfsson & Hitt — what an IT programme actually costs

*Beyond Computation*, *Journal of Economic Perspectives* 14(4), Fall 2000.
> "the average spending on computer hardware accounted for less than 4 percent of
> the typical start-up cost of $20.5 million, while software licenses and
> development were another 16 percent of total costs. The remaining costs included
> hiring outside and internal consultants to help design new business processes and
> to train workers in the use of the system."
**Use this, not the playbook's 1:10 claim. See the audit.**

### R39 · Klarna — the balance point  ✅ verified 13 September 2026

Ray's catch was right, and the answer is narrower than either narrative.

**The Diary of a CEO appearance is real but he was not a booked guest.** He
appears inside the Karen Hao episode of 26 March 2026, first as a direct message
Bartlett reads aloud with permission, then as a live phone call. Hao had said on
the same episode: "the Klarna CEO who laid off a bunch of people thinking that he
would replace everyone with AI, and then it didn't actually work and he had to ask
some people to come back." https://www.youtube.com/watch?v=Cn8HBj8QAbk at 01:22:13

**His direct message, read aloud at 01:22:41:**
> "I think sometimes people struggle with two things can be true at the same time.
> … this is the media misinterpreting my tweet. We are doubling down on AI more
> than ever."

**On the call at 01:35:22, asked directly whether he reversed:**
> "we believed in a world where AI is cheap and available, the value of human
> interaction will be regarded as higher. So the future of customer service VIP is
> a human. We have then hence doubled down on providing more of that. But at the
> same time the efficiency gains within the company has continued."
> "you can clearly see that AI has allowed us to do more with less people, but we
> have avoided layoffs and instead relied on natural attrition"

**⚠️ He does NOT claim he was misquoted. He twice exonerates the Bloomberg text.**
Big Technology Podcast, 16 May 2025:
> "if you read the original Bloomberg article it's quite balanced and describing
> quite accurately what what I said and what happened, but then what tends to
> happen in classic media is that they take just the headline"
20VC, 16 February 2026: "it's like very hard in the Bloomberg article. I'm not
going to blame the journalist."
> "the headline is like they're rolling AI back, and then the whole media circus go
> on like oh Klarna has just announced that they're rolling it back. It's like no,
> that's not at all."

**What he actually said to Bloomberg, 8 May 2025:**
> "As cost unfortunately seems to have been a too predominant evaluation factor
> when organising this, what you end up having is lower quality"
The subject is the cost-led organisation of outsourced support. **The sentence does
not say the AI assistant produced lower quality.** Bloomberg's lede went further
than his quote: "has gone too far … a sign the Swedish fintech's commitment to AI
has its limits."

**⭐ The same Bloomberg article described a two-person pilot and forecast further
shrinkage.** This is the most load-bearing fact against the reversal story.
> "The pilot has started small, with two of the new breed of customer-service
> agents live now"
> "In a year's time he expects the natural attrition rate of 20% to continue,
> taking the workforce down to about 2,500 from the current level of 3,000."

**The mutation, each step adding something the source does not contain.** Fortune,
9 May, inverted the causality. Gizmodo, 11 May, invented "700 really bad agents"
and a "human hiring spree". Forbes, 18 May, added "declining service quality and
customer dissatisfaction" while citing Gizmodo rather than Bloomberg. Futurism,
4 September, added a panic: "Then Panics … as the AI Fails".

**Klarna denied it on the record, in the same Forbes piece that carried the story:**
> "Klarna is not reversing on AI. … Klarna never eliminated human support. We still
> work with several thousand outsourced agents. The current pilot involves just two
> new agents in a flexible, remote setup. It's an addition, not a rehire or
> reversal. Sebastian Siemiatkowski acknowledged that an overemphasis on cost—not
> AI itself—led to lower quality."

**The 700 figure is Klarna's own, and it is an equivalence estimate.** Press
release, 27 February 2024: "It is doing the equivalent work of 700 full-time
agents". The same release: "Additionally, customers can still choose to interact
with live agents if they'd prefer."
https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/

**⭐ The filings never wavered. Headcount is monotonic, with no rebound.**
> "As of December 31, 2025, 2024, and 2023, we had approximately 2,831, 3,422, and
> 4,352 full-time employees, respectively." (20-F FY2025)
> 5,527 at 31 December 2022 (424B4, 10 September 2025).
> "The reduction … resulted from our strategic decision to reduce our overall
> headcount and drive operational efficiency by leveraging AI … We expect the
> number of employees to continue to decrease in future periods." **Unchanged
> across the F-1, the 424B4 and the 20-F.**
Automation share 69% → 80%. Agent-equivalents "over 700" → "over 850". Savings
US$39m → US$59m. Every figure moves the same way.

**⚠️ CORRECTION to R22 as first recorded.** The FY2025 20-F **does** quantify a
saving:
> "Our AI assistant handled 80% of customer service chats in the year ended
> December 31, 2025 … doing the work equivalent of over 850 full-time agents … and
> in 2025 delivered approximately $59 million in cost savings."
So the audited filing carries **both** the US$59m saving claim and the US$4m
expense increase. **They are in the same document.** That is a stronger teaching
point than the call-versus-filing contrast I first recorded, and S6 must use the
corrected version.

**The only textual trace of the pivot in any filing is the dual-track sentence,
and it concedes nothing.**
> "appreciating that certain consumers may nevertheless prefer to interact with
> human representatives, we continue to offer all of our customers that option."
**Verified absent** from the F-1 of 14 March 2025; present by 10 September 2025.
The AI risk factor is hypothetical throughout: "no assurance can be provided",
"may be", "may inadvertently". **No realised event is disclosed.**

**⚠️ His spoken headcount figures do not reconcile with the filings.** Peak stated
as 6,000, 7,000 and 7,400 on different occasions; the filed figure is 5,527.
**No source explains the gap. Present it as unresolved, do not resolve it.**

#### The four readings, kept separate

| Reading | Established? |
|---|---|
| (a) He was misquoted | **No.** He exonerates the Bloomberg text twice |
| (b) Quoted correctly, conclusion drawn was wrong | **Yes. This is his actual claim, and the record supports it** |
| (c) He changed his mind | **Yes, on a narrower point, and he admits it.** "too much focus on cost … [We] have to rethink this". On timing: "You could definitely place me in the Elon Musk box … I'm guilty as charge on that one" |
| (d) He is managing a reputational problem | **Partly, and observably.** But the pushback began within five days, is consistent across five occasions over ten months, and matches the filings |

**The line that carries the case:** the reversal exists in spoken interviews and
nowhere in the securities filings. In documents signed under SEC liability, the
direction of travel never changes.

⚠️ **Podcast quotes were extracted from auto-generated captions.** Before any of
this reaches a slide, a human should listen to the cited timestamp and confirm the
wording. The Bloomberg article is paywalled; its full text was read from The Star's
syndication.

## Evidence audit — working notes

The long-form audit behind the Research Brief. Source-keyed entries the build
reads are in `## Research Brief` above; these are the caveats, the arithmetic and
the discarded figures that must not reach a slide.

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

### Causes of failure  ✅ researched 2026-09-12

Two kinds of evidence, never mixed: what companies **self-report**, and what
researchers **observed**. Self-reports are what executives believe. Observations
are what happened.

#### Self-reported causes

**C-1 · 84% of practitioners name business leadership's framing as the root
cause. The highest single number in the brief, and it points at the audience.**
> "More than any other type of issue, our interviewees noted that failures driven
> by the decisions and expectations of the organization's business leadership were
> far and away the most frequent causes of project failure. Eighty-four percent of
> our interviewees cited one or more of these root causes as the primary reason
> that AI projects would fail."
> "the most common root cause of failure was the business leadership of the
> organization misunderstanding how to set the project on a pathway to success."
RAND, *The Root Causes of Failure for Artificial Intelligence Projects and How
They Can Succeed*, RR-A2680-1, 13 Aug 2024. n=65 semi-structured interviews
(50 industry, 15 academic), Aug–Dec 2023.
https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2600/RRA2680-1/RAND_RRA2680-1.pdf
**RAND's own caveat, which must be said aloud if this is used:**
> "because the majority of our interviewees were nonmanagerial engineers instead
> of business executives, the results may disproportionately reflect the
> perspective of individuals who do not hold leadership positions. Thus, the
> results may be skewed toward identifying leadership failures."

**C-2 / C-3 · RAND's remaining causes.** Data quality is second: "These two root
causes were cited spontaneously by more than one-half of the interviewees."
Then three more, each cited by a quarter to a third: chasing "the latest and
greatest technology than on solving real problems for its intended users";
inadequate infrastructure; and "the technology is applied to problems that are too
difficult for AI to solve."

**C-6 · ⚠️ Deloitte's leading-edge sample names worker skills as the top barrier.**
> "insufficient worker skills are the biggest barrier to integrating AI into
> existing workflows."
> "education—not role or workflow redesign—was the No. 1 way companies adjusted
> their talent strategies due to AI."
Deloitte 2026, n=3,235, field Aug–Sep 2025. **Frame is purposive:** "To obtain a
global view of how AI is being adopted by organizations on the leading edge of
AI". Not a population estimate.

#### Observed causes — the best evidence in the brief

**C-8 · 64% of AI-using US firms made NO organisational adjustment at all. A
measured fact, nationally representative, and the course's strongest single
finding.**
> "Figure 18 reveals that over half of AI-using businesses (64%) report no
> institutional adjustments, suggesting a reliance on 'off-the-shelf' AI/GenAI
> tools or a significant lag in organizational restructuring. The most common
> adjustments are training staff and developing new workflows – each applicable to
> about 15% of AI-using firms. Deeper capital-related shifts, such as changes to
> data management and storage practices and complementary capital investments,
> take place in a smaller fraction of firms (in the 7-8% range). The least common
> adjustment is hiring staff trained in AI."
Bonney, Breaux, Dinlersoz, Foster, Haltiwanger, Pande, *The Microstructure of AI
Diffusion*, US Census Bureau CES-WP-26-25, April 2026. BTOS 2nd AI supplement,
reference period Nov 2025–Jan 2026, **>117,000 distinct firms, nationally
representative, survey-weighted.**
https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-25.pdf

**C-9 · Use stays narrow.**
> "57% of users integrate AI in three or fewer business functions, most commonly
> Sales and Marketing (52%), Strategy and Business Development (45%), and IT
> (41%). … 65% of firms limit use to three or fewer tasks."
Same source. **Use this for the sales-and-marketing skew, not NANDA's figure,
which is internally inconsistent (see F-8 / W-11).**

**C-7 · Why firms never start: they think it does not apply to them. Regulation
is near-last.**
> "the most common barrier is that AI is not applicable to the business (65% of
> firms, firm-weighted)"
> "Lack of knowledge of the capabilities of AI comes at a distant second (22%),
> followed by concerns about privacy/security (20%). The least common barriers are
> using vendors or consulting services to implement AI and laws and regulations
> that prevent or restrict use of AI."
> "the absence of broad federal regulation as of early 2026 ensures that
> regulatory friction remains a minor factor in aggregate non-adoption."
Same source. **⚠️ Do not teach regulation as a leading cause of value failure.
The representative evidence points the other way.** Note this also sets a boundary
with the sibling governance course.

**C-10 · Measured null. Adoption is real, reported gains are real, and earnings
and hours do not move.**
> "We document rapid currents: most employers in exposed occupations have adopted
> chatbot initiatives, workers report productivity benefits, and new AI-related
> tasks are widespread. Yet these currents have not broken the surface: using
> difference-in-differences, we estimate precise null effects on earnings and
> recorded hours at both the worker and workplace levels, ruling out effects
> larger than 2% two years after the launch of ChatGPT."
> "Workplaces that encourage chatbot use exhibit no differential changes in
> employment or wage bills, job creation or destruction, or the composition of
> hires or separations"
Humlum & Vestergaard, *Still Waters, Rapid Currents*, RFBerlin DP 078/26, 13 Mar
2026 (prev. NBER WP 33777). ~25,000 Danish worker survey responses per round
linked to administrative records, difference-in-differences, 11 exposed
occupations. https://www.rfberlin.com/wp-content/uploads/2026/03/26078.pdf
⚠️ Imprint: "RFBerlin Discussion Papers often represent preliminary or incomplete
work and have not been peer-reviewed." **This is the cleanest statement available
that perceived productivity and measured financial effect are different things.**

**C-11 · Experimentally demonstrated harm outside the frontier.**
> "for a complex managerial task selected to be outside the frontier, subjects
> using AI were 19% less likely to produce correct solutions compared with those
> without AI"
Dell'Acqua et al., *Navigating the Jagged Technological Frontier*, SSRN 4573321,
15 Sep 2023, rev. 17 Mar 2026, *Organization Science*. **Pre-registered RCT,
n=758.** ⚠️ "In collaboration with the global management consulting firm Boston
Consulting Group", with BCG-affiliated co-authors. Disclose it.

### What the impact-reporting organisations do differently  ✅ researched 2026-09-12

**Every finding in this section is correlational. The narration must not upgrade
any of it into a promise.**

**W-1 · McKinsey: workflow redesign carries the most weight of 25 attributes
tested — and the footnote gives the R².**
> "out of 25 attributes tested for organizations of all sizes, the redesign of
> workflows has the biggest effect on an organization's ability to see EBIT impact
> from its use of gen AI. … Twenty-one percent of respondents reporting gen AI use
> by their organizations say their organizations have fundamentally redesigned at
> least some workflows."
Footnote 1, verbatim:
> "The correlation analyses considered 25 attributes and the reported effect of
> gen AI use on organizations' EBIT, and using the Johnson's Relative Weights
> regression analysis yielded an R-squared of 0.20."
McKinsey, *The state of AI: How organizations are rewiring to capture value*, Mar
2025. n=1,491, field 16–31 Jul 2024, 101 nations, GDP-weighted.
**Body text says "biggest effect"; the footnote says correlation. Both variables
are self-reported by the same respondent, and all 25 attributes together explain
~20% of variance. The defensible sentence:** among 25 attributes tested, workflow
redesign carried the most relative weight in a correlation with self-reported EBIT
impact, in a model explaining about a fifth of the variance.

**W-2 · CEO oversight of AI governance. Quote McKinsey's first sentence, not its
second.**
> "a CEO's oversight of AI governance … is one element most correlated with higher
> self-reported bottom-line impact from an organization's gen AI use."
The next sentence switches to "the element with the most impact on EBIT" — causal
language the footnote does not support. Same R²=0.20 model. 28% report CEO
oversight; 17% board oversight; "On average, respondents report that two leaders
are in charge."

**W-3 · All 12 adoption practices correlate positively, which weakens any single
prescription.**
> "We asked respondents about 12 adoption- and scaling-related practices for gen
> AI and found that there are positive correlations on EBIT impact from each. The
> one with the most impact on the bottom line is tracking well-defined KPIs for
> gen AI solutions"
> "only 1 percent of company executives describe their gen AI rollouts as 'mature.'"
Same source. **The KPI result is direct support for outcome 3, and it converges
with ST-29.**

**W-4 · ⚠️ The 2026 headline figure looks stronger than W-1 and is weaker.**
> "Nearly three-quarters of high performers report fundamentally redesigning
> workflows because of their AI use, up from 55 percent last year. By comparison,
> just one-quarter of other respondents report doing so."
> "they are twice as likely as others to say that their senior leaders demonstrate
> commitment to AI initiatives and to report that their organizations have defined
> processes to measure the impact of those initiatives."
McKinsey 2026, n=1,719. **The 2026 report publishes no regression, no R², and
never uses the word "correlated". The 73%-vs-25% is a raw cross-tabulation of two
self-reports from one respondent.** McKinsey's own framing of the conclusion is
experiential: "These are all practices that, in our experience, reinforce one
another." **This is exactly the figure a deck would upgrade into causal advice.**

**W-5 · Census finds the same relationship on 117,000 firms and names both
confounders. The best slide available for teaching the correlation trap.**
> "Regression analysis shows a robust positive correlation between firm commercial
> performance and the breadth of AI integration, including functional deployment,
> task-level use, and operational investment."
> "We underscore that these associations are descriptive and do not imply causal
> relationships. The observed correlations may be driven by unobserved firm-level
> heterogeneity, such as superior management practices, that simultaneously
> facilitates AI adoption and enhances performance. Furthermore, reverse causality
> remains a concern: firms with high performance or sales may simply possess the
> resources necessary to finance and implement sophisticated AI systems."
Census CES-WP-26-25, April 2026, >117,000 firms.
**Reverse causality is the live alternative explanation for W-1, W-2 and W-4:
profitable firms can afford to redesign workflows and to put a CEO on AI
governance. Put W-1's footnote and W-5's disclaimer side by side and an audience
of spend-approvers derives the lesson themselves.**

**W-6 · The practice with the largest association is *encouraging use* — and
training without encouragement is associated with smaller gains.**
> "Even in workplaces that neither encourage use nor provide enterprise tools or
> training, about 40% of workers have used AI chatbots at work … take-up rates
> almost double in workplaces with active employer initiatives. … adoption and
> reported benefits peak in workplaces that combine encouraged use with enterprise
> chatbots and training: 93% of workers in such settings report having used AI
> chatbots at work, 28% use them daily, and 19% report saving more than one hour
> per day"
> "Implemented individually, Encouraged use, Enterprise chatbots, and Training
> each raise extensive-margin take-up rates to 76%, 57%, and 69%, respectively."
> "By contrast, training and enterprise tools—when implemented without
> encouragement—are associated with smaller reported gains. This pattern is
> consistent with these initiatives being aimed at mitigating misuse rather than
> enhancing productivity."
Humlum & Vestergaard, 13 Mar 2026. **Authors' own hedge: "we interpret Equation
(1) as descriptive". And the same paper's causal half finds financial nulls
(C-10).** So the best-measured organisational-practice result in the literature is
descriptive, and it sits inside a paper whose identified estimates find no
financial effect.

**W-7 · Causal effect, suggestive mechanism. Gains concentrate in novices.**
> "we study the staggered introduction of a generative AI-based conversational
> assistant using data from 5,179 customer support agents. Access to the tool
> increases productivity, as measured by issues resolved per hour, by 14% on
> average, including a 34% improvement for novice and low-skilled workers but with
> minimal impact on experienced and highly skilled workers. We provide suggestive
> evidence that the AI model disseminates the best practices of more able workers"
Brynjolfsson, Li, Raymond, *Generative AI at Work*, NBER WP 31161, Apr 2023 rev.
Nov 2023, n=5,179. https://www.nber.org/system/files/working_papers/w31161/w31161.pdf
Effect is causal; the mechanism is "**suggestive**".

**W-8 · The only causal evidence bearing on a decision a leader makes: which
tasks you point AI at.**
> "For each one of a set of 18 realistic knowledge tasks within the frontier of AI
> capabilities … subjects using AI outperformed those not using AI, completing
> 12.2% more tasks and completing them 25.1% more quickly on average while also
> delivering solutions of significantly improved quality. However, for a complex
> managerial task selected to be outside the frontier, subjects using AI were 19%
> less likely to produce correct solutions"
Dell'Acqua et al., pre-registered, n=758. Task-level, single firm, BCG-partnered.
**Establishes nothing about EBIT.**

**W-9 · ⚠️ Deloitte's governance claim is asserted, not evidenced. It rhymes with
W-2, so it is tempting as corroboration. It is not corroboration.**
> "Enterprises where senior leadership actively shapes AI governance achieve
> significantly greater business value than those delegating the work to technical
> teams alone."
Deloitte 2026. **No n, no percentage, no test, no method attached to this
sentence.** It sits in a leader-FAQ narrative section.

**W-10 · NANDA on the successful 5%, with the best-worded correlation caveat in
the brief.**
> "Organizations that successfully cross the GenAI Divide do three things
> differently: they buy rather than build, empower line managers rather than
> central labs, and select tools that integrate deeply while adapting over time."
> "external partnerships with learning-capable, customized tools reached
> deployment ~67% of the time, compared to ~33% for internally built tools."
> "**Important Limitation:** These success rate differences may reflect
> organizational capabilities rather than implementation approach alone. …
> The correlation between external partnerships and success does not necessarily
> prove causation."
**That last sentence is quotable verbatim on a slide.** ⚠️ Also note NANDA is
promoting an agent-interoperability protocol that the report's own conclusions
recommend.

**W-11 · ⚠️ Where NANDA says returns actually came from — back office and external
spend, not headcount.**
> "some of the most dramatic cost savings we documented came from back-office
> automation."
> "these gains came without material workforce reduction. Tools accelerated work,
> but did not change team structures or budgets. Instead, ROI emerged from reduced
> external spend, eliminating BPO contracts, cutting agency fees, and replacing
> expensive consultants with AI-powered internal capabilities."
Its own caveat: "the sub-category and use-case breakdowns should be treated as
directional at best. Subcategories reflect synthesized notes and anecdotal
patterns, rather than precise accounting." **The report says 70% in one place and
~50% in two others for the same budget allocation. Do not cite that number.**
The "reduced external spend, not headcount" mechanism converges with ST-21 and
ST-22 and is worth teaching; the percentages are not.

#### Causation ladder — what each finding may be presented as

| Finding | Safe to present as |
|---|---|
| C-10 null earnings/hours (DiD, admin records) | **Causal null** |
| W-8 +12.2% / −19% (pre-registered RCT) | **Causal**, task level, says nothing about EBIT |
| W-7 +14% / +34% (staggered rollout) | Effect causal; mechanism suggestive |
| W-5 performance ↔ AI breadth (117k firms) | Correlation; reverse causality explicitly live |
| W-1 workflow redesign → EBIT | Correlation, R²=0.20, both variables self-reported |
| W-2 CEO governance → EBIT | Correlation, same model |
| W-6 encourage-use → adoption | Correlation, author-disclaimed |
| W-4 high performers redesign 3× | Raw cross-tab. **Weaker than W-1 despite looking stronger** |
| W-10 buy > build, 67% vs 33% | Correlation, self-selected n=52 |
| W-9 Deloitte senior leadership | **Consultancy assertion. Not evidence** |

**The one honest through-line the evidence supports.** Every practice associated
with financial impact — workflow redesign, senior ownership, measurement, breadth
of integration — is correlational, and all of it is plausibly downstream of firm
capability and profitability. The two sources with the best identification (Census,
and the Danish DiD) both refuse the causal reading, and Census names reverse
causality outright. The only causal evidence in the field is at task level, and it
says the decision that pays is **which tasks you point AI at**.

#### Stage model — defensible as structure, not as a funnel

No source follows one cohort through all stages, and no two of these share a
sampling frame. **A four-stage spine is legitimate teaching structure; the arrows
between stages must not carry numbers from different sources as if they compose.**

| Stage | Best-sourced datum | Source quality |
|---|---|---|
| Never started | 65% of non-adopters say AI is "not applicable to the business" | Census, representative, >117k firms |
| Piloted, never shipped | median 46% of projects abandoned pre-production; NANDA 20%→5% | S&P (n unpublished); NANDA (self-admittedly "directionally accurate") |
| Shipped, unadopted | "take-up rates almost double in workplaces with active employer initiatives" | Danish DiD-linked survey + admin records |
| Adopted, no measured benefit | 37% any EBIT, ~6% high performers; precise nulls on earnings and hours | McKinsey n=1,719; Danish DiD |

#### NOT ESTABLISHED — causes and practices

1. **Any experimental or quasi-experimental evidence that a governance or
   leadership practice raises AI financial outcomes.** Searched for field
   experiments on AI governance, CEO oversight and operating models. None found.
   **W-2 is correlational and must be taught as such.**
2. A frequency ranking of failure causes on a common representative base. No
   source provides one; any percentage carries its own frame.
3. The S&P "42% abandoned most initiatives, up from 17%" figure — primary is
   behind subscription; n and frame unpublished. Every carrier is journalism.
4. Gartner AI-failure statistics — issued without published sample or method.
5. McKinsey 2026's workflow finding as a published statistic (no R², no regression).
6. McKinsey 2026 Exhibit 11 per-practice percentages — SVG, labels not in page text.

### Controlled trials, and whether gains aggregate  ✅ researched 2026-09-12

**T-13 · The largest office-work RCT: time saved, nothing else changed. The
aggregation break in miniature, and the best single evidence for outcome 2.**
> "We present evidence from a field experiment across 66 firms and 7,137
> knowledge workers. … In the second half of the 6-month experiment, the 80% of
> treated workers who used this tool spent two fewer hours on email each week and
> reduced their time working outside of regular hours. Apart from these individual
> time savings, we do not detect shifts in the quantity or composition of workers'
> tasks resulting from individual-level AI provision."
> "treated and control workers replied to the same number of email threads,
> participated in the same number of Teams meetings, and completed the same number
> of Word documents."
> "Although we cannot measure productivity, the changing behaviors we see are
> consistent with workers independently exploring these new tools and saving time
> on individual tasks. Further research is needed to assess how co-inventions or
> team- or firm-level transformations may lead to broader changes"
Dillon, Jaffe, Immorlica & Stanton, *Shifting Work Patterns with Generative AI*,
arXiv:2504.11436v4, 13 Nov 2025; NBER WP 33795. Randomised, 66 firms, 7,137
workers (3,684 treated), 6 months. https://arxiv.org/abs/2504.11436
Its own measurement limit: "we do not observe the content of any work nor any
measures of productivity or performance evaluation."

**T-12 · Lab-to-field attenuation, stated by a team overlapping with the lab study
it deflates. The cleanest such statement available.**
> "we find that usage of a generative AI code suggestion tool increases software
> developer productivity by 26.08% (SE: 10.3%). We note that this estimate is
> substantially smaller than the 58% decrease Peng et al. (2023) find for the time
> to complete a software engineering task in the lab … Additionally, coding is only
> part of a software developer's job, so only some of the time saved on coding
> tasks may be spent on additional coding."
Cui, Demirer, Jaffe, Musolff, Peng & Salz. Three firm RCTs, n=4,867 developers,
2–8 months, real work. *Management Science*.
https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf
⚠️ Authors' own honesty: "Though each experiment is noisy"; "standard errors are
consistently large"; "only the effect on the number of pull requests is
statistically significant at conventional significance levels." **Outcomes are
pull requests, commits and builds — activity counts, not value.** A fourth
Accenture experiment was abandoned after a layoff hit 42% of participants and
gave "a negative and statistically insignificant point estimate of -39.18%".

**T-10 · ⚠️ THE METR SLOWDOWN IS GONE, AND ITS AUTHORS ABANDONED THE DESIGN.
Anyone citing the 19% slowdown today is a year out of date.**
> "Our early 2025 study found the use of AI causes tasks to take 19% longer, with
> a confidence interval between +2% and +39%. For the subset of the original
> developers who participated in the later study, we now estimate a speedup of
> -18% with a confidence interval between -38% and +9%. Among newly-recruited
> developers the estimated speedup is -4%, with a confidence interval between -15%
> and +9%."
> "we believe that the data from our new experiment gives us an unreliable signal
> of the current productivity effect of AI tools. The primary reason is that we
> have observed a significant increase in developers choosing not to participate
> in the study because they do not wish to work without AI"
> "30% to 50% of developers told us that they were choosing not to submit some
> tasks because they did not want to do them without AI. This implies we are
> systematically missing tasks which have high expected uplift from AI."
> "Wider adoption of AI has made it more difficult to measure task-level
> productivity"
METR, *We are Changing our Developer Productivity Experiment Design*, 24 Feb 2026.
57 developers, 143 repositories, 800+ tasks. https://metr.org/blog/2026-02-24-uplift-update/
**Both new intervals cross zero. Neither direction is settled — and the reason is
a measurement problem, which is outcome 3's argument arriving from an unexpected
direction.**

**T-8 / T-9 · The original METR trial, and its own list of what it does not show.**
> "16 developers with moderate AI experience complete 246 tasks … Before starting
> tasks, developers forecast that allowing AI will reduce completion time by 24%.
> After completing the study, developers estimate that allowing AI reduced
> completion time by 20%. Surprisingly, we find that allowing AI actually increases
> completion time by 19%"
arXiv:2507.09089, 12 Jul 2025. **n=16 developers.** The forecast-versus-outcome gap
(−24% expected, −20% believed afterwards, +19% measured) is the most useful part
for an executive audience: **the practitioners were wrong about their own
productivity in both directions, before and after.**
METR's Table 2 lists what its evidence does *not* demonstrate, including:
> "We do not claim that our developers or repositories represent a majority or
> plurality of software development work"
> "The slowdown we observe does not imply that current AI tools do not often
> improve developer's productivity—we find evidence that the high developer
> familiarity with repositories and the size and maturity of the repositories both
> contribute to the observed slowdown"

**T-1 / T-2 · The customer-support study: 15% published, not 14%, and it is a
staggered rollout, not an RCT.**
> published (QJE 140(2), 2025): "increases worker productivity, as measured by
> issues resolved per hour, by 15% on average, with substantial heterogeneity
> across workers."
> "Less skilled and less experienced workers improve significantly across all
> productivity measures, including a 30% increase in the number of issues resolved
> per hour. … In contrast, AI has little effect on the productivity of
> higher-skilled or more experienced workers. Indeed, we find evidence that AI
> assistance leads to a small decrease in the quality of conversations conducted by
> the most skilled agents."
Design: "We isolate the causal impact of access to AI recommendations using a
standard difference-in-differences regression". n=5,172 agents, GPT-3-era tool,
2020–21, single firm, single occupation.
https://danielle-li.github.io/assets/docs/GenerativeAIatWork.pdf
The generalisable mechanism, in the authors' words:
> "The greatest productivity gains may occur not where the AI system is most
> capable in absolute terms, but where its capabilities most effectively
> complement or exceed those of human workers."

**T-16 · 2026 RCT of agentic AI in live customer service: faster, and worse on
exactly the chats the AI handled.**
> "average chat duration declines by 16.8 percent in AI-eligible chats (p < 0.001)"
> "For AI-eligible chats … customer ratings decline by 0.412 points relative to
> those of control workers (p < 0.001). For AI-ineligible chats, by contrast …
> treated workers receive customer ratings that are 0.091 points higher"
> "In AI-eligible chats, the deployment of agentic AI substantially accelerates
> service completion, yet these gains in speed do not translate into a better
> customer experience."
Wang, Zhu, Feng, Lu & Jia, arXiv:2605.14830, May 2026. n=647 workers, 680,676
chats, Taobao, real customers. ⚠️ One author at Alibaba Group. ⚠️ No limitations
section found in the preprint.

**T-14 · A null average effect that hides active harm to weaker performers.**
> "We are unable to reject the null hypothesis that generative AI access has no
> impact … our point estimates suggest that high performers benefited by just over
> 15% from AI advice, whereas low performers did about 8% worse with AI assistance."
> "Exploratory analysis of WhatsApp interaction logs shows that both groups sought
> the AI mentor's advice, but that low performers did worse because they sought
> help on more challenging business tasks."
Otis, Clarke, Delecourt, Holtz & Koning. RCT, n=640 Kenyan entrepreneurs, 5
months, real businesses. *Management Science*.

#### The aggregation question — the chain breaks in four places

**Nobody has established that task-level gains aggregate to firm output. Each
break is named by a primary source.**

| Break | Evidence |
|---|---|
| **Lab → field** | The one team that ran both: field effect roughly half the lab effect (T-12) |
| **Task → job** | "we do not detect meaningful shifts in workers' tasks" (T-13); "coding is only part of a software developer's job" (T-12); "they may take their time savings as on-the-job leisure, which would increase welfare but not productivity" (T-21) |
| **Worker → firm** | No study measures both. The best firm-level RCT measures sales and explicitly not profit (T-24) |
| **Firm → economy** | "we report partial equilibrium short- to medium-run effects" (T-19); BLS does not measure it separately (T-22) |

**T-24 · The best firm-level randomised evidence measures top-line sales and says
so.**
> "Over 2023-2024, the platform integrated GenAI into seven business workflows …
> We find that GenAI adoption increases sales in most workflows, with effects
> ranging from no detectable impact to 16.3% … the implied annual incremental value
> is roughly $5 per consumer"
> "These figures should be interpreted cautiously: they assume that gains from
> different workflows can be summed without accounting for synergies or overlap …
> and capture top-line sales gains rather than bottom-line profitability or full
> return on investment."
> "our data do not allow us to estimate ROI directly—since we do not observe the
> full capital, engineering, inference, and organizational costs of GenAI
> deployment"
Fang, Yuan, Zhang, Donati & Sarvary, *Generative AI and Sales Productivity: Field
Experiments in Online Retail*, arXiv:2510.12049v6, 29 Jun 2026. Seven RCTs,
millions of users. ⚠️ Two authors consulted for, and one was employed by, the
partner company. ⚠️ v1 was titled "…Firm Productivity"; cite the current title.
**And the 16.3% is against no service at all, not against a human:**
> "Using Human Reply as the control … the GenAI Reply treatment shows no
> statistically significant differences in either sales or conversion, suggesting
> that the GenAI chatbot matches the quality of human service but does not
> outperform it."

**T-20 · The only attempt at the whole chain is a model calibration, and it
produces a small number its own author thinks is too high.**
> "these macroeconomic effects appear nontrivial but modest—no more than a 0.66%
> increase in total factor productivity (TFP) over 10 years."
> "even these estimates could be exaggerated, because early evidence is from
> easy-to-learn tasks … Consequently, predicted TFP gains over the next 10 years
> are even more modest and are predicted to be less than 0.53%."
Acemoglu, *The Simple Macroeconomics of AI*, NBER WP 32487, 2024; *Economic
Policy* 2025. **A theoretical model calibrated on other people's task-level
estimates. Not a measurement of aggregate output.**

**T-21 · The best empirical bridge is self-reported time savings, and it yields
about 1%.**
> "Workers report generative AI time savings equivalent to 1.6% of all work hours"
> "This suggests that generative AI may have increased labor productivity by up to
> 1.3% since the introduction of ChatGPT."
> "increased productivity by workers in some tasks will not increase measured
> productivity by as much if workers apply their saved time to less-productive
> activities"
> "our estimates will not capture firm-side adjustments to capital or work
> reorganizations"
Bick, Blandin & Deming, St. Louis Fed, 13 Nov 2025 (earlier: 27 Feb 2025, 5.4% of
hours → "a 1.1% increase in aggregate productivity"); survey NBER WP 32966.
**Nationally representative survey plus arithmetic. Not measurement of output.**

**T-22 · The statistical agency does not measure AI's productivity effect
separately.**
> "BLS implicitly captures AI use through its capital measure of software used in
> production."
US BLS, *Productivity and Artificial Intelligence*, page dated 8 Jun 2026.
https://www.bls.gov/productivity/articles-and-research/ai-and-productivity/home.htm

**T-23 · The productivity-paradox literature predicted this gap and names the
mechanism.**
> "Systems using artificial intelligence match or surpass human level performance
> in more and more domains … Yet measured productivity growth has declined by half
> over the past decade … We describe four potential explanations for this clash of
> expectations and statistics: false hopes, mismeasurement, redistribution, and
> implementation lags. While a case can be made for each, we argue that lags have
> likely been the biggest contributor"
> "their full effects won't be realized until waves of complementary innovations
> are developed and implemented. The required adjustment costs, organizational
> changes, and new skills can be modeled as a kind of intangible capital."
Brynjolfsson, Rock & Syverson, NBER WP 24001, 2017. **This is the theory behind
ST-31's "$1 tangible to $10 intangible" and behind C-8's 64%.**
⚠️ The J-curve paper's empirical findings are for software and computer hardware;
for AI it says only "the effects are small but growing". **Applying the J-curve to
generative AI is a prediction, not a finding.**

#### Headlines that are misquoted — a possible standalone section

**M-7 · ⚠️ The most spectacular "AI transforms knowledge work" result of 2024–25
was withdrawn for fabricated data, and circulated for six months first.** The
MIT materials-discovery paper claiming AI-assisted scientists found 44% more
materials. arXiv admin note (arXiv:2412.17866, v2, 20 May 2025):
> "Withdrawn by arXiv administrators due to concerns about the validity of the
> data and incomplete Institutional Review Board requirements"
MIT Department of Economics, Acemoglu & Autor, 16 May 2025:
> "we want to be clear that we have no confidence in the provenance, reliability
> or validity of the data and in the veracity of the research."
> "even in its non-published form, the paper is having an impact on discussions
> and projections about the effects of AI on science … the findings reported in
> this paper should not be relied on"
https://economics.mit.edu/news/assuring-accurate-research-record
**Candidate for its own slide.** It teaches the executive skill directly: the
question is not whether a number is impressive, it is who measured it and how.

| # | The claim as it circulates | What was measured |
|---|---|---|
| M-1 | "AI makes developers 19% slower" | 16 maintainers, own repos averaging 23k stars, early-2025 tools, CI +2% to +39%. **Superseded by the same authors** (T-10) |
| M-2 | "AI makes developers 55% faster" | One synthetic HTTP-server exercise, **70 completers**, CI 21–89%, no quality measure, authors employed by the tool's owner. Field figure is 26.08% (SE 10.3%) |
| M-3 | "14% customer-service gain" | Published figure is **15%**; staggered-rollout DiD, not an RCT; one firm, one occupation, GPT-3 era, 2020–21 |
| M-4 | "Consultants 19% worse with AI" | 19 **percentage points** (60–70% vs 79%), on one deliberately chosen task, against 18 tasks that showed gains. **The published abstract says "19%", which is where the error starts** |
| M-5 | "Writers 40% faster, 18% better" | One 27-minute writing task; authors say the design "may inflate our estimates" |
| M-6 | "GenAI raised sales 16.3%" | Against **no customer service at all**. Against a human: no significant difference |
| M-7 | "AI-assisted scientists found 44% more materials" | **Withdrawn. Fabricated data. Do not cite except as the cautionary case** |

#### NOT ESTABLISHED — trials and aggregation

1. **That task-level gains aggregate to firm-level output.** No study measures both.
2. **That they aggregate to economy-level output.** Only a model calibration exists.
3. **Firm-level ROI from any AI deployment, randomised or otherwise.** The best
   firm-level RCT says its data cannot estimate ROI.
4. **Whether low-skill or high-skill workers gain more.** Six studies point one
   way (support, writing, Copilot, BCG, and a 2026 online experiment closing
   three-quarters of an education gap); the Kenyan RCT points the other. Nobody
   reconciles them. ⚠️ The BCG authors note selective adoption may *widen* gaps.
5. **Whether measured gains persist.** Every study runs weeks to eight months. The
   longest, at six months, found time savings and no change in work composition.
   The support-study authors warn of a performance-target ratchet that could erase
   measured gains with no change in the technology.
6. **Whether AI shows a J-curve.** A prediction, not a finding.
7. Author limitations for the Alibaba, Cruces and BIS papers — retrieval blocked
   or truncated. Do not attribute limitations language to those three.
8. **BIS: AI adoption raises labour productivity ~4%** (12,000+ EU/US firms, IV on
   survey data, BIS WP 1325, 23 Jan 2026). ⚠️ **Page truncated to 125 characters on
   fetch. Re-verify by hand against the PDF before this goes on a slide.**

### Attribution — how value is credibly credited to AI  ✅ researched 2026-09-12

Ray's flag, and outcome 3 stands on it. It did **not** come back empty.

#### The requirement, from outside AI where the problem is older

**A-1 / A-2 · Without a comparison group there is no impact estimate. Full stop.**
> "Simply put, without a comparison group that yields an accurate estimate of the
> counterfactual, the true impact of a program cannot be established."
> "A valid comparison group (1) has the same characteristics, on average, as the
> treatment group in the absence of the program; (2) remains unaffected by the
> program; and (3) would react to the program in the same way as the treatment
> group, if given the program."
Gertler, Martinez, Premand, Rawlings & Vermeersch, *Impact Evaluation in
Practice*, 2nd ed., World Bank/IDB, 13 Sep 2016, ch.3 pp.51–52.
https://openknowledge.worldbank.org/handle/10986/25030

**A-13 · ⚠️ The World Bank calls before/after a "counterfeit" counterfactual.
This is the line that kills most corporate AI ROI claims.**
> "it is useful to discuss two common, but highly risky, methods of constructing
> comparison groups that many times lead to inappropriate ('counterfeit')
> estimates of the counterfactual: • Before-and-after comparisons …"
> "for a majority of programs implemented over a series of months or years, this
> assumption simply does not hold."
> "the baseline outcome is almost never a good estimate of the counterfactual.
> That is why we consider it a counterfeit estimate of the counterfactual."
Same source, ch.3 pp.54–55.

**A-14 · Microsoft's experimentation team, in the exact words an executive will
use to object.**
> "The most common question we get as an organization learns about controlled
> experiments is 'why not measure the metric of interest, ship the feature, and
> then look at the delta?'"
> "Our experience is that external variations overwhelm the effects we are trying
> to detect. In sequential tests, or quasi-experimental designs, we try to control
> for known confounding factors, but this is extremely hard to get right."
Kohavi, Deng, Frasca, Walker, Xu & Pohlmann, *Online Controlled Experiments at
Large Scale*, KDD 2013, §3.1.
https://exp-platform.com/Documents/2013%20controlledExperimentsAtScale.pdf
Same paper: "Only one third of the ideas tested at Microsoft improved the
metric(s) they were designed to improve."

#### The two numbers to build outcome 3 on

**A-32 / A-33 · ⭐ Observational attribution is off by a factor of three against a
randomised test on the same data. 416% claimed, 77% real.**
> "the observational methods overestimate ad effectiveness relative to the RCT…
> The bias can be large: in half of our studies, the estimated percentage increase
> in purchase outcomes is off by a factor of three across all methods."
> "the conversion rate among unexposed users was 0.020%, implying an ICR of 0.084%
> and a lift of 416%. This estimate is more that five times the true lift of 77%"
> "When we naively compared exposed to unexposed users, we estimated an ad lift of
> 416%. … suggested a lift of 221%. Matching the groups based on their propensity
> score, estimated with a rich set of explanatory variables, gave us a lift of
> 102%. Compared to the starting point, we have gotten much closer to the true RCT
> lift of 77%."
Gordon, Zettelmeyer, Bhargava & Chapsky, *A Comparison of Approaches to
Advertising Measurement: Evidence from Big Field Experiments at Facebook*, MSI WP
18-113, 2018; *Marketing Science* 38(2), 2019. 15 experiments.
https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_18-113.pdf
Kellogg white paper v1.2, 14 Jul 2016, for the 416%/77% walk-through.
**A-34 · Five years, 663 experiments and deep learning later, the gap persists:**
> "Although DML performs better than SPSM, neither method performs well, even
> using flexible deep learning models… Overall, despite having access to
> large-scale experiments and rich user-level data, we are unable to reliably
> estimate an ad campaign's causal effect."
arXiv:2201.07055v2, 4 Oct 2022; *Marketing Science* 42(4).
**This transfers directly: it is the same problem, on better data than any
enterprise has about its own AI.**

**A-45 · ⭐ The ceiling. To distinguish a 10% ROI difference, the median campaign
needed to be 62 times larger.**
> "Twenty-five large field experiments with major U.S. retailers and brokerages…
> reveal that measuring the returns to advertising is difficult. The median
> confidence interval on return on investment is over 100 percentage points wide."
> "The median campaign would have to be nine times larger to reliably distinguish
> a wildly profitable campaign (+50% ROI) from one that broke even (0% ROI).
> Achieving more standard tolerances for investment decisions, such as a 10% ROI
> difference, requires the median campaign to be 62 times larger to possess
> adequate power—nearly impossible for a campaign of any realistic size."
Lewis & Rao, *The Unfavorable Economics of Measuring the Returns to Advertising*,
*QJE* 130(4): 1941–1973, 2015.
**This is why attribution works at task and workflow level and fails at the
enterprise P&L. It is a mathematical ceiling, not an execution failure.**

**A-44 · The arithmetic behind it.**
> "to increase the experiment sensitivity (detectable effect size) by a factor of
> 10, say from 5% delta to 0.5%, you need 10² = 100 times more users."
> "those that succeed improve key metrics by 0.1% to 1.0%, once diluted to overall
> impact."
Kohavi et al., KDD 2013 and KDD 2014 Rule #2.

#### What it costs when someone actually does it

**A-5 / A-6 / A-7 · A real enterprise holdout: 4,867 developers, 2–8 months, and
still short of power.**
> "These field experiments, run by the companies as part of their ordinary course
> of business, provided a random subset of developers with access to an AI-based
> coding assistant"
> "our analysis must confront challenges related to statistical power despite the
> large number of developers in the experiments."
Three ways it degraded, all in the same paper: the control group got access
anyway ("Shortly after a larger fraction of developers in the treatment group
started using it, the control group was also allowed access"); take-up diluted the
treatment ("only 44.2% of developers adopted Copilot in the first 29 weeks"); and
a reorganisation destroyed one arm ("abandoned by the company after Accenture laid
off 19,000 employees that same month … including 42% of the developers
participating in this experiment").
**The cheap end, for contrast (A-8):** METR got a clean answer with 16 developers
and 246 randomised tasks, at $150/hr with screen recording. It answers one narrow
question about one workflow.

#### What organisations actually do — mostly, they estimate

**A-27 · ⭐ NO survey in the literature asks whether a control group was used.
The absence is a first-class finding.** Full published instruments were checked:
MIT NANDA Appendix 8.3, Census BTOS AI supplement Appendix A Q23–Q35, Deloitte's
ROI question set, Wharton/GBK QSP2A. **None contains an item about control groups,
holdouts, randomisation or counterfactuals. The surveys ask *whether* ROI was
measured, never *how it was identified*.**

**A-17 · Under one in five track KPIs at all.**
> "less than one in five saying their organizations are tracking KPIs for gen AI
> solutions."
> "More than 80 percent of respondents say their organizations aren't seeing a
> tangible impact on enterprise-level EBIT from their use of gen AI."
McKinsey, Mar 2025, n=1,491.

**A-22 · BCG: 60% monitor no financial KPI for AI.**
> "60% of companies are failing to define and monitor any financial KPIs related
> to AI value creation"
Chart: "32% Not tracking yet / 28% Operational only / 16% Financial only / 24%
Operational and financial". BCG, *AI Radar: From Potential to Profit*, Jan 2025,
n=1,803 C-level. https://web-assets.bcg.com/0b/f6/c2880f9f4472955538567a5bcb6a/ai-radar-2025-slideshow-jan-2025-r.pdf
BCG on its own data: "We drew insights on AI maturity and value from self-reported
data provided by the respondents."

**A-23 · IBM: two-thirds of Chief AI Officers start projects they cannot assess.**
> "72% of CAIOs say their organizations risk falling behind without AI impact
> measurement. But 68% initiate AI projects even if they can't assess their
> impact—because the most promising AI opportunities are often the most difficult
> to measure."
IBM IBV, *Solving the AI ROI puzzle*, 13 Jul 2025, n=624, 22 countries.
And from the CEO study (n=2,000, 6 May 2025): "CEOs say only 25% of AI initiatives
have delivered expected ROI—and only 16% have scaled enterprise-wide."

**A-20 / A-21 · ⚠️ Deloitte's own series contradicts itself across two
consecutive quarters, and the contradiction is usable evidence.**
Q3 2024 (n=2,770): "Tracked return on investment 35%" and "41% of organizations
have struggled to define and measure the exact impacts of their Generative AI
efforts." Also: "although a majority (54%) of organizations are seeking efficiency
and productivity improvements, only 38% reported they are tracking changes in
employee productivity."
Q4 2025 (n=2,773): "Almost all organizations report measurable ROI, and one-fifth
(20%) report ROI in excess of 30%." **The question wording is the explanation:**
> "Q: ROI to date: **Estimate** the ROI to date for this specific initiative."

**A-24 · An executive saying on the record that it cannot be computed, and that
they proceed anyway.**
> "'Any technology that's a little over a year old, nobody's going to have a
> year's worth of data to do a backward-looking ROI,' said one tech company
> executive we interviewed. 'And with the fundamental and foundational changes
> Generative AI offers, it's very hard to even offer a forward-looking [total cost
> of operating] or ROI…'"
> "many forward-thinking organizations are implementing Generative AI without
> specific ROI targets as they realize they can't afford to get left behind"
Deloitte Q2, Apr 2024, p.8. Also: "'When it comes to Generative AI, for now, we
are doing qualitative assessments,' said the director of AI business development
and strategy at a technology company."

#### ⭐ The decision rule for outcomes 3 and 4 — four lines, auditable, and not ours

**A-50 · UK government's definition of a real saving. Directly usable as the test
a leader applies to any AI benefit case.**
> "Cashable savings are those which lead to a direct reduction (all other things
> being equal) in a department budget."
> "The savings are defined as: ● Release of cash that relates to an activity that
> has already happened ● Not just relocating or deferring costs ● Fairly calculated
> and clearly positioned ● Captured in year and accrue within period ● Net of any
> double counting ● Understood and seen as reasonable by an impartial third party."
Cabinet Office / HM Treasury, *Government efficiency savings technical note*, pp.1, 7.
https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1064110/government-efficiency-savings-technical-note.pdf
**Anything failing those lines is an estimate. The surveys show an estimate is
what almost everyone has.**

**A-51 · The Green Book's additionality test — for benefits the market would have
delivered anyway.**
> "Deadweight: Outcomes that would have taken place without any intervention."
> "Additionality: Outcomes that take place as a result of the intervention. For
> example, a proposal to achieve growth in a particular industry should consider
> how it is genuinely raising productivity over and above market trends."
> "Substitution: The extent to which firms substitute one type of labour for
> another to benefit from an intervention, without increasing employment or output."
HM Treasury, *The Green Book 2026*, §4.17, §7.18.

**A-3 · UK Magenta Book adds the condition that usually binds for AI.**
> "The intervention effect is sufficiently large to be distinguished from expected
> 'noise' in the data."
> "To meet these requirements often requires building the evaluation design into
> the intervention design"
**A-46 · And the timing, which is the whole of outcome 3:**
> "baseline data – data collected before the intervention – will need to be
> collected early … Without appropriate data collection or data access planning an
> evaluation may be impossible, severely limited, or unnecessarily expensive."
HM Treasury, *Magenta Book*, Mar 2020, ch.2 p.78 and p.111.

#### Methods table — what each buys and costs

| Method | Requires | Costs | Cannot establish |
|---|---|---|---|
| Randomised holdout | Denying the tool to a control group for months | 4,867 devs over 2–8 months, still "noisy" | Survive control-group leakage, low take-up, or a reorg |
| Task-level A/B | A randomisable task stream, objective timing | 16 people, 246 tasks — the cheap end | Learning effects past the window; volunteer bias |
| Staggered rollout + DiD | Rollout timing not chosen by outcome; parallel trends | Long pre-period, many units | Parallel trends — "there is no way for us to prove" |
| Synthetic control | Clean donor units, long pre-window, low volatility | Meta asks 25+ pre-periods over 20+ geo-units | Effects near the size of the outcome's own noise |
| Geo experiment | Switchable by geography, all else held constant | Power analysis before launch | Anything if other activity moves |
| **Before/after vs baseline** | Only a baseline | Cheapest of all | **Attribution. "Counterfeit" counterfactual** |
| Matching / propensity | Rich observables + an untestable assumption | Data-heavy | Validation. 416% → 102% against a true 77% |
| Mix modelling | Independently varying inputs, enough data points | 156 weekly points for 20+ channels | Causality except "under certain narrow conditions" |
| Telemetry on the workflow | Logging | Cheap, no counterfactual included | **Productivity.** Measures activity only |
| Theory-based evaluation | An articulated mechanism | "Time consuming, resource intensive" | **A net effect size or an ROI number** |

**A-15 · Why telemetry is not the answer.**
> "Myth: Productivity is all about developer activity. This is one of the most
> common myths… working longer hours may signal developers having to 'brute-force'
> work to overcome bad systems"
> "it cannot be measured by a single metric or dimension."
Forsgren, Storey, Maddila, Zimmermann, Houck & Butler, *The SPACE of Developer
Productivity*, ACM Queue 19(1), 2021.

#### Sourced traps — each one a candidate quiz item

| Trap | The sourced statement |
|---|---|
| Baseline captured after the fact | "the baseline outcome is almost never a good estimate of the counterfactual" |
| Before/after passed off as attribution | "external variations overwhelm the effects we are trying to detect" |
| Early adopters volunteer | "treated agents already had higher resolutions per hour prior to AI model deployment (2.0 chats) relative to never-treated agents (1.7)" |
| Novelty decay | A 4.7% click lift that "were decreasing rapidly day over day" and would have shipped user dissatisfaction. Microsoft, arXiv:2102.12893 |
| Self-report substituted for measurement | "precise null effects on earnings and recorded hours"; "85% of chatbot users reallocate saved time to other job tasks"; adopters report "savings of about 3% of their work hours" |
| Believing the self-report over the data | "developers expected AI to speed them up by 24%, and even after experiencing the slowdown, they still believed AI had sped them up by 20%" |
| Individual gains claimed as enterprise gains | "An important limitation of above research and much of the literature on AI and productivity is the near total focus on individual work." Microsoft, Jul 2024 |
| Double counting | "avoid double-counting"; "Net of any double counting" |
| Savings with no spend falling | "Not just relocating or deferring costs" |
| Market trend banked as benefit | "Deadweight: Outcomes that would have taken place without any intervention" |
| Peeking and stopping early | "we are exposed to false positives due to multiple testing" |
| Underpowered null read as "no effect" | "policy makers might close down a program that, in fact, benefits children" |

#### ⚠️ Cross-source correction — Stanford's 1:10 figure

**ST-31 quotes the playbook: "for every $1 of tangible tech investment, companies
spend up to $10 on intangibles".** The attribution research could not find a
primary supporting that as a **spend** ratio. Brynjolfsson & Yang's 10:1 is
**intangible assets to IT assets** — a market-value correlation, not spending.
> "Analyses of 800 large firms by Brynjolfsson and Yang (1997) suggest that the
> ratio of intangible assets to information technology assets may be 10 to 1."
The nearest primary statement on spend is "for every dollar of IT there are
several dollars of organizational investments". **Use the ERP breakdown instead,
which is concrete and verified:**
> "the average spending on computer hardware accounted for less than 4 percent of
> the typical start-up cost of $20.5 million, while software licenses and
> development were another 16 percent of total costs. The remaining costs included
> hiring outside and internal consultants to help design new business processes and
> to train workers in the use of the system."
Brynjolfsson & Hitt, *Beyond Computation*, *JEP* 14(4), Fall 2000.
**So ~80% of an ERP programme was neither hardware nor software. That is the
same claim the playbook wanted, with a source that holds.**

**A-40 · And the lag, which is why measuring at 12 months understates.**
> "While short-term benefits were about what would be expected if they had
> 'normal' returns, long-term benefits were substantially larger: from 2 to 8 times
> as much as short-term benefits."
⚠️ Three published values across versions (2–5×, up to 5×, 2–8×). **Pin the
citation to the version quoted.**

#### Verdict — the answer to Ray's hard question

A credible attribution is buyable, and the literature is explicit about the price:
a control condition designed in **before** rollout, a baseline recorded **before**
anyone touches the tool, and a window long enough to outlast novelty. What cannot
be bought at any price is a credible attribution **after the fact**. So the choice
is not between a rigorous method and a quick one. It is between a designed
experiment and a number that is wrong by an unknown multiple in an unknown
direction.

And the scope is bounded by arithmetic, not diligence: effects worth chasing are
small against business noise, halving the detectable effect quadruples the sample,
and Lewis & Rao's 62× says enterprise-level ROI attribution is out of reach for
almost everyone. **Attribution works at the workflow. It fails at the P&L.** That
is the honest thing to teach, and it makes outcome 3 a demand for baselines on one
workflow rather than a demand for an ROI model nobody can build.

#### NOT ESTABLISHED — attribution

1. **Any survey asking firms whether they used a control group, holdout or
   randomised design.** Four full instruments checked. A genuine hole in the
   literature, not a retrieval failure.
2. **Any documented named enterprise running a randomised holdout for a
   non-coding AI deployment.** All three RCTs found are developer studies, plus the
   customer-support DiD. Searched finance, legal, marketing, service operations.
3. A required measurement period in months for a knowledge-work intervention.
4. A primary sentence stating "$10 organisational per $1 IT" as a spend ratio.
5. The Solow "computers everywhere except in the productivity statistics" line in
   its original 1987 source. **Do not attribute a wording to Solow.**
6. IBM 2026 CEO Study ROI figures — a circulating "72% have clear metrics"
   conflicts with the 2025 report's 68%. Treat 2026 IBM ROI figures as unverified.
7. **Figures traceable to no primary, which must not be used:** "84% see ROI but
   only 20–30% can prove it"; "only 29% can measure ROI confidently"; "average
   enterprise ROI of 5.9%"; "89% adopted but only 23% can measure ROI"; Meta's
   circulating "200,000 users per group / 2–4 weeks" holdout thresholds.

### Where value shows up, disclosed numbers, and the cost side  ✅ researched 2026-09-12

#### ⭐ The anchor case — Klarna. The whole course in one company.

**D-1 · In the audited 20-F, with its measurement source named. The rare good
disclosure.**
> "In February 2024, we launched our AI assistant in partnership with OpenAI. Our
> AI assistant has handled 80% of customer service chats in the year ended
> December 31, 2025 (according to our service chat log data), with no drop in
> consumer satisfaction levels since its introduction (according to internal
> consumer satisfaction surveys)."
Klarna Group plc, Form 20-F FY2025.
https://www.sec.gov/Archives/edgar/data/2003292/000200329226000007/klar-20251231.htm
**Note it is a volume share, not a saving.**

**D-2 · On the earnings call, a dollar figure and an FTE-equivalent, no method.**
> "it used to do about 700 full-time jobs. Now it is doing about 853 full-time
> jobs of a saving of $60 million."
Sebastian Siemiatkowski, CEO, Klarna Q3 2025 call, 18 Nov 2025. No baseline, no
definition of a "full-time job", no derivation of $60m.

**D-3 · ⭐ And the audited customer-service expense line WENT UP in the same year.**
> "Customer service and operations expenses for the year ended December 31, 2025
> increased by $4 million, or 2%, compared to the year ended December 31, 2024.
> Cost increased at a slower pace than volumes, with volumes up 32% year-over-year
> and transactions up 25% year-over-year, indicating continued operating leverage."
Audited line: **2023 $240m → 2024 $203m → 2025 $207m.** And in the one year the
cost actually fell, the filing does not credit AI:
> "This decrease was primarily driven by a decrease in customer service costs as
> we continued to make significant efforts to optimize and manage such costs."

**Nobody lied.** The call reports a counterfactual; the statement reports what was
spent. The filing claims **operating leverage against growth**, not absolute
saving. **The question to teach is not "what did AI save?" but "against what
baseline, and who audited it?"**

**D-4 · ⚠️ The rebalancing, stated carefully.** The CEO conceded quality slipped:
"As cost unfortunately seems to have been a too predominant evaluation factor…
what you end up having is lower quality." **Media interview, not official
reporting** (Bloomberg, May 2025). The 20-F asserts "no drop in consumer
satisfaction levels" and describes a "dual-track approach of combining broad and
continuing implementation of scalable AI in customer service with high-quality
human support." **Present as rebalancing, not abandonment — the AI share went up
(700 → 853 FTE-equivalent) while humans returned for complex work.**

#### The second teaching artefact — a denominator that excluded the work

**D-5 · ⭐ Presto Automation: "85% non-intervention" while humans typed the order.
The SEC opened a formal investigation.**
10-K FY2023 (11 Oct 2023):
> "Presto Voice currently achieves an 85% non-intervention rate on average,
> meaning that restaurant staff does not need to intervene in 85% of the orders
> placed… We have achieved an approximately 95% non-intervention rate at certain
> locations."
> "Our systems currently use a human agent (located offsite of the restaurant) to
> enter, review, validate and correct orders received by Presto Voice"
> "we had 137 full-time employees … and 149 contractors, consisting primarily of
> human agents supporting our HITL approach, who are primarily located in the
> Asia-Pacific region."
Four months later, the 10-Q (21 Feb 2024):
> "Pending the completion of that roll out, locations that use our AI technology
> currently use human agent intervention, including entering the order, in all
> instances."
> "the SEC had commenced a formal investigation into disclosures that the Company
> had made regarding certain aspects of its AI technology."
https://www.sec.gov/Archives/edgar/data/1822145/000155837023016336/prst-20230630x10k.htm
**"Restaurant staff" was the denominator. The offsite contractors were not counted,
and there were more contractors than employees. Always ask what the denominator
excludes.**

#### ⭐ The structural finding: where a number lives predicts how rigorous it is

**Quantified AI *benefits* live in CEO letters, prepared remarks and analyst
answers. Audited filings quantify AI's *costs* precisely and its benefits not at
all.**

| Costs, audited and precise | Benefits, unaudited |
|---|---|
| SAP restructuring **€3.2bn** (20-F) | SAP: "can save up to 90 minutes per consultant and day" — **"can" plus "up to" is a ceiling with no baseline** |
| Chegg goodwill impairment **$635.4m** (10-K) | IBM **$4.5bn** "productivity savings" — CEO letter and call, no baseline |
| Intuit restructuring **$300m** — **AI never named as the cause** | IBM **45%** developer gain — "reporting productivity gains", i.e. self-report |
| HP **$650m** restructuring cost | HP **$1bn** "gross run rate savings by end of fiscal 2028" — forward-looking, **gross, not net of the $650m** |
| CBA: AI appears as a cost — "investment in technology to support infrastructure, resilience and AI capabilities" | Sysco **$100m** "cost-savings program enabled by AI-driven process improvements, automation initiatives, and operating efficiencies" — no baseline, no period, no split |

**D-9 · ⚠️ IBM's $4.5bn is described as a stock and as a flow within three months.**
Annual Report: "approximately $4.5 billion in productivity savings **since the
beginning of 2023**." Q4 2025 call: "exiting 2025 with $4.5 billion of **annual run
rate** savings." Cumulative and annual run-rate are different quantities. Not
AI-only either — attributed to "simplifying our application and infrastructure
environments, aligning our teams by workflow and enabling a higher value-add
workforce through automation and AI-driven efficiencies." **The 10-K carries the
figure nowhere, and says instead:** "IBM's drive for greater agility,
productivity, flexibility and cost savings by continuously transforming with the
use of AI may not yield intended gains."

**D-10 · IBM's 45% is exactly the quantity METR showed is unreliable.**
> "We have more than 20,000 IBMers that are using Project Bob, reporting
> productivity gains averaging 45%"
Q4 2025 call, 28 Jan 2026. One quarter later the population grew to the entire
developer workforce, 45% stayed identical, and "reporting" was dropped. **Put this
slide next to the METR forecast/belief/measurement gap.**

**D-16 · JPMorgan defines "AI benefits" to include estimated revenue, then declines
to give the number.**
> "Benefits from AI include estimated growth in revenue, cost reduction and
> savings from risk reduction, such as fraud, that are directly attributable to AI
> initiatives"
Asked for the figure, Dimon: "we're not going to give you information which I think
puts us at a competitive disadvantage… you're going to have just, part of you has
to trust me, I'm sorry." 8-K EX-99.2, 23 Feb 2026; official transcript 13 Jan 2026.

**D-17 · ⭐ How it should be written. Use as the counter-example.**
> "Agentic messaging resolve rate¹ … 86% … FY26
> ¹ Percentage of customer conversations initiated through the agentic chatbot
> channel that are successfully resolved without a human assisted servicing
> pathway."
Commonwealth Bank of Australia, FY2026 Full Year Results Presentation.
**A defined denominator, a defined success condition, in an investor document.**

**D-13 · The only fully auditable number came from a tribunal, not a company.**
> "In effect, Air Canada suggests the chatbot is a separate legal entity that is
> responsible for its own actions. This is a remarkable submission."
> "I order Air Canada to pay Mr. Moffatt a total of $812.02"
*Moffatt v. Air Canada*, 2024 BCCRT 149, 14 Feb 2024. Worked line by line.

**D-14 · McDonald's ended a 100+ restaurant AI test and published no number at
all.** "the technology will be shut off in all restaurants currently testing it no
later than July 26, 2024." ⚠️ **Franchisee memo, news-reported only** — no release,
8-K or 10-K passage found. **The absence is the finding: the company best placed to
measure told shareholders nothing.**

**D-6 / D-7 · Two disclosed failures, kept separate.** Zillow wrote down **$304m**
on inventory bought "at higher prices than our current estimates of future selling
prices" and wound down Zillow Offers with a 25% workforce reduction (8-K Ex-99.3,
2 Nov 2021) — an algorithmic business failing. Chegg wrote goodwill to zero,
**$635.4m**, and kept AI out of the causal sentence, mentioning "Google's roll out
of AI Overviews" only in MD&A — **AI disrupting a company, not an AI project
failing.** Do not put these on the same slide.

**⭐ NOT ESTABLISHED, and the absence is a finding.** EDGAR full-text search
returns **0 hits** for "anticipated benefits of artificial intelligence" in 10-Ks
and for "may not realize the anticipated benefits of our artificial intelligence"
across all forms. **Companies disclose AI risk prospectively and AI wins
retrospectively, almost never the reverse.** Pfizer is the closest: "the risk that
anticipated cost savings from AI, automation and digital enablement efforts may not
be realized in the expected amounts or within expected timeframes" (10-Q, 4 Aug
2026) — and Pfizer quantifies no AI saving anywhere.

#### Where value shows up, when it does

**V-6 · ⭐ The cost/revenue proportion. Revenue is overwhelmingly aspirational.**
> "revenue growth largely remains an aspiration, with 74% of organizations hoping
> to grow revenue through their AI initiatives in the future compared to just 20%
> that are already doing so"
Achieving today / hope to achieve: efficiency and productivity **66/60** ·
decision-making **53/61** · reduce costs **40/65** · customer relationships
**38/60** · products and innovation **38/60** · **increase revenue 20/74**.
Deloitte, Jan 2026, n=3,235.

**V-1 / V-2 · McKinsey's function breakdown, and how to read it honestly.**
Cost decreases concentrate in supply chain (3% cut ≥20%, 10% cut 11–19%, 28% cut
≤10%), service operations (7/6/25) and manufacturing (1/8/28). Revenue increases
concentrate in marketing and sales (7% up >10%, 9% up 6–10%, 21% up ≤5%), product
development (8/10/18) and software engineering (11/5/15). McKinsey 2026, Exhibits
6–7, n=1,719. **⚠️ Even in the best function only ~41% report any cost decrease,
the largest band is the smallest effect, and non-reporters are excluded from the
chart — so the visual overstates the base rate.** And McKinsey's own threshold for
"meaningful" revenue is only 5% (2024 edition).

**V-8 / V-9 · Augmentation dominates, and predicted reductions did not arrive.**
Census: "Most users (66%) rely on AI solely to augment tasks, while AI-related
employment decreases are rare, occurring in only 2% of firms." McKinsey:
> "Just 14 percent of respondents from organizations using AI report that AI
> contributed to an overall decline in workforce size in the past year—less than
> half the 32 percent who, in last year's survey, expected workforce reductions
> over the same period."
McKinsey controlled for sample drift on this: "we also looked only at the 552
respondents who completed the survey in both 2025 and 2026 and the findings fully
reflected that of the overall sample." **So a cost case built on headcount removal
bets against the measured base rate.**

#### The cost side

**K-1 · The model is a small fraction of the system.**
> "only a tiny fraction of the code in many ML systems is actually devoted to
> learning or prediction … much of the remainder may be described as 'plumbing'."
> "Because a mature system might end up being (at most) 5% machine learning code
> and (at least) 95% glue code"
> "developing and deploying ML systems is relatively fast and cheap, but
> maintaining them over time is difficult and expensive."
Sculley et al. (Google), *Hidden Technical Debt in Machine Learning Systems*,
NeurIPS 2015. ⚠️ The 5%/95% is an estimate ("might end up being"), **not a
measurement — quote as expert testimony.**

**K-5 · ⭐ One in five organisations is already throttling AI use over running
cost. Inference cost is no longer theoretical.**
> "One in five respondents says their organization is limiting AI use because of
> operating costs, a share that is broadly consistent across organizations of
> different sizes and across many industries."
> "Twenty-eight percent of respondents say their organizations are spending more
> than 10 percent of their total enterprise-wide budget for information and
> communication technology on AI technologies."
McKinsey 2026, n=1,719, method published.

**K-12 · ⭐ Most of the NEW work AI creates is oversight, not production.**
> "only 41% of new tasks focus on 'productive AI use'… while the remaining 59%
> relate to 'AI implementation and oversight' (AI Quality Review, AI Integration,
> and AI Ethics & Compliance)."
> "about 25% spend more time on the same tasks they initially saved time on."
Humlum & Vestergaard, NBER WP 33777. Survey linked to administrative panel data.
**The strongest source on "the work moves to verification."**

**K-10 · Switching cost: prompts measurably regress on vendor model updates, and
you cannot stay put.**
> "we found that regression does exist over API updates: 58.8% of prompt + model
> combinations drop accuracy over API updates. Among them, 70.2% drop accuracy
> greater than 5%."
> "four out of these five models are already scheduled to be deprecated in 2024,
> effectively forcing application developers to switch"
Ma, Yang & Kästner (CMU), CAIN 2024, peer-reviewed. ⚠️ Narrow — 10 update pairs,
2 datasets. Good for the mechanism, not an effect size.

**K-3 · Leaders underestimate the data work, in RAND's interview data.**
> "Many interviewees (30 of 50) discussed persistent issues with data quality."
> "many interviewees (14 of 50) reported finding that senior leaders often
> underestimated the amount of time that it would take to train an AI model…
> They expect AI projects to take weeks instead of months"
⚠️ "80 percent of AI is the dirty work of data engineering" is **one interviewee's
phrase**, not a RAND measurement.

**K-18 · IT cost risk is fat-tailed.**
> "The analysis of a sample of 1,471 IT projects showed that the average cost
> overrun was 27% — but that figure masks a far more alarming 'fat tail' risk.
> Fully one in six of the projects in the sample was a Black Swan, with a cost
> overrun of 200%, on average, and a schedule overrun of almost 70%."
Flyvbjerg & Budzier, *HBR*, Sep 2011. ⚠️ **92% public sector, 83% US, mean project
$167m, and pre-AI.** Do not present as a private-sector or small-project figure.

**K-8 / K-9 · Overruns, with provenance flags.** DoiT survey (fielded by Sapio,
Feb 2026, 500 finance leaders, ±4.4pp): "79% experienced cost overruns in the past
12 months", mean overspend 30.9%, "only 15% can calculate AI ROI without
significant bottlenecks". ⚠️ **Vendor-commissioned — DoiT sells cloud cost
optimisation — but with a named independent fielder and published margin of
error.** Corroboration: 68% report at least some AI initiatives over budget, "Only
9% reported that over three-quarters of AI initiatives delivered measurable
financial returns" (WitnessAI via CFO Dive, ⚠️ dates and frame unstated).

**K-16 · ⚠️ RAND's "80% of AI projects fail" is a citation to a journalism piece,
not a RAND finding.** RAND's own contribution is the 65 interviews on *why*.
**The most commonly mis-cited number in this space.** The course must not repeat
it.

#### NOT ESTABLISHED — value, disclosure and cost

**Figures that must not be used:**
1. **BCG's "10-20-70"** cost split — no published sample or method, consultancy
   marketing. Use C-8/K-12 instead.
2. **"Share of AI project time spent on data preparation"** — circulating figures
   (Anaconda ~45%, CrowdFlower 60–80%, Kaggle ~15%) are vendor-published, disagree
   by 5×, no sampling frames.
3. **Any "3× TCO" claim** — almost certainly vendor content. Nearest real figures
   are the 30.9% mean overspend and the fat tail.
4. **Lumen's "~$50m AI savings"** — a misattribution. That figure is interest-expense
   saving from a bond coupon reduction. Lumen's own words attribute "over $400
   million in run rate savings" to "modernization and simplification", no AI.
5. **IBM "$3.5bn in productivity"** — not in any primary. Disclosed series is $2bn →
   $4.5bn → $5.5bn.
6. **IBM AskHR figures** ("94% handled", "HR 700 → 50") — zero hits across the 10-K,
   Annual Report and both transcripts. Press interviews and marketing only.
7. **Salesforce "9,000 → 5,000 support headcount", "$100m savings", "~85% of
   requests"** — absent from transcripts and the FY2026 10-K. Salesforce's stated
   figure is 64%. Traces to media interviews.
8. **ServiceNow "$350m annualized value", "2.3m hours"** — trace to a pre-earnings
   Fortune interview, absent from four checked earnings events.
9. **JPMorgan "$1bn–$1.5bn of value" / "$2bn"** — not in the 2023/2024/2025
   shareholder letters, the 2025 Annual Report, or the Investor Day deck.
10. **CBA "scam losses fell 76%", "call volumes down ~40%"** — newsroom media
    release only, not in investor materials.
11. **IBM's total loss on Watson Health** — IBM discloses a **$258m gain** on the
    asset sale and no impairment. The circulating "~$4bn spent, ~$1bn recovered" is
    not IBM's arithmetic. Do not attribute it to them.

**Genuine gaps in the literature:**
12. **The cost of migrating a production system between models or vendors.** K-10
    shows migration is forced; **nobody has priced it.**
13. **The cost of a parallel or shadow run, or the review burden.** K-12 gives task
    composition, not cost. **Nobody has costed the parallel run.**
14. **Any survey validating AI self-reports against measured financials.** None in
    this set does.
15. Exact per-function respondent counts behind McKinsey's Exhibits 6–7 (SVG).
16. Microsoft 365 Copilot's current list price from Microsoft's own live page
    (JS-rendered). The 2023 launch price was "USD30 per user, per month".

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

## Gate 1 — APPROVED 13 September 2026

Ray approved: **Outline A**; **both S5 and S6** as Representative Sections; and
**disclose the Workhelix interest**.

Two standing instructions recorded here because they bind every later stage:

**Language.** Narration passes through `no-ai-slop` and then `sg-english`, in that
order, **before** it is shown. Consequences that change how the script is written,
not just how it is edited:

- British spelling throughout. Dates as 13 September 2026. **S$ for Singapore
  dollars, and every other dollar qualified** — a bare "dollar" reads as S$ to this
  audience, so US figures are "US$60 million".
- No "lands" or "doesn't land" for succeeds or convinces. Ray had already called
  this; `sg-english` bans it independently.
- **This Course is recorded, so the spoken rules apply:** sentences of 15–20 words,
  at most one clause of subordination, **no parenthetical asides** and no dashes as
  rhythm. None of those can be heard.
- No rhetorical questions to the listener, no exclamation marks, no sports or
  military metaphor.
- Collective nouns take a singular verb: "the committee is".

**Klarna balance.** Ray recalls Siemiatkowski saying on *Diary of a CEO* that he
was misinterpreted. Verification dispatched 13 September 2026. Until it returns,
S6 must not assert the "Klarna reversed course on AI" narrative. The distinctions
to keep separate, because they are not the same claim: he was misquoted; he was
quoted correctly but the conclusion drawn was wrong; he changed his mind; he is
managing a reputational problem. Findings land under `### Klarna — balance`.

## Outline

**Teaching Strategy: problem-first.** Fixed by Ray's direction to open on the 95%
and ask why. Its failure mode is that problem-first can frustrate beginners — not
a live risk here, because the audience already has the problem.

**Minutes are an estimate and stay one until Narration exists (gate 2).**
Budget: 30 min × 135 effective wpm ≈ 4,050 words.

### Outline A — evidence ladder  ⬅ APPROVED 13 September 2026

**33 slides / 30 minutes / 8 sections.** All slides built 13 September 2026. Five assessment moments; S7 has none.

| Section | Slides | Min | Teaching intent | Sources | Narration | Slides |
|---|---|---:|---|---|---|---|
| S1 · The number everyone quotes | 1–4 | 3 | Open on the provocation and take it apart honestly | R01, R02 | drafted | built · for review |
| S2 · What the evidence agrees on instead | 5–7 | 3 | Replace one weak figure with a convergence; plant the self-report problem | R03, R05, R06, R07, R33, R34 | drafted | built · for review |
| S3 · The value was never stuck in the model | 8–12 | 5 | The thesis: organisation, not technology | R08, R09, R10 | drafted | built · for review |
| S4 · Which stage are you stuck at | 13–17 | 5 | **Outcome 1.** A diagnosis they can run on their own portfolio | R00, R06, R08, R12 | drafted | built · for review |
| S5 · Why a working model does not move the accounts | 18–23 | 5 | **Outcome 2.** The measured mechanism and the four breaks | R11, R12, R13, R18, R19, R20 | drafted | built · for review |
| S6 · One company, read two ways | 24–29 | 4 | The anchor case, balanced; where a number lives predicts its rigour | R22, R23, R24, R25, R39 | drafted | built · for review |
| S7 · Can value be attributed at all | 30–31 | 3 | **Outcome 3.** Yes at the workflow, no at the accounts | R27, R28, R29, R32, R35 | drafted | built · for review |
| S8 · The next ninety days | 32–33 | 2 | **Outcome 4.** A prioritisation decision and a four-line test | R30, R31, R04, R09 | drafted | built · for review |

**All 33 slides drafted: 3,512 words.** Composing S5 and S6 split two slides that carried
more than one idea and added S6's missing quiz, which took the course from 30 to 33.

At a raw 150 wpm the script runs **23.4 minutes** of speech. Five quiz pauses and
the visual beats should carry it to roughly 26 to 28 minutes. **That is inside 30
and I am not going to pad it.** The measured effective rate is 3,512 words over 30
minutes, or about 117 wpm.

### Outline B — Klarna as the running case

Same opener, same outcomes, same duration. Klarna becomes the spine rather than
section 6: introduced at minute 3, returned to in every section, with each stage
of the diagnosis illustrated on one company before generalising.

**Its failure mode, which is real.** It over-fits one example. Klarna is fintech
customer service — a single function, in a single sector, with an unusually
aggressive public posture. Generalisation to a manufacturer or a hospital gets
asserted rather than evidenced, and the Census and Danish data get demoted to
footnotes precisely where they are the strongest material available. It would be
a more engaging 30 minutes and a less defensible one.

**A third Outline would be manufactured.** Concept-first is the obvious candidate
and it contradicts an approved decision — it moves the 95% out of the opening
slot. Offering it as a live option would be padding.

## Representative Section for gate 2

**Proposed: S5 · Why a working model doesn't move the P&L.**

The most demanding section by every test the workflow names. Joint-largest
allocation at 5 minutes. Densest evidence — two causal studies, a task-composition
finding, and a four-step chain that has to read clearly as a diagram rather than a
list. It is outcome 2, which is the course's core claim. And its quiz is the
hardest to write, because the correct answer is a null result and the plausible
wrong answers are all things executives already believe.

S1 would look beautiful and prove nothing; it is a number and a correction.
**S6 (Klarna) is the honest alternative** — it carries the most complex on-slide
composition, a three-way comparison between a call, a filing and an expense line.
If the worry is layout rather than argument, S6 is the better sample. Say which.

## Narration

One block per slide. The build reads these, so the numbering must match
`slides.py`. Every block opens with a connecting sentence from the previous slide.
A narrator must never read a title aloud to bridge.

**Both language passes applied:** `no-ai-slop` then `sg-english`. Recorded
delivery, so sentences run 15 to 20 words with one clause of subordination at
most. No parenthetical asides and no dashes, because neither can be heard.

### S1 · The number everyone quotes

#### 01 · AI Value Management

**Sources:** [R00]
**Time:** 0:21  ·  40 words at 117 wpm

**Narration:**
Welcome to AI Value Management, a thirty-minute session for business leaders.
It is about why the value you were promised has not reached your accounts.
We will start with the most quoted statistic in enterprise AI, and take it apart.

#### 02 · Ninety-five per cent of AI pilots fail

**Sources:** [R01], [R00]
**Time:** 0:43  ·  83 words at 117 wpm

**Narration:**
You have almost certainly heard this figure quoted at you in the past year.
It comes from a July 2025 report by MIT's Project NANDA.
The headline travelled further than the report did.
Before we ask why AI value is not realised, we should establish whether this number says what people think.
So consider the question on screen, and choose an answer.
Take a moment.

The figure counts organisations, not pilots.
Hold that distinction, because it changes the size of the problem considerably.

#### 03 · It counts organisations, not pilots

**Sources:** [R01]
**Time:** 0:48  ·  94 words at 117 wpm

**Narration:**
The report measured something narrower.
Ninety-five per cent of organisations were getting zero return on their investment.
That is a statement about companies, not about projects.
The report also published its own funnel for task-specific tools.
Sixty per cent of organisations evaluated such tools.
Twenty per cent reached a pilot.
Five per cent reached production.

Five out of the twenty that piloted therefore made it through.
On the report's own numbers, the pilot failure rate is seventy-five per cent.
That is still poor. It is twenty percentage points better than the figure in circulation.

#### 04 · The report relabelled its own finding

**Sources:** [R01], [R02]
**Time:** 0:57  ·  111 words at 117 wpm

**Narration:**
The slip began inside the document itself.
One paragraph after that funnel, the report describes a ninety-five per cent failure rate.
Its own measure was organisations reporting no return, which is a different claim.

Three further things belong on the record.
The report defines success as something users or executives remarked upon, not something measured.
Its appendix gives a second, stricter definition based on measurable indicators. The two do not agree.
The sample was fifty-two organisations interviewed and a hundred and fifty-three leaders surveyed at four conferences.
The document calls itself preliminary findings and disclaims the positions of any affiliated employers.
The original link at MIT no longer serves the file.

### S2 · What the evidence agrees on instead

#### 05 · Four studies, four different questions

**Sources:** [R01], [R03], [R05], [R06], [R07]
**Time:** 0:57  ·  111 words at 117 wpm

**Narration:**
If that number is unreliable, the sensible response is to look at what else has been measured.
Four other sources ask adjacent questions, and each counts something different.
McKinsey surveyed one thousand seven hundred and nineteen respondents and asked about EBIT.
Deloitte surveyed three thousand two hundred and thirty-five leaders and asked which benefits they achieve today.
S&P Global asked one thousand and six firms what share of projects they abandoned.
The United States Census Bureau samples about 1.2 million businesses and asks whether AI is used.

Note the units. Organisations, respondents, projects and businesses are not interchangeable.
Most apparent disagreement between these figures is unit substitution rather than measurement error.

#### 06 · Where they converge

**Sources:** [R03], [R05], [R06]
**Time:** 0:57  ·  111 words at 117 wpm

**Narration:**
The units differ, so we should look for the question they answer in common.
All four bear on whether material financial impact can be evidenced.
McKinsey finds thirty-seven per cent report any EBIT impact, and about six per cent attribute five per cent or more.
Both figures are flat against the previous year.
Deloitte finds twenty per cent already growing revenue, against seventy-four per cent who hope to.
S&P finds forty-six per cent reporting no strong positive impact on any objective.

The methods and populations differ, and the answer is the same.
Only a small minority of organisations can evidence material bottom-line impact.
That share has not moved in a year.

#### 07 · Every figure here is a self-report

**Sources:** [R03], [R07], [R08], [R33], [R34]
**Time:** 0:47  ·  92 words at 117 wpm

**Narration:**
These sources share one property that outweighs their differences.
Every figure is something a respondent said, including the government statistics.
No study located for this session audits financial statements or deployment records.
Sixty per cent of firms in one survey monitor no financial indicator for AI at all.
In another, sixty-eight per cent of chief AI officers begin projects they cannot assess.

So the measurement problem is not only inside companies.
It runs through the evidence base on which the entire debate rests.
The final sections of this session return to it.

### S3 · The value was never stuck in the model

#### 08 · The difference was never the model

**Sources:** [R09]
**Time:** 0:52  ·  101 words at 117 wpm

**Narration:**
That is the state of the evidence. The more useful question is why.
Stanford's Digital Economy Lab examined fifty-one enterprise deployments across forty-one organisations.
Their conclusion is on screen, in their words.
The same technology and the same uses produced results measured in weeks for some and years for others.
The difference was the organisation, not the model.

The cases were selected because they succeeded, and the authors disclaim any claim to representativeness.
Its percentages describe successful deployments. They are not base rates for the economy.
We should also note that one author co-founded a company that sells AI benefit measurement.

#### 09 · Technology was the easiest part

**Sources:** [R09]
**Time:** 0:39  ·  76 words at 117 wpm

**Narration:**
If the organisation is the constraint, we should ask what specifically got in the way.
Across those fifty-one cases, seventy-seven per cent of the hardest challenges were not technical.
They were change management, data quality and process redesign.
Technology was described consistently as the easiest part.

An executive quoted in that study put it more bluntly.
All the hard work sits in process documentation and data architecture.
Do those two things, and the rest becomes straightforward.

#### 10 · Sixty-four per cent changed nothing else

**Sources:** [R08]
**Time:** 0:46  ·  90 words at 117 wpm

**Narration:**
That was interview evidence from companies that succeeded. Now consider a measurement.
The United States Census Bureau surveyed more than one hundred and seventeen thousand firms.
The sample is nationally representative and weighted.
Sixty-four per cent of firms using AI reported no institutional adjustments of any kind.
Training staff and developing new workflows each applied to about fifteen per cent.
Changes to data practices ran at seven to eight per cent.

Two-thirds of AI-using firms bought the tool and changed nothing around it.
This describes what firms did, measured directly.

#### 11 · The symptoms are not the causes

**Sources:** [R09], [R10]
**Time:** 1:01  ·  119 words at 117 wpm

**Narration:**
So the surrounding work is often skipped. The Stanford study ranked why that proves fatal.
Projects stuck in pilot, and an inability to prove return, appeared frequently.
Both are consequences rather than causes.
The leading cause was that the organisation was not ready to adopt, at thirty-five per cent.
Knowledge never captured follows at twenty-seven per cent, then legal or compliance blocks at eighteen.
Immature technology accounts for sixteen per cent.

RAND interviewed sixty-five practitioners and reached a sharper version of the same point.
Eighty-four per cent named business leadership's framing of the problem as a root cause.
RAND also discloses that most interviewees were engineers rather than executives.
The result may therefore be skewed towards identifying leadership failures.

#### 12 · Check your understanding

**Sources:** [R08], [R09]
**Time:** 0:27  ·  53 words at 117 wpm

**Narration:**
Before we turn that into a diagnosis, one question to test the distinction.
Consider the options on screen and choose.

The answer is the organisational one.
Immature technology accounts for sixteen per cent of failures in that study, and it is rarely the binding constraint.
The measured Census finding points the same way.

### S4 · Which stage are you stuck at

#### 13 · Four stages, four different failures

**Sources:** [R00], [R08], [R06], [R12], [R03]
**Time:** 0:44  ·  86 words at 117 wpm

**Narration:**
We can now put that evidence to work as a diagnosis you can run on your own portfolio.
Four stages sit between an idea and a benefit in the accounts.
Never started. Piloted but never shipped. Shipped but not adopted. Adopted with no measured benefit.

This structure is ours, assembled from four sources with different samples.
No single study follows one set of projects through all four stages.
So treat the stages as a diagnostic frame. Do not read the gaps between them as a funnel.

#### 14 · Stage one: it was never thought relevant

**Sources:** [R08], [R07]
**Time:** 0:47  ·  92 words at 117 wpm

**Narration:**
Start with the firms that never began, because the reason is not the one usually assumed.
Asked why they were not adopting, sixty-five per cent of firms said AI was not applicable to their business.
Lack of knowledge came second at twenty-two per cent, then privacy and security at twenty per cent.
Laws and regulations ranked among the least common barriers.

On nationally representative evidence, regulation is not what is holding adoption back.
Your governance obligations still bind, and the companion session covers them.
They are not the explanation for absent value.

#### 15 · Stage two: the pilot that never shipped

**Sources:** [R06], [R01]
**Time:** 0:52  ·  101 words at 117 wpm

**Narration:**
The second stage is the one most executives picture when they hear that AI is failing.
S&P Global reports that firms abandoned, on average, forty-six per cent of projects between proof of concept and adoption.
The share of companies abandoning most of their initiatives rose from seventeen to forty-two per cent in a year.
NANDA's funnel showed a comparable drop from pilot to production.

Two cautions. S&P has not published its field dates or question wording.
And a rising abandonment rate partly reflects a larger stock of projects available to abandon.
The direction is consistent across sources. The precision is not.

#### 16 · Stage three: shipped, and quietly ignored

**Sources:** [R12]
**Time:** 0:52  ·  101 words at 117 wpm

**Narration:**
The third stage is the least visible, because the project reports as delivered.
Danish researchers linked surveys of about twenty-five thousand workers to administrative records.
In workplaces that neither encouraged use nor provided tools, about forty per cent of workers used chatbots anyway.
Take-up roughly doubled where the employer actively encouraged use.
Where encouragement, enterprise tools and training combined, ninety-three per cent had used them.

Training and tools provided without encouragement were associated with smaller reported gains.
The authors describe this as consistent with mitigating misuse rather than improving productivity.
They also state that this part of their analysis is descriptive.

#### 17 · Stage four, and a question

**Sources:** [R03], [R12], [R00]
**Time:** 0:50  ·  97 words at 117 wpm

**Narration:**
The fourth stage is where most organisations that get this far now sit.
The tool is adopted, people report benefits, and no financial effect can be demonstrated.
Thirty-seven per cent report any EBIT impact, and about six per cent attribute five per cent or more.
The Danish study found precise null effects on earnings and recorded hours.

Test that combination now.
Read the situation on screen and choose the stage.

The answer is stage four. The tool is in use and the benefit is unevidenced.
Stage three would mean people are not using it. Here they are.

### S5 · Why a working model does not move the accounts

#### 18 · Two hours a week, measured

**Sources:** [R11]
**Time:** 0:42  ·  81 words at 117 wpm

**Narration:**
Stage four deserves a proper explanation, because it is the least intuitive.
The clearest evidence comes from a randomised experiment across sixty-six firms.
Seven thousand one hundred and thirty-seven knowledge workers took part over six months.
Among treated workers who used the tool, the saving was two fewer hours on email each week.
They also reduced time worked outside regular hours.

That is a measured benefit for each worker.
The question is what happened next, and the same study answers it.

#### 19 · And nothing downstream changed

**Sources:** [R11]
**Time:** 0:40  ·  78 words at 117 wpm

**Narration:**
The same study reports what happened next.
Treated and control workers replied to the same number of email threads.
They attended the same number of meetings.
They completed the same number of documents.
The authors detected no shift in the quantity or composition of anyone's tasks.

Two hours a week were released and no measurable output changed.
The authors are careful to say they could not observe productivity or performance directly.
What they could observe did not move.

#### 20 · A measured null on pay and hours

**Sources:** [R12]
**Time:** 0:50  ·  97 words at 117 wpm

**Narration:**
A second study tested the same question against national administrative records rather than telemetry.
The Danish work covered eleven occupations most exposed to chatbots.
Employers had adopted, workers reported benefits, and new AI-related tasks were widespread.
Using difference-in-differences, the authors estimate precise null effects on earnings and recorded hours.
They rule out effects larger than two per cent, two years after ChatGPT's launch.

A precise null has a specific meaning.
It does not mean nothing happened. It means any effect was too small to be distinguished from zero.
Note also that this paper has not been peer-reviewed.

#### 21 · Most of the new work was supervising the tool

**Sources:** [R12]
**Time:** 0:41  ·  79 words at 117 wpm

**Narration:**
The same Danish data shows where much of the saved time went.
Of the new tasks that AI created, only forty-one per cent involve using it productively.
The remaining fifty-nine per cent are implementation and oversight.
That covers quality review, integration work, and ethics and compliance.
About a quarter of users spend more time on the very tasks they initially saved time on.
Adopting the tool created work of its own, and most of that new work is supervision.

#### 22 · A faster task breaks down four times before the accounts

**Sources:** [R13], [R19], [R20], [R18], [R00]
**Time:** 1:11  ·  139 words at 117 wpm

**Narration:**
That pattern repeats at every level between a single task and the accounts.
The chain from a faster task to a better financial result breaks in four identifiable places.
First, laboratory to field. One team ran both, and the field gain was substantially smaller than the laboratory gain.
Second, task to job. Time saved on one task is not output gained, because most jobs contain many other tasks.
Third, worker to firm. No study located for this session measures both worker gains and firm profit.
Fourth, firm to economy. The United States Bureau of Labor Statistics does not measure AI's contribution separately.

The one model that estimates the whole chain projects very little.
It adds no more than two-thirds of one per cent to productivity over ten years.
Its author argues that even this figure could be too high.

#### 23 · Check your understanding

**Sources:** [R11], [R12]
**Time:** 0:38  ·  75 words at 117 wpm

**Narration:**
That is a lot of evidence pointing one way, so test what it does and does not show.
Choose the statement the research supports.

The correct answer is the third.
Individual time savings are well evidenced and firm-level financial effects are not.
The first option is contradicted by the trial, because the tools demonstrably save time.
The second understates what is known, because a precise null is a finding rather than an absence of research.

### S6 · One company, read two ways

#### 24 · Klarna published the number itself

**Sources:** [R22], [R39]
**Time:** 0:51  ·  99 words at 117 wpm

**Narration:**
All of that was general evidence. It helps to watch the problem happen to one company.
In February 2024 Klarna announced that its AI assistant handled two-thirds of customer service chats.
It described the assistant as doing the equivalent work of seven hundred full-time agents.
That figure came from Klarna, not from a critic.

Two details in that release are usually dropped.
It is an equivalence estimate, not a count of people made redundant.
And the release stated that customers could still choose to interact with live agents if they preferred.
Neither point survived into the story that followed.

#### 25 · What he said, and what was reported

**Sources:** [R39]
**Time:** 1:23  ·  162 words at 117 wpm

**Narration:**
Fifteen months later the chief executive gave an interview that was widely misreported.
His actual words were that cost had been too predominant a factor, and that what you end up with is lower quality.
Read carefully, he is describing how outsourced support had been organised.
He is not saying the AI assistant produced poor quality work.

The same article described a pilot of two people, and forecast headcount falling further to about two thousand five hundred.
Within ten days the story had become a reversal, a hiring spree, and an admission that AI had failed.
One outlet added customer dissatisfaction while citing another outlet rather than the interview.
He has pushed back five times in ten months, and the company denied it on the record.
He is careful about what he blames. He says the original article was balanced and he will not blame the journalist.
His objection is to the headline and to what was built on top of it.

#### 26 · The filings never wavered

**Sources:** [R22], [R39]
**Time:** 1:28  ·  171 words at 117 wpm

**Narration:**
There is a way to test which account is closer to the truth, and it does not involve trusting anyone.
Look at what the company said in documents signed under securities liability.
Full-time employees fell from five thousand five hundred to two thousand eight hundred across three years.
The decline is continuous, with no rebound in any year.
The filings attribute it to a strategic decision to use AI for efficiency, and expect headcount to keep falling.
That sentence is unchanged across three successive filings.
The share of chats handled by AI also rose, from sixty-nine to eighty per cent.
That rise runs from the listing prospectus to the next annual report.

One sentence about human agents did appear in a later filing and was absent from an earlier one.
That is the only textual trace of the pivot anywhere in the filings, and it concedes nothing.
So both things are true.
AI handles more of the work each year, and a human tier is being built on top of it.

#### 27 · A claimed saving and a smaller bill are different things

**Sources:** [R22], [R39], [R00]
**Time:** 0:57  ·  111 words at 117 wpm

**Narration:**
The filings settle the headcount question. The same filing also shows why a claimed saving needs checking.
The same annual filing claims about fifty-nine million United States dollars of cost savings from the assistant.
In the same document, the customer service and operations expense line rose by four million United States dollars, or two per cent.
Both statements appear in one filing, and both are true.
The saving is measured against a counterfactual. The expense line records what was spent.
The filing explains the gap as operating leverage, because volumes grew thirty-two per cent.
A claimed saving and a smaller bill are different things. Ask which one you are being shown.

#### 28 · A rate is only as honest as its denominator

**Sources:** [R24], [R25], [R00]
**Time:** 0:58  ·  113 words at 117 wpm

**Narration:**
A second company shows how far a figure can drift from the facts behind it.
Presto Automation reported an eighty-five per cent non-intervention rate for its drive-through ordering system.
Non-intervention meant that restaurant staff did not intervene.
Offsite human agents entered, reviewed and corrected the orders instead.
At the time, the company had more contractors than full-time employees.
The United States Securities and Exchange Commission opened a formal investigation into its disclosures about the technology.

Commonwealth Bank of Australia shows the alternative.
It publishes an eighty-six per cent resolve rate, and defines the denominator in a footnote.
For any rate you are shown, ask what the denominator is and who it leaves out.

#### 29 · Check your understanding

**Sources:** [R22], [R23], [R39]
**Time:** 0:46  ·  89 words at 117 wpm

**Narration:**
One question to test the Klarna case before we turn to attribution.
Read the situation on screen and choose.

The answer is the third.
The fifty-nine million figure is a saving measured against what costs would otherwise have been.
The eight hundred and fifty-three jobs figure is an equivalence estimate from an earnings call, with no stated baseline.
Only the expense line records what was spent, and the growth in volumes explains why it rose.
Read together, they show costs growing more slowly than the business, not costs falling.

### S7 · Can value be attributed at all

#### 30 · Off by a factor of three

**Sources:** [R27], [R28], [R35]
**Time:** 1:15  ·  147 words at 117 wpm

**Narration:**
That brings us to the question underneath all of this, which is whether the value can be attributed at all.
The discipline that has argued about this longest is advertising measurement.
Researchers ran fifteen large experiments at Facebook and compared methods on identical data.
Observational methods overestimated effectiveness, and in half the studies they were off by a factor of three.
A naive comparison of exposed against unexposed users suggested a lift of four hundred and sixteen per cent.
Careful statistical matching brought that down to one hundred and two per cent.
The randomised answer was seventy-seven per cent.

The World Bank's evaluation handbook names the underlying problem directly.
A baseline measured before an intervention is almost never a good estimate of the counterfactual.
They call before-and-after comparison a counterfeit estimate.
Microsoft's experimentation team says the same in industrial terms. External variation overwhelms the effect being sought.

#### 31 · It works at the workflow, not the accounts

**Sources:** [R29], [R32], [R00]
**Time:** 0:53  ·  104 words at 117 wpm

**Narration:**
Measurement also has a hard limit.
Across twenty-five large field experiments, the median confidence interval on return was over one hundred percentage points wide.
To distinguish a ten per cent difference in return reliably, the median campaign needed to be sixty-two times larger.
Halving the effect you wish to detect quadruples the sample required.

Attribution is achievable at the level of one workflow.
It is not achievable at the level of the enterprise accounts.
So the right demand is a baseline on one process, recorded before anyone touches the tool.
The guidance is explicit that this must be designed in before the intervention starts.

### S8 · The next ninety days

#### 32 · Four conditions that separate a saving from an estimate

**Sources:** [R30], [R31]
**Time:** 1:02  ·  121 words at 117 wpm

**Narration:**
Everything so far leads to a test you can apply without any technical knowledge.
The British government's definition of a cashable saving sets six conditions. Four matter most here.
The cash must relate to an activity that has already happened.
Costs must not merely be relocated or deferred.
The saving must be net of any double counting.
And it must be reasonable to an impartial third party.

Add one more test from the Treasury's Green Book, on additionality.
Deadweight describes outcomes that would have occurred without any intervention.
A benefit the market would have delivered anyway is not a benefit of your project.
Anything that fails these tests is an estimate. The surveys suggest an estimate is what most organisations hold.

#### 33 · What to do, and what to stop

**Sources:** [R00], [R30], [R32], [R04], [R09]
**Time:** 1:04  ·  124 words at 117 wpm

**Narration:**
The evidence supports five steps for the next ninety days.
Choose one workflow where the benefit would be visible in a budget line.
Record the baseline before anyone uses the tool, because it cannot be reconstructed afterwards.
Hold back a comparison group, even a small one.
Run it for at least a quarter, so that novelty has passed.
Name one person accountable for the benefit, not for the deployment.

It also supports stopping three things.
Stop funding tools without the surrounding process work, because two-thirds of firms do exactly that.
Stop accepting self-reported productivity as evidence of financial return.
Stop asking for enterprise-level return on investment, because that number cannot be produced honestly.
Ask instead which workflow you can measure properly, and start there.
