# Legal, contractual and marketing-compliance constraints on an AI-powered white-label property visualisation SaaS (UK first; then UAE, KSA, EU, US) — as of 20 October 2026

Scope note: these are research notes, not legal advice. Each finding is tagged **[LAW]** (statute or case law), **[GUIDANCE]** (regulator or industry-body guidance or code), **[PLATFORM]** (contract terms or policy of a vendor or portal) or **[SECONDARY]** (law-firm or commentary source). Points that need a solicitor are marked **[SOLICITOR]**. Points I could not verify against a primary source are marked **[UNVERIFIED]**.

---

## 1. Upstream AI provider terms (Anthropic, OpenAI, Google Gemini/Vertex/Veo, Black Forest Labs FLUX, Stability AI, Runway)

### Takeaway
None of the providers whose terms I checked forbids white-labelling, and the business/API tiers of Anthropic, OpenAI and Google (paid) all say they will not train on customer content and that the customer owns the outputs. The real constraints are elsewhere:
- **Model and tier choice.** FLUX [dev] open weights and Stability above US$1M revenue need paid commercial licences. Runway trains on your inputs and outputs and gives no indemnity. Gemini's free tier trains on your data outside the EEA, UK and Switzerland.
- **Flow-down duties.** The provider's AUP/Usage Policy has to be passed down to your customers, Anthropic requires an "outputs may be inaccurate" notice to users, and any interactive assistant must disclose that it is AI.
- **Watermarks.** Google media models apply SynthID and Content Credentials automatically, and these cannot be switched off.
- **Data residency.** Anthropic's first-party API offers only "global" or "us" inference. EU in-region processing for Claude has to go through Bedrock EU or Vertex EU endpoints.

