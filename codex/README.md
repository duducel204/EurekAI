# Codex — workflow de construção

Esta área contém o mecanismo de trabalho orientado a Goals usado pelo Codex para desenvolver o EurekAI. Ela não é sinônimo do conteúdo pedagógico do projeto.

## Estrutura
- `goals/`: contratos executáveis, roadmap e diretrizes.
- `retornos/`: relatórios auditáveis das execuções.

## Ciclo
`planejar → READY_FOR_CODEX → executar → validar → PR → auditoria/merge → atualizar estado → liberar próximo`.

Infraestrutura local de watcher, locks, logs e credenciais não deve ser versionada aqui. Outros agentes podem ler os Goals como contexto, mas não devem assumir que um Goal planejado foi executado sem evidência no Git/PR/retorno.

## Regra transversal
Este diretório participa de um corpus único e rastreável. Tags oferecem lentes de consulta; não duplicar o mesmo conteúdo apenas para classificá-lo. Fato, experiência, decisão, hipótese, tensão, lacuna e conteúdo proposto por IA devem permanecer distinguíveis. Todo agente deve preservar procedência e apontar para a fonte/evidência quando fizer afirmação material.

## Para agentes
Codex, Gemini CLI, Cloud Code/Gemini Code Assist e outros agentes autorizados devem tratar o GitHub como estado canônico. Leiam `/AGENTS.md` antes de alterar conteúdo. Se faltar evidência, registrem a lacuna ou investigação adequada; não preencham por inferência silenciosa.
