# 📋 Workflow: `/planejar` — Do Brainstorm ao Plano de Implementação

> Este fluxo de trabalho conduz uma demanda desde a ideia embrionária até um plano de tickets atômicos pronto para execução sem desperdício de tokens.

---

## 🧭 Passo 1: Travar a Intenção (Sabatina Socrática)
1. Analise o pedido do usuário sob uma ótica crítica.
2. Formule até 4 perguntas objetivas para eliminar ambiguidades sobre:
   * **Critério de conclusão observável (Definition of Done)**.
   * **Limites do escopo** (o que NÃO deve ser feito nesta iteração).
   * **Dependências, bibliotecas permitidas e restrições de infraestrutura**.
3. **Aguarde o retorno do usuário** antes de criar ou modificar qualquer arquivo.

---

## 🏛️ Passo 2: Construir o Desenho da Arquitetura
1. Registre as decisões em `DOCUMENTACOES/YYYYMMDD_HHMM_[PROJETO]_DECISOES.md`.
2. Inclua o Genesis Prompt no topo do documento.
3. Elabore a especificação detalhada em `DOCUMENTACOES/planos_de_implementacao/`.
4. Inclua obrigatoriamente a tabela de Dicionário de Termos no encerramento.

---

## 🌊 Passo 3: Fatiar em Ondas Paralelas
1. Organize as tarefas de modo que tickets simultâneos nunca editem os mesmos arquivos.
2. Exija um comando de verificação determinístico (ex: teste unitário ou checagem de tipos) para cada tarefa.
3. Obtenha aprovação explícita do usuário antes de iniciar o ciclo de codificação.
