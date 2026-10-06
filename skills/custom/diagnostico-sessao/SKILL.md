---
name: diagnostico-sessao
description: Audita e diagnostica sessões anteriores ou atuais do Antigravity inspecionando os arquivos transcript.jsonl para identificar loops de ferramentas, alucinações, desperdício de tokens, quebra de planos e erros repetidos, exigindo evidência citada (arquivo:linha).
---

# 🩺 Skill: Diagnóstico Forense de Sessões Antigravity

Esta skill estabelece o protocolo de auditoria e análise pós-morte (*post-mortem*) para investigar sessões do Antigravity que falharam, travaram em loop, demoraram excessivamente ou consumiram tokens além do esperado.

## 🚀 Quando Ativar
- Quando o usuário perguntar: *"o que deu errado nessa sessão?"*, *"por que demorou tanto?"*, *"por que gastou tantos tokens?"* ou *"o que o agente fez de errado?"*.
- Quando uma tarefa automatizada falhar sem motivo óbvio.
- Para auditar o histórico de uma conversa específica fornecida pelo ID ou caminho da conversa.

---

## 🔍 Regra Central: Evidência com Citação Obrigatória
> **PROIBIDO OPINAR SEM PROVA:** Todo apontamento no relatório de diagnóstico DEVE citar explicitamente o arquivo e a linha ou índice do passo: `transcript.jsonl:linha` (ou `step_index: N`). Conclusões baseadas em memória ou suposição são descartadas.

---

## 📋 Protocolo de Investigação Forense

### Etapa 1: Localização do Arquivo de Transcript
Os logs de execução do Antigravity ficam localizados em:
- **Transcript Compacto:** `C:\Users\<user>\.gemini\antigravity\brain\<conversation-id>\.system_generated\logs\transcript.jsonl`
- **Transcript Completo:** `C:\Users\<user>\.gemini\antigravity\brain\<conversation-id>\.system_generated\logs\transcript_full.jsonl`

Se a sessão a ser auditada for a atual, utilize o ID da sessão corrente. Se for uma sessão passada, inspecione a pasta `brain/` para listar os IDs recentes.

### Etapa 2: Triagem por 5 Dimensões Críticas
Inspecione as linhas do `transcript.jsonl` avaliando:

1. **Loops de Ferramentas / Bate-Rebate:**
   - O agente executou a mesma ferramenta (`run_command`, `replace_file_content`, `view_file`) repetidamente com pequenas variações sem sucesso?
2. **Aderência ao Plano:**
   - O plano inicial previa passos X, Y e Z. O agente desviou para tarefas não solicitadas ("enquanto estou aqui, vou refatorar...")?
3. **Erros Repetidos sem Investigação:**
   - Comandos que retornaram código de erro (`code != 0`), mas o agente tentou novamente sem ler o erro ou sem mudar os parâmetros?
4. **Vazamento / Explosão de Tokens:**
   - Comandos que despejaram milhares de linhas no terminal (ex: `Get-ChildItem -Recurse`, `npm test` verboso) sem paginação ou filtros adequados, estourando a janela de contexto.
5. **Conflito de Subagentes:**
   - Bate-rebate infinito entre subagente implementador e revisor sem encerramento.

---

### Etapa 3: Relatório Estruturado de Diagnóstico

O resultado deve ser apresentado estritamente no seguinte padrão:

```markdown
### 🩺 Relatório Forense da Sessão [<conversation-id>]

#### 1. ⏱️ Linha do Tempo e Resumo dos Fatos
- **Início:** [Timestamp de abertura]
- **Duração Total / Passos:** [Total de steps registrados]
- **Objetivo Declarado pelo Usuário:** [Texto original sanitizado]

#### 2. 🚨 Causa-Raiz Comprovada (com evidência)
- **Fato 1:** [Descrição do desvio ou falha] -> `transcript.jsonl:linha X` (`step_index: Y`)
- **Fato 2:** [Comando com falha ou loop detectado] -> `transcript.jsonl:linha Z`

#### 3. 💥 Impacto Operacional
- **Desperdício de Tokens:** [Ex: despejo massivo de log em terminal, repetição de chamadas]
- **Tempo Perdido:** [Estimativa de passos em falso]

#### 4. 🛠️ Plano de Ação e Prevenção
- [Qual regra, filtro ou restrição impedirá esse erro em sessões futuras]
```

---

## 🚫 Anti-Patterns do Auditor
- **Nunca culpar a ferramenta sem verificar a entrada:** Se o comando falhou por erro de sintaxe do agente, o erro é do agente, não do sistema operacional.
- **Nunca sugerir mais ferramentas como solução:** Se a sessão falhou por excesso de complexidade, a solução é simplificação e checkpoints frequentes (KISS).
