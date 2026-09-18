# Trilhas de Progressão Progressiva — Recorte P-001

**Estado:** CONCLUÍDO (Derivado do GOAL-006, alimentado por R-001, R-002 e R-003)
**Premissa:** Zero pressuposto conceitual. Separação explícita de dependências.

## Trilha A: Soberania de Dados e Limitações Locais (Eixo Cognitivo: Intencionalidade)

1.  **Ponto de Partida (Zero Pressuposto):** A necessidade humana elementar de privacidade. O conceito intuitivo de que dados confidenciais (como áudio ou texto pessoal) não devem trafegar em servidores de terceiros.
2.  **A Tensão Prática (O Gancho):** Como usufruir de assistentes inteligentes sem abrir mão da custódia do dado? (Conexão com a diretriz declarada em `E-017`).
3.  **O Mecanismo de Execução Sandbox:** Introdução ao conceito de computação de borda ou local utilizando ambientes autocontidos (Intuição baseada no contexto `#termux`).
4.  **A Fronteira Atual / Lacuna Histórica:** A complexidade real de manter um sistema 100% isolado. Estudo de caso da pendência de tradução offline aberta (`E-018`), ilustrando que escolhas arquiteturais geram trade-offs de engenharia.

*   *Status de Dependência:* Vínculo cognitivo estabelecido a partir da relação **R-003**.

## Trilha B: Isolamento de Ambientes e Pontes de Comunicação (Eixo Técnico: Engenharia)

1.  **Ponto de Partida (Zero Pressuposto):** O problema prático do conflito de ferramentas. A intuição de que misturar as configurações de dois sistemas operacionais diferentes em uma única pasta causa quebra de ambiente.
2.  **O Conceito de Desacoplamento:** A decisão lógica de separar projetos e responsabilidades em repositórios isolados (Conexão direta com a ação material documentada em `E-014`).
3.  **O Mecanismo de Integração (A Ponte):** Como fazer duas coisas separadas conversarem de forma padronizada sem se fundirem? O conceito abstrato de um servidor ou protocolo de contexto (Intuição da ponte MCP amparada por `E-015` e `E-016`).
4.  **A Verificação Silenciosa (Automação):** O uso de robôs invisíveis de checagem (Integração Contínua / CI) para garantir que a ponte não quebre a cada pequena alteração (`E-015`).

*   *Status de Dependência:* Vínculo sistêmico derivado das relações **R-001** e **R-002**.

## Diferenciação Epistemológica da Progressão
*   **Dependência Técnica:** Para entender a ponte (`E-015`), o aprendiz precisa compreender primeiro o motivo da separação dos ambientes (`E-014`).
*   **Hipótese Pedagógica:** Propor a intuição da "privacidade absoluta" como vetor para ensinar infraestrutura local é uma escolha didática a ser testada no GOAL-009; o corpus sustenta o fato de que a diretriz existia, não que este seja o único caminho de ensino.