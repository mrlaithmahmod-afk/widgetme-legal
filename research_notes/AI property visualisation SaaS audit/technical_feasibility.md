# Technical Feasibility & Technology Stack: Architectural Inputs to Accurate 3D, Renders, Walkthroughs and Video (as of 20 Oct 2026)

Labels used throughout:
- **[VERIFIED]**: stated in the cited primary or official source, checked this session.
- **[SECONDARY]**: stated by a third-party or aggregator source; treat with caution.
- **[ESTIMATE]**: analyst judgement drawn from the cited evidence.
- **[HYPOTHESIS]**: plausible but untested; the test that would settle it is given.
- **[PRE-2025]**: the source is older than 2025 and may have been superseded.

Method note: this used about 17 search and fetch calls, and Firecrawl rate limits cut the search short. Several vendor pricing pages and paper PDFs were not opened in full, and those items are listed under Gaps rather than guessed. Some licence facts come from background knowledge and were not re-checked this session. They are flagged "unverified this session" and sit only under Inferences or Gaps.

---

## 1. State of the art in raster/PDF floor-plan recognition and vectorisation

### Takeaway
On clean, CAD-exported raster plans, wall and opening recognition is mature: detection IoU is in the 0.95 range, and a 2026 VLM vectoriser reports 92.5% external-wall IoU. Accuracy drops sharply on scanned plans, falling to about 0.72 wall recall. No published system turns arbitrary plans into survey-grade vectors without review. Every commercial product found that publishes its workflow uses a human QA or correction step, or a capture step it controls itself.

