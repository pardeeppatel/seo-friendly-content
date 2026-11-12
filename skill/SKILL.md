---
name: seo-friendly-content
description: >-
  Interactive SEO content-writing and humanization engine by Pardeep Kumar (ToolNPlay.com).
  Guides the user step by step through focus keyword selection, 10 intent-matched SEO title
  suggestions (with regeneration), word count and FAQ selection, up-to-date grounded research
  without fake data, natural human-sounding prose editing, a 16:9 website-ready featured image,
  and a deterministic on-page SEO and anti-AI audit. Use whenever the user asks to write an SEO
  blog post, article, pillar guide, product page, or refresh existing web content.
---

# SEO Friendly Content — Interactive On-Page SEO & Human-Writing Engine

> **Developed by Pardeep Kumar** | **Powered by [ToolNPlay.com](https://ToolNPlay.com)**

An interactive, multi-step workflow for producing **search-optimized, natural, human-sounding web content** that satisfies top on-page SEO scoring criteria while eliminating robotic AI-writing tells.

> **Core Rule:** Write for human readers first and search engines second. Never sacrifice clarity, factual accuracy, or natural prose just to force a metric.

---

## Mandatory Interactive Workflow (Step-by-Step)

Do **not** jump straight into writing a full article when the user provides only a topic. Follow this exact 4-phase interactive loop, stopping at each gate for user confirmation:

### Phase 1: Topic & Focus Keyword Intake
1. Read the user's topic, niche, or existing draft.
2. Check whether the user has already specified a **Focus Keyword**.
3. If not provided, **STOP and ask**:
   - *"Do you already have a **Focus Keyword** (and optional Secondary Keywords) you are targeting, or should I suggest Focus Keywords along with the titles?"*
   - *(Optional)* *"Feel free to share your target audience, tone, or any existing website URLs you want linked internally."*

### Phase 2: 10 SEO Title Suggestions (Select or Regenerate Loop)
First, silently identify the topic's **Search Intent** (*Informational How-To, Listicle, Comparison/Review, Product/Transactional, or Content Refresh*) so the 10 titles span diverse, high-CTR angles rather than repeating one template.

* **Case A — User PROVIDED a Focus Keyword:**
  Generate **10 SEO titles** strictly following on-page title guidelines (see [`references/title-formulas.md`](./references/title-formulas.md)):
  - Primary Focus Keyword appears in the **first 50%** (ideally within the **first 50 characters**) of the title.
  - Total length is **`≤ 60` characters** (show exact character count next to each option).
  - Includes a **number** (where natural), a **power word**, and **strong non-clickbait sentiment**.
* **Case B — User did NOT provide a Focus Keyword:**
  Propose **10 complete options**, each containing:
  1. **SEO Title** (`≤ 60` chars, keyword in first 50%, number + power word + sentiment)
  2. **Designated Primary Focus Keyword**
  3. **2–3 Secondary / Long-Tail Keywords**

**MANDATORY STOP:** Ask the user to:
- Pick a numbered option (`#1`–`#10`), **or**
- Request **10 new regenerated title suggestions** (with any adjusted angle or keyword), **or**
- Provide their own custom title.

Repeat Phase 2 until the user confirms the title and Focus Keyword.

### Phase 3: Word Count, FAQ & Experience Context Confirmation
Once the title and Focus Keyword are confirmed, **STOP and ask in one combined prompt** (use a structured multi-choice prompt when available, or a clean numbered list):
1. **How many words are you looking for?**
   - `Less than 1,000 words` *(aim for `600–999` words on articles to avoid thin-content penalties, or `~200–400` words for product pages)*
   - `1,000–1,500 words`
   - `1,500–2,000 words`
   - `2,000–2,500 words`
   - `More than 2,500 words` *(Recommended for competitive pillar guides — maximum depth score)*
2. **Should we include an FAQ section in the content?** (`Yes` / `No`)
3. *(Optional)* **First-Hand Experience / E-E-A-T & Publishing Context:** Any personal experience, case study, brand voice, internal link URLs, or output format preference (`Markdown` vs. `Clean HTML`)?

### Phase 4: Grounded Research, Content Generation, 16:9 Featured Image & Audit
Execute all 5 sub-steps below before delivering the final package:

#### 4A. Up-to-Date Grounding (Zero Fake Data / Zero Dummy Content)
- Use live web search/browsing tools when available to gather **current facts, up-to-date statistics, pricing/dates, and real authoritative external sources** (never direct competitors).
- Strip any tracking parameters (`utm_source`, `referrer`, etc.) from URLs.
- **Zero Fabrication Rule:** Never invent statistics, years, quotes, case studies, DOIs, ISBNs, or URLs. Never output placeholders like `[INSERT_URL]`, `2026-XX-XX`, or `example.com/source`.
- For internal links where the user has not supplied real site URLs yet, insert clear editorial slots: `[Internal Link: <descriptive anchor text> -> link to your <topic> page]`.

#### 4B. On-Page SEO, SERP Reach & Readability Execution
Follow [`references/on-page-seo-rules.md`](./references/on-page-seo-rules.md) strictly:
- **SEO Metadata Package (Mandatory — Search-Engine-Limit Validated for Max SERP Reach):**
  - **Meta Title:** `50–60` characters max (strictly `≤ 60` chars so desktop/mobile SERPs do not truncate), Primary Focus Keyword within the first 50%.
  - **Meta Description:** `120–160` characters (sweet spot `140–155` chars for zero truncation on mobile and desktop), unique, compelling CTR copy containing the Primary Focus Keyword.
  - **URL Slug:** Short, lowercase, descriptive, containing the meaningful Primary Focus Keyword terms (trim stop words; keep full URL `≤ 75` chars).
  - **Primary Focus Keyword:** Clearly labeled single target keyword.
  - **Secondary Keywords:** `2–4` related / long-tail keywords (explicitly state `None` only if single-keyword product copy).
- **Keyword Placement & Anti-Pseudo-Stuffing:**
  - Place the Primary Focus Keyword naturally in the **first 10%** of the article (first paragraph).
  - Maintain **1.0%–1.5% keyword density** (hard ceiling `< 2.5%`). If a focus keyword is grammatically clunky, place the exact phrase cleanly in Meta Title, Meta Description, Slug, Opening 10%, one `H2`/`H3`, and one Image Alt Text, then use smooth grammatical variations and synonyms throughout the body.
  - Weave Primary and Secondary Keywords naturally into `H2`/`H3` subheadings.
- **Structure, Scannability & AI-Search Readiness (GEO):**
  - **Strictly one `H1`** (the main article title), followed by logical `H2` → `H3` → `H4` nesting (never skip levels like `H1 → H4`).
  - Include a **40–60 word direct Quick Answer** block right after the opening intro for Featured Snippets and AI-search citations.
  - Include a **Table of Contents** for posts `≥ 1,000` words and at least **1 structured comparison/summary table**.
  - Keep **every paragraph under 120 words** (target 2–4 sentences / ~40–80 words; zero walls of text).
  - Provide real value: concrete examples, actionable steps, real-world experience (from Phase 3 if supplied), and original takeaways (never thin filler).
- **Media Briefs (`4+` visuals for maximum media score):**
  - Include at least **4** in-article image/diagram/video briefs (plus the 16:9 Featured Image), each specifying:
    - Descriptive SEO filename (`.jpg` for photos, `.png` for diagrams/graphics with transparency)
    - `Alt Text` containing the Primary Focus Keyword (naturally on primary visuals)
- **FAQ Block & JSON-LD Schema (if user chose `Yes`):**
  - Add `4–6` concise, high-intent questions (`H2: Frequently Asked Questions` → `H3` per question) with direct, schema-ready answers.
  - Generate valid copy-paste **JSON-LD Schema** (`Article`, plus `FAQPage` when FAQ is included) matching the exact Meta Title, Meta Description, and Q&A content.

#### 4C. Human-Writing & Anti-AI Polish Pass
Review the entire draft against [`references/human-writing-rules.md`](./references/human-writing-rules.md) and eliminate robotic writing patterns:
- **Zero Robotic Vocabulary Clusters:** Remove `delve`, `deep dive`, `tapestry`, `testament`, `landscape` (abstract), `interplay`, `intricate`/`intricacies`, `pivotal`, `crucial`, `underscore` (verb), `showcase`, `foster`, `bolster`, `garner`, `boasts` (meaning "has"), `meticulous`, `vibrant`, `enduring`, `align with`, `enhance`, `highlighting`, `valuable insights`, `multifaceted`, `leverage`, `prioritize`, `dependable`, `quietly`, `steady`, `universally`, `echoed`, and sentence-initial `Additionally,`.
- **Zero Puffery & Trailing `-ing` Commentary:** Cut inflated significance claims and trailing participles (`"...underscoring its importance"`, `"...fostering deeper engagement"`).
- **Plain Verbs Over Circumlocutions:** Prefer `is`, `are`, `has`, `wrote`, `used` over `serves as a`, `stands as a`, `functions as`, `features`, `offers`, `utilized`.
- **Zero Negative Parallelisms & Rule-of-Three Spam:** Cut `"Not just X, but also Y"`, `"It's not X — it's Y"`, `"Y rather than X"`, and repetitive 3-adjective / 3-bullet padding.
- **No Formulaic Closings or Templates:** Do not use `"Challenges and Future Prospects"` or `"In conclusion"` / `"In summary"` / `"Overall"` sections. End with concrete next steps or a direct takeaway.
- **Clean Formatting & Zero Meta-Chatter:** No emoji icons in headings/lists, no bold-label bullet spam (`**Point**: explanation`), no spaced em-dash (` — `) punch-up overuse, and no conversational filler inside the article body.

#### 4D. Featured Image Generation (16:9 Website-Ready)
Every completed article must include a **16:9 featured image** ready to post directly on the user's website:
1. Craft a clean, topic-matched **16:9 visual concept** tied directly to the confirmed title and Primary Focus Keyword (avoid garbled text inside generated visuals unless clean editorial typography is needed).
2. **If an image-generation tool or subagent is available:**
   - Generate the **16:9 aspect ratio** featured image directly and save it with an SEO-friendly filename (e.g., `<primary-keyword-slug>-featured.jpg` or `.png`).
   - Return the **saved image path**, **recommended upload filename**, and **Alt Text** (containing the Primary Focus Keyword).
3. **If no image-generation tool is available** in the current environment:
   - Output a ready-to-run **16:9 Featured Image Prompt** (explicitly specifying `16:9` widescreen editorial composition), **SEO Filename**, and **Alt Text** so the user can generate and upload it immediately.

#### 4E. Automated SEO & Human-Writing Audit
Before sending the final response, run the local audit script if shell access is available:

```bash
python3 <skill_path>/scripts/audit_seo_content.py <article.md> \
  --keyword "<primary focus keyword>" \
  --secondary "<secondary 1>,<secondary 2>" \
  --seo-title "<seo title>" \
  --meta-desc "<meta description>" \
  --slug "<url-slug>" \
  --target-min <min_words> --target-max <max_words>
```

---

## Output Format

Present the final deliverable cleanly in four clearly separated blocks so the user can copy-paste everything straight into their CMS without stripping AI commentary:

1. **SEO Metadata & 16:9 Featured Image Card**
   - **Meta Title** (with exact character count, e.g. `54/60 chars`)
   - **Meta Description** (with exact character count, e.g. `148/160 chars`)
   - **URL Slug**
   - **Primary Focus Keyword**
   - **Secondary Keywords** (if any)
   - **16:9 Featured Image** (saved path or 16:9 prompt + SEO filename + Alt Text)
2. **Clean, Publish-Ready Article** (`H1` → Opening + 40–60w Quick Answer → TOC → Body with `4+` media briefs + Table → Optional FAQ → Concrete ending).
3. **Copy-Paste JSON-LD Schema** (`Article` schema, plus `FAQPage` schema if FAQ was enabled).
4. **Pre-Publish SEO & Human-Writing Scorecard** (Numeric `overall_score` out of `100`, word count, keyword density `%`, max paragraph length, heading hierarchy check, link/media check, and `0` robotic-tells check).
