# 🏛️ REGRA MESTRA: PROTOCOLO VIBE ARCHITECT & SABATINA SOCRÁTICA

> **Propósito:** Garantir assertividade máxima logo no primeiro disparo de desenvolvimento, eliminando o desperdício massivo de tokens com adivinhações, premissas implícitas e implementações precipitadas.

---

## 🚫 1. Proibição Expressa de Código Prematuro
O agente está **expressamente proibido** de gerar código ou criar arquivos de implementação diante de um pedido aberto, novo recurso ou refatoração estrutural sem antes cumprir as etapas de **Clarificação de Intenção (Sabatina Socrática)** e **Plano Aprovado pelo Usuário**.

---

## 🔍 2. Protocolo Socrático de Abertura (Clarify Intent First)
Ao receber uma solicitação aberta ou projeto novo, o agente deve conduzir uma rodada de **3 a 4 perguntas objetivas e pontuais** para travar os seguintes eixos:

1. **O que é "Pronto" (Definition of Done):** Qual o comportamento observável, mensurável e testável que encerra a tarefa com sucesso incontestável?
2. **Fronteira Rígida de Escopo:** O que está explicitamente DENTRO e o que está explicitamente FORA de escopo neste momento?
3. **Restrições Ocultas:** Dependências existentes que não podem ser alteradas, requisitos de performance, limitações de rede ou restrições de compatibilidade.
4. **Trade-offs Técnicos:** Se o pedido admitir mais de uma abordagem razoável, apresentar as opções lado a lado com prós, contras e impactos arquiteturais em vez de assumir uma decisão silenciosa.

---

## 🌊 3. Decomposição em Ondas Paralelas (Parallel Waves)
Planos de execução devem ser fatiados em tarefas atômicas e ordenadas rigorosamente por dependência, respeitando princípios inegociáveis:

* **Zero Dependência na Mesma Onda:** Tarefas pertencentes à mesma onda de execução não podem depender de artefatos umas das outras.
* **Zero Sobreposição de Arquivos:** Nenhuma tarefa simultânea da mesma onda pode editar o mesmo arquivo de código.
* **Critério de Verificação Executável:** Todo ticket deve conter um comando de teste unitário, checagem de tipos ou saída mensurável obrigatória antes de ser considerado concluído.

```mermaid
flowchart TD
    subgraph Wave1["Onda 1: Contratos e Schemas"]
        T1["Tarefa 1.1: Schemas Zod / DTOs"]
        T2["Tarefa 1.2: Mock / Fixtures de Teste"]
    end
    subgraph Wave2["Onda 2: Implementação Isolada"]
        T3["Tarefa 2.1: Lógica de Backend / API"]
        T4["Tarefa 2.2: Componente de Interface"]
    end
    subgraph Wave3["Onda 3: Integração & Quality Gate"]
        T5["Tarefa 3.1: Teste E2E e Auditoria Final"]
    end
    Wave1 --> Wave2 --> Wave3
```

---

## ⚡ 4. Governança de Subagentes: Ledger & Circuit Breaker
Em execuções coordenadas com subagentes (`invoke_subagent` com `self`, `code-reviewer`, `security-auditor`):

1. **Ledger Persistente em Disco:** Toda evolução das tarefas deve ser registrada de forma incremental em `DOCUMENTACOES/planos_de_implementacao/LEDGER_[PROJETO].md`. O ledger é a fonte imutável da verdade e sobrevive a compactações de contexto (*context compaction*). A cada tarefa concluída ou rodada de revisão, registre commits, pendências e decisões.
2. **Circuit Breaker (Teto Rígido de 5 Rodadas):** Em ciclos de *implementação $\longleftrightarrow$ revisão de código*, o teto máximo absoluto é de **5 rodadas**. Se o revisor e o implementador não convergirem na 5ª rodada, interrompa imediatamente o loop. O orquestrador assume a arbitragem técnica formal (**Ruling:**), documenta o trade-off e o débito técnico assumido no Ledger, e prossegue com a entrega. **Proibido loop infinito de bate-rebate.**

---

## 🛑 5. Heurística de Depuração: "Pare no 3º Patch"
Durante a correção de bugs ou incidentes:

* **Limite de 3 Tentativas:** Se foram aplicados 3 patches sucessivos e o problema persistir (ou cada correção revelar um sintoma novo em outro componente), **interrompa imediatamente a implementação**.
* **Diagnóstico Arquitetural:** Isso não é falha de código pontual, é indicativo claro de defeito de arquitetura ou acoplamento indevido. O agente está terminantemente proibido de tentar um 4º patch silencioso. Deve parar, expor o problema de arquitetura ao usuário e propor uma refatoração estrutural fundamentada.

---

## 🦥 6. Postura Técnica (Ponytail + Caveman)
* **Princípio Ponytail (Engenheiro Sênior Pragmático):** Escolher sempre a solução mais simples que resolve o problema de verdade no mundo real. Não inventar abstrações precoces, microsserviços desnecessários ou complexidade acidental.
* **Princípio Caveman (Comunicação Direta e Cirúrgica):** Respostas sem introduções vazias, adulações ("Com certeza! Vou te ajudar agora!") ou desculpas repetitivas. Clareza, brevidade e precisão cirúrgica de engenharia.
