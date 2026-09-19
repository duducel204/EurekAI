# GOAL-009 — Auditoria, validação e correção

**Status:** PREPARADO — NÃO LIBERADO  
**Executor-alvo:** QUALQUER EXECUTOR AUTORIZADO  
**Dependência:** GOAL-008 CONCLUÍDO e validado  
**Sequência:** 008 → 009 → 010  
**Modo:** AUDIT + CORRECT + VALIDATE

## Intent
Auditar o conteúdo realmente produzido no GOAL-008 e corrigir cirurgicamente precisão, procedência, coerência e pedagogia, sem reescrever indiscriminadamente material correto.

## Base obrigatória
Consumir os entregáveis e o relatório **reais** do GOAL-008. Não presumir que o lote passou apenas porque foi produzido.

## Operação
Auditar cada unidade aplicável pelas lentes:
- factual/técnica;
- epistemológica;
- procedência;
- coerência entre evidências, tags e relações;
- pedagógica;
- separação mecanismo/representação/exemplo;
- atemporalidade/versionamento;
- redundância;
- contradição;
- atualização necessária.

Classificar achados materiais como: aprovado, correção cirúrgica, lacuna, tensão ou bloqueio. Corrigir diretamente apenas o que estiver sustentado; preservar histórico e explicar mudança material.

## Deliverables
- conteúdo do GOAL-008 auditado e corrigido quando necessário;
- relatório de auditoria com achados e decisões;
- lista residual de lacunas/tensões não resolvidas;
- critérios reutilizáveis que emergirem da auditoria, sem universalização prematura;
- derivações concretas para o GOAL-010;
- relatório `execucoes/EXEC-GOAL-009.md`.

## Acceptance
- toda correção material é rastreável ao problema que a motivou;
- material correto não é refeito por preferência estilística;
- afirmações factuais permanecem sustentadas pelo corpus;
- hipóteses pedagógicas continuam identificadas;
- analogias não são tratadas como mecanismo;
- exemplos versionados não são universalizados;
- duplicações/contradições materiais são resolvidas ou registradas;
- nenhuma lacuna é escondida para obter aprovação;
- auditoria cobre amostra suficiente das duas trilhas produzidas no GOAL-008, quando existentes.

## Validação
- comparar resultado final com entregáveis e Acceptance do GOAL-008 e GOAL-009;
- executar validações mecânicas aplicáveis, incluindo `python ferramentas/check_all.py --base <BASE_MAIN_SHA>`;
- confirmar links, tags e estrutura quando cobertos pelas ferramentas;
- verificar novamente `origin/main`, reconciliar e revalidar se necessário;
- registrar apenas validações realmente executadas.

## Stop conditions
Parar se:
- erro factual/material não puder ser corrigido com o corpus disponível;
- auditoria revelar que premissa central do GOAL-008 é inválida;
- houver conflito semântico material com `main`;
- validação mecânica permanecer falhando;
- surgir decisão humana fora do escopo.

## Return
Entregar o corpus de conteúdo auditado, as correções, lacunas residuais e os padrões efetivamente observados que o GOAL-010 poderá operacionalizar.

## Gate
Permanece **PREPARADO — NÃO LIBERADO** até GOAL-008 chegar a `CONCLUÍDO` e validado. Dentro de sequência 008→009→010 previamente autorizada, pode ser promovido automaticamente a `READY_FOR_CODEX` somente após esse gate.