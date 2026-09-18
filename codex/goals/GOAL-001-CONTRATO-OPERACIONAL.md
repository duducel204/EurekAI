# GOAL-001 — Estabelecer o contrato operacional do EurekAI

**Status:** READY_FOR_CODEX  
**Fase:** Fundação  
**Tipo:** Planejamento, inspeção e formalização  
**Execução de conteúdo pedagógico:** NÃO AUTORIZADA

## Intent

Estabelecer um contrato operacional claro para o EurekAI antes da geração sistemática da base de conhecimento.

O objetivo deste Goal é permitir que o Codex compreenda o projeto, inspecione o estado real do repositório, identifique quais fontes de informação estão efetivamente disponíveis e formalize regras suficientes para que Goals posteriores possam trabalhar sem inventar conhecimento do autor, perder rastreabilidade ou confundir exploração com decisão.

## Current State

O repositório EurekAI está em fase inicial.

Já existem diretórios destinados a contexto, capturas, conhecimento, experiências, erros, descobertas, mapa do conhecimento, decisões, hipóteses, pedagogia, ideias de produto, integração com Codex e templates.

Existe também um registro inicial de origem e direção do projeto.

A estrutura atual é uma fundação de trabalho. Ela não deve ser interpretada como taxonomia definitiva do conhecimento.

## Context

O EurekAI pretende externalizar e estruturar o conhecimento adquirido por André através de estudo, experimentação, projetos, erros, descobertas e uso prático de inteligência artificial, computação, programação, ferramentas digitais e assuntos relacionados.

O autor não deve precisar reconstruir manualmente todo o seu conhecimento por meio de uma entrevista conceito por conceito.

Sempre que possível, Goals posteriores deverão utilizar evidências existentes em fontes reais — conversas, projetos, arquivos, código, erros, soluções e outros registros — para reconstruir o mapa de conhecimento do autor.

Exposição a um conceito não comprova domínio.

Exemplos:

- ter perguntado sobre API não significa dominar APIs;
- ter utilizado uma ferramenta comprova experiência, não necessariamente compreensão profunda;
- ter resolvido um problema fornece evidência diferente de apenas ter recebido uma explicação;
- conhecimento tácito ou parcialmente articulado deve ser preservado como tal.

## Princípios epistemológicos

Quando aplicável, distinguir explicitamente:

- **FATO** — informação observada ou verificável;
- **EXPERIÊNCIA** — algo que o autor efetivamente fez, tentou ou encontrou;
- **DECISÃO** — direção explicitamente escolhida pelo autor;
- **HIPÓTESE** — interpretação ou possibilidade ainda não confirmada;
- **TENSÃO** — informações ou direções que entram em conflito;
- **LACUNA** — informação necessária ainda ausente;
- **NÃO DECIDIDO** — alternativas ainda abertas;
- **CONHECIMENTO TÁCITO** — percepção ou capacidade existente que ainda não foi suficientemente articulada;
- **EVIDÊNCIA** — registro que sustenta uma inferência sobre conhecimento ou experiência.

Não converter automaticamente hipótese em decisão, exposição em domínio ou interpretação do assistente em conhecimento do autor.

## Modelo de trabalho

Fluxo conceitual pretendido:

```text
André
  ↓
conversa / projetos / experiências / registros
  ↓
exploração e planejamento
  ↓
convergência
  ↓
Goal
  ↓
Codex
  ↓
inspeção do estado real
  ↓
execução autorizada
  ↓
validação
  ↓
retorno com evidências
  ↓
nova análise
  ↺
```

PLAN e EXECUTE são estados diferentes.

Quando um Goal solicitar apenas inspeção ou planejamento, não antecipar execução estrutural ou produção massiva de conteúdo.

## Papel do Codex

O Codex deve funcionar como executor e agente de automação sobre o estado real do repositório.

Antes de agir:

1. ler o contexto existente;
2. inspecionar o repositório;
3. verificar as fontes realmente acessíveis;
4. identificar ambiguidades que alterem materialmente a execução;
5. respeitar o escopo do Goal;
6. evitar preencher lacunas com suposições.

Após agir:

1. validar o resultado;
2. registrar alterações de forma rastreável;
3. informar evidências;
4. informar lacunas;
5. informar decisões que ainda dependem do autor;
6. indicar o próximo estado possível sem executá-lo automaticamente quando estiver fora do Goal.

## In Scope

Neste Goal, o Codex deve:

1. inspecionar integralmente a estrutura atual do repositório;
2. ler os documentos de contexto existentes;
3. identificar a função aparente de cada diretório existente;
4. verificar quais fontes externas ou históricas estão realmente acessíveis no ambiente atual;
5. classificar essas fontes;
6. propor um contrato operacional mínimo para Goals posteriores;
7. identificar riscos de perda de informação, suposição, duplicação e drift;
8. propor como preservar procedência e estado epistemológico das informações;
9. verificar se a estrutura atual é suficiente para iniciar o GOAL-002;
10. retornar relatório objetivo com evidências.

