#!/usr/bin/env python3
"""Read-only repository/version preflight for multi-agent work.

Usage:
  python ferramentas/repo_state.py
  python ferramentas/repo_state.py --base <sha>

The script never commits, merges, rebases, stages or writes repository files.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def git(*args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=Path(__file__).resolve().parents[1],
        text=True,
        capture_output=True,
    )
    if check and proc.returncode != 0:
        msg = proc.stderr.strip() or proc.stdout.strip() or "git command failed"
        raise RuntimeError(msg)
    return proc.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", help="BASE_MAIN_SHA captured when work started")
    parser.add_argument("--no-fetch", action="store_true", help="Do not run git fetch origin")
    args = parser.parse_args()

    try:
        if not args.no_fetch:
            git("fetch", "origin")

        remote_main = git("rev-parse", "origin/main")
        current_head = git("rev-parse", "HEAD")
        branch = git("branch", "--show-current") or "(detached)"
        dirty = bool(git("status", "--porcelain", check=False))

        print(f"branch={branch}")
        print(f"head={current_head}")
        print(f"origin_main={remote_main}")
        print(f"dirty={'yes' if dirty else 'no'}")

        if args.base:
            print(f"base={args.base}")
            if args.base == remote_main:
                print("base_status=CURRENT")
                return 0

            print("base_status=STALE")
            print("changed_since_base:")
            changed = git("diff", "--name-only", f"{args.base}..{remote_main}", check=False)
            print(changed or "(unable to compute or no paths returned)")
            print(
                "ACTION: review new main commits/files, reconcile semantic overlap, "
                "revalidate, then publish."
            )
            return 2

        if current_head == remote_main:
            print("local_vs_main=AT_MAIN")
        else:
            print("local_vs_main=DIFFERENT")
            ahead_behind = git(
                "rev-list", "--left-right", "--count", f"HEAD...origin/main", check=False
            )
            if ahead_behind:
                print(f"head_vs_origin_main_counts={ahead_behind}")

        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
