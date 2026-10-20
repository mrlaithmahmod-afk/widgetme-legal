# Financial model summary — AI property visualisation SaaS (UK-first)

Workbook: `/home/user/widgetme-legal/reports/Property_Visualisation_Financial_Model.xlsx`. It has 36 monthly periods and every output is a live formula driven by the `Assumptions` sheet. Values below were read back after a LibreOffice headless recalculation, which found 0 formula errors. Built 20 Oct 2026. Currency is GBP at **£0.755 per US$** (X-Rates Oct 2026 average). All inputs come from the research notes in this folder; where a figure was missing the model labels it ASSUMPTION.

## Bottom line
- **Base case:** month-36 subscription MRR is £83,175 (ARR £998,096) from 171.1 customers. EBITDA first turns positive in month 22 and stays positive from month 34. The £50k founder cash runs out in month 6, and the cash low point is −£135,592 in month 25. That means about **£135,592 of external funding** on top of the £50k.
- **Bear case:** month-36 ARR is £301,021 and the business never breaks even in 36 months. Gross margin is about 21.0% under pessimistic unit costs, and the funding need is £378,187 and still growing.
- **Bull case:** month-36 ARR is £2,270,461. Sustained break-even comes in month 22, the funding need is £66,813, and month-36 cash is £567,649.
- **Verdict:** the idea is viable but not easy. On base assumptions it is a ~£1m-ARR UK business by year 3 that needs about £185,592 in total funding (£50k founder plus £135,592 external). The base gross margin of ~70% holds only if human 2D-confirm/QA stays at ~10 minutes per plan at offshore rates. Under the pessimistic cost case (15-minute confirms, $35/h QA, more retakes, 50% pixel-streamed tours) every tier falls to roughly a 1–33% gross margin at full included usage, and the Bear scenario never recovers. So the business depends on QA-minutes-per-plan and the cost of the interactive viewer, not on LLM or image-model prices. Measure both in pilots before committing.

## Key assumptions (Base unless shown as Bear / Base / Bull)
| Input | Value | Label |
|---|---|---|
| Starting cash | £50,000 | ASSUMPTION (founder-funded) |
| Image gen per attempt (Low/Base/High) | $0.113 / $0.240 / $0.240 | VERIFIED Gemini Nano Banana 2.1 / Pro 4K |
| Attempts per accepted image | 2 / 3 / 4 | ESTIMATE |
| Standard / cinematic video $/s (Base) | $0.12 / $0.40 | VERIFIED Veo 3.1 Fast / Standard |
| Human QA rate $/h (Low/Base/High) | $15 / $25 / $35 | ESTIMATE (Upwork/offshore) |
| Human 2D confirm, min per plan | 3 / 10 / 15 | ESTIMATE (technical_feasibility §7) |
| Deliverable rejection rate | 5.0% / 15.0% / 25.0% | ASSUMPTION |
| Pixel-streaming h per hosted property-month | 0 / 2 / 6.65 | ESTIMATE; WebGL default |
| WorkOS SSO | $125/connection/month | VERIFIED |
| ODA Drawings SDK (Sustaining) | $7,500 then $4,500/yr | VERIFIED (reconfirm) |
| ISO 27001 | £20,000 yr 1, £10,000/yr after | ESTIMATE |
| Insurance (cyber+PI+PL) | £4,000/yr | ESTIMATE |
| Monthly churn Studio / Agency / Dev Pro / Enterprise (Base) | 3.5% / 2.5% / 1.0% / 0.6% | ESTIMATE (SaaS Capital GRR ~91%/95%; SMB 2.5–3.5%) |
| Launch month Studio / Agency / Dev Pro / Enterprise (Bear / Base / Bull) | 9/6/4; 10/7/5; 12/9/6; 18/12/10 | ASSUMPTION (no enterprise before M12 in Base) |
| Included-credit utilisation (Bear/Base/Bull) | 75.0% / 65.0% / 60.0% | ASSUMPTION |
| Founder salary; employer on-costs | £30,000/yr; 20.0% | ASSUMPTION; ESTIMATE |
| Bear scenario cost case | High (pessimistic); Base and Bull use Base costs | ASSUMPTION (conservative) |

Hiring is a set of step functions. Each role starts the month after its trigger is first met, measured on the previous month's value: Customer support / QA lead #1 at 20 customers; Senior engineer #1 at £15,000 MRR; Account executive #1 (developers) at £25,000 MRR; Founder salary uplift to market at £50,000 MRR; Senior engineer #2 at £50,000 MRR; Customer success #2 at 150 customers; Marketing manager at £60,000 MRR; Account executive #2 at £80,000 MRR; Graphics / 3D engineer #3 at £120,000 MRR; Customer success #3 at 300 customers.

