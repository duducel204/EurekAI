# Framework de Engenharia Pedagógica Atemporal

**Estado:** CONCLUÍDO (Derivado do GOAL-007, operacionalizando o arcabouço de `pedagogia/PROGRESSAO-001.md`)
**Diretriz Fundamental:** Compreensão estrutural e intuitiva antes da nomenclatura técnica, preservando rigor absoluto.

## 1. O Protocolo de Transformação Causal
Toda unidade de transmissão de conhecimento gerada para o EurekAI deve estruturar-se sob a seguinte esteira de conversão de conceitos:

$$\text{Intuição Prática} \longrightarrow \text{Modelo Mental/Analogia} \longrightarrow \text{Mecanismo Invariante} \longrightarrow \text{Terminologia Técnica} \longrightarrow \text{Aplicação/Experimento}$$

## 2. Separação Rígida: Mecanismo Atemporal vs. Implementação Efêmera
Para evitar a obsolescência precoce do corpus de aprendizado, a engenharia pedagógica isola o coração conceitual do ferramental de mercado.

| Dimensão Atemporal (O Mecanismo) | Instanciação Versionada (A Ferramenta) | Exemplo Prático no Corpus |
| --- | --- | --- |
| **Isolamento de Contexto:** Divisão física de processos para garantir resiliência e evitar contaminação de dependências. | Repositórios Git separados, escopos Windows vs. Termux Linux. | `E-014` |
| **Protocolo de Mensageria Comum:** Uma interface neutra que traduz intenções entre dois sistemas isolados que falam línguas distintas. | Model Context Protocol (MCP), chamadas via JSON-RPC. | `E-015` |
| **Soberania Computacional Local:** A restrição intencional de execução de dados às bordas físicas do hardware para blindagem de privacidade. | Configurações específicas de Sandbox, binários offline no Termux Android. | `E-017`, `E-018` |

## 3. Critérios para Uso Didático de Falhas Reais
Erros e lacunas materiais (como a impossibilidade de tradução offline documentada em `E-018` ou des alinhamentos de commits em `T-001`) não devem ser limpos ou omitidos do ensino. Eles serão aplicados como instrumentação de aprendizado técnico sob as seguintes regras:
*   **O Erro como Sintoma Arquitetural:** O erro deve demonstrar o limite de uma escolha técnica, nunca ser exposto como uma falha pessoal isolada.
*   **Rastreabilidade:** Qualquer exemplo de debugging inserido no material didático deve conter o ponteiro exato para a ID da experiência que o gerou, garantindo auditoria de procedência histórica.

## 4. Estrutura Mínima para Unidades de Conteúdo (Diretriz para o GOAL-008)
As futuras lições produzidas sistematicamente deverão preencher obrigatoriamente os seguintes metadados em seus blocos Markdown:
1.  **Objetivo de Compreensão:** Qual intuição o aluno reterá.
2.  **O Vínculo de Evidência:** IDs do repositório (`E-xxx`) que ancoram a realidade técnica ensinada.
3.  **A Analogia Atemporal:** A ponte de linguagem simples (ex: explicar MCP usando a analogia de um tradutor diplomático entre dois países que não partilham o mesmo alfabeto).
4.  **O Experimento Controlado:** Cenário prático reproduzível de teste baseado em histórico real.