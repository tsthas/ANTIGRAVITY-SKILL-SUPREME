"""Adaptador MCP stdio para conectar o Google Antigravity ao servidor ai-memory.

Resolve dois problemas do protocolo entre Antigravity e ai-memory (rmcp):
1. O Antigravity envia `{"method": "server/discover"}` antes do `initialize`, o que faz
   o servidor Rust (`rmcp`) abortar a conexao esperando `initialize` como 1a mensagem.
2. Garante o envio de `notifications/initialized` logo apos a resposta do `initialize`,
   caso o cliente envie `tools/list` antes da notificacao.
3. Suporta tanto `mcp-remote` (lendo o Bearer token de `auth-tokens/default` em tempo
   de execucao sem expor segredos no `mcp_config.json`) quanto `ai-memory.exe mcp-bridge`.
"""
import json
import os
import shutil
import subprocess
import sys
import threading

DATA_DIR = os.environ.get(
    "AI_MEMORY_DATA_DIR",
    os.path.join(os.path.expanduser("~"), ".ai-memory"),
)
SERVER_URL = os.environ.get("AI_MEMORY_SERVER_URL", "http://127.0.0.1:49374/mcp")
AI_MEMORY_EXE = os.environ.get(
    "AI_MEMORY_EXE",
    os.path.join(os.path.expanduser("~"), "AppData", "Local", "Programs", "ai-memory", "ai-memory.exe"),
)


def ler_token() -> str:
    caminho = os.path.join(DATA_DIR, "auth-tokens", "default")
    with open(caminho, encoding="utf-8") as f:
        return f.read().strip()


def montar_comando() -> list[str]:
    modo = os.environ.get("AI_MEMORY_AGY_MODE", "bridge").lower()
    npx = shutil.which("npx.cmd") or shutil.which("npx")
    if modo == "mcp-remote" and npx:
        token = ler_token()
        return [
            npx,
            "-y",
            "mcp-remote",
            SERVER_URL,
            "--allow-http",
            "--header",
            f"Authorization: Bearer {token}",
        ]
    return [
        AI_MEMORY_EXE,
        "--data-dir",
        DATA_DIR,
        "mcp-bridge",
        "--no-session-id",
        "--server-url",
        SERVER_URL,
    ]


def main() -> int:
    cmd = montar_comando()
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=sys.stderr,
    )
    assert proc.stdin is not None and proc.stdout is not None

    out_lock = threading.Lock()
    init_req_id = None
    init_respondido = threading.Event()
    notificado_initialized = False

    def escrever_cliente(linha_bytes: bytes) -> None:
        with out_lock:
            sys.stdout.buffer.write(linha_bytes)
            sys.stdout.buffer.flush()

    def bomba_stdout() -> None:
        nonlocal init_req_id
        for linha in proc.stdout:
            try:
                msg = json.loads(linha.decode("utf-8", errors="ignore"))
                if isinstance(msg, dict) and init_req_id is not None and msg.get("id") == init_req_id:
                    escrever_cliente(linha)
                    init_respondido.set()
                    continue
            except Exception:
                pass
            escrever_cliente(linha)

    t = threading.Thread(target=bomba_stdout, daemon=True)
    t.start()

    for linha in sys.stdin.buffer:
        texto = linha.decode("utf-8", errors="ignore").strip()
        if not texto:
            continue
        try:
            msg = json.loads(texto)
        except Exception:
            proc.stdin.write(linha)
            proc.stdin.flush()
            continue

        metodo = msg.get("method") if isinstance(msg, dict) else None

        if metodo == "server/discover":
            resp = {
                "jsonrpc": "2.0",
                "id": msg.get("id"),
                "error": {"code": -32601, "message": "Method not found"},
            }
            escrever_cliente((json.dumps(resp) + "\n").encode("utf-8"))
            continue

        if metodo == "initialize":
            init_req_id = msg.get("id")
            proc.stdin.write(linha)
            proc.stdin.flush()
            init_respondido.wait(timeout=10.0)
            continue

        if metodo == "notifications/initialized":
            if not notificado_initialized:
                notificado_initialized = True
                proc.stdin.write(linha)
                proc.stdin.flush()
            continue

        if init_respondido.is_set() and not notificado_initialized:
            notificado_initialized = True
            notif = b'{"jsonrpc":"2.0","method":"notifications/initialized"}\n'
            proc.stdin.write(notif)
            proc.stdin.flush()

        proc.stdin.write(linha)
        proc.stdin.flush()

    try:
        proc.stdin.close()
    except Exception:
        pass
    return proc.wait()


if __name__ == "__main__":
    sys.exit(main())
