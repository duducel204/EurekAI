# Adaptador Cloud Code / Gemini Code Assist

Use o ambiente Google para colaborar no **mesmo** EurekAI, não para criar uma variante do projeto nem reorganizar o repositório segundo convenções próprias da ferramenta.

## Antes de editar
1. Leia `/AGENTS.md`.
2. Identifique o Goal, investigação ou pedido humano atual.
3. Identifique a zona correta de escrita.
4. Se a tarefa for apenas configurar Cloud Code/Gemini, prefira `.gemini/`, `.vscode/` ou configuração local — não altere o corpus.

## Onde escrever
- configuração/skills do Gemini → `.gemini/`;
- configuração do editor/Cloud Code → `.vscode/` quando realmente compartilhável;
- documentação específica do agente → `agentes/cloud-code/`;
- utilitário compartilhado entre agentes → `ferramentas/`;
- conteúdo do projeto → somente na pasta semântica correspondente e com evidência/decisão suficiente.

**`contexto/` não é pasta de scripts.** É memória contextual do projeto.

## Google Cloud
Diferencie sempre:
`serviço disponível → serviço configurado → serviço usado → serviço adotado/canonizado`.

A passagem entre esses estados exige evidência ou decisão explícita. Não registre “a arquitetura usa BigQuery/Cloud SQL/etc.” apenas porque a ferramenta possui acesso ou skill correspondente.

## Git
Não fazer `git add .` indiscriminadamente, não aprovar o próprio PR e não habilitar auto-merge sem autorização explícita. Mudanças amplas de infraestrutura devem preferir branch/PR auditável.

## Handoff
Toda conclusão reutilizável por outro agente deve voltar ao GitHub na estrutura canônica e com procedência suficiente para auditoria. Configuração puramente local não precisa virar conhecimento.
