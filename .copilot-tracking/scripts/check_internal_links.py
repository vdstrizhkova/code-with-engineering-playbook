#!/usr/bin/env python3
"""Anchor-aware internal link checker for the docs/ tree.

Validates every relative markdown link and its optional #fragment against the
actual heading slugs of the target file, replicating python-markdown / MkDocs
Material slugification. External (http/https/mailto) links are out of scope
(handled separately by lychee in CI); this script focuses on the internal
links and deep anchors that the deduplication work relies on.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

DOCS = Path(__file__).resolve().parents[2] / "docs"

LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
ATX_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HTML_ANCHOR_RE = re.compile(r'<a[^>]+(?:name|id)=["\']([^"\']+)["\']', re.I)
ATTR_ID_RE = re.compile(r"\{:?\s*#([A-Za-z0-9_-]+)[^}]*\}\s*$")
CODE_FENCE_RE = re.compile(r"^\s*(```|~~~)")


def slugify(text: str) -> str:
    """Match python-markdown's default (toc) slugify: strip tags/punct, lower, spaces->hyphens."""
    text = re.sub(r"<[^>]+>", "", text)  # strip inline HTML
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)  # drop punctuation
    text = text.strip().lower()
    text = re.sub(r"[\s]+", "-", text)
    return text


def headings_to_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if CODE_FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in HTML_ANCHOR_RE.finditer(line):
            anchors.add(m.group(1))
        hm = ATX_RE.match(line)
        if not hm:
            continue
        heading = hm.group(2)
        attr = ATTR_ID_RE.search(heading)
        if attr:
            anchors.add(attr.group(1))
            heading = ATTR_ID_RE.sub("", heading).strip()
        slug = slugify(heading)
        if not slug:
            continue
        n = counts.get(slug, 0)
        anchors.add(slug if n == 0 else f"{slug}_{n}")
        counts[slug] = n + 1
    return anchors


def main() -> int:
    md_files = sorted(DOCS.rglob("*.md"))
    anchors_cache: dict[Path, set[str]] = {}
    errors: list[str] = []

    for md in md_files:
        text = md.read_text(encoding="utf-8")
        # blank out fenced code so we don't parse links inside code samples
        lines, in_fence, kept = text.splitlines(), False, []
        for line in lines:
            if CODE_FENCE_RE.match(line):
                in_fence = not in_fence
                kept.append("")
                continue
            kept.append("" if in_fence else line)
        body = "\n".join(kept)

        for m in LINK_RE.finditer(body):
            target = m.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = target.split(" ", 1)[0]  # drop optional "title"
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            frag = ""
            if "#" in target:
                path_part, frag = target.split("#", 1)
            else:
                path_part = target
            path_part = unquote(path_part)
            frag = unquote(frag)

            if path_part == "":
                dest = md  # same-file anchor
            else:
                dest = (md.parent / path_part).resolve()
                if dest.is_dir():
                    # directory link resolves to its index (README.md)
                    readme = dest / "README.md"
                    dest = readme if readme.exists() else dest
                if not dest.exists():
                    errors.append(f"{md.relative_to(DOCS)}: missing target -> {target}")
                    continue

            if frag:
                if dest.suffix.lower() != ".md":
                    continue
                if dest not in anchors_cache:
                    anchors_cache[dest] = headings_to_anchors(dest)
                if frag not in anchors_cache[dest]:
                    errors.append(
                        f"{md.relative_to(DOCS)}: missing anchor '#{frag}' in {dest.relative_to(DOCS)}"
                    )

    if errors:
        print(f"FAIL: {len(errors)} internal link/anchor problem(s):")
        for e in errors:
            print("  -", e)
        return 1
    print(f"OK: checked {len(md_files)} markdown files, all internal links and anchors resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
