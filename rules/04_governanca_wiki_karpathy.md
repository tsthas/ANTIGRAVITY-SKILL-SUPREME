# 🧠 SISTEMA DE GOVERNANÇA: WIKI KARPATHY (SEGUNDO CÉREBRO)

> **Propósito:** Padronizar a gestão do Segundo Cérebro no ecossistema Antigravity integrado ao Obsidian, mantendo uma base de conhecimento destilada, hiperconectada por wikilinks e pronta para ingestão contínua por agentes autônomos.

---

## 📂 1. Estrutura de Diretórios Obrigatória

```text
├── RAW/                      # Arquivos brutos (transcrições, clips web, notas brutas, PDFs)
│   └── _processados/         # Destino de arquivos brutos já ingeridos
└── WIKI/                     # Conhecimento destilado e estruturado
    ├── fontes/               # Resumos fiéis de cada documento original
    ├── conceitos/            # Definições técnicas atômicas, frameworks e padrões
    ├── entidades/            # Pessoas, ferramentas, empresas, APIs, bibliotecas, modelos
    ├── sinteses/             # Visões consolidadas e tópicos agregadores macro
    └── index.md              # Grafo mestre e índice de entrada
```

---

## ⚙️ 2. Pipeline de Ingestão (Comando `/ingerir`)

Sempre que acionado pelo comando `/ingerir` ou ao processar itens em `RAW/`:

1. **Leitura e Extração:**
   - Analisar o arquivo bruto em `RAW/`.
   - Extrair entidades-chave, termos técnicos, conceitos, autores e decisões operacionais.
2. **Destilação da Fonte (`WIKI/fontes/`):**
   - Criar arquivo Markdown com o resumo estruturado (`fonte-[nome-do-arquivo].md`).
   - Registrar referências temporais e metadados de origem.
3. **Criação e Atualização Atômica:**
   - **Conceitos (`WIKI/conceitos/`):** Uma ideia técnica por arquivo.
   - **Entidades (`WIKI/entidades/`):** Documentar ferramentas, APIs, LLMs ou serviços.
   - **Sínteses (`WIKI/sinteses/`):** Criar nós agregadores sempre que um tópico aparecer em $\ge 3$ fontes.
4. **Conexões Semânticas (Wikilinks Obsidian):**
   - Utilizar links bidirecionais no formato `[[Nome da Nota]]`.
   - Toda nota gerada DEVE conter uma seção final `## Relações` com links estruturados.
5. **Limpeza e Manutenção:**
   - Mover o arquivo original processado para `RAW/_processados/`.
   - Atualizar `WIKI/index.md` com os novos links e categorias.

---

## 📐 3. Template Obrigatório de Nota Atômica

```markdown
---
tipo: [fonte | conceito | entidade | sintese]
data_ingestao: YYYY-MM-DD
tags: [#categoria, #subcategoria]
---

# Nome do Tópico

## Resumo Executivo
[Explicação concisa, precisa e direta em 2 a 3 frases]

## Detalhes & Aplicação
- [Ponto chave 1 com links: [[Outro Conceito]]]
- [Ponto chave 2 com referências cruzadas: [[Entidade Relacionada]]]

## Relações
- **Origem / Fonte:** [[fonte-origem]]
- **Relacionados:** [[Conceito A]], [[Entidade B]]
```

---

## 🔁 4. Protocolo Looping (Processamento em Lote Autônomo)

Quando disparado o comando `/looping` ou rotina em lote:
* O agente lista todos os arquivos na raiz de `RAW/`.
* Itera sequencialmente sobre cada item, gerando fontes, conceitos, entidades e atualizando o `WIKI/index.md`.
* Move para `RAW/_processados/` sem interromper o fluxo até a pasta estar completamente esgotada.
