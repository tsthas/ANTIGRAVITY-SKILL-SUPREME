---
name: looping
description: >-
  Executa o protocolo autônomo de ingestão em fila da Wiki Karpathy (Segundo Cérebro).
  Ative ao usar /looping ou quando precisar processar em lote todos os arquivos presentes
  na pasta RAW/, gerando resumos em WIKI/fontes/, conceitos atômicos, entidades, wikilinks [[...]],
  atualizando o WIKI/index.md e movendo os originais para RAW/_processados/.
---

# Skill: Looping de Ingestão de Conhecimento (Wiki Karpathy)

Esta skill executa o pipeline autônomo e iterativo de processamento de dados da pasta `RAW/` para a base estruturada `WIKI/`.

---

## 🎯 PROTOCOLO DE EXECUÇÃO AUTÔNOMA

Sempre que acionado pelo comando `/looping` ou quando solicitado o processamento em lote da pasta `RAW/`, assuma a postura de **Executor de Ingestão de Conhecimento** e execute o seguinte ciclo até que a pasta `RAW/` esteja completamente vazia:

### Ciclo Iterativo:

1. **PASSO 1 - Varredura de Fila:**
   * Inspecione o diretório `RAW/` no workspace ativo e liste todos os arquivos pendentes (excluindo a subpasta `_processados/`).
   * Se não houver nenhum arquivo pendente, finalize imediatamente informando:
     > `✅ Fila de ingestão concluída. A pasta RAW/ está vazia e o WIKI/index.md foi atualizado.`

2. **PASSO 2 - Processamento Atômico do Primeiro Arquivo:**
   * Selecione o primeiro arquivo da lista em `RAW/`.
   * Leia o conteúdo integral do arquivo.
   * Extraia entidades-chave, termos técnicos, conceitos fundamentais e decisões operacionais.

3. **PASSO 3 - Destilação da Fonte (`WIKI/fontes/`):**
   * Crie o arquivo `WIKI/fontes/fonte-[nome-do-arquivo].md` com o resumo executivo, tópicos-chave e referências temporais/de origem.

4. **PASSO 4 - Criação e Conexão de Nós Semânticos:**
   * **Conceitos (`WIKI/conceitos/`):** Crie notas atômicas (uma ideia por arquivo) para termos técnicos ou frameworks novos.
   * **Entidades (`WIKI/entidades/`):** Documente ferramentas, bibliotecas, modelos ou APIs citadas.
   * **Sínteses (`WIKI/sinteses/`):** Se um tema se repetir em 3 ou mais fontes ao longo do histórico, crie ou atualize o nó de síntese agregador.
   * **Wikilinks Obrigatórios:** Todas as notas geradas devem usar links bidirecionais no padrão Obsidian `[[Nome da Nota]]` e conter a seção final `## Relações`.

5. **PASSO 5 - Atualização do Grafo de Entrada:**
   * Adicione os novos links gerados no arquivo central `WIKI/index.md`.

6. **PASSO 6 - Limpeza e Arquivamento:**
   * Crie a pasta `RAW/_processados/` caso não exista.
   * Mova o arquivo original processado de `RAW/` para `RAW/_processados/`.

7. **PASSO 7 - Próximo Ciclo Automático:**
   * **NÃO pare nem solicite confirmação intermediária.** Volte imediatamente ao **PASSO 1** e processe o próximo arquivo da fila até esgotar todos os itens de `RAW/`.

---

## 📐 PADRÃO OBRIGATÓRIO DE NOTA MARKDOWN

Toda nota atômica deve seguir este formato:

```markdown
---
tipo: [fonte | conceito | entidade | sintese]
data_ingestao: YYYY-MM-DD
tags: [#categoria, #subcategoria]
---

# Nome do Tópico

## Resumo Executivo
[Explicação concisa e direta em 2-3 frases]

## Detalhes & Aplicação
- [Ponto chave 1 com links: [[Outro Conceito]]]
- [Ponto chave 2]

## Relações
- **Origem / Fonte:** [[fonte-origem]]
- **Relacionados:** [[Conceito A]], [[Entidade B]]
```
