#!/usr/bin/env python3
"""Validador mínimo para registros EKL-0 em JSONL.

Uso:
    python ferramentas/validate_ekl.py caminho/arquivo.jsonl --mode classificacao
    python ferramentas/validate_ekl.py caminho/arquivo.jsonl --mode mineracao

Este script valida forma e códigos. Não valida verdade semântica.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

CLASSES = {"P", "A", "D", "G", "E", "O", "H", "R", "F", "L"}
EV = {"A", "M", "B", "N"}
MINE = {0, 1, 2, 3}
CONF = {"H", "M", "L", "U"}
KIND = {"DEC", "HIP", "APR", "PRO", "GOV", "ERR", "EVD", "LAC", "REL"}

CLASS_FIELDS = {"i", "cl", "ev", "m", "cf", "rs"}
MINING_FIELDS = {"i", "x"}
EXTRACTION_FIELDS = {"k", "r", "v", "cf"}


def fail(errors: list[str], line_no: int, message: str) -> None:
    errors.append(f"linha {line_no}: {message}")


def validate_classificacao(obj: dict[str, Any], line_no: int, errors: list[str]) -> None:
    extra = set(obj) - CLASS_FIELDS
    missing = {"i", "cl", "ev", "m", "cf", "rs"} - set(obj)
    if extra:
        fail(errors, line_no, f"campos não permitidos: {sorted(extra)}")
    if missing:
        fail(errors, line_no, f"campos obrigatórios ausentes: {sorted(missing)}")
        return
    if not isinstance(obj["i"], str) or not obj["i"].strip():
        fail(errors, line_no, "i deve ser string não vazia")
    if not isinstance(obj["cl"], list) or not obj["cl"]:
        fail(errors, line_no, "cl deve ser lista não vazia")
    else:
        invalid = [c for c in obj["cl"] if c not in CLASSES]
        if invalid:
            fail(errors, line_no, f"classes inválidas: {invalid}")
    if obj["ev"] not in EV:
        fail(errors, line_no, f"ev inválido: {obj['ev']!r}")
    if obj["m"] not in MINE:
        fail(errors, line_no, f"m inválido: {obj['m']!r}")
    if obj["cf"] not in CONF:
        fail(errors, line_no, f"cf inválido: {obj['cf']!r}")
    if not isinstance(obj["rs"], str) or not obj["rs"].strip():
        fail(errors, line_no, "rs deve ser string não vazia")


def validate_mineracao(obj: dict[str, Any], line_no: int, errors: list[str]) -> None:
    extra = set(obj) - MINING_FIELDS
    missing = {"i", "x"} - set(obj)
    if extra:
        fail(errors, line_no, f"campos não permitidos: {sorted(extra)}")
    if missing:
        fail(errors, line_no, f"campos obrigatórios ausentes: {sorted(missing)}")
        return
    if not isinstance(obj["i"], str) or not obj["i"].strip():
        fail(errors, line_no, "i deve ser string não vazia")
    if not isinstance(obj["x"], list):
        fail(errors, line_no, "x deve ser lista")
        return
    for idx, ext in enumerate(obj["x"]):
        if not isinstance(ext, dict):
            fail(errors, line_no, f"x[{idx}] deve ser objeto")
            continue
        extra_ext = set(ext) - EXTRACTION_FIELDS
        missing_ext = EXTRACTION_FIELDS - set(ext)
        if extra_ext:
            fail(errors, line_no, f"x[{idx}] campos não permitidos: {sorted(extra_ext)}")
        if missing_ext:
            fail(errors, line_no, f"x[{idx}] campos ausentes: {sorted(missing_ext)}")
            continue
        if ext["k"] not in KIND:
            fail(errors, line_no, f"x[{idx}].k inválido: {ext['k']!r}")
        for key in ("r", "v"):
            if not isinstance(ext[key], str) or not ext[key].strip():
                fail(errors, line_no, f"x[{idx}].{key} deve ser string não vazia")
        if ext["cf"] not in CONF:
            fail(errors, line_no, f"x[{idx}].cf inválido: {ext['cf']!r}")


def validate_file(path: Path, mode: str) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                fail(errors, line_no, f"JSON inválido: {exc}")
                continue
            if not isinstance(obj, dict):
                fail(errors, line_no, "registro deve ser objeto JSON")
                continue
            if mode == "classificacao":
                validate_classificacao(obj, line_no, errors)
            elif mode == "mineracao":
                validate_mineracao(obj, line_no, errors)
            else:
                raise ValueError(mode)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida JSONL EKL-0")
    parser.add_argument("path", type=Path)
    parser.add_argument("--mode", choices=["classificacao", "mineracao"], required=True)
    args = parser.parse_args()

    errors = validate_file(args.path, args.mode)
    if errors:
        print("EKL-0 inválido:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"EKL-0 válido: {args.path} ({args.mode})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
