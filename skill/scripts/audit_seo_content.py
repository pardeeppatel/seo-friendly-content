#!/usr/bin/env python3
"""Deterministic On-Page SEO & Human-Writing Auditor.

Developed by Pardeep Kumar (ToolNPlay.com).
Checks a Markdown article against on-page SEO readability thresholds and
scans for high-risk robotic writing patterns and placeholder leaks.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROBOTIC_VOCAB_PATTERNS: list[tuple[str, str]] = [
    ("delve", r"\bdelv(?:e|ed|es|ing)\b"),
    ("deep dive", r"\bdeep\s+dive\b"),
    ("tapestry", r"\btapestry\b"),
    ("testament", r"\btestament\b"),
    ("landscape (abstract)", r"\blandscape\b"),
    ("interplay", r"\binterplay\b"),
    ("intricate/intricacies", r"\bintricat(?:e|ely)\b|\bintricacies\b"),
    ("pivotal", r"\bpivotal\b"),
    ("crucial", r"\bcrucial\b"),
    ("underscore", r"\bunderscor(?:e|ed|es|ing)\b"),
    ("showcase", r"\bshowcas(?:e|ed|es|ing)\b"),
    ("foster", r"\bfoster(?:ed|ing|s)?\b"),
    ("bolster", r"\bbolster(?:ed|ing|s)?\b"),
    ("garner", r"\bgarner(?:ed|ing|s)?\b"),
    ("boasts", r"\bboasts\b"),
    ("meticulous", r"\bmeticulous(?:ly)?\b"),
    ("vibrant", r"\bvibrant\b"),
    ("enduring", r"\benduring\b"),
    ("align with", r"\balign(?:s|ed|ing)?\s+with\b"),
    ("enhance", r"\benhanc(?:e|ed|es|ing)\b"),
    ("highlighting", r"\bhighlighting\b"),
    ("valuable insights", r"\bvaluable\s+insights\b"),
    ("multifaceted", r"\bmultifaceted\b"),
    ("leverage (buzzword)", r"\bleverag(?:e|ed|es|ing)\b"),
    ("universally", r"\buniversally\b"),
    ("Additionally (sentence start)", r"(?:^|\n)\s*Additionally,"),
]

ROBOTIC_PHRASE_PATTERNS: list[tuple[str, str]] = [
    ("serves/stands as", r"\b(?:serves|stands|functions|operates)\s+as\s+(?:a|an|the)\b"),
    ("Not just/only ... but", r"\bnot\s+(?:just|only)\b[^.!?\n]{1,120}\bbut\b"),
    ("Challenges and Future", r"\bchallenges\s+and\s+future\b"),
    ("In summary/conclusion", r"(?:^|\n)\s*(?:#+\s*)?(?:in\s+summary|in\s+conclusion|overall,)\b"),
    ("It is important to note", r"\bit\s+is\s+(?:important|crucial|worth)\s+to\s+(?:note|remember)\b"),
    ("Tracking parameter leak", r"(?:utm_source=|referrer=)"),
    ("Placeholder URL / date", r"(?:example\.com/|INSERT_SOURCE_URL|20\d\d-XX-XX)"),
]


def strip_markdown(text: str) -> str:
    """Return plain prose tokens from Markdown for word and density counts."""
    cleaned = re.sub(r"```.*?```", " ", text, flags=re.S)
    cleaned = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r" \1 ", cleaned)
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r" \1 ", cleaned)
    cleaned = re.sub(r"[#*_`>|~]", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def count_words(text: str) -> int:
    """Count word tokens in text."""
    return len(re.findall(r"\b[\w'-]+\b", text))


def count_keyword_occurrences(text: str, keyword: str) -> int:
    """Count case-insensitive whole-phrase occurrences (including simple plural)."""
    kw = keyword.strip()
    if not kw:
        return 0
    escaped = re.escape(kw)
    pattern = rf"\b{escaped}s?\b"
    return len(re.findall(pattern, text, flags=re.I))


def split_paragraphs(md: str) -> list[tuple[int, str]]:
    """Split Markdown into prose paragraphs with starting line numbers."""
    paragraphs: list[tuple[int, str]] = []
    buf: list[str] = []
    start_line = 1
    in_code = False

    for idx, line in enumerate(md.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        is_block_break = (
            not stripped
            or stripped.startswith("#")
            or stripped.startswith(("- ", "* ", "> ", "|"))
            or bool(re.match(r"^\d+\.\s", stripped))
            or stripped.startswith("![")
        )
        if is_block_break:
            if buf:
                paragraphs.append((start_line, " ".join(buf)))
                buf = []
            continue
        if not buf:
            start_line = idx
        buf.append(stripped)

    if buf:
        paragraphs.append((start_line, " ".join(buf)))
    return paragraphs


def audit_headings(md: str, primary: str, secondary: list[str]) -> dict:
    """Check H1 uniqueness, level jumps, and keyword usage in subheadings."""
    headings: list[tuple[int, int, str]] = []
    in_code = False
    for idx, line in enumerate(md.splitlines(), start=1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{1,6})\s+(.+)$", line.strip())
        if m:
            headings.append((idx, len(m.group(1)), m.group(2).strip()))

    h1_count = sum(1 for _, lvl, _ in headings if lvl == 1)
    skipped_levels: list[str] = []
    prev_lvl = 0
    for line_no, lvl, text in headings:
        if prev_lvl and lvl > prev_lvl + 1:
            skipped_levels.append(f"Line {line_no}: H{prev_lvl} -> H{lvl} ({text})")
        prev_lvl = lvl

    subheadings = [text for _, lvl, text in headings if lvl in (2, 3)]
    primary_in_sub = any(count_keyword_occurrences(h, primary) > 0 for h in subheadings)
    secondary_in_sub = {
        kw: any(count_keyword_occurrences(h, kw) > 0 for h in subheadings)
        for kw in secondary
        if kw.strip()
    }

    return {
        "h1_count": h1_count,
        "total_headings": len(headings),
        "skipped_levels": skipped_levels,
        "primary_in_subheading": primary_in_sub,
        "secondary_in_subheadings": secondary_in_sub,
    }


def audit_media_and_links(md: str, primary: str) -> dict:
    """Check Markdown images, media briefs, alt text, and internal/external links."""
    md_images = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", md)
    alt_matches = list(re.finditer(r"Alt(?:\s+Text)?:\s*[`\"']?([^`\"\n]+)", md, flags=re.I))
    brief_matches = re.findall(
        r"(?:IMAGE|VIDEO|MEDIA|INFOGRAPHIC)\s*(?:BRIEF|PLACEHOLDER)?", md, flags=re.I
    )

    alts = [alt for alt, _ in md_images] + [m.group(1).strip() for m in alt_matches]
    primary_in_alt = any(count_keyword_occurrences(a, primary) > 0 for a in alts)

    links = re.findall(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", md)
    external_links = [u for _, u in links if u.startswith(("http://", "https://"))]
    internal_links = [u for _, u in links if u.startswith("/") and not u.startswith("//")]
    internal_slots = len(re.findall(r"\[Internal Link:", md, flags=re.I))

    return {
        "markdown_images": len(md_images),
        "media_briefs_detected": len(brief_matches),
        "total_media_items": max(len(md_images), len(brief_matches)),
        "primary_in_alt_text": primary_in_alt,
        "external_links": len(external_links),
        "internal_links_or_slots": len(internal_links) + internal_slots,
    }


STOP_WORDS = {"a", "an", "the", "for", "of", "in", "on", "to", "and", "or", "with", "by", "at", "from"}


def check_slug(slug: str, primary: str) -> dict:
    """Validate slug contains meaningful keyword tokens and stays concise."""
    if not slug:
        return {"text": "", "length": 0, "ok_concise": None, "keyword_present": None}
    slug_norm = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")
    slug_tokens = set(slug_norm.split("-"))
    kw_tokens = [t for t in re.findall(r"[a-z0-9]+", primary.lower()) if t not in STOP_WORDS]
    if not kw_tokens:
        kw_tokens = re.findall(r"[a-z0-9]+", primary.lower())
    exact_match = primary.lower().replace(" ", "-") in slug_norm
    tokens_match = bool(kw_tokens) and all(tok in slug_tokens for tok in kw_tokens)
    return {
        "text": slug,
        "length": len(slug),
        "ok_concise": len(slug) <= 60,
        "keyword_present": exact_match or tokens_match,
    }


def compute_score(
    total_words: int,
    target_min: int | None,
    seo_title: str,
    title_len: int,
    kw_in_title_first_half: bool | None,
    meta_desc: str,
    meta_len: int,
    kw_in_meta: bool | None,
    slug_info: dict,
    kw_in_first_10_pct: bool,
    primary_density_pct: float,
    headings: dict,
    long_paragraphs: list[dict],
    media_links: dict,
    robotic_count: int,
) -> dict:
    """Compute a transparent 0-100 on-page SEO and human-writing score."""
    checks: dict[str, dict] = {}
    max_applicable = 0
    earned = 0

    def add_check(name: str, pts: int, max_pts: int, passed: bool | str) -> None:
        nonlocal max_applicable, earned
        max_applicable += max_pts
        earned += pts
        checks[name] = {"score": pts, "max": max_pts, "status": passed}

    if seo_title:
        add_check("meta_title_length_<=60", 5 if title_len <= 60 else 0, 5, title_len <= 60)
        add_check("keyword_in_title_first_50_pct", 5 if kw_in_title_first_half else 0, 5, bool(kw_in_title_first_half))
    else:
        checks["meta_title"] = {"score": 0, "max": 10, "status": "not_provided"}

    if meta_desc:
        add_check("meta_description_120_160", 5 if 120 <= meta_len <= 160 else 0, 5, 120 <= meta_len <= 160)
        add_check("keyword_in_meta_description", 5 if kw_in_meta else 0, 5, bool(kw_in_meta))
    else:
        checks["meta_description"] = {"score": 0, "max": 10, "status": "not_provided"}

    if slug_info["text"]:
        slug_ok = bool(slug_info["keyword_present"] and slug_info["ok_concise"])
        add_check("keyword_in_concise_slug", 5 if slug_ok else 0, 5, slug_ok)
    else:
        checks["url_slug"] = {"score": 0, "max": 5, "status": "not_provided"}

    add_check("keyword_in_first_10_pct", 10 if kw_in_first_10_pct else 0, 10, kw_in_first_10_pct)

    if total_words >= 2500 or (target_min is not None and total_words >= target_min and target_min >= 600):
        wc_pts = 15 if total_words >= 2500 else 12 if total_words >= 2000 else 10 if total_words >= 1500 else 8 if total_words >= 1000 else 5
    elif total_words >= 2000:
        wc_pts = 12
    elif total_words >= 1500:
        wc_pts = 10
    elif total_words >= 1000:
        wc_pts = 7
    elif total_words >= 600:
        wc_pts = 4
    else:
        wc_pts = 0
    add_check("content_depth_word_count", wc_pts, 15, wc_pts >= 10)

    add_check("keyword_in_subheading", 5 if headings["primary_in_subheading"] else 0, 5, headings["primary_in_subheading"])
    add_check("keyword_in_image_alt", 5 if media_links["primary_in_alt_text"] else 0, 5, media_links["primary_in_alt_text"])

    if 1.0 <= primary_density_pct <= 1.5:
        dens_pts, dens_ok = 5, True
    elif 0.5 <= primary_density_pct <= 2.5:
        dens_pts, dens_ok = 3, "acceptable"
    else:
        dens_pts, dens_ok = 0, False
    add_check("keyword_density_1.0_to_1.5_pct", dens_pts, 5, dens_ok)

    add_check("external_links_present", 5 if media_links["external_links"] >= 1 else 0, 5, media_links["external_links"] >= 1)
    add_check("internal_links_present", 5 if media_links["internal_links_or_slots"] >= 1 else 0, 5, media_links["internal_links_or_slots"] >= 1)

    h_ok = headings["h1_count"] == 1 and not headings["skipped_levels"]
    add_check("heading_hierarchy_valid", 5 if h_ok else 0, 5, h_ok)
    add_check("all_paragraphs_<=120_words", 5 if not long_paragraphs else 0, 5, not long_paragraphs)

    media_cnt = media_links["total_media_items"]
    media_pts = 5 if media_cnt >= 4 else 3 if media_cnt >= 1 else 0
    add_check("media_count_4_plus", media_pts, 5, media_cnt >= 4)

    ai_pts = 10 if robotic_count == 0 else 5 if robotic_count <= 2 else 0
    add_check("human_writing_0_robotic_tells", ai_pts, 10, robotic_count == 0)

    norm_pct = round((earned / max(1, max_applicable)) * 100)
    rating = "Strong (81-100)" if norm_pct >= 81 else "Moderate (51-80)" if norm_pct >= 51 else "Weak (0-50)"

    return {
        "overall_score": earned,
        "max_possible_on_provided_fields": max_applicable,
        "normalized_score_pct": norm_pct,
        "rating": rating,
        "checks": checks,
    }


def scan_robotic_tells(md: str) -> list[dict]:
    """Scan text for overused robotic vocabulary, phrasing crutches, and leaks."""
    findings: list[dict] = []
    lines = md.splitlines()
    for label, pattern in ROBOTIC_VOCAB_PATTERNS + ROBOTIC_PHRASE_PATTERNS:
        regex = re.compile(pattern, flags=re.I | re.M)
        for line_no, line in enumerate(lines, start=1):
            for match in regex.finditer(line):
                findings.append(
                    {"rule": label, "line": line_no, "match": match.group(0).strip()}
                )
    return findings


def run_audit(args: argparse.Namespace) -> dict:
    """Run full SEO + human-writing audit and return structured results."""
    raw = Path(args.file).read_text(encoding="utf-8") if args.file != "-" else sys.stdin.read()
    plain = strip_markdown(raw)
    words = re.findall(r"\b[\w'-]+\b", plain)
    total_words = len(words)

    primary = args.keyword.strip()
    secondary = [s.strip() for s in args.secondary.split(",") if s.strip()] if args.secondary else []

    first_10_pct_limit = total_words if total_words < 300 else max(1, int(total_words * 0.10))
    opening_text = " ".join(words[:first_10_pct_limit])
    kw_in_first_10_pct = count_keyword_occurrences(opening_text, primary) > 0

    primary_count = count_keyword_occurrences(plain, primary)
    primary_word_len = max(1, count_words(primary))
    primary_density_pct = round((primary_count * primary_word_len / max(1, total_words)) * 100, 2)

    combined_hits = primary_count * primary_word_len
    secondary_counts: dict[str, int] = {}
    for skw in secondary:
        hits = count_keyword_occurrences(plain, skw)
        secondary_counts[skw] = hits
        combined_hits += hits * max(1, count_words(skw))
    combined_density_pct = round((combined_hits / max(1, total_words)) * 100, 2)

    paragraphs = split_paragraphs(raw)
    long_paragraphs = [
        {"line": ln, "words": count_words(p), "preview": p[:90] + "..."}
        for ln, p in paragraphs
        if count_words(p) > 120
    ]

    seo_title = args.seo_title.strip()
    title_len = len(seo_title)
    title_first_half = seo_title[: max(1, title_len // 2)] if seo_title else ""
    kw_in_title_first_half = (
        count_keyword_occurrences(title_first_half, primary) > 0 if seo_title else None
    )

    meta_desc = args.meta_desc.strip()
    meta_len = len(meta_desc)
    kw_in_meta = count_keyword_occurrences(meta_desc, primary) > 0 if meta_desc else None

    slug_info = check_slug(args.slug.strip(), primary)
    headings = audit_headings(raw, primary, secondary)
    media_links = audit_media_and_links(raw, primary)
    robotic_tells = scan_robotic_tells(raw)

    score_summary = compute_score(
        total_words=total_words,
        target_min=args.target_min,
        seo_title=seo_title,
        title_len=title_len,
        kw_in_title_first_half=kw_in_title_first_half,
        meta_desc=meta_desc,
        meta_len=meta_len,
        kw_in_meta=kw_in_meta,
        slug_info=slug_info,
        kw_in_first_10_pct=kw_in_first_10_pct,
        primary_density_pct=primary_density_pct,
        headings=headings,
        long_paragraphs=long_paragraphs,
        media_links=media_links,
        robotic_count=len(robotic_tells),
    )

    return {
        "score_summary": score_summary,
        "word_count": total_words,
        "target_range": [args.target_min, args.target_max],
        "within_word_target": (
            (args.target_min is None or total_words >= args.target_min)
            and (args.target_max is None or total_words <= args.target_max)
        ),
        "meta_title": {
            "length": title_len,
            "ok_under_60": title_len <= 60 if seo_title else None,
            "keyword_in_first_50_pct": kw_in_title_first_half,
        },
        "meta_description": {
            "length": meta_len,
            "ok_120_to_160": 120 <= meta_len <= 160 if meta_desc else None,
            "keyword_present": kw_in_meta,
        },
        "slug": slug_info,
        "keywords": {
            "primary": primary,
            "primary_count": primary_count,
            "primary_density_pct": primary_density_pct,
            "secondary_counts": secondary_counts,
            "combined_density_pct": combined_density_pct,
            "density_status": (
                "low (<1.0%)"
                if primary_density_pct < 1.0
                else "optimal (1.0-1.5%)"
                if primary_density_pct <= 1.5
                else "acceptable (1.5-2.5%)"
                if primary_density_pct <= 2.5
                else "OVER-STUFFED (>2.5%)"
            ),
            "keyword_in_first_10_pct": kw_in_first_10_pct,
        },
        "headings": headings,
        "paragraphs": {
            "total": len(paragraphs),
            "over_120_words": long_paragraphs,
        },
        "media_and_links": media_links,
        "human_writing_scan": {
            "issues_count": len(robotic_tells),
            "issues": robotic_tells,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Markdown content for On-Page SEO and human-writing rules.")
    parser.add_argument("file", help="Path to Markdown file, or '-' for stdin")
    parser.add_argument("--keyword", required=True, help="Primary focus keyword")
    parser.add_argument("--secondary", default="", help="Comma-separated secondary keywords")
    parser.add_argument("--seo-title", default="", help="SEO title to check (<=60 chars)")
    parser.add_argument("--meta-desc", default="", help="Meta description to check (120-160 chars)")
    parser.add_argument("--slug", default="", help="URL slug to check")
    parser.add_argument("--target-min", type=int, default=None, help="Minimum target word count")
    parser.add_argument("--target-max", type=int, default=None, help="Maximum target word count")
    args = parser.parse_args()

    report = run_audit(args)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
