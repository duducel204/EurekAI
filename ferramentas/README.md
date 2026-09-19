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
- `check_all.py`: agregador de validações.
- `pre_commit_check.py`: apoio de pré-commit/checks locais.

## Estado pós-GOAL-010

As ferramentas devem continuar servindo pipelines, auditorias e PRs. Novas ferramentas devem ser determinísticas sempre que possível.

## Regra semântica

Validação mecânica não substitui validação semântica. Um check pode dizer que links, tags e campos existem; não prova que a interpretação está correta.