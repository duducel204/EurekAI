# GOAL-003 — Mineração inicial e inventário de evidências

**Status:** CONCLUÍDO COMO MINERAÇÃO INICIAL / MINERAÇÃO CONTÍNUA PODE PROSSEGUIR  
**Dependência:** GOAL-002 concluído e validado  
**Modo:** EXECUTE + VALIDATE

## Intent
Produzir inventário auditável da trajetória de conhecimento de André a partir de fontes reais/autorizadas. Não classificar domínio.

## Pergunta central
Quais pegadas observáveis existem de descoberta, pergunta, tentativa, configuração, uso, erro, diagnóstico, solução, reaplicação, comparação, explicação, construção, decisão, mudança de direção, conhecimento tácito, dúvida ou lacuna?

## Unidade mínima
Preservar quando disponível: ID; tags; evento; descrição objetiva; fonte/lote/localizador; data; ator; contexto/projeto; resultado; assistência externa/IA; interpretação; limites; estado epistemológico; confirmação; relações; derivação/linhagem.

Vocabulário observacional: EXPOSIÇÃO, PERGUNTOU, TENTOU, USOU, CONFIGUROU, ERROU, DIAGNOSTICOU, RESOLVEU, REAPLICOU, EXPLICOU, CONSTRUIU, DECIDIU.

## Tags como matriz simples
Aplicar [INDEX-TAGS](../../mapa-do-conhecimento/INDEX-TAGS.md).

Preferir:
`E-xxx | Tags: #api #erro #diagnostico #experiencia`

a duplicar a mesma evidência em estruturas separadas.

Tags devem conectar:
- assunto/tecnologia;
- natureza: evidência, artefato, documento, ideia, plano etc.;
- evento/trajetória;
- cognição/aprendizagem;
- participação humano–IA.

Uma combinação de tags funciona como consulta/lente. Relação explícita continua disponível quando a conexão não puder ser representada adequadamente por tags.

## Mineração com derivação
Aplicar [DIRETRIZ-TRANSVERSAL-DERIVACAO-REUTILIZAVEL](DIRETRIZ-TRANSVERSAL-DERIVACAO-REUTILIZAVEL.md).

Ao ler uma fonte, quando sustentado, extrair na mesma passagem:
1. evidência observável;
2. tags;
3. sequência/trajectória;
4. relações candidatas;
5. transição cognitiva;
6. matéria-prima pedagógica reutilizável;
7. possíveis destinos em Goals futuros.

Observar especialmente:
- conceito antes do nome;
- nome antes da compreensão;
- transição de modelo mental;
- reaprendizagem/retenção;
- transferência entre projetos;
- conhecimento tácito;
- tensão/contraevidência;
- autoria cognitiva humano–IA.

Essas derivações permanecem candidatas; não executam Goals posteriores.

## Escrita em alta vazão
Ler uma vez e preservar material reutilizável. Acelerar por lote, deduplicação, atualização incremental, validação mecânica e paralelização. Não acelerar por inferência sem evidência, classificação de domínio ou proliferação de arquivos.

## Inferências proibidas
Não afirmar domínio; não afirmar desconhecimento por ausência; não presumir autoria intelectual por commit; não presumir compreensão profunda por código possivelmente gerado por IA; não tratar tag como conclusão.

## Continuidade
A mineração inicial está concluída, mas novos lotes podem continuar entrando por `fontes/` e `investigacao/` enquanto Goals posteriores avançam. Não exigir mineração exaustiva antes da modelagem.

## Resultado histórico
O primeiro inventário e corpus auditável foram produzidos. GOAL-003 serve agora como contrato para mineração contínua e incremental.
