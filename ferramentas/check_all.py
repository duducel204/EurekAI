#!/usr/bin/env python3
"""Run shared read-only EurekAI checks.

Usage:
  python ferramentas/check_all.py
  python ferramentas/check_all.py --base <BASE_MAIN_SHA>
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "ferramentas"


def run(name: str, *args: str) -> int:
    print(f"\n== {name} ==")
    proc = subprocess.run([sys.executable, str(TOOLS / name), *args], cwd=ROOT)
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", help="BASE_MAIN_SHA captured when work started")
    parser.add_argument("--no-fetch", action="store_true")
    args = parser.parse_args()

    state_args: list[str] = []
    if args.base:
        state_args += ["--base", args.base]
    if args.no_fetch:
        state_args += ["--no-fetch"]

    results = [
        run("repo_state.py", *state_args),
        run("validate_tags.py"),
        run("validate_links.py"),
    ]

    failed = [code for code in results if code != 0]
    if failed:
        print("\nCHECKS: ATTENTION REQUIRED")
        return max(failed)

    print("\nCHECKS: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