## Unit cost per successful deliverable
Each deliverable cost is built from these components: LLM tokens, image gen, video gen, GPU, streaming, storage, CDN, CAD fees, human 2D confirm, human output QA and support allocation. It includes the case's rejection rate.

| Deliverable | Low £ | Base £ | High £ | Low $ | Base $ | High $ | Base human-labour share |
|---|---|---|---|---|---|---|---|
| Single room image | £1.22 | £5.39 | £10.81 | $1.62 | $7.14 | $14.32 | 79.3% |
| 5 room images | £3.05 | £10.86 | £20.86 | $4.04 | $14.39 | $27.63 | 63.2% |
| 2-bed flat (8 images + plan) | £5.00 | £16.22 | £30.85 | $6.62 | $21.48 | $40.86 | 60.7% |
| 4-bed house (19 images, 2 floors) | £10.57 | £34.79 | £66.08 | $13.99 | $46.08 | $87.52 | 57.6% |
| Interactive 3D property (WebGL tour, 1st month hosting) | £5.68 | £16.92 | £41.05 | $7.53 | $22.41 | $54.37 | 73.7% |
| 30s walkthrough video | £5.11 | £16.19 | £36.90 | $6.77 | $21.45 | $48.87 | 53.9% |
| 60s cinematic video | £11.87 | £54.16 | £134.36 | $15.72 | $71.73 | $177.96 | 18.2% |
| Developer marketing package (per house type) | £32.44 | £114.14 | £258.12 | $42.97 | $151.18 | $341.88 | 38.8% |
| 50-unit development (6 plan types) | £252.65 | £870.61 | £1,910.91 | $334.64 | $1,153.12 | $2,531.01 | 40.0% |
| 200-unit development (15 plan types) | £686.15 | £2,394.03 | £5,212.20 | $908.81 | $3,170.91 | $6,903.57 | 39.3% |
| Ongoing hosting per interactive property-month | £0.06 | £2.85 | £14.26 | $0.08 | $3.77 | $18.88 | — |

Human labour (the 2D confirm per plan plus output QA plus support) is **about 39–79% of base cost** for every deliverable except the 60s cinematic video, where Veo seconds dominate. LLM tokens cost cents per deliverable and do not matter.

Retry/failure sensitivity (Base case). Cost per success = fixed + repeatable/(1 − f), and rejected attempts re-incur generation and QA:

| Deliverable | £ @5% | £ @15% | £ @30% | £ @50% |
|---|---|---|---|---|
| Single room image | £5.27 | £5.39 | £5.63 | £6.18 |
| 5 room images | £10.21 | £10.86 | £12.18 | £15.18 |
| 2-bed flat (8 images + plan) | £15.09 | £16.22 | £18.50 | £23.69 |
| 4-bed house (19 images, 2 floors) | £32.22 | £34.79 | £40.03 | £51.90 |
| Interactive 3D property (WebGL tour, 1st month hosting) | £16.23 | £16.92 | £18.33 | £21.52 |
| 30s walkthrough video | £15.07 | £16.19 | £18.49 | £23.69 |
| 60s cinematic video | £49.16 | £54.16 | £64.32 | £87.36 |
| Developer marketing package (per house type) | £104.40 | £114.14 | £133.97 | £178.92 |
| 50-unit development (6 plan types) | £790.33 | £870.61 | £1,034.02 | £1,404.41 |
| 200-unit development (15 plan types) | £2,168.24 | £2,394.03 | £2,853.68 | £3,895.56 |

## Pricing recommendation
Keep the hypothesised price anchors, but sell **credits** instead of 'unlimited'. Every geometry-true output needs a human 2D confirm per plan, so single-image orders are labour-heavy and need a per-plan credit charge.

