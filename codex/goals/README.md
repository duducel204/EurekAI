# Goals

Goals são contratos de trabalho convergidos para execução. Eles transformam planejamento em uma unidade verificável sem exigir que o executor reconstrua a conversa de origem.

## Um Goal deve conter
Intenção/objetivo, dependências, estado, operação, restrições, entregáveis, critérios de aceitação, validação, stop conditions e retorno esperado.

## Dois gates operacionais

### `READY_FOR_CODEX` — gate de entrada
O nome é **legado**.

A partir da canonização da execução multiagente, `READY_FOR_CODEX` significa **PRONTO PARA EXECUTOR AUTORIZADO**. O executor pode ser Codex, Gemini/Cloud Code, humano ou outro agente autorizado.

Manter o literal evita quebrar automações existentes enquanto a semântica passa a ser genérica.

### `CONCLUÍDO` — gate de saída
Só usar após entregáveis, Acceptance e validações terem sido cumpridos e existir retorno/handoff auditável.

## Estados de preparação
`SEED_DRAFT`, `DRAFT_EVOLUTIVO` e `PREPARADO` não autorizam execução por si só.

Bloqueios devem ser explícitos.

## Execução sequencial
O protocolo canonizado está em [PROTOCOLO-EXECUCAO-SEQUENCIAL.md](PROTOCOLO-EXECUCAO-SEQUENCIAL.md).

Uma sequência explicitamente autorizada pode promover automaticamente o próximo Goal para `READY_FOR_CODEX` **somente depois** que a dependência anterior atingir `CONCLUÍDO` com validação.

## Pipeline sobreposto
Enquanto N executa, N+1 pode amadurecer e N+2... podem receber sementes. Dependência não observada impede promoção prematura para READY, mas não impede exploração.

## Regra transversal
Este diretório participa de um corpus único e rastreável. Tags oferecem lentes de consulta; não duplicar o mesmo conteúdo apenas para classificá-lo. Fato, experiência, decisão, hipótese, tensão, lacuna e conteúdo proposto por IA devem permanecer distinguíveis. Todo agente deve preservar procedência e apontar para a fonte/evidência quando fizer afirmação material.

## Para agentes
Qualquer executor autorizado deve tratar o GitHub como estado canônico, ler `/ESTADO.md`, `/AGENTS.md` e `/agentes/INDEX.md`, registrar a base usada e validar a versão atual antes de publicar.

Novos relatórios multiagente devem preferir `/execucoes/`.
