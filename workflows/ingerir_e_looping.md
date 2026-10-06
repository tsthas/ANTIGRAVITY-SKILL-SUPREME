# 📥 Workflow: `/ingerir` — Ingestão Atômica de Conhecimento

> Processa um único arquivo de dado bruto da pasta `RAW/` e o destila para o formato estruturado do Obsidian na pasta `WIKI/`.

---

## ⚡ Como Invocar
```text
/ingerir RAW/nota_reuniao_projeto.txt
```

---

## 🔄 Passos Executados pelo Agente
1. Lê o documento original em sua totalidade.
2. Extrai entidades, tecnologias, decisões e conceitos.
3. Cria o resumo estruturado em `WIKI/fontes/fonte-[nome].md`.
4. Atualiza ou gera as notas atômicas em `WIKI/conceitos/` e `WIKI/entidades/`.
5. Interconecta tudo com links bidirecionais `[[Wikilinks]]`.
6. Atualiza o índice mestre `WIKI/index.md`.
7. Move o arquivo original para `RAW/_processados/`.

---

# 🔁 Workflow: `/looping` — Ingestão Autônoma de Fila

> Processa múltiplos arquivos em lote de forma sequencial sem interrupção humana até esgotar a fila de entrada.

---

## ⚡ Como Invocar
```text
/looping
```

---

## 🔄 Passos do Ciclo em Loop
1. Varre `RAW/` em busca de arquivos não processados.
2. Se vazio, emite confirmação de encerramento e exibe o resumo do grafo atualizado.
3. Se contiver arquivos:
   - Pega o primeiro da fila.
   - Executa o pipeline completo do `/ingerir`.
   - Mover para `RAW/_processados/`.
   - Reinicia imediatamente o ciclo para o próximo arquivo sem aguardar nova confirmação.