| | Studio | Agency | Developer Pro | Enterprise |
|---|---|---|---|---|
| List price / month | £149 | £499 | £1,499 | £5,000 |
| Included credits / month | 52 | 204 | 444 | 1,874 |
| Effective £ per included credit | £2.87 | £2.45 | £3.38 | £2.67 |
| Overage £ / credit | £4.00 | £3.50 | £3.00 | £2.50 |
| Setup fee | £0 | £500 | £1,500 | £7,500 |
| Extra development fee per plan type | £0 | £0 | £350 | £350 |
| Hosted interactive properties / SSO | 1 / 0 | 5 / 0 | 15 / 0 | 50 / 1 |
| GM at 100% of included usage (Base cost) | 57.9% | 53.7% | 72.5% | 64.7% |
| GM at 65% utilisation (Base cost) | 71.2% | 68.1% | 80.7% | 75.0% |
| GM at 100% usage (High cost) | 15.8% | 0.9% | 32.9% | 17.2% |
| Overage GM (Base cost) | 70.7% | 69.0% | 72.7% | 67.5% |

Hypothesis price points tested against the same usage mixes (GM at 100% usage, Base / High cost): Studio £149 57.9% / 15.8%; Agency £499 53.7% / 0.9%; Developer Pro £1,499 72.5% / 32.9%; Enterprise £3k 41.9% / -37.2%; Enterprise £5k 64.7% / 17.2%; Enterprise £10k 81.8% / 58.1%.

Monthly price needed for a target gross margin at 100% of included usage:

| Tier | 60% (Base) | 70% | 80% | 85% | 60% (High) | 70% | 80% | 85% |
|---|---|---|---|---|---|---|---|---|
| Studio | £157 | £214 | £334 | £464 | £323 | £440 | £686 | £955 |
| Agency | £582 | £791 | £1,235 | £1,718 | £1,279 | £1,740 | £2,717 | £3,778 |
| Developer Pro | £1,016 | £1,368 | £2,092 | £2,844 | £2,543 | £3,424 | £5,235 | £7,118 |
| Enterprise | £4,399 | £5,922 | £9,055 | £12,312 | £10,496 | £14,128 | £21,604 | £29,375 |

One-off or per-development prices needed for 70% / 80% GM at Base cost: 2-bed flat (8 images + plan) £59 / £92; 4-bed house (19 images, 2 floors) £126 / £197; Developer marketing package (per house type) £411 / £642; 50-unit development (6 plan types) £3,132 / £4,892; 200-unit development (15 plan types) £8,612 / £13,451.
An extra 50-unit development billed at £2,100 (6 plan types × £350) earns a 57.4% margin at Base cost and 7.9% at High cost. At High cost, price per plan type should rise to £500–600, which is the top of the competitor anchor of £300–£600 per plot type.

The recommended structure has five parts: (1) subscription with included credits; (2) overage priced above the included-credit rate; (3) setup fees that cover onboarding labour (Agency £500, Developer Pro £1,500, Enterprise £7,500); (4) per-development fees by plan type, because cost scales with plan types, not units; (5) WebGL viewers as the default, with pixel-streamed tours sold as a paid add-on, because streaming is the largest cost risk at High cost.

## Scenario outputs
| Metric | Bear M12 | Bear M24 | Bear M36 | Base M12 | Base M24 | Base M36 | Bull M12 | Bull M24 | Bull M36 |
|---|---|---|---|---|---|---|---|---|---|
| Subscription MRR | £875 | £9,587 | £25,085 | £4,882 | £31,822 | £83,175 | £15,167 | £77,200 | £189,205 |
| ARR | £10,494 | £115,039 | £301,021 | £58,588 | £381,862 | £998,096 | £182,005 | £926,399 | £2,270,461 |
| Customers | 4.5 | 29.8 | 66.5 | 18.3 | 79.6 | 171.1 | 46.4 | 172.0 | 352.2 |
| Gross margin | -6.5% | 19.6% | 21.0% | 65.0% | 70.9% | 72.7% | 72.4% | 75.1% | 76.4% |
| GM incl. support/CS salaries | -6.5% | -10.2% | 9.3% | 65.0% | 62.3% | 65.7% | 56.5% | 68.0% | 71.9% |
| Monthly EBITDA | −£9,003 | −£12,224 | −£15,111 | −£6,691 | −£3,110 | £14,890 | −£219 | £15,589 | £88,562 |
| Cash balance (cumulative) | −£66,878 | −£195,050 | −£378,187 | −£61,611 | −£134,713 | −£73,161 | −£39,179 | −£14,269 | £567,649 |
| Headcount | 1 | 2 | 3 | 1 | 4 | 7 | 2 | 7 | 10 |

