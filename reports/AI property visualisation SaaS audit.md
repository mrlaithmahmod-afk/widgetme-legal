# Geometry-true visualisation survives only as a narrow wedge

**Bottom line.** You can build an AI-powered, white-label property visualisation SaaS today, but not the version the brief describes: a hands-off "upload anything, get accurate 3D" platform. Every commercial plan-to-3D product we examined still hides a human somewhere: a QA team, a reviewer who checks every AI result, or a capture step the vendor controls ([Planner 5D](https://tool.planner5d.com/b2b-floor-plan-recognition); [Getfloorplan](https://getfloorplan.com/for-personal-users); [Archilogic](https://www.archilogic.com/pricing)). Frontier LLMs still score close to random at turning images into floor plans ([Andon Labs Blueprint-Bench](https://andonlabs.com/evals/blueprint-bench)). The economics follow from that. Model and API spend is trivial: about **£4.76 of AI cost for a 2-bed flat package** ([pricing inputs](https://ai.google.dev/gemini-api/docs/pricing)). Human interpretation and QA are about **39–79% of the base cost of each deliverable**. That moves the true cost of a successful 2-bed package to **£16.22 (US$21.48)**, and the cost range is **£5.00–£30.85** depending on QA minutes and failure rates ([financial model](Property_Visualisation_Financial_Model.xlsx)). On base assumptions the business reaches **~£1.0m ARR by month 36**, first turns EBITDA-positive in **month 22**, and needs **~£185.6k of total funding**. On pessimistic unit costs it never breaks even and needs **£378k and rising**. The product is therefore more a tech-enabled service with a SaaS wrapper than pure software. It is defensible only if it owns the narrow problem nobody else has solved well: **geometry-true, compliance-ready marketing assets for off-plan developers, generated from CAD/IFC/vector PDFs, and sold through CGI studios and marketing agencies under their brand**. Our verdict is **conditional**. Do not build the platform yet. Run the 30-day validation programme in §20, and stop if QA minutes per plan or developer willingness to pay miss the thresholds set there. Our opportunity score is **49/100**.

**Evidence labels used throughout:**

- **[VF] Verified fact:** stated in a cited primary or official source.
- **[EST] Estimate:** analyst judgement or arithmetic derived from cited figures.
- **[ASM] Assumption:** a model input with no direct evidence.
- **[HYP] Hypothesis requiring testing:** the test that would settle it is named.

Currency is GBP, converted at **£0.755 per US$1** (X-Rates October 2026 average, 20 days of data, checked 20 Oct 2026) ([X-Rates](https://www.x-rates.com/average/?from=USD&to=GBP&amount=1&year=2026)). The source says its header timestamp is inconsistent and that the rate should be cross-checked against the BoE or ECB.

---

## 1. Executive summary: a real problem, a crowded shelf, a thin margin for error

The core finding is that the idea is technically buildable but commercially fragile. Five facts drive this.

**First, the "AI" is cheap but the human is not.** One Claude Sonnet 5.5 parse of a 4K plan costs about **US$0.05** [EST] ([Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing)). A 4K photoreal image costs **US$0.113–0.24** per attempt [VF] ([Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)). Even so, the base-case cost of each deliverable is **58–79% human labour** for stills and tours, because a person has to confirm the 2D interpretation and QA the output ([financial model](Property_Visualisation_Financial_Model.xlsx)).

**Second, the market already sells most of the pieces.** Getfloorplan sells a plan-in, 2D + 3D + 360 + render bundle, white-labelled, for **US$25–115 a set** [VF] ([Getfloorplan pricing](https://getfloorplan.com/pricing)). Realitiq already sells a CAD/BIM-in, white-label digital twin at **€400–600 per unit** [VF] ([Realitiq](https://www.realitiq.com/en/prices-for-projects/)). Planner 5D, Coohom, Homestyler and Collov all offer white-label APIs that a rival could wrap [VF] ([Coohom OpenAPI](https://open.coohom.com/pub/saas/open-platform/design-building); [Planner 5D API](https://support.planner5d.com/en/articles/15189751-planner-5d-b2b-api-technical-overview)).

**Third, compliance is tightening, and that favours a geometry-true product.** The New Homes Quality Code (March 2026) requires CGI and video not to mislead and restricts altered marketing material [VF] ([NHQB](https://www.nhqb.org.uk/the-code/part-1-selling-a-new-home/); [Walker Morris](https://www.walkermorris.co.uk/comment-opinion/the-new-homes-quality-code-march-2026-update-what-you-need-to-know/)). Rightmove requires AI and CGI "Enhanced Edits" to be labelled and accompanied by accurate images [VF] ([Rightmove Technical Guidelines](https://media.rightmove.co.uk/pdf/rightmove_technical_guidelines.pdf)). EU AI Act Article 50 has applied since 2 August 2026 [VF] ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations)).

**Fourth, the best-fit UK buyers are few and under pressure.** We estimate about **500 medium developers and about 200 off-plan sellers** [EST] ([market notes](https://www.londonstockexchange.com/news-article/RMV/annual-financial-report/17479517)). London private new-build sales in Q3 2026 were **the lowest since Q1 2009** [VF] ([Knight Frank](https://www.knightfrank.co.uk/research/article/2026/10/the-gulf-between-ambition-and-delivery-in-the-london-new-homes-market)).

**Fifth, the base financial case is a ~£1m-ARR business in three years, not a venture-scale one.** £5m ARR would need roughly the entire UK national-housebuilder universe plus about 18% of medium developers [EST] ([financial model](Property_Visualisation_Financial_Model.xlsx)).

| Question | Short answer | Label |
|---|---|---|
| Technically feasible? | Yes for conceptual images (9/10). Yes for structurally faithful renders with a human confirm step (7.5/10). Yes for navigable accurate 3D from IFC/DWG (8/10), with HITL from raster (6/10), and no when fully automated from raster (3/10) | EST ([technical notes](https://www.sciencedirect.com/science/article/pii/S0926580526004346)) |
| Profitable? | Base gross margin ~70% (36-month cumulative); sustained break-even in M34; ~£185.6k total funding | EST/ASM ([model](Property_Visualisation_Financial_Model.xlsx)) |
| Defensible? | Weakly. Wrappers are trivially copyable. Defensibility comes from a geometry-validation pipeline, compliance workflows, the channel and per-developer data, none of which exists yet | EST |
| Recommendation | Validate before building. If validated, wedge into CAD/IFC-first developer packs sold via studios and agencies | EST |

---

## 2. Technical feasibility verdict: accuracy comes from parsers and people, not from LLMs

### Scores by output class

The evidence separates three products that are often sold as one. The scores below are analyst judgement [EST] drawn from the cited benchmarks; no end-to-end public benchmark exists.

| Class | Score /10 | Demonstrated vs experimental | Basis |
|---|---|---|---|
| **A. AI conceptual images** (mood or style "inspired by" the plan) | **9** | **Demonstrated.** Text and image-to-image tools, generated video and Marble worlds all ship today | Image APIs widely available at US$0.03–0.24 per image [VF] ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)); commodity tools such as Interior AI and Collov [VF] ([Collov](https://www.collov.ai/pricing)) |
| **B. Structurally faithful renders** | **7.5** | **Demonstrated:** deterministic rendering from vector or BIM models (Blender, Unreal). **Experimental:** AI enhancement with *measured* geometry preservation (no public benchmark) | Image models score below random on layout [VF] ([Andon Labs](https://andonlabs.com/evals/blueprint-bench)); research says video models "still show deficiencies in 3D consistency" [VF] ([VideoGPA](https://arxiv.org/html/2601.23286)) |
| **C. Navigable, dimensionally accurate 3D** | **8** from IFC/DWG; **6** from raster with HITL; **3** fully automated from raster | **Demonstrated** for IFC/CAD and for raster with a human check. **Experimental** when fully automatic | Scanned-plan wall recall is 0.723 vs 0.974 for CAD-derived plans [VF] ([Automation in Construction 2026](https://www.sciencedirect.com/science/article/pii/S0926580526004346)); Planner 5D has a human review every AI result [VF] ([Planner 5D](https://tool.planner5d.com/b2b-floor-plan-recognition)) |

Recognition from clean plans is now good, but not good enough to skip review. On CAD-derived renderings of CubiCasa5k layouts, wall recall@0.5 is **0.974** with mean IoU **0.953**. On scanned versions of the same plans, recall falls to **0.723**, and only **50.4%** of walls reach IoU ≥ 0.85 [VF] ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0926580526004346)). The strongest 2026 vectoriser, Beike's FloorplanVLM, reports **92.52% external-wall IoU** and handles slanted and curved walls. It is trained on Chinese-market data, and we could not confirm that its weights are released [VF] ([arXiv 2602.06507](https://arxiv.org/abs/2602.06507)). Whether it degrades on UK, EU and US drafting conventions is a **[HYP]**. The test is to score 200 local plans, half clean and half scanned, on wall IoU, room-polygon F1, opening F1 and area error.

### Direct answers to the technical questions

| Question | Answer | Label / source |
|---|---|---|
| **Can Claude read floor plans?** | Claude can read the *semantics*: room labels, layer names, finish schedules, and pairing dimension strings with walls. It cannot be trusted as the geometry extractor. No published benchmark measures frontier LLMs on dimension OCR or vector extraction from drawings. On the nearest benchmark (photos to plan), Claude Opus 4 scored **0.286** against a random baseline of **0.279** and a human score of **0.547**, and agentic iteration "showed no meaningful improvement". Those models are now superseded, and no Opus 5.5 score exists | VF ([Blueprint-Bench](https://andonlabs.com/evals/blueprint-bench)); HYP for Opus/Sonnet 5.5. Test: a 300-plan dimension-OCR and endpoint-error eval, as in the technical notes |
| **Spatial reasoning over structured JSON?** | Strong. Claude Fable 5 scored 88.8% and Opus 4.8 87.5% on Snap's 3D spatial benchmark. The weak points are physical constraints and coherence | VF ([Snap](https://eng.snap.com/spatial_intelligence); [FloorplanQA](https://arxiv.org/abs/2507.07644)) |
| **Missing dimensions?** | Scale can be inferred from door widths, but a single door is accurate only to about **±10–15%**. Taking the median of several doors, or using a stated GIA, gives about **±3–5%**. A least-squares fit across OCR'd dimension strings gives about **±1–2%**. A commercial vectoriser (ARCHLine.XP) makes the user set scale manually | EST; VF for ARCHLine ([ARCHLine.XP](https://help.archlinexp.com/hc/en-us/articles/20856004418449-From-raster-to-BIM-Converting-floor-plans-to-3D-models)). HYP: compare methods on 200 plans with known scale |
| **Multi-storey?** | Storeys can be registered automatically by matching stair footprints and external outlines, but the user must confirm. Floor-to-floor height, roof form and riser count are usually absent from 2D plans. They must come from sections or elevations, or be labelled defaults. No academic benchmark exists | EST ([technical notes](https://arxiv.org/abs/2507.07644)) |
| **CAD/BIM?** | DWG, DXF and IFC remove the recognition problem: geometry is exact by construction. Wall, door and window classification from DWG layers is about **80–95%** correct [EST]. IFC typed entities give near-100% semantic fidelity on well-authored models [EST]. The tooling is ODA Drawings SDK (Sustaining tier US$7,500, then US$4,500/yr, permits SaaS) [VF], web-ifc (MPL-2.0) [VF] and ezdxf | VF ([ODA pricing](https://www.opendesign.com/pricing.md); [web-ifc](https://github.com/ThatOpen/engine_web-ifc)) |
| **Consistency across room views?** | Consistency is solved deterministically only when every view is rendered from one canonical 3D scene. Generative enhancement must be gated by edge-F1 and mask-IoU drift checks. Pure generated video (Veo and similar) is class A only | EST; VF that video models lack 3D consistency ([VideoGPA](https://arxiv.org/html/2601.23286)) |
| **Stairs and curved walls?** | Curved walls are newly handled by sequence models (FloorplanVLM). Stairs need riser and going data that plans rarely carry, and LLMs "fail to respect physical constraints" | VF ([arXiv 2602.06507](https://arxiv.org/abs/2602.06507); [FloorplanQA](https://arxiv.org/abs/2507.07644)) |
| **Does it work without manual 3D artists?** | Yes, without *3D artists*: a procedural builder plus Blender handles that work. No, without *humans*: a 2D confirm/edit step of about 3–15 minutes per plan is required for raster input [EST] | ([Planner 5D](https://tool.planner5d.com/b2b-floor-plan-recognition); [CubiCasa](https://www.cubi.casa/start-scanning-first-floor-plan/)) |

---

## 3. Complete system architecture: deterministic core, LLM at the edges, a human at stage 4

The only defensible architecture follows a **"geometry is truth" contract**. A canonical vector model, held as a JSON schema or an IFC subset, is the only source of geometry. Every render is derived from it. AI may change pixels but must pass automated drift checks. Every displayed measurement comes from the model, never from generated imagery [EST] ([technical notes, Planner 5D evidence](https://tool.planner5d.com/b2b-floor-plan-recognition)). This design follows directly from the evidence that image models alter structure. Collov users report added or erased walls and windows [VF] ([Trustpilot UK](https://uk.trustpilot.com/review/collov.ai)), and REimagineHome's own terms say its outputs are "not to scale" [VF] ([chez terms](https://chez.reimaginehome.ai/terms-of-use)).

| # | Stage | Recommended tech | Claude role | Expected first-pass accuracy [EST] | Cost per unit |
|---|---|---|---|---|---|
| 1 | Ingestion | File sniffing; PyMuPDF to separate vector from raster PDFs; ODA SDK for DWG; ezdxf; IfcOpenShell or web-ifc | None | ~99% format handling | ODA US$7,500 yr 1 [VF] ([ODA](https://www.opendesign.com/pricing.md)); APS ~US$1.50–3 per translation [EST/UNVERIFIED] ([Autodesk Flex](https://www.autodesk.com/buying/flex)) |
| 2 | Parsing | Vector: extract primitives directly. Raster: MitUNet-class segmentation or a FloorplanVLM-class VLM if licensable, plus PaddleOCR or docTR | **Haiku 5.5** maps layer and block names to canonical classes; **Sonnet 5.5** reads room labels | Vector 90–98% classification; clean raster 90–97% wall IoU; scans 70–85% | Sonnet parse ≈ US$0.05 (£0.04); batch ≈ US$0.026 [EST] ([Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing)) |
| 3 | Geometry reconstruction | Skeletonise, fit lines and arcs, snap junctions; least-squares scale fit; room polygons; storey registration (Shapely/CGAL) | **Sonnet 5.5** proposes pairings of dimension strings to wall segments, each verified numerically | Scale ±1–2% with dimensions; ±3–15% from doors alone | CPU only; negligible |
| 4 | **Human confirm/edit (mandatory for raster)** | Browser 2D editor with confidence overlays, one-click scale confirmation and storey alignment | None | Near-100% topological correctness after review | **3 / 10 / 15 min per plan** (Low/Base/High) at **US$15 / 25 / 35/h** [EST] ([model](Property_Visualisation_Financial_Model.xlsx)), about **£2–6 per plan type** [EST] ([Upwork](https://www.upwork.com/hire/architectural-rendering-freelancers/cost/)) |
| 5 | Structural validation | Rule engine: closed rooms, wall-thickness bands, openings contained in walls, door widths 0.6–1.0 m, stair rules, GIA reconciliation | **Haiku/Sonnet** write plain-English issue explanations only | Catches gross errors, but not plausible-but-wrong layouts | Negligible |
| 6 | Materials | Parse the finish schedule (PDF/XLSX) to room → surface → code; map codes to a curated PBR library (CC0 sources) via embedding search plus rerank | **Sonnet 5.5** extracts schedules and reranks matches | Untested [HYP]; needs a schedule-extraction F1 eval | Cents |
| 7 | Scene generation | Procedural builder: extrude walls, boolean openings, parametric doors and windows, slabs, simple roofs; furniture laid out by a collision/clearance solver; export glTF and IFC | **Sonnet/Opus** propose furnishing JSON, which the solver validates | Exact relative to the confirmed vector | ~1 GPU-h scene build, US$1.09–1.86 [EST] ([RunPod](https://www.runpod.io/pricing)) |
| 8 | Rendering | Blender headless: Cycles for hero shots, EEVEE for drafts; baked lightmaps plus Three.js/Babylon for the web | None | Exact geometry by construction | 4K Cycles still US$0.03–0.15 on an RTX 4090 at US$0.89/h; 30 s Cycles walkthrough US$7–13 [EST] ([Renderjuice](https://www.renderjuice.com/gpus/rtx-4090-for-blender)) |
| 9 | AI enhancement (optional) | Low-denoise (0.2–0.4) depth/canny-conditioned img2img, or instruction edit (Gemini image, gpt-image-2, or FLUX Kontext under a licence) | None | Drift not measured publicly; gate every frame | US$0.113 (Nano Banana 2.1 4K) to US$0.24 (Pro 4K) per attempt [VF] ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)) |
| 10 | QA | Automated edge-F1 and per-object mask IoU, base render vs enhanced; area re-measured from the model; human spot QA | **Opus 5.5** as an *advisory* visual judge only; **Haiku** for bulk triage (<US$0.001 per image) | Rejection threshold set from the §5 drift test | Haiku <US$0.001, Sonnet ≈US$0.007 per image [EST] ([Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing)) |
| 11 | Delivery | CDN-hosted glTF/KTX2 WebGL viewer (default); MP4 via Mux or Cloudflare Stream; optional Spark splats for context; pixel streaming as a paid add-on | **Haiku/Sonnet** write customer-facing summaries | n/a | R2 US$0.015/GB-month, free egress [VF] ([R2](https://developers.cloudflare.com/r2/pricing/)); pixel streaming US$1.82–2.82 per user-hour [VF] ([GameLift Streams](https://aws.amazon.com/gamelift/streams/pricing/); [Vagon](https://vagon.io/streams/pricing)) |

Claude should be kept out of five jobs: pixel-to-coordinate extraction, scale determination, wall endpoints, area values and structural judgements. Andon Labs observed agents "claiming success" while their output was wrong [VF] ([Andon Labs](https://andonlabs.com/evals/blueprint-bench)). Model routing should send bulk classification to **Haiku 5.5** (US$0.10/0.50 per MTok), schedule parsing and pairing to **Sonnet 5.5** (US$2/10), and hard ambiguous cases plus QA reasoning to **Opus 5.5** (US$4/20). **Fable 5.1** (US$10/50) is not needed in the hot path, and it also requires 30-day retention, which excludes it from zero data retention (ZDR) by default [VF] ([Claude models](https://platform.claude.com/docs/en/about-claude/models/overview); [data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)).

---

## 4. Model, API and licensing comparison: the licence column eliminates more options than the price column

Token and image prices hardly matter to unit economics. Licence and data terms decide which vendors can be used at all. Runway's terms let it train on your inputs and outputs under a perpetual licence. That is incompatible with promising enterprise customers "no training on your data" [VF] ([Runway Terms §4.4](https://runway.com/terms-of-use)). OpenAI shut down Sora 2 and its Videos API on **24 Sep 2026** "with no one-to-one replacement" [VF] ([OpenAI Sora 2 page](https://developers.openai.com/api/docs/models/sora-2)). That is a live example of vendor churn.

| Category | Option | Price (Oct 2026) | Commercial / white-label terms | Data / training | Verdict |
|---|---|---|---|---|---|
| LLM | Claude Haiku / Sonnet / Opus / Fable 5.x | US$0.10/0.50; 2/10; 4/20; 10/50 per MTok; batch −50% [VF] ([pricing](https://platform.claude.com/docs/en/about-claude/pricing)) | Customer owns outputs; white-label permitted. Must flow down the AUP and notify users that outputs may be inaccurate; publicity needs consent [VF] ([Commercial Terms](https://assets.ctfassets.net/5965pury2lcm/4e9p7xwZDo6mBgWfSyDsCV/907c229ef3ee22366fa66837419bde2c/Anthropic_T_Cs.pdf)) | No training on commercial data. First-party inference geo is `global` or `us` only, so EU/UK residency means Bedrock or Vertex [VF] ([data residency](https://platform.claude.com/docs/en/manage-claude/data-residency)) | **Use**, via Bedrock eu-west-2 for UK residency |
| LLM | OpenAI GPT-5.x | US$0.05–5 in / 0.40–30 out [VF] ([OpenAI pricing](https://developers.openai.com/api/docs/pricing)) | Customer owns output; account may not be resold. Output indemnity is lost if output is "modified, transformed, or used in combination" [VF] ([Services Agreement](https://openai.com/policies/services-agreement/)) | No training by default | Fallback |
| LLM | Gemini 4 Argon / 3.x Flash | Argon US$2/10 → **US$4/20 from 1 Dec 2026**; Flash doubles 1 Jan 2027 [VF] ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)) | Paid tier: no training. Free tier trains outside EEA/UK/CH [VF] ([Gemini terms](https://ai.google.dev/gemini-api/terms)) | Transient storage "in any country" | Price-rising; secondary |
| Image | Gemini Nano Banana 2.1 / Pro | US$0.113 / 0.24 per 4K image [VF] | Vertex indemnity covers "unmodified" output only [VF] ([Google terms](https://cloud.google.com/terms/service-terms)) | SynthID and Content Credentials are automatic and cannot be switched off [SECONDARY] | **Primary image engine** |
| Image | gpt-image-2 | US$0.165–0.211 high quality [VF] | As OpenAI above | — | Alternative |
| Image | FLUX (BFL) | API ~US$0.048/image; fal FLUX 2 US$0.012/MP [VF] ([fal](https://fal.ai/pricing)) | API includes commercial rights. Self-hosted [dev] needs a paid licence (reported US$999/month for 100k images), and no API resale [VF] ([BFL licence](https://bfl.ai/legal/self-hosted-commercial-license-terms)) | Training on outputs needs a separate licence | Use via API; self-host only with a licence |
| Image | Stability | Free under US$1M revenue; custom above [VF] ([Stability](https://stability.ai/license)) | Licence cliff at US$1M | — | Avoid as a core dependency |
| Video | Veo 3.1 Standard / Fast / Lite | US$0.40 / 0.12 / 0.08 per s at 1080p [VF] | Auto-signed Content Credentials | — | Class A cinematic only |
| Video | Kling 3.0 / Runway Gen-4.5 / Luma Ray 3.2 | US$0.112 / 0.12 / ~0.24 per s [VF] ([Kling](https://kling.ai/document-api/pricing/base/video.md); [Runway](https://docs.dev.runwayml.com/guides/pricing/)) | Runway: no user indemnity; **trains on inputs and outputs** [VF] | — | Exclude Runway's standard terms |
| Video | Sora 2 | **Shut down 24 Sep 2026** [VF] | — | — | Unavailable |
| Renderer | Blender headless | Free; GPU ~US$0.89/h (4090) [VF] ([RunPod](https://www.runpod.io/pricing)) | Output belongs to the user; GPL applies to the program, not to renders [VF] ([Blender FAQ](https://www.blender.org/support/faq/)) | — | **Default** |
| Renderer | Unreal Engine | US$1,850/seat/yr above US$1M revenue; **5% royalty over US$1M** for runtime apps licensed to third parties [VF] ([Epic](https://www.unrealengine.com/blog/we-are-updating-unreal-engine-twinmotion-and-realitycapture-pricing-in-late-april)) | Pixel-streamed SaaS is likely to trigger the royalty [EST; SOLICITOR] | — | Premium add-on after legal review |
| Renderer | Unity Industry | US$4,950/seat/yr [VF] ([Unity](https://unity.com/products/unity-industry)) | — | — | Not needed |
| Web 3D | Three.js / Babylon / Spark splats | Free; Spark is MIT [VF] ([Spark 2.0](https://www.worldlabs.ai/blog/spark-2.0)) | Splats are *not* dimensionally authoritative [EST] | — | Default viewer |
| CAD/BIM | ODA SDK; ezdxf; IfcOpenShell; web-ifc; LibreDWG | ODA Sustaining US$7,500 then US$4,500 [VF]; web-ifc MPL-2.0 [VF] | LibreDWG is GPL-3.0 copyleft [EST, unverified]; CubiCasa5K dataset likely **CC BY-NC** (non-commercial) [EST] | — | ODA + ezdxf + web-ifc |
| Streaming | GameLift Streams / Vagon | US$1.82/h (L4); US$2.16–2.82/h + ~US$20/month per app [VF] | — | — | Paid add-on only |

---

## 5. Proof-of-concept specification: what must be proven before a line of product code

**This PoC has NOT been executed.** No results exist. Every threshold below is a design choice [ASM], justified from cited evidence. They are not observations.

### Inputs and outputs

| Plan type | Input files | Required outputs |
|---|---|---|
| P1 Simple flat | Clean vector PDF of a 2-bed flat plus a finish schedule (XLSX) | Confirmed vector JSON; 3D floor plan; 8 room stills (furnished and unfurnished); WebGL tour; 30 s walkthrough |
| P2 Multi-storey house | Two-storey 4-bed, raster PDF per floor, one section drawing | As P1, plus storey registration, stairs, roof from section; 19 stills; 60 s cinematic |
| P3 Irregular layout | Plan with curved and slanted walls (non-Manhattan) | As P1, with a curved-wall fidelity report |
| P4 Poor scan PDF | Phone photo or 150–200 DPI scan of a paper plan, partial dimensions | As P1; scale inferred and flagged; HITL minutes logged |
| P5 IFC/CAD | IFC 2x3/4 model plus a DWG of the same scheme | As P2; semantic mapping report; cross-check of the IFC-derived model against the DWG |

Use **10 instances of each type (50 plans)**, drawn from real UK schemes with the owner's permission. Use of plans must be licensed: *Signature Realty* held that making AutoCAD versions and marketing from drawings without a licence infringed [VF] ([Bird & Bird](https://www.twobirds.com/en/insights/2017/uk/it-ip-law-bytes-apr17/copyright-architects-drawings)).

### Metrics and acceptance thresholds

| Metric | Accept | Kill / redesign | Justification |
|---|---|---|---|
| Wall IoU before HITL, P1/P5 | ≥ 0.95 | < 0.90 | CAD-derived benchmark mean IoU 0.953 [VF] ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0926580526004346)) |
| Wall recall before HITL, P4 | ≥ 0.72 | < 0.60 | Scanned benchmark recall 0.723 [VF] |
| Opening (door/window) F1 before HITL, P1 | ≥ 0.90 | < 0.80 | R2V reports ~90% precision and recall [VF] ([ICCV 2017](https://openaccess.thecvf.com/content_iccv_2017/html/Liu_Raster-To-Vector_Revisiting_Floorplan_ICCV_2017_paper.html)) |
| Topology after HITL (closed rooms, correct openings) | 100% | Any published error | The "dimensionally accurate" claim depends on it |
| Scale error | ≤ ±2% where dimensions exist; ≤ ±5% door-median | > ±5% | Least-squares fit ±1–2%; door-median ±3–5% [EST] |
| Room-area error vs ground truth (MAPE) | ≤ 3% | > 5% | Beats CubiCasa's claimed 3–5% error [VF] ([CubiCasa help](https://help.cubi.casa/en/articles/3352314-frequently-asked-questions-scanning-and-floor-plans)) and Archilogic's ±5% target [VF] ([Archilogic](https://help.archilogic.com/knowledge/best-practice-for-floor-plans)) |
| DWG layer → class accuracy (Haiku/Sonnet-assisted) | ≥ 90% | < 80% | Heuristic range 80–95% [EST] |
| **HITL minutes per plan (median)** | **≤ 5 clean; ≤ 15 scan** | **> 10 clean or > 20 scan** | The model's Base is 10 min and High is 15. Above that, every tier falls to a 1–33% gross margin [EST] ([model](Property_Visualisation_Financial_Model.xlsx)) |
| Render drift (structural edge displacement after AI enhancement) | ≤ 1% of image width | > 2% | Hypothesised 1–2% band [HYP] |
| Deliverable rejection rate | ≤ 15% | > 30% | Model Base 15%; cost per 2-bed rises from £16.22 to £18.50 at 30% [EST] |
| Cost per successful 2-bed package | ≤ £16.22 | > £30.85 | Model Base vs High [EST] |
| Claude dimension-string OCR exact match vs PaddleOCR+parser | Report only; adopt the better | — | No benchmark exists [HYP] |

### Minimal human-in-the-loop

The human confirms the **2D vector and scale once per plan type**: one known dimension, storey alignment and any flagged low-confidence regions. A **named customer approver** then signs off each asset before export. That approval is a compliance requirement in its own right (see §13). All other stages run without a human. Spot QA should drop to sampling only once the rejection rate is below 15% across 200 consecutive deliverables [ASM].

---

## 6. Generation unit economics: the human is ~60% of the cost, the model is noise

All figures come from the financial model's `Unit_Costs` sheet, built 20 Oct 2026 at **£0.755/US$** ([workbook](Property_Visualisation_Financial_Model.xlsx); [X-Rates](https://www.x-rates.com/average/?from=USD&to=GBP&amount=1&year=2026)). Each cost covers LLM tokens, image and video generation, GPU, streaming, storage, CDN, CAD fees, the human 2D confirm, human output QA and a support allocation, including that case's rejection rate. The three cases are:

| Case | Image cost per attempt | Attempts per accepted image | QA rate | Confirm time per plan | Rejection rate | Label |
|---|---|---|---|---|---|---|
| **Low** | US$0.113 | 2 | US$15/h | 3 min | 5% | VF prices / EST / ASM |
| **Base** | US$0.24 | 3 | US$25/h | 10 min | 15% | VF prices / EST / ASM |
| **High** | US$0.24 | 4 | US$35/h | 15 min | 25% | VF prices / EST / ASM |

### Cost per successful deliverable

| Deliverable | Low £ | Base £ | High £ | Low $ | Base $ | High $ | Human share (Base) |
|---|---|---|---|---|---|---|---|
| Single room image | £1.22 | £5.39 | £10.81 | $1.62 | $7.14 | $14.32 | 79.3% |
| 5 room images | £3.05 | £10.86 | £20.86 | $4.04 | $14.39 | $27.63 | 63.2% |
| 2-bed flat (8 images + plan) | £5.00 | £16.22 | £30.85 | $6.62 | $21.48 | $40.86 | 60.7% |
| 4-bed house (19 images, 2 floors) | £10.57 | £34.79 | £66.08 | $13.99 | $46.08 | $87.52 | 57.6% |
| Interactive 3D (WebGL, first month) | £5.68 | £16.92 | £41.05 | $7.53 | $22.41 | $54.37 | 73.7% |
| 30 s walkthrough | £5.11 | £16.19 | £36.90 | $6.77 | $21.45 | $48.87 | 53.9% |
| 60 s cinematic | £11.87 | £54.16 | £134.36 | $15.72 | $71.73 | $177.96 | 18.2% |
| Developer package (per house type) | £32.44 | £114.14 | £258.12 | $42.97 | $151.18 | $341.88 | 38.8% |
| 50-unit development (6 types) | £252.65 | £870.61 | £1,910.91 | $334.64 | $1,153.12 | $2,531.01 | 40.0% |
| 200-unit development (15 types) | £686.15 | £2,394.03 | £5,212.20 | $908.81 | $3,170.91 | $6,903.57 | 39.3% |
| Hosting per interactive property-month | £0.06 | £2.85 | £14.26 | $0.08 | $3.77 | $18.88 | — |

For comparison, the AI/API-only cost of a 2-bed package is about **US$6.30 (£4.76)** before any human QA [EST] ([pricing inputs, Gemini](https://ai.google.dev/gemini-api/docs/pricing)). Human labour roughly triples it.

### Failure-rate sensitivity (Base case)

Cost per success = fixed cost + repeatable cost ÷ (1 − f). Rejected attempts re-incur generation and QA. USD figures are the GBP figures ÷ 0.755 [EST].

| Deliverable | 5% | 15% | 30% | 50% | 50% in USD |
|---|---|---|---|---|---|
| Single room image | £5.27 | £5.39 | £5.63 | £6.18 | $8.19 |
| 5 room images | £10.21 | £10.86 | £12.18 | £15.18 | $20.11 |
| 2-bed flat | £15.09 | £16.22 | £18.50 | £23.69 | $31.38 |
| 4-bed house | £32.22 | £34.79 | £40.03 | £51.90 | $68.74 |
| Interactive 3D | £16.23 | £16.92 | £18.33 | £21.52 | $28.50 |
| 30 s walkthrough | £15.07 | £16.19 | £18.49 | £23.69 | $31.38 |
| 60 s cinematic | £49.16 | £54.16 | £64.32 | £87.36 | $115.71 |
| Developer package | £104.40 | £114.14 | £133.97 | £178.92 | $236.98 |
| 50-unit development | £790.33 | £870.61 | £1,034.02 | £1,404.41 | $1,860.15 |
| 200-unit development | £2,168.24 | £2,394.03 | £2,853.68 | £3,895.56 | $5,159.68 |

### Gross profit per customer

The formula used is:

> **GP per customer-month = Subscription price + overage revenue − [utilisation × included credits × cost per credit] − per-customer fixed COGS (hosting, SSO at US$125/connection/month, payment fees)**
>
> **Gross margin = GP ÷ revenue**

| Tier | Price | GP at 65% use (Base) | GP at 100% use (Base) | GP at 100% use (High) |
|---|---|---|---|---|
| Studio | £149 ($197) | £106.09 (71.2%) | £86.27 (57.9%) | £23.54 (15.8%) |
| Agency | £499 ($661) | £339.82 (68.1%) | £267.96 (53.7%) | **£4.49 (0.9%)** |
| Developer Pro | £1,499 ($1,985) | £1,209.69 (80.7%) | £1,086.77 (72.5%) | £493.17 (32.9%) |
| Enterprise | £5,000 ($6,623) | £3,750 (75.0%) | £3,235 (64.7%) | £860 (17.2%) |

The margins come from the model; the GP figures are price × GM [EST]. **Gross margin is not net profit.** In the Base case the model shows a **~70% 36-month gross margin**. That falls to **62–66% once support and customer-success salaries are included**. EBITDA is still **−£3,110 in month 24**, because engineering, sales, the founder's salary, ISO 27001 (£20k in year 1) and insurance (£4k/yr) sit below the gross line [EST/ASM] ([model](Property_Visualisation_Financial_Model.xlsx)). The model's ~70% is above ICONIQ's **~45–53%** average for AI products [VF/SECONDARY] ([SaaStr on ICONIQ](https://saastr.com/whats-truly-great-now-in-b2b-ai-per-iconiq-115-growth-at-100m-55-gross-margins-and-655k-in-revenue-per-employee)). It holds only if QA stays offshore and short.

---

## 7. Competitor analysis: every piece exists, and nobody ships the whole stack without humans

### Capability matrix

All prices are as published in October 2026 unless noted. Complaints come from review sites and are anecdotal.

| # | Competitor | Audience | Pricing | Plan upload | Automation vs human | Structural accuracy |
|---|---|---|---|---|---|---|
| 1 | [Getfloorplan](https://getfloorplan.com/pricing) | Agents, developers, 3D agencies | $25–$115 per set [VF] | JPG/PNG/PDF/DWG, one floor per file [VF] | AI + QA team; ~24h [VF] | Not disclosed |
| 2 | [Realitiq](https://www.realitiq.com/en/prices-for-projects/) | DACH developers | €400–600/unit + €2,000 setup [VF] | DWG/DXF/IFC [VF] | Not disclosed | CAD-based |
| 3 | [ProPlan Studio](https://www.proplanstudio.com/) | US builders | Configurator $499/mo; $1,000/model setup [VF] | Team builds the model [VF] | Human ("AI accelerates") | Human-modelled |
| 4 | [IdealTwin](https://www.idealtwin.com/pricing) | Developers | $2–4/unit/month [VF] | Not stated | Unreal plugin | Not disclosed |
| 5 | [realtySTUDIO](https://realty.studio/for/developers) | Gulf developers | $12,500–$59,500+ launch; from $499/mo [VF] | Not stated | 48h launch | Not disclosed |
| 6 | [Archilogic](https://www.archilogic.com/pricing) | Workplace/facilities | $329/plan conversion; $24.90–59/plan/month [VF] | JPG/PNG/PDF/DXF/DWG [VF] | "White-glove", human; 2 days [VF] | ±5% target [VF] |
| 7 | [RoomSketcher](https://www.roomsketcher.com/pricing/) | Agents, homeowners | $0–70/mo; AI Convert $20/floor [VF] | JPG/PNG/PDF; no CAD [VF] | AI walls only; manual for poor plans [VF] | Schematic |
| 8 | [Planner 5D](https://planner5d.com/pricing) | Consumers, B2B | $19.99–49.99/mo; Enterprise custom [VF] | JPG/PNG/PDF/DWG/DXF [VF] | Human review of every B2B result [VF] | Human-corrected |
| 9 | [Coohom](https://www.coohom.com/pricing) | Design/retail | Not published | CAD/PDF/images [VF] | Auto walls; manual fallback [VF] | Users report random walls [VF] |
| 10 | [Homestyler](https://www.homestyler.com/pricing) | Designers | $6.80–19.90/mo; coins [VF] | JPG/PNG/DWG/DXF/PDF (beta) [VF] | Auto (beta) + manual [VF] | Not disclosed |
| 11 | [Maket.ai](https://www.maket.ai/pricing) | Homeowners, pros | $20–100/mo [VF] | Upload 20 credits [VF] | "Human-validated" for 100% accuracy [VF] | Human-checked |
| 12 | [Collov AI](https://www.collov.ai/pricing) | Agents, stagers | $19–127/mo [VF] | JPEG/PNG/PDF [VF] | Generative | **Alters walls and windows** (reviews) [VF] |
| 13 | [Rendair](https://rendair.ai/tools/floorplan-to-render) | Architects | Not rendered | CAD/PDF/image claimed [VF] | Visual-based engine [VF] | Geometry changes (reviews) [VF] |
| 14 | [CubiCasa](https://www.cubi.casa/pricing/) | Agents, MLS | Plus 3D tier; prices hidden [VF] | **No**: app scan only [VF] | Auto + QA [VF] | 95–97% claimed [VF] |
| 15 | [Matterport (CoStar)](https://support.matterport.com/s/article/Matterport-Price-List) | Agents, AEC | $14–355/mo; Pro3 $3,995 [VF] | **No**: depth scan [VF] | Capture | Schematic CAD [VF] |
| 16 | [Giraffe360](https://www.giraffe360.com/build-your-plan/) | UK agents | From £159/mo, 12-month commitment [VF] | **No**: robotic camera [VF] | ML + processing ≤72h [VF] | LiDAR-measured |
| 17 | [Floorfy](https://floorfy.com/) | Iberian/Italian agents | €999 yr 1 or €74/mo [VF] | **No**: 360 photos [VF] | Automatic | Not disclosed |
| 18 | [BoxBrownie](https://www.boxbrownie.com/pricing) | Agents | Render $350; staging $30/image [VF] | Photos/sketches/PDF [VF] | Human service | Human |
| 19 | [Virtual Staging AI](https://www.virtualstagingai.app/prices) | Agents | $16–79/mo [VF] | Photos only [VF] | 10 s automatic [VF] | n/a |
| 20 | UK CGI studios, e.g. [Hyrez](https://hyrez.uk/services), [Shakworks](https://www.shakworks.com/architectural-visualisation-services) | Developers | £350–£1,500/still; animation from £3,500–£5,000 [VF] | Any | Fully human; 2–4 weeks [VF] ([Property CGI](https://www.propertycgiltd.com/cgi)) | High |
| 21 | Sales-suite agencies ([EyeSiteView](https://eyesiteview.co.uk/interactive-property-cgi/), [ShowReal360](https://www.showreal360.com/)) | UK developers | Per development, POA | From the studio's own CGI | Human + Unreal | High |

| # | Competitor | Interactive 3D | White label | API | Limitations / complaints | Our potential advantage |
|---|---|---|---|---|---|---|
| 1 | Getfloorplan | 360/VR [VF] | From the $61 Pro set [VF] | Yes [VF] | "Parts of the building had no roof"; missed 24h; limited customisation [VF] ([Trustpilot](https://www.trustpilot.com/review/getfloorplan.com)) | Self-serve editing; development-level portal; CAD/IFC exactness |
| 2 | Realitiq | Digital twin [VF] | Yes [VF] | Not stated | DACH-only focus | UK compliance presets; per-plan-type pricing |
| 3 | ProPlan | Configurator [VF] | Custom domain [VF] | Embed | Human modelling cost | Automated plan-to-model |
| 4 | IdealTwin | Yes [VF] | Enterprise [VF] | CRM | Unit pricing; not UK | Plan automation |
| 5 | realtySTUDIO | Yes | Yes | Enterprise [VF] | Gulf focus | UK first; geometry audit trail |
| 6 | Archilogic | Yes | — | REST/GraphQL [VF] | Not residential marketing | Possible supplier, not a rival |
| 7 | RoomSketcher | Live 3D/360 [VF] | Pro/Enterprise [VF] | Enterprise | Hard-to-edit walls; billing [VF] ([Capterra](https://www.capterra.com/p/164021/RoomSketcher/)) | Photoreal + development scale |
| 8 | Planner 5D | Yes | B2B [VF] | JS/REST [VF] | Renewal/refund complaints [VF] | Usable as a commodity backend by rivals; a risk to us |
| 9 | Coohom | Yes | Yes [VF] | OpenAPI [VF] | Save failures; walls [VF] | Geometry validation |
| 10 | Homestyler | Yes | Enterprise [VF] | Yes | Coin costs; crashes [VF] | Developer focus |
| 11 | Maket | No | — | Scale tier | Nonsensical layouts [VF] ([Trustpilot](https://www.trustpilot.com/review/maket.ai)) | Real plans, not generated layouts |
| 12 | Collov | "AI 3D tour" [VF] | API, no branding [VF] | Yes | Structural alteration [VF] | Measured, not hallucinated |
| 13 | Rendair | No | — | — | Geometry changes [VF] | Drift-gated enhancement |
| 14 | CubiCasa | 3D plan | "Fully white-label" SDK [VF] | Yes [VF] | Misread floor counts; inaccurate square footage [VF] ([Capterra](https://www.capterra.com/p/193054/CubiCasa/)) | Off-plan; CubiCasa needs a built property |
| 15 | Matterport | Tours | — | Enterprise [VF] | Expensive hosting; price rises [VF] | Off-plan |
| 16 | Giraffe360 | Tours | — | Plus tiers [VF] | Billing/cancellation [VF] | Off-plan; partner for resale |
| 17 | Floorfy | Tours | — | REST [VF] | No weekend processing [VF] | Off-plan |
| 18 | BoxBrownie | 360 staging | — | — | Missed instructions [VF] | Minutes, not days; £ vs $350 |
| 19 | Virtual Staging AI | No | Sublicensing [VF] | Yes [VF] | Refunds [VF] | Compliance labelling |
| 20 | CGI studios | Bespoke | Studio brand | — | Cost; 2–4 weeks | Speed and price; **or make them our channel** |
| 21 | Sales-suite agencies | Unreal configurators | Agency brand | — | Per-scheme bespoke builds | Self-serve; automated |

**Differentiation verdict: weak on features, plausible on positioning [EST].** Plan-to-3D, AI renders, white-label tours and configurators each exist as products. White-label APIs from Planner 5D, Coohom, Homestyler, Collov and CubiCasa mean that a "cheaper interface" over them is not defensible [VF] ([competitor notes, Collov API](https://collov.ai/API)). The defensible gap is a combination. It takes in **CAD/IFC/vector PDF**, produces **geometry-true assets with an audit trail**, works across **multiple plots in a development**, ships **UK compliance presets**, and runs at **self-serve speed**. Capture players (Matterport, Giraffe360, CubiCasa, Floorfy) structurally cannot serve off-plan. Getfloorplan is the most direct threat, and it is one product decision (a developer portal) away from closing the gap.

---

## 8. Market and segmentation: a £22m SAM where the best buyers number in the hundreds

| Seg | Who | Count | Current visualisation spend | WTP [HYP] | Sales cycle [EST] | Churn [EST] | TAM | SAM | SOM (Y3) |
|---|---|---|---|---|---|---|---|---|---|
| A | Independent agents | ~10,650 branches [EST] of 16,385 Rightmove branches [VF] | £1k–£6k/branch/yr [EST] | £50–£150/branch/mo | Days–4 wks | High | £32.0m | £4.79m | £0.24m |
| B | Multi-branch agencies | ~200–300 groups / ~5,735 branches [EST] | As A | £40–£100/branch/mo | 3–9 months | Low once embedded | £17.2m | £3.10m | £0.09m |
| C | Prime agents | ~300 [EST]; 126k £2m+ homes [VF] | £500–£2k/listing [EST] | £150–£500/listing | 1–3 months | Medium | £5.0m | £1.50m | £0.12m |
| D | Small developers | ~2,000 [EST] | £1k–£5k/project [VF] ([iCreate](https://icreate.co.uk/cgi-price-list/)) | £500–£2,500/project | 1–4 wks | High | £4.0m | £1.20m | £0.06m |
| E | Medium developers | ~500 [EST] | £7k–£20k/scheme + show homes £50k–£150k | £5k–£25k/scheme/yr | 1–3 months | Medium-low | £15.0m | £4.20m | £0.34m |
| F | Nationals | ~25 [EST] | House-type libraries | £50k–£250k/yr | 6–18 months | Low | £8.5m | £1.88m | £0.09m |
| G | Off-plan sellers | ~200 [EST] | £20k–£100k+/scheme [EST] | £10k–£40k/scheme | 1–4 months | Medium | £7.5m | £1.80m | £0.18m |
| H | Marketing/CGI agencies | ~200 [EST] | Tooling | £3k–£10k/yr or white-label | 1–2 months | Medium | £2.0m | £0.60m | £0.03m |
| I | Architects | 3,769 RIBA practices [VF] | £350–£4.5k/view | £30–£100/user/mo | Days–2 months | High (micro) | £7.9m | £1.36m | £0.04m |
| J | Interior designers | 6,415 businesses [VF] | $350–$800/render | £30–£80/mo | Days | High | £6.4m | £0.96m | £0.03m |
| K | BTR operators | ~120 [EST]; starts down 79% [VF] | Lease-up CGI | £5k–£20k/scheme | 3–9 months | Low-medium | £2.5m | £0.60m | £0.03m |
| | **Total** | | | | | | **≈£108m (±40%)** | **≈£22.0m** | **≈£1.25m ARR** |

Sources: [Rightmove FY2025](https://www.londonstockexchange.com/news-article/RMV/annual-financial-report/17479517); [RIBA Benchmarking 2025](https://www.riba.org/media/br1k2otq/riba-benchmarking-2025-executive-summary.pdf); [IBISWorld](https://www.ibisworld.com/united-kingdom/industry/interior-design-activities/14549/); [RE:UK BTR](https://realestateuk.org/our-work/reuk-build-to-rent-report-q2-2026/); [VisuArchitect](https://www.visuarchitect.com/questions/3d-architectural-visualization/how-much-does-3d-visualisation-cost/). Every ACV in the SAM is a hypothesis. TAM, SAM and SOM are bottom-up estimates [EST].

The arithmetic shows how small the visualisation line is inside a developer's budget. A 50-home, £17.5m GDV scheme budgets **2.5–3% of GDV** for sales and marketing, about £440k–£525k [VF for benchmark ([GLA EIR](https://www.london.gov.uk/who-we-are/governance-and-spending/sharing-our-information/freedom-information/foi-disclosure-log/eir-gla-benchmarks-development-viability-reviews)); EST for arithmetic]. Visualisation is only about **£7k–£20k** of that [EST]. Making CGI cheaper therefore saves developers little. The pitch has to target the large line items: the **£50k–£150k show home** [VF] ([Impact Aerial](https://www.impactaerial.co.uk/2026/03/10/virtual-tour-for-new-build-homes-the-developers-guide-to-immersive-marketing-in-2026/)) and slow absorption. Show-home substitution is an adjacent **£43m–£130m** pool [EST]. It is untested [HYP]; the test is to ask 10 developers whether a configurator plus a virtual show home would let them downgrade a physical show home.

**Top three segments:** **E medium developers** (highest SAM per customer outside enterprise), **G off-plan sellers** (the most urgent: a record 4,629 complete-but-unsold London homes in H1 2026 [VF] ([Evening Standard](https://www.standard.co.uk/news/london/london-new-build-home-sales-houses-property-b1292587.html))) and **C prime agents** (brand-driven, and useful as reference logos). **First target: E+G together**, reached through **H (CGI studios and marketing agencies) as the channel**. They share one buyer persona (Sales & Marketing Director) and one bundle. The contrarian risk is that G's budgets are contracting at exactly the moment its urgency peaks: London sales to UK individuals are **down 67% since 2022** [VF] ([Molior](https://www.moliorlondon.com/media/molior-report-media-2026/04/molior-residential-development-in-london-april-2026-final.pdf)).

**Expansion:** Dubai's **446 off-plan launches in 2025** [VF] ([Christie's Dubai](https://www.christiesrealestatedubai.com/the-journal/dubai-breaks-real-estate-records-in-2025/)) and an off-plan share of **62.6–73%** of transactions [VF] ([Zawya/DLD](https://www.zawya.com/en/press-release/research-studies/dubai-real-estate-market-hits-aed-682.5bln-with-214912-transactions-in-2025-371494)) make it the natural second market. ROSHN's 400,000-home mandate, with **78% of 2025 deals made via its app**, signals digital readiness in Saudi Arabia [VF] ([AGBI](https://www.agbi.com/analysis/construction/2026/01/giga-project-roshn-says-most-sales-made-via-app/)). The EU and US were not sized; that is a gap to close before any expansion decision.

---

## 9. Recommended pricing: keep the £149–£5,000 ladder, sell credits, and reprice Agency

### Hypothesis price points tested

The table shows gross margin at 100% of included usage, Base cost / High cost [EST] ([model](Property_Visualisation_Financial_Model.xlsx)).

| Price point | GM Base | GM High | Verdict |
|---|---|---|---|
| Studio £149 | 57.9% | 15.8% | Viable only with credits and ~65% utilisation |
| Agency £499 | 53.7% | **0.9%** | **Underpriced.** It needs £791 for 70% GM at Base |
| Developer Pro £1,499 | 72.5% | 32.9% | Healthiest tier |
| Enterprise £3,000 | 41.9% | **−37.2%** | Reject |
| Enterprise £5,000 | 64.7% | 17.2% | Floor price |
| Enterprise £10,000 | 81.8% | 58.1% | Target for full-service enterprise |

### Price needed for a target gross margin (100% usage)

| Tier | 60% Base | 70% | 80% | 85% | 60% High | 70% | 80% | 85% |
|---|---|---|---|---|---|---|---|---|
| Studio | £157 | £214 | £334 | £464 | £323 | £440 | £686 | £955 |
| Agency | £582 | £791 | £1,235 | £1,718 | £1,279 | £1,740 | £2,717 | £3,778 |
| Developer Pro | £1,016 | £1,368 | £2,092 | £2,844 | £2,543 | £3,424 | £5,235 | £7,118 |
| Enterprise | £4,399 | £5,922 | £9,055 | £12,312 | £10,496 | £14,128 | £21,604 | £29,375 |

### Recommended structure

| | Studio | Agency | Developer Pro | Enterprise |
|---|---|---|---|---|
| List / month | £149 | £499 (**test £699–£799** [HYP]) | £1,499 | £5,000+ |
| Included credits / month | 52 | 204 | 444 | 1,874 |
| Overage / credit | £4.00 | £3.50 | £3.00 | £2.50 |
| Setup fee | £0 | £500 | £1,500 | £7,500 |
| Per extra plan type | — | — | £350 | £350 |
| Hosted interactive properties / SSO | 1 / 0 | 5 / 0 | 15 / 0 | 50 / 1 |
| GM at 65% utilisation (Base) | 71.2% | 68.1% | 80.7% | 75.0% |

Source: [model `Pricing` sheet](Property_Visualisation_Financial_Model.xlsx). The Agency repricing range is our recommendation, derived from the 70%-GM price of £791.

**Business model choice: hybrid subscription + credits + setup + per-development fees [EST].** Cost scales with **plan types, not units**: a 50-unit, 6-type development costs £870.61 at Base. Per-unit pricing in the Realitiq style (€400–600/unit) would over-earn on large schemes and lose deals on small ones. Price per plan type, anchored at the top of the **£300–£600 per plot type** competitor band, and raise it to **£500–£600** if High costs materialise [EST] ([model](Property_Visualisation_Financial_Model.xlsx); [Realitiq](https://www.realitiq.com/en/prices-for-projects/)). Do not sell "unlimited": every geometry-true output requires a paid human confirm.

**Abuse prevention [EST]:**

- Meter credits per *plan interpretation*, not per image, so the human confirm is always paid for.
- Cap retakes per asset; the model assumes 3 attempts per accepted image at Base.
- Make WebGL the default viewer and sell pixel streaming as a metered add-on. At High cost, streaming is 6.65 h per hosted property-month at US$1.82–2.82/h [VF prices].
- Rate-limit hosted viewers per tier.
- Require card or Bacs before the first generation. Card-required trials convert at a **25–35% median vs 4–6%** without a card [SECONDARY] ([Userpilot/ChartMogul](https://userpilot.com/blog/free-trial-conversion-rate/)).
- Enforce rights warranties at upload.

**Are £25k–£100k+ enterprise deals realistic? Possible but unproven, and not before month 12 [EST].** Published anchors exist:

- realtySTUDIO sells **$12,500–$59,500+** launches [VF] ([realtySTUDIO](https://realty.studio/for/developers)).
- ProPlan cites **$15k–$50k** freelance configurator builds [VF vendor claim] ([ProPlan](https://www.proplanstudio.com/)).
- UK nationals' WTP of **£50k–£250k/yr** is a hypothesis [HYP] ([market notes](https://www.nhbc.co.uk/kontentdocuments/6d97b78c-0f03-40b7-b8ff-6acec08927de/small-house-builders-and-developers.pdf)).

A Developer Pro customer at £1,499 already pays about £18k/yr. Rightmove New Homes ARPA is **£2,135 per development per month** [VF] ([Rightmove FY2025](https://www.londonstockexchange.com/news-article/RMV/annual-financial-report/17479517)), which proves developers pay £25k+/yr per scheme for marketing *distribution*. To justify £25k–£100k+ a buyer would need three things:

- measured avoidance of show-home or CGI spend (£50k–£150k per show home);
- an options/upgrade uplift, with EyeSiteView's vendor-claimed **41.7%** uplift at Castle Green as the only evidence ([EyeSiteView](https://eyesiteview.co.uk/case-studies/home-buyer-engagement-off-plan/));
- ISO 27001, SSO and audit logs to pass procurement.

The test is three paid pilots measuring cost per reservation against a studio package [HYP].

---

## 10. Thirty-six-month financial model: a £1m-ARR base case that needs ~£186k to get there

The full model is in [`reports/Property_Visualisation_Financial_Model.xlsx`](Property_Visualisation_Financial_Model.xlsx), with sheets README, Assumptions, Unit_Costs, Pricing, Model_Bear/Base/Bull, Milestones and Summary. It has 36 monthly periods and live formulas, and recalculated with 0 errors. Customers are fractional expected values. MRR excludes overage, setup and per-development fees. Tax, VAT timing and R&D credits are ignored. All conversion, churn and launch inputs are [ASM]/[EST].

| Metric | Bear M12 | Bear M24 | Bear M36 | Base M12 | Base M24 | Base M36 | Bull M12 | Bull M24 | Bull M36 |
|---|---|---|---|---|---|---|---|---|---|
| Subscription MRR | £875 | £9,587 | £25,085 | £4,882 | £31,822 | £83,175 | £15,167 | £77,200 | £189,205 |
| ARR | £10,494 | £115,039 | £301,021 | £58,588 | £381,862 | £998,096 | £182,005 | £926,399 | £2,270,461 |
| Customers | 4.5 | 29.8 | 66.5 | 18.3 | 79.6 | 171.1 | 46.4 | 172.0 | 352.2 |
| Gross margin | −6.5% | 19.6% | 21.0% | 65.0% | 70.9% | 72.7% | 72.4% | 75.1% | 76.4% |
| GM incl. support/CS salaries | −6.5% | −10.2% | 9.3% | 65.0% | 62.3% | 65.7% | 56.5% | 68.0% | 71.9% |
| Monthly EBITDA | −£9,003 | −£12,224 | −£15,111 | −£6,691 | −£3,110 | £14,890 | −£219 | £15,589 | £88,562 |
| Cumulative cash | −£66,878 | −£195,050 | −£378,187 | −£61,611 | −£134,713 | −£73,161 | −£39,179 | −£14,269 | £567,649 |
| Headcount | 1 | 2 | 3 | 1 | 4 | 7 | 2 | 7 | 10 |

| Scenario metric | Bear | Base | Bull |
|---|---|---|---|
| First EBITDA ≥ 0 | Not in 36m | M22 | M15 |
| Sustained break-even | Not in 36m | **M34** | M22 |
| £50k founder cash runs out | M6 | M6 | M6 |
| External funding needed | £378,187 (still growing) | **£135,592** (low point M25) | £66,813 |
| 36-month cumulative revenue | £299,788 | £1,082,159 | £2,674,063 |
| 36-month gross margin | 14.5% | 70.0% | 74.8% |

### Milestones and the customer mix each requires

| Milestone | Bear | Base | Bull | Mix (Studio / Agency / Dev Pro / Enterprise = total) |
|---|---|---|---|---|
| £10k MRR | M25 | M16 | M11 | 14 / 4 / 2 / 1 = 21 |
| £25k MRR | M36 | M22 | M15 | 34 / 10 / 6 / 1 = 51 |
| £50k MRR | — | M29 | M20 | 68 / 21 / 11 / 3 = 103 |
| £100k MRR | — | — | M28 | 137 / 41 / 22 / 6 = 206 |
| £250k MRR | — | — | — | 342 / 103 / 55 / 14 = 514 |
| £1m ARR | — | — | M25 | 114 / 34 / 18 / 5 = 171 |
| £5m ARR | — | — | — | 569 / 172 / 92 / 23 = 857 |

The £5m ARR row is the decisive sanity check. It needs **about 23 enterprise and 92 Developer Pro accounts**, which is roughly every UK national housebuilder (~25) plus ~18% of medium developers. It is **not credible UK-only within 36 months** [EST] ([model](Property_Visualisation_Financial_Model.xlsx)). The base M36 ARR of ~£1.0m sits close to the independent bottom-up SOM of ~£1.25m [EST], so the two methods agree.

### Solo-founder capacity

The founder works ~180 h/month, with 35% (63 h) available for delivery. That covers roughly **125 two-bed packages, 61 four-bed houses, or 14 Agency / 11 Developer Pro / 2.8 Enterprise accounts** a month. In the Base case, delivery hours exceed founder capacity in **month 14 at ~26 customers**, when the first support/QA hire starts [EST] ([model](Property_Visualisation_Financial_Model.xlsx)). A solo founder also has to deliver **6–15 engineering-months** of build [EST] ([technical notes](https://arxiv.org/abs/2602.06507)). That makes the solo path slow at best.

---

## 11. Customer acquisition: resell through the studios you would otherwise disrupt

**A reseller-first strategy through CGI studios and property marketing agencies (segment H) is the recommended channel [EST].** There are four reasons:

1. Developers already buy from them; studios bundle CGI with interactive tools and lock clients in [VF] ([White Crow](https://www.whitecrowstudios.co.uk/services/interactive-experiences)).
2. White-label is what they need, since their brand faces the client.
3. Studios carry the revision expectations and approvals that the platform cannot afford to staff.
4. They face AI margin pressure, and some are already adopting AI themselves (White Crow says CROWSEYE is "powered by AI") [VF].

The counter-risk is that studios adopt AI internally instead of reselling. No survey evidence exists on this, so it is a [HYP] that needs primary interviews ([GTM notes](https://matterport.com/news/matterport-expands-its-value-added-reseller-var-program-emea-apac-and-latam)).

### Commission and margin modelling

No verified 2025–26 source confirms reseller margins. Matterport discloses only "special rates" and a "SaaS Recruiting Commission" in exchange for annual revenue commitments [VF] ([Matterport partners](https://www.matterport.com/en-gb/node/1443)). The inputs below are therefore **[ASM]**: a **20–30% wholesale discount** or a **10–20% recurring referral commission for 12 months**. GP figures are derived from the model's COGS [EST].

| Tier | Direct GP @65% (Base) | 20% discount GP / GM | 30% discount GP / GM | 15% referral GP / GM | 30% discount at **High** cost, 100% use |
|---|---|---|---|---|---|
| Studio £149 | £106.09 / 71.2% | £76.29 / 64.0% | £61.39 / 58.9% | £83.74 / 56.2% | **−£21.16 (−20.3%)** |
| Agency £499 | £339.82 / 68.1% | £240.02 / 60.1% | £190.12 / 54.4% | £264.97 / 53.1% | **−£145.21 (−41.6%)** |
| Developer Pro £1,499 | £1,209.69 / 80.7% | £909.89 / 75.9% | £759.99 / 72.4% | £984.84 / 65.7% | £43.47 (4.1%) |
| Enterprise £5,000 | £3,750 / 75.0% | £2,750 / 68.8% | £2,250 / 64.3% | £3,000 / 60.0% | **−£640 (−18.3%)** |

The implication is that **resellers should get Developer Pro economics and a platform-plus-usage price, not discounts on Studio or Agency seats.** At High cost, discounted lower tiers lose money on every customer.

**Channel conflict controls [EST]:**

- Deal registration, so direct sales never undercut a registered partner deal.
- The agency owns the client relationship on white-label workspaces.
- Volume-committed discount tiers, following the Matterport template.
- Direct sales limited to enterprise (F) and the Reapit agent channel.

### Direct motions

| Motion | Cost / benchmark | Label / source |
|---|---|---|
| Outbound to E/G directors | Cold email replies 1–5% (~3%); LinkedIn acceptance ~22% at VP+, then ~10% reply; **~8–12 meetings per 1,000 contacts** | VF benchmarks ([Belkins](https://belkins.io/resources/b2b-cold-outreach-benchmarks-2025-report); [GetFuzzy](https://getfuzzy.ai/blog/linkedin-outreach-statistics)); ASM conversion |
| Developer pipeline data | Barbour ABI ~£4k–£11k/yr; 10 free leads | VF ([Barbour ABI](https://barbour-abi.com/construction-leads/get-10-free-leads/)) |
| Agent marketplace (later, for A/B) | Reapit AppMarket: agents install free, partners set prices; network membership reportedly £1,500+/yr | VF / SECONDARY ([Reapit FAQ](https://reapit.atlassian.net/wiki/spaces/RW/pages/923598951/AppMarket+Frequently+Asked+Questions)) |
| Events | UKREiiF pavilion £39.5k ex VAT; generic 12 sqm stand ~£9.7k; year-1 budget £15k–£40k | VF ([Find a Tender](https://www.find-tender.service.gov.uk/Notice/064887-2025)); EST |
| CAC payback target | 6–12 months self-serve; 14–20 months developer sales-led (median B2B 15–16 months) | SECONDARY ([Aleph](https://www.getaleph.com/answers/cac-payback-period-saas-2026)); ASM |

---

## 12. White-label enterprise specification: residency and disclosure rules set the architecture

| Requirement | Specification | Basis |
|---|---|---|
| **Multi-tenancy and isolation** | Tenant → workspace → project hierarchy. Per-tenant encryption keys and storage prefixes. Separate GPU job queues with per-tenant quotas. No cross-tenant caching of prompts or assets | EST |
| **SSO / directory** | SAML/OIDC via WorkOS at **US$125/connection/month** (1–15), or Clerk at US$75 per extra connection. SCIM priced the same | VF ([WorkOS](https://workos.com/pricing); [Clerk](https://clerk.com/pricing)) |
| **Storage** | R2 at US$0.015/GB-month with free egress. A 4-bed package is ~3 GB, ≈US$0.045/month | VF price; EST size ([R2](https://developers.cloudflare.com/r2/pricing/)) |
| **Audit** | Immutable logs of inputs, model version, prompt, edits and **named approver per asset**. SIEM streaming at US$125/month per SIEM via WorkOS | VF price ([WorkOS](https://workos.com/pricing)); EST design |
| **Residency** | UK/EU by default. Claude **via Bedrock In-Region eu-west-2 or the EU geo profile**, or a Vertex EU endpoint. **Never the first-party `global` endpoint** for residency claims. Vertex global has "No data residency guarantees" | VF ([Claude data residency](https://platform.claude.com/docs/en/manage-claude/data-residency); [AWS Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html); [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/multi-region-endpoints-for-claude-available-on-vertex-ai)) |
| **Retention** | Configurable per tenant; deletion on termination. Anthropic ZDR is available via sales but **excludes the Batch API (29-day retention)**, Files API and others. Fable/Mythos models need 30-day retention | VF ([Claude data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)) |
| **Provider disclosure obligations** | Flow down the Anthropic AUP to customers. **Notify users that outputs may be inaccurate.** Any assistant or chat UI must disclose that it is AI. Naming Anthropic publicly needs its consent; naming it to end users is not required. Keep Google SynthID/C2PA marks intact. A 2026 Usage Policy update takes effect 12 Nov 2026 and has not been reviewed | VF ([Anthropic Commercial Terms](https://assets.ctfassets.net/5965pury2lcm/4e9p7xwZDo6mBgWfSyDsCV/907c229ef3ee22366fa66837419bde2c/Anthropic_T_Cs.pdf); [Usage Policy archive](https://archive.ph/sinqA)) |
| **GDPR** | The platform is processor (customer is controller): Art 28 DPA, sub-processor list, complaints procedure (DUAA, from 19 Jun 2026). For US sub-processors, use the UK Extension to the DPF, or IDTA/Addendum plus a TRA. EU→UK adequacy runs to 27 Dec 2031. Blur faces and documents in photos | VF ([ICO UK Extension](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/adequacy-regulations/how-does-the-uk-extension-to-the-eu-us-data-privacy-framework-work/); [EC adequacy](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_25_3059/IP_25_3059_EN.pdf); [GOV.UK DUAA](https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes)) |
| **IP / ownership** | Assign "whatever rights exist" in outputs, *as is*. Do not warrant that copyright exists: the UK proposes removing s9(3) computer-generated-work protection, and the USCO says purely AI material is unprotectable | VF ([GOV.UK report](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence/report-on-copyright-and-artificial-intelligence); [USCO](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)) |
| **Training limits** | Default: **no training on customer uploads**; using them would make the platform a controller for that purpose. Exclude Runway's standard terms. Training on FLUX outputs needs a separate licence | VF ([Runway](https://runway.com/terms-of-use); [BFL KB](https://help.bfl.ai/articles/9272590838-self-serve-dev-license-overview-pricing)) |
| **Architectural copyright** | Customer warrants its rights to convert and market the plans. Architect-credit fields. Planning-portal download warning. Takedown process | VF ([Blair v Osborne](https://swarb.co.uk/c/ca/1970blair-osborne.html); [Signature Realty](https://knyvet.bailii.org/ew/cases/EWHC/Ch/2016/3583.html); [RIBAJ](https://www.ribaj.com/intelligence/legal-copyright-in-architects-drawings-licenses-and-infringement/)) |
| **Liability** | Outputs are "illustrative". Liability cap (e.g. 12 months' fees). Customer indemnity for published content. **No IP indemnity beyond upstream cover**: OpenAI's is lost for modified output, and Google's covers only unmodified output. PI/E&O and cyber insurance (~£4k/yr [EST]) | VF ([OpenAI](https://openai.com/policies/service-terms/); [Google](https://cloud.google.com/terms/service-terms)); SOLICITOR |
| **Certification** | ISO 27001: £12k–£25k in year 1; auditor £4k–£8k | VF/SECONDARY ([Pyralink](https://pyralink.co.uk/insights/2026-05-26-iso-27001-cost-uk-certification/)) |

What UK housebuilders actually require in procurement (ISO 27001 vs SOC 2 vs Cyber Essentials Plus) is **unverified**. Five enterprise discovery calls would settle it [HYP].

---

## 13. Compliance and product safeguards: the approval gate is the product

No UK statute mandates an "AI" label. The test is whether an image misleads the average consumer, and **a disclaimer cannot cure a fundamentally misleading image** [VF] ([ASA](https://www.asa.org.uk/news/disclosure-of-ai-in-advertising-striking-the-balance-between-creativity-and-responsibility.html); [Taylor Wimpey ruling](https://www.asa.org.uk/rulings/Taylor-Wimpey-UK-Ltd-A12-190009.html)). A Winkworth branch took down AI-enhanced images after a buyer complained that a chimney breast had been removed [VF/SECONDARY] ([AOL/Observer](https://www.aol.co.uk/articles/rapid-rise-housefishing-ai-enhanced-090025000.html)).

| Regime | Rule | Product safeguard |
|---|---|---|
| **UK DMCCA 2024** ss225–227 | Misleading actions and omissions; strict-liability offences; CMA fines up to 10% of global turnover; in force 6 Apr 2025 [VF] ([CMA207](https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices)) | Geometry lock; flag structural, view or neighbour changes; customer bears publication responsibility in contract |
| **ASA/CAP** | Upgraded images need an adjacent, equally prominent "includes optional upgrades" line; advertiser liable for AI output [VF] ([CAP off-plan advice](https://www.asa.org.uk/advice-online/property-new-build-and-off-plan-homes.html); [ASA Jun 2026](https://www.asa.org.uk/news/ai-and-deepfakes-four-things-advertisers-need-to-know-before-they-hit-run.html)) | **Specification-tier toggle**: "from"-price images show standard spec; upgrade label auto-inserted |
| **Rightmove** | "Enhanced Edits" (AI/CGI) must be labelled and accompanied by current accurate images; no text in images; no identifiable people [VF] ([Rightmove guidelines](https://media.rightmove.co.uk/pdf/rightmove_technical_guidelines.pdf)) | Rightmove preset; "pair packs"; confirm with Rightmove whether an in-image label counts as text |
| **Zoopla** | Member must make AI-produced content clear [SECONDARY, verify] ([AI Flip Room](https://aifliproom.com/blog/virtual-staging-rules-united-kingdom)) | Zoopla preset; labels carried in metadata |
| **NHQB Code** (Mar 2026) | CGI and video not misleading; GIA per RICS; altered material restricted [VF] ([NHQB](https://www.nhqb.org.uk/the-code/part-1-selling-a-new-home/)) | GIA computed from the model; version link to approved drawings |
| **EU AI Act Art 50** | Providers must machine-mark outputs (from 2 Aug 2026; 2 Dec 2026 for systems already on the market); deployers must visibly label deepfakes; fines up to €15M / 3% [VF] ([EC](https://commission.europa.eu/news-and-media/news/safer-and-more-transparent-ai-2026-08-02_en); [McCann FitzGerald](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/ai-transparency-european-commissions-guidelines-on-article-50-part-2-deployer-obligations)) | C2PA + watermark on every output; EU icon preset; consider signing the Code of Practice |
| **California AB 723** (BPC §10140.8) | Licensees must disclose altered images and link or QR to the original; CRMLS bans AI landscaping [VF] ([CA BPC](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10140.8.); [CRMLS FAQ](https://go.crmls.org/wp-content/uploads/2026/02/2026%5FDigitally%5FAltered%5FImages%5FFAQs%5Fv1.pdf)) | Hosted original-image page + QR; MLS export fields; landscaping block in the CA preset |
| **Dubai Trakheesi** | Every ad needs a permit number/QR (AED 1,000); off-plan must be RERA-registered with escrow [VF] ([DLD](https://dubailand.gov.ae/en/eservices/real-estate-ad-permit/); [Brokerage Guide](https://dubailand.gov.ae/media/i31iv1n0/real_estate_brokerage_practice_guide_2024.pdf)) | Mandatory permit/QR slot; block Dubai export without a permit number |
| **Saudi REGA / Wafi** | Ad licence tied to a brokerage contract; Wafi off-plan licence requires approved architectural designs [VF] ([REGA](https://rega.gov.sa/en/rega-services/eservices/real-estate-advertisement-license-issuance/); [Wafi](https://rega.gov.sa/en/rega-services/platforms/wafi-off-plan-sales-and-lease/?currentPage=42&tabActive=Wafi+Projects)) | Generate only from Wafi-approved plans; version-link to them |
| **Planning** (LI TGN 06/19, LVMF) | Type 4 verified views need survey-grade methods [VF] ([LI TGN 06/19](https://www.landscapeinstitute.org/wp-content/uploads/2019/09/LI_TGN-06-19_Visual_Representation-1.pdf)) | Mark outputs "Not a verified view"; no planning export presets |

**Mandatory gates (none optional):**

1. **Rights gate** at upload.
2. **Interpretation gate:** human 2D confirm.
3. **Spec-tier and label gate:** jurisdiction preset chosen.
4. **Named approver sign-off** per asset, logged.
5. **Export gate:** permit/QR fields present where required; originals paired.

None of these has been validated with a regulator, portal or insurer [EST; SOLICITOR].

---

## 14. Premium experience and the buyer configurator: indispensable only if it touches revenue

A configurator becomes indispensable when it changes the developer's P&L, not when it looks good. The evidence points to three levers:

- **Options and extras revenue.** EyeSiteView reports a **41.7% uplift** in options and extras at Castle Green Homes after configurators, from 700+ buyers [VF vendor claim] ([EyeSiteView](https://eyesiteview.co.uk/case-studies/home-buyer-engagement-off-plan/)).
- **Show-home avoidance.** A show home costs **£50k–£150k+** [VF] ([Impact Aerial](https://www.impactaerial.co.uk/2026/03/10/virtual-tour-for-new-build-homes-the-developers-guide-to-immersive-marketing-in-2026/)).
- **Digital-first transactions.** ROSHN made **78% of its deals in-app** [VF] ([AGBI](https://www.agbi.com/analysis/construction/2026/01/giga-project-roshn-says-most-sales-made-via-app/)).

UK configurators today are mostly agency-built per development (Marmoset, EyeSiteView, ShowReal360) [VF] ([Marmoset](https://marmoset.digital/what-we-do); [ShowReal360](https://www.showreal360.com/)). Overseas SaaS anchors run from **$499/mo** (ProPlan) to **$2–4/unit/month** (IdealTwin) [VF].

Four features would make it indispensable [EST/HYP]:

1. **Live availability** synced to CRM, as Marmoset and IMMERSIV do.
2. **Spec-tier-correct pricing**, so every finish swap shows its cost. That doubles as ASA/NHQB compliance.
3. **Measured data in-viewer**: room dimensions and GIA from the model, never from pixels.
4. **Reservation-intent analytics** that tie viewer sessions to leads.

Premium photoreal real-time (Unreal pixel streaming) should stay a paid add-on. It costs about **US$24–38/month per property** at 100 sessions [EST], and Unreal's royalty terms are unresolved [SOLICITOR]. Whether the configurator is a must-have or a nice-to-have is the single largest commercial [HYP]. Test it by asking 10 developers whether it would let them skip or downgrade a physical show home, and with paid pilots measuring cost per reservation.

---

## 15. Defensibility and long-term strategy: a £10m ARR outcome requires leaving the UK

**Moats available [EST]:**

1. A proprietary gold set of UK, Gulf and EU plans with confirmed vectors. HITL corrections become training data, with customer consent.
2. A validated drift-gated rendering pipeline that can claim "measured, not hallucinated".
3. Compliance presets and audit trails that procurement teams come to depend on.
4. Channel lock-in through studios' white-label workspaces.
5. Development-level data integrations (CRM, live availability).

None of these exists today, and each can be copied within 12–24 months by a funded rival such as Getfloorplan, Realitiq or Giraffe360 (whose Series B was ~$10m [VF] ([Cipio](https://www.cipiopartners.com/news/2026-03-26-cipio-partners-invests-in-giraffe360-as-lead-investor-in-usd-10-million-series-b-round))).

**£10m+ ARR potential: low in the UK alone.** £5m ARR already needs ~857 customers, including ~23 enterprise accounts [EST] ([model](Property_Visualisation_Financial_Model.xlsx)). Reaching £10m needs Dubai, Saudi Arabia, and the EU or US, plus an agent volume play (A/B) through Reapit. The UK is a beachhead, not the prize.

**Likely acquirers:** portals and their owners, which are vertically integrating 3D:

- CoStar bought Matterport for ~$1.6bn, closed 28 Feb 2025, at ~9–10x trailing revenue [VF deal; EST multiple] ([CoStar 8-K](https://www.sec.gov/Archives/edgar/data/1057352/000119312525042465/d899523d8k.htm); [Construction Dive](https://www.constructiondive.com/news/costar-deal-matterport-ai-reality-capture/714360/)).
- REA bought 61.5% of iGUIDE and invested in IMMERSIV [VF] ([BusinessWire](https://www.businesswire.com/news/home/20251002905299/en/REA-Group-to-Acquire-Leading-3D-Tour-and-Interactive-Floor-Plan-Technology-iGUIDE); [BNA](https://www.businessnewsaustralia.com/articles/rea-group-lifts-stake-in-3d-architectural-visualisation-tool-startup-immersiv.html)).

Rightmove, Zoopla/Houseful, Reapit, Giraffe360, Esoft and Chaos are plausible strategic buyers [EST]. Private SaaS medians are **~3–5x ARR**, and 7–9x for Rule-of-40 > 50 with NRR > 120% [SECONDARY] ([Livmo](https://livmo.com/blog/saas-valuation-multiples-2026/)). A base-case ~£1m ARR business would be worth roughly £3–5m [EST]. That is a solid founder outcome, not a venture return.

---

## 16. MVP roadmap: phases 0–5 with gates that can stop the build

Effort figures are allocations within the technical notes' totals (A 2–4, B 6–12, C 9–15 engineering-months) [EST]. Infrastructure prices are [VF] where cited.

| Phase | Deliverables | Dependencies | Effort [EST] | Key risks | Infra cost | Acceptance criteria | Validation gate |
|---|---|---|---|---|---|---|---|
| **0. Validation (30 days)** | §20 programme: 20 discovery calls, 50-plan time trial, pricing test, 3 pilot LOIs | Plan access with rights | ~1 founder-month | False positives from friendly interviews | Barbour ABI free leads; Claude/Gemini API pennies | Kill criteria in §20 not triggered | **Go/no-go** |
| **1. Vector-first PoC** | Vector PDF/DXF/IFC → canonical JSON → 2D confirm editor → Blender stills | ezdxf, web-ifc, Blender | 2–3 eng-months | Layer-semantics variety | GPU at ~US$0.89/h ([RunPod](https://www.runpod.io/pricing)) | §5 thresholds on P1/P5 | Studio partner accepts output with ≤1 revision round [ASM] |
| **2. Raster + HITL** | Segmentation + OCR + least-squares scale; scan handling; storey registration | Licensed training data (CubiCasa5K likely non-commercial) | 3–5 eng-months | Licensing; UK drafting conventions | Data licence (unknown) | P2–P4 thresholds; HITL ≤ 15 min on scans | Median HITL ≤ 10 min across 50 plans |
| **3. Photoreal + video + WebGL viewer** | PBR library, schedule parser, drift-gated enhancement, 30 s/60 s video, embeddable branded viewer | Phases 1–2 | 3–4 eng-months | Drift above threshold; Veo pricing changes | Images US$0.113–0.24 each; Veo US$0.12–0.40/s | Drift ≤ 1% width; rejection ≤ 15% | 3 paid pilots delivered at ≤ Base unit cost |
| **4. White-label + compliance** | Multi-tenancy, reseller workspaces, SSO, audit, jurisdiction presets, C2PA, approval gate | Phase 3 | 2–3 eng-months | Procurement demands (ISO 27001) | WorkOS US$125/connection; ISO 27001 £20k yr 1; insurance £4k/yr ([model](Property_Visualisation_Financial_Model.xlsx)) | Pass one developer security questionnaire | First reseller signs a volume commitment |
| **5. Configurator + expansion** | Live availability, spec-tier pricing, analytics; Dubai preset (Trakheesi), Arabic/RTL | Phase 4; CRM integrations | 3–5 eng-months | Unreal royalty; Gulf demand amid regional conflict | Pixel streaming US$1.82–2.82/h (add-on) | Options-uplift or show-home-avoidance evidence | £25k MRR reached (Base M22) before hiring for expansion |

The total of **~14–21 engineering-months** [EST] exceeds the 6–15 range for a single class and confirms that a solo founder cannot ship everything. **Phases 1 and 3 on vector inputs only are the minimum sellable product.**

---

## 17. Legal and commercial risks

| Risk | Likelihood / impact [EST] | Mitigation | Source |
|---|---|---|---|
| Misleading-image claims (DMCCA, ASA, NHQB) flowing to the platform via its customers | Medium / High | Geometry lock, approval gate, contract allocation, PI cover | [CMA207](https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices) |
| Copyright in uploaded plans | Medium / Medium | Warranties, credits, takedown | [Signature Realty](https://knyvet.bailii.org/ew/cases/EWHC/Ch/2016/3583.html) |
| No copyright in outputs (s9(3) repeal) | Medium / Low-Medium | Assign "as is"; add human authorship steps | [GOV.UK](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence/report-on-copyright-and-artificial-intelligence) |
| Upstream vendor churn or price rises (Sora shut down; Gemini text prices double) | High / Medium | Multi-vendor abstraction | [OpenAI](https://developers.openai.com/api/docs/models/sora-2); [Gemini](https://ai.google.dev/gemini-api/docs/pricing) |
| Licence traps (FLUX [dev], Stability > US$1M, Runway training, LibreDWG GPL, CubiCasa5K NC) | Medium / High | Model allowlist; legal review | [BFL](https://bfl.ai/legal/non-commercial-license-terms); [Stability](https://stability.ai/license) |
| Unreal 5% royalty on a pixel-streamed SaaS | Medium / Medium | WebGL default; Epic EULA review | [Epic](https://www.unrealengine.com/blog/we-are-updating-unreal-engine-twinmotion-and-realitycapture-pricing-in-late-april) |
| EU Art 50 non-compliance | High if EU-exposed / High (€15M / 3%) | C2PA + labels before EU launch | [EC](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations) |
| Data residency mis-selling (first-party Claude is global/us only) | Medium / High | Bedrock/Vertex EU routing | [Claude docs](https://platform.claude.com/docs/en/manage-claude/data-residency) |
| Indemnity gap (upstream indemnities void for modified output) | Medium / Medium | Do not promise IP indemnity | [OpenAI Service Terms](https://openai.com/policies/service-terms/) |
| Gulf demand shock from 2026 regional conflict | Unknown / Medium | Stage the expansion | [Bank of England](https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate) |
| Customer concentration in a small, stressed segment (E/G) | High / High | Channel diversification | [Knight Frank](https://www.knightfrank.co.uk/research/article/2026/10/the-gulf-between-ambition-and-delivery-in-the-london-new-homes-market) |

---

## 18. Top 10 reasons this could fail

1. **QA minutes blow out.** At 15 minutes per plan and US$35/h, every tier drops to a **1–33% gross margin** and the Bear case never recovers [EST] ([model](Property_Visualisation_Financial_Model.xlsx)).
2. **Customers expect studio-style revisions,** turning the business into a 40–55%-margin service [EST] ([ICONIQ via SaaStr](https://saastr.com/whats-truly-great-now-in-b2b-ai-per-iconiq-115-growth-at-100m-55-gross-margins-and-655k-in-revenue-per-employee)).
3. **Getfloorplan adds a developer portal** at its $25–$115 per-set price point [VF price] ([Getfloorplan](https://getfloorplan.com/pricing)).
4. **The core segments are tiny and stressed:** ~700 E+G organisations [EST], London sales at a post-2009 low [VF].
5. **Visualisation is a small budget line** (£7k–£20k of £440k–£525k per scheme) [EST], so cost savings do not move buyers.
6. **Studios adopt AI themselves** rather than resell, closing the channel [HYP].
7. **Raster accuracy disappoints on UK drafting conventions** (scan wall recall 0.723) [VF] ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0926580526004346)).
8. **A regulatory or portal crackdown** on AI imagery hits customers' willingness to publish any AI output [EST] ([AOL/Observer](https://www.aol.co.uk/articles/rapid-rise-housefishing-ai-enhanced-090025000.html)).
9. **Enterprise procurement** (ISO 27001, SSO, 6–18-month cycles) outlasts the runway. Cash goes negative in month 6 in every scenario [EST].
10. **Solo-founder capacity runs out at ~26 customers (M14)** while 6–15 engineering-months of build remain [EST].

## 19. Top 10 competitive advantages we could build

1. A **CAD/IFC-first** pipeline with exact geometry, which capture players cannot match for off-plan [VF] ([CubiCasa](https://www.cubi.casa/pricing/); [Matterport](https://support.matterport.com/s/article/Matterport-CAD-File)).
2. A **measured-drift guarantee** on AI enhancement, the opposite of Collov or Rendair complaints [VF complaints] ([Trustpilot](https://uk.trustpilot.com/review/collov.ai)).
3. **Jurisdiction compliance presets** (Rightmove, Zoopla, NHQB, Art 50, AB 723, Trakheesi) built into export [EST].
4. A **named-approver audit trail** that procurement and insurers value [EST].
5. **Per-plan-type pricing** that undercuts studio packages (£3k–£8k launch packs) [VF] ([Blockout](https://www.blockoutdigital.com/guides/how-much-does-architectural-cgi-cost)).
6. **White-label workspaces for studios and agencies**, which turns disruptees into a channel [EST].
7. A **development-level data model** (plots, types, availability), unlike the unit-centric RoomSketcher and Planner 5D [EST].
8. A **proprietary corrected-plan dataset** from HITL edits, with consent [EST].
9. **UK/EU residency by design** via Bedrock eu-west-2 [VF] ([AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html)).
10. **Gulf readiness** (RTL, permit/QR slots, Wafi plan linkage) for the 446 launches a year in Dubai [VF] ([Christie's](https://www.christiesrealestatedubai.com/the-journal/dubai-breaks-real-estate-records-in-2025/)).

---

## 20. Thirty-day validation programme with kill criteria

| Days | Activity | Output | Kill criterion [ASM] |
|---|---|---|---|
| 1–2 | Build lists: 10 free Barbour ABI leads, the Rightmove New Homes developer list, 30 UK CGI studios and marketing agencies | 150 E/G targets; 30 H targets | — |
| 3–4 | Assemble the 50-plan gold set (10 per type in §5) with permission; write ground truth for 20 of them | Licensed test set | Cannot obtain 30 licensed plans → the rights model is broken |
| 5–7 | Outreach: email plus LinkedIn to 300 E/G and 30 H contacts (benchmark ~8–12 meetings per 1,000 [ASM] ([Belkins](https://belkins.io/resources/b2b-cold-outreach-benchmarks-2025-report))) | Meetings booked | — |
| 8–12 | **Technical spike**: vector PDF/IFC → JSON → Blender still for P1/P5; Claude Sonnet/Opus dimension-OCR vs PaddleOCR on 50 plans | Metrics vs §5 thresholds | Wall IoU < 0.90 on clean vector input |
| 8–19 | 20 discovery calls (E/G/H). Ask about current CGI spend, show-home spend, the "would a configurator let you downgrade a show home?" question, and procurement requirements | Interview log | **< 5 of 20 report ≥ £1,000/month of relevant spend they would redirect** |
| 13–17 | **HITL time trial**: 5 operators × 50 plans in the 2D editor (clickable prototype) | Median minutes per plan by type | **Median > 10 min clean or > 20 min scan** |
| 15–21 | Van Westendorp survey plus a price-tier landing page (£149/£499/£799/£1,499) | Acceptable price range | Developer acceptable range below £500/month |
| 18–24 | Studio/agency reseller conversations: test 20–30% wholesale vs a referral model, and probe channel conflict | Reseller term sheet interest | **0 of 30 studios willing to pilot white-label** |
| 22–28 | Concierge-deliver 3 developer packs (founder plus offshore QA), billed | Unit cost, revisions, NPS | **Cost per 2-bed > £30.85, or > 2 revision rounds average** |
| 26–29 | Compliance check: email Rightmove about in-image labels; one solicitor review of terms; one PI broker quote | Written answers | Insurer refuses AI-content PI cover |
| 30 | Decision memo: update the model's `Assumptions` with measured QA minutes, rejection rate and WTP | Go / pivot / kill | **Kill if ≥ 2 kill criteria trigger; pivot to a studio-tooling product if only demand fails** |

The thresholds are design choices [ASM]. They are tied to the model's Base/High boundaries and to the §5 PoC thresholds. **The programme has not been run.**

---

## 21. Final investment recommendation: fund the experiment, not the company

**Do not commit the ~£185.6k the Base case requires** [EST] ([model](Property_Visualisation_Financial_Model.xlsx)) until the 30-day programme produces three measured facts:

1. Median HITL time of **≤10 minutes per clean plan**.
2. At least **5 of 20 developers or agencies** confirming ≥£1,000/month of redirectable spend.
3. At least **one CGI studio** willing to pilot a white-label reseller arrangement.

If all three hold, build Phases 1 and 3 on **vector and IFC inputs only**. Sell **Developer Pro (£1,499) and per-plan-type development fees** through studios. Reprice Agency to ~£700–£800 [HYP], and postpone raster-scan support, agents (A/B) and pixel streaming. If demand fails but the pipeline works, pivot to selling the geometry-validation pipeline *to* studios as tooling. If the HITL minutes fail, kill the project: the business would be a service at 40–55% margins competing with BoxBrownie and offshore studios.

---

## FINAL VERDICT

| # | Question | Direct answer |
|---|---|---|
| 1 | **Buildable today?** | **Yes, in a constrained form.** Conceptual images 9/10. Faithful renders 7.5/10 with HITL. Accurate navigable 3D 8/10 from IFC/DWG, 6/10 from raster with HITL, **3/10 fully automatic** [EST] ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0926580526004346); [Blueprint-Bench](https://andonlabs.com/evals/blueprint-bench)) |
| 2 | **Works without manual 3D artists?** | **Yes for artists, no for humans.** Procedural geometry and Blender replace modelling, but a 3–15 minute human 2D confirm per raster plan remains mandatory, and every competitor shipping this has one [VF] ([Planner 5D](https://tool.planner5d.com/b2b-floor-plan-recognition); [Getfloorplan](https://getfloorplan.com/for-personal-users)) |
| 3 | **Genuinely difficult part?** | Turning raster or scanned plans into **topologically correct, correctly scaled, multi-storey vectors**, plus **proving** that AI enhancement did not move a wall. Rendering and LLM spend are solved problems [EST] |
| 4 | **True cost of one successful property?** | **2-bed flat: £16.22 ($21.48) Base**, £5.00–£30.85 Low–High, **£23.69 at a 50% failure rate. 4-bed house: £34.79 ($46.08) Base.** About 58–61% of it is human labour, and AI alone is ~£4.76 [EST] ([model](Property_Visualisation_Financial_Model.xlsx)) |
| 5 | **Realistic price?** | Studio **£149**, Agency **£699–£799** (not £499), Developer Pro **£1,499**, Enterprise **≥£5,000/month**, plus **£350–£600 per extra plan type** and setup fees. One-off packs: **£59–£92** for a 2-bed and **£411–£642** per house type at 70–80% GM [EST/HYP] |
| 6 | **Who pays £1,000+/month?** | **Medium developers (E) and off-plan sellers (G)** with live schemes. WTP of £5k–£40k per scheme per year is [HYP]; the anchor is Rightmove New Homes at **£2,135 per development per month** [VF]. National housebuilders (F) at £50k–£250k/yr [HYP] after month 12. Not independent agents (£50–£150/branch [HYP]) |
| 7 | **Is white-label attractive?** | **Yes as a channel, weak as a moat.** Studios and agencies need it, but five incumbents already offer white-label APIs [VF] ([Coohom](https://open.coohom.com/pub/saas/open-platform/design-building); [CubiCasa](https://www.cubi.casa/developers/)). Wholesale discounts on Studio/Agency tiers go negative at High cost [EST] |
| 8 | **Realistic monthly profit at 12/24/36 months?** | Monthly **EBITDA**, not net profit. **Base: −£6,691 / −£3,110 / +£14,890.** Bear: −£9,003 / −£12,224 / −£15,111. Bull: −£219 / +£15,589 / +£88,562 [EST] ([model](Property_Visualisation_Financial_Model.xlsx)) |
| 9 | **Sufficiently differentiated?** | **Not yet.** Differentiation exists only in the *combination*: CAD/IFC-in, geometry-true, development-level, compliance-ready, white-label for studios. It is unproven and copyable within 12–24 months [EST] |
| 10 | **Would you invest your own money?** | **Only in the 30-day validation, not in the £185.6k build.** I would invest in the build only once measured HITL minutes are ≤10 per clean plan and developer WTP is confirmed by paid pilots [EST] |

### Opportunity score: 49 / 100

| Dimension | Weight | Score /10 | Weighted | Rationale |
|---|---|---|---|---|
| Technical feasibility | 15 | 6.5 | 9.75 | Vector/IFC path solid; raster needs HITL; drift unmeasured |
| Demand | 20 | 5.5 | 11.00 | Real pain (unsold stock, show-home costs) but small, stressed segments |
| Pricing power | 15 | 5.0 | 7.50 | Studio anchors are high (£350–£1,500 per still), but Getfloorplan anchors at $25–$115 |
| Competition | 10 | 4.0 | 4.00 | 20+ adjacent players; Getfloorplan and Realitiq are close |
| Distribution | 15 | 4.0 | 6.00 | Studio channel plausible but unverified; enterprise cycles of 6–18 months |
| Retention | 10 | 5.5 | 5.50 | Developers churn by scheme; enterprise sticky; SMB churn 2.5–3.5%/month |
| Defensibility | 15 | 3.5 | 5.25 | No moat today; data and compliance moats must be earned |
| **Total** | **100** | | **49.0** | |

The weights and scores are analyst judgement [EST]. The score supports a **conditional "validate, then wedge"** decision rather than a build-now decision. It would rise most from evidence on two dimensions: distribution (a signed studio reseller) and pricing power (paid developer pilots at ≥£1,499/month).
