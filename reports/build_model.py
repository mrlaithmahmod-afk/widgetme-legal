#!/usr/bin/env python3
"""Build the 36-month financial model for the AI property visualisation SaaS.
All outputs are live Excel formulas driven by the Assumptions sheet."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.worksheet.properties import PageSetupProperties

OUT = "/home/user/widgetme-legal/reports/Property_Visualisation_Financial_Model.xlsx"

BLUE = Font(name="Arial", size=10, color="0000FF")
BLACK = Font(name="Arial", size=10, color="000000")
GREEN = Font(name="Arial", size=10, color="008000")
BOLD = Font(name="Arial", size=10, bold=True)
H1 = Font(name="Arial", size=14, bold=True)
H2 = Font(name="Arial", size=11, bold=True, color="FFFFFF")
HFILL = PatternFill("solid", fgColor="1F3864")
SFILL = PatternFill("solid", fgColor="D9E1F2")
YFILL = PatternFill("solid", fgColor="FFFF00")
KFILL = PatternFill("solid", fgColor="FFF2CC")
WRAP = Alignment(wrap_text=True, vertical="top")
GBP0 = '£#,##0;(£#,##0);"-"'
GBP2 = '£#,##0.00;(£#,##0.00);"-"'
USD2 = '$#,##0.00;($#,##0.00);"-"'
USD0 = '$#,##0;($#,##0);"-"'
PCT = '0.0%;(0.0%);"-"'
NUM1 = '#,##0.0;(#,##0.0);"-"'
NUM2 = '#,##0.00;(#,##0.00);"-"'
NUM0 = '#,##0;(#,##0);"-"'

wb = Workbook()

SRC = {
    "claude": "https://platform.claude.com/docs/en/about-claude/pricing",
    "gemini": "https://ai.google.dev/gemini-api/docs/pricing",
    "kling": "https://kling.ai/document-api/pricing/base/video.md",
    "runpod": "https://www.runpod.io/pricing",
    "aws_g6e": "https://instances.vantage.sh/aws/ec2/g6e.xlarge",
    "gamelift": "https://aws.amazon.com/gamelift/streams/pricing/",
    "vagon": "https://vagon.io/streams/pricing",
    "r2": "https://developers.cloudflare.com/r2/pricing/",
    "bunny": "https://bunny.net/pricing/",
    "flex": "https://www.autodesk.com/buying/flex",
    "aps": "https://aps.autodesk.com/blog/aps-business-model-evolution",
    "upwork": "https://www.upwork.com/hire/architectural-rendering-freelancers/cost/",
    "stripe": "https://stripe.com/gb/pricing",
    "workos": "https://workos.com/pricing",
    "vercel": "https://vercel.com/pricing",
    "xrates": "https://www.x-rates.com/average/?from=USD&to=GBP&amount=1&year=2026",
    "oda": "https://www.opendesign.com/pricing.md",
    "saascap": "https://www.saas-capital.com/research/saas-retention-benchmarks-for-private-b2b-companies/",
    "iconiq": "https://saastr.com/whats-truly-great-now-in-b2b-ai-per-iconiq-115-growth-at-100m-55-gross-margins-and-655k-in-revenue-per-employee",
    "aleph": "https://www.getaleph.com/answers/cac-payback-period-saas-2026",
    "salesmind": "https://sales-mind.ai/blog/post/kpi-benchmarks-saas-sales-teams-2025",
    "henderson": "https://www.hendersonscott.co.uk/media/11zjl0na/hs-technology-salary-guide-2026.pdf",
    "pyralink": "https://pyralink.co.uk/insights/2026-05-26-iso-27001-cost-uk-certification/",
    "hightable": "https://hightable.io/iso-27001-3-year-cost-cycle-guide",
    "barbour": "https://barbour-abi.com/construction-leads/get-10-free-leads/",
    "reapitkb": "https://wppropertyfeed.co.uk/knowledge-base/category/feeds",
    "proplan": "https://www.proplanstudio.com/",
    "realitiq": "https://www.realitiq.com/en/prices-for-projects/",
    "idealtwin": "https://www.idealtwin.com/pricing",
    "getfloorplan": "https://getfloorplan.com/pricing",
    "metropix": "https://www.landmark.co.uk/products/metropix/pricing/",
    "rightmove": "https://www.londonstockexchange.com/news-article/RMV/annual-financial-report/17479517",
    "blockout": "https://www.blockoutdigital.com/guides/how-much-does-architectural-cgi-cost",
    "planner5d": "https://tool.planner5d.com/b2b-floor-plan-recognition",
    "booth": "https://boothexhibits.com/?p=19816",
}

# =====================================================================
# Assumptions sheet
# =====================================================================
A = wb.active
A.title = "Assumptions"
A["A1"] = "Assumptions — all model inputs (blue = editable input; black = formula)"
A["A1"].font = H1
A["A2"] = ("Columns C/D/E: for unit-cost inputs = Low / Base / High cost case; for growth inputs = Bear / Base / Bull scenario. "
           "Single-value inputs sit in column D. Labels: VERIFIED = quoted from a vendor/primary page in the research notes; "
           "ESTIMATE = researcher estimate built from cited prices; ASSUMPTION = modeller's judgement where the notes have no figure.")
A["A2"].alignment = WRAP
A.merge_cells("A2:G2")
A.row_dimensions[2].height = 45
for c, w in zip("ABCDEFG", [52, 16, 13, 13, 13, 13, 95]):
    A.column_dimensions[c].width = w

REF = {}       # key -> row
MULTI = {}     # key -> bool (has low/high)
row = [4]


def hdr(title, cols=("Parameter", "Unit", "Low / Bear", "Base", "High / Bull", "Label", "Source / reasoning")):
    r = row[0]
    A.cell(r, 1, title).font = H2
    for i in range(1, 8):
        A.cell(r, i).fill = HFILL
    r += 1
    for i, c in enumerate(cols, 1):
        cell = A.cell(r, i, c)
        cell.font = BOLD
        cell.fill = SFILL
    row[0] = r + 1


def add(key, name, unit, low, base, high, label, source, fmt=None):
    r = row[0]
    A.cell(r, 1, name).font = BLACK
    A.cell(r, 2, unit).font = BLACK
    multi = low is not None
    for col, v in ((3, low), (4, base), (5, high)):
        if v is None:
            continue
        cell = A.cell(r, col, v)
        cell.font = BLUE if not (isinstance(v, str) and v.startswith("=")) else BLACK
        if fmt:
            cell.number_format = fmt
    A.cell(r, 6, label).font = BOLD if label == "ASSUMPTION" else BLACK
    if label == "ASSUMPTION":
        A.cell(r, 6).fill = KFILL
    A.cell(r, 7, source).font = BLACK
    A.cell(r, 7).alignment = Alignment(wrap_text=False)
    REF[key] = r
    MULTI[key] = multi
    row[0] = r + 1


def blank():
    row[0] += 1


def a(key, case=None):
    """absolute reference to Assumptions value. case: 1/2/3 => C/D/E, or column letter."""
    r = REF[key]
    if case is None or not MULTI[key]:
        return f"Assumptions!$D${r}"
    col = {1: "C", 2: "D", 3: "E"}.get(case, case)
    return f"Assumptions!${col}${r}"


# ---- General
hdr("1. General")
add("fx", "FX rate: GBP per 1 USD", "£ per $", None, 0.755, None, "VERIFIED",
    "X-Rates Oct-2026 monthly average 0.755183 (20 days) — " + SRC["xrates"], "0.000")
add("start_cash", "Starting cash (founder-funded)", "£", None, 50000, None, "ASSUMPTION",
    "Brief example: £50k founder-funded. No external funding modelled.", GBP0)
add("months", "Model horizon", "months", None, 36, None, "ASSUMPTION", "36 monthly periods; month 1 = first month of company operation (pre-launch build included)")
blank()

# ---- Unit costs
hdr("2. Unit-cost component prices (USD unless stated) — Low / Base / High cost case")
add("llm_parse", "LLM floor-plan parse (one high-res plan, structured JSON)", "$ / plan", 0.026, 0.052, 0.10, "ESTIMATE",
    "pricing_inputs §1: Sonnet 5.5 ≈ $0.052; Batch ≈ $0.026; Opus 5.5 ≈ $0.10 — " + SRC["claude"], USD2)
add("llm_orch", "LLM orchestration + vision QA per generated image", "$ / image", 0.02, 0.03, 0.05, "ESTIMATE",
    "pricing_inputs §1: $0.02–0.05 per room image on Sonnet 5.5 — " + SRC["claude"], USD2)
add("llm_video", "LLM shot planning / prompting per video", "$ / video", 0.05, 0.10, 0.20, "ASSUMPTION",
    "Not in notes; scaled from per-image orchestration cost (a video = ~6 shots).", USD2)
add("img_price", "Image generation per attempt (4K photoreal)", "$ / attempt", 0.113, 0.24, 0.24, "VERIFIED",
    "Gemini Nano Banana 2.1 4K $0.113 (low); Nano Banana Pro 4K $0.24 (base/high) — " + SRC["gemini"], USD2)
add("img_attempts", "Generation attempts per accepted image", "x", 2, 3, 4, "ESTIMATE",
    "pricing_inputs §12: 3 attempts per accepted 4K image (gap: replace with pilot data)")
add("std_video_price", "Standard walkthrough video generation", "$ / second", 0.07, 0.12, 0.168, "VERIFIED",
    "Kling 2.6 1080p $0.07/s; Veo 3.1 Fast 1080p $0.12/s; Kling 3.0 with audio 1080p $0.168/s — " + SRC["gemini"] + " ; " + SRC["kling"], USD2)
add("cine_video_price", "Cinematic video generation", "$ / second", 0.12, 0.40, 0.60, "VERIFIED",
    "Veo 3.1 Fast $0.12/s (low); Veo 3.1 Std 1080p $0.40/s (base); Veo Std 4K $0.60/s (high) — " + SRC["gemini"], USD2)
add("video_retake", "Video retake multiplier (seconds billed / seconds delivered)", "x", 1.5, 2, 3, "ESTIMATE",
    "pricing_inputs §12: 2x retakes assumed; range is modeller's")
add("std_sec", "Length of standard walkthrough video", "seconds", None, 30, None, "ASSUMPTION", "Deliverable definition (30s walkthrough)")
add("cine_sec", "Length of cinematic video", "seconds", None, 60, None, "ASSUMPTION", "Deliverable definition (60s cinematic)")
add("gpu_price", "GPU rental for scene build / base render (Blender headless)", "$ / GPU-hour", 0.59, 1.09, 1.86, "VERIFIED",
    "RunPod L4 $0.59/h; RunPod L40S $1.09/h; AWS g6e.xlarge L40S $1.861/h — " + SRC["runpod"] + " ; " + SRC["aws_g6e"], USD2)
add("gpu_mult", "GPU-hours multiplier vs base quantities", "x", 0.5, 1, 2, "ESTIMATE",
    "pricing_inputs §5: 4K Cycles still 2–10 min on RTX 4090; scene build ~1h L40S. Modelling/asset setup can dominate.")
add("stream_h", "Interactive viewer: pixel-streaming hours per hosted property per month", "hours", 0, 2, 6.65, "ESTIMATE",
    "pricing_inputs §6: 100 sessions x 8 min = 13.3 h if fully pixel-streamed; high = 50% of sessions streamed (6.65 h). Low = WebGL/three.js only (≈$0). Base = WebGL default + occasional streaming (ASSUMPTION).")
add("stream_price", "Pixel-streaming capacity price", "$ / user-hour", 1.82, 1.82, 2.82, "VERIFIED",
    "AWS GameLift Streams gen6n_ultra L4 $1.82/h; Vagon L4 Pro G3 $2.82/h — " + SRC["gamelift"] + " ; " + SRC["vagon"], USD2)
add("store_price", "Object storage (Cloudflare R2 Standard)", "$ / GB-month", None, 0.015, None, "VERIFIED", SRC["r2"], "0.000")
add("retention", "Storage retention charged per deliverable", "months", None, 12, None, "ASSUMPTION", "Assets kept 12 months in hot storage")
add("cdn_price", "CDN delivery (Bunny)", "$ / GB", 0.005, 0.01, 0.01, "VERIFIED", "Bunny $0.01/GB EU/NA; $0.005 volume network — " + SRC["bunny"], "0.000")
add("host_cdn_gb", "CDN GB per hosted interactive property per month", "GB", None, 10, None, "ESTIMATE",
    "~100 WebGL sessions x ~100 MB (modeller's estimate based on pricing_inputs §6 session count)")
add("aps_fee", "CAD translation fee (Autodesk APS Flex) per DWG/RVT file", "$ / file", 0, 1.5, 3, "ESTIMATE",
    "pricing_inputs §8: budget $1.50–$3/file (UNVERIFIED after Dec-2025 APS price change); low = IFC/DXF via open-source parsers — " + SRC["flex"])
add("aps_share", "Share of plans needing paid CAD translation", "%", None, 0.30, None, "ASSUMPTION",
    "Most inputs are PDF/raster or IFC/DXF (free parsers); ODA SDK licence covers DWG in-house", PCT)
add("qa_rate", "Human QA / 2D-confirm operator rate (fully loaded)", "$ / hour", 15, 25, 35, "ESTIMATE",
    "pricing_inputs §11: offshore $15–25/h (Upwork median $20–30/h; 3D artists $25–40/h); high = $35/h — " + SRC["upwork"], USD2)
add("confirm_min", "Human 2D vector/scale confirm-edit per plan", "minutes / plan", 3, 10, 15, "ESTIMATE",
    "technical_feasibility §7: target 3–5 min clean CAD, 10–15 min scans; pricing_inputs §11: 10–20 min per plan. Mandatory HITL step for raster input — " + SRC["planner5d"])
add("img_qa_min", "Human review per delivered image attempt", "minutes / image", 0.5, 1, 1.5, "ASSUMPTION",
    "Not measured in notes. Automated drift QA + human spot-check of every customer-facing image (DMCC 2024 misdescription risk).")
add("vid_qa_min", "Human review per video attempt", "minutes / video", 5, 10, 15, "ASSUMPTION", "Watch-through + shot check; not in notes")
add("unit_qa_min", "Human check per development unit (finish swaps / availability data)", "minutes / unit", 1, 1.5, 2.5, "ASSUMPTION", "Not in notes")
add("support_rate", "Customer support handling rate (allocated to COGS)", "$ / hour", 25, 30, 35, "ASSUMPTION",
    "UK part-time/outsourced support; no UK support salary in notes (gtm_benchmarks gaps)", USD2)
add("support_mult", "Support minutes multiplier vs base quantities", "x", 0.5, 1, 1.5, "ASSUMPTION", "Tickets, revision requests, re-uploads")
add("fail_rate", "Deliverable-level QA rejection / redo rate used for COGS", "%", 0.05, 0.15, 0.25, "ASSUMPTION",
    "On top of per-image attempts. Applied as cost per success = fixed + repeatable/(1-f). Replace with pilot data.", PCT)
add("fail_t1", "Failure-table rate 1", "%", None, 0.05, None, "ASSUMPTION", "Retry/failure sensitivity table", PCT)
add("fail_t2", "Failure-table rate 2", "%", None, 0.15, None, "ASSUMPTION", "Retry/failure sensitivity table", PCT)
add("fail_t3", "Failure-table rate 3", "%", None, 0.30, None, "ASSUMPTION", "Retry/failure sensitivity table", PCT)
add("fail_t4", "Failure-table rate 4", "%", None, 0.50, None, "ASSUMPTION", "Retry/failure sensitivity table", PCT)
add("hostq_storage", "Storage per hosted interactive property", "GB", None, 2, None, "ESTIMATE", "pricing_inputs §7: ~2 GB source scenes per property")
blank()

# ---- Development definitions
hdr("3. Development deliverable definitions")
add("d50_types", "50-unit development: distinct plan (house) types", "types", None, 6, None, "ESTIMATE", "pricing_inputs §12 example: 6 floor-plan types")
add("d50_units", "50-unit development: units", "units", None, 50, None, "ESTIMATE", "pricing_inputs §12")
add("d200_types", "200-unit development: distinct plan types", "types", None, 15, None, "ESTIMATE", "pricing_inputs §12 example: 15 types (repeated plan types)")
add("d200_units", "200-unit development: units", "units", None, 200, None, "ESTIMATE", "pricing_inputs §12")
add("unit_imgs", "Images per unit (1 plan render + 2 finish swaps)", "images / unit", None, 3, None, "ESTIMATE", "pricing_inputs §12: 50 x (1 plan render + 2 finish swaps)")
add("site_qa", "Site-plan / availability setup QA per development", "minutes", None, 60, None, "ASSUMPTION", "Not in notes")
add("site_gpu", "Site-plan / aerial GPU hours per development", "GPU-hours", None, 2, None, "ASSUMPTION", "Not in notes")
add("credits_unit", "Credits charged per development unit", "credits / unit", None, 3, None, "ASSUMPTION", "Credit design choice")
blank()

# ---- Deliverable quantity matrix
DELIV = ["Single room image", "5 room images", "2-bed flat (8 images + plan)", "4-bed house (19 images, 2 floors)",
         "Interactive 3D property (WebGL tour, 1st month hosting)", "30s walkthrough video", "60s cinematic video",
         "Developer marketing package (per house type)", "50-unit development (6 plan types)", "200-unit development (15 plan types)"]
QF = ["plans", "images", "std_videos", "cine_videos", "gpu_h", "interactive", "storage_gb", "cdn_gb", "units", "extra_qa", "support_min", "credits"]
QF_LABEL = ["Plans (2D confirm)", "Accepted images", "30s videos", "60s videos", "GPU-hours", "Interactive props", "Storage GB",
            "CDN GB", "Dev units", "Extra QA min", "Support min", "Credits charged"]
r = row[0]
A.cell(r, 1, "4. Deliverable quantity drivers (base quantities; cost case changes prices/minutes, not quantities)").font = H2
for i in range(1, 14):
    A.cell(r, i).fill = HFILL
r += 1
A.cell(r, 1, "Deliverable").font = BOLD
A.cell(r, 1).fill = SFILL
for j, lab in enumerate(QF_LABEL):
    c = A.cell(r, 2 + j, lab)
    c.font = BOLD
    c.fill = SFILL
    c.alignment = WRAP
A.row_dimensions[r].height = 30
r += 1
QBASE = [
    [1, 1, 0, 0, 0.05, 0, 0.1, 0.5, 0, 0, 2, 5],
    [1, 5, 0, 0, 0.2, 0, 0.5, 2, 0, 2, 3, 10],
    [1, 8, 0, 0, 0.5, 0, 1, 5, 0, 5, 5, 15],
    [2, 19, 0, 0, 1.0, 0, 2, 10, 0, 10, 8, 32],
    [1, 0, 0, 0, 1.0, 1, 2, 10, 0, 15, 10, 20],
    [1, 0, 1, 0, 0.5, 0, 0.5, 5, 0, 0, 5, 20],
    [1, 0, 0, 1, 1.0, 0, 1, 10, 0, 0, 8, 60],
    [2, 22, 1, 1, 2.0, 1, 3, 20, 0, 30, 30, 160],
]
QROW = {}
for i, d in enumerate(DELIV):
    A.cell(r, 1, d).font = BLACK
    QROW[i] = r
    for j, f in enumerate(QF):
        col = 2 + j
        if i < 8:
            v = QBASE[i][j]
            c = A.cell(r, col, v)
            c.font = BLUE
        else:
            tkey, ukey = ("d50_types", "d50_units") if i == 8 else ("d200_types", "d200_units")
            pkg = f"{CL(col)}${QROW[7]}"
            T, U = a(tkey), a(ukey)
            if f == "plans":
                fm = f"={T}*{pkg}"
            elif f == "images":
                fm = f"={T}*{pkg}+{U}*{a('unit_imgs')}"
            elif f in ("std_videos", "cine_videos", "interactive"):
                fm = f"={T}*{pkg}"
            elif f == "gpu_h":
                fm = f"={T}*{pkg}+{a('site_gpu')}"
            elif f == "storage_gb":
                fm = f"={T}*{pkg}+{U}*0.1"
            elif f == "cdn_gb":
                fm = f"={T}*{pkg}+{U}*1"
            elif f == "units":
                fm = f"={U}"
            elif f == "extra_qa":
                fm = f"={T}*{pkg}+{a('site_qa')}"
            elif f == "support_min":
                fm = "=120" if i == 8 else "=240"
            elif f == "credits":
                fm = f"={T}*{pkg}+{U}*{a('credits_unit')}"
            c = A.cell(r, col, fm)
            c.font = BLACK
        c.number_format = NUM2 if f == "gpu_h" else '#,##0.0;(#,##0.0);"-"'
    r += 1
A.cell(r, 1, ("Rows 1–8 quantities: ESTIMATE from pricing_inputs §12 (image counts per flat/house/package) and §5–7 (GPU, storage, CDN); "
              "support minutes and credits are ASSUMPTIONS. Rows 9–10 are formulas: plan types x house-type package + units x per-unit images "
              "(cost scales with plan types, not units). Development support minutes (120/240) are ASSUMPTIONS.")).alignment = WRAP
A.merge_cells(start_row=r, start_column=1, end_row=r, end_column=13)
A.row_dimensions[r].height = 42
row[0] = r + 2
for col in range(8, 14):
    if A.column_dimensions[CL(col)].width is None or A.column_dimensions[CL(col)].width < 12:
        A.column_dimensions[CL(col)].width = 12


def q(i, f):
    return f"Assumptions!${CL(2 + QF.index(f))}${QROW[i]}"


# ---- Pricing inputs
TIERS = ["Studio", "Agency", "DevPro", "Ent"]
TNAME = {"Studio": "Studio", "Agency": "Agency", "DevPro": "Developer Pro", "Ent": "Enterprise"}
hdr("5. Pricing inputs (recommended structure; prices are hypotheses — none observed for this product)")
add("price_Studio", "Studio list price", "£ / month", None, 149, None, "ASSUMPTION",
    "Brief hypothesis. Anchors: Metropix £44.90–£59.75/office/mo; agent WTP £50–£150/branch/mo (market_segments Q4) — " + SRC["metropix"], GBP0)
add("price_Agency", "Agency list price (white-label viewer)", "£ / month", None, 499, None, "ASSUMPTION",
    "Brief hypothesis. Anchors: prime agents £400–£1,000/office/mo; marketing agencies £3k–£10k/yr seats (market_segments Q4/Q6)", GBP0)
add("price_DevPro", "Developer Pro list price (1 live development hosted)", "£ / month", None, 1499, None, "ASSUMPTION",
    "Brief hypothesis. Anchors: developers £5k–£25k/scheme/yr; Rightmove New Homes £2,135/dev/mo; ProPlan configurator $499/mo — " + SRC["rightmove"], GBP0)
add("price_Ent", "Enterprise price used in model (range £3k–£10k+)", "£ / month", None, 5000, None, "ASSUMPTION",
    "Brief range £3k–£10k+. Nationals WTP £50k–£250k/yr enterprise licence (market_segments Q4 [HYP])", GBP0)
add("price_Ent_lo", "Enterprise hypothesis — low point", "£ / month", None, 3000, None, "ASSUMPTION", "Brief range", GBP0)
add("price_Ent_hi", "Enterprise hypothesis — high point", "£ / month", None, 10000, None, "ASSUMPTION", "Brief range", GBP0)
add("over_Studio", "Studio overage price", "£ / credit", None, 4.00, None, "ASSUMPTION", "Set above included-credit value to protect margin", GBP2)
add("over_Agency", "Agency overage price", "£ / credit", None, 3.50, None, "ASSUMPTION", "", GBP2)
add("over_DevPro", "Developer Pro overage price", "£ / credit", None, 3.00, None, "ASSUMPTION", "", GBP2)
add("over_Ent", "Enterprise overage price", "£ / credit", None, 2.50, None, "ASSUMPTION", "", GBP2)
add("setup_Studio", "Studio setup fee", "£ one-off", None, 0, None, "ASSUMPTION", "Self-serve", GBP0)
add("setup_Agency", "Agency setup fee (white-label branding)", "£ one-off", None, 500, None, "ASSUMPTION", "", GBP0)
add("setup_DevPro", "Developer Pro setup fee", "£ one-off", None, 1500, None, "ASSUMPTION",
    "Anchors: ProPlan $1,000 per-model setup; Realitiq €2,000 setup — " + SRC["proplan"] + " ; " + SRC["realitiq"], GBP0)
add("setup_Ent", "Enterprise setup / integration fee", "£ one-off", None, 7500, None, "ASSUMPTION", "realtySTUDIO launch packages $12.5k–$59.5k (competitors Q3)", GBP0)
add("per_type_fee", "Per-development fee: price per plan (house) type, additional developments", "£ / plan type", None, 350, None, "ASSUMPTION",
    "competitors Q3 inference: UK entrant could anchor £300–£600 per plot type + platform fee; Realitiq €400–600/unit", GBP0)
add("hosted_Studio", "Studio: hosted interactive properties (avg)", "properties", None, 1, None, "ASSUMPTION", "")
add("hosted_Agency", "Agency: hosted interactive properties (avg)", "properties", None, 5, None, "ASSUMPTION", "")
add("hosted_DevPro", "Developer Pro: hosted interactive properties / plots (avg)", "properties", None, 15, None, "ASSUMPTION", "")
add("hosted_Ent", "Enterprise: hosted interactive properties / plots (avg)", "properties", None, 50, None, "ASSUMPTION", "")
add("sso_Studio", "Studio: SSO connections", "connections", None, 0, None, "ASSUMPTION", "")
add("sso_Agency", "Agency: SSO connections", "connections", None, 0, None, "ASSUMPTION", "")
add("sso_DevPro", "Developer Pro: SSO connections", "connections", None, 0, None, "ASSUMPTION", "")
add("sso_Ent", "Enterprise: SSO connections", "connections", None, 1, None, "ASSUMPTION", "Enterprise requires SAML SSO (legal_compliance: procurement norms UNVERIFIED)")
add("sso_price", "WorkOS SSO price per connection (1–15)", "$ / month", None, 125, None, "VERIFIED", SRC["workos"], USD0)
add("paypct_Studio", "Studio payment fees (% of billing)", "%", None, 0.022, None, "VERIFIED",
    "Stripe UK card 1.5% + Billing 0.7% — " + SRC["stripe"], PCT)
add("paypct_Agency", "Agency payment fees (% of billing)", "%", None, 0.022, None, "VERIFIED", "Stripe UK card 1.5% + Billing 0.7%", PCT)
add("paypct_DevPro", "Developer Pro payment fees (% of billing)", "%", None, 0.011, None, "VERIFIED",
    "Invoice 0.4% + Billing 0.7% + Bacs (capped £4, below) — " + SRC["stripe"], PCT)
add("paypct_Ent", "Enterprise payment fees (% of billing)", "%", None, 0.011, None, "VERIFIED", "Invoice 0.4% + Billing 0.7% + Bacs cap £4", PCT)
add("payfix_Studio", "Studio payment fixed fee", "£ / invoice", None, 0.20, None, "VERIFIED", "Stripe 20p per card transaction", GBP2)
add("payfix_Agency", "Agency payment fixed fee", "£ / invoice", None, 0.20, None, "VERIFIED", "Stripe 20p", GBP2)
add("payfix_DevPro", "Developer Pro payment fixed fee", "£ / invoice", None, 4.00, None, "VERIFIED", "Bacs Direct Debit 1% capped at £4", GBP2)
add("payfix_Ent", "Enterprise payment fixed fee", "£ / invoice", None, 4.00, None, "VERIFIED", "Bacs cap £4", GBP2)
add("onb_Studio", "Studio onboarding labour", "hours / new customer", None, 0.5, None, "ASSUMPTION", "")
add("onb_Agency", "Agency onboarding labour (branding, integration)", "hours / new customer", None, 3, None, "ASSUMPTION", "")
add("onb_DevPro", "Developer Pro onboarding labour", "hours / new customer", None, 8, None, "ASSUMPTION", "")
add("onb_Ent", "Enterprise onboarding labour (security review, SSO, integration)", "hours / new customer", None, 30, None, "ASSUMPTION", "")
add("onb_rate", "Onboarding labour rate (UK)", "£ / hour", None, 35, None, "ASSUMPTION", "UK CS/solutions rate incl. on-costs; no UK CSM salary in notes", GBP0)
blank()

# ---- Tier usage mix
r = row[0]
A.cell(r, 1, "6. Included usage per tier (deliverables per month at 100% of allowance) — allowance credits are derived from this mix").font = H2
for i in range(1, 12):
    A.cell(r, i).fill = HFILL
r += 1
A.cell(r, 1, "Tier").font = BOLD
A.cell(r, 1).fill = SFILL
SHORT = ["1 image", "5 rooms", "2-bed flat", "4-bed house", "Interactive 3D", "30s video", "60s cine", "Dev package", "50-unit dev", "200-unit dev"]
for j, s in enumerate(SHORT):
    c = A.cell(r, 2 + j, s)
    c.font = BOLD
    c.fill = SFILL
r += 1
MIX = {
    "Studio": [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    "Agency": [0, 2, 4, 2, 1, 2, 0, 0, 0, 0],
    "DevPro": [0, 0, 0, 2, 3, 0, 0, 2, 0, 0],
    "Ent": [0, 0, 0, 2, 6, 2, 1, 3, 1, 0],
}
MIXROW = {}
for t in TIERS:
    A.cell(r, 1, TNAME[t]).font = BLACK
    for j, v in enumerate(MIX[t]):
        c = A.cell(r, 2 + j, v)
        c.font = BLUE
    MIXROW[t] = r
    r += 1
A.cell(r, 1, ("ASSUMPTION: typical monthly deliverable mix per tier (Studio = small agent/designer; Agency = multi-listing agent or "
              "marketing agency; Developer Pro = SME developer with 1 live scheme; Enterprise = national/off-plan seller with a "
              "50-unit launch per month). Allowance credits = SUMPRODUCT(mix, credits per deliverable).")).alignment = WRAP
A.merge_cells(start_row=r, start_column=1, end_row=r, end_column=11)
A.row_dimensions[r].height = 42
row[0] = r + 2


def mix(t, j):
    return f"Assumptions!${CL(2 + j)}${MIXROW[t]}"


# ---- Scenario growth inputs
hdr("7. Scenario inputs — Bear / Base / Bull (columns C / D / E)")
add("cost_case", "Unit-cost case used (1 = Low, 2 = Base, 3 = High)", "index", 3, 2, 2, "ASSUMPTION",
    "Conservative: Bull still uses Base costs; Bear uses High (pessimistic-but-plausible) costs")
LAUNCH = {"Studio": (9, 6, 4), "Agency": (10, 7, 5), "DevPro": (12, 9, 6), "Ent": (18, 12, 10)}
INIT = {"Studio": (0.8, 1.5, 2.5), "Agency": (0.2, 0.3, 0.5), "DevPro": (0.1, 0.2, 0.3), "Ent": (0.05, 0.08, 0.12)}
RAMP = {"Studio": (0.12, 0.25, 0.45), "Agency": (0.04, 0.08, 0.13), "DevPro": (0.015, 0.03, 0.05), "Ent": (0.004, 0.008, 0.012)}
CAP = {"Studio": (5, 9, 15), "Agency": (2, 3.5, 5.5), "DevPro": (0.6, 1.2, 2.0), "Ent": (0.15, 0.3, 0.5)}
CHURN = {"Studio": (0.045, 0.035, 0.025), "Agency": (0.035, 0.025, 0.02), "DevPro": (0.015, 0.01, 0.0075), "Ent": (0.01, 0.006, 0.004)}
EXP = {"Studio": (0.001, 0.002, 0.004), "Agency": (0.003, 0.005, 0.008), "DevPro": (0.004, 0.008, 0.012), "Ent": (0.005, 0.01, 0.015)}
REAL = {"Studio": (0.85, 0.90, 0.95), "Agency": (0.80, 0.85, 0.90), "DevPro": (0.85, 0.90, 0.95), "Ent": (0.70, 1.00, 1.10)}
for t in TIERS:
    add(f"launch_{t}", f"{TNAME[t]}: first month new customers can sign", "month", *LAUNCH[t], "ASSUMPTION",
        "Base: build months 1–5 (6–15 eng-months of work per technical_feasibility §8). Enterprise: no wins before month 9+; "
        "enterprise cycle ~180 days (" + SRC["salesmind"] + "); nationals 6–18 months (market_segments Q6)" if t == "Ent" else
        "Pre-launch build + paid pilots; agent self-serve first; developer cycles 1–3 months (market_segments Q6)")
for t in TIERS:
    add(f"init_{t}", f"{TNAME[t]}: new customers in launch month", "customers / month", *INIT[t], "ASSUMPTION",
        "Founder-led outbound: ~8–12 meetings per 1,000 contacts (gtm_benchmarks outbound [ASSUMPTION]); fractional customers = expected value", NUM2)
for t in TIERS:
    add(f"ramp_{t}", f"{TNAME[t]}: monthly increase in new-customer rate", "customers / month per month", *RAMP[t], "ASSUMPTION",
        "Linear ramp from launch; capped below", "0.000")
for t in TIERS:
    add(f"cap_{t}", f"{TNAME[t]}: cap on founder/marketing-driven new customers", "customers / month", *CAP[t], "ASSUMPTION",
        "Cap keeps base case near SOM ≈ £1.25m ARR by yr3 (market_segments Q7) or below", NUM2)
add("ae_up_DevPro", "Extra Developer Pro wins per productive AE", "customers / month", 0.15, 0.3, 0.4, "ASSUMPTION",
    "No UK win-rate benchmarks found (gtm_benchmarks gaps)", NUM2)
add("ae_up_Ent", "Extra Enterprise wins per productive AE", "customers / month", 0.02, 0.05, 0.08, "ASSUMPTION", "Long cycles; tiny universe (~25 nationals)", "0.000")
add("ae_lag", "AE ramp time before productive", "months", 4, 3, 3, "ASSUMPTION", "Sales cycle 75–180 days (" + SRC["salesmind"] + ")")
for t in TIERS:
    add(f"churn_{t}", f"{TNAME[t]}: monthly logo churn", "% / month", *CHURN[t], "ESTIMATE" if t in ("Studio", "Agency") else "ESTIMATE",
        ("gtm_benchmarks: SMB agents 2.5–3.5%/mo; Studio skewed higher (smallest, most price-sensitive)" if t in ("Studio", "Agency") else
         "SaaS Capital 2025: median GRR ~91% (<$250k ACV) => ~0.8%/mo; 95% (>$250k) => ~0.4%/mo; developers project-based (scheme ends) — " + SRC["saascap"]), PCT)
for t in TIERS:
    add(f"exp_{t}", f"{TNAME[t]}: monthly expansion on retained MRR", "% / month", *EXP[t], "ESTIMATE",
        "Sized so NRR ≈ 95–102% base (SaaS Capital median NRR 102% at $25–50k ACV; gtm_benchmarks [ASSUMPTION] 95–102%)", PCT)
for t in TIERS:
    add(f"real_{t}", f"{TNAME[t]}: realised price as % of list (discounts, annual prepay, resellers)", "%", *REAL[t], "ASSUMPTION",
        "Reseller discounts 20–30% and referral 10–20% (gtm_benchmarks [ASSUMPTION], unverified); Enterprise realised = £3.5k/£5k/£5.5k" if t == "Ent" else
        "Reseller discounts 20–30% on a share of deals (gtm_benchmarks [ASSUMPTION])", PCT)
add("util", "Average utilisation of included credits", "%", 0.75, 0.65, 0.60, "ASSUMPTION", "Higher utilisation = more COGS (Bear)", PCT)
add("over_pct", "Overage credits as % of included credits (portfolio average)", "%", 0.02, 0.05, 0.08, "ASSUMPTION", "", PCT)
add("setup_collect", "Share of list setup fees actually collected", "%", 0.5, 0.75, 1.0, "ASSUMPTION", "Setup fees commonly discounted/waived to close", PCT)
add("devs_year", "Additional developments per Developer Pro customer per year", "developments / yr", 0.5, 1.0, 1.5, "ASSUMPTION",
    "SME developers run 1–5 live sites (market_segments Q6)", NUM2)
add("iso_start", "Month ISO 27001 programme starts", "month", 15, 10, 8, "ASSUMPTION", "Needed before enterprise procurement (UNVERIFIED norm, legal_compliance Q3)")
blank()

# ---- Opex inputs
hdr("8. Operating cost inputs (single value, all scenarios)")
add("founder_sal", "Founder salary (below market until MRR trigger)", "£ / year", None, 30000, None, "ASSUMPTION", "Survival salary; uplift is a hire-table step", GBP0)
add("oncost", "Employer on-costs (NIC + pension + benefits)", "% of salary", None, 0.20, None, "ESTIMATE", "gtm_benchmarks: ~15% employer NIC + 3–5% pension ≈ 18–22%", PCT)
add("contract_eng", "Contract engineering budget until Engineer #1 is hired", "£ / month", None, 2000, None, "ASSUMPTION",
    "Senior contractors £400–£600/day (Henderson Scott 2026) => ~4 days/month — " + SRC["henderson"], GBP0)
add("mkt_fixed", "Digital marketing programmes", "£ / month", None, 1000, None, "ASSUMPTION", "Content, ads, outbound tooling", GBP0)
add("events", "Events (delegate passes, fringe sponsorship)", "£ / year", None, 15000, None, "ESTIMATE",
    "gtm_benchmarks: realistic yr-1 events £15k–£40k; small UK stand ~£9.7k — " + SRC["booth"], GBP0)
add("reapit", "Reapit developer network membership", "£ / year", None, 1500, None, "ESTIMATE", "Reported '£1500+ per annum' (secondhand) — " + SRC["reapitkb"], GBP0)
add("barbour", "Developer pipeline data (Barbour ABI) from Developer Pro launch", "£ / year", None, 4000, None, "VERIFIED", "Subscriptions start ~£4k — " + SRC["barbour"], GBP0)
add("mkt_var", "Variable marketing", "% of revenue", None, 0.05, None, "ASSUMPTION", "", PCT)
add("commission", "Sales commission on new Developer Pro + Enterprise first-year ACV (once an AE exists)", "%", None, 0.10, None, "ASSUMPTION", "No UK AE comp data in notes", PCT)
add("sw_base", "Software & tools (base)", "£ / month", None, 400, None, "ASSUMPTION", "Vercel Pro $20/seat, Clerk/WorkOS AuthKit free tier, Sentry etc. — " + SRC["vercel"], GBP0)
add("sw_head", "Software & tools per head", "£ / head / month", None, 40, None, "ASSUMPTION", "", GBP0)
add("infra_base", "Platform infrastructure (always-on services, DB, queues)", "£ / month", None, 300, None, "ASSUMPTION", "Small fixed costs $0–$100/mo each (pricing_inputs §9 gaps)", GBP0)
add("infra_cust", "Platform infrastructure per customer", "£ / customer / month", None, 1.5, None, "ASSUMPTION", "", GBP2)
add("oda_init", "ODA Drawings SDK — Sustaining membership (SaaS use), first year", "$", None, 7500, None, "VERIFIED", "technical_feasibility §4 (reconfirm) — " + SRC["oda"], USD0)
add("oda_renew", "ODA Sustaining renewal", "$ / year", None, 4500, None, "VERIFIED", SRC["oda"], USD0)
add("oda_start", "Month ODA licence purchased (DWG support goes live)", "month", None, 8, None, "ASSUMPTION", "Before Developer Pro launch; DXF/IFC via free parsers before that")
add("iso_y1", "ISO 27001 year-1 programme (consultant + compliance platform + Stage 1/2 audit)", "£", None, 20000, None, "ESTIMATE",
    "gtm_benchmarks: £12k–£25k first year (Pyralink); auditor £4k–£8k — " + SRC["pyralink"], GBP0)
add("iso_ongoing", "ISO 27001 ongoing (surveillance audits + platform)", "£ / year", None, 10000, None, "ESTIMATE",
    "gtm_benchmarks: ~£8k–£12k/yr after (surveillance 30–40% of initial fee) — " + SRC["hightable"], GBP0)
add("insurance", "Insurance: cyber + PI/tech E&O + public liability", "£ / year", None, 4000, None, "ESTIMATE", "gtm_benchmarks [ESTIMATE] £2k–£6k/yr; get broker quotes", GBP0)
add("legal_m", "Legal, accounting, admin", "£ / month", None, 400, None, "ASSUMPTION", "Not researched (gtm_benchmarks gaps)", GBP0)
add("legal_once", "One-off legal set-up (T&Cs, DPA, AI-output disclaimers) in month 1", "£", None, 5000, None, "ASSUMPTION",
    "legal_compliance flags solicitor review of DMCC 2024 / UK GDPR terms", GBP0)
add("founder_hours", "Founder working hours per month", "hours", None, 180, None, "ASSUMPTION", "~42 h/week", NUM0)
add("founder_ops", "Share of founder time available for delivery ops (2D confirm, QA, support, onboarding)", "%", None, 0.35, None, "ASSUMPTION",
    "Remainder goes to product/engineering (6–15 eng-months of build), sales and admin. Basis of solo-founder capacity estimate.", PCT)
blank()

# ---- Hiring step functions
r = row[0]
A.cell(r, 1, "9. Hiring plan — step functions (role hired in the month AFTER the trigger is first met; never un-hired)").font = H2
for i in range(1, 8):
    A.cell(r, i).fill = HFILL
r += 1
for i, c in enumerate(["Role", "Trigger metric", "Threshold", "Salary £/yr", "Recruit fee %", "Label", "Reasoning / source"], 1):
    A.cell(r, i, c).font = BOLD
    A.cell(r, i).fill = SFILL
r += 1
HIRES = [
    ("Customer support / QA lead #1", "Customers", 20, 32000, 0.0, "ASSUMPTION", "Founder ops capacity (see Summary) is exhausted around this customer count"),
    ("Senior engineer #1", "MRR", 15000, 85000, 0.15, "VERIFIED", "UK senior £70k–£100k base (Henderson Scott 2026) — " + SRC["henderson"]),
    ("Account executive #1 (developers)", "MRR", 25000, 60000, 0.15, "ASSUMPTION", "No UK AE salary in notes; OTE commission modelled separately"),
    ("Founder salary uplift to market", "MRR", 50000, 30000, 0.0, "ASSUMPTION", "Founder moves from £30k to £60k"),
    ("Senior engineer #2", "MRR", 50000, 85000, 0.15, "VERIFIED", "Henderson Scott 2026"),
    ("Customer success #2", "Customers", 150, 35000, 0.0, "ASSUMPTION", ""),
    ("Marketing manager", "MRR", 60000, 50000, 0.15, "ASSUMPTION", ""),
    ("Account executive #2", "MRR", 80000, 60000, 0.15, "ASSUMPTION", ""),
    ("Graphics / 3D engineer #3", "MRR", 120000, 90000, 0.15, "ESTIMATE", "Graphics premium on £70k–£100k senior band (gaps: no sourced premium)"),
    ("Customer success #3", "Customers", 300, 35000, 0.0, "ASSUMPTION", ""),
]
HROW = []
AE_IDX = [2, 7]
ENG1_IDX = 1
FOUNDER_UP_IDX = 3
for h in HIRES:
    for i, v in enumerate(h, 1):
        c = A.cell(r, i, v)
        c.font = BLUE if i in (2, 3, 4, 5) else BLACK
        if i == 3:
            c.number_format = '#,##0'
        if i == 4:
            c.number_format = GBP0
        if i == 5:
            c.number_format = PCT
    if h[5] == "ASSUMPTION":
        A.cell(r, 6).fill = KFILL
        A.cell(r, 6).font = BOLD
    HROW.append(r)
    r += 1
A.cell(r, 1, "Trigger metric must be 'Customers' (total paying customers) or 'MRR' (subscription MRR, £). Evaluated on the previous month's value to avoid circularity.").alignment = WRAP
A.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
row[0] = r + 2

A.freeze_panes = "A4"

# =====================================================================
# Unit_Costs sheet
# =====================================================================
U = wb.create_sheet("Unit_Costs")
U["A1"] = "Unit costs — cost per SUCCESSFUL deliverable, built from components (USD unless stated)"
U["A1"].font = H1
U["A2"] = ("Repeatable components (LLM, image gen, video gen, GPU, output-review QA) are re-incurred when a deliverable is rejected; "
           "fixed components (2D confirm, hosting, storage, CDN, CAD fees, support) are incurred once. "
           "Cost per success = fixed + repeatable / (1 − failure rate). Human labour (2D confirm + QA + support) is shown explicitly.")
U["A2"].alignment = WRAP
U.merge_cells("A2:S2")
U.row_dimensions[2].height = 32
U.column_dimensions["A"].width = 50
for i in range(2, 21):
    U.column_dimensions[CL(i)].width = 12.5

UC_COLS = ["LLM tokens", "Image gen", "Video gen", "GPU render", "3D streaming (1st mo)", "Storage", "CDN", "3rd-party fees (CAD)",
           "Human 2D confirm", "Human output QA", "Support alloc.", "Attempt cost (USD)", "of which repeatable",
           "Failure rate", "Cost / success (USD)", "Cost / success (GBP)", "Human labour share", "Human minutes / success"]
UCROW = {}   # (case, i) -> row
ur = 4
CASES = {1: "LOW", 2: "BASE", 3: "HIGH"}
for case in (1, 2, 3):
    U.cell(ur, 1, f"{CASES[case]} cost case").font = H2
    for i in range(1, 20):
        U.cell(ur, i).fill = HFILL
    ur += 1
    U.cell(ur, 1, "Deliverable").font = BOLD
    U.cell(ur, 1).fill = SFILL
    for j, c in enumerate(UC_COLS):
        cell = U.cell(ur, 2 + j, c)
        cell.font = BOLD
        cell.fill = SFILL
        cell.alignment = WRAP
    U.row_dimensions[ur].height = 30
    ur += 1
    for i, d in enumerate(DELIV):
        U.cell(ur, 1, d).font = BLACK
        x = lambda k: a(k, case)
        f = {}
        f["B"] = f"={q(i,'plans')}*{x('llm_parse')}+{q(i,'images')}*{x('llm_orch')}+({q(i,'std_videos')}+{q(i,'cine_videos')})*{x('llm_video')}"
        f["C"] = f"={q(i,'images')}*{x('img_attempts')}*{x('img_price')}"
        f["D"] = (f"=({q(i,'std_videos')}*{a('std_sec')}*{x('std_video_price')}+{q(i,'cine_videos')}*{a('cine_sec')}*{x('cine_video_price')})"
                  f"*{x('video_retake')}")
        f["E"] = f"={q(i,'gpu_h')}*{x('gpu_mult')}*{x('gpu_price')}"
        f["F"] = f"={q(i,'interactive')}*{x('stream_h')}*{x('stream_price')}"
        f["G"] = f"={q(i,'storage_gb')}*{a('store_price')}*{a('retention')}"
        f["H"] = f"={q(i,'cdn_gb')}*{x('cdn_price')}"
        f["I"] = f"={q(i,'plans')}*{a('aps_share')}*{x('aps_fee')}"
        f["J"] = f"={q(i,'plans')}*{x('confirm_min')}/60*{x('qa_rate')}"
        f["K"] = (f"=({q(i,'images')}*{x('img_qa_min')}+({q(i,'std_videos')}+{q(i,'cine_videos')})*{x('vid_qa_min')}"
                  f"+{q(i,'units')}*{x('unit_qa_min')}+{q(i,'extra_qa')})/60*{x('qa_rate')}")
        f["L"] = f"={q(i,'support_min')}*{x('support_mult')}/60*{x('support_rate')}"
        f["M"] = f"=SUM(B{ur}:L{ur})"
        f["N"] = f"=B{ur}+C{ur}+D{ur}+E{ur}+K{ur}"
        f["O"] = f"={x('fail_rate')}"
        f["P"] = f"=(M{ur}-N{ur})+N{ur}/(1-O{ur})"
        f["Q"] = f"=P{ur}*{a('fx')}"
        f["R"] = f"=IF(P{ur}=0,0,(J{ur}+K{ur}/(1-O{ur})+L{ur})/P{ur})"
        f["S"] = (f"={q(i,'plans')}*{x('confirm_min')}+({q(i,'images')}*{x('img_qa_min')}+({q(i,'std_videos')}+{q(i,'cine_videos')})*{x('vid_qa_min')}"
                  f"+{q(i,'units')}*{x('unit_qa_min')}+{q(i,'extra_qa')})/(1-O{ur})+{q(i,'support_min')}*{x('support_mult')}")
        for col, fm in f.items():
            c = U[f"{col}{ur}"]
            c.value = fm
            c.font = GREEN if col == "O" else BLACK
            c.number_format = {"O": PCT, "R": PCT, "S": NUM1, "Q": GBP2}.get(col, USD2)
        UCROW[(case, i)] = ur
        ur += 1
    # ongoing hosting per property-month
    U.cell(ur, 1, "Ongoing hosting per interactive property per month (streaming + CDN + storage)").font = BOLD
    U[f"M{ur}"] = (f"={a('stream_h', case)}*{a('stream_price', case)}+{a('host_cdn_gb')}*{a('cdn_price', case)}"
                   f"+{a('hostq_storage')}*{a('store_price')}")
    U[f"M{ur}"].number_format = USD2
    U[f"Q{ur}"] = f"=M{ur}*{a('fx')}"
    U[f"Q{ur}"].number_format = GBP2
    UCROW[(case, "host")] = ur
    ur += 2

# Summary table Low/Base/High USD + GBP
U.cell(ur, 1, "Cost per successful deliverable — summary").font = H2
for i in range(1, 9):
    U.cell(ur, i).fill = HFILL
ur += 1
for j, c in enumerate(["Deliverable", "Low (USD)", "Base (USD)", "High (USD)", "Low (GBP)", "Base (GBP)", "High (GBP)", "Base human labour share"]):
    U.cell(ur, 1 + j, c).font = BOLD
    U.cell(ur, 1 + j).fill = SFILL
    U.cell(ur, 1 + j).alignment = WRAP
ur += 1
SUMROW = {}
for i, d in enumerate(DELIV):
    U.cell(ur, 1, d)
    for k, case in enumerate((1, 2, 3)):
        U.cell(ur, 2 + k, f"=P{UCROW[(case, i)]}").number_format = USD2
        U.cell(ur, 5 + k, f"=Q{UCROW[(case, i)]}").number_format = GBP2
    U.cell(ur, 8, f"=R{UCROW[(2, i)]}").number_format = PCT
    SUMROW[i] = ur
    ur += 1
U.cell(ur, 1, "Ongoing hosting per interactive property-month")
for k, case in enumerate((1, 2, 3)):
    U.cell(ur, 2 + k, f"=M{UCROW[(case, 'host')]}").number_format = USD2
    U.cell(ur, 5 + k, f"=Q{UCROW[(case, 'host')]}").number_format = GBP2
SUMROW["host"] = ur
ur += 2

# Failure table
U.cell(ur, 1, "Retry / failure sensitivity — BASE cost case: cost per success at deliverable-level rejection rates (QA on rejects included)").font = H2
for i in range(1, 10):
    U.cell(ur, i).fill = HFILL
ur += 1
U.cell(ur, 1, "Deliverable").font = BOLD
U.cell(ur, 1).fill = SFILL
fk = ["fail_t1", "fail_t2", "fail_t3", "fail_t4"]
for k, key in enumerate(fk):
    c = U.cell(ur, 2 + k, f'="USD @ "&TEXT({a(key)},"0%")')
    c.font = BOLD
    c.fill = SFILL
    c2 = U.cell(ur, 6 + k, f'="GBP @ "&TEXT({a(key)},"0%")')
    c2.font = BOLD
    c2.fill = SFILL
ur += 1
FAILROW = {}
for i, d in enumerate(DELIV):
    br = UCROW[(2, i)]
    U.cell(ur, 1, d)
    for k, key in enumerate(fk):
        U.cell(ur, 2 + k, f"=(M{br}-N{br})+N{br}/(1-{a(key)})").number_format = USD2
        U.cell(ur, 6 + k, f"={CL(2+k)}{ur}*{a('fx')}").number_format = GBP2
    FAILROW[i] = ur
    ur += 1
U.cell(ur, 1, ("Note: the base case already assumes 3 generation attempts per accepted image and 2x video retakes; this table adds "
               "deliverable-level rejection (whole set redone after QA/customer rejection). Rejected attempts re-incur generation AND "
               "human output-review minutes; 2D confirm, storage and support are not repeated.")).alignment = WRAP
U.merge_cells(start_row=ur, start_column=1, end_row=ur, end_column=9)
U.row_dimensions[ur].height = 45
U.freeze_panes = "B4"

# =====================================================================
# Pricing sheet
# =====================================================================
P = wb.create_sheet("Pricing")
P["A1"] = "Pricing — tiers, allowances, overages, setup & per-development fees; gross margin at included usage"
P["A1"].font = H1
P.column_dimensions["A"].width = 58
for i in range(2, 12):
    P.column_dimensions[CL(i)].width = 15
pr = 3
P.cell(pr, 1, "A. Recommended structure: subscription + included credits + overage + setup fee + per-development fee").font = H2
for i in range(1, 6):
    P.cell(pr, i).fill = HFILL
pr += 1
for j, t in enumerate(["Metric"] + [TNAME[t] for t in TIERS]):
    P.cell(pr, 1 + j, t).font = BOLD
    P.cell(pr, 1 + j).fill = SFILL
pr += 1
PR = {}


def prow(key, label, fn, fmt, bold=False):
    global pr
    P.cell(pr, 1, label).font = BOLD if bold else BLACK
    for j, t in enumerate(TIERS):
        c = P.cell(pr, 2 + j, fn(t, j))
        c.number_format = fmt
        c.font = GREEN if str(fn(t, j)).startswith("=Assumptions") else BLACK
    PR[key] = pr
    pr += 1


def col_of(j):
    return CL(2 + j)


prow("price", "List price (£ / month)", lambda t, j: f"={a('price_'+t)}", GBP0, True)
prow("credits", "Included credits / month (= tier usage mix)",
     lambda t, j: "=" + "+".join(f"{mix(t,k)}*{q(k,'credits')}" for k in range(10)), NUM0)
prow("ppc", "Effective price per included credit (£)", lambda t, j: f"=IF({col_of(j)}{PR['credits']}=0,0,{col_of(j)}{PR['price']}/{col_of(j)}{PR['credits']})", GBP2)
prow("over", "Overage price (£ / credit)", lambda t, j: f"={a('over_'+t)}", GBP2)
prow("setup", "Setup fee (£ one-off)", lambda t, j: f"={a('setup_'+t)}", GBP0)
prow("devfee", "Per-development fee, extra developments (£ per plan type; Developer Pro/Enterprise)",
     lambda t, j: f"={a('per_type_fee')}" if t in ("DevPro", "Ent") else 0, GBP0)
prow("hosted", "Hosted interactive properties included", lambda t, j: f"={a('hosted_'+t)}", NUM0)
prow("sso", "SSO connections included", lambda t, j: f"={a('sso_'+t)}", NUM0)
pr += 1
for case in (1, 2, 3):
    P.cell(pr, 1, f"{CASES[case]} cost case").font = BOLD
    P.cell(pr, 1).fill = SFILL
    pr += 1
    prow(f"usage{case}", "  Cost of included usage at 100% (£ / month)",
         lambda t, j, c=case: "=" + "+".join(f"{mix(t,k)}*Unit_Costs!$Q${UCROW[(c,k)]}" for k in range(10)), GBP0)
    prow(f"fixed{case}", "  Per-account fixed cost: hosting + SSO (£ / month)",
         lambda t, j, c=case: f"={a('hosted_'+t)}*Unit_Costs!$Q${UCROW[(c,'host')]}+{a('sso_'+t)}*{a('sso_price')}*{a('fx')}", GBP0)
    prow(f"pay{case}", "  Payment fees at list price (£ / month)",
         lambda t, j: f"={col_of(j)}{PR['price']}*{a('paypct_'+t)}+{a('payfix_'+t)}", GBP2)
    prow(f"gm100_{case}", "  Gross margin at 100% of included usage",
         lambda t, j, c=case: f"=1-({col_of(j)}{PR['usage'+str(c)]}+{col_of(j)}{PR['fixed'+str(c)]}+{col_of(j)}{PR['pay'+str(c)]})/{col_of(j)}{PR['price']}", PCT, True)
    prow(f"gmutil_{case}", "  Gross margin at Base-scenario utilisation",
         lambda t, j, c=case: f"=1-({col_of(j)}{PR['usage'+str(c)]}*{a('util',2)}+{col_of(j)}{PR['fixed'+str(c)]}+{col_of(j)}{PR['pay'+str(c)]})/{col_of(j)}{PR['price']}", PCT)
    prow(f"cpc{case}", "  Cost per credit (£)",
         lambda t, j, c=case: f"=IF({col_of(j)}{PR['credits']}=0,0,{col_of(j)}{PR['usage'+str(c)]}/{col_of(j)}{PR['credits']})", GBP2)
    prow(f"overgm{case}", "  Overage gross margin",
         lambda t, j, c=case: f"=IF({col_of(j)}{PR['over']}=0,0,1-{col_of(j)}{PR['cpc'+str(c)]}/{col_of(j)}{PR['over']}-{a('paypct_'+t)})", PCT)
    prow(f"setupgm{case}", "  Setup fee gross margin (onboarding labour)",
         lambda t, j: f"=IF({col_of(j)}{PR['setup']}=0,0,1-{a('onb_'+t)}*{a('onb_rate')}/{col_of(j)}{PR['setup']})", PCT)
    prow(f"mins{case}", "  Human minutes per credit",
         lambda t, j, c=case: f"=IF({col_of(j)}{PR['credits']}=0,0,(" + "+".join(f"{mix(t,k)}*Unit_Costs!$S${UCROW[(c,k)]}" for k in range(10)) + f")/{col_of(j)}{PR['credits']})", NUM2)
pr += 1
# per-development economics
P.cell(pr, 1, "Per-development fee economics (extra development = 50-unit, 6 plan types)").font = BOLD
P.cell(pr, 1).fill = SFILL
pr += 1
P.cell(pr, 1, "  Fee charged (£) = plan types x £ per plan type")
P.cell(pr, 2, f"={a('d50_types')}*{a('per_type_fee')}").number_format = GBP0
PR["devrev"] = pr
pr += 1
for case in (1, 2, 3):
    P.cell(pr, 1, f"  Delivery cost (£), {CASES[case]} case")
    P.cell(pr, 2, f"=Unit_Costs!$Q${UCROW[(case,8)]}").number_format = GBP0
    P.cell(pr, 3, f"=IF($B${PR['devrev']}=0,0,1-B{pr}/$B${PR['devrev']}-{a('paypct_DevPro')})").number_format = PCT
    P.cell(pr, 4, "← gross margin")
    PR[f"devcost{case}"] = pr
    pr += 1
pr += 1

# B. Hypothesis evaluation
P.cell(pr, 1, "B. Hypothesis price points evaluated against the tier usage mix (gross margin at 100% included usage / at Base utilisation)").font = H2
for i in range(1, 8):
    P.cell(pr, i).fill = HFILL
pr += 1
for j, c in enumerate(["Hypothesis", "Price £/mo", "Usage mix", "GM @100% Base cost", "GM @100% High cost", "GM @util Base cost", "GM @util High cost"]):
    P.cell(pr, 1 + j, c).font = BOLD
    P.cell(pr, 1 + j).fill = SFILL
    P.cell(pr, 1 + j).alignment = WRAP
pr += 1
HYP = [("Studio £149", "price_Studio", "Studio"), ("Agency £499", "price_Agency", "Agency"), ("Developer Pro £1,499", "price_DevPro", "DevPro"),
       ("Enterprise £3k", "price_Ent_lo", "Ent"), ("Enterprise £5k", "price_Ent", "Ent"), ("Enterprise £10k", "price_Ent_hi", "Ent")]
for lab, pk, t in HYP:
    j = TIERS.index(t)
    P.cell(pr, 1, lab)
    P.cell(pr, 2, f"={a(pk)}").number_format = GBP0
    P.cell(pr, 3, TNAME[t])
    for k, (case, ut) in enumerate([(2, False), (3, False), (2, True), (3, True)]):
        uref = f"{col_of(j)}{PR['usage'+str(case)]}" + (f"*{a('util',2)}" if ut else "")
        P.cell(pr, 4 + k, f"=1-({uref}+{col_of(j)}{PR['fixed'+str(case)]}+B{pr}*{a('paypct_'+t)}+{a('payfix_'+t)})/B{pr}").number_format = PCT
    pr += 1
pr += 1

# C. Price required for target GM
P.cell(pr, 1, "C. Price required for target gross margin (price = (cost + fixed payment fee) / (1 − GM − payment %))").font = H2
for i in range(1, 10):
    P.cell(pr, i).fill = HFILL
pr += 1
GMS = [0.60, 0.70, 0.80, 0.85]
P.cell(pr, 1, "Target gross margin →").font = BOLD
for k, g in enumerate(GMS):
    c = P.cell(pr, 2 + k, g)
    c.font = BLUE
    c.number_format = PCT
    c2 = P.cell(pr, 6 + k, f"={CL(2+k)}{pr}")
    c2.number_format = PCT
GMROW = pr
pr += 1
P.cell(pr, 1, "Item").font = BOLD
for k in range(4):
    P.cell(pr, 2 + k, "Base cost £").font = BOLD
    P.cell(pr, 6 + k, "High cost £").font = BOLD
pr += 1
P.cell(pr, 1, "Subscription tiers at 100% of included usage (£ / month)").font = BOLD
P.cell(pr, 1).fill = SFILL
pr += 1
for j, t in enumerate(TIERS):
    P.cell(pr, 1, TNAME[t])
    for k in range(4):
        for off, case in ((2, 2), (6, 3)):
            g = f"{CL(off+k)}${GMROW}"
            cost = f"({col_of(j)}${PR['usage'+str(case)]}+{col_of(j)}${PR['fixed'+str(case)]}+{a('payfix_'+t)})"
            P.cell(pr, off + k, f"={cost}/(1-{g}-{a('paypct_'+t)})").number_format = GBP0
    pr += 1
P.cell(pr, 1, "One-off deliverables / per-development pricing (£ each, card payment)").font = BOLD
P.cell(pr, 1).fill = SFILL
pr += 1
for i, d in enumerate(DELIV):
    P.cell(pr, 1, d)
    for k in range(4):
        for off, case in ((2, 2), (6, 3)):
            g = f"{CL(off+k)}${GMROW}"
            P.cell(pr, off + k, f"=(Unit_Costs!$Q${UCROW[(case,i)]}+{a('payfix_Studio')})/(1-{g}-{a('paypct_Studio')})").number_format = GBP2
    pr += 1
pr += 1
notes = [
    "Recommendation (see financial_model_summary.md): keep the £149 / £499 / £1,499 / £5k+ anchors but sell CREDITS, not 'unlimited'. "
    "Every geometry-true output needs a human 2D confirm per plan, so a single-image order is labour-dominated: charge per plan conversion inside the credit price.",
    "Overages are priced above the effective included-credit price; setup fees cover onboarding labour; developments beyond the first are billed per plan type, "
    "because delivery cost scales with plan types, not units.",
    "Pixel streaming is the margin risk for interactive tours: default to WebGL/three.js viewers (pricing_inputs §6) and charge for streamed tours separately.",
]
for n in notes:
    P.cell(pr, 1, n).alignment = WRAP
    P.merge_cells(start_row=pr, start_column=1, end_row=pr, end_column=9)
    P.row_dimensions[pr].height = 32
    pr += 1
P.freeze_panes = "B3"


def pref(key, t, case=None):
    j = TIERS.index(t)
    k = key + (str(case) if case is not None else "")
    return f"Pricing!${col_of(j)}${PR[k]}"


# =====================================================================
# Model sheets
# =====================================================================
FIRST = 3  # column C = month 1
NM = 36
MCOL = [CL(FIRST + m) for m in range(NM)]  # month m+1
LASTC = MCOL[-1]


def build_model(name, sc):
    S = wb.create_sheet(name)
    scl = {1: "C", 2: "D", 3: "E"}[sc]
    S["A1"] = f"{name.replace('_', ' ')} scenario — monthly model, 36 months (£). All cells are formulas driven by Assumptions column {scl}."
    S["A1"].font = H1
    S.column_dimensions["A"].width = 52
    S.column_dimensions["B"].width = 14
    for c in MCOL:
        S.column_dimensions[c].width = 10.5
    R = {}
    rr = [4]
    S.cell(3, 1, "Month").font = BOLD
    S.cell(3, 2, "Unit").font = BOLD
    for m in range(NM):
        c = S.cell(3, FIRST + m, m + 1)
        c.font = BOLD
        c.fill = SFILL
        c.alignment = Alignment(horizontal="center")
    S.cell(4, 1, "Year").font = BOLD
    for m in range(NM):
        S.cell(4, FIRST + m, f'="Y"&ROUNDUP({MCOL[m]}$3/12,0)').alignment = Alignment(horizontal="center")
    rr[0] = 6

    def sec(title):
        r_ = rr[0]
        S.cell(r_, 1, title).font = H2
        for i in range(1, FIRST + NM):
            S.cell(r_, i).fill = HFILL
        rr[0] = r_ + 1

    def line(key, label, unit, fn, fmt=GBP0, bold=False, fill=None):
        r_ = rr[0]
        S.cell(r_, 1, label).font = BOLD if bold else BLACK
        S.cell(r_, 2, unit)
        for m in range(NM):
            col = MCOL[m]
            prev = MCOL[m - 1] if m > 0 else None
            v = fn(m + 1, col, prev, r_)
            c = S.cell(r_, FIRST + m, v)
            c.number_format = fmt
            if bold:
                c.font = BOLD
            if fill:
                c.fill = fill
        R[key] = r_
        rr[0] = r_ + 1
        return r_

    def blankline():
        rr[0] += 1

    x = lambda k: a(k, sc)
    # reserve hires flags rows later; but new customers reference productive AE row. Build headcount block first.
    sec("Headcount (step functions; triggers evaluated on previous month)")
    # placeholders for metric rows: customers total and MRR total -> keys defined later; we know row numbers only after.
    # So we pre-allocate rows for hires and fill formulas after all rows exist.
    hire_rows = []
    for hidx, h in enumerate(HIRES):
        hire_rows.append(rr[0])
        S.cell(rr[0], 1, f"{h[0]} (1 = hired)")
        S.cell(rr[0], 2, "flag")
        R[f"hire{hidx}"] = rr[0]
        rr[0] += 1
    R["heads"] = rr[0]
    S.cell(rr[0], 1, "Total headcount incl. founder").font = BOLD
    S.cell(rr[0], 2, "FTE")
    rr[0] += 1
    R["ae"] = rr[0]
    S.cell(rr[0], 1, "Account executives in seat")
    S.cell(rr[0], 2, "FTE")
    rr[0] += 1
    R["ae_prod"] = rr[0]
    S.cell(rr[0], 1, "Productive AEs (in seat ≥ ramp months)")
    S.cell(rr[0], 2, "FTE")
    rr[0] += 2

    sec("Customers")
    for t in TIERS:
        def fn(m, col, prev, r_, t=t):
            base = f"IF({col}$3<{x('launch_'+t)},0,MIN({x('cap_'+t)},{x('init_'+t)}+{x('ramp_'+t)}*({col}$3-{x('launch_'+t)})))"
            if t in ("DevPro", "Ent"):
                base += f"+IF({col}$3<{x('launch_'+t)},0,{col}${R['ae_prod']}*{x('ae_up_'+t)})"
            return "=" + base
        line(f"new_{t}", f"New customers — {TNAME[t]}", "logos", fn, NUM2)
    for t in TIERS:
        line(f"churn_{t}", f"Churned customers — {TNAME[t]}", "logos",
             lambda m, col, prev, r_, t=t: f"={prev}{r_+4}*{x('churn_'+t)}" if prev else "=0", NUM2)
    for t in TIERS:
        line(f"cust_{t}", f"Customers (end of month) — {TNAME[t]}", "logos",
             lambda m, col, prev, r_, t=t: (f"={prev}{r_}+{col}{R['new_'+t]}-{col}{R['churn_'+t]}" if prev else f"={col}{R['new_'+t]}-{col}{R['churn_'+t]}"), NUM1)
    line("new_tot", "Total new customers", "logos", lambda m, col, prev, r_: "=" + "+".join(f"{col}{R['new_'+t]}" for t in TIERS), NUM2, True)
    line("churn_tot", "Total churned customers", "logos", lambda m, col, prev, r_: "=" + "+".join(f"{col}{R['churn_'+t]}" for t in TIERS), NUM2)
    line("cust_tot", "Total paying customers", "logos", lambda m, col, prev, r_: "=" + "+".join(f"{col}{R['cust_'+t]}" for t in TIERS), NUM1, True, KFILL)
    blankline()

    sec("Revenue")
    for t in TIERS:
        line(f"mrr_{t}", f"Subscription MRR — {TNAME[t]}", "£",
             lambda m, col, prev, r_, t=t: ((f"={prev}{r_}*(1-{x('churn_'+t)})*(1+{x('exp_'+t)})+" if prev else "=")
                                            + f"{col}{R['new_'+t]}*{a('price_'+t)}*{x('real_'+t)}"), GBP0)
    line("mrr", "Subscription MRR (total) — milestone metric", "£", lambda m, col, prev, r_: "=" + "+".join(f"{col}{R['mrr_'+t]}" for t in TIERS), GBP0, True, KFILL)
    line("arr", "ARR (subscription MRR x 12)", "£", lambda m, col, prev, r_: f"={col}{R['mrr']}*12", GBP0, True)
    for t in TIERS:
        line(f"arpa_{t}", f"ARPA — {TNAME[t]}", "£ / month",
             lambda m, col, prev, r_, t=t: f"=IF({col}{R['cust_'+t]}<0.0001,0,{col}{R['mrr_'+t]}/{col}{R['cust_'+t]})", GBP0)
    line("arpa", "ARPA — blended", "£ / month", lambda m, col, prev, r_: f"=IF({col}{R['cust_tot']}<0.0001,0,{col}{R['mrr']}/{col}{R['cust_tot']})", GBP0)
    for t in TIERS:
        line(f"overrev_{t}", f"Overage revenue — {TNAME[t]}", "£",
             lambda m, col, prev, r_, t=t: f"={col}{R['cust_'+t]}*{pref('credits',t)}*{x('over_pct')}*{a('over_'+t)}", GBP0)
    for t in TIERS:
        line(f"setuprev_{t}", f"Setup fees — {TNAME[t]}", "£",
             lambda m, col, prev, r_, t=t: f"={col}{R['new_'+t]}*{a('setup_'+t)}*{x('setup_collect')}", GBP0)
    line("devs", "Additional developments launched (Developer Pro)", "developments",
         lambda m, col, prev, r_: f"={col}{R['cust_DevPro']}*{x('devs_year')}/12", NUM2)
    line("devrev", "Per-development fees", "£", lambda m, col, prev, r_: f"={col}{R['devs']}*{a('d50_types')}*{a('per_type_fee')}", GBP0)
    line("rev_sub", "Revenue — subscription", "£", lambda m, col, prev, r_: f"={col}{R['mrr']}", GBP0)
    line("rev_over", "Revenue — overage", "£", lambda m, col, prev, r_: "=" + "+".join(f"{col}{R['overrev_'+t]}" for t in TIERS), GBP0)
    line("rev_setup", "Revenue — setup + per-development fees", "£",
         lambda m, col, prev, r_: "=" + "+".join(f"{col}{R['setuprev_'+t]}" for t in TIERS) + f"+{col}{R['devrev']}", GBP0)
    line("rev", "Total revenue", "£", lambda m, col, prev, r_: f"={col}{R['rev_sub']}+{col}{R['rev_over']}+{col}{R['rev_setup']}", GBP0, True, KFILL)
    blankline()

    sec("Cost of goods sold")
    case = x("cost_case")

    def cpc(t):
        return f"CHOOSE({case},{pref('cpc',t,1)},{pref('cpc',t,2)},{pref('cpc',t,3)})"

    def fixacct(t):
        return f"CHOOSE({case},{pref('fixed',t,1)},{pref('fixed',t,2)},{pref('fixed',t,3)})"

    for t in TIERS:
        line(f"cogs_use_{t}", f"Generation + human QA on included usage — {TNAME[t]}", "£",
             lambda m, col, prev, r_, t=t: f"={col}{R['cust_'+t]}*{pref('credits',t)}*{x('util')}*{cpc(t)}", GBP0)
    line("cogs_over", "Generation + human QA on overage usage", "£",
         lambda m, col, prev, r_: "=" + "+".join(f"{col}{R['cust_'+t]}*{pref('credits',t)}*{x('over_pct')}*{cpc(t)}" for t in TIERS), GBP0)
    line("cogs_host", "Interactive hosting / streaming (per account)", "£",
         lambda m, col, prev, r_: "=" + "+".join(f"{col}{R['cust_'+t]}*{a('hosted_'+t)}*CHOOSE({case},Unit_Costs!$Q${UCROW[(1,'host')]},Unit_Costs!$Q${UCROW[(2,'host')]},Unit_Costs!$Q${UCROW[(3,'host')]})" for t in TIERS), GBP0)
    line("cogs_sso", "SSO connections (WorkOS)", "£",
         lambda m, col, prev, r_: "=(" + "+".join(f"{col}{R['cust_'+t]}*{a('sso_'+t)}" for t in TIERS) + f")*{a('sso_price')}*{a('fx')}", GBP0)
    line("cogs_onb", "Onboarding labour (new customers)", "£",
         lambda m, col, prev, r_: "=(" + "+".join(f"{col}{R['new_'+t]}*{a('onb_'+t)}" for t in TIERS) + f")*{a('onb_rate')}", GBP0)
    line("cogs_dev", "Delivery of additional developments", "£",
         lambda m, col, prev, r_: f"={col}{R['devs']}*CHOOSE({case},Unit_Costs!$Q${UCROW[(1,8)]},Unit_Costs!$Q${UCROW[(2,8)]},Unit_Costs!$Q${UCROW[(3,8)]})", GBP0)
    line("cogs_pay", "Payment processing fees", "£",
         lambda m, col, prev, r_: "=" + "+".join(
             f"({col}{R['mrr_'+t]}+{col}{R['overrev_'+t]}+{col}{R['setuprev_'+t]})*{a('paypct_'+t)}+{col}{R['cust_'+t]}*{a('payfix_'+t)}" for t in TIERS)
         + f"+{col}{R['devrev']}*{a('paypct_DevPro')}", GBP0)
    line("cogs_infra", "Platform infrastructure", "£",
         lambda m, col, prev, r_: f"={a('infra_base')}+{a('infra_cust')}*{col}{R['cust_tot']}", GBP0)
    line("cogs_oda", "ODA Drawings SDK licence (DWG)", "£",
         lambda m, col, prev, r_: (f"=IF({col}$3={a('oda_start')},{a('oda_init')},IF(AND({col}$3>{a('oda_start')},MOD({col}$3-{a('oda_start')},12)=0),{a('oda_renew')},0))*{a('fx')}"), GBP0)
    line("cogs", "Total COGS", "£", lambda m, col, prev, r_: f"=SUM({col}{R['cogs_use_Studio']}:{col}{R['cogs_oda']})", GBP0, True)
    line("gp", "Gross profit", "£", lambda m, col, prev, r_: f"={col}{R['rev']}-{col}{R['cogs']}", GBP0, True, KFILL)
    line("gm", "Gross margin", "%", lambda m, col, prev, r_: f"=IF({col}{R['rev']}=0,0,{col}{R['gp']}/{col}{R['rev']})", PCT, True)
    blankline()

    sec("Operating expenses")
    line("op_founder", "Founder salary (incl. on-costs)", "£", lambda m, col, prev, r_: f"={a('founder_sal')}*(1+{a('oncost')})/12", GBP0)
    for hidx, h in enumerate(HIRES):
        hr_ = HROW[hidx]
        line(f"op_hire{hidx}", f"{h[0]} (incl. on-costs)", "£",
             lambda m, col, prev, r_, hidx=hidx, hr_=hr_: f"={col}{R['hire'+str(hidx)]}*Assumptions!$D${hr_}*(1+{a('oncost')})/12", GBP0)
    line("op_recruit", "Recruitment fees (hire month)", "£",
         lambda m, col, prev, r_: "=" + "+".join(
             (f"({col}{R['hire'+str(h)]}-{prev}{R['hire'+str(h)]})" if prev else f"{col}{R['hire'+str(h)]}")
             + f"*Assumptions!$D${HROW[h]}*Assumptions!$E${HROW[h]}" for h in range(len(HIRES))), GBP0)
    line("op_contract", "Contract engineering (until Engineer #1)", "£",
         lambda m, col, prev, r_: f"=IF({col}{R['hire'+str(ENG1_IDX)]}=0,{a('contract_eng')},0)", GBP0)
    line("op_mkt", "Marketing programmes + events", "£", lambda m, col, prev, r_: f"={a('mkt_fixed')}+{a('events')}/12", GBP0)
    line("op_data", "Channel & data subscriptions (Reapit network, Barbour ABI)", "£",
         lambda m, col, prev, r_: f"={a('reapit')}/12+IF({col}$3>={x('launch_DevPro')},{a('barbour')}/12,0)", GBP0)
    line("op_mktvar", "Variable marketing (% revenue)", "£", lambda m, col, prev, r_: f"={col}{R['rev']}*{a('mkt_var')}", GBP0)
    line("op_comm", "Sales commission (Developer Pro + Enterprise new ACV)", "£",
         lambda m, col, prev, r_: f"=IF({col}{R['ae']}>0,({col}{R['new_DevPro']}*{a('price_DevPro')}*{x('real_DevPro')}+{col}{R['new_Ent']}*{a('price_Ent')}*{x('real_Ent')})*12*{a('commission')},0)", GBP0)
    line("op_sw", "Software & tools", "£", lambda m, col, prev, r_: f"={a('sw_base')}+{a('sw_head')}*{col}{R['heads']}", GBP0)
    line("op_iso", "ISO 27001 programme + compliance platform", "£",
         lambda m, col, prev, r_: f"=IF({col}$3<{x('iso_start')},0,IF({col}$3<{x('iso_start')}+12,{a('iso_y1')}/12,{a('iso_ongoing')}/12))", GBP0)
    line("op_ins", "Insurance (cyber, PI, public liability)", "£", lambda m, col, prev, r_: f"={a('insurance')}/12", GBP0)
    line("op_legal", "Legal, accounting, admin", "£", lambda m, col, prev, r_: f"={a('legal_m')}+IF({col}$3=1,{a('legal_once')},0)", GBP0)
    line("opex", "Total operating expenses", "£", lambda m, col, prev, r_: f"=SUM({col}{R['op_founder']}:{col}{R['op_legal']})", GBP0, True)
    line("op_eng", "  memo: engineering (eng hires + contract)", "£",
         lambda m, col, prev, r_: f"={col}{R['op_hire1']}+{col}{R['op_hire4']}+{col}{R['op_hire8']}+{col}{R['op_contract']}", GBP0)
    line("op_sales", "  memo: sales & marketing (AEs, marketing hire, programmes, commission)", "£",
         lambda m, col, prev, r_: f"={col}{R['op_hire2']}+{col}{R['op_hire7']}+{col}{R['op_hire6']}+{col}{R['op_mkt']}+{col}{R['op_data']}+{col}{R['op_mktvar']}+{col}{R['op_comm']}", GBP0)
    line("op_support", "  memo: support / customer success hires", "£",
         lambda m, col, prev, r_: f"={col}{R['op_hire0']}+{col}{R['op_hire5']}+{col}{R['op_hire9']}", GBP0)
    blankline()

    sec("Profitability & cash")
    line("contrib", "Contribution (gross profit − direct S&M: programmes, data, variable mkt, commission)", "£",
         lambda m, col, prev, r_: f"={col}{R['gp']}-{col}{R['op_mkt']}-{col}{R['op_data']}-{col}{R['op_mktvar']}-{col}{R['op_comm']}", GBP0)
    line("contrib_pct", "Contribution margin", "%", lambda m, col, prev, r_: f"=IF({col}{R['rev']}=0,0,{col}{R['contrib']}/{col}{R['rev']})", PCT)
    line("ebitda", "EBITDA (monthly operating profit)", "£", lambda m, col, prev, r_: f"={col}{R['gp']}-{col}{R['opex']}", GBP0, True, KFILL)
    line("ebitda_pct", "EBITDA margin", "%", lambda m, col, prev, r_: f"=IF({col}{R['rev']}=0,0,{col}{R['ebitda']}/{col}{R['rev']})", PCT)
    line("cum_ebitda", "Cumulative EBITDA", "£", lambda m, col, prev, r_: f"={prev}{r_}+{col}{R['ebitda']}" if prev else f"={col}{R['ebitda']}", GBP0)
    line("cash_open", "Opening cash", "£", lambda m, col, prev, r_: f"={prev}{r_+1}" if prev else f"={a('start_cash')}", GBP0)
    line("cash", "Closing cash balance (negative = funding required)", "£", lambda m, col, prev, r_: f"={col}{R['cash_open']}+{col}{R['ebitda']}", GBP0, True, KFILL)
    line("burn", "Net burn (cash outflow)", "£", lambda m, col, prev, r_: f"=MAX(0,-{col}{R['ebitda']})", GBP0)
    line("runway", "Runway at current burn", "months",
         lambda m, col, prev, r_: f'=IF({col}{R["burn"]}=0,"cash+",IF({col}{R["cash"]}<=0,0,{col}{R["cash"]}/{col}{R["burn"]}))', NUM1)
    blankline()

    sec("Helpers (used by Milestones / Summary)")
    line("mrr_max", "Running max subscription MRR", "£", lambda m, col, prev, r_: f"=MAX({prev}{r_},{col}{R['mrr']})" if prev else f"={col}{R['mrr']}", GBP0)
    line("be_flag", "EBITDA ≥ 0 (1 = yes)", "flag", lambda m, col, prev, r_: f"=IF({col}{R['ebitda']}>=0,1,0)", NUM0)
    # sustained flag: computed right-to-left
    r_s = rr[0]
    S.cell(r_s, 1, "EBITDA ≥ 0 this month and every later month (1 = yes)")
    S.cell(r_s, 2, "flag")
    for m in range(NM):
        col = MCOL[m]
        if m == NM - 1:
            S.cell(r_s, FIRST + m, f"={col}{R['be_flag']}")
        else:
            S.cell(r_s, FIRST + m, f"=IF(AND({col}{R['be_flag']}=1,{MCOL[m+1]}{r_s}=1),1,0)")
        S.cell(r_s, FIRST + m).number_format = NUM0
    R["be_sust"] = r_s
    rr[0] += 1
    line("ops_hours", "Human delivery hours needed (QA, 2D confirm, support, onboarding)", "hours",
         lambda m, col, prev, r_: "=(" + "+".join(
             f"{col}{R['cust_'+t]}*{pref('credits',t)}*({x('util')}+{x('over_pct')})*CHOOSE({case},{pref('mins',t,1)},{pref('mins',t,2)},{pref('mins',t,3)})" for t in TIERS)
         + ")/60+(" + "+".join(f"{col}{R['new_'+t]}*{a('onb_'+t)}" for t in TIERS) + ")", NUM1)
    line("gm_loaded", "Memo: gross margin if support/CS salaries were treated as COGS", "%",
         lambda m, col, prev, r_: f"=IF({col}{R['rev']}=0,0,({col}{R['gp']}-{col}{R['op_support']})/{col}{R['rev']})", PCT)
    line("neg_flag", "Cash balance < 0 (1 = yes)", "flag", lambda m, col, prev, r_: f"=IF({col}{R['cash']}<0,1,0)", NUM0)
    line("ent_flag", "Enterprise new customers > 0 (1 = yes)", "flag", lambda m, col, prev, r_: f"=IF({col}{R['new_Ent']}>0,1,0)", NUM0)
    line("founder_cap", "Founder delivery capacity", "hours", lambda m, col, prev, r_: f"={a('founder_hours')}*{a('founder_ops')}", NUM1)
    line("cap_flag", "Delivery hours exceed solo-founder capacity (1 = yes)", "flag",
         lambda m, col, prev, r_: f"=IF({col}{R['ops_hours']}>{col}{R['founder_cap']},1,0)", NUM0)

    # now fill hire flags
    for hidx, h in enumerate(HIRES):
        hr_ = HROW[hidx]
        r_ = R[f"hire{hidx}"]
        for m in range(NM):
            col = MCOL[m]
            prev = MCOL[m - 1] if m > 0 else None
            if prev is None:
                fm = "=0"
            else:
                metric = f'IF(Assumptions!$B${hr_}="Customers",{prev}{R["cust_tot"]},{prev}{R["mrr"]})'
                fm = f"=MAX({prev}{r_},IF({metric}>=Assumptions!$C${hr_},1,0))"
            c = S.cell(r_, FIRST + m, fm)
            c.number_format = NUM0
    for m in range(NM):
        col = MCOL[m]
        S.cell(R["heads"], FIRST + m, "=1+" + "+".join(f"{col}{R['hire'+str(h)]}" for h in range(len(HIRES)) if h != FOUNDER_UP_IDX)).number_format = NUM0
        S.cell(R["ae"], FIRST + m, "=" + "+".join(f"{col}{R['hire'+str(h)]}" for h in AE_IDX)).number_format = NUM0
        S.cell(R["ae_prod"], FIRST + m,
               f"=IF({col}$3>{x('ae_lag')},OFFSET({col}{R['ae']},0,-{x('ae_lag')}),0)").number_format = NUM0
    S.freeze_panes = "C5"
    return R


MR = {}
for name, sc in (("Model_Bear", 1), ("Model_Base", 2), ("Model_Bull", 3)):
    MR[name] = build_model(name, sc)
R = MR["Model_Base"]  # rows identical across sheets
SCN = [("Bear", "Model_Bear"), ("Base", "Model_Base"), ("Bull", "Model_Bull")]


def rng(sheet, key):
    return f"{sheet}!$C${R[key]}:${LASTC}${R[key]}"


def at(sheet, key, month):
    return f"INDEX({rng(sheet,key)},{month})"


# =====================================================================
# Milestones
# =====================================================================
M = wb.create_sheet("Milestones")
M["A1"] = "Milestones — first month reached (subscription MRR basis; ARR = MRR x 12)"
M["A1"].font = H1
M.column_dimensions["A"].width = 34
for i in range(2, 10):
    M.column_dimensions[CL(i)].width = 16
mr = 3
for j, c in enumerate(["Milestone", "MRR threshold £", "Bear", "Base", "Bull"]):
    M.cell(mr, 1 + j, c).font = BOLD
    M.cell(mr, 1 + j).fill = SFILL
mr += 1
MILES = [("£10k MRR", "=10000"), ("£25k MRR", "=25000"), ("£50k MRR", "=50000"), ("£100k MRR", "=100000"),
         ("£250k MRR", "=250000"), ("£1m ARR", "=1000000/12"), ("£5m ARR", "=5000000/12")]
MILEROW = []
for lab, thr in MILES:
    M.cell(mr, 1, lab)
    c = M.cell(mr, 2, thr)
    c.number_format = GBP0
    c.font = BLUE
    for k, (sn, sh) in enumerate(SCN):
        M.cell(mr, 3 + k, f'=IF(COUNTIF({rng(sh,"mrr_max")},"<"&$B{mr})>=36,"Not reached in 36m",COUNTIF({rng(sh,"mrr_max")},"<"&$B{mr})+1)')
        M.cell(mr, 3 + k).alignment = Alignment(horizontal="center")
    MILEROW.append(mr)
    mr += 1
mr += 1
M.cell(mr, 1, "Example customer mix needed to hit each milestone (uses Base-case month-36 MRR mix by tier and month-36 ARPA)").font = H2
for i in range(1, 8):
    M.cell(mr, i).fill = HFILL
mr += 1
for j, c in enumerate(["Milestone", "MRR £"] + [TNAME[t] for t in TIERS] + ["Total customers"]):
    M.cell(mr, 1 + j, c).font = BOLD
    M.cell(mr, 1 + j).fill = SFILL
mr += 1
M.cell(mr, 1, "Base m36 share of MRR")
for j, t in enumerate(TIERS):
    M.cell(mr, 3 + j, f"=IF({at('Model_Base','mrr',36)}=0,0,{at('Model_Base','mrr_'+t,36)}/{at('Model_Base','mrr',36)})").number_format = PCT
SHR = mr
mr += 1
M.cell(mr, 1, "Base m36 ARPA £/month")
for j, t in enumerate(TIERS):
    M.cell(mr, 3 + j, f"={at('Model_Base','arpa_'+t,36)}").number_format = GBP0
ARR_ = mr
mr += 1
for k, (lab, thr) in enumerate(MILES):
    M.cell(mr, 1, lab)
    M.cell(mr, 2, f"=$B${MILEROW[k]}").number_format = GBP0
    for j, t in enumerate(TIERS):
        cl = CL(3 + j)
        M.cell(mr, 3 + j, f"=IF({cl}${ARR_}=0,0,$B{mr}*{cl}${SHR}/{cl}${ARR_})").number_format = NUM0
    M.cell(mr, 7, f"=SUM(C{mr}:F{mr})").number_format = NUM0
    mr += 1
mr += 1
M.cell(mr, 1, ("Read: e.g. '£100k MRR' needs roughly the customers shown at today's modelled price realisation and mix. "
               "Compare with the UK universes (market_segments Q1/Q7): ~500 medium developers, ~200 off-plan sellers, ~25 nationals, ~10,650 independent agent branches; "
               "SOM estimate ≈ £1.25m ARR by year 3.")).alignment = WRAP
M.merge_cells(start_row=mr, start_column=1, end_row=mr, end_column=7)
M.row_dimensions[mr].height = 45

# =====================================================================
# Summary
# =====================================================================
Sm = wb.create_sheet("Summary")
Sm["A1"] = "Summary — key outputs by scenario (months 12 / 24 / 36)"
Sm["A1"].font = H1
Sm.column_dimensions["A"].width = 46
for i in range(2, 12):
    Sm.column_dimensions[CL(i)].width = 13
sr = 3
Sm.cell(sr, 1, "Metric").font = BOLD
Sm.cell(sr, 1).fill = SFILL
col = 2
for sn, sh in SCN:
    for mth in (12, 24, 36):
        c = Sm.cell(sr, col, f"{sn} M{mth}")
        c.font = BOLD
        c.fill = SFILL
        c.alignment = Alignment(horizontal="center")
        col += 1
sr += 1
METRICS = [("Subscription MRR (£)", "mrr", GBP0), ("ARR (£)", "arr", GBP0), ("Total revenue in month (£)", "rev", GBP0),
           ("Paying customers", "cust_tot", NUM1), ("  Studio", "cust_Studio", NUM1), ("  Agency", "cust_Agency", NUM1),
           ("  Developer Pro", "cust_DevPro", NUM1), ("  Enterprise", "cust_Ent", NUM1), ("Blended ARPA (£/mo)", "arpa", GBP0),
           ("Gross margin (month)", "gm", PCT), ("  memo: GM incl. support/CS salaries", "gm_loaded", PCT), ("Monthly EBITDA (£)", "ebitda", GBP0), ("Cumulative EBITDA (£)", "cum_ebitda", GBP0),
           ("Cash balance (£; negative = funding needed)", "cash", GBP0), ("Headcount incl. founder", "heads", NUM0)]
SUMR = {}
for lab, key, fmt in METRICS:
    Sm.cell(sr, 1, lab)
    col = 2
    for sn, sh in SCN:
        for mth in (12, 24, 36):
            Sm.cell(sr, col, f"={at(sh,key,mth)}").number_format = fmt
            col += 1
    SUMR[key] = sr
    sr += 1
sr += 1
Sm.cell(sr, 1, "Scenario-level outputs").font = H2
for i in range(1, 5):
    Sm.cell(sr, i).fill = HFILL
sr += 1
for j, c in enumerate(["Metric", "Bear", "Base", "Bull"]):
    Sm.cell(sr, 1 + j, c).font = BOLD
    Sm.cell(sr, 1 + j).fill = SFILL
sr += 1
SL = {}


def srow(key, lab, fn, fmt):
    global sr
    Sm.cell(sr, 1, lab)
    for k, (sn, sh) in enumerate(SCN):
        c = Sm.cell(sr, 2 + k, fn(sh))
        c.number_format = fmt
        c.alignment = Alignment(horizontal="right")
    SL[key] = sr
    sr += 1


srow("be1", "First month with EBITDA ≥ 0", lambda sh: f'=IFERROR(MATCH(1,{rng(sh,"be_flag")},0),"Not reached in 36m")', NUM0)
srow("be2", "Sustained break-even month (EBITDA ≥ 0 from then on)", lambda sh: f'=IFERROR(MATCH(1,{rng(sh,"be_sust")},0),"Not reached in 36m")', NUM0)
srow("mincash", "Lowest cash balance (£)", lambda sh: f"=MIN({rng(sh,'cash')})", GBP0)
srow("minmonth", "Month of lowest cash", lambda sh: f"=MATCH(MIN({rng(sh,'cash')}),{rng(sh,'cash')},0)", NUM0)
srow("funding", "External funding needed to stay ≥ £0 (£)", lambda sh: f"=MAX(0,-MIN({rng(sh,'cash')}))", GBP0)
srow("negmonth", "First month cash goes negative", lambda sh: f'=IFERROR(MATCH(1,{rng(sh,"neg_flag")},0),"Never")', NUM0)
srow("rev36", "Cumulative revenue, 36 months (£)", lambda sh: f"=SUM({rng(sh,'rev')})", GBP0)
srow("gm36", "Gross margin, 36-month cumulative", lambda sh: f"=IF(SUM({rng(sh,'rev')})=0,0,SUM({rng(sh,'gp')})/SUM({rng(sh,'rev')}))", PCT)
srow("caphit", "First month human delivery hours exceed solo-founder capacity",
     lambda sh: f'=IFERROR(MATCH(1,{rng(sh,"cap_flag")},0),"Not in 36m")', NUM0)
srow("cust_at_cap", "Customers in that month", lambda sh: f'=IFERROR(INDEX({rng(sh,"cust_tot")},MATCH(1,{rng(sh,"cap_flag")},0)),"n/a")', NUM1)
srow("hire0", "Month first support/QA hire starts", lambda sh: f'=IFERROR(MATCH(1,{sh}!$C${R["hire0"]}:${LASTC}${R["hire0"]},0),"Not in 36m")', NUM0)
srow("hire1", "Month Engineer #1 starts", lambda sh: f'=IFERROR(MATCH(1,{sh}!$C${R["hire1"]}:${LASTC}${R["hire1"]},0),"Not in 36m")', NUM0)
srow("hire2", "Month AE #1 starts", lambda sh: f'=IFERROR(MATCH(1,{sh}!$C${R["hire2"]}:${LASTC}${R["hire2"]},0),"Not in 36m")', NUM0)
srow("ent1", "Month first Enterprise customer signs (any fraction)",
     lambda sh: f'=IFERROR(MATCH(1,{rng(sh,"ent_flag")},0),"Not in 36m")', NUM0)
sr += 1

# Solo founder capacity
Sm.cell(sr, 1, "Solo-founder delivery capacity estimate (Base cost case)").font = H2
for i in range(1, 6):
    Sm.cell(sr, i).fill = HFILL
sr += 1
Sm.cell(sr, 1, "Founder hours available for delivery ops / month")
Sm.cell(sr, 2, f"={a('founder_hours')}*{a('founder_ops')}").number_format = NUM1
CAPR = sr
sr += 1
for j, c in enumerate(["Unit", "Human minutes each", "Max per month (founder only)"]):
    Sm.cell(sr, 1 + j, c).font = BOLD
    Sm.cell(sr, 1 + j).fill = SFILL
sr += 1
SOLO = {}
for i in (0, 2, 3, 4, 7, 8):
    Sm.cell(sr, 1, DELIV[i])
    Sm.cell(sr, 2, f"=Unit_Costs!$S${UCROW[(2,i)]}").number_format = NUM1
    Sm.cell(sr, 3, f"=IF(B{sr}=0,0,$B${CAPR}*60/B{sr})").number_format = NUM1
    SOLO[i] = sr
    sr += 1
for t in TIERS:
    Sm.cell(sr, 1, f"{TNAME[t]} customer-month at Base utilisation (+overage)")
    Sm.cell(sr, 2, f"={pref('credits',t)}*({a('util',2)}+{a('over_pct',2)})*{pref('mins',t,2)}").number_format = NUM1
    Sm.cell(sr, 3, f"=IF(B{sr}=0,0,$B${CAPR}*60/B{sr})").number_format = NUM1
    SOLO[t] = sr
    sr += 1
Sm.cell(sr, 1, ("Reasoning: founder works ~180 h/month; ~35% is assumed available for delivery operations (mandatory human 2D confirm per plan, "
                "output QA, support, onboarding) because the rest goes to building the product (6–15 engineering-months per technical_feasibility), "
                "selling and admin. Capacity = available minutes / human minutes per unit (Unit_Costs column S, Base case incl. rejects). "
                "Onboarding hours for new customers reduce this further.")).alignment = WRAP
Sm.merge_cells(start_row=sr, start_column=1, end_row=sr, end_column=10)
Sm.row_dimensions[sr].height = 58
sr += 2
Sm.cell(sr, 1, "Key unit-economics references").font = H2
for i in range(1, 6):
    Sm.cell(sr, i).fill = HFILL
sr += 1
for j, c in enumerate(["Tier", "GM @100% (Base)", "GM @util (Base)", "GM @100% (High)", "Cost/credit Base £"]):
    Sm.cell(sr, 1 + j, c).font = BOLD
    Sm.cell(sr, 1 + j).fill = SFILL
sr += 1
for t in TIERS:
    Sm.cell(sr, 1, TNAME[t])
    Sm.cell(sr, 2, f"={pref('gm100_',t,2)}").number_format = PCT
    Sm.cell(sr, 3, f"={pref('gmutil_',t,2)}").number_format = PCT
    Sm.cell(sr, 4, f"={pref('gm100_',t,3)}").number_format = PCT
    Sm.cell(sr, 5, f"={pref('cpc',t,2)}").number_format = GBP2
    sr += 1
Sm.freeze_panes = "B4"

# =====================================================================
# README
# =====================================================================
RD = wb.create_sheet("README", 0)
RD.column_dimensions["A"].width = 26
RD.column_dimensions["B"].width = 120
lines = [
    ("Property Visualisation SaaS — 36-month financial model", None, H1),
    ("Purpose", "Test whether a UK-first AI property visualisation SaaS (floor plans / CAD / IFC → geometry-true 3D, renders, tours, video, "
                "white-label viewers and configurators) can become a viable business. Built to be conservative: the aim is to find out "
                "whether the idea deserves to exist, not to flatter it.", None),
    ("Date / currency", "Built 20 Oct 2026. Model currency GBP (£); vendor prices in USD converted at the FX rate below. Prices ex VAT. "
                        "No corporation tax, VAT timing, R&D credits, capex or working-capital effects (annual prepayments ignored).", None),
    ("FX rate", "£0.755 per US$1 (≈ $1.324 per £) — X-Rates October 2026 monthly average (0.755183, 20 days). Editable at Assumptions!D" + str(REF["fx"]) + ".", None),
    ("How to use", "1) Change blue cells on Assumptions (and the target-GM row on Pricing, milestone thresholds on Milestones). "
                   "2) Everything else recalculates. 3) Read Summary first, then Milestones, Pricing, Unit_Costs. "
                   "Scenario sheets (Model_Bear / Model_Base / Model_Bull) use Assumptions columns C / D / E respectively. "
                   "Unit-cost Low/Base/High also use columns C / D / E; each scenario picks a cost case via 'Unit-cost case used'.", None),
    ("Colour legend", "Blue text = hard-coded input you can change. Black text = formula. Green text = direct link to another sheet. "
                      "Yellow-shaded label = ASSUMPTION (modeller's judgement, no source in notes). Light-yellow rows in model sheets = key outputs.", None),
    ("Source labels", "VERIFIED = quoted from a vendor or primary page cited in the research notes. ESTIMATE = researcher estimate built from cited "
                      "prices. ASSUMPTION = modeller's judgement where the notes have no figure (replace with pilot data).", None),
    ("Sheets", "Assumptions · Unit_Costs (cost per successful deliverable, Low/Base/High, retry/failure table) · Pricing (tiers, allowances, overage, "
               "setup, per-development; GM at included usage; price for 60/70/80/85% GM) · Model_Bear / Model_Base / Model_Bull (monthly, 36m) · "
               "Milestones · Summary.", None),
    ("Key modelling choices", "MRR milestone metric = subscription MRR only (overage, setup and per-development fees are revenue but not MRR). "
                              "Customers are expected values (fractional). Hires are step functions triggered by the previous month's customers or MRR. "
                              "Human QA is costed at contractor rates in COGS even when the founder does it (conservative). "
                              "Enterprise wins cannot start before month 12 (Base), 18 (Bear), 10 (Bull). Self-serve launch month 6 (Base), 9 (Bear), 4 (Bull).", None),
    ("Research notes", "/home/user/widgetme-legal/research_notes/AI property visualisation SaaS audit/ : pricing_inputs.md, market_segments.md, "
                       "gtm_benchmarks.md, competitors.md, technical_feasibility.md, legal_compliance.md", None),
]
rr_ = 1
for k, v, f in lines:
    c = RD.cell(rr_, 1, k)
    c.font = f or BOLD
    if v:
        RD.cell(rr_, 2, v).alignment = WRAP
        RD.row_dimensions[rr_].height = max(15, 15 * (len(v) // 115 + 1))
    rr_ += 1
rr_ += 1
RD.cell(rr_, 1, "Sources (from notes)").font = H2
RD.cell(rr_, 1).fill = HFILL
RD.cell(rr_, 2).fill = HFILL
rr_ += 1
SRC_LABEL = {
    "claude": "Claude API pricing (LLM tokens)", "gemini": "Gemini API pricing (Nano Banana images, Veo video)", "kling": "Kling API video pricing",
    "runpod": "RunPod GPU pricing", "aws_g6e": "AWS g6e.xlarge (Vantage)", "gamelift": "AWS GameLift Streams pricing", "vagon": "Vagon Streams pricing",
    "r2": "Cloudflare R2 pricing", "bunny": "Bunny CDN pricing", "flex": "Autodesk Flex tokens (APS)", "aps": "APS business model change",
    "upwork": "Upwork rendering freelancer rates", "stripe": "Stripe UK pricing", "workos": "WorkOS SSO pricing", "vercel": "Vercel pricing",
    "xrates": "X-Rates USD/GBP 2026 averages", "oda": "Open Design Alliance membership pricing", "saascap": "SaaS Capital retention benchmarks 2025",
    "iconiq": "ICONIQ AI gross margins (via SaaStr)", "aleph": "CAC payback benchmarks (Aleph)", "salesmind": "Sales cycle benchmarks",
    "henderson": "Henderson Scott Technology Salary Guide 2026", "pyralink": "ISO 27001 UK cost (Pyralink)", "hightable": "ISO 27001 3-year cycle (HighTable)",
    "barbour": "Barbour ABI subscriptions", "reapitkb": "Reapit developer network fee (secondhand)", "proplan": "ProPlan Studio pricing",
    "realitiq": "Realitiq per-unit pricing", "idealtwin": "IdealTwin per-unit pricing", "getfloorplan": "Getfloorplan pricing",
    "metropix": "Landmark Metropix pricing", "rightmove": "Rightmove FY2025 ARPA", "blockout": "Blockout Digital CGI pricing guide",
    "planner5d": "Planner 5D B2B recognition (human review)", "booth": "UK stand sample budget",
}
for k, url in SRC.items():
    RD.cell(rr_, 1, SRC_LABEL.get(k, k))
    RD.cell(rr_, 2, url)
    rr_ += 1

for ws in wb.worksheets:
    for row_ in ws.iter_rows():
        for c in row_:
            if c.font is None or c.font.name != "Arial":
                f = c.font
                c.font = Font(name="Arial", size=f.size if f and f.size else 10, bold=f.bold if f else False,
                              color=f.color if f else None)

wb.save(OUT)
print("saved", OUT)
print("Summary rows", SUMR, SL)