## Inventário obrigatório de fontes

Para cada fonte potencialmente relevante, classificar como:

- **DISPONÍVEL** — Codex consegue acessar diretamente agora;
- **NÃO DISPONÍVEL** — não existe acesso no ambiente atual;
- **PRECISA SER EXPORTADA** — existe, mas precisa ser fornecida ao ambiente;
- **PODE SER AUTOMATIZADA** — existe caminho técnico plausível para ingestão automatizada;
- **EXIGE INTERVENÇÃO DO ANDRÉ** — depende de ação humana.

Não afirmar acesso a uma fonte sem testá-lo.

Fontes a considerar incluem, sem limitar:

- repositório EurekAI;
- outros repositórios relevantes;
- arquivos locais disponíveis ao ambiente;
- documentação de projetos;
- código;
- histórico Git;
- conversas exportadas ou disponibilizadas;
- handoffs;
- registros de erros e soluções;
- outras fontes identificadas durante a inspeção.

## Out of Scope

Neste Goal, NÃO:

- gerar toda a base de conhecimento;
- inventar níveis pedagógicos definitivos;
- preencher diretórios com conteúdo genérico sobre IA;
- afirmar o nível de domínio do autor sem evidência;
- criar produto, site, aplicativo ou jogo;
- implementar arquitetura complexa sem necessidade demonstrada;
- executar o GOAL-002;
- reorganizar massivamente o repositório sem autorização;
- apagar conteúdo existente apenas porque uma estrutura alternativa parece melhor.

## Diretriz pedagógica preservada

Goals posteriores deverão buscar explicações atemporais e intuitivas.

Princípio:

> compreensão antes de terminologia, sem sacrificar precisão.

Quando útil, o conhecimento poderá seguir progressão semelhante a:

```text
intuição
→ metáfora ou comparação
→ modelo mental
→ exemplo concreto
→ conceito
→ mecanismo
→ terminologia técnica
→ experimento
→ aplicação
→ aprofundamento
```

Metáforas devem facilitar compreensão, não substituir precisão técnica.

O conteúdo não deve depender desnecessariamente de uma faixa etária específica. Uma boa explicação fundamental deve poder ajudar crianças, adultos e pessoas mais velhas, variando posteriormente profundidade, ritmo e interação quando necessário.

## Proveniência

Goals posteriores devem preservar, quando relevante, a origem das informações.

Exemplo conceitual:

```text
AUTOR DISSE
→ evidência direta

AUTOR FEZ
→ experiência observável/documentada

ASSISTENTE PROPÔS
→ hipótese ou proposta

AUTOR CONFIRMOU
→ informação validada pelo autor

NÃO CONFIRMADO
→ permanece hipótese, captura ou pendência
```

## Deliverables

Ao concluir este Goal, produzir no repositório:

1. um relatório de inspeção do estado atual;
2. um inventário das fontes disponíveis e indisponíveis;
3. uma proposta de contrato operacional mínimo para o Codex;
4. uma lista de riscos e mecanismos de mitigação;
5. uma avaliação objetiva de prontidão para o GOAL-002;
6. uma lista curta de perguntas bloqueadoras, somente se realmente necessárias.

Os nomes e localização exatos dos arquivos podem ser escolhidos pelo Codex de acordo com a estrutura existente, desde que sejam claros e rastreáveis.

## Acceptance Criteria

O Goal será considerado concluído quando:

- o estado real do repositório tiver sido inspecionado;
- nenhuma fonte tiver sido presumida como acessível sem verificação;
- estiver claro de onde o GOAL-002 poderá obter evidências;
- estiver definido como diferenciar evidência, inferência, hipótese e decisão;
- estiver definido como impedir que exposição seja tratada como domínio;
- riscos principais estiverem registrados;
- nenhuma geração massiva de conteúdo tiver sido iniciada;
- nenhuma arquitetura definitiva tiver sido imposta sem necessidade;
- o Codex retornar evidências suficientes para André e a conversa de planejamento decidirem o próximo passo.

## Stop Conditions

Interromper e retornar ao autor quando:

- uma decisão necessária estiver fora do escopo deste Goal;
- uma fonte essencial exigir credencial, permissão ou ação humana;
- houver risco de perda ou sobrescrita de informação;
- duas interpretações produzirem consequências arquitetônicas materialmente diferentes;
- o Goal não puder ser concluído sem inventar informação.

## Return to André

O retorno deve ser curto, verificável e estruturado em:

1. **O que foi inspecionado**
2. **O que foi encontrado**
3. **Fontes disponíveis**
4. **Fontes ausentes ou bloqueadas**
5. **Riscos**
6. **Arquivos criados ou alterados**
7. **Evidências de validação**
8. **Prontidão para GOAL-002**
9. **Decisões necessárias do André**, se houver

Não iniciar GOAL-002 automaticamente.

---

## Próximo Goal previsto

**GOAL-002 — Reconstruir o mapa de conhecimento do autor a partir de evidências.**

GOAL-002 permanece apenas previsto até revisão dos resultados deste Goal.
