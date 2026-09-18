# Framework de Engenharia Pedagógica Atemporal

**Estado:** CONCLUÍDO (Derivado do GOAL-007, operacionalizando o arcabouço de `pedagogia/PROGRESSAO-001.md`)
**Diretriz Fundamental:** Compreensão estrutural e intuitiva antes da nomenclatura técnica quando isso ajudar, preservando rigor e procedência.

## 1. Protocolo de Transformação Pedagógica

Uma unidade pode usar, adaptar ou alternar a seguinte sequência:

$$\text{Intuição Prática} \longrightarrow \text{Modelo Mental/Analogia} \longrightarrow \text{Mecanismo Invariante} \longrightarrow \text{Terminologia Técnica} \longrightarrow \text{Aplicação/Experimento}$$

A sequência é repertório de transformação, não cadeia causal nem template obrigatório. Quando uma representação não funcionar, deve-se trocar analogia, exemplo, profundidade ou experimento sem alterar o mecanismo técnico central.

## 2. Separação: Mecanismo Atemporal vs. Implementação Efêmera

Para reduzir obsolescência, separar o mecanismo conceitual da ferramenta usada como exemplo.

| Dimensão atemporal | Instanciação versionada | Exemplo no corpus |
| --- | --- | --- |
| **Isolamento de contexto:** separação de responsabilidades/ambientes para reduzir acoplamento e interferência entre dependências. | Repositórios Git separados e contextos Windows/Termux. | `E-014` |
| **Interface/protocolo entre contextos:** comunicação padronizada entre componentes separados. | MCP no contexto testado/documentado. | `E-015`, `E-016` |
| **Processamento local como direção arquitetural:** manter processamento sob controle local quando esse requisito existir. | Direção documentada para processamento local e tradução offline ainda pendente. | `E-017`, `E-018` |

Os exemplos não transformam automaticamente a ferramenta citada em única implementação possível do mecanismo.

## 3. Critérios para Uso Didático de Falhas e Lacunas Reais

Falhas, tensões e lacunas só podem virar material didático com procedência suficiente.

* **Estado correto:** distinguir erro observado, relato de erro, pendência, tensão documental e hipótese; não chamar uma pendência de impossibilidade.
* **O erro/lacuna como caso técnico:** demonstrar mecanismo ou limite técnico sem convertê-lo em julgamento pessoal.
* **Rastreabilidade:** todo caso real deve apontar para a evidência/experiência que o sustenta e preservar seus limites.
* **Representação alternativa:** se o caso não destravar compreensão, trocar analogia, exemplo ou experimento sem mudar o conceito central.

## 4. Estrutura Mínima para Unidades de Conteúdo — Diretriz para GOAL-008

As futuras unidades devem registrar, no mínimo:

1. **Objetivo de compreensão:** qual mecanismo/intuição se pretende transmitir.
2. **Vínculo de evidência:** IDs que ancoram exemplos reais; quando a parte for puramente pedagógica, rotulá-la como hipótese/representação.
3. **Representação inicial:** analogia, comparação ou modelo mental apropriado.
4. **Mecanismo e terminologia:** explicação tecnicamente precisa, separada da analogia.
5. **Experimento/aplicação:** cenário reproduzível quando aplicável.
6. **Alternativa de representação:** pelo menos uma forma de reexplicar o mesmo mecanismo quando necessário.
7. **Temporalidade:** indicar o que é mecanismo atemporal e o que depende de ferramenta/versão.

## 5. Teste contra as trilhas atuais

* **Trilha A:** o framework separa a direção atemporal de controle/processamento local do exemplo versionado Termux/tradução offline e mantém a ordem como hipótese pedagógica.
* **Trilha B:** o mesmo framework separa isolamento/comunicação/verificação como mecanismos dos exemplos Git/MCP/CI, sem converter sua sequência contextual em pré-requisito obrigatório.

Assim, o contrato é reutilizável nas duas trilhas atuais sem universalizar as relações observadas no corpus.