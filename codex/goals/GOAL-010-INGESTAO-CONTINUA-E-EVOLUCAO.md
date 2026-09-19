# GOAL-010 — Ingestão contínua e evolução

**Status:** PREPARADO — NÃO LIBERADO  
**Executor-alvo:** QUALQUER EXECUTOR AUTORIZADO  
**Dependência:** GOAL-009 CONCLUÍDO e validado  
**Sequência:** 008 → 009 → 010  
**Modo:** DESIGN + IMPLEMENT MINIMUM + VALIDATE

## Intent
Fechar a infraestrutura cognitiva inicial do EurekAI com um processo incremental e auditável para incorporar novas fontes/evidências e identificar quais estruturas derivadas podem precisar de revisão, sem reconstrução integral.

## Base obrigatória
Consumir os padrões e problemas **realmente observados** nos GOALs 008 e 009. Não escolher stack, banco, scheduler ou agente permanente sem necessidade demonstrada.

## Operação
1. mapear o fluxo mínimo `nova fonte → extração → evidência → tags/relações → validação → corpus → impactos`;
2. definir identidade/deduplicação e lineage/procedência mínimos;
3. definir como nova evidência sinaliza artefatos potencialmente afetados sem sobrescrevê-los silenciosamente;
4. definir tratamento de contradição, tensão, lacuna e evidência insuficiente;
5. reutilizar ferramentas existentes antes de criar novas;
6. automatizar apenas verificações determinísticas justificadas;
7. manter revisão humano/IA para inferência material;
8. demonstrar o processo com um caso controlado ou fixture seguro, sem alterar história factual para fabricar sucesso;
9. produzir relatório em `execucoes/`.

## Deliverables
- contrato canônico de ingestão/evolução incremental;
- fluxo mínimo executável ou operacionalmente reproduzível;
- regra de deduplicação/idempotência quando aplicável;
- regra de procedência/lineage;
- mecanismo leve para registrar impacto potencial sobre relações, trilhas e conteúdo;
- tratamento explícito de conflitos/tensões;
- demonstração controlada do ciclo;
- backlog separado para automações/infraestrutura ainda não justificadas;
- relatório `execucoes/EXEC-GOAL-010.md`.

## Acceptance
- nova entrada não exige reconstrução integral do repositório;
- histórico não é sobrescrito silenciosamente;
- duplicação é detectada ou explicitamente tratada;
- procedência permanece recuperável;
- impacto potencial de nova evidência pode ser identificado;
- inferência material não é promovida automaticamente a fato;
- processo é agente-neutro e compreensível sem a conversa original;
- não cria infraestrutura pesada sem necessidade observada;
- demonstração controlada não contamina o corpus factual;
- estado final distingue claramente sistema implementado, processo documentado e backlog futuro.

## Validação
- testar o fluxo mínimo com fixture/caso controlado;
- verificar idempotência/deduplicação quando aplicável;
- verificar que procedência e impacto continuam rastreáveis;
- executar validações mecânicas aplicáveis, incluindo `python ferramentas/check_all.py --base <BASE_MAIN_SHA>`;
- verificar `origin/main` antes da publicação final e reconciliar avanço;
- registrar no relatório comandos/resultados efetivamente executados.

## Stop conditions
Parar se:
- a implementação exigir decisão de stack/infraestrutura não sustentada pelos Goals anteriores;
- o teste ameaçar contaminar ou sobrescrever corpus canônico;
- deduplicação/procedência não puderem ser preservadas;
- houver conflito semântico material com `main`;
- validação permanecer falhando;
- for necessária decisão humana fora do escopo.

## Return
Entregar o processo incremental validado, sua demonstração, limitações e backlog. O fechamento do GOAL-010 representa o fim da construção da **infraestrutura cognitiva inicial**, não o fim da evolução do EurekAI.

## Gate
Permanece **PREPARADO — NÃO LIBERADO** até GOAL-009 chegar a `CONCLUÍDO` e validado. Dentro de sequência 008→009→010 previamente autorizada, pode ser promovido automaticamente a `READY_FOR_CODEX` somente após esse gate.