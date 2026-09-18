#!/usr/bin/env python3
"""Validate local relative Markdown links in the EurekAI corpus.

Skips external URLs, anchors, mailto links and .gemini vendor/tooling content.
Read-only, standard-library only, cross-platform.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SKIP_PARTS = {".git", ".gemini"}


def clean_target(raw: str) -> str | None:
    target = raw.strip().split()[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = unquote(target.split("#", 1)[0])
    return target or None


def main() -> int:
    broken: list[tuple[str, str]] = []
    checked = 0

    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for raw in LINK_RE.findall(text):
            target = clean_target(raw)
            if target is None:
                continue
            checked += 1
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                broken.append((str(path.relative_to(ROOT)), raw))
                continue
            if not resolved.exists():
                broken.append((str(path.relative_to(ROOT)), raw))

    if broken:
        for source, target in broken:
            print(f"BROKEN_LINK {source} -> {target}")
        return 1

    print(f"OK: {checked} local Markdown links checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
