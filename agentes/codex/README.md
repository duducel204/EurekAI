# Adaptador Codex

Codex é atualmente o executor sistemático dos Goals do EurekAI.

## Entrada
Leia `/AGENTS.md`, `codex/goals/ROADMAP-GOALS.md`, o Goal selecionado, seus predecessores/retornos quando exigidos e os READMEs das áreas afetadas.

## Execução
Respeite literalmente o estado do Goal, dependências, stop conditions e critérios de aceitação. Verifique Git/PRs antes de repetir trabalho. Trabalhe por branch/PR quando o workflow exigir.

## Saída
Produza retorno auditável em `codex/retornos/` quando especificado e deixe o Git consistente com a execução. Não promova o Goal seguinte por conta própria quando isso exigir revisão externa.

Runtime local, watcher, locks e credenciais ficam fora do corpus/versionamento salvo decisão explícita.
