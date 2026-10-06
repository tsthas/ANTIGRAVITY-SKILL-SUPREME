# 📖 REGRA MESTRA: DICIONÁRIO DE TERMOS (GLOSSÁRIO EXECUTIVO E CONFLUENCE)

> **Propósito:** Garantir a democratização e a compreensão universal de todas as documentações técnicas, decisões arquiteturais e operacionais publicadas no Atlassian Confluence, apresentadas para diretoria ou compartilhadas publicamente, assegurando que leitores de diferentes áreas e níveis de senioridade compreendam plenamente os termos, sem ambiguidades.

---

## 📐 1. Diretriz de Escopo Obrigatório vs. Dispensado

### Alvo Obrigatório (Deve Conter Glossário):
* **Todas as documentações destinadas ao Atlassian Confluence** ou relatórios corporativos.
* Documentos formais de Arquitetura e Decisões (`DECISOES.md`, `ARQUITETURA.md`).
* Manuais de Operação e Especificações Técnicas (`TO-SPEC`) voltadas a usuários/humanos.
* Grandes manuais de projetos open source (como este repositório).

### Escopo Dispensado:
* Documentações puramente efêmeras de trabalho interno do agente (notas de scratch, planos atômicos temporários e walkthroughs de hotfixes pontuais).

---

## 📝 2. Estrutura Padrão Obrigatória

Sempre ao final da documentação (última seção), insira obrigatoriamente a tabela:

```markdown
## 📖 Dicionário de Termos (Glossário)

| Termo / Sigla | Definição Clara e Acessível |
| :--- | :--- |
| **[Sigla / Conceito]** | [Explicação sucinta em português, contextualizada para o domínio da aplicação] |
```

---

## 🎯 3. Critérios de Curadoria dos Termos
1. **Acrônimos e Siglas Técnicas:** Devem ser expandidos e explicados (ex: *JWT, SSO, RBAC, API, IdP, RLS, NOPASSWD, DTO, SSRF, IDOR*).
2. **Nomenclaturas de Negócio e Domínio:** Termos específicos do negócio, telecomunicações, logística, afiliados ou automação.
3. **Evitar Termos Triviais:** Não definir termos óbvios de computação básica (como "computador", "arquivo", "internet"), focando estritamente nos conceitos relevantes ao projeto.
