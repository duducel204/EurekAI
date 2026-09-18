# Adaptador Cloud Code / Gemini Code Assist

Use o ambiente Google para colaborar no **mesmo** EurekAI, não para criar uma variante do projeto nem reorganizar o repositório segundo convenções próprias da ferramenta.

## Reinício de sessão
O Cloud Code/Gemini Code Assist deve assumir que o chat anterior pode ter sido perdido.

Antes de qualquer trabalho material:
1. execute `git fetch origin` e confirme o HEAD de `origin/main`;
2. leia `/ESTADO.md`, `/AGENTS.md` e `/agentes/INDEX.md`;
3. leia `/GEMINI.md` e este arquivo;
4. leia o README da área afetada e o Goal/INV aplicável;
5. registre a base usada e verifique PRs/branches/commits recentes.

## Antes de editar
1. Identifique o Goal, investigação ou pedido humano atual.
2. Identifique a zona correta de escrita.
3. Se a tarefa for apenas configurar Cloud Code/Gemini, prefira `.gemini/`, `.vscode/` ou configuração local — não altere o corpus.

## Onde escrever
- configuração/skills do Gemini → `.gemini/`;
- configuração do editor/Cloud Code → `.vscode/` quando realmente compartilhável;
- documentação específica do agente → `agentes/cloud-code/`;
- utilitário compartilhado entre agentes → `ferramentas/`;
- conteúdo do projeto → somente na pasta semântica correspondente e com evidência/decisão suficiente.

**`contexto/` não é pasta de scripts.** É memória contextual do projeto.

`codex/retornos/` é reservado ao workflow Codex, salvo autorização explícita.

`conhecimento/` organiza conhecimento estruturado; `pedagogia/` é a camada que o transforma em aprendizagem.

## Google Cloud
Diferencie sempre:
`serviço disponível → serviço configurado → serviço usado → serviço adotado/canonizado`.

A passagem entre esses estados exige evidência ou decisão explícita. Não registre “a arquitetura usa BigQuery/Cloud SQL/etc.” apenas porque a ferramenta possui acesso ou skill correspondente.

## Git
Não fazer `git add .` indiscriminadamente, não aprovar o próprio PR e não habilitar auto-merge sem autorização explícita. Mudanças amplas de infraestrutura devem preferir branch/PR auditável.

Antes de commit, push ou PR, execute novo `git fetch origin` e compare `origin/main` com a base registrada. Se houver avanço, revise o delta, verifique sobreposição semântica, reconcilie/rebase conforme necessário e refaça as validações antes de publicar.

## Handoff
Toda conclusão reutilizável por outro agente deve voltar ao GitHub na estrutura canônica e com procedência suficiente para auditoria. Configuração puramente local não precisa virar conhecimento.
