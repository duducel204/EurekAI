#!/usr/bin/env python3
"""Validate EurekAI Tags: lines against mapa-do-conhecimento/INDEX-TAGS.md.

Read-only, standard-library only, cross-platform.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "mapa-do-conhecimento" / "INDEX-TAGS.md"
TAG_RE = re.compile(r"#[a-z0-9-]+")
SKIP_PARTS = {".git", ".gemini"}


def main() -> int:
    if not INDEX.exists():
        print(f"ERROR: missing {INDEX.relative_to(ROOT)}", file=sys.stderr)
        return 1

    valid = set(TAG_RE.findall(INDEX.read_text(encoding="utf-8")))
    errors: list[tuple[str, str]] = []

    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line in text.splitlines():
            if not line.startswith("Tags:"):
                continue
            for tag in TAG_RE.findall(line):
                if tag not in valid:
                    errors.append((str(path.relative_to(ROOT)), tag))

    if errors:
        for path, tag in errors:
            print(f"UNKNOWN_TAG {tag} in {path}")
        return 1

    print(f"OK: {len(valid)} indexed tags; all explicit Tags: lines are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
