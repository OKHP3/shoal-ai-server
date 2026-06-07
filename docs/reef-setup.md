# Reef Setup: Your Private AI Server

The reef is the machine that runs AI models and serves them to every device on your network. For hardware recommendations, see [builds/](../builds/).

## Prerequisites

- A machine with 16GB+ RAM (see [builds/](../builds/) for options)
- macOS, Linux, or Windows (with WSL2) on the reef machine
- A local network (Wi-Fi or Ethernet) shared by your client devices

## Step 1: Install Ollama

Ollama downloads, runs, and serves AI models over an API.

**macOS / Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows (via WSL2):**
Install WSL2 first (`wsl --install` from PowerShell), then run the Linux install inside the WSL terminal.

Verify: `ollama --version`

## Step 2: Pull a Model

Pick a model that fits your RAM:

| RAM | Recommended Model | Command |
|-----|-------------------|---------|
| 16GB | Llama 3.1 8B | `ollama pull llama3.1:8b` |
| 24-32GB | Gemma 3 12B | `ollama pull gemma3:12b` |
| 64GB+ | Mistral Small 3.1 24B | `ollama pull mistral-small3.1:24b` |

Test locally: `ollama run llama3.1:8b "What is the capital of Texas?"`

## Step 3: Open Ollama to the Network

By default Ollama only listens on localhost. Set the host to `0.0.0.0` to allow LAN access.

**macOS (launchd):**
```bash
launchctl setenv OLLAMA_HOST "0.0.0.0"
```
Restart Ollama (quit from the menu bar and reopen).

**Linux (systemd):**
```bash
sudo systemctl edit ollama
# Add: [Service]
# Environment="OLLAMA_HOST=0.0.0.0"
sudo systemctl daemon-reload && sudo systemctl restart ollama
```

**Verify from another device:**
```bash
curl http://[REEF-IP]:11434/api/tags
```
Replace `[REEF-IP]` with the reef's local IP. You should see JSON listing your models.

## Step 4: Install Open WebUI

Open WebUI gives every person their own account, chat history, and model access through a browser.

**Docker (recommended):**
```bash
docker run -d \
  --name open-webui \
  --restart always \
  -p 3000:8080 \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  -v open-webui:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

On Linux hosts (not Docker Desktop), replace `host.docker.internal` with `172.17.0.1` or the host's LAN IP.

**Without Docker:**
```bash
pip install open-webui
open-webui serve --host 0.0.0.0 --port 3000
```

## Step 5: First Login

From any device on the network, open a browser:
```
http://[REEF-IP]:3000
```

The first person to sign up becomes admin. All subsequent signups default to "pending" until the admin approves them. That is it. Your reef is live.

## Step 6: Concurrency (Optional)

For 2-6 users, enable parallel processing:
```bash
# macOS
launchctl setenv OLLAMA_NUM_PARALLEL "4"
# Linux (in systemd override)
Environment="OLLAMA_NUM_PARALLEL=4"
```

Four concurrent inference slots per loaded model. Each slot uses additional RAM proportional to context length. Queue depth defaults to 512 via `OLLAMA_MAX_QUEUE`.

## Step 7: Firewall (Windows Reef Only)

```powershell
New-NetFirewallRule -DisplayName "Ollama LAN" -Direction Inbound -LocalPort 11434 -Protocol TCP -Action Allow
New-NetFirewallRule -DisplayName "Open WebUI LAN" -Direction Inbound -LocalPort 3000 -Protocol TCP -Action Allow
```

## What's Next

- [Connect client devices](fish-guide.md)
- [Set up users and permissions](multi-user.md)
- [Enable remote access](remote-access.md)

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
