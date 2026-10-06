# ==============================================================================
# 🚀 ANTIGRAVITY-SKILL-SUPREME: Script de Setup Automatizado para Windows
# ==============================================================================
# Este script provisiona todo o ambiente de desenvolvimento recomendado via WinGet
# ==============================================================================

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "🛸 Iniciando Provisionamento da Toolchain Antigravity..." -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# Função auxiliar para instalar pacote via winget
function Install-App {
    param (
        [string]$Name,
        [string]$Id
    )
    Write-Host "[*] Verificando instalação de: $Name ($Id)..." -ForegroundColor Yellow
    winget install --id $Id --exact --accept-package-agreements --accept-source-agreements --silent
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[+] $Name instalado ou ja atualizado com sucesso!" -ForegroundColor Green
    } else {
        Write-Host "[-] Aviso ao processar $Name (Codigo: $LASTEXITCODE). Prosseguindo..." -ForegroundColor DarkYellow
    }
}

# 1. Controle de Versão e CLI
Install-App -Name "Git for Windows" -Id "Git.Git"
Install-App -Name "GitHub CLI" -Id "GitHub.cli"

# 2. Runtimes de Desenvolvimento
Install-App -Name "Node.js LTS" -Id "OpenJS.NodeJS.LTS"
Install-App -Name "Python 3.12" -Id "Python.Python.3.12"

# 3. Gerenciador Astral uv (Ultrarrápido)
Write-Host "[*] Instalando Astral uv (Gerenciador ultrarrapido de Python)..." -ForegroundColor Yellow
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 4. Bun Runtime
Write-Host "[*] Instalando Bun Runtime..." -ForegroundColor Yellow
powershell -ExecutionPolicy ByPass -c "irm https://bun.sh/install.ps1 | iex"

# 5. Editores e Segundo Cérebro
Install-App -Name "Visual Studio Code" -Id "Microsoft.VisualStudioCode"
Install-App -Name "Obsidian" -Id "Obsidian.Obsidian"

# 6. Multimídia e IA
Install-App -Name "FFmpeg" -Id "Gyan.FFmpeg"
Install-App -Name "Ollama" -Id "Ollama.Ollama"

# 7. Contêineres
Install-App -Name "Docker Desktop" -Id "Docker.DockerDesktop"

Write-Host "`n==========================================================" -ForegroundColor Cyan
Write-Host "✅ Provisionamento concluido com sucesso!" -ForegroundColor Green
Write-Host "💡 Dica: Reinicie o terminal do PowerShell para recarregar o PATH." -ForegroundColor White
Write-Host "==========================================================" -ForegroundColor Cyan
