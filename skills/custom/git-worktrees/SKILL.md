---
name: git-worktrees
description: Gerencia isolamento de desenvolvimento através de Git Worktrees em ambiente Windows/PowerShell, executando baseline de testes limpos e garantindo merge e limpeza segura do workspace.
---

# 🌿 Skill: Git Worktrees (Isolamento de Desenvolvimento)

Esta skill estabelece o fluxo de trabalho profissional de isolamento de código em projetos gerenciados pelo Antigravity, evitando modificações diretas no branch de produção/trabalho (`main`/`master`) e prevenindo poluição de repositório.

## 🚀 Quando Ativar
- Ao iniciar uma nova funcionalidade, refatoração de médio/grande porte ou correção de bug complexo.
- Antes de iniciar a execução de um plano de implementação (`TO-SPEC` / `planos_de_implementacao/`).
- Quando for necessário isolar totalmente as alterações sem criar múltiplos clones pesados do repositório.

---

## 📋 Protocolo de 4 Etapas

### Etapa 1: Detecção de Isolamento Existente
Antes de criar qualquer coisa, verifique se a sessão já está em um worktree:

```powershell
$gitDir = git rev-parse --git-dir
$gitCommon = git rev-parse --git-common-dir
```

- **Se `$gitDir -ne $gitCommon`:** O workspace atual já é um worktree isolado. **Não crie outro worktree.** Pule diretamente para a Etapa 3 (Baseline de Testes).
- **Se `$gitDir -eq $gitCommon`:** Você está no repositório base. Prossiga para a Etapa 2.

---

### Etapa 2: Criação Segura do Worktree

1. **Verificação Obrigatória do `.gitignore`:**
   O diretório `.worktrees/` DEVE estar listado no `.gitignore` para evitar comitar recursivamente a pasta do worktree:
   ```powershell
   git check-ignore -q .worktrees
   if ($LASTEXITCODE -ne 0) {
       Add-Content -Path .gitignore -Value "`n.worktrees/`nworktrees/"
       git add .gitignore
       git commit -m "chore: ignorar diretorio de worktrees no git"
   }
   ```

2. **Criação do Branch e do Diretório:**
   ```powershell
   $branchName = "feature/nome-da-tarefa"
   git worktree add ".worktrees/$branchName" -b "$branchName"
   ```

3. **Contexto de Operação:**
   Todas as ferramentas de edição e comandos do Antigravity para esta tarefa devem operar a partir do caminho `.worktrees/$branchName`.

---

### Etapa 3: Baseline Limpo de Testes (Clean Baseline)
Antes de escrever uma única linha de código na nova feature, execute os testes existentes do projeto:

```powershell
# Executar comando conforme o ecossistema:
npm test          # Node.js / TypeScript
pytest            # Python
cargo test        # Rust
go test ./...     # Go
```

- **Se houver falha no baseline:** PARE imediatamente e avise o usuário: *"Os testes existentes já estão falhando antes do início da tarefa. Deseja investigar ou prosseguir assim mesmo?"*
- **Se o baseline estiver verde:** Registre que o baseline é limpo e prossiga para a implementação com TDD.

---

### Etapa 4: Finalização e Encerramento Seguro

Quando a implementação estiver 100% concluída e **todos os testes estiverem passando no worktree**, apresente exatamente este menu ao usuário:

```markdown
### 🏁 Implementação Concluída com Sucesso!
Todos os testes foram validados e estão verdes. Como deseja prosseguir?

1. **Merge Local no branch base:** Executa o merge no branch principal, revalida testes e limpa o worktree.
2. **Push e Pull Request:** Sobe o branch para o repositório remoto e preserva o worktree para revisão.
3. **Manter como está:** Preserva o branch e o worktree para validação manual.
```

#### Execução da Escolha:

- **Opção 1 (Merge Local):**
  1. Retorne ao diretório raiz do repositório principal.
  2. Atualize o branch base (`git checkout main; git pull`).
  3. Execute o merge (`git merge feature/nome-da-tarefa`).
  4. Rode a suíte de testes no branch mesclado.
  5. Remova o worktree: `git worktree remove .worktrees/feature/nome-da-tarefa`.
  6. Remova o branch local já mesclado: `git branch -d feature/nome-da-tarefa`.

- **Opção 2 (Push & PR):**
  1. Execute `git push -u origin feature/nome-da-tarefa`.
  2. Mantenha o worktree ativo até a aprovação e conclusão do PR.

- **Opção de Descarte (Discard):**
  - **Atenção:** Só execute o descarte forçado se o usuário pedir explicitamente digitando a palavra de segurança **`discard`**.
  - Remova o worktree com `git worktree remove --force` e delete o branch.

---

## 🚫 Regras Anti-Falha (Red Flags)
- **Proibido comitar sem verificar o `.gitignore`:** Nunca crie um worktree sem garantir que `.worktrees/` está ignorado.
- **Proibido assumir que o baseline estava quebrado:** Se o teste falhou depois da sua edição, o bug foi introduzido por você, a menos que o baseline inicial já estivesse falho.
- **Proibido deletar branch com arquivos não salvos:** Nunca use `--force` em remoção de worktree a menos que o usuário tenha confirmado o descarte.
