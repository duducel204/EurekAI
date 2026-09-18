#!/usr/bin/env python3
"""Pre-commit integrity check for EurekAI.
Ensures the local branch is synchronized with origin/main and runs all validations.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def check_git_status() -> int:
    print("--- Verificando integridade para EurekAI ---")
    try:
        # 1. Fetch origin
        subprocess.run(["git", "fetch", "origin"], check=True, cwd=ROOT)

        # 2. Verificar se o main local está atrás do remoto
        result = subprocess.run(["git", "rev-list", "HEAD..origin/main", "--count"], capture_output=True, text=True, check=True, cwd=ROOT)
        behind_count = int(result.stdout.strip())

        if behind_count > 0:
            print(f"ALERTA: Você está {behind_count} commits atrás de origin/main.")
            print("Por favor, execute 'git rebase origin/main' antes de prosseguir.")
            return 1

        # 3. Executar o conjunto completo de testes compartilhados do repositório
        print("Executando checagem comum do repositório (check_all.py)...")
        check_all_script = ROOT / "ferramentas" / "check_all.py"
        proc = subprocess.run([sys.executable, str(check_all_script)], cwd=ROOT)
        if proc.returncode != 0:
            print("ERRO: Algumas validações mecânicas falharam.")
            return proc.returncode

        print("Tudo pronto para o commit conforme AGENTS.md.")
        return 0
    except Exception as exc:
        print(f"ERRO: Falha ao executar validações de pre-commit: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(check_git_status())