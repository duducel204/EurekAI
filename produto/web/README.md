# EurekAI — Web MVP

Este diretório contém o protótipo da experiência web do EurekAI.

## Hipótese do MVP

O EurekAI não começa explicando um conceito. Ele cria uma pequena experiência em que a pessoa:

`prevê → testa → compara → percebe → descobre o princípio → aplica em outro contexto`

A unidade básica do produto é um **experimento cognitivo interativo**, não uma aula ou página de conteúdo.

## Experimento atual — Contexto

O MVP valida uma única experiência de 60–90 segundos:

1. a pessoa escolhe um modo de entrada;
2. formula uma hipótese sobre o que melhora uma resposta;
3. mantém a mesma pergunta e altera apenas o contexto;
4. compara respostas;
5. identifica por conta própria o que mudou;
6. recebe o nome do princípio somente depois da descoberta;
7. aplica o princípio a um segundo problema para testar transferência.

### Modos

- **Quero descobrir:** fluxo direto para adulto curioso.
- **Quero uma missão:** linguagem de desafio para criança/jovem.
- **Quero aprender para ensinar:** enquadramento para responsável/professor.

O princípio é o mesmo; a experiência deve poder mudar conforme o perfil. O MVP inicia essa adaptação sem duplicar conteúdo.

## Regras pedagógicas

- experiência antes do nome técnico;
- pergunta antes da explicação;
- erro gera nova evidência e nova tentativa;
- não confundir parâmetro técnico com verdade factual;
- não expor infraestrutura interna (EKL-0, pipelines, Goals) ao usuário final;
- concluir com aplicação em situação diferente para verificar compreensão.

## Implementação

HTML, CSS e JavaScript estáticos, sem cadastro, backend ou dependência de modelo externo. As respostas são explicitamente apresentadas como simuladas. Isso mantém o experimento barato, determinístico e auditável enquanto a hipótese pedagógica é validada.

O deploy continua sendo feito por GitHub Pages através de `.github/workflows/deploy-pages.yml`.

## Próximo critério de evolução

Antes de adicionar novos temas, validar se uma pessoa que entra sem conhecer o conceito consegue sair da experiência reconhecendo e aplicando o princípio de contexto.

Se isso funcionar, novos princípios podem ser transformados em novos experimentos cognitivos seguindo a mesma arquitetura.