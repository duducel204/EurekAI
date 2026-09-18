# Índice de Tags — EurekAI

**Estado:** EXPERIMENTAL / EVOLUTIVO

Tags funcionam como uma matriz de conexão sobre o corpus. Elas não substituem procedência, IDs de evidência ou relações explícitas quando necessárias. Evitam duplicar o mesmo conteúdo em várias estruturas.

## Sintaxe mínima

Usar tags legíveis em minúsculas, sem acentos, quando possível:

`#api #artefato #erro #diagnostico #plano`

Uma unidade pode ter várias tags. A combinação funciona como uma consulta/lente.

Exemplos:
- `#api #artefato` — artefatos relacionados a API.
- `#api #erro #diagnostico` — problemas e diagnósticos envolvendo API.
- `#github #plano` — planos envolvendo GitHub.
- `#mcp #reaplicacao` — reaplicações envolvendo MCP.
- `#ia #ideia #conceito-antes-do-nome` — ideias em que o mecanismo apareceu antes do termo.

## Famílias iniciais — abertas

### Assunto / tecnologia
`#api #github #github-cli #pr #auto-merge #git #ssh #shell #automacao #script #validacao #codex #mcp #termux #powershell #gemini #openwebui #cloud #agentes`

### Natureza do item
`#evidencia #artefato #documento #ideia #plano #decisao #hipotese #experiencia #erro #descoberta #pendencia`

### Evento / trajetória
`#pergunta #tentativa #configuracao #uso #diagnostico #solucao #reaplicacao #explicacao #construcao #mudanca-de-direcao`

### Cognição / aprendizagem
`#conceito-antes-do-nome #nome-antes-da-compreensao #transicao-mental #conhecimento-tacito #reaprendizagem #estalo`

### Participação humano–IA
`#ia-explicou #andre-propos #ia-propos #andre-modificou #andre-rejeitou #andre-corrigiu-ia #autoria-incerta`

## Adição justificada no GOAL-004

`#termux` conecta E-014–E-018 no [modelo M-001](MODELO-001-CONHECIMENTO-OBSERVADO.md), permitindo consultar decisões, teste, relato e lacuna do mesmo contexto. Não é sinônimo de `#mcp`: tradução local e decisões de privacidade pertencem ao contexto Termux sem necessariamente envolver a ponte MCP. Nenhum alias novo foi necessário.

## Regra de crescimento

Não tentar prever todas as tags. Criar uma nova tag quando ela:
1. conectar material que será útil recuperar em conjunto;
2. aparecer repetidamente ou tiver alto valor de navegação;
3. não for sinônimo desnecessário de tag existente.

Antes de criar variante, consultar este índice. Quando duas tags convergirem para o mesmo significado, escolher uma canônica e registrar alias em vez de reetiquetar silenciosamente o passado.

## Tags não são conclusões

`#api` significa relação com API, não domínio de API.
`#diagnostico` exige evidência de diagnóstico naquele contexto.
`#reaplicacao` exige ocorrência posterior relacionada.
`#conceito-antes-do-nome` é candidato até a ordem histórica estar suficientemente sustentada.

## Aplicação

A partir do GOAL-004, e retroativamente quando houver ganho real, documentos, evidências, ideias, planos, artefatos e demais unidades podem receber uma linha compacta:

`Tags: #api #artefato #erro #diagnostico`

Não criar arquivos separados apenas para representar combinações de tags. Mapas e matrizes futuras devem preferir consultas/índices sobre o mesmo corpus.

## Princípio

**Uma unidade, várias conexões.**

O corpus permanece único; tags oferecem lentes cruzadas entre assuntos, artefatos, documentos, ideias, planos, experiências e trajetória cognitiva.
