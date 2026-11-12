# On-Page SEO & Readability Rules Reference

> **Developed by Pardeep Kumar** | **Powered by [ToolNPlay.com](https://ToolNPlay.com)**

---

## 1. Score Thresholds & Guiding Principle
- **81–100 (Strong):** Ready to publish (aim as close to 100 as natural readability allows).
- **51–80 (Moderate):** Needs further on-page optimization.
- **0–50 (Weak):** Missing foundational SEO elements.
- **UX-First Rule:** Readers come first, search engines second. Never force unnatural phrasing just to hit a numeric target.

---

## 2. Foundational On-Page Checklist

| Check | Scope | Exact Requirement |
| :--- | :--- | :--- |
| **Focus Keyword in Meta Title** | Primary only | Include Primary Focus Keyword in Meta Title within the **first 50%** (ideally **first 50 characters**). Keep total Meta Title **50–60 characters** (max 60) so desktop and mobile SERPs display it without truncation. |
| **Focus Keyword in Meta Description** | Primary only | Include Primary Focus Keyword within **120–160 characters** (sweet spot **140–155 characters** for desktop + mobile SERPs). Summarize value and match search intent to drive CTR. |
| **Focus Keyword in URL Slug** | Primary only | Include meaningful Primary Focus Keyword terms in a clean, descriptive, lowercase slug (trim filler/stop words). |
| **Keyword in First 10% of Content** | Primary only | Appear naturally within the **first 10%** of the article (or anywhere in the post if `< 300` words). |
| **Focus Keyword in Content** | Primary + Secondary | Include all focus keywords naturally across the body (singular/plural supported). |
| **Overall Content Length** | Content-only | `> 2,500` words = 100% \| `2,000–2,500` = 70% \| `1,500–2,000` = 60% \| `1,000–1,500` = 40% \| `600–1,000` = 20% \| `< 600` = 0%. *(Exception: Product pages ~200+ words.)* |

---

## 3. Additional On-Page & Linking Checklist

| Check | Scope | Exact Requirement |
| :--- | :--- | :--- |
| **Focus Keyword in Subheadings** | Primary + Secondary | Include Primary and Secondary Keywords naturally in `H2` / `H3` headings (improves relevance and SERP sitelinks). |
| **Focus Keyword in Image Alt Text** | Primary only | Include Primary Focus Keyword (singular or plural) descriptively in key image `alt` attributes. |
| **Keyword Density** | Primary + Secondary | Target **1.0%–1.5%**. Hard warning ceiling at **> 2.5%**. Lower natural density is safer than stuffing. |
| **URL Length** | Page URL | Keep the **full URL ≤ 75 characters** (`domain + slug`). Keep slugs short and free of filler words. |
| **External Links (`dofollow`)** | Content-only | Link to **authoritative, relevant external sources** with at least one followed (`dofollow`) link. Never link to direct competitors or low-quality/link-farm sites. |
| **Internal Links** | Content-only | Link contextually to relevant pages/posts on the same site (or subdomain/main domain) using descriptive, keyword-rich anchor text. Prevents orphan pages. |
| **Keyword Uniqueness** | Primary only | Never target the exact same Primary Focus Keyword across multiple posts (prevents cannibalization and duplicate content). |

---

## 4. Title & Content Readability Checklist

### Title Readability
1. **Keyword Position:** Primary Focus Keyword appears in the **first 50%** of the SEO title.
2. **Sentiment:** Evokes strong positive or negative emotion/curiosity—**strictly without clickbait** (exaggerated titles trigger pogo-sticking/bounces).
3. **Power Word:** Contains at least one compelling power word.
4. **Number:** Contains a number (e.g., `7`, `10+`, `2026`).

### Content Readability
1. **Table of Contents (TOC):** Include a TOC on long-form guides (`≥ 1,000` words) for navigation and potential SERP jump-to links.
2. **Short Paragraphs:** **No paragraph may exceed 120 words** (any single paragraph over 120 words fails readability checks). Target 2–4 sentences (~40–80 words).
3. **Media Presence:** Include **at least 4 images or videos** for a 100% media score (`1` passes partially; `4+` achieves 100%). Recommend JPEG for photos, PNG for transparent graphics/diagrams, compressed sizes, and descriptive filenames.

---

## 5. Content & On-Page Mistakes to Actively Prevent
- **Poor Keyword Research:** Avoid vague or impossible head terms when a specific **long-tail keyword** better matches intent.
- **Keyword Stuffing ("Pseudo-Stuffing"):** Never repeat exact keywords robotically. Satisfy strict placement checks cleanly, then rely on **synonyms, semantic variants, and natural phrasing** in body prose.
- **Thin / Low-Quality Content:** Always match **search intent** (informational, transactional, comparison), include **real-life examples, step-by-step instructions, accurate data, and original insights**.
- **Broken Heading Hierarchy:** Exactly **one `H1`** per page; never skip heading levels (`H1 → H2 → H3 → H4`).
- **Stale / Outdated Content:** Use up-to-date statistics, current-year context, and verified references.
- **Missing Schema Readiness:** Structure FAQs, How-Tos, and Product specs cleanly so they map directly to structured data (FAQ / Article / HowTo / Product Schema).

---

## 6. Featured Snippets & AI-Search Readiness (GEO / AEO)
To maximize reach in both traditional SERPs and AI-generated answer boxes:
- **40–60 Word Direct Quick Answer:** Place a concise, self-contained answer block right after the opening hook (or under key question headings) so search engines can extract it cleanly for featured snippets and AI citations.
- **Structured Comparison Tables & Steps:** Include at least one clean Markdown table or numbered step block summarizing specs, pros/cons, or workflows.
- **Copy-Paste JSON-LD Schema:** Emit valid `Article` JSON-LD (and `FAQPage` JSON-LD when an FAQ section is included) matching the exact Meta Title, Meta Description, and Q&A pairs.