### Cited Findings
**Anthropic**
- [PLATFORM] Under the commercial terms for Claude via third-party hosts, Anthropic agrees that the customer owns all outputs and assigns to it any right it has in them. The terms also say "Anthropic may not train models on Customer Content from Services." — [Anthropic Commercial Terms (3P-hosted version, PDF)](https://assets.ctfassets.net/5965pury2lcm/4e9p7xwZDo6mBgWfSyDsCV/907c229ef3ee22366fa66837419bde2c/Anthropic_T_Cs.pdf); the same wording appears in [AWS Bedrock third-party model terms](https://aws.amazon.com/legal/bedrock/third-party-models/)
- [PLATFORM] The customer must use "reasonable efforts" to make sure its own customers and end users comply with the AUP. The customer "must notify its Users" that factual assertions in outputs should not be relied on without checking, and it is responsible for deciding whether human review is appropriate before sharing outputs. — [Anthropic Commercial Terms PDF](https://assets.ctfassets.net/5965pury2lcm/4e9p7xwZDo6mBgWfSyDsCV/907c229ef3ee22366fa66837419bde2c/Anthropic_T_Cs.pdf)
- [PLATFORM] The publicity clause says "Neither party may make public statements about Customer's use of the Services without the other party's permission." So naming Anthropic or Claude in marketing needs permission, and nothing in these terms requires naming Anthropic to end users. — [Anthropic Commercial Terms PDF](https://assets.ctfassets.net/5965pury2lcm/4e9p7xwZDo6mBgWfSyDsCV/907c229ef3ee22366fa66837419bde2c/Anthropic_T_Cs.pdf)
- [PLATFORM] Use is restricted to "countries and regions Anthropic currently supports", and building competing models is prohibited. — [Anthropic Commercial Terms PDF](https://assets.ctfassets.net/5965pury2lcm/4e9p7xwZDo6mBgWfSyDsCV/907c229ef3ee22366fa66837419bde2c/Anthropic_T_Cs.pdf)
- [PLATFORM] Usage Policy (2024 version, archived copy):
  - "All customer-facing chatbots including any external-facing or interactive AI agent" must disclose to users that they are interacting with an AI system.
  - "High-risk" use cases (which include housing-eligibility decisions and "media or professional journalistic content" auto-generated for publication) need human-in-the-loop review and disclosure that Anthropic's services are being used.
  - Property marketing visualisation is not obviously on the high-risk list.
  - Source: [Anthropic Usage Policy (archive, May 2024 version)](https://archive.ph/sinqA)
- [PLATFORM] Anthropic announced a 2026 Usage Policy update, effective 12 November 2026. — [Anthropic, 2026 Usage Policy update](https://www.anthropic.com/news/2026-usage-policy-update) **[UNVERIFIED: content of the changes not reviewed]**
- [PLATFORM] Anthropic says that for commercial customers it acts as processor, with the customer as controller, and that it does not train on commercial data unless the customer opts into the Development Partner Program. — [Anthropic Privacy Center](https://privacy.claude.com/en/articles/9267385-does-anthropic-act-as-a-data-processor-or-controller)
- [PLATFORM] Zero data retention (ZDR):
  - Available per organisation, subject to Anthropic's approval, via sales. Under ZDR, Anthropic "does not store customer prompts or responses at rest after the API response is returned".
  - User Safety classifier results are still kept.
  - Not covered: Batch API (29-day retention), Files API, code execution, MCP connector, Console.
  - Certain "Covered Models" (Claude Fable 5/5.1, Mythos 5/5.1) require 30-day retention and are not available under ZDR unless Anthropic expressly authorises it.
  - Sources: [Claude docs – API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention); [Anthropic Privacy Center – ZDR](https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to)
- [PLATFORM] Data residency on the first-party Claude API:
  - `inference_geo` takes only `"global"` (the default) or `"us"`. "Workspace geo" controls where data is stored at rest.
  - On Bedrock and Google Cloud, the region is set by the endpoint or inference profile instead.
  - Source: [Claude docs – Data residency](https://platform.claude.com/docs/en/manage-claude/data-residency)
  - Claude Platform on AWS likewise offers only US (1.1x price) and Global. — [AWS – Claude Platform data residency](https://docs.aws.amazon.com/claude-platform/latest/userguide/data-residency.html)
- [PLATFORM] Amazon Bedrock offers three routing options: In-Region (strictly one Region), Geographic cross-Region (including an EU geography: "prompts and outputs may move within the geography but not outside it") and Global. eu-west-2 (London) is a listed Region. AWS advises checking the destination Regions with GetInferenceProfile rather than relying on the prefix alone. — [AWS Bedrock – Regional availability](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html); [AWS Bedrock – inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
- [PLATFORM] Vertex AI offers regional, US/EU multi-region (GA from 15 May 2026) and global endpoints for Claude. The global endpoint has "No data residency guarantees". — [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/multi-region-endpoints-for-claude-available-on-vertex-ai)

**OpenAI**
- [PLATFORM] The customer retains its input and owns its output, and OpenAI assigns its rights in the output to the customer. OpenAI "will not use Customer Content to develop or improve the Services, unless Customer explicitly agrees". Output "may not be unique". The customer "may not resell or lease access to its Account". — [OpenAI Services Agreement](https://openai.com/policies/services-agreement/)
- [PLATFORM] IP indemnity covers claims that the Services infringe. The Service Terms extend it to claims that the customer's use or distribution of Output infringes. That extension is excluded where:
  - the customer knew or should have known of the infringement;
  - safety or filtering features were disabled;
  - output was "modified, transformed, or used in combination with products or services not provided by... OpenAI";
  - the customer lacked rights in the input; or
  - the claim is a trademark claim.
  - Sources: [OpenAI Services Agreement §13](https://openai.com/policies/services-agreement/); [OpenAI Service Terms](https://openai.com/policies/service-terms/)
- [PLATFORM] For Prompt-to-Voice, OpenAI requires that generated speech be disclosed as AI-generated and that "OpenAI-provided indicators of AI origin" not be removed, and the customer must flow these duties down to its End Users. — [OpenAI Service Terms](https://openai.com/policies/service-terms/)

**Google (Gemini API, Vertex AI, Veo)**
- [PLATFORM] On Gemini API Paid Services, Google "doesn't use your prompts ... or responses to improve our products". Prompts are logged for a limited period for abuse detection and "may be stored transiently or cached in any country". On Unpaid Services, Google uses content to improve its products and human reviewers may read it, except that EEA, Switzerland and UK users get the paid-tier data terms even on free services. — [Gemini API Additional Terms](https://ai.google.dev/gemini-api/terms)
- [PLATFORM] On Vertex AI, Generated Output is Customer Data and Google asserts no ownership of it. Google's indemnity extends to "unmodified Generated Output" from "Generative AI Indemnified Services". — [Google Cloud Service Specific Terms §20](https://cloud.google.com/terms/service-terms)
- [PLATFORM / SECONDARY] Veo on Vertex: "All images or videos created or modified using the listed models are automatically digitally signed by Google LLC" (Content Credentials). Flow outputs carry invisible SynthID marks. — documentation quoted in [adtestbench watermark dataset, citing docs.cloud.google.com content-credentials page](https://adtestbench.com/data/watermarks.csv) **[verify against Google's primary docs]**

**Black Forest Labs (FLUX)**
- [PLATFORM] Under the FLUX [dev] Non-Commercial License, use "for revenue-generating activity" or "in direct interactions with or that has impact on end users" is not a Non-Commercial Purpose. Outputs may be used commercially, but the licence conditions include content filtering or review and "disclosure (or other indication) that the Output was generated or modified using artificial intelligence". — [BFL Non-Commercial License](https://bfl.ai/legal/non-commercial-license-terms); [FLUX.2 licence on GitHub](https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL)
- [PLATFORM] The Self-Hosted Commercial License (revised 4 August 2026) lets you integrate FLUX [dev] into a "Customer Application". It prohibits exposing the model to third parties via an API endpoint or reselling it. — [BFL Self-Hosted Commercial License](https://bfl.ai/legal/self-hosted-commercial-license-terms)
- [PLATFORM] Usage through the BFL API includes full commercial rights. Self-hosting tiers include "Professional: Agencies and service providers ... up to 3 clients". FLUX.2 [klein] 4B is Apache 2.0. Training on FLUX outputs needs a separate Synthetic Data licence. — [BFL Knowledge Base – licensing](https://help.bfl.ai/articles/9272590838-self-serve-dev-license-overview-pricing)

**Stability AI**
- [PLATFORM] The Community License is free for commercial use below US$1M annual revenue "regardless of the source of that revenue". Above that threshold, an Enterprise licence is required. — [Stability AI License](https://stability.ai/license)

**Runway**
- [PLATFORM] Runway claims no ownership of inputs or outputs and does not restrict commercial use. However, "Inputs and Outputs may be used by the Company to train and improve its AI models", under a perpetual, irrevocable licence. — [Runway Terms of Use §4.4](https://runway.com/terms-of-use)
- [SECONDARY] Runway's indemnity runs from the user to Runway only, so there is no copyright indemnity for the user. Free-plan videos carry a Runway watermark; paid plans do not. — [Archibal summary](https://archibal.ai/models/google/veo-3-1/via-runway); [adtestbench dataset](https://adtestbench.com/data/watermarks.csv)

### Inferences
- White-labelling is permitted, but if the white-label product includes a chat or agent interface, end users must be told they are dealing with AI. That can be done under the customer's brand; Anthropic does not need to be named. Naming Anthropic in sales collateral needs its permission under the publicity clause.
- Customer uploads (floor plans, CAD, BIM) are customer content or confidential information under the Anthropic, OpenAI and Google paid terms. Runway's default terms are incompatible with promising enterprise customers "no training on your data" unless an enterprise agreement says otherwise. Free-tier Gemini is unsafe for non-EEA/UK customer data.
- For UK or EU residency claims, route Claude through Bedrock (In-Region eu-west-2 or the EU geo profile) or a Vertex EU endpoint. Do not use first-party `global`. Note that ZDR on Bedrock or Vertex depends on those hosts' own retention and abuse-logging terms.
- The OpenAI output indemnity is lost where output is "modified, transformed, or used in combination" with other products. A pipeline that composites, edits or upscales outputs will probably fall outside it. Do not promise customers indemnity cover that the upstream providers do not give you.
- Do not offer FLUX [dev] open weights or Stability models (once revenue passes US$1M) in production without a paid licence. Several licences (FLUX) and Google's tooling build in AI-disclosure or provenance marks. The product should keep these marks and must not let users strip them.

### Gaps
- I did not review the full current (2026) Anthropic Commercial Terms of Service on anthropic.com, or the text of the November 2026 Usage Policy update. In particular I have not verified the copyright-indemnity clause I recall from prior knowledge. **[UNVERIFIED]**
- I did not review OpenAI's sharing & publication policy, its EU data residency offer, or C2PA metadata on OpenAI images.
- I did not review Google's Prohibited Use Policy on removing SynthID.
- I did not review Runway Enterprise terms, which may differ.

---

## 2. Copyright: architectural drawings and plans, AI outputs (UK, US, EU)

### Takeaway
In the UK, architects' drawings and buildings are protected as artistic works, and copyright normally stays with the architect.
- A client who has paid is impliedly licensed to use the plans "for all purposes connected with the erection" of that building on that site. Commentary says this extends to marketing.
- The licence does not pass to a developer who did not acquire it through the chain (Signature Realty v Fortis, 2016), and plans downloaded from a planning portal carry restrictive licences.
- On AI outputs, the UK government's March 2026 report proposes removing s9(3) protection for computer-generated works, while keeping protection for AI-assisted works. The US Copyright Office says purely AI-generated material is not protectable.
- The platform therefore cannot assume it or its customer owns the plans or the outputs. It needs customer warranties about input rights, and it should treat output ownership as uncertain.

### Cited Findings
- [LAW] *Blair v Osborne & Tomkins* [1971] 2 QB 78 (CA):
  - The architect retains copyright, but "when the owner of a building plot employs an architect to prepare plans ... the architect impliedly promises that, in return for his fee, he will give a licence to the owner to use the plans for the building on that site".
  - The licence extends to builders and to a purchaser of the site, "but for no other purpose".
  - Passing off the architect's work as one's own was not licensed.
  - Source: [swarb summary of Blair](https://swarb.co.uk/c/ca/1970blair-osborne.html)
- [LAW] *Signature Realty Ltd v Fortis Developments Ltd* [2016] EWHC 3583 (Ch):
  - The developer infringed the architect's drawings by using them for "marketing the properties", for tendering, for altered versions, and for "making AutoCAD versions of the drawings".
  - The implied licence did not pass because Fortis did not buy the site from the architect's client.
  - The planning-portal licence limited downloads to consultation uses.
  - The originality bar for drawings is "not high".
  - Sources: [Bird & Bird summary](https://www.twobirds.com/en/insights/2017/uk/it-ip-law-bytes-apr17/copyright-architects-drawings); [BAILII judgment](https://knyvet.bailii.org/ew/cases/EWHC/Ch/2016/3583.html)
- [SECONDARY] The RIBA Journal says the implied licence "for all purposes connected with the building" "would also extend to reproducing the plans in marketing material to be shown to prospective purchasers". It does not permit removing the architect's name. — [RIBAJ, Architects' copyright in more detail](https://www.ribaj.com/intelligence/legal-copyright-in-architects-drawings-licenses-and-infringement/)
- [GUIDANCE / LAW] UK computer-generated works:
  - Under CDPA s9(3), the author of a computer-generated work is "the person by whom the arrangements necessary for the creation of the work are undertaken", with protection lasting 50 years.
  - The 2024 consultation flagged a contradiction between this and the originality requirement.
  - Source: [UK Copyright and AI consultation](https://www.gov.uk/government/consultations/copyright-and-artificial-intelligence/copyright-and-artificial-intelligence)
- [GUIDANCE] The government's Report on Copyright and AI (18 March 2026, under DUAA s136) says: "in the absence of evidence of its ongoing value, we propose that this specific type of protection should be removed, while copyright should continue to protect works created with AI assistance". — [GOV.UK report](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence/report-on-copyright-and-artificial-intelligence)
  - [SECONDARY] HSF Kramer calls even this conclusion "less than definite". — [HSF Kramer](https://www.hsfkramer.com/notes/ip/2026-03/uk-government-report-on-copyright-and-ai-concludes-more-evidence-is-needed-although-s9-3-cdpa-could-go)
- [GUIDANCE] US Copyright Office, Part 2 report (29 January 2025):
  - "Copyright does not extend to purely AI-generated material".
  - "prompts do not alone provide sufficient control".
  - Human selection, arrangement or modification can be protected.
  - Sources: [USCO Part 2 report](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf); [USCO AI page](https://www.copyright.gov/ai/)
- [LAW] US architectural works:
  - An "original design of a building embodied in any tangible medium of expression, including a building, architectural plans, or drawings" may be registered as an architectural work. Claims in the technical drawings and in the architectural work are registered separately.
  - Source: [37 CFR §202.11](https://www.law.cornell.edu/cfr/text/37/202.11)
  - *Design Basics v Lexington Homes* (7th Cir. 2017) found protection for home plans "thin" in a "crowded field", warned about "intellectual property trolls", and held that posting plans online does not by itself prove access. — [7th Cir. opinion](https://media.ca7.uscourts.gov/cgi-bin/rssExec.pl?Path=Y2017%2FD06-06%2FC%3A16-3817%3AJ%3AHamilton%3Aaut%3AT%3AfnOp%3AN%3A1975299%3AS%3A0&Submit=Display); [FindLaw](https://caselaw.findlaw.com/court/us-7th-circuit/1863319.html)
- [GUIDANCE] The UK consultation says most EU Member States and the US do not protect works without a human author; Ireland, India and Singapore have provisions similar to the UK's. — [UK consultation](https://www.gov.uk/government/consultations/copyright-and-artificial-intelligence/copyright-and-artificial-intelligence)

### Inferences
- **Who has rights to upload.** A developer that commissioned the architect usually holds at least an implied licence covering marketing. Agents, later site purchasers, and anyone using plans pulled from a planning portal may not.
- **Converting plans is copying.** Turning plans into 3D, CAD or BIM models and renders is a reproduction or adaptation; *Signature Realty* treated AutoCAD versions as infringing.
- **What to put in terms.** The platform's terms should require the customer to warrant that it has the copyright or a licence covering 3D conversion and marketing use. They should also include a customer indemnity and a notice-and-takedown process for rights-holders. **[SOLICITOR]**
- **Output IP.** If s9(3) is repealed, purely AI-generated CGI may have no UK copyright, in line with the US and EU, making it hard to stop competitors copying marketing images. The underlying architectural design copyright is unaffected. Contracts should assign "whatever rights exist" in outputs to the customer, not warrant that copyright exists.
- **Credits.** Keep architect credits and attributions in outputs. Removing them is outside the implied licence (*Blair*; RIBAJ).

### Gaps
- I did not verify the EU position (CJEU originality test, *Infopaq*/*Cofemel*) against a primary source in this pass.
- I did not research *Getty Images v Stability AI* (UK High Court, 2025) or the status of any UK legislative vehicle for s9(3) repeal.
- I found no UK case specifically on estate-agent floor-plan copying, beyond the general principles above.

---

## 3. Data protection and enterprise security (UK GDPR / DPA 2018 / DUAA 2025; transfers)

### Takeaway
The platform is a processor of its customers' data: uploads, buyer leads, and any people visible in photos. It needs Article 28-compliant DPAs, a flow-down of sub-processors (Anthropic, Bedrock, Google and so on), and lawful transfer routes. The legal landscape for transfers is now stable:
- Most DUAA 2025 data protection changes took effect on 5 February 2026.
- The complaints-procedure duty followed on 19 June 2026.
- The ICO became the Information Commission on 30 September 2026.
- EU adequacy for the UK was renewed until 27 December 2031.
- The UK Extension to the DPF lets UK data go to DPF-certified US recipients; otherwise use the IDTA or Addendum plus a transfer risk assessment (TRA).

### Cited Findings
- [LAW] Under SI 2026/82, most DUAA Part 5 provisions came into force on 5 February 2026. These include s70 (lawfulness), s71 (purpose limitation), s80 (automated decision-making) and s85 (international transfers). — [legislation.gov.uk SI 2026/82 reg 2](https://legislation.gov.uk/uksi/2026/82/regulation/2/made/data.xht)
- [GUIDANCE] The ICO confirms that most remaining provisions commenced on 5 February 2026, except the requirement to have a complaints procedure, which was due on 19 June 2026. — [ICO statement](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/statement-on-the-commencement-of-the-data-use-and-access-act-duaa/)
- [GUIDANCE] The Information Commissioner's functions transferred to the Information Commission from 30 September 2026. Controllers must handle complaints, for example "by providing an electronic complaint form". — [GOV.UK DUAA commencement plans](https://www.gov.uk/guidance/data-use-and-access-act-2025-plans-for-commencement); [GOV.UK DUAA changes](https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes)
- [LAW] Schedule 4 "recognised legitimate interests" covers crime, safeguarding, emergencies and similar purposes. It is not a general commercial basis. — [DUAA Sch 4](https://www.legislation.gov.uk/ukpga/2025/18/schedule/4)
- [LAW] EU adequacy for the UK was renewed on 19 December 2025, with a sunset on 27 December 2031. — [EC press release](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_25_3059/IP_25_3059_EN.pdf); [ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/receiving-personal-information-from-the-eea/)
  - DUAA kept the core rule that transfers need adequacy regulations, appropriate safeguards or a derogation. — [EC renewal decision](https://commission.europa.eu/document/download/b36eedab-43b8-46eb-ac30-a8d1e6e69f51_en?filename=Renewal+UK+adequacy+GDPR.pdf)
- [GUIDANCE] UK transfers to the US:
  - The UK Extension is a partial adequacy finding, independent of the EU's (clarified 30 July 2026).
  - The recipient must have active DPF status and have self-certified to the UK Extension.
  - If you rely on the IDTA or Addendum instead, "you must complete a TRA".
  - Sources: [ICO – UK Extension](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/adequacy-regulations/how-does-the-uk-extension-to-the-eu-us-data-privacy-framework-work/); [ICO – TRA for US](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/completing-a-transfer-risk-assessment/completing-a-tra-using-the-uk-government-s-analysis-us/)
- [PLATFORM] Data in AI-generated images: Rightmove requires that listing videos not contain anything "likely to breach the Data Protection Laws (look out for ... people, pictures of people, personal information)" and that no "living person can be identified". — [Rightmove Technical Guidelines Jan 2026](https://media.rightmove.co.uk/pdf/rightmove_technical_guidelines.pdf)
- [PLATFORM] Anthropic acts as processor on commercial products (see Q1). Google processes paid Gemini API data under its processor DPA. — [Anthropic Privacy Center](https://privacy.claude.com/en/articles/9267385-does-anthropic-act-as-a-data-processor-or-controller); [Gemini API terms](https://ai.google.dev/gemini-api/terms)

### Inferences
- **Roles.** The customer (developer or agent) is controller and the platform is processor for uploads and generated assets. The platform is controller for its own account and billing data. If the platform wants to use customer uploads to improve its own models, it becomes a controller for that purpose, which needs separate contractual permission and transparency. The safest default is "no training on customer uploads" unless the customer opts in, mirroring upstream terms.
- **Personal data in uploads.** Floor plans are rarely personal data alone, but they can be when linked to an address or occupier. Photos of occupied homes can show residents, family photos and documents. A detection and blur step lowers both data protection risk and Rightmove-compliance risk.
- **Transfer map.** UK customer to platform (UK or EU hosting) needs nothing extra. To US sub-processors: use DPF/UK Extension where certified, otherwise IDTA/Addendum plus TRA. EU customers can rely on UK adequacy to 2031.

### Gaps
- I found no authoritative source in this pass on what UK housebuilders and agents typically require in procurement (ISO 27001, SOC 2 Type II, Cyber Essentials Plus, annual pen tests, SSO/SAML, audit logs). This is common market practice from prior knowledge, not a verified finding. **[UNVERIFIED]**
- I found no ICO guidance specific to generative-AI processors in this pass.
- I did not verify the DUAA's new "not materially lower" transfer test wording in the primary text.

---

## 4. UK consumer protection and marketing rules for property CGI and AI imagery (DMCCA, CAP/ASA, NTSELAT, TPO, portals, NHQB)

### Takeaway
No UK statute requires a specific "AI" or "CGI" label. The legal test is whether an image misleads the average consumer, either directly or by omission, under DMCCA 2024 ss225–227 (in force 6 April 2025). That test is enforced:
- criminally, on a strict liability basis;
- by the CMA directly, with fines up to 10% of global turnover;
- by the ASA under CAP Code 3.1/3.3/3.17.

The practical labelling rules come from:
- **Rightmove:** label "Enhanced Edits" (AI, CGI, object add/remove) and show them alongside current, accurate images.
- **Zoopla:** make AI-produced photos clear.
- **New Homes Quality Code (March 2026):** CGI, photography and video must not mislead, and altered materials are restricted.

The ASA says a disclaimer cannot cure a fundamentally misleading image.

### Cited Findings
**DMCCA 2024 and the CMA**
- [LAW] The UCP provisions in DMCCA Part 4 Chapter 1 replace the CPUTRs and "apply to practices that take place from 6 April 2025". The offences are strict liability ("no need to prove the intent of the trader"), with up to 2 years' imprisonment. Due diligence and innocent publication defences exist under s238. — [CMA207 Unfair commercial practices guidance](https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices)
- [LAW] The CMA can now decide infringements itself and fine "up to 10% of their global turnover". Early priorities include information "that is objectively false". — [CMA press release 7 April 2025](https://www.gov.uk/government/news/cma-to-boost-consumer-and-business-confidence-as-new-consumer-protection-regime-comes-into-force); [CMA200](https://assets.publishing.service.gov.uk/media/6808ca0d8c1316be7978e74b/CMA_200_Direct_consumer_enforcement_guidance.pdf)
- [LAW] Under s226, a misleading action includes "an overall presentation which is likely to deceive ... even if the information it contains is true". Under s227, a misleading omission includes omitting "material information". — quoted in [AI Flip Room summary of DMCCA ss225–227](https://aifliproom.com/blog/virtual-staging-rules-united-kingdom); statute at [legislation.gov.uk DMCCA](https://www.legislation.gov.uk/id/ukpga/2024/13)

**ASA / CAP**
- [GUIDANCE / ASA ruling] *Taylor Wimpey UK Ltd* (14 November 2012): a show-home bathroom image with upgrades next to a "from" price was misleading. The ASA said that "Image from actual show home" did not cure it. — [ASA ruling](https://www.asa.org.uk/rulings/Taylor-Wimpey-UK-Ltd-A12-190009.html)
- [GUIDANCE] CAP advice on off-plan homes: if there are no images of the "from"-price property, an upgraded image is acceptable with "image includes optional upgrades at additional cost" placed adjacent to it and given equal prominence, and with the price of the home shown where known. Service charges must be made clear (*Pegasus Homes*, 13 November 2024; *Ballymore*, 15 August 2018). — [CAP Advice: New build and off plan homes](https://www.asa.org.uk/advice-online/property-new-build-and-off-plan-homes.html)
- [GUIDANCE / ASA ruling] *Birch's Group Ltd* (2016): footage of homes from a different site, and a show home not viewable at the advertised open weekend, was misleading under BCAP 3.1. — [ASA ruling](https://www.asa.org.uk/rulings/birchs-group-ltd-a16-350150.html)
- [GUIDANCE] ASA on AI disclosure:
  - "There is no blanket legal requirement in the UK to disclose the use of AI in ads".
  - "disclosure alone is very unlikely to mitigate the harm caused by a fundamentally misleading message".
  - Source: [ASA, Disclosure of AI in advertising (29 May 2025)](https://www.asa.org.uk/news/disclosure-of-ai-in-advertising-striking-the-balance-between-creativity-and-responsibility.html)
- [GUIDANCE] ASA, June 2026: the Code is "media-neutral" and "the advertiser remains responsible for any output used in their ads", even when ads are produced with automated AI tools (*Stripe & Stare Ltd*). — [ASA, AI and Deepfakes (11 June 2026)](https://www.asa.org.uk/news/ai-and-deepfakes-four-things-advertisers-need-to-know-before-they-hit-run.html)
- [GUIDANCE] CAP: "Images which give an inaccurate impression about the product ... by exaggerating the quality or size ... are likely to mislead". Small print such as "not representative" is generally insufficient (gaming analogy). — [CAP Misleading advertising](https://www.cap.org.uk/Advice-Training-on-the-rules/Advice-Online-Database/Misleading-Advertising.aspx); [ASA, A picture says a thousand words (Sep 2025)](https://www.asa.org.uk/news/a-picture-says-a-thousand-words-avoiding-misleading-imagery-in-ads.html)

**Portals**
- [PLATFORM] Rightmove Agent and Developer Technical Guidelines (January 2026), para 10:
  - "Enhanced Edits" means content "(i) generated and/or manipulated by AI; (ii) CGI; or (iii) manipulated or modified manually, such as adding or removing objects ... changing architectural features".
  - Enhanced Edits are permitted if they do not misrepresent the property, but must be "accompanied by current, accurate images of the room and/or property; and clearly labelled as being AI or otherwise enhanced".
  - Images must not contain text, and no identifiable living person may appear (except for some member types).
  - Source: [Rightmove Technical Guidelines PDF](https://media.rightmove.co.uk/pdf/rightmove_technical_guidelines.pdf)
- [PLATFORM] Rightmove's commercial listing guide says AI- or CGI-generated people can be used, but the listing "must include actual images of the property where possible". — [Rightmove commercial listing guide (Jan 2026)](https://hub.rightmove.co.uk/content/uploads/2026/01/Ultimate-Commercial-Property-Listing-Guide-2.pdf)
- [PLATFORM / SECONDARY] Rightmove's help page (modified 22 September 2026, as quoted): AI images "should not be used to disguise the property's true condition, add features that do not exist". — quoted in [AI Flip Room](https://aifliproom.com/blog/virtual-staging-rules-united-kingdom) **[verify on rightmove.co.uk]**
- [PLATFORM / SECONDARY] Zoopla Member Terms (1 December 2025), clause 5.1(c): where photographic content "is produced using autonomous technology (fully or partial), machine learning or other analogous technologies the Member will make this clear". Clause 5.1(d) lets Zoopla decline such content. The same source found no public OnTheMarket rule. — quoted in [AI Flip Room](https://aifliproom.com/blog/virtual-staging-rules-united-kingdom) **[verify primary Zoopla terms]**

**Property Ombudsman and NTSELAT**
- [GUIDANCE / SECONDARY] TPO Code clause 7i requires agents to take "all reasonable steps to ensure that all statements ... whether oral, pictorial or written, are accurate and are not misleading". — quoted in [AI Flip Room](https://aifliproom.com/blog/virtual-staging-rules-united-kingdom)
- [SECONDARY] NTSELAT's 2023 material information guidance (Parts A/B/C) is reportedly no longer on its site. On 18 June 2026 the government reportedly promised a Code of Practice for property agents "Later this year". — [AI Flip Room](https://aifliproom.com/blog/virtual-staging-rules-united-kingdom) **[UNVERIFIED against NTSELAT/GOV.UK primary; treat as uncertain]**

**New Homes Quality Code (NHQB)**
- [GUIDANCE] New Homes Quality Code (applies to homes reserved from 2 March 2026):
  - 1.1: "Developers must ensure that all sales and marketing material – including visual representations such as photography, CGI, and video – is not misleading".
  - 1.2: material information must be given, including size per the RICS Code of Measuring Practice (GIA) and specification, including items not in the standard spec.
  - Source: [NHQB Code Part 1](https://www.nhqb.org.uk/the-code/part-1-selling-a-new-home/); [NHQB Code PDF March 2026](https://www.nhqb.org.uk/wp-content/uploads/2026/02/Large-text-New-Homes-Quality-Code-V2-March-2026.pdf)
- [SECONDARY] The March 2026 update requires material information upfront across "online property portals, digital and printed brochures ... CRM‑driven property feeds". Developers are "now restricted from using altered marketing materials, including edited photography, video, or CGI, which could be considered misleading". — [Walker Morris](https://www.walkermorris.co.uk/comment-opinion/the-new-homes-quality-code-march-2026-update-what-you-need-to-know/)
- [PLATFORM] Example of market practice: Lovell's CGI disclaimer says images are "for illustrative purposes and final elevations and materials may differ". — [Lovell](https://newhomes.lovell.co.uk/marketing/computer-generated-images-cgi/)

### Inferences
- **The core rule.** An AI render may show the property as it will or could be, honestly qualified. It may not show something the buyer will not get at the advertised price, such as:
  - upgrades without an adjacent, equally prominent qualification;
  - views or green space that won't exist;
  - wrong dimensions;
  - removed pylons or neighbouring buildings.
- **Disclaimers have limits.** Adding "CGI for illustrative purposes" does not cure a materially misleading image (Taylor Wimpey; ASA AI guidance).
- **Who is liable.** The platform is probably not the "trader" making the listing, but it could be exposed. Liability can flow to a person whose act caused another to commit an offence, per CMA207. Its marketing claims ("photoreal, accurate") also matter. Contract terms should put publication responsibility on the customer.
- **Product consequences of the Rightmove rules.** Auto-label every AI or CGI output with an "AI-generated / CGI" tag. Preserve the source or "real" images and export them together. Keep text out of the image apart from the required label (confirm with Rightmove whether an in-image label counts as prohibited text). No identifiable people unless they are synthetic and the customer type allows it.

### Gaps
- I could not confirm the current status of NTSELAT's Material Information Parts A/B/C guidance from the primary source. A secondary source reports it was withdrawn.
- I did not retrieve the primary text of Zoopla's or OnTheMarket's terms.
- I found no ASA ruling specifically on an AI-generated property image as of October 2026.
- I did not check the Propertymark rules in the primary source.

---

## 5. Liability for inaccurate representations (off-plan buyers relying on CGI) and contractual allocation

### Takeaway
Buyers of off-plan homes have two routes:
- claims against the developer or agent for misrepresentation; and
- from 2025, statutory private redress under DMCCA/CPUTR-derived rights (transitional; CMA technical note).

The developers' standard defence is entire-agreement and non-reliance clauses. These are tested for fairness in consumer land contracts and for reasonableness under s3 of the Misrepresentation Act. Fraudulent misstatements by professionals (such as architects' completion certificates) give rise to direct liability.

For the SaaS, the key exposure is a claim over from its customer. It should allocate risk through:
- customer approval and sign-off of every published asset;
- customer responsibility for accuracy and labelling;
- caps and exclusions;
- disclaimers in the outputs; and
- PI/tech E&O insurance.

### Cited Findings
- [LAW] *Shaftsbury House (Developments) Ltd v Lee* [2010] EWHC 1484 (Ch): in an off-plan purchase, the buyer's misrepresentation defence failed for lack of reliance. The court considered an entire-agreement / non-reliance clause and noted that consumer unfair-terms rules (then UTCCR 1999) apply to contracts for land. — [BAILII](https://www.bailii.org/ew/cases/EWHC/Ch/2010/1484.html)
- [LAW / SECONDARY] The Court of Appeal (2017) upheld a standard conveyancing non-reliance clause as fair and reasonable where the buyer was legally advised and had equal bargaining power, despite plans showing a non-permitted extension. — [Helix Law summary](https://helix-law.co.uk/sellers-contract-clause-avoids-liability-for-misrepresentation-made-to-buyer-of-land/) (case name not given in the source; I believe it is *First Tower Trustees v CDS*-era authority but have not verified this) **[UNVERIFIED case name]**
- [LAW] *Aitsan Ltd v Duffy* (2026, Chancellor): an architect was liable for fraudulent misrepresentation to off-plan buyers via a false completion certificate. The appeal concerned how to quantify loss. — [Approved judgment PDF](https://s47657.pcdn.co/wp-content/uploads/2026/07/Aitsan-Ltd-and-others-v-Duffy-and-another.pdf)
- [LAW] Consumer private redress rights under the CPUTRs continue until a new statutory instrument replaces them under DMCCA. — [CMA Technical note](https://assets.publishing.service.gov.uk/media/67ee863298b3bac1ec299c81/Technical_note.pdf)
- [PLATFORM] Upstream providers push accuracy risk onto the customer:
  - OpenAI: "Customer is solely responsible for all use of the Outputs and for evaluating the accuracy". — [OpenAI Services Agreement](https://openai.com/policies/services-agreement/)
  - Anthropic: the customer must evaluate outputs and notify users that they may be inaccurate. — [Anthropic Commercial Terms PDF](https://assets.ctfassets.net/5965pury2lcm/4e9p7xwZDo6mBgWfSyDsCV/907c229ef3ee22366fa66837419bde2c/Anthropic_T_Cs.pdf)
- [GUIDANCE] The ASA treats the advertiser as responsible for AI output even when the ad was generated by automated tools. — [ASA June 2026](https://www.asa.org.uk/news/ai-and-deepfakes-four-things-advertisers-need-to-know-before-they-hit-run.html)

### Inferences
Contract structure for the SaaS (B2B, so UCTA reasonableness applies, not the CRA) **[SOLICITOR]**:
1. Customer warrants input accuracy and rights (plans, specifications, finishes).
2. A mandatory approval step before export or publish, with an audit log of who approved what.
3. The customer is solely responsible for regulatory compliance of published marketing: DMCCA, CAP, NHQB, portal rules, Trakheesi/REGA permits.
4. The platform makes no warranty of dimensional or visual accuracy; outputs are "illustrative".
5. Liability cap, for example 12 months' fees, with exclusion of indirect loss. Carve-outs only where the law requires them (fraud, death or personal injury).
6. A customer indemnity for third-party (buyer or regulator) claims arising from published content.
7. Hold PI / tech E&O and cyber cover. Check that it covers AI-generated content.

Disclaimers embedded in deliverables should be short and adjacent to the image (for example "CGI – indicative only; specification, finishes and landscaping may differ"). They cannot rescue a materially misleading image (Q4).

### Gaps
- I found no reported UK case where a buyer sued specifically over a misleading developer CGI (as opposed to oral statements or certificates).
- I found no source on market-standard PI insurance terms for AI-visualisation vendors.
- I did not research the details of the forthcoming DMCCA private-redress SI.

---

## 6. EU AI Act Article 50 and US rules (FTC, California AB 723, MLS rules)

### Takeaway
**EU.** Article 50 has applied since 2 August 2026.
- Providers of generative systems must machine-mark outputs. Systems already on the market before 2 August 2026 have until 2 December 2026 for the Art 50(2) marking duty, according to a law-firm briefing.
- Deployers must visibly label "deepfakes": content resembling existing "persons, objects, places, entities or events" that would falsely appear authentic.
- Fines reach €15M or 3% of turnover. A Commission-endorsed Code of Practice and Guidelines exist.
- A photoreal render of a real or planned building or place can fall within the deepfake definition. The platform (provider) must mark outputs, and its customers (deployers) must label them.

**US.** California BPC §10140.8 (AB 723), effective 1 January 2026, requires real-estate licensees to disclose digitally altered images and link to the unaltered original. CRMLS Rule 11.5.2 implements it and goes further.

### Cited Findings
- [LAW / GUIDANCE] "Article 50 of the AI Act applies from 2 August 2026."
  - Providers must "Add machine-readable marks to enable the detection of AI-generated or manipulated content".
  - Deployers must inform people when they are exposed to deepfakes.
  - Source: [EC Guidelines on transparency obligations](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations)
- [GUIDANCE] The Commission says the scope covers "images, audio, and video content that resemble existing persons, objects, places, entities, or events (deepfakes)". The EU has created a set of icons for labelling. Fines are up to €15M or 3% of global turnover, with proportionality for SMEs. — [European Commission news, 2 August 2026](https://commission.europa.eu/news-and-media/news/safer-and-more-transparent-ai-2026-08-02_en)
- [GUIDANCE] The Code of Practice on Transparency of AI-generated Content was finalised in June 2026. The Commission and AI Board confirmed it as an "adequate voluntary tool". About 190 signatories had signed by end of July 2026. Non-signatories must show compliance by "alternative equivalently adequate means". — [EC Code of Practice page](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content); [EC press release](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content)
- [SECONDARY] McCann FitzGerald on Article 50:
  - Art 50(2) marking applies from 2 December 2026 to systems already on the market before 2 August 2026.
  - Deepfake disclosures "must be clear and perceivable – machine-readable markings alone are insufficient".
  - A lighter regime applies to "evidently artistic, creative ... or analogous works".
  - Disclosure is due "at the latest at ... first exposure".
  - The Guidelines were published 20 July 2026, and give examples of exceptions "such as standard editing".
  - Sources: [McCann FitzGerald](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/ai-transparency-european-commissions-guidelines-on-article-50-part-2-deployer-obligations); [EC Guidelines page](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations)
- [LAW] California BPC §10140.8 (AB 723, Stats. 2025 ch. 497, effective 1 January 2026):
  - A broker or salesperson "or person acting on their behalf" who uses a "digitally altered image" in an ad must include "a statement disclosing that the image has been altered and a link ... URL, or QR code" to the original, "reasonably conspicuous and located on or adjacent to the image".
  - The definition covers AI changes to "fixtures, furniture ... flooring, walls, paint color ... facade, floor plans ... views through windows, and neighboring properties".
  - Lighting, colour correction and cropping are excluded.
  - A wilful violation of the Real Estate Law is a crime.
  - Sources: [CA BPC §10140.8](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10140.8.); [AB 723 bill text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB723)
- [PLATFORM] CRMLS Rule 11.5.2 (February 2026 FAQ):
  - The original must be displayed "immediately before or after" the altered image, which must be labelled "Virtually Staged", "AI Altered" or similar.
  - Images may not alter real property elements "unless the listed property will be improved to match ... at time of close".
  - "AI-generated landscaping images are not permitted in the MLS".
  - Source: [CRMLS FAQ PDF](https://go.crmls.org/wp-content/uploads/2026/02/2026%5FDigitally%5FAltered%5FImages%5FFAQs%5Fv1.pdf)

### Inferences
- **The platform is likely an AI Act "provider".** If it puts a generative system on the EU market under its own name or a white-label brand, it must embed machine-readable marks (C2PA Content Credentials plus a watermark) by the applicable date. It should consider signing the Code of Practice, or at least aligning with it.
- **Customers are deployers.** EU customers publishing photoreal renders of real places or buildings need a visible label; the EU icon set is an option. Offer an auto-applied, non-removable-by-default label in EU workspaces. Whether a clearly stylised architectural CGI of an unbuilt building is a "deepfake" is a matter of interpretation. **[SOLICITOR]**
- **California.** AB 723 targets licensees and those "acting on their behalf". A US agent customer using virtual staging or AI renovations needs an "altered" statement, the original image, and a link or QR code. Product features: keep the originals, generate a hosted "original image" page with a QR code, and add labels in MLS export fields.

### Gaps
- I did not retrieve the FTC's position on AI imagery in real estate, NAR Code of Ethics Art. 12 commentary on virtual staging, or other states' laws.
- I did not confirm whether the Digital Omnibus (2025 proposal) changed Art 50 timing beyond the 2 December 2026 grace period reported by McCann FitzGerald.

---

## 7. UAE (Dubai DLD/RERA, Trakheesi; UAE PDPL) and Saudi Arabia (REGA, Wafi; PDPL)

### Takeaway
**Dubai.** Every real estate ad, including electronic and portal ads, needs a DLD/RERA Trakheesi permit with the permit number (and QR code) shown. Brokers need a Form A marketing contract. Off-plan projects can only be marketed if they are registered with RERA and have an escrow account.

**Saudi Arabia.** Ads need a REGA real-estate advertisement licence tied to a brokerage contract. Off-plan marketing needs a Wafi marketing licence, which requires approved "architectural designs and engineering plans".

**Data.** UAE federal PDPL Arts 22–23 allow transfers to adequate jurisdictions or with contractual safeguards. Saudi Arabia's 2024 Transfer Regulation allows transfers with SCCs, BCRs or certification, plus a risk assessment. It is not strict localisation.

**Product impact.** Generated marketing must leave room for permit numbers and QR codes, must be consistent with the approved plans, and cannot be used to market unregistered off-plan projects.

### Cited Findings
- [LAW / GUIDANCE] DLD Real Estate Ad Permit covers "Electronic advertisements", "Real estate promotion platforms", "Classified advertisements" and other channels, issued via Trakheesi. The fee is AED 1,000 (AED 5,000 for a launch event). Brokers need a copy of the marketing contract with the owner. At exhibitions, it is "not allowed to showcase off-plan properties that are not registered with the Escrow Account Department". — [DLD Real Estate Ad Permit](https://dubailand.gov.ae/en/eservices/real-estate-ad-permit/)
- [GUIDANCE] RERA Brokerage Practice Guide 2024: brokerages "must obtain a permit for any real estate advertisement or marketing material through the Trakheesi system ... the permit number must be displayed on the ad". Off-plan marketing requires a licensed and registered project and an escrow account. — [DLD Brokerage Practice Guide 2024](https://dubailand.gov.ae/media/i31iv1n0/real_estate_brokerage_practice_guide_2024.pdf)
- [GUIDANCE] DLD circulars cover "Applying the QR code system for real estate ads" (April 2023), "Terms and conditions for real estate marketing on portals" (August 2022), "Real Estate ads Terms and conditions", and compliance with Law No. 8 of 2007 on marketing real estate projects (March 2025). — [DLD Rules & Regulations](https://dubailand.gov.ae/en/about-dubai-land-department/rules-regulations/)
- [LAW / GUIDANCE] Saudi REGA real estate advertisement licence: issued via the REGA platform against "A brokerage contract that includes a marketing scope". The applicant acknowledges the accuracy of the information entered. — [REGA Ad License service](https://rega.gov.sa/en/rega-services/eservices/real-estate-advertisement-license-issuance/)
- [LAW] Saudi off-plan (Wafi), under the Off-Plan Sale and Lease Law (Council of Ministers Resolution 196, 1445H):
  - A marketing licence requires the title deed, the marketing contract and "Architectural designs and engineering plans".
  - Reservations are capped at 5%, paid into escrow.
  - Developers must "Disclose the current status of the project".
  - Source: [REGA Wafi](https://rega.gov.sa/en/rega-services/platforms/wafi-off-plan-sales-and-lease/?currentPage=42&tabActive=Wafi+Projects)
- [LAW] UAE PDPL (Federal Decree-Law 45/2021):
  - Art 22 permits transfers to states with adequate data protection law.
  - Art 23 permits transfers otherwise by contract, explicit consent, contract performance and similar grounds. Controls are deferred to Executive Regulations.
  - Source: [UAE PDPL text](https://www.uaelegislation.gov.ae/en/legislations/1972/download)
- [LAW] Saudi PDPL: in force 14 September 2023, with the grace period ending 14 September 2024. The Transfer Regulation was updated 1 September 2024, with SCCs, BCRs and "Certificate of Accreditation" as safeguards and a risk assessment required in specified cases. — [SDAIA Transfer Regulation](https://sdaia.gov.sa/Documents/RegulationonPersonalDataEN.pdf); [HFW](https://www.hfw.com/insights/the-year-in-review-kingdom-of-saudi-arabia-2024/); [Morgan Lewis](https://www.morganlewis.com/pubs/2024/09/saudi-arabia-personal-data-protection-law-transition-period-ends-september-14); [King & Spalding](https://www.kslaw.com/news-and-insights/international-personal-data-transfers-under-saudi-arabias-data-protection-law)

### Inferences
- **Dubai.** Add a "permit number / QR" field and template slot to every export (renders, videos, social cuts). Optionally block publishing to Dubai channels until a permit number is entered. Off-plan Dubai customers should confirm RERA registration and escrow before marketing.
- **Saudi Arabia.** Off-plan visualisation should be generated from the approved plans submitted to Wafi, and the product should keep a version link to them. Divergence between marketing CGI and the approved plans creates regulatory risk.
- **Data.** Neither country appears to require strict local hosting for ordinary commercial personal data under its general PDPL, based on the sources reviewed. Government or semi-government developer clients may impose localisation by contract or sectoral rules (for example NCA controls in Saudi Arabia). **[UNVERIFIED; SOLICITOR]**

### Gaps
- I did not find whether Dubai or Saudi rules specifically address CGI or AI imagery accuracy, or require AI labels.
- I did not check the status of the UAE PDPL Executive Regulations (historically delayed) or DIFC/ADGM free-zone regimes.
- I did not check Saudi NCA cloud/ECC localisation rules or the REGA advertising regulation's content rules (accuracy, imagery).

---

## 8. Planning vs marketing use of CGIs (verified views, LVMF, LI TGN 06/19)

### Takeaway
Images submitted with planning applications are held to a separate, more demanding standard.
- The Landscape Institute's TGN 06/19 defines visualisation Types 1–4. Type 4 is "survey / scale verifiable", the AVR or "Verified View" standard. Visualisations must give "a fair representation" through "replicable, transparent and structured processes" and come with a Technical Methodology.
- The London View Management Framework (LVMF) sets out Accurate Visual Representation (AVR) procedure for London's strategic views.
- TGN 06/19 is "currently under review".

Marketing-grade AI renders should never be presented or sold as planning-grade visualisations.

### Cited Findings
- [GUIDANCE] TGN 06/19:
  - Visualisations should "provide a fair representation of what would be likely to be seen", "be based on replicable, transparent and structured processes", be accompanied by a Technical Methodology, and "where necessary ... be capable of being verified".
  - Type 3 is for many planning applications.
  - Type 4 "require[s] the use of equipment and processes which provide quantifiable verification data ... (as per industry-standard 'AVRs' or 'Verified Views')", with a 50mm lens on a full-frame camera and the label "Visualisation Type: 4" shown.
  - Source: [LI TGN 06/19 PDF](https://www.landscapeinstitute.org/wp-content/uploads/2019/09/LI_TGN-06-19_Visual_Representation-1.pdf)
- [GUIDANCE] "TGN 06/19 is currently under review." — [Landscape Institute visualisation page](https://landscapeinstitute.org/policy-practice/technical/digital-practice-mapping-visualisation/visualisation/)
- [GUIDANCE] LVMF SPG: "An Accurate Visual Representation (AVR) is a static or moving image that shows the location of a proposed development, the degree to which it will be visible, its detailed form and/or the materials to be used". — [LVMF 2012](https://www.london.gov.uk/sites/default/files/gla_migrate_files_destination/LVMF%20March%202012%20part%201.pdf?token=YJoKa7uK)
- [SECONDARY] Practitioners treat LVMF Appendix C as industry best practice for urban AVRs, commonly using a 24mm lens. — [St Albans ES Appendix 7.5, Verified View Methodology](https://www.stalbans.gov.uk/sites/default/files/attachments/E2.12a%20ES%20Vol%203%20-%20Appendix%207.5%20-%20Verified%20View%20Methodology.pdf)

### Inferences
- **Terms of service.** State that outputs are not verified views or AVRs and must not be submitted as TGN 06/19 Type 3/4 visualisations or LVMF AVRs unless produced through a separate verified workflow (survey data, camera matching, methodology).
- **Product controls.** Watermark or tag renders "Not a verified view – marketing illustration". Block or warn on "planning" export presets. A future premium verified-view workflow would need survey control points, lens metadata and a methodology report, and probably a human professional sign-off.
- **Why it matters.** If marketing images differ from planning-approved visualisations, objectors may challenge them and they may mislead under DMCCA. Marketing renders should be traceable to the approved drawings.

### Gaps
- I did not find any case or decision where an AI-generated visualisation was rejected in planning.
- I did not find the timetable for the TGN 06/19 revision.

---

## 9. Synthesis: compliance map and concrete product safeguards

### Takeaway
The highest-priority risks, in order:
1. Misleading marketing imagery (UK DMCCA/CAP/NHQB, Rightmove/Zoopla rules, California AB 723, EU Art 50 labelling).
2. Rights in uploaded plans (*Signature Realty*).
3. Upstream licence and data terms (FLUX, Stability, Runway training; residency).
4. Data protection transfers and processor duties.

Most of these can be handled by product design (labelling, keeping originals, provenance marks, approval workflow, permit fields) combined with B2B terms that put publication responsibility on the customer.

### Cited Findings
- Rightmove requires a label plus accurate images alongside every AI or CGI image. — [Rightmove Technical Guidelines](https://media.rightmove.co.uk/pdf/rightmove_technical_guidelines.pdf)
- California requires a disclosure, the original image, and a link or QR code. — [CA BPC §10140.8](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10140.8.)
- The EU requires machine-readable marks (provider) and visible deepfake labels (deployer). — [EC Guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations)
- Dubai requires the permit number on the ad. — [DLD Brokerage Guide](https://dubailand.gov.ae/media/i31iv1n0/real_estate_brokerage_practice_guide_2024.pdf)
- A disclaimer won't cure a misleading image. — [ASA](https://www.asa.org.uk/news/disclosure-of-ai-in-advertising-striking-the-balance-between-creativity-and-responsibility.html)
- Using drawings for marketing or CAD without a licence infringes. — [Bird & Bird on Signature Realty](https://www.twobirds.com/en/insights/2017/uk/it-ip-law-bytes-apr17/copyright-architects-drawings)

### Inferences
Proposed safeguards (inferred from the findings above; to be validated with counsel **[SOLICITOR]**):

1. **Provenance and labelling by default**
   - C2PA Content Credentials plus an invisible watermark on every output (EU Art 50(2)).
   - A configurable visible label ("CGI", "AI-generated", "Virtually staged") positioned to suit each portal.
   - Jurisdiction presets: UK-Rightmove, UK-Zoopla, EU-Art50 (EU icon), CA-AB723 (label plus QR to the original), Dubai (Trakheesi permit number and QR slot).
   - Labels carried in file names and metadata so they survive portal reformatting.
2. **Originals kept and paired**
   - Store the source photos and plans with every derived asset.
   - Export "pair packs" (original plus enhanced), and offer a hosted original-image page or QR code for California.
3. **Accuracy guardrails**
   - Lock geometry to the uploaded CAD/BIM dimensions, with tolerance checks and GIA calculation per RICS where area is shown.
   - Flag any change to structural elements, views, neighbouring buildings, utilities or landscaping (prohibited by CRMLS and risky under DMCCA).
   - A "specification tier" toggle so "from"-price images show standard spec, and an auto-inserted "includes optional upgrades at additional cost" line when upgrades are rendered (CAP/ASA).
4. **Approval workflow and audit trail**
   - A named approver must sign off each asset before export.
   - Immutable logs of the inputs, model, prompt and edits.
   - Version linkage to planning-approved or Wafi-approved drawings.
5. **Rights checks on inputs**
   - At upload, the customer confirms its rights in the plans (architect licence or assignment), with architect credit fields.
   - Warn if a file appears to come from a planning portal.
   - Takedown process for rights-holders.
6. **No planning use**
   - "Not a verified view" marking.
   - No TGN 06/19 Type 4 / LVMF AVR claims unless a separate verified pipeline exists.
7. **Model and vendor governance**
   - Allowlist only models with commercial rights, no-training terms and suitable residency: Claude via Bedrock or Vertex EU/UK; BFL API or a paid self-hosted licence; Gemini/Vertex paid tier.
   - Exclude Runway's standard terms for customer content, and FLUX [dev] or Stability without licences.
   - Never strip upstream watermarks.
   - Show an AI-interaction disclosure in any assistant UI (Anthropic AUP; EU Art 50(1)).
8. **Data protection**
   - Processor DPA with sub-processor list, UK/EU hosting by default, IDTA/DPF plus TRA for US sub-processors.
   - Default "no training on customer data".
   - Configurable retention, with deletion on termination.
   - Face and personal-document blurring in photo inputs.
   - Complaints procedure (DUAA, from 19 June 2026).
9. **Contract**
   - The customer is responsible for publication compliance (DMCCA, CAP, NHQB, portal rules, Trakheesi, REGA).
   - Outputs are illustrative only, with no accuracy warranty.
   - Liability cap and customer indemnity; outputs assigned "as is".
   - Flow-down of the upstream AUPs.
   - No IP indemnity promised beyond what upstream providers give.
   - PI and cyber insurance in place.

### Gaps
- None of these safeguards has been validated with a regulator, portal or insurer. Rightmove's view on whether an in-image AI label conflicts with its "no text in images" rule is unconfirmed.
- I did not verify enterprise procurement norms (ISO 27001, SOC 2, Cyber Essentials Plus, SSO) (see Q3).
