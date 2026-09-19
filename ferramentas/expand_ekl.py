#!/usr/bin/env python3
"""Expansor mínimo para registros EKL-0 em JSONL.

Uso:
    python ferramentas/expand_ekl.py entrada.jsonl --mode classificacao
    python ferramentas/expand_ekl.py entrada.jsonl --mode mineracao

A expansão é para leitura humana e auditoria. Não canoniza conteúdo.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

CLASS_MAP = {
    "P": "produto",
    "A": "aprendizado",
    "D": "decisao",
    "G": "governanca",
    "E": "execucao",
    "O": "operacional",
    "H": "hipotese",
    "R": "erro",
    "F": "fonte_evidencia",
    "L": "lacuna",
}

EV_MAP = {"A": "alto", "M": "medio", "B": "baixo", "N": "nulo"}
MINE_MAP = {0: "nao_minerar", 1: "minerar", 2: "revisar", 3: "bloquear"}
CONF_MAP = {"H": "alta", "M": "media", "L": "baixa", "U": "indefinida"}
KIND_MAP = {
    "DEC": "decisao",
    "HIP": "hipotese",
    "APR": "aprendizado",
    "PRO": "produto",
    "GOV": "governanca",
    "ERR": "erro",
    "EVD": "evidencia",
    "LAC": "lacuna",
    "REL": "relacao",
}


def expand_classificacao(obj: dict[str, Any]) -> dict[str, Any]:
    return {
        "item_id": obj.get("i"),
        "classes": [CLASS_MAP.get(c, c) for c in obj.get("cl", [])],
        "valor_epistemologico": EV_MAP.get(obj.get("ev"), obj.get("ev")),
        "acao_mineracao": MINE_MAP.get(obj.get("m"), obj.get("m")),
        "confianca": CONF_MAP.get(obj.get("cf"), obj.get("cf")),
        "razao_curta": obj.get("rs"),
    }


def expand_mineracao(obj: dict[str, Any]) -> dict[str, Any]:
    return {
        "item_id": obj.get("i"),
        "extracoes": [
            {
                "tipo": KIND_MAP.get(ext.get("k"), ext.get("k")),
                "localizador": ext.get("r"),
                "valor": ext.get("v"),
                "confianca": CONF_MAP.get(ext.get("cf"), ext.get("cf")),
            }
            for ext in obj.get("x", [])
        ],
    }


def iter_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def main() -> int:
    parser = argparse.ArgumentParser(description="Expande JSONL EKL-0 para JSON humano")
    parser.add_argument("path", type=Path)
    parser.add_argument("--mode", choices=["classificacao", "mineracao"], required=True)
    parser.add_argument("--pretty", action="store_true", help="imprime JSON indentado em vez de JSONL")
    args = parser.parse_args()

    expanded = []
    for obj in iter_jsonl(args.path):
        if args.mode == "classificacao":
            expanded.append(expand_classificacao(obj))
        else:
            expanded.append(expand_mineracao(obj))

    if args.pretty:
        print(json.dumps(expanded, ensure_ascii=False, indent=2))
    else:
        for obj in expanded:
            print(json.dumps(obj, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
