# Competitor Landscape: AI-powered, white-label property visualisation SaaS (floor plan / CAD / BIM to 3D, renders, tours, video). UK focus, checked October 2026

Method note: Researched 18–20 Oct 2026. I read vendor pricing pages directly where I could (Getfloorplan, RoomSketcher, CubiCasa, Cedreo, BoxBrownie, Virtual Staging AI, Collov, Esoft, Rendair). Other per-vendor fields come from an Exa research-agent pass over official pages, help centres and review sites (sources listed per row), plus targeted searches. "UNVERIFIED" means I could not confirm the item on a primary source. Prices are as published on the source page when checked (Oct 2026) unless another date is given. Review-site complaints are anecdotal opinions, not established facts.

## Q1. Which competitors already go upload-plan → 3D → renders automatically, and how much human drafting is behind it?

### Takeaway
Many tools take an uploaded 2D plan, but almost none deliver fully automatic, geometry-true 3D, photoreal renders and interactive tours together without a human in the loop. Getfloorplan is the closest direct analogue: AI plus a human QA team, about 24h turnaround, $25–$115 per set, white-label from the $61 tier. RoomSketcher, Maket and Archilogic sell either AI conversion with manual correction or explicitly human "white-glove" redraws. BoxBrownie and Styldod are human redraw services. CubiCasa, Giraffe360, Matterport and Floorfy need a site capture (app, camera or 360 photos), so they cannot work off-plan. Generative AI renderers (Rendair, MNML, LookX, Interior AI, Spacely, Collov) produce images, not trustworthy geometry.

### Cited Findings — per-competitor profiles

