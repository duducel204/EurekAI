# GOAL-005 — Relações, dependências e transferências

**Status:** PREPARADO — NÃO LIBERADO  
**Executor alvo:** QUALQUER EXECUTOR AUTORIZADO  
**Dependência:** GOAL-004 concluído e validado  
**Sequência:** 005 → 006 → 007  
**Modo:** EXECUTE + VALIDATE

## Intent
Descobrir e registrar, com força de evidência explícita, como conhecimentos, experiências, projetos, artefatos, ideias e planos se conectam — sem transformar coocorrência em causalidade, sequência em pré-requisito ou recorrência em domínio.

O corpus e as tags continuam sendo a matriz principal. Relações explícitas só devem ser criadas quando acrescentarem significado que tags/interseções não expressem adequadamente.

## Estado herdado do GOAL-004
O GOAL-004 validou um recorte inferencial pequeno e auditável:

- E-014–E-019 são as unidades atualmente aptas para inferência;
- E-001–E-013 continuam como pistas históricas sem localizador individual suficiente;
- C-001 e C-002 são **clusters candidatos**, não relações definitivas;
- T-001 é uma tensão preservada;
- não há evidência suficiente, neste recorte, para afirmar causalidade, pré-requisito conceitual, transferência pessoal, transição cognitiva ou autoria humano–IA;
- INV-001 continua parcial e pode ampliar o corpus posteriormente.

O GOAL-005 deve partir exatamente desses limites e não “completar” o que ainda não está demonstrado.

## Hipóteses a testar
Testar somente quando houver evidência suficiente:

- **relação contextual:** itens aparecem no mesmo contexto/projeto;
- **relação conceitual:** A ajuda a compreender/usar B;
- **dependência prática:** B exige A naquele contexto;
- **sequência histórica:** A ocorreu antes/depois de B;
- **transferência:** um mecanismo reaparece em outro projeto/contexto;
- **trajetória de resolução:** erro → diagnóstico → solução → reaplicação;
- **transição cognitiva:** evento altera modelo mental;
- **participação humano–IA:** quem propôs, executou, modificou, rejeitou ou corrigiu.

## Estados de relação
Não usar pontuação numérica inventada.

- **OBSERVADA:** a própria fonte/evidência mostra a relação;
- **CANDIDATA SUSTENTADA:** há indícios suficientes para registrar a conexão como candidata, com limites explícitos;
- **INSUFICIENTE:** a hipótese existe, mas o corpus atual não sustenta registro positivo;
- **CONTESTADA/TENSIONADA:** há evidências ou documentos incompatíveis que precisam permanecer visíveis.

Nenhum desses estados equivale a domínio, competência ou causalidade pessoal.

## Operação
1. Confirmar HEAD de `origin/main`, registrar `BASE_MAIN_SHA` e aplicar o protocolo em `PROTOCOLO-EXECUCAO-SEQUENCIAL.md`.
2. Ler GOAL-001–004, retornos, `INDEX-TAGS.md`, `MODELO-001-CONHECIMENTO-OBSERVADO.md`, inventários e INV-001.
3. Trabalhar primeiro sobre E-014–E-019. Não promover E-001–E-013 sem novos localizadores verificáveis.
4. Consultar interseções de tags, contexto, sequência e artefatos antes de criar qualquer relação explícita.
5. Revisar C-001, C-002 e T-001:
   - preservar como candidatos/tensão quando a evidência continuar insuficiente;
   - promover somente se nova evidência verificável justificar;
   - registrar por que não houve promoção quando aplicável.
6. Extrair novas relações apenas quando o vínculo acrescentar informação real além das tags.
7. Para cada relação explícita, registrar: origem, destino, tipo, direção quando houver, estado, evidências, contraevidência/tensão e limite de inferência.
8. Preservar relações pedagógicas apenas como candidatas para GOAL-006/007; não criar progressão ainda.
9. Atualizar investigação somente quando surgir lacuna material que altere o mapa.
10. Não decidir tecnologia de grafo, banco, ontologia, visualização ou taxonomia definitiva.

## Deliverables
- camada leve de relações sobre o corpus, preferencialmente em `mapa-do-conhecimento/`, sem duplicar evidências;
- destino explícito de C-001, C-002 e T-001;
- novas tags/aliases somente quando justificadas;
- lacunas/tensões novas, se materiais;
- derivações candidatas para GOAL-006–008;
- relatório/handoff em `execucoes/`.

## Acceptance
O resultado deve permitir responder:
- quais conexões são observadas;
- quais são candidatas sustentadas;
- quais hipóteses permanecem insuficientes;
- quais relações estão tensionadas;
- que evidências sustentam cada conexão;
- quais relações não podem ser promovidas e por quê.

Deve preservar:
`coocorrência ≠ relação`;  
`sequência ≠ causalidade`;  
`dependência técnica ≠ pré-requisito pedagógico`;  
`reaparecimento ≠ transferência pessoal`;  
`artefato ≠ autoria`.

## Validação
Antes de `CONCLUÍDO`:
1. conferir cada Deliverable e item de Acceptance;
2. validar localizadores/evidências de toda relação promovida;
3. executar `python ferramentas/check_all.py --base <BASE_MAIN_SHA>` quando disponível;
4. verificar novamente `origin/main` e reconciliar avanço relevante;
5. registrar resultado auditável em `execucoes/`.

## Stop conditions
Bloquear e não promover GOAL-006 quando:
- uma relação necessária depender de inferência não sustentada;
- Acceptance não puder ser demonstrado;
- surgir conflito semântico material com novo `main`;
- houver decisão humana necessária fora do escopo;
- validação falhar sem correção segura.

## Return
Registrar em `execucoes/`: executor, branch, base, entregáveis, relações promovidas/não promovidas, validações, lacunas, HEAD remoto final e estado.

## Gate
Este Goal está preparado, não liberado.

Quando uma ordem humana autorizar a sequência 005→006→007, o executor selecionado pode, em sua branch de execução, promover GOAL-005 para `READY_FOR_CODEX`.

Nesse estado, `READY_FOR_CODEX` significa **pronto para executor autorizado**, não exclusividade do Codex.

Somente após validação completa pode passar a `CONCLUÍDO` e liberar automaticamente GOAL-006 dentro da sequência autorizada.
