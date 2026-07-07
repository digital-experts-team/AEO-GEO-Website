# Aretto — AEO / GEO / SEO Program: Strategy, Execution & Impact

Client: Aretto (D2C kids' footwear, Pune) · Role: AEO/GEO & Organic Growth · Portfolio case study

> One-line summary: Built Aretto's AI-search visibility engine — turning a single-product D2C brand into a consistently cited answer for "best kids shoes India" queries across ChatGPT, Perplexity, Gemini and Google AI Overviews — by combining entity-first SEO, answer-formatted content, earned-media amplification, and a citation-tracking measurement system.

---

## 1. Starting Context (Before)

* Strong product story (patented expandable sole, "world's first") but no structured AI-search strategy
* Discovery dependent on paid social + Shark Tank spike; organic search visibility limited to branded queries
* Brand entity facts inconsistent across the web; no schema markup; no answer-formatted content
* Zero tracking of AI citations or share of voice — no way to know if ChatGPT/Perplexity ever recommended the brand
Baseline audit (Week 1–2):

- [ ] Ran 25 "money prompts" manually across ChatGPT, Perplexity, Gemini, Google AI Overviews (e.g. best kids shoes India, shoes that grow with kids' feet, barefoot shoes for toddlers India)
- [ ] Logged: mention rate, citation rate, position in list, sentiment, competitor share
- [ ] Crawl audit: schema coverage, extractability, Core Web Vitals
- [ ] Mention audit: which third-party domains carried consistent brand facts
Baseline result: mentioned in [X]% of category prompts — fill with your actual number. (Benchmark context: 91% of online stores appear in 0% of AI shopping answers — Nudge 2026 audit.)

---

## 2. Strategy — The 4-Layer Citation Flywheel

Thesis: AI engines cite brands when (a) entity facts are consistent across many independent domains, (b) owned content is extractable and answer-formatted, (c) retailer/aggregator pages corroborate, and (d) the technical layer lets crawlers in.

1. Entity Layer — one set of quotable, falsifiable facts repeated everywhere: "world's first expanding kids' shoes", "patented Supergrooves™ sole", "expands 18mm / 3 sizes", "zero-drop, wide toe box"
1. Owned Content Layer — answer-first blog + FAQ architecture targeting commercial-intent queries
1. Earned Consensus Layer — media, listicles, retailer pages, UGC that independently repeat the entity facts
1. Technical Layer — schema, crawlability, extractable HTML
---

## 3. What I Executed

### 3.1 Owned content (AEO)

* Built topical-authority clusters on wearetto.com/blogs: Foot Growth & Development, Shoe Sizing & Fit, Buying Guides, Comfort & Technology, Sustainability — narrow niche depth over breadth (topical clusters correlate with ~2.5x higher AI citation rates — Conductor 2026 benchmarks)
* Published owned comparison/listicle content ("Best Shoes Brands in India for Kids", "Walking vs Running Shoes for Kids", "Best Children's Running Shoes") — listicles are the most-cited content type for commercial queries (~41% — Wix study). Deliberately named competitors (Campus, Liberty, Adidas, ASICS) so pages read as editorial roundups, not ads
* Restructured FAQ into extractable Q→A blocks: one question, one direct answer with the specific number in the first sentence
* Answer-first formatting site-wide: direct answer in the first 1–2 sentences under each header (44% of LLM citations come from the first 30% of a page — Growth Memo)
### 3.2 Earned media & consensus (GEO)

* Leveraged Shark Tank India S3 appearance: IANS wire syndication → dozens of independent domains (IMDb, Daijiworld, regional news) repeating identical entity facts
* Seeded/maintained structured brand profiles across the Shark Tank recap ecosystem (KeeVurds, StartupArticle, d2c.fyi, ViesStories) — aggregator-style pages LLMs pull heavily from
* Funding PR (₹4.5Cr round, Hardik Pandya as investor) → YourStory, Inc42, LinkedIn coverage — celebrity-investor news hook = fresh mention wave
* Secured placements in third-party "Top kids footwear brands in India" listicles
* International/institutional coverage (ZOZO Fashion Tech News interview, Japan) — high-trust source type for LLMs
### 3.3 Retailer & marketplace corroboration

* Optimized FirstCry brand page with the full entity story (18mm expansion, Supergrooves mechanism, "2/3 of kids wear the wrong size" stat) — retailer domains are cited up to 4x more than brand-owned PDPs (Avenue Z Beauty Index), so the retailer page becomes a citation proxy
### 3.4 Technical (SEO foundation)

* Product + FAQ + Organization schema (JSON-LD) — structured data drives 40–60% more AI references (Conductor)
* Core Web Vitals fixes (LCP target <2.5s; sites with LCP >4s are 72% less likely to be cited — Onely)
* Ensured GPTBot / PerplexityBot / Google-Extended crawl access in robots.txt
---

## 4. Measurement System (What I Tracked)

> This is the part hiring managers care about most — the system, not just the numbers.

Weekly manual prompt panel: 25 money prompts × 4 engines (ChatGPT, Perplexity, Gemini, AI Overviews), logged in a tracker:

* Mention rate (% of prompts where Aretto is named)
* Citation rate (% where wearetto.com or a page carrying our facts is linked)
* Avg. list position · Sentiment · Source cited (owned / retailer / media / UGC)
* Share of Voice = Aretto mentions ÷ total brand mentions across the prompt panel
Tooling: [name the tool you used — e.g. Otterly / Profound / Peec / manual sheet]

Downstream KPIs:

* AI-referral sessions (GA4 regex: chatgpt.com, perplexity.ai, gemini.google.com referrers)
* Branded search volume lift (leading indicator — brand mentions happen 3.2x more often than citations, so branded search rises before referral traffic — BrightEdge)
* Conversion rate of AI-referred traffic (benchmark: ChatGPT-referred shoppers convert at ~11.4% vs 5.3% organic — Adobe)
---

## 5. Impact

|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
⚠️ Fill brackets with your real tracked numbers. Keep the benchmark column — it shows you know what good looks like even before they ask.

---

## 6. Key Learnings (Interview Talking Points)

1. Mentions ≠ citations. ChatGPT names consumer brands in answer text far more often than it links them — so I tracked both separately.
1. Only ~11% of domains are cited by both ChatGPT and Perplexity — I ran platform-specific playbooks: entity/earned-media work for ChatGPT (parametric), fresh answer-formatted pages for Perplexity (real-time retrieval).
1. The retailer page is a Trojan horse. When AI routes shopping answers to retailers 4x more than brand PDPs, optimizing the FirstCry brand page was higher-ROI than another blog post.
1. Earned media is the moat. One Shark Tank appearance, properly amplified, created the cross-domain consensus that no amount of owned content could.
1. Biggest remaining gap: Reddit/UGC (≈29% of ChatGPT shopping citations) and YouTube (≈16% of Perplexity's top citations) — my proposed next phase.
---

## 7. Appendix

* Prompt panel (25 queries) — [link your sheet]
* Weekly tracking sheet — [link]
* Before/after screenshots of AI answers — [add — these are the single most convincing artifact in an interview]
* Content calendar & published pieces — [link]