**1. Getfloorplan** (getfloorplan.com). Most direct competitor.
- Audience: agents, developers/construction, marketing and 3D agencies — [Getfloorplan](https://getfloorplan.com/)
- Pricing (Oct 2026): Basic set (2D+3D) $25; Plus set (2D, 3D, 360 tour) $45; Pro set (adds white label) $61; Max Render set (adds renderings) $69; Multi Set Pro (3 styles in one) $115. Custom add-ons include an "editable 3D model FBX/GLB scene from basic floorplan", custom window views (200+ options) and exterior/garden — [Getfloorplan pricing](https://getfloorplan.com/pricing). StagingMate recorded the same prices on 9 Oct 2026 — [StagingMate](https://stagingmate.com/compare/getfloorplan-alternative)
- Upload: JPG, PNG, DWG, PDF, one apartment or house floor per file — [Getfloorplan personal](https://getfloorplan.com/for-personal-users)
- Automatic vs human: AI generation with results checked by a Quality Assurance team; customisation and edits are done by that team — [Getfloorplan personal](https://getfloorplan.com/for-personal-users). Third-party reviews say every render goes through human QA, which is why delivery takes about 24h — [StagingMate](https://stagingmate.com/compare/getfloorplan-alternative); [Aigregator](https://aigregator.com/tools/getfloorplan). A Japanese DB says it renders with Unreal Engine (UNVERIFIED on primary source) — [PERSC DB](https://db.persc.jp/getfloorplan/)
- Claims capacity of up to 1,000 floor plans in 24h — [Capterra UK](https://www.capterra.co.uk/software/1048926/getfloorplan)
- Interactive 3D: 360 tours/VR. White label: yes, from the Pro set. API: developer/integration page exists — [Getfloorplan developers](https://getfloorplan.com/developers)
- Complaints: Trustpilot 4.2 from 27 reviews (snapshot). Complaints include "Sloppy rendering… Parts of the building had no roof" (Dec 2024), missed 24h delivery, refund and order handling, and an incentive-for-review offer — [Trustpilot](https://www.trustpilot.com/review/getfloorplan.com). Cannot incorporate a user's own furniture moodboard — [Home Stratosphere](https://www.homestratosphere.com/2d-layout-to-3d-virtual-tour/). Users say customisation is limited, e.g. wall and floor colours — [Trustpilot UK p2](https://uk.trustpilot.com/review/getfloorplan.com?page=2). StagingMate reports 4.5/5 from 30 reviews as of Oct 2026, which conflicts with the 4.2/27 snapshot (timing difference) — [StagingMate](https://stagingmate.com/compare/getfloorplan-alternative)
- Strengths: price, speed, bundle (2D, 3D, 360, renders), white label at $61.
- Our potential advantage: self-serve editing, true editable geometry and a developer-grade brand portal instead of a per-order service. No human-QA bottleneck if our automation actually holds up.

**2. RoomSketcher** (roomsketcher.com)
- Pricing (Oct 2026, USD excl. VAT): Free; Pro $24/mo monthly or $12/mo billed $144/yr; Team $70/mo or $35/mo billed $420/yr (5 users); Enterprise custom (API integration, custom branding). Order Floor Plans (human drawing service) $38/floor on Free, from $18/floor on Pro/Team; AI Convert $20/floor; FloorCapture $20/floor — [RoomSketcher pricing](https://www.roomsketcher.com/pricing/)
- Upload/automation: AI Convert takes JPG/PNG/PDF and maps walls, doors and windows into an editable project, but not furniture. Hand-drawn or low-quality plans must be traced manually. CAD input is not supported — [RoomSketcher AI Convert](https://www.roomsketcher.com/features/ai-convert/). A separate human "expert illustrators" redraw service exists — [RoomSketcher order](https://www.roomsketcher.com/order-floor-plans/)
- Interactive 3D: Live 3D and 360 Views. White label: own branding on Pro/Team; "custom branding setup" on Enterprise — [pricing](https://www.roomsketcher.com/pricing/)
- Complaints: auto-renewal and invoice issues, credit costs, glitches, hard-to-edit wall outlines. Many reviewers also praise support — [Trustpilot](https://www.trustpilot.com/review/roomsketcher.com); [Capterra](https://www.capterra.com/p/164021/RoomSketcher/)
- Our advantage: photoreal renders and video at developer quality, CAD/BIM ingest, and multi-unit development projects. RoomSketcher is unit-centric and schematic in style.

**3. CubiCasa** (cubi.casa)
- Pricing: tiers Lite, Standard, Plus and Plus 3D. The current page shows no prices. Plus 3D includes a 3D floor plan with furniture and textures (48h). CAD (.dwg/.dae/.obj/.fbx) and 3D video renders are add-ons — [CubiCasa pricing](https://www.cubi.casa/pricing/). Older help content cited a $15 Plus upgrade and a $35 CAD add-on (UNVERIFIED as current) — via agent summary of [CubiCasa help](https://help.cubi.casa/en/articles/3352314-frequently-asked-questions-scanning-and-floor-plans)
- Upload: no. It needs a scan in the CubiCasa app, processed automatically with human QA on room labels. Vendor claims 95–97% accuracy (3–5% error) — [CubiCasa help](https://help.cubi.casa/en/articles/3352314-frequently-asked-questions-scanning-and-floor-plans)
- White label/API: Mobile SDK and Core APIs, "fully white-label solution" — [CubiCasa developers](https://www.cubi.casa/developers/). Featured on Realtor.com and Redfin listings — [pricing](https://www.cubi.casa/pricing/)
- Complaints: invoice increases when floor counts are misread, inaccurate walls or square footage, tedious revisions — [Capterra](https://www.capterra.com/p/193054/CubiCasa/)
- Our advantage: CubiCasa cannot do off-plan, since it needs a built property. We serve developers before construction.

**4. Archilogic** (archilogic.com)
- Pricing: Starter free (5 plans); conversion $329 per floor plan; Plus from $24.90/floor plan/month billed annually (10 plans minimum); Professional $59/floor plan/month billed annually; Enterprise custom — [Archilogic pricing](https://www.archilogic.com/pricing)
- Upload: JPG/PNG/PDF/DXF/DWG, model ready within 2 business days. Conversion is "white-glove" with real people ensuring quality, so it is human-assisted — [Archilogic help](https://help.archilogic.com/knowledge/upload-a-floor-plan); [pricing](https://www.archilogic.com/pricing). Target accuracy is ±5% on raster plans with dimensions — [Archilogic help](https://help.archilogic.com/knowledge/best-practice-for-floor-plans)
- API: REST, GraphQL, webhooks, Floor Plan SDK — [Archilogic developers](https://developers.archilogic.com/). Focus is workplace/facilities, not residential marketing.
- Our advantage: residential marketing outputs (photoreal, video, staging). Archilogic is a spatial-data infrastructure play and a possible supplier or partner.

**5. Planner 5D** (planner5d.com)
- Pricing: Free; Premium $19.99/mo or $59.99/yr; Professional $49.99/mo or $399.99/yr; Enterprise custom — [Planner 5D pricing](https://planner5d.com/pricing)
- Upload: AI recognition turns JPG/PNG/PDF/DWG/DXF and more into an editable 3D project, taking 10 minutes to 24h and sometimes needing manual wall or dimension fixes — [Planner 5D support](https://support.planner5d.com/en/articles/14434484-how-to-upload-a-floor-plan)
- White label: Enterprise/B2B white-label planner. API: JS and REST APIs including AI floor-plan recognition — [Planner 5D B2B](https://tool.planner5d.com/b2b-business); [API overview](https://support.planner5d.com/en/articles/15189751-planner-5d-b2b-api-technical-overview)
- Complaints: auto-renewal, refund difficulty, import/render problems — [Trustpilot](https://www.trustpilot.com/review/planner5d.com)
- Note: the Planner 5D API could be used as a commodity backend by a rival white-label entrant.

**6. Homestyler** (homestyler.com)
- Pricing: Basic free; Pro+ from $6.80/mo; Master+ from $11.80/mo; Team from $19.90/seat/mo; Enterprise custom. Coin-based fees: 4K render 49 coins, video 199–399 coins — [Homestyler pricing](https://www.homestyler.com/pricing)
- Upload: JPG/PNG/WEBP/DWG/DXF/PDF with "Auto Generate (Beta)" walls, doors and windows, or manual tracing — [Homestyler forum](https://www.homestyler.com/forum/view/2092564746527305729)
- White label and API/SDK on Enterprise — [Homestyler business](https://www.homestyler.com/pricing/business)
- Complaints: billing and cancellation friction, browser crashes, coin costs — [Trustpilot](https://www.trustpilot.com/review/homestyler.com)

**7. Coohom** (coohom.com)
- Pricing: no published prices found — [Coohom pricing](https://www.coohom.com/pricing) (UNVERIFIED)
- Upload: CAD/PDF/PNG/JPG with auto-generation of walls, doors and windows. Manual tracing is the fallback — [Coohom help](https://www.coohom.com/helpcenter/how-to-upload-a-cad-floor-plan-from-images-or-pdf)
- White label and OpenAPI explicitly offered — [Coohom OpenAPI](https://open.coohom.com/pub/saas/open-platform/design-building)
- Complaints: random or undeletable walls, save failures, renewal pricing — [Trustpilot](https://www.trustpilot.com/review/coohom.com); [Capterra](https://www.capterra.com/p/192882/Coohom/reviews/)
- Note: Homestyler and Coohom are both reportedly part of the Manycore/Kujiale group (UNVERIFIED in this session). Their white-label APIs are the main "existing software" a cheaper wrapper could sit on.

**8. Cedreo** (cedreo.com)
- Pricing: Free plan with one project. Personal, Pro and Enterprise prices did not appear in the fetched page text (UNVERIFIED). Personal projects include 20 rendering credits — [Cedreo pricing](https://cedreo.com/pricing/)
- Upload: DWG/DXF/PDF/JPG/PNG imported as a reference layer that users trace manually, not converted automatically — [Cedreo help](https://help.cedreo.com/en/how-to-import-a-floor-plan)
- Audience: home builders, remodelers, contractors. API not found.
- Complaints: learning curve, cannot import whole DWG projects, cancellation charges — [Trustpilot](https://www.trustpilot.com/review/www.cedreo.com); [Capterra](https://www.capterra.com/p/177284/Cedreo/)

**9. Floorplanner** (floorplanner.com)
- Pricing: free up to 5 projects. Credit packs: 5 for $8.15 up to 100 for $163. Subscription prices not exposed — [Floorplanner pricing](https://floorplanner.com/pricing)
- Upload: no evidence of auto-conversion. Partners redraw existing plans by hand — [Floorplanner partners](https://floorplanner.com/partners). Enterprise white-label Roomplanner and APIs — [Floorplanner enterprise](https://floorplanner.com/enterprise)

**10. Maket.ai** (maket.ai)
- Pricing: Free (30 credits); Homeowner $20/mo; Pro $100/mo (3,000 credits); Scale custom with API. A floor-plan upload costs 20 credits — [Maket pricing](https://www.maket.ai/pricing)
- Automatic vs human: Homeowner gets one AI-assisted upload that needs review. Pro gets up to 5 "human-validated" uploads per month, described as "100% accurate", within a few hours — [Maket pricing](https://www.maket.ai/pricing)
- Complaints: nonsensical generated layouts, wasted credits, cancellation trouble — [Trustpilot](https://www.trustpilot.com/review/maket.ai)

**11. Matterport (now CoStar)** (matterport.com)
- Pricing (support price list dated 9 Oct 2026): Starter 5 $14/mo (£12); Professional 20 $69/mo (£57); Business 100 $355/mo (£291); Enterprise custom. Pro3 camera $3,995 / £3,195 — [Matterport price list](https://support.matterport.com/s/article/Matterport-Price-List). Prices rose in May 2025, e.g. Starter 5 from $11.99 to $14 — [Matterport](https://support.matterport.com/s/article/Subscription-Plan-Price-Changes). A third-party tracker reports that on 12 Oct 2026 Matterport removed Starter and Business, re-laddered Professional to start at 10 spaces for $90/mo annual ($108 monthly), and added a $1,995 Pro3 bundle (secondary source, UNVERIFIED on matterport.com) — [PricingSaaS](https://pricingsaas.com/companies/matterport/diffs/2026W42)
- Upload: no PDF/CAD-to-3D. It needs a depth scan, and its CAD output is schematic-level — [Matterport CAD](https://support.matterport.com/s/article/Matterport-CAD-File). API/SDK paid on Enterprise — [Developer tools](https://support.matterport.com/s/article/Developer-Tools-Pricing-and-Availability)
- Scale: 14M+ spaces digitised in 177 countries — [CoStar](https://investors.costargroup.com/news-releases/news-release-details/costar-group-completes-acquisition-matterport-ushering-new-era)
- Complaints: expensive hosting, price changes, billing — [Trustpilot](https://www.trustpilot.com/review/matterport.com)
- Our advantage: Matterport is useless for off-plan. It is a capture-of-existing-space business.

**12. Giraffe360** (giraffe360.com). London/Manchester HQ, UK estate-agent stronghold.
- Pricing: UK camera subscription "from £159 p/m", 12-month commitment, 24h turnaround on photos, "fully drawn & measured" floor plans and tours — [Giraffe360 build-your-plan](https://www.giraffe360.com/build-your-plan/). Terms of service commit to processing within 72h and 98% uptime; subscriptions are non-cancellable and auto-renew — [Giraffe360 ToS Feb 2026](https://www.giraffe360.com/https-www-giraffe360-com-terms-of-service-uk-eu-2026-feb/)
- Capability: robotic camera with LiDAR floor plans, HDR photos, tours, video, virtual staging, property website; 50+ ML models — [The Next Web](https://thenextweb.com/news/giraffe360-10m-series-b). API on Content Studio Plus/Camera tiers — [Giraffe360 pricing](https://giraffe360.com/pricing)
- Complaints: Trustpilot 4.7/5 (76 reviews per agent snapshot); billing and cancellation complaints — [Trustpilot](https://www.trustpilot.com/review/www.giraffe360.com); [WeGetAround forum](https://www.wegetaroundnetwork.com/topic/19359/giraffe360-cancellation-and-billing-issues/)
- Our advantage: also capture-only, with no off-plan or CAD input. A potential partner for resale while we own new-build.

**13. Floorfy** (floorfy.com). Spain.
- Pricing: €999 first year (Medium plan plus Ricoh Theta X camera) or from €74/mo with camera rental — [Floorfy](https://floorfy.com/)
- Capability: generates floor plans and 3D tours automatically from 360 photos, with no PDF/CAD upload. REST API for CRMs/portals — [Floorfy docs](https://floorfy-docs.vercel.app/reference/integration)
- Complaints: price, no weekend processing — [Capterra UK](https://www.capterra.co.uk/software/198229/floorfy)

**14. Kuula** (kuula.co)
- 360 tour hosting with manual authoring. Pro replaces branding; Business adds a custom domain, so white label is available. JS player API. Prices did not render (UNVERIFIED) — [Kuula pricing](https://kuula.co/page/pricing); [Kuula Pro](https://kuula.co/page/pro)
- Complaints: small sample (4.4/5, 12 reviews), image quality — [Trustpilot](https://www.trustpilot.com/review/kuula.co)

**15. BoxBrownie** (boxbrownie.com). Human editing service.
- Pricing (USD): virtual staging $30/image; floor plan redraw 2D $30–35, 3D colour $40; external or internal render $350; streetscape $500; large external project $750; development site plans $30–$200 by lot count; 360 staging $60 — [BoxBrownie pricing](https://www.boxbrownie.com/pricing)
- Human redraw from photos, sketches and PDFs — [BoxBrownie commercial floor plans](https://www.boxbrownie.com/commercial-floor-plans)
- Complaints: Trustpilot 4.4 (347 reviews); missed instructions, correction delays — [Trustpilot](https://www.trustpilot.com/review/boxbrownie.com)
- Our advantage: a $350 render benchmark versus near-zero marginal cost, plus instant iteration.

**16. Styldod** (styldod.com). Human redraws.
- 2D from $9/story, 3D colour $24/story (discounted from $39); 3D in 72h — [Styldod floor plan](https://www.styldod.com/floor-plan)

**17. Virtual Staging AI** (virtualstagingai.app)
- $16/mo (6 photos) up to $79/mo (150 photos, API); 10-second turnaround — [VSAI pricing](https://www.virtualstagingai.app/prices). Offers white-label sublicensing — [VSAI whitelabel](https://www.virtualstagingai.app/whitelabel)
- Photos only, no floor-plan-to-3D. Complaints: auto-renewal and refunds (Trustpilot 176 reviews, 15% 1-star per agent snapshot) — [Trustpilot](https://www.trustpilot.com/review/virtualstagingai.app)

**18. Collov AI** (collov.ai)
- $19/mo (60 credits) to $127/mo Enterprise (526 credits, API); Premium adds AI 3D tour and 360 — [Collov pricing](https://www.collov.ai/pricing)
- A Floorplan Visualizer takes JPEG/PNG/PDF and generates a "3D model and virtual tour" — [Collov floorplan](https://collov.ai/floorplan-visualizer). White-label API with no Collov branding — [Collov API](https://collov.ai/API)
- Complaints: altered room layouts, added or erased walls and windows, billing and refunds, chatbot-only support — [Trustpilot UK](https://uk.trustpilot.com/review/collov.ai). This is evidence that its generative output is not geometry-locked.

**19. roOomy** (rooomy.com)
- Human-designed staging: $49–69/photo; Matterport tour staging $434–$1,754 by size — [roOomy order](https://rooomy.com/order/). No plan upload.

**20. REimagineHome** (reimaginehome.ai)
- Credit plans (Essential 30 to Agency 900 credits/mo); prices not exposed — [REimagineHome pricing](https://www.reimaginehome.ai/pricing). Its "chez" photo-to-plan product states measurements are estimates and "not to scale" — [chez terms](https://chez.reimaginehome.ai/terms-of-use)

**21. Interior AI** (interiorai.com)
- Pro $49/mo, Premium $99, Ultra $199. Image formats only — [Interior AI](https://interiorai.com/)
- Trustpilot: 90% 1-star of 10 reviews (cancellation, charges) — [Trustpilot](https://www.trustpilot.com/review/interiorai.com)

**22. Spacely AI** (spacely.ai)
- Top-up 200 credits for $9; other plan prices not exposed. Sketch, model or photo to render — [Spacely pricing](https://www.spacely.ai/pricing). Odd object transformations reported — [The Verge](https://www.theverge.com/24171559/ai-design-app-chatgpt-ikea-spacely-decoratly)

**23. AI architectural renderers (Rendair, MNML.ai, LookX, ArkoAI, Veras)**
- Rendair: floorplan-to-render claims to build walls, rooms and furnishings from AutoCAD, Revit, PDF or image — [Rendair tool](https://rendair.ai/tools/floorplan-to-render). Its own FAQ says the primary engine is visual-based — [Rendair FAQ](https://rendair.ai/faq/what-file-formats-can-i-upload). Prices not rendered on the page — [Rendair pricing](https://rendair.ai/pricing). Trustpilot reports geometry changes and billing issues — [Trustpilot](https://www.trustpilot.com/review/www.rendair.ai)
- MNML.ai: Lite $29, Plus $49, Studio $119/mo. Floor-plan AI keeps "walls as drawn" but outputs images — [MNML pricing](https://mnml.ai/pricing); [MNML floor plan](https://mnml.ai/floor-plan-ai)
- LookX: Individual $20/mo; Team $269/mo for 5 seats; image in, image out — [LookX pricing](https://www.lookx.ai/price.html); [AECHub](https://www.aechub.org/tools/lookx-ai/review)
- Veras (EvolveLAB, now marketed by Chaos): $59/mo or $348/yr; works from BIM models — [Veras pricing](https://www.evolvelab.io/veras/pricing); [Chaos Veras](https://www.chaos.com/veras)
- ArkoAI: SketchUp/Rhino/Revit plugin; prices not exposed — [Arko pricing](https://arko.ai/pricing)

**24. Real-time and offline renderers (pro tools used by studios)**
- Lumion View $229/yr, Pro $1,149/yr, Studio $1,499/yr per floating seat — [Lumion](https://lumion.com/product/buy.html)
- Enscape Solo $47.90/mo billed annually ($574.80/yr) — [Chaos Enscape](https://www.chaos.com/enscape/buy-online)
- Twinmotion: free under $1M revenue, otherwise $445/seat/yr — [Twinmotion licence](https://www.twinmotion.com/license)
- D5 Render: prices not exposed on page (UNVERIFIED) — [D5 pricing](https://www.d5render.com/pricing)
- None of these convert 2D plans automatically. All need a modelled scene and a skilled operator.

**25. Higharc** (higharc.com). US homebuilder design-to-sales platform with BIM, configurable plans and shoppable 3D. Sales-led pricing, no public API — [Higharc](https://www.higharc.com/); [APIs.io](https://apis.io/providers/higharc/)

**26. Esoft** (esoft.com). Outsourced editing back-office for photography companies: AI, hybrid (AI plus human QC) and premium human editing for photos, video, floor plans and 3D. Promo AI editing from $0.20/image. Coconut platform with API (HDPhotoHub, Aryeo, Tonomo) — [Esoft](https://www.esoft.com/)

### Inferences
- Upload → 3D → render pipelines all hide humans somewhere. Getfloorplan uses QA staff. Maket's "100% accurate" tier is human-validated. Archilogic's conversion is white-glove at $329. RoomSketcher, BoxBrownie, Styldod and Floorplanner partners use human illustrators. Self-serve AI conversions (RoomSketcher AI Convert, Planner 5D, Homestyler, Coohom) handle walls, doors and windows only, and their own docs say users must correct results.
- Generative-image tools (Collov, Rendair, Interior AI, Spacely, REimagineHome) produce attractive images but sometimes alter structure. That is a liability under UK consumer law (see Q5).
- The market prices per-unit 3D packages at about $20–$115 (AI/hybrid) and $350–£1,500 per image (human CGI).

### Gaps
- Exact share of human labour inside Getfloorplan's or Collov's pipeline is not disclosed.
- Cedreo, Kuula, D5, Rendair, ArkoAI, Coohom and CubiCasa list prices did not show on fetched pages.
- No independent accuracy benchmarks exist for any plan-to-3D tool.
- I did not profile Zillow 3D Home, Polycam/Metaroom, Vectorworks, Archicad AI or Archidaze/Veovis/Plotplan for lack of time and tool budget.

## Q2. What do UK off-plan developers use for sales suites and CGI, and what do they charge?

### Takeaway
UK housebuilders buy CGI from a long tail of studios at roughly £250–£2,000 per still, £3,500–£12,000 for an animation and £1,200–£4,000+ for a 360 tour. Interactive sales suites (siteplans, apartment finders, configurators, Unreal walkthroughs) come from specialist agencies, usually priced per development and quoted on request. I found published price lists only from smaller studios. Tier-1 London studios (Hayes Davidson, Picture Plane, Forbes Massie, Uniform, Virtual Planet etc.) do not publish prices.

### Cited Findings
- Property CGI Ltd: external renders from £625/image, internal from £550; 2–4 weeks; 2 revision rounds — [Property CGI Ltd](https://www.propertycgiltd.com/cgi)
- Joanna James: new-build CGI about £500+VAT for a single view, about £450 each for up to 10 views, about £250 each for 10+. A 17-view example came to £4,750+VAT (average £280); 7–15 days — [Joanna James](https://joanna-james.com/cgi-visualisations/new-build-cgi-visuals/)
- VisuArchitect: planning CGI from £395/image (£650 for 1 view), £250/image if the client supplies a clean RVT/SKP/IFC model — [VisuArchitect](https://www.visuarchitect.com/service/planning-applications/). Its 2025 guide gives extension exterior stills £450–£900, a commercial 3–5 view package £2,500–£6,000, verified views £1,800–£4,500 per view and a 30–60s flythrough £3,500–£12,000 — [VisuArchitect guide](https://www.visuarchitect.com/questions/3d-architectural-visualization/how-much-does-3d-visualisation-cost/)
- Hyrez: exterior housetype from £750, exterior apartment from £1,000, interior CGI with full design scheme from £1,500, whole-development animation from £5,000; interactive Unreal showcases and "Digisuite" POA — [Hyrez](https://hyrez.uk/services)
- CGIs Newcastle (June 2026): exterior from £450+VAT, interior from £400, 3D floor plans from £125/floor, 360 tour £1,200–£4,000+ — [CGIs Newcastle](https://www.cgisnewcastle.co.uk/post/how-much-does-a-property-cgi-cost-2026-guide)
- Shakworks (London): exterior from £350, interior from £450, 30s animation from £3,500, aerial from £1,500 — [Shakworks](https://www.shakworks.com/architectural-visualisation-services)
- Blockout Digital: planning render £350–£600, marketing launch package £3,000–£8,000, interactive walkthroughs from about £3,000 — [Blockout Digital](https://www.blockoutdigital.com/guides/how-much-does-architectural-cgi-cost)
- Sales-suite technology vendors (UK):
  - Marmoset: sales app across kiosk, tablet, web and phone from one CMS; "Marmoset Pro" real-time 3D with time-of-day lighting and apartment finders; live availability from CMS/CRM — [Marmoset](https://marmoset.digital/what-we-do)
  - EyeSiteView: interactive siteplans, virtual showhomes, housetype configurators, flythroughs. Castle Green Homes case study: 700+ potential buyers and a 41.7% uplift in options and extras after configurators (vendor claim) — [EyeSiteView](https://eyesiteview.co.uk/interactive-property-cgi/); [case study](https://eyesiteview.co.uk/case-studies/home-buyer-engagement-off-plan/)
  - White Crow Studios CROWSEYE/NEST: per-development pricing, "no monthly fees", CMS for availability, built from the studio's own CGI — [White Crow](https://www.whitecrowstudios.co.uk/services/interactive-experiences)
  - ShowReal360 (The Lines Group): Unreal-style real-time development with configurator, time of day, cloud streaming, Rightmove integration — [ShowReal360](https://www.showreal360.com/); [Lines Group](https://www.linesgroup.co.uk/showreal360)
  - Offplan.studio: home/apartment finder from existing CGIs, own branding, embeddable — [Offplan Studio](https://offplan.studio/)
  - Dot UX: Antler Homes and Mulberry Homes interactive marketing suites (2024) — [Dot UX](https://www.dotux.co.uk/works/antler-homes-interactive-marketing-suite)
  - Visually Sonic "Synth Space": modular CGI, plot selector, configurator and multilingual AI buyer guide — [Visually Sonic](https://www.visuallysonic.com/synth-space)

### Inferences
- A typical UK mid-size development (10–20 CGIs, a 360 tour, an animation and an interactive siteplan) likely costs £10k–£40k+ from studios, based on summing the cited bands. This is an estimate, not a sourced figure.
- Studios bundle CGI with interactive tools and lock in the client ("built from your existing CGI assets"). Our wedge is a self-serve, per-plot, per-month model with assets generated from the architect's plans/BIM.

### Gaps
- No published pricing from Hayes Davidson, Picture Plane, Forbes Massie, Uniform, Virtual Planet, Visualisation One, Darcy Jones, Vaxxu or Tag. I could not verify which large UK developers use which studio. Property Week, EG and Estate Agent Today were not searched within budget.

## Q3. Is anyone offering white-label buyer configurators for developers, and at what price?

### Takeaway
Yes. A growing set of SaaS sales platforms publish prices, mostly US/EU/Middle East: ProPlan Studio, IdealTwin, Realitiq, realtySTUDIO, IMMERSIV, Aareas and ASRR Alpha. In the UK, configurators are mainly agency-built per development (EyeSiteView, ShowReal360, Marmoset). Self-serve, plan-in, white-label developer configurators with published UK pricing appear thin.

### Cited Findings
- ProPlan Studio (US builders): 3D configurator $499/mo (or $416 annual); AI Render Studio $150/mo (250 credits); interactive site maps $499/mo; traditional renders $500/mo (10 renders); $1,000 per-model setup; one-line embed with custom domain and branding. The team builds the 3D model ("AI accelerates our production"). It quotes freelance configurator builds at $15k–$50k and studio renders at $800–$2,000 per image — [ProPlan Studio](https://www.proplanstudio.com/); [configurator](https://www.proplanstudio.com/products/configurator)
- IdealTwin: per-unit SaaS. Pro $2/unit/month (15 units minimum), Scale $4/unit/month, Enterprise (500+ units) with white-label and CRM; Unreal Engine plugin; configurator and quotation in Business tier — [IdealTwin](https://www.idealtwin.com/pricing)
- Realitiq (DACH): digital twins from DWG/DXF/IFC at €600/unit (1–20 units), €500 (21–50), €400 (51+), plus €2,000 setup; white-label with own colours and logo; AI renderings for buyers €27 per 100 — [Realitiq](https://www.realitiq.com/en/prices-for-projects/). This is the closest analogue to the proposed product (CAD/BIM in, white label, per unit).
- realtySTUDIO: Essential launch $12,500 (1 building, 100 units, 48h); Professional $29,500; Enterprise $59,500+ with API; platform fees from $499/mo; multilingual with RTL (Gulf focus) — [realtySTUDIO](https://realty.studio/for/developers)
- IMMERSIV (Brisbane): off-plan 3D platform syncing CRM and live stock. REA Group made a follow-on investment in July 2025 (about 20% holding per filings) — [Business News Australia](https://www.businessnewsaustralia.com/articles/rea-group-lifts-stake-in-3d-architectural-visualisation-tool-startup-immersiv.html)
- Aareas Interactive: cloud 3D home configurator with rules engine and API to ERP/CRM; pricing not published — [Aareas](https://aareas.com/home-configurator/)
- ASRR Alpha (NL): BIM-validated buyer configurator; buyer portal +€10/home/month — [ASRR](https://asrr.nl/alpha/construction)
- Tiny Easy: custom-priced configurator subscription plus setup — [Tiny Easy](https://www.tinyeasy.com/configurator-pricing)
- Yuniyo: white-label buyer-to-resident portal, setup fee plus per-unit monthly — [Yuniyo](https://yuniyo.com/products/developer-suite)
- EvaCore: Saudi-focused developer platform, quote-only; notes AI processing currently leaves the Kingdom — [EvaCore](https://evacore.io/en/products/developer-platform)

### Inferences
- Price anchors exist: about €400–600 per unit (Realitiq), $2–4 per unit per month (IdealTwin), and $499–$799/mo plus $1,000/model (ProPlan). A UK entrant could anchor at about £300–£600 per plot type plus a platform fee (inference).
- Most of these still use human 3D production. Automation of the plan-to-model step is the real differentiator if it can be achieved.
- Data residency matters for Gulf buyers (the EvaCore note).

### Gaps
- Spatial Dimension, Esoft "Exactly", Glimpse, PureWeb, Ultra Realty and Virtuoso were not verified within budget. Whether any of them sells a UK self-serve developer configurator remains open.

## Q4. Funding, acquisitions and market moves, 2024–2026

### Takeaway
Portals are buying 3D capture: CoStar bought Matterport and REA Group bought iGUIDE and invested in IMMERSIV. Hardware-plus-AI capture players keep raising (Giraffe360 Series B, March 2026). Floorfy is consolidating in Southern Europe. Matterport is raising prices after the acquisition.

### Cited Findings
- CoStar completed its Matterport acquisition on 28 Feb 2025: $2.75 cash plus 0.03552 CoStar shares per Matterport share — [CoStar 8-K](https://www.sec.gov/Archives/edgar/data/1057352/000119312525042465/d899523d8k.htm). The deal is reported as $1.6B — [Inman](https://www.inman.com/2025/02/28/costar-closes-1-6b-matterport-acquisition-ahead-of-schedule/); [HousingWire](https://www.housingwire.com/articles/costar-closes-purchase-of-matterport/). A later Inman piece says $1.8B, which conflicts — [Inman Oct 2025](https://www.inman.com/2025/10/28/realtor-com-parent-goes-after-its-own-virtual-tour-target-amid-battle-with-costar/)
- Matterport subscription prices rose in May 2025 — [Matterport](https://support.matterport.com/s/article/Subscription-Plan-Price-Changes). A further plan restructure was reported in Oct 2026 (secondary) — [PricingSaaS](https://pricingsaas.com/companies/matterport/diffs/2026W42)
- REA Group agreed on 2 Oct 2025 to acquire 61.5% of Planitar (iGUIDE), whose tours featured on 25% of Canadian homes sold in 2025 — [BusinessWire](https://www.businesswire.com/news/home/20251002905299/en/REA-Group-to-Acquire-Leading-3D-Tour-and-Interactive-Floor-Plan-Technology-iGUIDE)
- REA Group raised its IMMERSIV stake in July 2025, after an initial investment in Oct 2024 — [Business News Australia](https://www.businessnewsaustralia.com/articles/rea-group-lifts-stake-in-3d-architectural-visualisation-tool-startup-immersiv.html)
- Giraffe360 raised a $10M Series B led by Cipio Partners on 26 Mar 2026. Total disclosed equity is about $32M (Series A $16M led by Founders Fund, Nov 2022). It has 200+ staff and is in the Sunday Times 100 Tech — [Cipio](https://www.cipiopartners.com/news/2026-03-26-cipio-partners-invests-in-giraffe360-as-lead-investor-in-usd-10-million-series-b-round); [TNW](https://thenextweb.com/news/giraffe360-10m-series-b). Property Wire reports the round as £7.5M and about 1,000 property brands — [Property Wire](https://www.propertywire.com/company-news/giraffe360-secures-7-5m-series-b-funding-round/)
- Floorfy acquired Realisti.co (Italy) in Sept 2025. It was profitable in 2024, has 8,000+ agents and launched Gyro hardware and generative AI home staging — [PropTech Connect](https://proptechconnect.com/floorfy-expands-into-italy-with-the-acquisition-of-realisti-co/)
- Three Space Lab raised a $3M seed (Aug 2025) for VR off-plan luxury real estate, targeting Miami, St Tropez and Dubai — [PR Newswire](https://www.prnewswire.com/news-releases/three-space-lab-secures-3m-seed-round-to-revolutionize-luxury-real-estate-with-ai-and-vr-302533046.html)
- Peek (virtual tours) secured $5M in May 2025; Pupil (London) is listed as acquired — [Tracxn](https://tracxn.com/d/companies/virtual-staging/__Wd3CDYJekgcKCSfc0i8TJR7tjuc1WDFon41USlZVkAs)
- Veras is now marketed under Chaos, which owns Enscape — [Chaos Veras](https://www.chaos.com/veras) (acquisition date UNVERIFIED)

### Inferences
- Portal owners (CoStar/Homes.com, REA/Realtor.com) are vertically integrating 3D. Rightmove or Zoopla could follow in the UK, which makes portal partnership or exit a plausible path, and also a competitive threat.

### Gaps
- I did not verify Esoft funding or M&A, virtual-staging consolidations (e.g. BoxBrownie), Getfloorplan funding, CubiCasa ownership changes, or Rightmove/Zoopla 3D moves.

## Q5. Is the concept differentiated or a cheaper interface on existing software? Why would customers switch?

### Takeaway
Plan-to-3D, AI renders and white-label tours each exist as commodities, and Planner 5D, Coohom, Homestyler and Collov even offer white-label APIs. A thin wrapper would not be defensible. Defensible differentiation would combine four things: (1) geometry-true models from CAD/BIM/PDF, with measurements that survive into renders (an anti-"housefishing" stance); (2) development-level, multi-plot projects with a live-availability sales app and configurator; (3) UK developer and agent white-labelling plus integrations (Reapit/Alto/Rightmove); (4) self-serve speed at a fraction of studio cost. Customers would switch for cost and turnaround against studios (£350–£1,500/image, weeks), and for trust and compliance against generative staging tools.

### Cited Findings
- UK regulation: since the Property Misdescriptions Act was repealed, listings fall under the Digital Markets, Competition and Consumers Act 2024. National Trading Standards considers misleading AI edits to contravene it; penalties include fines, bans and imprisonment — [AOL/Observer July 2026](https://www.aol.co.uk/articles/rapid-rise-housefishing-ai-enhanced-090025000.html)
- UK case: a Winkworth branch took down AI-enhanced images after a buyer complained that a chimney breast had been removed in the imagery — [AOL](https://www.aol.co.uk/articles/rapid-rise-housefishing-ai-enhanced-090025000.html)
- Consumer backlash: r/RealEstate "The AI staging has to stop" thread, with complaints that "the scale is almost always wrong" and buyers who swipe left. A Coraly study found about 11% of roughly 40,000 primary listing photos in early 2026 showed signs of alteration — [BAM Oct 2026](https://nowbam.com/has-ai-staging-gone-too-far-heres-what-buyers-are-saying/). An r/realtors agent said AI added square footage and a buyer refused to offer — [Newsweek](https://www.newsweek.com/realtor-looks-at-home-photos-what-they-notice-infuriates-11733147). US MLS fines are reportedly about $2,500 for misrepresentation (anecdotal Reddit claim) — [Newsweek](https://www.newsweek.com/realtor-looks-at-home-photos-what-they-notice-infuriates-11733147)
- Generative tools altering structure: Collov reviews report added or erased walls and windows — [Trustpilot UK](https://uk.trustpilot.com/review/collov.ai). Rendair reviews report geometry changes — [Trustpilot](https://www.trustpilot.com/review/www.rendair.ai). REimagineHome chez says outputs are "not to scale" — [chez terms](https://chez.reimaginehome.ai/terms-of-use)
- Existing white-label APIs a rival could wrap: Planner 5D — [API](https://support.planner5d.com/en/articles/15189751-planner-5d-b2b-api-technical-overview); Coohom — [OpenAPI](https://open.coohom.com/pub/saas/open-platform/design-building); Homestyler — [business](https://www.homestyler.com/pricing/business); Collov — [API](https://collov.ai/API); Virtual Staging AI — [whitelabel](https://www.virtualstagingai.app/whitelabel); CubiCasa — [developers](https://www.cubi.casa/developers/)
- Studio cost and time benchmarks: £350–£1,500 per image, 2–4 weeks — [Property CGI Ltd](https://www.propertycgiltd.com/cgi); [Hyrez](https://hyrez.uk/services); [Shakworks](https://www.shakworks.com/architectural-visualisation-services). Configurator builds $15k–$50k (vendor claim) — [ProPlan Studio](https://www.proplanstudio.com/)
- Clean BIM input already cuts studio prices, e.g. £250 vs £395+ per image — [VisuArchitect](https://www.visuarchitect.com/service/planning-applications/). That supports ingesting BIM/IFC as a cost lever.

### Inferences
- Competitor gaps we could own:
  - Capture-based players (Matterport, Giraffe360, CubiCasa, Floorfy, iGUIDE) cannot do off-plan.
  - Plan-upload consumer tools (Planner 5D, RoomSketcher, Homestyler) are unit-level, have consumer aesthetics and lack development or sales-suite features.
  - Getfloorplan is a per-order service with limited editing and a human QA bottleneck.
  - Studios are slow and expensive, and lock clients in.
  - Configurator SaaS (Realitiq, IdealTwin, ProPlan) mostly rely on human modelling and are not UK-focused.
- Biggest risks:
  - Getfloorplan or Collov adding developer portals.
  - Realitiq or IdealTwin entering the UK.
  - Portals (Rightmove/Zoopla) bundling 3D.
  - Studios adopting AI (White Crow already says CROWSEYE is "powered by AI") — [White Crow](https://www.whitecrowstudios.co.uk/services/interactive-experiences)
- Switching triggers: per-plot cost and speed for SME housebuilders that cannot afford studio packages; agents and agencies wanting unlimited branded assets; trust and compliance messaging ("measured, not hallucinated") under DMCC 2024.
- UAE/Saudi: off-plan markets favour multilingual/RTL platforms (realtySTUDIO, EvaCore), and data residency is a selling point. In the US, MLS rules and portal-owned 3D (CoStar/Matterport) dominate. In the EU, Floorfy (Iberia/Italy) and Realitiq (DACH) are regional incumbents.

### Gaps
- No quantitative data on how UK developers decide between studios and SaaS. No UK-specific survey on configurator adoption.
- I did not check Reapit/Alto marketplace listings for 3D or floor-plan apps.
- No customer-count figures were verified for most vendors.
