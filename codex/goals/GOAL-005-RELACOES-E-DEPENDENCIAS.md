# GOAL-005 — Relações, dependências e transferências

**Status:** PREPARADO — NÃO LIBERADO  
**Executor:** NÃO DEFINIDO  
**Dependência:** GOAL-004 concluído e validado  
**Modo futuro:** EXECUTE + VALIDATE

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
Não usar pontuação numérica inventada. Cada relação candidata deve ser classificada em um destes estados:

- **OBSERVADA:** a própria fonte/evidência mostra a relação;
- **CANDIDATA SUSTENTADA:** há indícios suficientes para registrar a conexão como candidata, com limites explícitos;
- **INSUFICIENTE:** a hipótese existe, mas o corpus atual não sustenta registro positivo;
- **CONTESTADA/TENSIONADA:** há evidências ou documentos incompatíveis que precisam permanecer visíveis.

Nenhum desses estados equivale a domínio, competência ou causalidade pessoal.

## Operação
1. Sincronizar `main` e ler `AGENTS.md`, o adaptador do executor, GOAL-001–004, retornos, `INDEX-TAGS.md`, `MODELO-001-CONHECIMENTO-OBSERVADO.md`, inventários e INV-001.
2. Trabalhar primeiro sobre E-014–E-019. Não promover E-001–E-013 sem novos localizadores verificáveis.
3. Consultar interseções de tags, contexto, sequência e artefatos antes de criar qualquer relação explícita.
4. Revisar C-001, C-002 e T-001:
   - preservar como candidatos/tensão quando a evidência continuar insuficiente;
   - promover somente se nova evidência verificável justificar;
   - registrar por que não houve promoção quando aplicável.
5. Extrair novas relações apenas quando o vínculo acrescentar informação real além das tags.
6. Para cada relação explícita, registrar:
   - origem;
   - destino;
   - tipo;
   - direção, quando houver;
   - estado da relação;
   - evidências que sustentam;
   - contraevidência/tensão;
   - limite de inferência.
7. Preservar relações pedagógicas apenas como candidatas para GOAL-006/007 quando sustentadas; não criar progressão ainda.
8. Atualizar investigação somente quando surgir lacuna material que altere o mapa.
9. Não decidir tecnologia de grafo, banco, ontologia, visualização ou taxonomia definitiva.

## Deliverables
- uma camada leve de relações sobre o corpus existente, preferencialmente em `mapa-do-conhecimento/`, sem duplicar evidências;
- registro explícito do destino de C-001, C-002 e T-001;
- novas tags/aliases somente se realmente justificadas;
- lacunas/tensões novas, se materiais;
- derivações candidatas para GOAL-006–008, sem executá-los;
- handoff/relatório de execução no local definido quando o executor for escolhido.

## Acceptance
O resultado deve permitir responder:

- quais conexões são observadas;
- quais são apenas candidatas;
- quais hipóteses permanecem insuficientes;
- quais relações estão tensionadas;
- que evidências sustentam cada conexão;
- quais relações não podem ser promovidas e por quê.

Deve ser possível distinguir claramente:
`coocorrência ≠ relação`,
`sequência ≠ causalidade`,
`dependência técnica ≠ pré-requisito pedagógico`,
`reaparecimento ≠ transferência pessoal`,
`artefato ≠ autoria`.

## Não decidir ainda
- grafo/banco/ontologia definitivos;
- taxonomia fixa;
- níveis de aprendizagem;
- visualização final;
- executor do Goal.

## Gate de liberação
Este Goal está **preparado**, mas deliberadamente **não está liberado**.

Não alterar para `READY_FOR_CODEX`, `READY_FOR_GEMINI` ou outro estado executável até André escolher o executor. Essa escolha deve também definir onde o relatório/handoff da execução será registrado.

Ao escolher o executor:
1. registrar o executor;
2. definir o destino do retorno;
3. mudar apenas então para o estado executável correspondente.
