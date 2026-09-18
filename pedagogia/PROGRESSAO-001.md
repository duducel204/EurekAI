# Trilhas de Progressão Progressiva — Recorte P-001

**Estado:** CONCLUÍDO (Derivado do GOAL-006, alimentado por R-001, R-002 e R-003)
**Premissa:** Zero pressuposto conceitual. Separação explícita entre relações observadas e escolhas pedagógicas.

## Trilha A: Soberania de Dados e Limitações Locais (Eixo Cognitivo: Intencionalidade)

1. **Ponto de Partida (Zero Pressuposto):** introduzir intuitivamente privacidade e custódia de dados.
2. **A Tensão Prática (O Gancho):** como usufruir de assistentes inteligentes mantendo processamento/dados sob controle local? A direção de processamento local e privacidade está documentada em `E-017`.
3. **Representação candidata:** apresentar computação local/na borda e ambientes autocontidos usando o contexto `#termux` como exemplo, não como pré-requisito demonstrado.
4. **A Fronteira Atual / Lacuna Histórica:** usar a tradução offline ainda não concluída (`E-018`) como exemplo de diferença entre direção arquitetural e implementação efetiva.

* **Base factual:** R-003 sustenta coexistência contextual entre E-017 e E-018.
* **Hipótese pedagógica:** a ordem acima é uma escolha didática candidata; R-003 não demonstra dependência técnica ou cognitiva entre seus passos.

## Trilha B: Isolamento de Ambientes e Pontes de Comunicação (Eixo Técnico: Engenharia)

1. **Ponto de Partida (Zero Pressuposto):** introduzir intuitivamente separação de responsabilidades e ambientes.
2. **O Conceito de Desacoplamento:** usar a separação documentada em `E-014` como caso concreto.
3. **O Mecanismo de Integração (A Ponte):** apresentar comunicação padronizada entre ambientes separados usando a ponte MCP observada em `E-015` e relatada em `E-016`.
4. **A Verificação Silenciosa (Automação):** usar a CI de `E-015` para explicar verificação automatizada, preservando o limite de que sucesso no runner não comprova execução no aparelho.

* **Base factual:** R-001 e R-002 sustentam relações contextuais.
* **Hipótese pedagógica:** a ordem separação → ponte → CI é candidata; as relações observadas não provam que compreender E-014 seja pré-requisito técnico ou cognitivo para compreender E-015/E-016.

## Diferenciação Epistemológica da Progressão

* **Relações observadas:** R-001, R-002 e R-003 fornecem contexto e casos concretos.
* **Dependência técnica:** nenhuma dependência pedagógica/técnica entre os conceitos foi demonstrada pelo recorte atual.
* **Hipóteses pedagógicas:** as duas ordens propostas são caminhos candidatos a testar; não são currículo obrigatório nem inferência sobre domínio de André.
* **Bifurcação:** as trilhas A e B podem ser percorridas independentemente; o corpus atual não sustenta uma ordem obrigatória entre elas.