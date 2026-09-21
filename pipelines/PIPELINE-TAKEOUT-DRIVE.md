# Pipeline candidata — Google Takeout/Drive v1

**Estado:** DEFINIDA, NÃO EXECUTADA
**Fonte:** Google Drive/Takeout autorizado por André
**Estado canônico:** GitHub/EurekAI após validação e PR.

## Entrada candidata

- `Takeout/Gemini`;
- `Takeout/NotebookLM`;
- `Takeout/Gemini no Workspace/Conversation History`.

Os caminhos foram fornecidos como caso de referência. Existência, conteúdo, volume, formato, acesso e autorização granular devem ser testados antes da execução. Não mover a exportação integral para o GitHub.

## Fases

1. **Pré-voo humano:** confirmar origem, diretório permitido, exclusões, dados de terceiros e política de retenção.
2. **Inventário local determinístico:** listar arquivos sem conteúdo; registrar caminho lógico redigido quando necessário, tamanho, extensão/MIME, datas disponíveis e hash. Gerar `source_id`, `item_id` e manifesto local.
3. **Indexação:** parsers por formato extraem estrutura e contagens. Conteúdo bruto continua na fonte. Itens desconhecidos ficam `BLOQUEADO`, sem leitura improvisada.
4. **Deduplicação:** hash exato consolida cópias preservando ocorrências; similaridade cria candidatos, nunca corroboração automática.
5. **Classificação:** regras identificam formatos/ruído; LLM leve recebe metadados e amostra limitada somente quando necessário. Quando aplicável, a saída deve usar `schemas/EKL-0-CLASSIFICACAO-TAKEOUT.md`.
6. **Mineração seletiva:** somente itens autorizados e relevantes, uma conversa/documento ou trecho por vez. Quando aplicável, a saída deve usar `schemas/EKL-0-MINERACAO-TAKEOUT.md`, preservando localizador e campo semântico legível.
7. **Auditoria/canonização:** validar contra original, deduplicar derivações, expandir EKL-0 quando necessário, transformar somente itens aprovados em evidência/unidade e abrir PR. Sem auto-merge.

## EKL-0 nesta pipeline

EKL-0 é uma linguagem compacta intermediária para reduzir repetição de metadados durante classificação e mineração.

Uso permitido nesta pipeline:

- classificar itens inventariados;
- registrar mineração seletiva;
- reduzir consumo de tokens;
- facilitar validação mecânica por `ferramentas/validate_ekl.py`;
- expandir para leitura humana por `ferramentas/expand_ekl.py`.

Uso proibido:

- substituir validação semântica;
- canonizar diretamente sem revisão;
- ocultar significado semântico;
- processar corpus inteiro;
- transformar comando operacional em conhecimento.

## Retomada e idempotência

O estado local por `run_id` mantém contrato, hash do manifesto, cursor e última transição confirmada de cada item. Reexecutar um item com mesmo hash e versão do processo reutiliza o resultado validado. Mudança de hash cria nova versão e marca derivações dependentes para revisão. Falha de um item não reinicia o lote.

## Controle de contexto e custo

Nenhum prompt recebe o Takeout inteiro. Limites por item/trecho e orçamento por rodada são definidos antes da mineração. Indexação, hash, fila e contagem não usam LLM. Classificação barata precede mineração mais cara. Resultados sem procedência são rejeitados.

EKL-0 reduz repetição estrutural, mas não reduz a exigência de procedência. O valor semântico extraído deve permanecer legível.

## Segurança

Não registrar credenciais, tokens, callbacks, conteúdo privado bruto ou dados de terceiros no repositório. Logs locais redigem caminhos e valores sensíveis. Falha de autenticação interrompe a fonte; não significa ausência. O executor opera somente nos diretórios explicitamente autorizados.

## Critério para primeira execução

Exige autorização do diretório real, política de dados, ferramenta/parsers escolhidos e espaço para estado local. Este documento não concede esse acesso nem afirma que os arquivos foram processados.

Antes da primeira execução real, validar o EKL-0 em amostra artificial ou amostra explicitamente autorizada e pequena.
