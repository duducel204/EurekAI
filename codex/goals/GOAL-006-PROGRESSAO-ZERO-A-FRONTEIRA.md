# GOAL-006 — Progressão do zero à fronteira atual

**Status:** CONCLUÍDO
**Executor alvo:** QUALQUER EXECUTOR AUTORIZADO
**Dependência:** GOAL-005 CONCLUÍDO e validado
**Sequência:** 005 → 006 → 007
**Modo:** EXECUTE + VALIDATE

## Intent
Derivar caminhos de aprendizagem a partir das relações realmente sustentadas pelo corpus, partindo de zero pressuposto e sem transformar a organização interna do conhecimento em currículo rígido.

## Princípios
- pode haver múltiplos caminhos para o mesmo conceito;
- pré-requisito técnico e pré-requisito cognitivo são coisas diferentes;
- relação observada não vira automaticamente ordem pedagógica;
- experiências e erros reais podem sugerir sequência, mas não impõem currículo;
- ausência de evidência gera hipótese/lacuna, não ordem inventada.

## Entrada obrigatória
Consumir o resultado **real** do GOAL-005 e seu relatório em `execucoes/`.

Não pressupor quais relações o GOAL-005 encontrará.

Relações `INSUFICIENTE` não podem ser usadas como pré-requisito positivo. Relações tensionadas devem permanecer visíveis.

## Estrutura candidata
`ponto de partida → intuição → capacidade necessária → conceito/mecanismo → experimento → aplicação → conexão seguinte`

Essa estrutura é uma lente, não um template obrigatório.

## Operação
1. Confirmar `origin/main`/base e verificar que GOAL-005 passou ao gate `CONCLUÍDO`.
2. Ler a camada de relações e o relatório do GOAL-005.
3. Identificar pontos de entrada que realmente possam partir de zero pressuposto.
4. Separar, quando sustentado:
   - pré-requisito técnico;
   - pré-requisito cognitivo;
   - conveniência de ordem;
   - hipótese pedagógica ainda não testada.
5. Derivar uma ou mais trilhas candidatas; não forçar uma única sequência.
6. Para cada passo, apontar a relação/evidência de origem ou marcar explicitamente como hipótese pedagógica.
7. Registrar bifurcações, atalhos e lacunas quando o corpus não sustentar uma ordem linear.
8. Preservar pontos de dificuldade, estalos, exemplos, exercícios e representações alternativas como matéria-prima para GOAL-007/008.
9. Não decidir níveis fixos, faixa etária, duração, gamificação ou interface.

## Deliverables
- documento canônico de progressão candidata em `pedagogia/`;
- uma ou mais trilhas derivadas, quando sustentadas;
- distinção explícita entre dependências técnicas, cognitivas e hipóteses pedagógicas;
- lacunas que impedem ordenar certos conceitos;
- derivações úteis para GOAL-007/008;
- relatório/handoff em `execucoes/`.

## Acceptance
O resultado deve:
- partir explicitamente de zero pressuposto;
- permitir mais de um caminho quando necessário;
- rastrear cada ordem proposta a relação/evidência ou marcá-la como hipótese;
- não usar relação insuficiente como fato;
- diferenciar dependência técnica de pré-requisito pedagógico;
- não classificar domínio de André;
- não duplicar o corpus em capítulos.

## Validação
Antes de `CONCLUÍDO`:
1. conferir Deliverables e Acceptance;
2. comparar cada passo de progressão com a saída real do GOAL-005;
3. verificar que hipóteses pedagógicas estão rotuladas como hipóteses;
4. executar `python ferramentas/check_all.py --base <BASE_MAIN_SHA>` quando disponível;
5. rever `origin/main` e reconciliar avanço relevante;
6. registrar relatório em `execucoes/`.

## Stop conditions
Bloquear e não promover GOAL-007 quando:
- GOAL-005 não estiver concluído/validado;
- a progressão depender de relações inexistentes ou insuficientes;
- Acceptance não puder ser demonstrado;
- mudança em `main` alterar materialmente a base;
- houver decisão humana necessária fora do escopo;
- validação falhar sem correção segura.

## Return
Registrar em `execucoes/`: executor, base, trilhas produzidas, relações usadas, hipóteses criadas, validações, lacunas e estado.

## Gate
Este Goal permanece preparado enquanto GOAL-005 não estiver `CONCLUÍDO`.

Dentro de uma sequência 005→006→007 previamente autorizada, o executor pode promovê-lo automaticamente para `READY_FOR_CODEX` somente após validar e concluir GOAL-005.

`READY_FOR_CODEX` significa **pronto para executor autorizado**.
