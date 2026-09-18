# Camada de Relações e Dependências — Índice R-001

**Estado:** CONCLUÍDO (Derivado do GOAL-005)
**Base Inferencial:** E-014 a E-019. Itens históricos E-001 a E-013 permanecem marcados como INSUFICIENTES por falta de localizadores.

## Relações Mapeadas

* **R-001 (E-014 ↔ E-015):** *Sequência Histórica / Relação Contextual*.
  * **Estado:** OBSERVADA.
  * **Descrição:** A decisão documentada de desmembrar os repositórios (E-014) e o artefato de teste Python validado em CI (E-015) pertencem ao mesmo contexto documentado e ao recorte temporal inspecionado.
  * **Limite:** A sequência/coocorrência não demonstra causalidade, dependência técnica, autoria individual ou execução em hardware físico local.

* **R-002 (E-014 ↔ E-016):** *Relação Contextual*.
  * **Estado:** OBSERVADA.
  * **Descrição:** A separação documentada do projeto (E-014) e o relato de execução da ponte com `exit_code: 0` (E-016) pertencem ao mesmo contexto Termux/MCP.
  * **Limite:** E-016 é relato documental; sem log original de runtime não se infere ator, circunstância da chamada, causalidade ou dependência em relação a E-014.

* **R-003 (E-017 ↔ E-018):** *Relação Contextual Tensionada*.
  * **Estado:** OBSERVADA.
  * **Descrição:** A direção documentada de processamento local/privacidade (E-017) coexiste no mesmo contexto com a tradução offline registrada como pendência não concluída (E-018).
  * **Limite:** O corpus sustenta intenção arquitetural + lacuna de implementação. Não demonstra que E-017 cause E-018 nem que tradução offline seja dependência técnica necessária da diretriz.

## Destino das Projeções Candidatas

* **Cluster C-001 (E-014, E-015, E-016):** preservado como agrupamento contextual. R-001 e R-002 explicitam vínculos observáveis sem promover o cluster a causalidade, pré-requisito ou transferência.
* **Cluster C-002 (E-017, E-018):** preservado como agrupamento contextual tensionado. R-003 registra a coexistência entre direção declarada e implementação incompleta, sem inferir dependência necessária.
* **Tensão T-001 (DTGEapp — E-019):** preservada como **CONTESTADA/TENSIONADA**. O README descreve módulos ativos cujos nomes não aparecem na árvore do commit `f5d4768`; E-019 não resolve qual descrição representa o estado real.

## Limites de promoção

Neste recorte não foram demonstradas causalidade, transferência pessoal, pré-requisito conceitual, trajetória cognitiva ou autoria humano–IA. Essas hipóteses permanecem insuficientes até surgirem evidências/localizadores adicionais.