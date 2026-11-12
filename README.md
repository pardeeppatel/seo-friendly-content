# SEO Friendly Content v1.1.0

> **Interactive On-Page SEO Engine, Human-Writing Polisher & Branded 16:9 Featured Image Workflow**  
> *Crafted for Antigravity, Cursor, Claude Code & Generic AI Coding Assistants.*

[![Version](https://img.shields.io/badge/version-1.1.0-indigo.svg)](package.json)
[![License: Free to Use (Not Open Source)](https://img.shields.io/badge/License-Free%20to%20Use%20(Proprietary)-blue.svg)](LICENSE)
[![Credit](https://img.shields.io/badge/Developed%20by-Pardeep%20Kumar-orange.svg)](https://github.com/PardeepPatel)
[![Powered By](https://img.shields.io/badge/Powered%20by-ToolNPlay.com-purple.svg)](https://ToolNPlay.com)

---

<p align="center">
  <img src="assets/featured-preview.jpg" alt="SEO Friendly Content Preview" width="100%">
</p>

---

## What It Does

**SEO Friendly Content** turns your AI assistant into a structured editorial writer that pairs **strict on-page SEO engineering** with **natural, human-sounding prose**:

1. **Interactive 4-Phase Workflow:** Never rushes into generic text. Walks you through Focus Keyword selection, 10 title options (with regeneration), word count selection, and FAQ inclusion.
2. **High-CTR Title Engineering:** Places your Focus Keyword in the first 50% (`≤ 60` chars total), pairing numbers, power words, and non-clickbait sentiment triggers.
3. **Full On-Page SEO Compliance:** Enforces clean URL slugs (`≤ 75` chars total URL), meta descriptions (`120–160` chars), first-10% keyword placement, `1.0%–1.5%` keyword density (without awkward pseudo-stuffing), strict `H1 → H2 → H3` hierarchy, Table of Contents, short paragraphs (`≤ 120` words), `4+` media briefs with alt text, and authoritative external/internal link slots.
4. **Human-Writing Guardrails:** Actively strips robotic vocabulary clusters, trailing `-ing` puffery, negative parallelisms, rule-of-three padding, spaced em-dash spam, and placeholder leaks.
5. **Up-to-Date Grounding (Zero Dummy Data):** Uses real, current facts and verifiable sources with zero fabricated URLs or fake statistics.
6. **16:9 Website-Ready Featured Image (with Optional Site Branding):** Generates (or prepares) a 16:9 featured image saved cleanly with its SEO filename, keyword-rich alt text, and subtle corner branding when you provide your main Website URL.
7. **Organized Per-Article Folder Management:** Asks once for your designated output folder (remembered across future sessions in `user-config.json`), then creates a clean `<output_dir>/<url-slug>/` bundle for every article (`article.md`, `<url-slug>-featured.jpg`, `seo-metadata.md`, and `schema.json`).
8. **Deterministic Python Auditor:** Verifies word count, keyword density, heading structure, paragraph lengths, internal/external links (`--site-url`), and scans for robotic writing patterns before final delivery.

---

## Installation

### Method A: One-Command Install via GitHub (Recommended)

Run in your Terminal (`macOS`/`Linux`) or PowerShell (`Windows`):

#### 1. Antigravity (Global — All Workspaces)
```bash
npx github:pardeeppatel/seo-friendly-content --global
```

#### 2. Antigravity (Current Workspace Only)
```bash
npx github:pardeeppatel/seo-friendly-content --gemini
```

#### 3. Cursor
```bash
npx github:pardeeppatel/seo-friendly-content --cursor
```

#### 4. Claude Code
```bash
npx github:pardeeppatel/seo-friendly-content --claude
```

#### 5. Generic `.agents/` Workspace Skill
```bash
npx github:pardeeppatel/seo-friendly-content --agents
```

### Method B: Clone & Install Locally

```bash
git clone https://github.com/PardeepPatel/seo-friendly-content.git
cd seo-friendly-content
node bin/cli.js --global
```

---

## How to Update

To update an existing installation to the latest version across your global and local skill directories:

```bash
npx github:pardeeppatel/seo-friendly-content --update
```

If you cloned the repository locally:

```bash
cd seo-friendly-content
git pull origin main
node bin/cli.js --update
```

> Your files in `~/.gemini/config/skills/seo-friendly-content` (and any detected `.agents`, `.cursor`, or `.claude` skill folders) are refreshed immediately—no IDE restart required.

---

## How to Use

Once installed, give your AI assistant any content topic or refresh request:

**Example Prompts:**
* *"Write an SEO-friendly article on Cloud Cost Optimization using seo-friendly-content"*
* *"Create a product guide for ergonomic standing desks"*
* *"Rewrite and optimize this draft for better search rankings"*

### Step-by-Step Interactive Flow

1. **First-Time Folder & Optional Website Setup:** On your first run, the assistant asks for a **designated output folder** (saved to `user-config.json` and reused automatically on future runs) plus an **optional Website URL** (used for better internal linking, JSON-LD URLs, and subtle 16:9 featured image branding).
2. **Focus Keyword Check:** The assistant asks whether you already have a Focus Keyword (and optional Secondary Keywords) or want suggestions.
3. **10 SEO Title Suggestions:**
   * If you **have** a Focus Keyword, it generates **10 titles** built around that keyword (keyword in the first 50%, `≤ 60` chars, number + power word + sentiment).
   * If you **don't**, it proposes **10 Title + Focus Keyword + Secondary Keyword** pairs.
   * Pick `#1–#10` or ask to regenerate 10 fresh options.
4. **Word Count & FAQ Selection:** Choose your target length (`< 1,000`, `1,000–1,500`, `1,500–2,000`, `2,000–2,500`, or `> 2,500` words) and whether to include a schema-ready **FAQ section** (`Yes` / `No`).
5. **Organized Output Folder + Chat Deliverable:** Saves `<output_dir>/<url-slug>/` (`article.md`, `<url-slug>-featured.jpg`, `seo-metadata.md`, `schema.json`) and outputs all 4 copy-paste blocks in chat:
   * **SEO Metadata & Saved Bundle Card** (Meta Title, Meta Description, Slug, Keywords, Saved Path)
   * **16:9 Featured Image** (branded if Website URL is set, with SEO filename & alt text)
   * **Clean, Publish-Ready Article** (`H1` → Quick Answer → TOC → Body → `4+` Media Briefs → Table → Optional FAQ)
   * **Copy-Paste JSON-LD Schema + Automated Audit Scorecard** (`word_count`, `density %`, `paragraphs > 120 words`, `headings`, `human_writing_scan`)

### Running the Standalone SEO Auditor CLI

```bash
python3 skill/scripts/audit_seo_content.py article.md \
  --keyword "your focus keyword" \
  --secondary "secondary one,secondary two" \
  --seo-title "Your SEO Title Here" \
  --meta-desc "Your 120-160 character meta description containing your focus keyword." \
  --slug "your-focus-keyword" \
  --site-url "https://yoursite.com" \
  --target-min 1500 --target-max 2000
```

---

## Repository Structure

```text
seo-friendly-content/
├── bin/
│   └── cli.js                             # Installer, updater & CLI wrapper
├── skill/
│   ├── SKILL.md                           # Core interactive skill workflow
│   ├── references/
│   │   ├── on-page-seo-rules.md           # On-page SEO thresholds & mistake prevention
│   │   ├── human-writing-rules.md         # Anti-AI writing & human-prose rules
│   │   └── title-formulas.md              # Title templates, power words & sentiment
│   └── scripts/
│       └── audit_seo_content.py           # Zero-dependency SEO + human-writing linter
├── assets/
│   └── featured-preview.jpg               # 16:9 banner preview
├── LICENSE                                # Free-to-Use Proprietary License
├── package.json
└── README.md
```

---

## License & Terms of Use

* **License:** **Free to Use — Proprietary Freeware (NOT Open Source)** — see [LICENSE](LICENSE).
* **100% Free to Use:** Free for personal, client, blog, agency, and commercial website content. You retain 100% ownership of all articles and images you generate.
* **Not Open Source / No Redistribution:** You may not resell, redistribute, rebrand, mirror, or repackage this skill, its scripts, rulebooks, or workflows as a competing product or agent skill.

---

## Credits

* **Developed by:** **[Pardeep Kumar](https://github.com/PardeepPatel)**
* **Powered by:** **[ToolNPlay.com](https://ToolNPlay.com)**
