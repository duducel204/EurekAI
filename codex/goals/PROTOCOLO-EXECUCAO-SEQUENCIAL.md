# PROTOCOLO — Execução sequencial automática de Goals

**Estado:** CANONIZADO  
**Aplicações:** GOAL-005 → GOAL-006 → GOAL-007 (concluída); GOAL-008 → GOAL-009 → GOAL-010 (preparada)  
**Natureza:** execução multiagente com validação entre etapas

## Dois gates operacionais

### GATE 1 — `READY_FOR_CODEX`
O nome é legado. A partir deste protocolo, significa:

**PRONTO PARA EXECUTOR AUTORIZADO.**

O executor pode ser Codex, Gemini/Cloud Code, ChatGPT com capacidade de execução, humano ou outro agente autorizado.

`READY_FOR_CODEX` não significa preferência pelo Codex e não autoriza qualquer agente aleatório a iniciar trabalho. A autorização vem do estado do Goal + comando/escopo humano aplicável.

### GATE 2 — `CONCLUÍDO`
É o gate de saída.

Um Goal só pode chegar a `CONCLUÍDO` quando:
- entregáveis existirem;
- critérios de aceitação forem atendidos;
- validações mecânicas aplicáveis passarem;
- limitações/lacunas forem registradas;
- houver relatório/handoff auditável;
- não existir stop condition ativa.

Estados como `SEED_DRAFT`, `DRAFT_EVOLUTIVO` e `PREPARADO` são estados de planejamento, não gates de execução.

## Sequência 005 → 006 → 007
Uma única ordem humana pode autorizar a sequência inteira.

Essa autorização é **condicional**:
- GOAL-005 executa primeiro;
- GOAL-006 só pode ser promovido ao GATE 1 depois de GOAL-005 chegar ao GATE 2;
- GOAL-007 só pode ser promovido ao GATE 1 depois de GOAL-006 chegar ao GATE 2.

Falha de validação interrompe a sequência. Não “pular” etapa.

## Modelo operacional padrão
Para reduzir intervenção manual, o executor pode trabalhar em **uma branch de execução da sequência**, com um checkpoint por Goal.

Fluxo:

```text
main atual
  ↓
branch de execução
  ↓
GOAL-005 → validar → checkpoint
  ↓
GOAL-006 → validar → checkpoint
  ↓
GOAL-007 → validar → checkpoint
  ↓
validação final da sequência
  ↓
PR para revisão/canonização
```

O estado escrito na branch é provisório até merge. `main` continua sendo a verdade canônica.

## Promoção automática dentro da sequência
Ao receber ordem explícita para executar a sequência:
1. criar/sincronizar branch a partir do HEAD atual de `origin/main`;
2. registrar `BASE_MAIN_SHA`;
3. dentro da branch, promover GOAL-005 de `PREPARADO` para `READY_FOR_CODEX`;
4. executar e validar GOAL-005;
5. somente se aprovado, marcar GOAL-005 `CONCLUÍDO` e promover GOAL-006 para `READY_FOR_CODEX`;
6. repetir a regra para GOAL-006 → GOAL-007;
7. somente após GOAL-007 validado, marcar a sequência pronta para PR.

Não é necessária nova autorização humana entre 005, 006 e 007 se a ordem inicial autorizou explicitamente a sequência completa.

## Validação por etapa
Antes de marcar qualquer Goal `CONCLUÍDO`:
1. verificar todos os Deliverables;
2. verificar cada item de Acceptance;
3. executar validações específicas do Goal;
4. executar, quando disponível:
   `python ferramentas/check_all.py --base <BASE_MAIN_SHA>`;
5. registrar relatório em `execucoes/`;
6. verificar novamente `origin/main`.

Se `main` avançou:
- ler o delta;
- detectar conflito textual e semântico;
- reconciliar quando seguro;
- refazer validações;
- interromper se a mudança alterar premissas do Goal.

## Stop conditions
Interromper a sequência quando houver:
- critério de aceitação não atendido;
- evidência insuficiente que impeça o objetivo;
- conflito semântico material com novo `main`;
- dependência não concluída;
- alteração de escopo;
- necessidade de decisão humana não coberta pelo Goal;
- falha de validação não resolvida.

O executor deve preservar o trabalho realizado, registrar o bloqueio e **não promover o Goal seguinte**.

## Relatórios de execução
Novas execuções multiagente devem preferir `execucoes/`.

O relatório mínimo registra:
- Goal;
- executor;
- branch;
- `BASE_MAIN_SHA`;
- HEAD de `origin/main` na validação final;
- entregáveis;
- critérios de aceitação;
- validações;
- lacunas/tensões;
- resultado: `CONCLUÍDO` ou `BLOQUEADO`.

`codex/retornos/` permanece como histórico e área do workflow Codex legado.

## Publicação
O executor não deve:
- autoaprovar o próprio PR;
- fazer auto-merge sem decisão explícita;
- force-push para apagar história;
- publicar sobre base antiga sem reconciliação.

## Princípio
**Automatizar a sequência não significa remover gates. Significa fazer o executor atravessar os gates sozinho somente quando a evidência e as validações permitirem.**


## Aplicação 008 → 009 → 010
A mesma mecânica de gates aplica-se à sequência 008→009→010:
- 008 entra primeiro;
- 009 só entra após 008 `CONCLUÍDO` e validado;
- 010 só entra após 009 `CONCLUÍDO` e validado;
- uma autorização humana explícita para a sequência inteira dispensa nova autorização entre etapas;
- qualquer stop condition interrompe a progressão.

Os arquivos específicos de GOAL-008, GOAL-009 e GOAL-010 definem Deliverables, Acceptance, validações e stop conditions próprios. O protocolo geral não substitui esses contratos.
