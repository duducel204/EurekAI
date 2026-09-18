# Goals

Goals são contratos de trabalho convergidos para execução. Eles transformam planejamento em uma unidade verificável sem exigir que o executor reconstrua a conversa de origem.

## Um Goal deve conter
Intenção/objetivo, dependências, estado, operação, restrições, entregáveis, critérios de aceitação e retorno esperado. Quando necessário, explicite testes, caminhos permitidos e stop conditions.

## Estados
Estados devem ser literais e auditáveis, por exemplo: `SEED_DRAFT`, `DRAFT_EVOLUTIVO`, `READY_FOR_CODEX`, `CONCLUÍDO` ou bloqueio explicitamente documentado. `READY_FOR_CODEX` é autorização operacional para o watcher; não use como simples anotação.

## Pipeline sobreposto
Enquanto N executa, N+1 pode amadurecer e N+2... podem receber sementes. Dependência não observada impede promoção prematura para READY, mas não impede exploração.

## Regra transversal
Este diretório participa de um corpus único e rastreável. Tags oferecem lentes de consulta; não duplicar o mesmo conteúdo apenas para classificá-lo. Fato, experiência, decisão, hipótese, tensão, lacuna e conteúdo proposto por IA devem permanecer distinguíveis. Todo agente deve preservar procedência e apontar para a fonte/evidência quando fizer afirmação material.

## Para agentes
Codex, Gemini CLI, Cloud Code/Gemini Code Assist e outros agentes autorizados devem tratar o GitHub como estado canônico. Leiam `/AGENTS.md` antes de alterar conteúdo. Se faltar evidência, registrem a lacuna ou investigação adequada; não preencham por inferência silenciosa.
