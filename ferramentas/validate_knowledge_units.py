#!/usr/bin/env python3
"""Validate the minimum structure of canonical knowledge units."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIT_FILE = ROOT / "conhecimento" / "UNIDADES-001.md"
REQUIRED = {
    "Objetivo",
    "Origem",
    "Evidências",
    "Relações",
    "Hipóteses",
    "Mecanismo atemporal",
    "Exemplo versionado",
    "Representação inicial",
    "Representação alternativa",
    "Terminologia",
    "Experimento",
    "Tags",
    "Confiança",
    "Lacunas",
    "Executor",
    "Geração",
}


def main() -> int:
    text = UNIT_FILE.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^## (UC-\d{3}) — .+$", text, re.MULTILINE))
    if not matches:
        print("ERROR: no UC-NNN units found", file=sys.stderr)
        return 1

    errors: list[str] = []
    ids = [match.group(1) for match in matches]
    if len(ids) != len(set(ids)):
        errors.append("duplicate unit IDs")

    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.end() : end]
        fields = {
            field.group(1).strip()
            for field in re.finditer(r"^- \*\*([^:*]+):\*\*", block, re.MULTILINE)
        }
        missing = sorted(REQUIRED - fields)
        if missing:
            errors.append(f"{match.group(1)} missing: {', '.join(missing)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {len(ids)} knowledge units; IDs unique; required fields present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