| Scenario metric | Bear | Base | Bull |
|---|---|---|---|
| First month EBITDA ≥ 0 | Not reached in 36m | M22 | M15 |
| Sustained break-even month | Not reached in 36m | M34 | M22 |
| Cash first negative | M6 | M6 | M6 |
| Lowest cash balance | −£378,187 | −£135,592 | −£66,813 |
| Month of lowest cash | M36 | M25 | M16 |
| External funding needed | £378,187 | £135,592 | £66,813 |
| 36-month cumulative revenue | £299,788 | £1,082,159 | £2,674,063 |
| 36-month gross margin | 14.5% | 70.0% | 74.8% |
| Support/QA hire #1 starts | M22 | M14 | M9 |
| Engineer #1 starts | M30 | M19 | M13 |
| AE #1 starts | Not in 36m | M23 | M16 |
| First enterprise signing (fractional) | M18 | M12 | M10 |

## Milestones (first month reached; subscription MRR basis)
| Milestone | Bear | Base | Bull |
|---|---|---|---|
| £10k MRR | M25 | M16 | M11 |
| £25k MRR | M36 | M22 | M15 |
| £50k MRR | Not reached in 36m | M29 | M20 |
| £100k MRR | Not reached in 36m | Not reached in 36m | M28 |
| £250k MRR | Not reached in 36m | Not reached in 36m | Not reached in 36m |
| £1m ARR | Not reached in 36m | Not reached in 36m | M25 |
| £5m ARR | Not reached in 36m | Not reached in 36m | Not reached in 36m |

Example customer mix needed for each milestone, using the Base month-36 MRR mix and ARPA (Studio / Agency / Developer Pro / Enterprise = total): £10k MRR: 14 / 4 / 2 / 1 = 21; £25k MRR: 34 / 10 / 6 / 1 = 51; £50k MRR: 68 / 21 / 11 / 3 = 103; £100k MRR: 137 / 41 / 22 / 6 = 206; £250k MRR: 342 / 103 / 55 / 14 = 514; £1m ARR: 114 / 34 / 18 / 5 = 171; £5m ARR: 569 / 172 / 92 / 23 = 857. For scale, the UK has about 500 medium developers, 200 off-plan sellers and 25 nationals, and the researcher's SOM is about £1.25m ARR by year 3. £5m ARR would need about 23 enterprise accounts and about 92 Developer Pro accounts at today's mix. That is roughly the whole national-housebuilder universe plus about 18% of medium developers, so it is not credible as UK-only within 36 months.

## Solo-founder capacity
The founder is assumed to work about 180 h/month, with 35% (63 h) available for delivery operations: 2D confirm, QA, support and onboarding. The rest goes to building the product (6–15 engineering-months per technical_feasibility), selling and admin. Capacity = available minutes ÷ human minutes per unit, at Base cost and including rejects:

| Unit | Human minutes | Max per month (founder only) |
|---|---|---|
| Single room image | 13.2 | 286.9 |
| 2-bed flat (8 images + plan) | 30.3 | 124.8 |
| 4-bed house (19 images, 2 floors) | 62.1 | 60.9 |
| Interactive 3D property (WebGL tour, 1st month hosting) | 37.6 | 100.4 |
| Developer marketing package (per house type) | 134.7 | 28.1 |
| 50-unit development (6 plan types) | 1,083.5 | 3.5 |
| Studio customer-month at Base utilisation (+overage) | 73.9 | 51.1 |
| Agency customer-month at Base utilisation (+overage) | 265.3 | 14.2 |
| Developer Pro customer-month at Base utilisation (+overage) | 354.6 | 10.7 |
| Enterprise customer-month at Base utilisation (+overage) | 1,344.7 | 2.8 |

So a solo founder can deliver about 125 2-bed-flat packages or about 61 4-bed houses a month. That is roughly 51 Studio, 14 Agency, 11 Developer Pro or 2.8 Enterprise accounts on their own. In the Base scenario, delivery hours exceed founder capacity in month 14, at about 26 customers. The first support/QA hire, triggered at 20 customers, starts in month 14. QA overflow is costed in COGS at contractor rates throughout.

## Caveats
- Customers are fractional expected values. The model ignores tax, VAT timing, R&D tax credits, working capital and capex. MRR excludes overage, setup and per-development fees.
- The Base ~70% gross margin is above ICONIQ's ~45–55% average for AI products because COGS here excludes support/CS salaries (the memo row adds them back) and assumes offshore QA. If customers expect studio-style revisions, the business behaves like a tech-enabled service (40–55%).
- Prices, allowances, QA minutes, rejection rates, conversion and churn are hypotheses. Replace them with pilot data (time trials on 50 plans; Van Westendorp pricing tests; 3 paid developer pilots).
