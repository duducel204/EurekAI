# Registro de contexto — origem e direção do EurekAI

> Estado: exploração  
> Natureza: registro de contexto, não especificação definitiva  
> Regra: este documento preserva o raciocínio atual sem transformar hipóteses em decisões.

## 1. Origem

O EurekAI nasceu da intenção de externalizar e registrar o conhecimento que André adquiriu sobre inteligência artificial, computação, ferramentas e desenvolvimento por meio de uso prático, experimentação, projetos, erros, descobertas e resolução de problemas.

A intenção inicial não é produzir uma enciclopédia genérica sobre IA. O ponto de partida é registrar aquilo que o autor efetivamente sabe, entende, já utilizou, tentou, resolveu ou ainda não consegue explicar completamente.

Também são relevantes conhecimentos tácitos: situações em que existe percepção prática ou intuição, mas o conhecimento ainda não foi formalizado em uma explicação precisa.

## 2. Horizonte do conhecimento

Existe a intenção de organizar esse conhecimento de forma que possa ser compreendido progressivamente desde um usuário de nível zero — alguém sem os conhecimentos prévios do autor — até níveis mais avançados próximos da fronteira atual de conhecimento e prática do próprio autor.

A ordem, os níveis e a taxonomia definitivos ainda não estão definidos.

Conhecimentos avançados utilizados durante a própria construção do projeto — por exemplo GitHub, Codex, workflows, automação, agentes e arquitetura de repositórios — podem posteriormente tornar-se parte dos níveis avançados do conhecimento registrado.

## 3. Separação importante

Há duas coisas diferentes que não devem ser confundidas.

### Conteúdo / conhecimento

É aquilo que está sendo externalizado, estruturado, relacionado e posteriormente poderá ser utilizado por alguém que parte de níveis anteriores de conhecimento.

### Mecanismo de construção

É o conjunto de ferramentas e processos usados para desenvolver o próprio repositório, incluindo a interação entre André, ChatGPT, Codex e GitHub.

O mecanismo de construção não deve determinar automaticamente a estrutura pedagógica do conteúdo.

## 4. Função desta conversa de planejamento

A conversa utilizada para desenvolver o EurekAI funciona como um laboratório cognitivo de alta temperatura.

Ela pode:

- explorar livremente;
- levantar possibilidades;
- decompor ideias;
- relacionar conhecimentos;
- identificar contradições;
- recuperar experiências;
- formular hipóteses;
- identificar lacunas;
- ajudar a tornar explícito conhecimento tácito;
- convergir posteriormente para informações úteis ao Codex.

Durante essa exploração, uma interpretação proposta pelo assistente não deve ser automaticamente tratada como conhecimento ou decisão do autor.

É importante distinguir, quando aplicável:

- informação fornecida pelo autor;
- experiência relatada;
- decisão;
- hipótese;
- interpretação;
- dúvida;
- lacuna;
- possibilidade futura;
- conhecimento ainda difícil de explicar.

O vai e volta da exploração pode ser útil. O requisito é preservar o estado epistemológico das ideias e evitar que exploração seja confundida com decisão.

## 5. Função esperada do Codex

O Codex será utilizado como agente de execução e automação sobre o repositório.

As informações exploradas na conversa podem ser convergidas em contexto, objetivos, restrições, critérios e tarefas que serão transferidos ao Codex.

O Codex deve trabalhar a partir do estado real do repositório e não de uma estrutura presumida quando essa estrutura ainda não tiver sido decidida.

O fluxo pretendido, ainda sujeito a refinamento, é aproximadamente:

```text
André
  ↓
exploração e planejamento
  ↓
convergência
  ↓
instrução / objetivo para Codex
  ↓
Codex trabalha no repositório
  ↓
resultado e evidências
  ↓
nova análise
  ↓
próxima iteração
```

## 6. Possibilidade futura preservada

Durante a exploração surgiu a possibilidade de que a base de conhecimento possa posteriormente alimentar uma experiência educacional progressiva e interativa, inclusive um site, aplicativo ou jogo capaz de ensinar inteligência artificial e conhecimentos relacionados para adultos e crianças.

Também surgiu a hipótese de valor de que responsáveis possam atribuir valor a uma experiência que prepare crianças para compreender, questionar, utilizar e construir com inteligência artificial.

Isso é uma possibilidade futura importante, mas não deve ser confundida com o objetivo operacional imediato do repositório nem tratada como produto já decidido.

## 7. Princípio para as próximas iterações

Antes de transformar exploração em estrutura definitiva:

1. preservar a informação;
2. identificar sua natureza e seu estado;
3. separar o que foi decidido do que ainda está sendo explorado;
4. convergir apenas quando houver informação suficiente;
5. então transferir um objetivo claro ao Codex;
6. analisar o resultado antes da próxima execução.

Este documento deve evoluir conforme o entendimento do projeto amadurecer. Mudanças de direção relevantes devem permanecer rastreáveis pelo histórico do Git.
