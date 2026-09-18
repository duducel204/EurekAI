# GOAL-003 — Mineração inicial e inventário de evidências

**Status:** READY_AFTER_GOAL_002_VALIDATION
**Dependência:** GOAL-002 concluído e validado
**Modo:** EXECUTE + VALIDATE

## Intent
Usar somente fontes reais disponíveis/autorizadas para produzir a primeira mineração sistemática de evidências sobre a trajetória de conhecimento de André. O resultado não é classificação final do que André sabe; é inventário auditável de evidências, lacunas, tensões e candidatos a conhecimento.

## Regra de ativação
Antes de executar, verificar o retorno do GOAL-002. Se aquisição/investigação não estiver funcional ou não houver corpus minimamente útil, não improvisar: registrar bloqueio e criar/atualizar pendências.

## Pergunta central
Quais pegadas observáveis existem de que André descobriu, perguntou, recebeu explicação, tentou, configurou, usou, errou, diagnosticou, resolveu, reaplicou, comparou, explicou, construiu, decidiu, mudou de direção, demonstrou conhecimento tácito ou apresentou dúvida/lacuna?

## In Scope
- Fixar commit/base e lote.
- Minerar somente fontes acessíveis/autorizadas.
- Extrair evidências com procedência reproduzível.
- Agrupar por tópicos somente com suporte.
- Detectar reaplicação em contextos distintos.
- Separar erros, diagnósticos e soluções.
- Registrar contraevidência, incerteza e tensões.
- Detectar conhecimento possivelmente tácito sem completá-lo.
- Identificar lacunas e transformá-las em pendências materiais.
- Produzir inventário compacto para revisão.
- Não escrever trilha pedagógica nem capítulos.

## Modelo de evidência
Preservar quando disponível: ID; tópicos candidatos; evento; descrição objetiva; fonte/localizador; data; ator; resolução de identidade; contexto/projeto; resultado; assistência externa/IA; interpretação; limites; tipo epistemológico; confirmação; relações; derivação/linhagem.

## Vocabulário observacional
EXPOSIÇÃO, PERGUNTOU, TENTOU, USOU, CONFIGUROU, ERROU, DIAGNOSTICOU, RESOLVEU, REAPLICOU, EXPLICOU, CONSTRUIU, DECIDIU.

Não é ranking de domínio. A escala DESCOBRI → ENTENDI → USEI → RESOLVI → DOMINO permanece hipótese futura; não concluir DOMINO neste Goal.

## Agrupamento
Evitar arquivo por frase. Preferir unidades agregadoras auditáveis por tema, projeto ou lote, mantendo referências individuais. Não duplicar evidência em categorias; usar relações.

## Inferências permitidas
Pergunta sustenta exposição naquele momento. Configuração documentada sustenta uso/configuração naquele contexto. Diagnóstico seguido de correção verificável sustenta diagnóstico/solução naquele contexto. Reaplicação posterior é evidência adicional. Explicação própria consistente sustenta articulação.

## Inferências proibidas
Não afirmar domínio; não afirmar desconhecimento por falta de evidência; não presumir autoria intelectual por commit; não presumir compreensão profunda por código possivelmente gerado por IA; não aplicar confirmação pontual em bloco.

## Pendências
Criar/atualizar somente quando investigação puder melhorar materialmente o inventário: outras conversas ChatGPT, outras IAs fornecidas, outro repositório, handoff/documento, confirmação específica de André ou documentação oficial para validar aspecto técnico.

## Deliverables
Manifesto do corpus; inventário inicial; tópicos candidatos provisórios; relações; lacunas/tensões; pendências; cobertura/limitações; relatório em codex/retornos/.

## Acceptance Criteria
Toda afirmação material rastreável; ausência não vira desconhecimento; eventos não achatados em sabe/não sabe; IA não atribuída automaticamente; duplicatas não corroboram artificialmente; pendências preservadas; inventário permite desenhar próximo modelo sem reler todo corpus; sem taxonomia definitiva, trilha ou capítulos.

## Stop Conditions
Aplicar GOAL-001 e GOAL-002. Corpus insuficiente deve gerar cobertura explícita e fila de investigação, nunca compensação com conhecimento genérico.

## Return
Commit/base; corpus; quantidade/tipos de evidências; tópicos candidatos; relações; lacunas/tensões; pendências; limitações; arquivos alterados; recomendação baseada em evidências. Não executar Goals posteriores.
