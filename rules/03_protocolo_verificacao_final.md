# 🛡️ REGRA MESTRA: PROTOCOLO DE VERIFICAÇÃO FINAL (QUALITY GATE)

> **Propósito:** Definir o padrão inegociável de auditoria pré-merge e encerramento de tarefas, garantindo que nenhum código entre em produção sem validação sob 4 eixos rigorosos de engenharia.

---

## 🎯 Gatilhos em Linguagem Natural
Sempre que o usuário enviar comandos curtos ou similares a:
* **"faz a verificação final"** / **"faz a verificacao final"**
* **"verifica pra mim se está tudo bem"** / **"verifica se tá tudo certo"**
* **"audita esse projeto"** / **"audita esse código"**
* **"/verificar"** ou **"/review"**

O agente deve **imediatamente** ativar o **Protocolo de Auditoria Final de Engenharia**, baseado nas skills de produção de Addy Osmani (`agent-skills`).

---

## 🔍 Os 4 Eixos Obrigatórios da Verificação

O agente deve auditar o código recente/projeto sob 4 pilares rigorosos:

### 1. Qualidade & Arquitetura (`code-review-and-quality`)
* Aderência a princípios SOLID, coesão modular e baixo acoplamento.
* Tratamento adequado de erros e exceções (sem blocos silenciosos como `except: pass` ou `catch (e) {}`).
* Tipagem determinística e clara (TypeScript estrito ou tipagem estrita com Pydantic v2).

### 2. Segurança & DevSecOps (`security-and-hardening`)
* Checagem ativa dos 7 pilares defensivos: zero segredos hardcoded (.env devidamente sanitizado).
* Ausência de vulnerabilidades do OWASP Top 10 (injeção SQL, command injection, IDOR, XSS, SSRF).
* Validação estrita de entradas externas e ausência de funções perigosas como `eval()`.

### 3. Simplicidade & Código Limpo (`code-simplification`)
* **Cerca de Chesterton (*Chesterton's Fence*):** não alterar, contornar ou remover código existente sem antes compreender o motivo original pelo qual ele foi colocado lá.
* Remoção de código morto, imports não utilizados ou trechos redundantes (código zumbi).
* Eliminação de *overengineering* prematuro (aplicação estrita dos princípios KISS e YAGNI).

### 4. Critério de Conclusão Real (`definition-of-done`)
* Não aceitar suposições do tipo *"parece que funciona"*; exigir evidência factual de teste automatizado executado, compilação bem-sucedida ou verificação de integridade comprovada no terminal.

---

## 📋 Formato Obrigatório do Relatório de Retorno

O relatório de verificação deve ser apresentado em **Português do Brasil (pt-BR)** seguindo rigorosamente a estrutura:

```markdown
### 🛡️ Relatório de Verificação Final (Quality Gate)

#### 1. 🟢 O que está aprovado
- [Lista de componentes e fluxos testados com sucesso e em conformidade]

#### 2. ⚠️ Apontamentos de Atenção e Melhorias
- **[Crítico / Segurança]:** [Riscos de quebra, vazamento de chaves ou vulnerabilidade]
- **[Qualidade / Manutenibilidade]:** [Sugestões pontuais de desacoplamento ou legibilidade]
- **[Opcional / Polimento]:** [Ajustes cosméticos, tipagem extra ou micro-otimizações]

#### 3. 🚀 Veredito Final
- **[APROVADO]** | **[APROVADO COM RESSALVAS]** | **[BLOQUEADO - NECESSITA AJUSTES]**
```
