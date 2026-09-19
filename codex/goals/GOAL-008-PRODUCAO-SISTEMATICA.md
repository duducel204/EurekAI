# GOAL-008 — Produção sistemática de conteúdo

**Status:** PREPARADO — NÃO LIBERADO  
**Executor-alvo:** QUALQUER EXECUTOR AUTORIZADO  
**Dependência:** GOAL-007 CONCLUÍDO, revalidado e validado  
**Sequência:** 008 → 009 → 010  
**Modo:** EXECUTE + VALIDATE

## Intent
Transformar o framework pedagógico validado em um primeiro lote real de unidades de conteúdo, com alta reutilização do corpus e sem transformar hipóteses pedagógicas em fatos.

## Base obrigatória
Consumir o estado canônico real de:
- `mapa-do-conhecimento/`;
- `pedagogia/PROGRESSAO-001.md`;
- `pedagogia/FRAMEWORK-PEDAGOGICO.md`;
- evidências e seus limites;
- relatório final do GOAL-007.

Não presumir conteúdo que o corpus não sustenta.

## Operação
1. sincronizar com `origin/main` e registrar `BASE_MAIN_SHA`;
2. selecionar material suficiente para testar as duas trilhas atuais, sem obrigação de cobrir todo o corpus;
3. produzir unidades usando a estrutura mínima do framework;
4. separar explicitamente mecanismo atemporal, representação/analogia, exemplo versionado, experimento e hipótese pedagógica;
5. preservar IDs/procedência e limites das evidências;
6. deduplicar conteúdo e reutilizar derivações existentes;
7. registrar lacunas que impeçam aprofundamento, sem preenchê-las por inferência;
8. produzir relatório em `execucoes/`.

## Deliverables
- um primeiro lote canônico de unidades em `conteudo/` (criar a área se necessário, com README de contrato);
- cobertura de pelo menos um recorte da Trilha A e um da Trilha B, quando o corpus permitir;
- índice simples das unidades produzidas;
- registro das lacunas/hipóteses encontradas;
- derivações concretas para o GOAL-009;
- relatório `execucoes/EXEC-GOAL-008.md`.

## Acceptance
- unidades compreensíveis a partir de zero pressuposto quando esse for o ponto declarado;
- evidência, mecanismo e hipótese pedagógica distinguíveis;
- nenhuma inferência de domínio pessoal de André;
- analogia não substitui mecanismo técnico;
- exemplos dependentes de ferramenta/versão identificados;
- procedência auditável;
- conteúdo não duplica desnecessariamente o corpus-fonte;
- framework do GOAL-007 demonstrado em uso real em mais de uma trilha ou limitação explicitada;
- não decide UI, plataforma comercial, volume final ou produto.

## Validação
- conferir cada unidade contra as evidências citadas e seus limites;
- verificar aderência ao `FRAMEWORK-PEDAGOGICO.md`;
- executar validações mecânicas aplicáveis, incluindo `python ferramentas/check_all.py --base <BASE_MAIN_SHA>` quando disponível;
- verificar novamente `origin/main` e reconciliar avanço antes de publicar;
- registrar no relatório o que foi efetivamente executado, sem tratar simulação como teste.

## Stop conditions
Parar se:
- o corpus não sustentar unidades reais suficientes para testar o framework;
- surgir conflito material com evidência ou com o framework;
- validação mecânica falhar sem correção segura;
- `main` avançar alterando premissas;
- for necessária decisão humana de produto/escopo não coberta por este Goal.

## Return
Entregar lote, índice, lacunas, validações e handoff suficiente para o GOAL-009 auditar o resultado real.

## Gate
Este Goal está **PREPARADO — NÃO LIBERADO**. Em uma ordem humana que autorize explicitamente a sequência 008→009→010, o executor pode promovê-lo ao gate `READY_FOR_CODEX` e iniciar a sequência segundo o protocolo canônico.