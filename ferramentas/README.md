# Ferramentas

**Estado atual:** utilitários compartilhados ativos para validação, estado e checks.

## Função

`ferramentas/` contém scripts e utilitários revisáveis usados pelo EurekAI.

Ferramentas não são conhecimento canônico. Elas executam verificações, inventários ou apoio operacional.

## Scripts atuais

- `repo_state.py`: valida base/estado de repositório e concorrência.
- `validate_tags.py`: valida tags canônicas.
- `validate_links.py`: valida links Markdown relativos.
- `validate_goal_sequence.py`: valida estrutura da sequência 005→007.
- `validate_knowledge_units.py`: valida IDs e campos obrigatórios de unidades de conhecimento.
- `validate_ekl.py`: valida registros EKL-0 em JSONL para classificação ou mineração.
- `expand_ekl.py`: expande registros EKL-0 compactos para JSON humano.
- `check_all.py`: agregador de validações.
- `pre_commit_check.py`: apoio de pré-commit/checks locais.

## EKL-0

As ferramentas EKL-0 servem à preparação da leitura do histórico/Takeout.

Uso esperado:

```bash
python ferramentas/validate_ekl.py saida-classificacao.jsonl --mode classificacao
python ferramentas/validate_ekl.py saida-mineracao.jsonl --mode mineracao
python ferramentas/expand_ekl.py saida-classificacao.jsonl --mode classificacao --pretty
python ferramentas/expand_ekl.py saida-mineracao.jsonl --mode mineracao --pretty
```

Esses scripts validam e expandem forma. Não provam verdade semântica e não canonizam conteúdo.

## Estado pós-GOAL-010

As ferramentas devem continuar servindo pipelines, auditorias e PRs. Novas ferramentas devem ser determinísticas sempre que possível.

## Regra semântica

Validação mecânica não substitui validação semântica. Um check pode dizer que links, tags, campos e códigos existem; não prova que a interpretação está correta.
