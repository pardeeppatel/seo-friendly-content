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

### Phase 1: Settings Check, Topic & Focus Keyword Intake
1. **Check Persistent User Settings (`<skill_path>/user-config.json`):**
   - Look for `<skill_path>/user-config.json`:
     ```json
     {
       "output_dir": "/path/to/designated-folder",
       "website_url": "https://yoursite.com",
       "brand_name": "YourSite.com"
     }
     ```
   - **If `user-config.json` already exists** and `output_dir` is set: reuse the saved `output_dir` and optional `website_url`/`brand_name` automatically without re-asking (briefly note them in one line; only update if the user asks to change them).
2. Read the user's topic, niche, or existing draft and check whether they already provided a **Focus Keyword**, **Designated Output Folder**, or **Main Website URL**.
3. **STOP and ask cleanly for any missing items in one combined intake message:**
   - **Focus Keyword** *(if not provided)*: *"Do you already have a **Focus Keyword** (and optional Secondary Keywords) you are targeting, or should I suggest Focus Keywords along with the titles?"*
   - **Designated Output Folder** *(FIRST TIME ONLY, when `user-config.json` has no `output_dir`)*: *"Where should I save your generated content? Each article gets its own subfolder `<folder>/<url-slug>/` holding the article, SEO-named featured image, metadata, and JSON-LD schema. Share a folder path, or reply `default` to use `./seo-content` in your current workspace. (Saved for future runs.)"*
   - **Main Website URL *(Optional — FIRST TIME ONLY, or whenever changing site)*:** *"Optional: What is your main **Website URL** (e.g., `https://yoursite.com`)? If shared, I will use it for better internal linking, JSON-LD schema URLs, and subtle domain branding on your 16:9 featured image. (Reply `skip` to leave blank.)"*
4. As soon as the user confirms their folder (and optional website URL, or `skip`), save `<skill_path>/user-config.json` immediately so next time the skill opens ready to use that exact folder and site. *(Store `website_url: ""` when skipped so you do not re-ask on future runs.)*

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

### Phase 4: Grounded Research, Content Generation, Branded 16:9 Image, Audit & Export
Execute all 6 sub-steps below before delivering the final package:

#### 4A. Up-to-Date Grounding & Website Internal Linking (Zero Fake Data)
- Use live web search/browsing tools when available to gather **current facts, up-to-date statistics, pricing/dates, and real authoritative external sources** (never direct competitors of the user's site).
- Strip any tracking parameters (`utm_source`, `referrer`, etc.) from URLs.
- **Website URL Internal Linking (when `website_url` is set):**
  - Search `site:<domain> <topic keywords>` via web search when available to discover **verified live pages** on the user's site that fit naturally as internal links.
  - Only insert full internal URLs you directly verified in search results or user input. Never guess or invent URLs on their domain.
  - For unverified related topics (or when no `website_url` is set), insert clear editorial slots: `[Internal Link: <descriptive anchor text> -> link to your <topic> page]` (or mention `<domain>` as the target site).
- **Zero Fabrication Rule:** Never invent statistics, years, quotes, case studies, DOIs, ISBNs, or URLs. Never output placeholders like `[INSERT_URL]` or `2026-XX-XX`.

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
- **In-Article Visuals & Media Briefs (`4+` visuals for maximum media score):**
  - Include at least **4** in-article visuals or media briefs (in addition to the 16:9 Featured Image), each with a descriptive SEO filename (`.jpg` for photos/editorial visuals, `.png` for graphics) and `Alt Text` containing the Primary Focus Keyword on primary visuals.
  - When an image-generation tool or subagent is available, generate applicable clean in-article images (see `4D`) and embed them directly as `![<Alt Text>](./images/<seo-filename>)`; use clean Mermaid diagrams or concise Media Briefs only where dense readable text or live product screenshots are needed.
- **FAQ Block & JSON-LD Schema (always include `Article`; add `FAQPage` if user chose `Yes`):**
  - Add `4–6` concise, high-intent questions (`H2: Frequently Asked Questions` → `H3` per question) with direct, schema-ready answers when FAQ is enabled.
  - Generate valid copy-paste **JSON-LD Schema** (`Article`, plus `FAQPage` when FAQ is included) matching the exact Meta Title, Meta Description, and Q&A content. When `website_url` is configured, populate `mainEntityOfPage.@id`, `publisher.name`, `publisher.url`, and featured `image` paths with `<website_url>/<url-slug>`.

#### 4C. Human-Writing & Anti-AI Polish Pass
Review the entire draft against [`references/human-writing-rules.md`](./references/human-writing-rules.md) and eliminate robotic writing patterns:
- **Zero Robotic Vocabulary Clusters:** Remove `delve`, `deep dive`, `tapestry`, `testament`, `landscape` (abstract), `interplay`, `intricate`/`intricacies`, `pivotal`, `crucial`, `underscore` (verb), `showcase`, `foster`, `bolster`, `garner`, `boasts` (meaning "has"), `meticulous`, `vibrant`, `enduring`, `align with`, `enhance`, `highlighting`, `valuable insights`, `multifaceted`, `leverage`, `prioritize`, `dependable`, `quietly`, `steady`, `universally`, `echoed`, and sentence-initial `Additionally,`.
- **Zero Puffery & Trailing `-ing` Commentary:** Cut inflated significance claims and trailing participles (`"...underscoring its importance"`, `"...fostering deeper engagement"`).
- **Plain Verbs Over Circumlocutions:** Prefer `is`, `are`, `has`, `wrote`, `used` over `serves as a`, `stands as a`, `functions as`, `features`, `offers`, `utilized`.
- **Zero Negative Parallelisms & Rule-of-Three Spam:** Cut `"Not just X, but also Y"`, `"It's not X — it's Y"`, `"Y rather than X"`, and repetitive 3-adjective / 3-bullet padding.
- **No Formulaic Closings or Templates:** Do not use `"Challenges and Future Prospects"` or `"In conclusion"` / `"In summary"` / `"Overall"` sections. End with concrete next steps or a direct takeaway.
- **Clean Formatting & Zero Meta-Chatter:** No emoji icons in headings/lists, no bold-label bullet spam (`**Point**: explanation`), no spaced em-dash (` — `) punch-up overuse, and no conversational filler inside the article body.

#### 4D. Niche-Matched Visuals: Branded 16:9 Featured Image & In-Article Images
Every completed article must include custom visuals tailored to its topic vibe (never a repetitive template):

1. **Niche-Matched Visual Direction & Anti-Cliché Rule (Mandatory):**
   - **Never repeat a generic template:** Do **not** default to *"desk + laptop + notebook + coffee cup"* unless the topic is specifically about desk setups, stationery, or journaling.
   - **Match style, setting, palette & lighting to the article's niche and search intent:**
     - *Travel / Study Abroad / Cities:* Real atmospheric destination, transit, or architectural photography in natural light (not an indoor study desk).
     - *Tech / SaaS / Developer / AI:* Sleek 3D isometric architecture metaphors, dark-mode minimal geometry, or clean hardware/interface macro photography.
     - *Comparisons ("X vs Y") / Decisions:* Split-frame dual-tone visual contrast or balanced symbolic object pairing with high negative space.
     - *Product / Gear Reviews:* Studio hero macro shot with directional rim lighting and shallow depth of field.
     - *Finance / Legal / Strategy:* Minimalist editorial illustration, modern architectural lines, or symbolic 3D sculpture concepts.
     - *Health / Wellness / Food / Home:* Natural daylight documentary or crisp texture-rich studio photography.
   - **Vary Framing:** Rotate wide environmental shots, shallow-DOF macros, split comparisons, and minimal illustrations so every post—and every image inside a post—feels custom art-directed.
2. **Optional Website Branding (Featured Image):** If `website_url` (or `brand_name`) is set in `user-config.json` or prompt context, add a **subtle, crisp domain badge or corner watermark** (e.g., minimalist bottom-right pill or clean editorial corner typography reading `<domain>` such as `YourSite.com`) without obscuring the main subject. Inspect the generated image visually to confirm accurate spelling and clean composition.
3. **Generate 16:9 Featured Image + Applicable In-Article Images (when image-gen tool/subagent is available):**
   - **16:9 Featured Image:** Generate a `16:9` aspect-ratio featured image matching the niche direction above, and save/copy it to `<output_dir>/<url-slug>/<url-slug>-featured.jpg` (or `.png`). Return its saved path, SEO filename, and Alt Text.
   - **In-Article Images (`images/`):** For each in-article visual slot where conceptual, photographic, architectural, comparison, or illustrated imagery applies cleanly (avoiding visuals that depend on tiny paragraphs of AI-rendered text), generate the actual image too, save it as `<output_dir>/<url-slug>/images/<in-article-seo-filename>.jpg` (or `.png`), visually inspect it, and embed `![<Alt Text>](./images/<in-article-seo-filename>.jpg)` directly inside `article.md`. For dense step-by-step text charts or UI screenshots where AI text rendering is unsuitable, keep clean Mermaid diagrams or concise Media Briefs instead.
4. **If no image-generation tool is available** in the current environment:
   - Output a ready-to-run **16:9 Featured Image Prompt** (following the niche direction + subtle `<domain>` corner branding when `website_url` is set) plus custom niche-matched prompts, **SEO Filenames**, and **Alt Text** for all in-article visual briefs.

#### 4E. Automated SEO & Human-Writing Audit
Before saving and sending the final response, run the local audit script if shell access is available:

```bash
python3 <skill_path>/scripts/audit_seo_content.py <output_dir>/<url-slug>/article.md \
  --keyword "<primary focus keyword>" \
  --secondary "<secondary 1>,<secondary 2>" \
  --seo-title "<seo title>" \
  --meta-desc "<meta description>" \
  --slug "<url-slug>" \
  --site-url "<website_url_if_set>" \
  --target-min <min_words> --target-max <max_words>
```

#### 4F. Save Organized Article Bundle (`<output_dir>/<url-slug>/`)
Inside the user's saved `output_dir`, create a dedicated subfolder named after the article's **URL Slug** (`<output_dir>/<url-slug>/`) so every article and all of its images stay neatly isolated and easy to manage:
- `<output_dir>/<url-slug>/article.md` — clean publish-ready article (or `article.html` if requested) with generated images embedded cleanly
- `<output_dir>/<url-slug>/<url-slug>-featured.jpg` *(or `.png`)* — branded 16:9 featured image renamed cleanly to its exact SEO filename
- `<output_dir>/<url-slug>/images/<seo-filename>.jpg` *(or `.png`)* — generated in-article visuals (when applicable)
- `<output_dir>/<url-slug>/seo-metadata.md` — Meta Title, Meta Description, URL Slug, Primary/Secondary Keywords, Website URL, Featured Image Alt Text, and Audit Scorecard
- `<output_dir>/<url-slug>/schema.json` — valid JSON-LD `Article` (+ optional `FAQPage`) schema

---

## Output Format

Present the final deliverable cleanly in four clearly separated blocks so the user can either use the saved bundle in `<output_dir>/<url-slug>/` or copy-paste directly into their CMS:

1. **SEO Metadata, Saved Folder & 16:9 Featured Image Card**
   - **Saved Article Folder** (`<output_dir>/<url-slug>/` listing the saved files)
   - **Website URL** (if configured)
   - **Meta Title** (with exact character count, e.g. `54/60 chars`)
   - **Meta Description** (with exact character count, e.g. `148/160 chars`)
   - **URL Slug**
   - **Primary Focus Keyword**
   - **Secondary Keywords** (if any)
   - **16:9 Featured Image** (saved path in `<url-slug>/`, branding status, SEO filename, Alt Text — or 16:9 prompt when image-gen is unavailable)
2. **Clean, Publish-Ready Article** (`H1` → Opening + 40–60w Quick Answer → TOC → Body with `4+` media briefs + Table → Optional FAQ → Concrete ending).
3. **Copy-Paste JSON-LD Schema** (`Article` schema, plus `FAQPage` schema if FAQ was enabled).
4. **Pre-Publish SEO & Human-Writing Scorecard** (Numeric `overall_score` out of `100`, word count, keyword density `%`, max paragraph length, heading hierarchy check, link/media check, and `0` robotic-tells check).
