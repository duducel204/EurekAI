#!/usr/bin/env python3
"""Structural preflight for the prepared GOAL-005 -> 006 -> 007 sequence.

Read-only. It does not decide semantic correctness or execute Goals.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOALS = {
    "005": ROOT / "codex/goals/GOAL-005-RELACOES-E-DEPENDENCIAS.md",
    "006": ROOT / "codex/goals/GOAL-006-PROGRESSAO-ZERO-A-FRONTEIRA.md",
    "007": ROOT / "codex/goals/GOAL-007-ENGENHARIA-PEDAGOGICA-ATEMPORAL.md",
}
REQUIRED = [
    "## Intent",
    "## Operação",
    "## Deliverables",
    "## Acceptance",
    "## Validação",
    "## Stop conditions",
    "## Return",
]
DEPENDENCIES = {"006": "GOAL-005", "007": "GOAL-006"}


def field(text: str, name: str) -> str:
    m = re.search(rf"^\*\*{re.escape(name)}:\*\*\s*(.+?)\s*$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def main() -> int:
    errors: list[str] = []

    for gid, path in GOALS.items():
        if not path.exists():
            errors.append(f"GOAL-{gid}: missing file {path.relative_to(ROOT)}")
            continue

        text = path.read_text(encoding="utf-8")
        status = field(text, "Status") or "(missing)"
        dep = field(text, "Dependência") or "(missing)"
        print(f"GOAL-{gid}: status={status} | dependencia={dep}")

        if "SEED_DRAFT" in status or "DRAFT_EVOLUTIVO" in status:
            errors.append(f"GOAL-{gid}: still draft, not structurally prepared")

        for section in REQUIRED:
            if section not in text:
                errors.append(f"GOAL-{gid}: missing section {section}")

        expected = DEPENDENCIES.get(gid)
        if expected and expected not in dep:
            errors.append(f"GOAL-{gid}: dependency should reference {expected}")

    if errors:
        print("\nSEQUENCE PREFLIGHT: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1

    print("\nSEQUENCE PREFLIGHT: OK")
    print("Semantic acceptance must still be validated during execution.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
