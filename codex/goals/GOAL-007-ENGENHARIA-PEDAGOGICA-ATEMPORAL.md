# GOAL-007 — Engenharia pedagógica atemporal

**Status:** PREPARADO — NÃO LIBERADO  
**Executor alvo:** QUALQUER EXECUTOR AUTORIZADO  
**Dependência:** GOAL-006 CONCLUÍDO e validado  
**Sequência:** 005 → 006 → 007  
**Modo:** EXECUTE + VALIDATE

## Intent
Definir um contrato pedagógico reutilizável para transformar conhecimento e trajetórias reais em compreensão robusta, sem depender de moda, versão específica de ferramenta, faixa etária fixa ou formato de produto.

## Princípio
**Compreensão antes de terminologia, sem sacrificar precisão.**

Progressão candidata:
`intuição → comparação/metáfora → modelo mental → exemplo concreto → conceito → mecanismo → terminologia técnica → experimento → aplicação → aprofundamento`

Ela é um repertório de transformação, não obrigação de preencher todas as etapas.

## Entrada obrigatória
Consumir o resultado **real** do GOAL-006 e seu relatório em `execucoes/`.

Não criar pedagogia sobre uma progressão presumida.

## Hipóteses a testar
- mudar a representação pode destravar compreensão;
- conceito-antes-do-nome pode ser estratégia pedagógica;
- erros reais podem virar experimentos quando a evidência sustentar o caso;
- transições cognitivas podem indicar pontos de estalo;
- mecanismos atemporais devem ser separados de exemplos dependentes de versão/ferramenta;
- uma explicação fundamental pode servir a públicos diferentes variando profundidade, ritmo e interação.

## Operação
1. Confirmar base atual e que GOAL-006 chegou a `CONCLUÍDO`.
2. Ler progressões/trilhas reais produzidas pelo GOAL-006.
3. Derivar regras pedagógicas reutilizáveis, distinguindo:
   - mecanismo/invariante;
   - representação/analogia;
   - exemplo;
   - experimento;
   - ferramenta/versão específica.
4. Definir como trocar de representação quando uma explicação falhar sem alterar o conceito central.
5. Usar erros, tentativas e estalos reais apenas quando houver procedência suficiente; caso contrário, manter como candidato.
6. Definir um formato mínimo para futuras unidades do GOAL-008 sem produzir o conteúdo em escala.
7. Preservar alternativas: diferentes pessoas podem precisar de diferentes metáforas, exemplos ou ritmos.
8. Não decidir produto final, persona única, UI, gamificação, voz ou duração de módulos.

## Deliverables
- contrato/framework pedagógico canônico em `pedagogia/`;
- regras de transformação de conhecimento em compreensão;
- separação explícita entre mecanismo atemporal e exemplo versionado;
- estratégias de representação alternativa;
- critérios para uso pedagógico de erros/experiências reais;
- estrutura mínima candidata para GOAL-008;
- relatório/handoff em `execucoes/`.

## Acceptance
O contrato deve:
- ser aplicável a mais de uma trilha do GOAL-006;
- permitir explicar primeiro e nomear depois quando isso ajudar;
- manter precisão técnica;
- preservar procedência de exemplos reais;
- distinguir conteúdo atemporal de conteúdo dependente de ferramenta/versão;
- permitir representação alternativa sem trocar o conceito;
- entregar ao GOAL-008 estrutura suficiente para produção sistemática;
- não decidir interface/produto final.

## Validação
Antes de `CONCLUÍDO`:
1. conferir Deliverables e Acceptance;
2. testar o contrato contra pelo menos duas unidades/trilhas quando o corpus permitir; se não permitir, registrar a limitação;
3. verificar que exemplos não foram convertidos em regra universal sem suporte;
4. executar `python ferramentas/check_all.py --base <BASE_MAIN_SHA>` quando disponível;
5. rever `origin/main` e reconciliar avanço relevante;
6. registrar relatório em `execucoes/`.

## Stop conditions
Bloquear quando:
- GOAL-006 não estiver concluído/validado;
- não houver material suficiente para testar o contrato minimamente;
- o framework exigir inventar evidência ou experiência;
- Acceptance não puder ser demonstrado;
- mudança relevante de `main` invalidar premissas;
- houver decisão humana fora do escopo;
- validação falhar sem correção segura.

## Return
Registrar em `execucoes/`: executor, base, contrato produzido, testes realizados, validações, limitações, HEAD remoto final e estado.

## Gate
Este Goal permanece preparado enquanto GOAL-006 não estiver `CONCLUÍDO`.

Dentro de uma sequência 005→006→007 previamente autorizada, o executor pode promovê-lo automaticamente para `READY_FOR_CODEX` somente após validar e concluir GOAL-006.

`READY_FOR_CODEX` significa **pronto para executor autorizado**.

GOAL-007 só chega a `CONCLUÍDO` após sua própria validação; a sequência então pode ser encerrada e submetida a PR/revisão.
