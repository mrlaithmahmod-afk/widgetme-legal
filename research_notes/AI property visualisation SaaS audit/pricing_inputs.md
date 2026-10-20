# Pricing Inputs for AI Property Visualisation SaaS: Unit Economics (checked 20 October 2026)

All prices were checked on **2026-10-20** unless the line says otherwise. Prices are in USD unless marked £. They are list or pay-as-you-go rates and exclude VAT. Conversions to GBP use **1 USD = £0.755** (see the FX section). "ESTIMATE" marks any figure that is not quoted directly from a vendor page. "UNVERIFIED" marks any figure that could not be confirmed on a primary page.

---

## 1. Anthropic Claude API: token prices, caching, batch and image tokens

### Takeaway
Claude Sonnet 5.5 costs $2/$10 per MTok and Opus 5.5 costs $4/$20 per MTok. Haiku 5.5 costs $0.10/$0.50 per MTok for prompts up to 100k tokens. Batch processing halves all of these. Cache reads cost 0.05x on Opus and Sonnet 5.5. A 4K floor-plan image costs about 1,560 tokens at standard resolution and about 4,784 tokens at high resolution. Reading one plan therefore costs about 1–2 cents on Opus, so LLM spend is negligible next to image and video generation.

### Cited Findings
- Claude Opus 5.5: $4 input / $20 output per MTok. Claude Sonnet 5.5: $2 / $10. Claude Haiku 5.5: $0.10 input / $0.50 output per MTok for prompts up to 100k tokens, and $0.50 / $2.50 above 100k. Claude Fable 5.1 (top tier): $10 / $50. — [Claude pricing docs](https://platform.claude.com/docs/en/about-claude/pricing)
- Prompt caching: a 5-minute cache write costs 1.25x the base input price (Opus $5, Sonnet $2.50, Haiku $0.125 per MTok). A 1-hour write costs 2x (Opus $8, Sonnet $4, Haiku $0.20). A cache read costs 0.05x on Opus 5.5 ($0.20) and Sonnet 5.5 ($0.10), and $0.01/MTok on Haiku 5.5 for prompts up to 100k. — [Claude pricing docs](https://platform.claude.com/docs/en/about-claude/pricing)
- Batch API: 50% off input and output. Opus 5.5 batch is $2/$10, Sonnet 5.5 $1/$5, Haiku 5.5 $0.05/$0.25. — [Claude pricing docs](https://platform.claude.com/docs/en/about-claude/pricing)
- Image tokens = ⌈width/28⌉ × ⌈height/28⌉. The maximum image size is 8000×8000 px. Examples: 1000×1000 = 1,296 tokens; 1920×1080 = 1,560 (standard) or 2,691 (high-res); 3840×2160 = 1,560 (standard) or 4,784 (high-res). The docs say 4,784 tokens cost "about $19.14 per thousand images" on Opus 5.5. — [Claude Vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)
- The vision page still uses "Claude Haiku 4.5's $1 per million input tokens" as a worked example. That conflicts with the $0.10/MTok Haiku 5.5 price on the pricing page, so the two pages differ by model generation. — [Claude Vision docs](https://platform.claude.com/docs/en/build-with-claude/vision) vs [pricing](https://platform.claude.com/docs/en/about-claude/pricing)

### Inferences
- **ESTIMATE, cost to parse one floor plan.** Assume one high-res 4K plan image (4,784 tokens), a 6k-token system prompt and a 3k-token structured JSON output. On Sonnet 5.5 that is about (10.8k × $2 + 3k × $10)/1e6 ≈ **$0.052 (£0.04)**. With the system prompt cached it is about $0.04. On Opus 5.5 it is about $0.10 (£0.08). Through the Batch API it is about $0.026 on Sonnet.
- **ESTIMATE, QA vision pass per generated image.** One Haiku 5.5 pass costs about 2k tokens in and 300 out, which is under $0.001. A Sonnet 5.5 pass costs about $0.007.
- **ESTIMATE, orchestration per room image.** This covers prompting plus QA of 2–3 candidates and comes to about **$0.02–0.05** on Sonnet 5.5.

### Gaps
- The pages give no separate PDF page-token rule. The safe assumption is that a PDF page costs image tokens for the rendered page plus its text tokens.

---

## 2. OpenAI: GPT-5.x, gpt-image and Sora

### Takeaway
GPT-5.x vision models range from $0.20 to $5 per MTok input. gpt-image-2 per-image list prices run $0.005–$0.211, with high quality at $0.165–$0.211. The Sora 2 and Videos API **shut down on 24 Sep 2026**, so OpenAI has no video option.

### Cited Findings
- GPT text models, short context, per 1M tokens (input / cached input / output):
  - gpt-5.6-sol: $4 / $0.40 / $20
  - gpt-5.6-terra: $2 / $0.20 / $12
  - gpt-5.6-luna: $0.20 / $0.02 / $1.20
  - gpt-5.5: $5 / $0.50 / $30
  - gpt-5.4: $2.50 / $0.25 / $15
  - gpt-5.4-mini: $0.75 / $0.075 / $4.50
  - gpt-5-mini: $0.25 / $0.025 / $2
  - gpt-5-nano: $0.05 / $0.005 / $0.40

  — [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- gpt-image-2 token rates: image input $8, cached image input $2, image output $30 per 1M tokens. — [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- Per-image costs from the legacy table:

  | Model | Low (1024² / 1024×1536 / 1536×1024) | Medium | High |
  |---|---|---|---|
  | GPT Image 2 | $0.006 / $0.005 / $0.005 | $0.053 / $0.041 / $0.041 | $0.211 / $0.165 / $0.165 |
  | GPT Image 1.5 | $0.009 / $0.013 / $0.013 | $0.034 / $0.05 / $0.05 | $0.133 / $0.20 / $0.20 |
  | GPT Image 1 Mini | — | — | $0.036–$0.052 |

  The newer gpt-image-2.5 "sunburst"/"flare" models use the same token rates. They add xhigh and max quality levels, but the guide publishes no per-image table for them. — [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- Sora 2 cost $0.10/s at 720p. Sora 2 Pro cost $0.30/s at 720p, $0.50/s at 1024×1792 and $0.70/s at 1080p. The page states: "The Sora 2 models and Videos API were shut down on September 24, 2026… no one-to-one replacement." — [OpenAI Sora 2 model page](https://developers.openai.com/api/docs/models/sora-2)

### Inferences
- The OpenAI image option for a landscape room image is about **$0.165 (£0.125)** at gpt-image-2 high. 4K output would need an upscale step.
- OpenAI video is not available for the cost model.

### Gaps
- No per-image prices are published for gpt-image-2.5 at xhigh or max quality. These are UNVERIFIED and appear only in an interactive calculator.

---

## 3. Google: Gemini, Nano Banana image models, Imagen and Veo

### Takeaway
Google's image models give the best quality-to-cost ratio for 4K stills. Gemini 3 Pro Image (Nano Banana Pro) costs $0.134 per 1K/2K image and $0.24 per 4K image. Nano Banana 2.1 costs $0.113 per 4K image. Veo 3.1 costs $0.40/s (Standard, with audio, 720p/1080p), $0.12/s (Fast, 1080p) and $0.08/s (Lite, 1080p). **Several Gemini text prices double on 1 Dec 2026 or 1 Jan 2027.**

### Cited Findings
- Text models, paid tier, per 1M tokens:
  - Gemini 4 Argon: $2 in / $10 out until 30 Nov 2026, then **$4 / $20 from 1 Dec 2026**
  - Gemini 3.8 Flash and 3.6 Flash: $0.75 / $3.75 until 31 Dec 2026, then **$1.50 / $7.50 from 1 Jan 2027**
  - Gemini 3.1 Pro Preview: $2 / $12 (≤200k tokens)
  - Gemini 3 Flash Preview: $0.50 / $3
  - Gemini 2.5 Pro: $1.25 / $10
  - Gemini 2.5 Flash: $0.30 / $2.50

  — [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- Image models (per-image equivalents):

  | Model | Output price | Per image |
  |---|---|---|
  | Gemini 3 Pro Image (Nano Banana Pro) | $120/M tokens | $0.134 (1K/2K), $0.24 (4K) |
  | Gemini 3.1 Flash Image (Nano Banana 2) | — | $0.045 (0.5K), $0.067 (1K), $0.101 (2K), $0.151 (4K) |
  | Gemini Nano Banana 2.1 | $30/M tokens | $0.0336 (1K), $0.0504 (2K), $0.113 (4K) |
  | Gemini 3.1 Flash Lite Image | — | $0.0336 (1K) |
  | Gemini 2.5 Flash Image | — | $0.039 (≤1024px) |

  — [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- Veo 3.1 per second, with audio (the default):

  | Tier | 720p | 1080p | 4K |
  |---|---|---|---|
  | Standard | $0.40 | $0.40 | $0.60 |
  | Fast | $0.10 | $0.12 | $0.30 |
  | Lite | $0.05 | $0.08 | not supported |

  — [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- Runway resells Veo 3.1 at 40 credits/s with audio ($0.40/s) or 20 credits/s without audio ($0.20/s). Veo 3.1 Fast is 15 credits/s with audio or 10 credits/s without. That suggests Google's no-audio price is about half the audio price. — [Runway API pricing](https://docs.dev.runwayml.com/guides/pricing/)

### Inferences
- Unit cost for a 4K photoreal room image on Nano Banana Pro is **$0.24 (£0.18)**. On Nano Banana 2.1 it is **$0.113 (£0.085)**.
- Unit cost for a 30-second clip on Veo 3.1 Standard 1080p is $12 (£9.06). On Veo 3.1 Fast 1080p it is $3.60 (£2.72).
- Any model built on Gemini 4 Argon or 3.x Flash should use the post-increase prices.

### Gaps
- Imagen 4 per-image prices are UNVERIFIED. They do not appear on the Gemini API page, and the Vertex AI pricing page would not render. ESTIMATE, from prior knowledge: about $0.02 (Fast), $0.04 (Standard) and $0.06 (Ultra) per image. Re-check before use.
- Veo prices without audio are not shown on the Gemini page.

---

## 4. Other image and video APIs: FLUX/BFL, fal.ai, Runway, Kling, Luma, Stability

### Takeaway
Image prices run from about $0.005 to $0.15 per image. Video prices run from about $0.04 to $0.42 per second at 4K. Kling 3.0 and Veo Fast are the cheapest credible 1080p options at about $0.11–0.14/s. Runway Gen-4.5 costs $0.12/s.

### Cited Findings
- **BFL (FLUX):** the calculator shows "$0.048 / image" but does not tie it to a model. Self-hosted licence tiers list only volumes: Builder 10K images/month, Platform 100K/month and Professional 100K/month. Enterprise is priced through sales. No licence fees are shown, so licence costs are **UNVERIFIED**. — [BFL pricing](https://bfl.ai/pricing)
- **fal.ai image models:**
  - FLUX 2: $0.012/MP
  - FLUX 2 Flash: $0.005/MP
  - Flux 3 Image: $0.048/MP
  - FLUX.1 [dev]: $0.025/MP
  - Nano Banana 2: $0.08/image
  - Nano Banana Pro: $0.15/image
  - Seedream 5.0 Pro: $0.135/image
  - Seedream V4.5: $0.04/image
  - SeedVR2 upscale: $0.001/MP

  — [fal.ai pricing](https://fal.ai/pricing)
- **fal.ai video models:**
  - Kling Video v3 Pro/Standard: $0.14/s
  - Kling O3: $0.14/s
  - Kling v2.6: $0.07/s
  - MiniMax H3 Max: $0.05/s
  - PixVerse V6: $0.005/s
  - Seedance 2.0 Fast: $0.0112 per 1,000 tokens (about $1.21 per video)

  — [fal.ai pricing](https://fal.ai/pricing)
- **fal.ai GPUs, list price (low price in brackets):** H100 $4.50/h ($2.49), H200 $6.00/h, B200 $7.99/h, RTX PRO 6000 $4.00/h ($1.99). — [fal.ai pricing](https://fal.ai/pricing)
- **Runway API:** 1 credit = $0.01.
  - Video: gen4_turbo 5 credits/s ($0.05/s), gen4.5 12 credits/s ($0.12/s), aleph2 28 credits/s ($0.28/s, 56-credit minimum)
  - Images: gen4_image 5 credits (720p) or 8 credits (1080p); gemini_image3_pro 20 credits (1K/2K) or 40 credits (4K); nano_banana_2.1 4, 6 or 12 credits

  — [Runway API pricing](https://docs.dev.runwayml.com/guides/pricing/)
- **Kling API, per second (1 unit = $0.14):**
  - Kling 3.0, no audio: $0.084 (720p), $0.112 (1080p), $0.42 (4K)
  - Kling 3.0, with audio: $0.126 (720p), $0.168 (1080p)
  - Kling 3.0 Turbo, with audio: $0.112 (720p), $0.14 (1080p)
  - Kling 2.5 Turbo / 2.6, no audio: $0.042 (720p), $0.07 (1080p)

  — [Kling API pricing (video)](https://kling.ai/document-api/pricing/base/video.md)
- **Luma API, Ray 3.2 SDR:** text- or image-to-video costs $0.15 / $0.30 / $1.20 per 5 s at 540p / 720p / 1080p, and $0.45 / $0.90 / $3.60 per 10 s. HDR costs 2x and HDR+EXR 3x. Billing is per 5-second block. — [Luma API](https://lumalabs.ai/api); [Luma Agents pricing docs](https://docs.agents.lumalabs.ai/guides/pricing/)
- **Stability AI:** the Community licence is free for businesses under $1M annual revenue. Enterprise (over $1M) is "Custom Pricing". The licence page shows no API credit price. — [Stability AI licence](https://stability.ai/license)

### Inferences
- 1080p video cost per second, cheapest to dearest: Kling 2.6 at $0.07, Veo 3.1 Lite at $0.08, Kling 3.0 at $0.112, Veo Fast at $0.12, Runway Gen-4.5 at $0.12, Luma Ray 3.2 at $0.24 (5 s blocks), Veo Standard at $0.40.
- 4K FLUX output on fal (3840×2160 = 8.3 MP) is about $0.10 on FLUX 2 or $0.04 on FLUX 2 Flash.

### Gaps
- The BFL self-host licence fee is not public.
- Stability Enterprise pricing is not public.

---

## 5. GPU compute and rendering (Blender, Unreal), benchmarks and render farms

### Takeaway
An RTX 4090 rents for $0.89/h on RunPod. An L4 costs $0.59/h on RunPod or about $0.805/h on AWS g6.xlarge. An L40S costs $1.09/h on RunPod or about $1.861/h on AWS g6e.xlarge. In Blender Cycles the 4090 is about 47% faster than the L40S. A 4K production interior frame probably costs **$0.05–0.30 of GPU time** (ESTIMATE), but a full Cycles walkthrough runs to tens of dollars.

### Cited Findings
- **RunPod on-demand** (Community and Secure Cloud priced the same):
  - RTX 4090: $0.89/h
  - RTX 5090: $1.19/h
  - L4: $0.59/h
  - A40: $0.59/h
  - RTX A6000: $0.59/h
  - L40S: $1.09/h
  - H100 PCIe: $2.89/h; H100 SXM: $3.99/h

  — [RunPod pricing](https://www.runpod.io/pricing)
- **Lambda, per GPU-hour:** A10 (24 GB) $1.29, A6000 $1.09, A100 40 GB $1.99, H100 SXM $3.99–4.29, H100 PCIe $3.29, B200 $6.69–6.99, GH200 $2.29. — [Lambda pricing](https://lambda.ai/pricing)
- **AWS g6.xlarge** (1× L4, 24 GB): on-demand Linux "starting at $0.8048/h", spot $0.645/h. **AWS g6e.xlarge** (1× L40S, 48 GB): $1.861/h. The source is an aggregator, the region is unspecified and probably us-east-1. AWS's own page links out to the EC2 pricing page instead of listing prices. — [Vantage g6.xlarge](https://instances.vantage.sh/aws/ec2/g6.xlarge); [Vantage g6e.xlarge](https://instances.vantage.sh/aws/ec2/g6e.xlarge); [AWS G6 page](https://aws.amazon.com/ec2/instance-types/g6/)
- **Blender benchmark scores** (Renderjuice, which aggregates Blender Open Data): RTX 4090 scores 11,573–11,592 on Blender 5.2.0 with OptiX. L40S scores 7,848 (Blender 4.5), making the 4090 47.5% faster.
- **Seconds per benchmark frame on an RTX 4090:** Junkshop 4.83 s, Monster 3.53 s, Classroom 7.43 s. On an L40S: Junkshop 9.10 s, Monster 4.54 s. These runs use 240–300 samples at benchmark resolution. — [Renderjuice L40S vs 4090](https://www.renderjuice.com/gpus/compare/l40s-vs-rtx-4090); [Renderjuice RTX 4090](https://www.renderjuice.com/gpus/rtx-4090-for-blender)
- iRender rendered an official Blender demo file at **4K** in 30.40 s on one GPU, 18.19 s on two and 16 s on four. Multi-GPU scaling in Cycles is poor, so running one job per GPU is more efficient. This is a vendor video. — [iRender (YouTube)](https://www.youtube.com/watch?v=9Ru4bh_DQ6c)
- Blender Open Data's own site references Blender 5.2.0. Its score tables load dynamically and could not be extracted. — [Blender Open Data](https://opendata.blender.org/)
- **GarageFarm render farm:**
  - GPU: $0.004 (Low), $0.006 (Medium) or $0.012 (High) per OctaneBench-hour
  - CPU: $0.024, $0.036 or $0.072 per GHz-hour
  - GPU nodes: $3.22–$25.76/h
  - Example: 50 frames × 1 h × $1.50 = $75. No per-frame Cycles price is published.

  — [GarageFarm pricing](https://garagefarm.net/pricing)

### Inferences (ESTIMATES)
- **4K photoreal Cycles interior still** (1,024–2,048 samples plus denoise): about 2–10 min on an RTX 4090. At $0.89/h that is **$0.03–0.15 per frame**, or about $0.06–0.30 on an L4 or L40S. This assumes the scene is already built. Modelling and asset setup dominate real cost.
- **30 s walkthrough in Cycles** (900 frames at 30 fps, 1080p, about 30–60 s/frame on a 4090): 7.5–15 GPU-hours, or about **$7–13** on RunPod. At 4K, multiply by roughly 3–4.
- **30 s walkthrough in Unreal Movie Render Queue** (about 1–5 s/frame): under 1.5 GPU-hours, or about **$1** of compute.
- **60 s cinematic** (1,800 frames): roughly twice the 30 s figures, so about $14–26 in Cycles at 1080p or about $2 in Unreal.

### Gaps
- No primary Blender Open Data median figures were extracted for the L4 or A10.
- RebusFarm (its pricing URL returned 404) and Fox Renderfarm per-frame rates are **UNVERIFIED**.
- Prices for Vast.ai, CoreWeave, GCP and Azure GPUs were not fetched because of tool rate limits. Vast.ai 4090 marketplace rates are typically about $0.3–0.5/h (ESTIMATE, UNVERIFIED).

---

## 6. Interactive 3D hosting: Unreal pixel streaming per concurrent user-hour

### Takeaway
Pixel streaming costs about **$0.16–$2.82 per concurrent-user-hour**. A typical Unreal archviz app needs a full L4-class GPU per user, which costs about $1.8–2.8 per hour. A 10-minute viewer session therefore costs about **$0.30–0.47 (£0.23–0.35)**, and the service carries fixed per-app fees on top.

### Cited Findings
- **AWS GameLift Streams** bills per second for allocated capacity, whether it is idle or in use.
  - gen4n_high (T4): $0.4982 per capacity-hour in Oregon, $0.6571 in Frankfurt
  - gen6n_ultra_win2022 (L4, one session per GPU, supports UE up to 5.6): $1.82 per capacity-hour in Oregon
  - gen6n_small: $0.16/h in Ohio, with up to 12 sessions per GPU

  — [GameLift Streams pricing](https://aws.amazon.com/gamelift/streams/pricing/); [Gen6 launch](https://aws.amazon.com/about-aws/whats-new/2025/12/aws-gameliftstream-gen6-enhanced-autoscaling/); [stream classes](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-groups.html)
- **Vagon Streams**, billed per minute:
  - L4 Starter G3: $0.036/min ($2.16/h)
  - L4 Pro G3: $0.047/min ($2.82/h)
  - A10G: $0.036–0.046/min
  - T4: $0.025–0.035/min
  - Application maintenance: $0.67/day per region (about $20/month)

  — [Vagon Streams pricing](https://vagon.io/streams/pricing)
- **Arcware:** "Core €89 a month plus up to €0.10 a minute". **Eagle 3D:** Core $29/month including 300 minutes, then $0.10/min. Both come from a third-party comparison dated 9 Oct 2026. Arcware's own page returned a 503 error, so this is **UNVERIFIED at the primary source**. — [SimplyStream calculator](https://simplystream.com/calculator)

### Inferences
- **ESTIMATE, one interactive 3D property.** Assume 100 viewer sessions a month at 8 minutes each, which is 13.3 user-hours. On GameLift gen6n_ultra that costs about $24/month. On Vagon Pro G3 it costs about $38/month plus $20 maintenance. If idle capacity is kept warm, costs rise sharply.
- A WebGL, three.js or Gaussian-splat viewer served from R2 or a CDN costs almost nothing per view. That makes it a strong alternative to pixel streaming for gross margin.

### Gaps
- PureWeb pricing was not found.
- GameLift storage per GB-month was not shown on the page.

---

## 7. Storage and CDN

### Takeaway
Storage and delivery are negligible per property. Cloudflare R2 costs $0.015/GB-month with free egress. Bunny CDN costs $0.01/GB in Europe and North America. Mux and Cloudflare Stream cost about $0.001 per minute delivered.

### Cited Findings
- **Cloudflare R2:** Standard storage $0.015/GB-month (Infrequent Access $0.01). Class A operations cost $4.50 per million, Class B $0.36 per million. Egress is free. The free tier covers 10 GB, 1M Class A and 10M Class B operations. — [R2 pricing](https://developers.cloudflare.com/r2/pricing/)
- **Cloudflare Stream:** $5 per 1,000 minutes stored per month and $1 per 1,000 minutes delivered. Ingest and encoding are free. — [Stream pricing](https://developers.cloudflare.com/stream/pricing/)
- **Mux:** 1080p basic encoding is free (plus tier $0.03125/min). Storage costs $0.003/min/month and delivery $0.001/min, with 100,000 delivery minutes free each month. 2K and 4K tiers cost more but are not quoted. — [Mux pricing](https://www.mux.com/pricing)
- **Bunny CDN:** $0.01/GB in Europe and North America, or $0.005/GB on the volume network for the first 500 TB. Minimum charge is $1/month. — [Bunny pricing](https://bunny.net/pricing/)

### Inferences
- **ESTIMATE, storage for a 4-bed house package.** Assume about 40 × 4K images at 15 MB, plus two 1080p videos (about 300 MB) and source scenes (about 2 GB), for roughly 3 GB in total. Storage costs about $0.045/month on R2. Delivering 1,000 video plays of 60 s costs about $1 on Stream or Mux.

### Gaps
- AWS S3 London pricing was not fetched. The usual figure is about $0.024/GB-month plus egress (UNVERIFIED).
- Cloudflare Images pricing was not fetched.

---

## 8. CAD/BIM conversion and floor-plan vectorisation

### Takeaway
APS Model Derivative pricing is token-based. One Flex token costs $3.00 at list price. The Flex page still says 0.5 tokens per complex job and 1 token per simple job, but APS announced price increases in December 2025, so treat **about $1.50–$3 or more per translation as UNVERIFIED**. Getfloorplan's AI 2D/3D floor-plan sets cost $25–$115 per plan.

### Cited Findings
- **Flex token list price:** $3.00 each up to 4,999 tokens, falling to $2.40 at 250k or more. The Flex page lists Model Derivative API at "0.5 token per complex job, 1 token per simple job", Automation API at 2 tokens per processing hour and Reality Capture at 1 token per 50 photos. Viewer and Data Management are free. — [Autodesk Flex](https://www.autodesk.com/buying/flex)
- **APS business model change** (effective 8 Dec 2025): APS added Free, Prepay (Flex) and Pay-as-you-go tiers. "Pricing for the Model Derivative API and Automation API for Revit, AutoCAD, and Inventor will increase." Basic interactions cost 1 token per 300,000 API calls. The minimum Flex purchase is 100 tokens, and tokens expire after one year. The exact new rate chart is an image that could not be read. — [APS blog](https://aps.autodesk.com/blog/aps-business-model-evolution)
- **Getfloorplan:** Basic set (2D + 3D) $25, Plus (with 360 tour) $45, Pro $61, Max Render $69, Multi Set Pro $115. An API is available. — [Getfloorplan pricing](https://getfloorplan.com/pricing)

### Inferences
- If the platform translates customer DWG or RVT files through APS, budget about **$1.50–$3 per file (ESTIMATE)** until the new rate chart is confirmed. Using the free tier in early stages may cover pilot volumes.

### Gaps
- No ODA (Open Design Alliance) membership fees were found.
- No CubiCasa or Archilogic API prices were found, which suggests they are sales-led.
- The current APS free-tier monthly limits are UNVERIFIED.

---

## 9. Payments and infrastructure overheads

### Takeaway
Stripe UK charges 1.5% + 20p on standard UK cards, plus 0.7% for Billing. WorkOS SSO costs **$125 per connection per month** for the first 15 connections. Clerk enterprise SSO costs $75/month per extra connection. Vercel Pro costs $20 per seat per month.

### Cited Findings
- **Stripe UK:**
  - Standard UK cards: 1.5% + 20p
  - Premium UK cards: 2.8% + 20p
  - EEA cards: 2.5% + 20p
  - International cards: 3.15% + 20p, plus 2% for FX
  - Stripe Billing: 0.7% of billing volume
  - Stripe Tax: 0.5% per transaction
  - Invoicing: 0.4%
  - Bacs Direct Debit: 1% (minimum 20p, cap £4)

  — [Stripe UK pricing](https://stripe.com/gb/pricing)
- **WorkOS SSO, per connection:** $125 each for 1–15, $100 for 16–30, $80 for 31–50, $65 for 51–100, custom above 100. Directory Sync is priced the same. AuthKit is free up to 1M MAU. Audit-log streaming costs $125/month per SIEM. — [WorkOS pricing](https://workos.com/pricing)
- **Clerk:**
  - Free up to 50,000 monthly retained users per app
  - Pro: $25/month, or $20/month billed annually
  - Overage: $0.02 per retained user above 50k
  - One enterprise SSO connection included; extras cost $75/month each (2–15) or $60 (16–100)
  - B2B Enhanced add-on: $100/month

  — [Clerk pricing](https://clerk.com/pricing)
- **Vercel Pro:** $20/month per developer seat, including $20 of usage credit and 1 TB transfer. Extra transfer starts at $0.15/GB. Fluid Active CPU starts at $0.128/h. — [Vercel pricing](https://vercel.com/pricing)

### Inferences
- **ESTIMATE, payment cost on a £2,500 developer package paid by UK card on Billing:** 1.5% + 20p + 0.7% ≈ **£55.20 (2.2%)**. Paid by Bacs it costs £4 plus 0.7%.
- WorkOS SSO is a fixed **$125/month (about £94) per enterprise customer**. Price it into enterprise tiers or pass it through. Clerk is cheaper at $75 per connection.

### Gaps
- Pricing for Sentry, Fly.io, Render and Auth0 was not fetched, so these are UNVERIFIED. They are small fixed costs, typically $0–$100/month at early stage (ESTIMATE).

---

## 10. USD to GBP exchange rate

### Takeaway
Use **£0.755 per USD**, which is about $1.324 per £1.

### Cited Findings
- X-Rates monthly averages, GBP per USD: Sep 2026 0.745193; Oct 2026 0.755183 (based on 20 days); Aug 2026 0.738648. The page header carries an inconsistent timestamp ("Jan 01, 2026"), so cross-check against the BoE or ECB rate. — [X-Rates USD/GBP 2026 averages](https://www.x-rates.com/average/?from=USD&to=GBP&amount=1&year=2026)

### Gaps
- The Bank of England spot rate for mid-October 2026 was not separately verified.

---

## 11. Human labour and UK CGI market benchmarks

### Takeaway
UK studio list prices start at about **£245–£700 per interior still**, **£295–£1,000 or more per exterior**, and **£1,495–£3,500 for a 30-second walkthrough**. Floor-plan redraws cost **£4.75–£70 per plan**, and £15.80–£395 for 3D plans. Offshore artists on Upwork charge a median of about $20–30/h, with listings from $5 to $15/h.

### Cited Findings
- **3DAV (UK), ex VAT:** exterior £295 (Starter) or £595 (Growth); interior £245 or £495; 2D or 3D floor plan £195 or £395; walkthrough £1,495 (up to 30 s) or £2,995 (up to 90 s). — [3DAV pricing](https://www.3darchitecturevisualization.co.uk/pricing.html)
- **100CGI (London):** interior stills £550 (small), £700 (medium) or £800 (large); exterior from £1,000; walkthrough £2,500 for 60 s plus £1,000 per extra 30 s; 3D tour £1,500 including 5,000 sqft; retainer from £0.51/sqft. The 3D scene build is quoted separately. — [100CGI price list](https://100cgi.com/price-list/)
- **Shakworks (London):** exterior from £350, interior from £450, 30 s animation from £3,500, aerial view from £1,500. — [Shakworks](https://www.shakworks.com/architectural-visualisation-services)
- **HyRez (UK):** exterior house type from £750; apartment exterior from £1,000; interior with design scheme from £1,500; whole-development animation from £5,000. — [HyRez services](https://hyrez.uk/services)
- **Real Render 3D (UK):** exterior £345, interior £245, flythrough £2,295, 60 s video £1,650. — [Real Render 3D](https://www.realrender3d.co.uk/)
- **Monolith Visuals (UK), Tier 3 with no existing 3D model:** interior £643.50 (small), £910 (medium) or £1,222 (large); exterior £845, £980 or £1,430. — [Monolith Visuals](https://www.monolithvisuals.com/)
- **UK floor-plan redraw services:**
  - Sketch2Plan: £5 + VAT per plan
  - VizCraft: 2D B&W from £4.75, 3D from £15.80, 3D CGI from £35.50
  - Elements Property: £6.95 (1–2 bed), £8.95 (3–4 bed)
  - Fenridge: 2D £30, colour £60, 3D £90
  - House Plan Direct: £40 for up to 3 rooms
  - Floor Plans UK: £70 (1 floor), £110 (2 floors), £150 (3 floors)
  - dijitul: £45/h + VAT

  — [Sketch2Plan](https://www.sketch2plan.com/); [VizCraft](https://vizcraft.biz/floor-plans); [Elements Property](https://elementsproperty.co.uk/floorplan-conversion/); [Fenridge](https://fenridge.co.uk/estate-agents/); [House Plan Direct](https://houseplandirect.com/estate-agent-floor-plans); [Floor Plans UK](https://floorplansuk.com/); [dijitul](https://dijitulmedia.co.uk/floor-plans/)
- **Upwork:** median architectural rendering specialist rate is $20–30/h. Typical project prices: exterior $160–450, interior $160–400, 3D floor-plan set $100–360, 30–60 s walkthrough $600–1,800. Example profiles charge $5/h (Pakistan), $12/h and $15/h (Vietnam). Upwork's 3D rendering artist page gives $25–40/h. — [Upwork architectural rendering cost](https://www.upwork.com/hire/architectural-rendering-freelancers/cost/); [Upwork 3D rendering artists](https://www.upwork.com/hire/3d-rendering-artists/); [Upwork architectural rendering profiles](https://www.upwork.com/hire/architectural-rendering-freelancers/)

### Inferences
- **ESTIMATE, human-in-the-loop QA and fix-up:** 10–20 minutes per plan at an offshore $15–25/h costs about **$2.50–8 (£2–6) per floor-plan type**. A full offshore redraw costs £5–£10 per plan at UK redraw-service prices.

### Gaps
- No PeoplePerHour data or formal UK salary survey for 3D artists was obtained.

---

## 12. Per-unit cost assumptions for each deliverable (all ESTIMATES built from the cited prices)

Assumptions:
- Each accepted 4K room image needs 3 generation attempts. The base model is Nano Banana Pro 4K ($0.24); the low case is Nano Banana 2.1 4K ($0.113).
- Claude Sonnet 5.5 parses each plan once for $0.05 and runs QA and orchestration for $0.03 per image.
- Storage and CDN are treated as zero (under $0.05).
- FX is £0.755 per USD.
- No human QA is included unless stated.

| Deliverable | Composition | AI/API cost (base) | Low case | Notes |
|---|---|---|---|---|
| 1 photoreal room image | plan parse + 3 × $0.24 + QA | about **$0.80 (£0.60)** | about $0.40 (£0.30) | gpt-image-2 high: about $0.55 |
| 5 room images | parse + 5 × (3 × $0.24) + QA | about **$3.80 (£2.87)** | about $1.80 | |
| 2-bed flat (about 8 images: living, kitchen, 2 beds, bath, hall, 2 alternates, plus 2D/3D plan) | parse $0.05 + 8 × $0.75 + QA | about **$6.30 (£4.76)** | about $3 | add £2–6 human QA |
| 4-bed house (about 16 interior + 3 exterior images + plans) | 19 × $0.75 + parse $0.10 | about **$14.50 (£10.95)** | about $7 | |
| Interactive 3D property | scene build on GPU (about 1 h L40S, $1.09–1.86) + streaming 13 user-hours/month at $1.82 | about **$2 one-off + about $24/month** | WebGL/splat about $0 per view | Vagon adds about $20/month per app |
| 30 s walkthrough video | AI: 6 × 5 s clips with 2× retakes = 60 s billed. Veo Fast 1080p: $7.20; Kling 3.0: $6.72; Veo Std: $24 | about **$7 (£5.30)** | about $4 (Kling 2.6) | Unreal render about $1; Cycles about $7–13 |
| 60 s cinematic | 120 s billed (2× retakes) at Veo 3.1 Std 1080p $0.40/s | about **$48 (£36)** | about $14 (Veo Fast) | 4K Veo Std at $0.60/s: $72 |
| Full developer marketing package (house type: 20 stills + 2 exteriors + 30 s + 60 s + 3D tour) | 22 × $0.75 + $7 + $48 + $2 | about **$75 (£57)** plus hosting | about $30 | UK studio equivalent about £10k–£20k |
| 50-unit development (e.g. 6 floor-plan types) | 6 × house-type package + 50 × (1 plan render + 2 finish swaps × $0.75) | about **$560 (£420)** | about $250 | cost scales with plan types, not units |
| 200-unit development (e.g. 15 types) | 15 × package + 200 × $2.25 | about **$1,575 (£1,190)** | about $700 | add SSO $125/month if enterprise |

### Inferences
- Variable AI cost per deliverable is small: about £1–£60 per property package, against UK studio prices of £245–£1,500 per still. Gross margin is therefore driven by retake rates, human QA minutes, 3D streaming hours and fixed overheads such as WorkOS SSO and Stripe fees, not by model token prices.
- The biggest pricing risks are:
  1. The Gemini price rises on 1 Dec 2026 and 1 Jan 2027 (text only so far).
  2. Vendor model churn, such as Sora being shut down on 24 Sep 2026.
  3. Unconfirmed APS translation rates.
  4. Pixel streaming costs if capacity is kept warm.

### Gaps
- The retake multiplier (3x for images, 2x for video) and the human QA minutes are ESTIMATES. They should be replaced with measured pilot data.