### Cited Findings
- **CubiCasa5K** has 5,000 floor-plan images annotated as polygons in more than 80 object categories. Its baseline is a multi-task CNN. **[VERIFIED][PRE-2025: 2019]** — [arXiv 1904.01920](https://arxiv.org/abs/1904.01920)
- The CubiCasa5K GitHub README states no metrics and does not name its licence in the page text. It links to a LICENSE file, and the dataset is hosted on Zenodo. **[VERIFIED]** — [GitHub CubiCasa/CubiCasa5k](https://github.com/CubiCasa/CubiCasa5k)
- **Raster-to-Vector (Liu et al., ICCV 2017)** detects junctions (wall corners, door end-points) and assembles them into primitives with integer programming. It reports "around 90% precision and recall". **[VERIFIED][PRE-2025]** — [ICCV 2017 open access](https://openaccess.thecvf.com/content_iccv_2017/html/Liu_Raster-To-Vector_Revisiting_Floorplan_ICCV_2017_paper.html)
- A survey reports one GAN or hybrid method at 92% overall accuracy and 84% mean IoU on the R2V dataset (pixel-level walls). **[SECONDARY]** — [ACM DL survey](https://dl.acm.org/doi/10.1145/3747227.3747250)
- One paper reports an average segmentation IoU of 72.7% on CubiCasa5k against a prior benchmark of 57.5%. **[SECONDARY; venue quality uncertain]** — [TURCOMAT paper](https://www.turcomat.org/index.php/turkbilmat/article/download/3620/3113/6799)
- **MitUNet (Dec 2025)** combines a Mix-Transformer encoder, a U-Net decoder and Tversky loss for thin-wall segmentation. Its authors claim it beats standard models on CubiCasa5k and a regional dataset, and that the code and dataset are public. Exact numbers were not extracted this session. **[VERIFIED abstract]** — [arXiv 2512.02413](https://arxiv.org/abs/2512.02413)
- **FloorplanVLM (Beike/KE Holdings, Feb 2026)** treats vectorisation as image-to-JSON sequence generation. It is trained with SFT followed by GRPO on Floorplan-2M and Floorplan-HQ-300K, and handles slanted walls and curved arcs. On its own open-sourced FPBench-2K it reports **92.52% external-wall IoU**, plus a 96.1% output-validity rate (the validity figure comes from the alphaXiv summary). **[VERIFIED abstract]** — [arXiv 2602.06507](https://arxiv.org/abs/2602.06507); [alphaXiv summary](https://www.alphaxiv.org/abs/2602.06507)
- **Robustness to scans (Automation in Construction, 2026)** pairs CAD-derived and scanned versions of the same CubiCasa5k layouts:
  - CAD-derived: WALL recall@0.5 = 0.974, mean IoU 0.953; WINDOW recall 0.997, mean IoU 0.978.
  - Scanned: WALL recall 0.723, mean IoU 0.825 (IoU ≥ 0.85 for only 0.504); WINDOW recall 0.884.
  **[VERIFIED from search excerpt]** — [ScienceDirect S0926580526004346](https://www.sciencedirect.com/science/article/pii/S0926580526004346)
- **RoomFormer (CVPR 2023, MIT licence)** is a two-level-query Transformer that reconstructs floor plans from 3D scan density maps. It was SOTA on Structured3D and SceneCAD at the time and can be extended to room types, doors and windows. Its input is point-cloud density maps, not raster drawings. **[VERIFIED][PRE-2025]** — [GitHub ywyue/RoomFormer](https://github.com/ywyue/RoomFormer)
- **Commercial: Planner 5D B2B Floor Plan Recognition.** AI does the recognition, then "a human Planner 5D interior designer reviews every result and makes manual corrections where necessary". Turnaround is within one business day, a REST API is offered, and bulk terms go through sales. **[VERIFIED vendor page, via search summary]** — [Planner 5D B2B recognition](https://tool.planner5d.com/b2b-floor-plan-recognition)
- **Commercial: ARCHLine.XP vectoriser.** It recommends 300–500 DPI scans, and the user sets scale manually from a known dimension or a door width. **[VERIFIED vendor help]** — [ARCHLine.XP help](https://help.archlinexp.com/hc/en-us/articles/20856004418449-From-raster-to-BIM-Converting-floor-plans-to-3D-models)

### Inferences
- **[ESTIMATE]** Expected wall-geometry accuracy by input type:
  - Clean digital PDFs or CAD-exported PNGs, with a 2026-class model (FloorplanVLM-style, or a fine-tuned segmenter plus vectorisation): roughly 90–97% wall IoU.
  - Phone photos and scans of paper plans: roughly 70–85%.
  - The step from pixel IoU to *topologically correct, closed room polygons with correct openings* is where most residual errors sit. That makes a human confirm/edit step necessary for any output sold as "dimensionally accurate".
- **[ESTIMATE]** Open-source licences, unverified this session: the CubiCasa5K dataset is CC BY-NC 4.0, i.e. **non-commercial**. Production use would need a CubiCasa licence or a retrain on own or licensed data. RoomFormer is MIT (verified above).
- **[HYPOTHESIS]** FloorplanVLM-style models trained on Beike's Chinese-market data may degrade on UK/EU/US drafting conventions. **Test:** score 200 local-market plans, half clean and half scanned, on wall IoU, room-polygon F1, door/window F1 and area error; compare against a fine-tuned open segmenter plus heuristic vectoriser.

### Gaps
- Exact door, window and room-level metrics were not extracted from the MitUNet, FloorplanVLM, Raster-to-Graph or RPLAN, MSD or FloorPlanCAD papers. Full PDFs need reading for per-class tables.
- FloorPlanCAD (CAD panoptic symbol spotting, ICCV 2021) and MSD (Modified Swiss Dwellings, ECCV 2024) were not checked this session.
- I could not confirm whether FloorplanVLM weights are released, or under what licence; only FPBench-2K is stated as open-sourced.
- Commercial pure-API vectorisers (for example Getfloorplan's API, Archilogic) had no technical accuracy disclosures in the results.

---

## 2. How well frontier multimodal LLMs read floor plans

### Takeaway
No published benchmark measures frontier LLMs on *reading dimension strings and extracting precise vector geometry from architectural drawings*. Adjacent benchmarks find that spatial reasoning is improving but unreliable. LLMs should not be the geometry extractor of record. They are useful for semantics, OCR cross-checking, schedule parsing and code generation against a validated intermediate representation.

### Cited Findings
- **Current Claude lineup (official, Oct 2026):**

  | Model | Price (input / output per MTok) |
  |---|---|
  | Claude Fable 5.1 (`claude-fable-5-1`) | $10 / $50 |
  | Claude Opus 5.5 (`claude-opus-5-5`) | $4 / $20 |
  | Claude Sonnet 5.5 (`claude-sonnet-5-5`) | $2 / $10 |
  | Claude Haiku 5.5 (`claude-haiku-5-5`) | from $0.10 / $0.50 |

  All have a 1M-token context, 128K max output, and text plus image input. Batch is 50% off. **[VERIFIED]** — [Claude models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- **Blueprint-Bench (Andon Labs, 2025)** converts about 20 apartment photos into a 2D floor plan:
  - Human 0.547 (12-apartment subset).
  - GPT-5 0.431, Gemini 2.5 Pro 0.421.
  - Claude Opus 4 0.286, Claude Sonnet 4 0.272.
  - Random baseline 0.279.
  - Nano Banana (Gemini 2.5 Flash Image) 0.168, GPT Image 0.300.

  "Most models perform at or below our random baseline". Agentic iteration (Claude Code, Codex) "showed no meaningful improvement". **[VERIFIED]** This measures photo-to-plan, not plan-reading, and the models tested are now superseded. — [Andon Labs Blueprint-Bench](https://andonlabs.com/evals/blueprint-bench); [arXiv 2509.25229](https://arxiv.org/abs/2509.25229)
- A "Blueprint-Bench 2" column appears in an Oct 2026 leaderboard aggregator, but no per-model scores were captured. **[SECONDARY]** — [BenchLM multimodal](https://benchlm.ai/multimodal-grounded)
- **FloorplanQA (Wonka group, v3 Jan 2026)** gives LLMs symbolic JSON/XML layouts and asks about distance, visibility, path-finding and placement across 15 LLMs. Models "succeed in shallow queries" but "often fail to respect physical constraints, preserve spatial coherence". **[VERIFIED abstract]** — [arXiv 2507.07644](https://arxiv.org/abs/2507.07644)
- **Snap Spatial Benchmark (2026)** has 80 questions on 3D placement, transforms and engine conventions. GPT-5.5 scored 93.8%, Gemini 3 Flash Preview 92.5%, Claude Fable 5 88.8%, and Claude Opus 4.8 87.5%. Gaps remain "around 3D engine-specific conventions and engine-native spatial code patterns". **[VERIFIED vendor blog]** — [Snap Engineering](https://eng.snap.com/spatial_intelligence)
- On the AIMultiple visual-reasoning benchmark, Gemini 3.1 Pro scored 71 overall (visual logic 58), GPT-5.2 67, Claude Opus 4.6 55 (visual logic 36) and Claude Sonnet 4.6 52. **[SECONDARY]** — [AIMultiple](https://aimultiple.com/visual-reasoning)

### Inferences
- **[ESTIMATE]** Text-domain spatial reasoning over *structured* geometry is now strong (about 88–94% on Snap's benchmark). Pixel-to-geometry extraction is weak (Blueprint-Bench). The architecture should therefore have a CV model or deterministic parser produce JSON geometry, with the LLM reasoning over that JSON. That is where LLMs are most reliable.
- **[ESTIMATE]** LLMs reliably write Blender Python, Three.js and JSON *when given explicit coordinates*. The risk lies in inventing coordinates, not in syntax. Mitigations are schema-constrained outputs (tool use or JSON schema) and deterministic validators, such as closed polygons, wall thickness ranges and a door width plausibility band of 0.6–1.0 m.
- **[ESTIMATE]** Known failure modes, consistent across the benchmarks above: miscounting rooms and openings, swapping adjacency, ignoring scale consistency, and confidently claiming success (Andon Labs notes Claude Code "claiming success" while wrong).

### Gaps
- No benchmark was found for **OCR of dimension strings** (for example 3.45 m or 11'-4") on plans, or for **scale inference** by LLMs. **Test to resolve:**
  - Build 300 plans with ground-truth vectors: clean CAD exports, scans, and with or without dimensions.
  - Ask Claude Opus 5.5, Sonnet 5.5, GPT-5.5 and Gemini 3.x for: (a) every dimension string with its bounding box; (b) room areas; (c) wall endpoint coordinates in metres.
  - Metrics: dimension-OCR exact match; area error (MAPE); endpoint error (mm); room-count accuracy; JSON validity.
  - Compare against PaddleOCR or docTR plus a deterministic dimension-line parser.
- No Blueprint-Bench scores were found for Claude Opus 5.5, Sonnet 5.5, GPT-5.5 or Gemini 3.5.

---

## 3. Missing dimensions, scale inference, multi-storey, stairs, roofs, curved walls

### Takeaway
These are the main sources of unrecoverable error in raster-only pipelines. Scale can be inferred from door widths, scale bars or a stated total area, but only to within a few percent. Multi-storey alignment, roof pitch and stair geometry are generally *not present* in a 2D plan and must be assumed or supplied by a user. Curved and slanted walls are newly handled by sequence models such as FloorplanVLM.

### Cited Findings
- ARCHLine.XP's commercial vectoriser has the user set scale from "a recognizable distance in the image, such as a dimension or a known door length". **[VERIFIED]** — [ARCHLine.XP help](https://help.archlinexp.com/hc/en-us/articles/20856004418449)
- FloorplanVLM explicitly targets "slanted walls and curved arcs" and reports "robust generalization across non-Manhattan architectures". **[VERIFIED abstract]** — [arXiv 2602.06507](https://arxiv.org/abs/2602.06507)
- FloorplanQA finds that LLMs fail to "respect physical constraints" on layouts, which bears on stairs and clearances. **[VERIFIED abstract]** — [arXiv 2507.07644](https://arxiv.org/abs/2507.07644)

### Inferences
- **[ESTIMATE]** Door-width scale inference: interior doors vary by about 0.70–0.90 m in UK/EU and 28–36" in US, so a single-door estimate can be off by ±10–15%. Taking the median of several doors, or adding a stated GIA/total area, should tighten this to about ±3–5%. **[HYPOTHESIS]** Test: on 200 plans with known scale, compare the error of door-median, scale-bar, OCR-dimension least-squares fit and stated-area methods.
- **[ESTIMATE]** The best practice is a *least-squares scale fit* across all OCR'd dimension strings matched to the detected wall segments they annotate. Inconsistency between strings becomes a QA flag, and an LLM can help pair strings to segments.
- **[ESTIMATE]** Multi-storey alignment can be automated by matching stair footprints and external wall outlines between levels (rigid 2D registration). It should be confirmed by the user. Floor-to-floor height, roof pitch and form, and stair riser count must come from a section, elevation or user input, or from defaults that are labelled as defaults.

### Gaps
- No academic benchmark for multi-storey alignment or roof inference from 2D plans was found.

---

## 4. CAD/BIM route: DWG/DXF/IFC tooling, licensing, cost and reliability

### Takeaway
Vector CAD and IFC inputs remove the recognition problem entirely. Geometry is exact by construction, so the remaining issues are layer semantics and data quality. Production-viable SaaS stacks exist:
- **ezdxf** for DXF.
- **ODA Drawings SDK**, Sustaining tier at $7,500 then $4,500/yr, for DWG in SaaS.
- **IfcOpenShell** or **web-ifc** (MPL-2.0) for IFC.
- **Autodesk APS** (pay-as-you-go Flex tokens) as an alternative DWG/RVT path.

### Cited Findings
- **ODA membership** (cached page; agreements dated Oct 2025):

  | Tier | Initial | Renewal | Terms |
  |---|---|---|---|
  | Commercial | $3,000 | $2,250 | limited; fewer than 100 desktop/mobile copies per year |
  | Sustaining | $7,500 | $4,500 | unlimited, **including web/SaaS** |
  | Founding | $37,500 | $18,000 | adds source code |

  **[VERIFIED via search summary of the ODA pricing page and FAQ; reconfirm before budgeting]** — [ODA pricing](https://www.opendesign.com/pricing.md); [ODA FAQ](https://www.opendesign.com/faq/question/how-can-i-join-open-design-alliance-and-use-your-sdks.md)
- **Autodesk APS:**
  - There is a free tier, plus subscriptions with pooled monthly usage, plus Flex tokens. Enterprise volume discounts start at 5,000+ tokens.
  - Data Model API pricing took effect for Manufacturing on 17 Aug 2026 and for AEC on 6 Oct 2026.
  - Model Derivative token rates were not captured.

  **[VERIFIED]** — [APS blog, 3 Sep 2026](https://aps.autodesk.com/blog/coming-august-data-model-apis-included-subscriptions-plus-flexible-ways-scale); [APS pricing](https://aps.autodesk.com/pricing)
- **web-ifc (That Open Company)** reads and writes IFC in JS/WASM "at native speeds" and is licensed **MPL-2.0**. **[VERIFIED]** — [GitHub ThatOpen/engine_web-ifc](https://github.com/ThatOpen/engine_web-ifc)

### Inferences
- **[ESTIMATE]** Licences unverified this session:
  - IfcOpenShell: LGPL-3.0.
  - ezdxf: MIT.
  - LibreDWG: **GPL-3.0**, a copyleft risk if linked into distributed software. Running it server-side only is less risky, but get legal sign-off.
  - Speckle: Apache-2.0 server and connectors.
- **[ESTIMATE]** Reliability: DWG/DXF gives exact geometry, but semantic classification depends on layer naming, which varies by firm. Expect walls, doors and windows to be classified correctly about 80–95% of the time using layer heuristics plus block names, with LLM help mapping arbitrary layer names to a canonical set. IFC gives typed IfcWall, IfcDoor, IfcSlab and IfcStair, with near-100% semantic fidelity on well-authored models.
- **[HYPOTHESIS]** "CAD/IFC is an order of magnitude more reliable than raster" for geometry. **Test:** run the same 50 projects as IFC, DWG and raster PDF exports through the pipeline and compare wall endpoint error and room-area error against the IFC ground truth.

### Gaps
- APS Model Derivative per-job token cost was not found. A Revit RVT-to-IFC/SVF translation cost model is needed.
- The Speckle hosted pricing page and the IfcOpenShell licence were not checked this session.

---

## 5. Rendering engines and real-time/web delivery: capability and licensing

### Takeaway
For an automated SaaS:
- **Blender headless (Cycles/EEVEE)** is the lowest-cost, most automatable offline renderer. Blender says outputs belong to the user, and GPL applies to the program, not the renders.
- **Three.js** or **Babylon.js** with glTF is the default for browser walkthroughs.
- **Unreal Engine**: linear archviz output from companies with $1M+ revenue needs $1,850/seat/yr. *Distributing* a runtime app to third parties (pixel streaming product) triggers the **5% royalty over $1M**.
- **Unity Industry** costs $4,950/seat/yr.
- Gaussian-splat web rendering is now production-grade (Spark 2.x, three.js r186 native splats), but splats need captures or generation and are *not dimensionally authoritative*.

### Cited Findings
- **Blender licensing:** "output of Blender, in the form of .blend files, is considered program output, and the sole copyright of the user". Older artist FAQs add that renders and exports are the user's property, and that Python scripts are separate works. **[VERIFIED FAQ; mailing-list items PRE-2025]** — [Blender FAQ](https://www.blender.org/support/faq/); [bf-committers 2004](https://lists.blender.org/pipermail/bf-committers/2004-November/008253.html)
- **Unreal Engine pricing:**
  - Non-game companies with more than $1M annual gross revenue pay **$1,850 per seat per year**. Linear content explicitly includes "architectural visualizations".
  - "If you're developing a non-game application that is licensed to third-party end users and relies on Unreal Engine code at runtime then you will need to pay royalties": **5% over $1M** lifetime gross.
  - From 27 May 2026, Unreal Subscriptions no longer include Twinmotion and RealityScan.

  **[VERIFIED]** — [Epic blog](https://www.unrealengine.com/blog/we-are-updating-unreal-engine-twinmotion-and-realitycapture-pricing-in-late-april)
- **Unity Industry** costs $4,950/yr per seat, with CAD/BIM integration and deployment to more than 20 platforms. **[VERIFIED]** — [Unity Industry](https://unity.com/products/unity-industry)
- **Spark (World Labs)** is an MIT-licensed Gaussian-splat renderer for three.js (r180+), running on WebGL2. Spark 2.0 (14 Apr 2026) added an LoD system that streams very large 3DGS worlds. It reads PLY and SPZ. **[VERIFIED via World Labs blog and Spark docs]** — [World Labs Spark 2.0](https://www.worldlabs.ai/blog/spark-2.0); [sparkjs.dev](https://sparkjs.dev/docs/overview/)
- **three.js r186** shipped a native Gaussian splat renderer and splat raycasting. **[SECONDARY]** — [RadianceFields](https://radiancefields.com/three.js-ships-its-native-gaussian-splat-renderer-and-splat-raycasting-in-r186)
- **World Labs Marble:**
  - Generates explorable worlds from prompts and images and exports SPZ/PLY splats (about 2M or 500K splats), collider meshes and GLB.
  - Splat export needs the paid Standard plan. Textured GLB and **commercial rights need Pro**.

  **[VERIFIED docs index; plan details partly SECONDARY]** — [Marble splat export docs](https://docs.worldlabs.ai/marble/export/gaussian-splat/index.md); [third-party skill summary](https://skills.cat/skills/cloudai-x/world-labs-skills/world-labs-export)

### Inferences
- **[ESTIMATE]** Recommended rendering stack:
  - Offline stills and video: Blender 4.x/5.x headless on GPU workers (Cycles for hero shots, EEVEE for drafts).
  - Interactive: glTF/GLB with KTX2 and Draco in Three.js or Babylon (unverified this session: MIT and Apache-2.0 licences respectively) with baked lightmaps.
  - Premium real-time: Unreal pixel streaming, but only after a royalty and EULA legal review, because a SaaS offering an Unreal-runtime walkthrough to end users is likely "licensed to third-party end users".
- **[ESTIMATE]** Marble-type generated splats suit *mood/conceptual* walkthroughs (class A). They are not suitable for class C, because geometry is hallucinated from images and has no metric guarantee.
- **[ESTIMATE]** Chaos V-Ray/Corona cloud, D5, Enscape and NVIDIA Omniverse are designed around desktop authoring. Their headless and API automation for multi-tenant SaaS is limited or enterprise-negotiated. This could not be verified this session.

### Gaps
- Chaos Cloud API, D5 Render API, Enscape automation and Omniverse (Kit/RTX headless, NVIDIA AI Enterprise licensing) terms were not checked.
- No legal confirmation was found that Unreal pixel-streaming SaaS counts as "licensed to third-party end users". Epic's EULA FAQ or direct contact is needed.

---

## 6. Generative visual layer: conditioned image models, video, PBR, and licences

### Takeaway
Depth-, edge- and segmentation-conditioned image generation and image editing (FLUX Kontext, gpt-image, Gemini image) can photorealistically *shade* a deterministic render. They do not preserve exact geometry, and no published metric guarantees it. Video models (Veo, Sora, Runway, Kling, Luma) are improving at 3D consistency in research, but there is no published guarantee of geometric faithfulness to a given model. Self-hosting BFL open weights commercially costs $999/month.

### Cited Findings
- **BFL self-serve commercial licence for open-weight FLUX.1 [dev] variants, including Kontext [dev]:** **$999/month for up to 100,000 images, then $0.01/image**. The base FLUX.1 [dev] Non-Commercial Licence requires content filters or manual review. **[VERIFIED BFL page]** — [BFL licensing](https://bfl.ai/pricing/licensing); [BFL Kontext dev announcement](https://bfl.ai/blog/flux-1-kontext-dev)
  - One source says Kontext [dev] is under the FLUX.2 NC licence; BFL's own page says FLUX.1 [dev] NC. **[CONFLICT]** — [AlternativeTo](https://alternativeto.net/news/2025/6/black-forest-labs-launches-flux-1-kontext-dev--a-new-12b-parameter-image-editing-model/) vs BFL
- **Image models fail at layout:** on Blueprint-Bench, image models scored *below random*. Nano Banana scored 0.168 and added "forbidden details like furniture"; GPT Image scored 0.300. This is direct evidence that image generators should not be trusted for layout. **[VERIFIED]** — [Andon Labs](https://andonlabs.com/evals/blueprint-bench)
- **Research on 3D-consistent video (2026):**
  - ViewRope proposes a camera-ray positional encoding and ViewBench, a benchmark for view consistency and loop closure. — [arXiv 2602.07854](https://arxiv.org/pdf/2602.07854)
  - Geometry-as-context (CVPR 2026) — [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_Geometry-as-context_Modulating_Explicit_3D_in_Scene-consistent_Video_Generation_to_Geometry_CVPR_2026_paper.html)
  - WorldStereo — [arXiv 2603.02049](https://arxiv.org/abs/2603.02049)
  - VideoGPA, which states current models "still show deficiencies in 3D consistency". — [arXiv 2601.23286](https://arxiv.org/html/2601.23286)
  - 3DScenePrompt (Sony, ICLR 2026) — [Sony AI](https://ai.sony/publications/3d-scene-prompting-for-scene-consistent-camera-controllable-video-generation)

  **[VERIFIED abstracts]**

### Inferences
- **[ESTIMATE]** The "render-then-enhance" pattern is the only defensible route to class B:
  1. Render beauty, depth, normal, object-ID/segmentation and line passes from the true model.
  2. Apply constrained img2img: low denoise, around 0.2–0.4, with depth or canny ControlNet, or instruction editing with Kontext, gpt-image or Gemini.
  3. **Measure drift automatically:** run edge detection on input and output and compute Chamfer distance or edge-F1 on structural edges; check segmentation-mask IoU per object ID; reject frames above a threshold.
  4. Optionally composite the original geometry edges back in.
- **[ESTIMATE]** For video, do not use text- or image-to-video for structurally faithful walkthroughs. Render the camera path in Blender or the real-time engine, then (optionally) apply per-frame or video-to-video style transfer with temporal consistency, and check drift per frame. Pure gen-video (Veo, Kling and others) is class A only.
- **[ESTIMATE]** PBR materials: author or license a curated PBR library (for example CC0 sources such as ambientCG and Poly Haven; licences unverified this session) mapped from finish-schedule codes. Generative texture models are acceptable for novel finishes but need a tileability and roughness sanity check.
- **[HYPOTHESIS]** Low-denoise depth-conditioned enhancement keeps structural edges within about 1–2% of image width. **Test:** take 500 render/enhance pairs, run edge-F1 at 2px tolerance and per-object mask IoU, and plot drift against the denoise strength sweep.

### Gaps
- OpenAI gpt-image and Google Imagen/Gemini image commercial terms and pricing pages were not fetched. Google and OpenAI API terms generally assign outputs to the customer (unverified this session).
- No published per-model geometry-preservation numbers exist for Veo, Sora, Runway, Kling or Luma. ViewBench-style evaluation on architectural camera paths is the test needed.
- Licensing for Stable Diffusion 3.5 and SDXL (Stability Community Licence, with a revenue threshold) was not verified this session.

---

## 7. Guaranteeing dimensional accuracy and non-hallucination; the minimum human-in-the-loop step; evidence from products

### Takeaway
Every commercial product examined either controls capture (CubiCasa phone scan, 24-hour turnaround with a "QA process") or puts a human reviewer on each AI result (Planner 5D says so explicitly). Getfloorplan claims automation, but only third-party directories describe it. The evidence supports one mandatory, minimal HITL step: **confirm/edit the 2D vector interpretation and scale** before any 3D generation. Everything downstream can then be deterministic.

### Cited Findings
- **CubiCasa:**
  - The user scans with a phone and receives a floor plan "in up to 24h". The process uses "advanced image-recognition technology and a QA process".
  - PLUS costs $15, PLUS 3D $65, CAD export $35.
  - CubiCasa claims 4M scans and 200,000+ companies.

  **[VERIFIED vendor pages]** — [CubiCasa start](https://www.cubi.casa/start-scanning-first-floor-plan/); [CubiCasa smartphone page](https://www.cubi.casa/create-2d-floor-plan-smartphone/); [CubiCasa blog feed](https://www.cubi.casa/tag/floor-plan-app/feed/)
- A CubiCasa post contrasts AI photo-editing turnaround of 30 minutes with 8–12 hours for human editors, which implies human editors were historically used for that product line. **[SECONDARY (social post)]** — [CubiCasa Facebook](https://www.facebook.com/cubicasaInc/posts/our-latest-blog-covers-everything-you-need-to-know-from-ai-powered-editing-and-o/1605939558240066/)
- **Planner 5D:** a human designer reviews every AI result, and turnaround is one business day. **[VERIFIED]** — [Planner 5D](https://tool.planner5d.com/b2b-floor-plan-recognition)
- **Getfloorplan:**
  - Input is a JPG/PNG/PDF upload. Output is 2D, 3D and a 360 tour within about 24 hours.
  - Directories cite "no human involvement required" and up to 1,000 renders a day.
  - Prices of about $20–$69 per set conflict between sources.

  **[SECONDARY, unverified]** — [Capterra](https://www.capterra.com/p/10008922/Getfloorplan/); [genai.works](https://genai.works/applications/getfloorplan)
- On Blueprint-Bench, agents that iterated still produced errors "despite claiming success". This supports external validators over LLM self-checks. **[VERIFIED]** — [Andon Labs](https://andonlabs.com/evals/blueprint-bench)

### Inferences
- **[ESTIMATE]** A 24-hour turnaround across vendors is a tell: it is consistent with queued human QA rather than pure automation. This is unconfirmed for Getfloorplan.
- **[ESTIMATE]** Minimum HITL design: a browser 2D editor showing the detected walls, openings and rooms overlaid on the source image, with confidence heatmaps, scale confirmation (pick one known dimension) and storey alignment. Target under 3–5 minutes per plan for clean inputs and 10–15 for scans. **[HYPOTHESIS]** Test: time trials with five operators on 50 plans.
- **[ESTIMATE]** The "geometry is truth" contract:
  1. A canonical vector model, a JSON schema or IFC subset, is the only source of geometry.
  2. All renders and walkthroughs are derived from it.
  3. AI enhancement may change pixels but must pass automated drift checks.
  4. Any measured value displayed (areas, dimensions) comes from the model, never from generated imagery.

### Gaps
- Cedreo, RoomSketcher and Floorplanner workflows were not researched this session. They are largely user-drawn editors with optional paid drafting services, per prior knowledge (unverified).

---

## 8. Feasibility scores, required technology and engineering difficulty by output class

### Takeaway
A is feasible now and commoditised. B is feasible with a deterministic render core plus constrained AI enhancement and an HITL vector check. C is feasible from CAD/IFC inputs, and from raster only with human confirmation. Dimensional accuracy cannot be honestly claimed from unreviewed raster input.

### Cited Findings
- Scores below draw on the evidence in sections 1–7: wall IoU on CAD-derived vs scanned images ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0926580526004346)), FloorplanVLM ([arXiv](https://arxiv.org/abs/2602.06507)), Blueprint-Bench ([Andon Labs](https://andonlabs.com/evals/blueprint-bench)), Unreal licensing ([Epic](https://www.unrealengine.com/blog/we-are-updating-unreal-engine-twinmotion-and-realitycapture-pricing-in-late-april)), Spark ([World Labs](https://www.worldlabs.ai/blog/spark-2.0)), and human-in-the-loop vendors ([Planner 5D](https://tool.planner5d.com/b2b-floor-plan-recognition)).

### Inferences (all [ESTIMATE])

| Class | Feasibility /10 | Demonstrated vs experimental | Required tech | Engineering difficulty |
|---|---|---|---|---|
| **A. AI conceptual images** (mood, style, "inspired by this plan") | **9/10** | DEMONSTRATED: text/image-to-image (FLUX, gpt-image, Gemini image), gen-video, Marble worlds | Image/video APIs, prompt building from plan semantics (LLM) | Low (2–4 eng-months for production quality and moderation) |
| **B. Structurally faithful renders** (stills/video matching the real layout, openings, finishes) | **7.5/10** | DEMONSTRATED: deterministic render from vector or BIM (Blender, Unreal). EXPERIMENTAL: automated AI enhancement with *measured* geometry preservation; no public benchmark | Vectoriser + HITL editor + procedural 3D builder + PBR library + Blender headless + constrained img2img + drift QA | Medium–High (6–12 eng-months) |
| **C. Navigable, dimensionally accurate 3D** (web walkthrough, true metres) | **8/10 from IFC/DWG; 6/10 from raster with HITL; 3/10 fully automated from raster** | DEMONSTRATED for IFC/CAD (web-ifc, Three.js). Raster: demonstrated only with a human check (Planner 5D, CubiCasa QA). Fully automatic: EXPERIMENTAL | IFC/DXF parsers, ODA SDK, canonical schema, glTF export, lightmap baking, Three.js/Babylon viewer, optional splats for context only | High (9–15 eng-months; multi-storey, stairs and roofs dominate) |

### Gaps
- Scores are analyst judgement. No end-to-end public benchmark exists. Test: a 100-project gold set (IFC ground truth plus PDF exports plus scans), with per-stage metrics as in section 9.

---

## 9. Recommended component architecture, accuracy per stage, and where LLMs help vs deterministic/CV

### Takeaway
Use specialist CV and deterministic geometry for everything that produces numbers. Use Claude Sonnet 5.5 or Haiku 5.5 for classification, mapping and schedule parsing. Use Opus 5.5 for occasional hard reasoning: ambiguous plan interpretation, QA explanations, code generation against the schema. Use image models only for final-pixel enhancement behind automated drift gates.

### Cited Findings
- Claude model tiers and prices: Haiku 5.5 from $0.10/$0.50, Sonnet 5.5 $2/$10, Opus 5.5 $4/$20 per MTok; batch is 50% off. — [Claude models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- LLMs are strong on structured spatial reasoning (Snap Spatial Benchmark, 87.5–93.8% for top models) — [Snap](https://eng.snap.com/spatial_intelligence). They are weak on photo- or image-to-plan (Blueprint-Bench) — [Andon Labs](https://andonlabs.com/evals/blueprint-bench). They are inconsistent on physical constraints (FloorplanQA) — [arXiv 2507.07644](https://arxiv.org/abs/2507.07644).
- Image-to-JSON VLM vectorisation reaches 92.5% external-wall IoU — [arXiv 2602.06507](https://arxiv.org/abs/2602.06507).

### Inferences (all [ESTIMATE] unless noted; "accuracy" means expected first-pass correctness before the human check)

| Stage | Recommended tech | Deterministic / CV / LLM | Likely accuracy |
|---|---|---|---|
| 1. Ingestion | File type sniffing; PDF vector vs raster detection (PyMuPDF/pdfium); DWG via ODA SDK (Sustaining tier for SaaS); DXF via ezdxf; IFC via IfcOpenShell (server) or web-ifc (client) | Deterministic | ~99% format handling |
| 2. Parsing | **Vector PDF/DXF/DWG:** extract lines and blocks directly, and use an LLM (Haiku/Sonnet) to map layer and block names to canonical classes. **Raster:** wall/opening segmentation (MitUNet-class, or a FloorplanVLM-class VLM if licensable) + OCR (PaddleOCR/docTR) for dimensions and room labels | CV + deterministic; LLM for layer mapping and room-label semantics | Vector: 90–98% classification. Raster clean: 90–97% wall IoU. Scans: 70–85% |
| 3. Geometry reconstruction | Vectorisation: skeletonise, fit lines/arcs, snap junctions, enforce Manhattan where justified; least-squares scale fit to OCR dimension strings; room polygonisation; storey registration | Deterministic (Shapely/CGAL); LLM may pair dimension strings with segments, with each pairing then verified numerically | Scale ±1–2% with dimensions; ±3–15% from door widths only |
| 4. **Human confirm/edit (mandatory for raster)** | Web 2D editor showing confidence overlays | Human | Raises output to near-100% topological correctness |
| 5. Structural validation | Rule engine: closed rooms, wall thickness bands, opening-in-wall containment, door swing clearance, stair rise/going rules, area reconciliation against stated GIA | Deterministic; LLM writes human-readable issue explanations | Catches most gross errors; cannot detect plausible-but-wrong layouts |
| 6. Material assignment | Parse the finish schedule (PDF/XLSX) with an LLM (Sonnet 5.5) into structured room→surface→finish code; map to a curated PBR library via embedding search and LLM rerank | LLM + retrieval; deterministic UV/scale rules | Schedule extraction likely high on clean tables (untested; needs eval); material match subjective |
| 7. Scene generation | Procedural builder: extrude walls, boolean openings, door/window parametric families, slabs, ceilings, simple roof from user parameters; furniture via rule-based or LLM-proposed layout *constrained* by a collision/clearance checker; export glTF and IFC | Deterministic; LLM proposes furnishing JSON, a solver validates it | Geometry exact relative to the confirmed vector |
| 8. Rendering | Blender headless (Cycles/EEVEE) for stills and video; baked lightmaps plus Three.js/Babylon for web; optional Unreal pixel streaming after licence review | Deterministic | Exact geometry by construction |
| 9. AI enhancement (optional) | Depth/edge-conditioned img2img or instruction edit (FLUX Kontext under BFL commercial licence, gpt-image, Gemini image) at low denoise | Generative | Drift unmeasured publicly; gate per frame |
| 10. QA | Automated: edge-F1 and mask IoU between base render and enhanced output; area and dimension re-measurement from the model; LLM-as-judge (Opus 5.5) for visual artefacts *as an advisory signal only* | Deterministic + CV; LLM advisory | Target: reject >X% drift (threshold to be set from the section 6 test) |
| 11. Delivery | CDN-hosted glTF/KTX2 viewer, MP4 video, stills, optional splat context via Spark; measured values come only from the model | Deterministic | n/a |

- **Where LLMs add measurable value:**
  - Layer and block name mapping.
  - Room-label and finish-schedule extraction.
  - Pairing dimension strings with walls, verified numerically.
  - Furnishing proposals as constrained JSON.
  - Writing Blender/Three.js glue code at development time.
  - QA explanations and customer-facing summaries.
  - Advisory visual QA.
- **Where LLMs should not be used as the source of truth:** pixel-to-coordinate extraction, scale determination, wall endpoints, area values, and structural judgements.
- **Model routing:** Haiku 5.5 for bulk classification and mapping; Sonnet 5.5 for schedule parsing and pairing; Opus 5.5 for hard ambiguous cases and QA reasoning. Fable 5.1 is not needed in the hot path; its value here is a hypothesis.

### Gaps
- Per-stage accuracy figures are estimates. The validation programme needed is a gold set of 100 projects, with a matched IFC truth plus PDF and scan derivatives where available. Measure per stage:
  - Wall IoU.
  - Opening F1.
  - Room-polygon F1.
  - Area MAPE.
  - Scale error.
  - Schedule-extraction F1.
  - Render drift edge-F1.
  - HITL minutes per plan.
- Claude-specific evals for dimension OCR and finish-schedule extraction have not been published. Run the section 2 test.
