# Extending a SHOAL Reef With an Agent Gateway (OpenClaw)

The core SHOAL stack is Ollama plus Open WebUI. Some reefs go further and also run an agent framework like [OpenClaw](https://docs.openclaw.ai) on the same box, so fish devices can reach an agent gateway in addition to a chat UI. That is not part of the documented core stack in this repository, but the pattern shows up often enough to be worth a note here, since it hits the exact same class of problem as the core stack does: a service that defaults to loopback-only and needs to be told to listen on the LAN.

**Confirmed, real-world instance:** [`mac-studio-local-ai-workbench`](https://github.com/OKHP3/mac-studio-local-ai-workbench) documents a live reef running this exact combination (Ollama, Open WebUI, plus OpenClaw's Gateway), and [`infusing-a-soul`](https://github.com/OKHP3/infusing-a-soul) documents a Windows-hosted OpenClaw client meant to consume it. This page is the generic version of what those two repos work through with real IPs, ports, and terminal output. Read those repos for the actual household's current status; read this page for the pattern itself.

## Why this is harder than the core stack

Ollama's fix is one environment variable (`OLLAMA_HOST`) and a service restart — see [reef-setup.md](reef-setup.md). An agent gateway like OpenClaw's usually has no equivalent GUI toggle for its bind address, because the gateway is designed to be reached by its own local Control UI first and by remote clients second, if at all. Finding the setting is a locate-then-fix job, not a single documented command.

## Locate-and-fix playbook

Run this in a real terminal on the reef machine, not through the agent framework's own chat interface (if its model provider is broken, as can happen, its chat-based config tools won't work either — this needs to be terminal-first).

**1. Try the CLI first**, if the framework ships one:

```zsh
openclaw config list
openclaw config get gateway
```

Look for a `host` / `bindHost` / `listen` style key under the gateway section. If the CLI supports `config set`, that is the fast path:

```zsh
openclaw config set gateway.host 0.0.0.0
```

**2. If there's no CLI, or it doesn't expose the setting, find the raw config file.** Agent frameworks in this pattern commonly keep state under a dotfile directory in the user's home (for OpenClaw, that convention is `~/.openclaw/`) or, for Electron-based control apps, under the platform's application-support directory:

```zsh
find ~/.openclaw -maxdepth 4 -type f \( -iname "*.json" -o -iname "*.yaml" -o -iname "*.yml" -o -iname "*.toml" \) 2>/dev/null
find ~/Library/Application\ Support -maxdepth 2 -iname "*openclaw*" 2>/dev/null   # macOS
```

**3. Grep whatever config file that finds, for the bind setting:**

```zsh
grep -in "host\|bind\|listen\|0.0.0.0\|127.0.0.1" <config-file>
```

**4. Confirm how the gateway process is actually managed**, so you know how to restart it once the value changes:

```zsh
ps aux | grep -i <framework-name>
launchctl list | grep -i <framework-name>      # macOS
brew services list | grep -i <framework-name>  # macOS, if installed via Homebrew
```

A gateway that's a child process of the desktop Control app restarts by quitting and reopening that app. A gateway managed as its own service (launchd, systemd, Homebrew services) restarts independently of any GUI.

**5. Edit and restart.** Back up any config file before hand-editing it (`cp config.json config.json.bak`), and prefer a small script over manual editing to avoid corrupting JSON/YAML formatting.

**6. Verify from another device on the network**, not from the reef itself:

```zsh
curl -v --max-time 5 http://<reef-lan-ip>:<gateway-port>
```

Any response — even an error page or a rejected WebSocket upgrade — means the bind address changed. A connection failure (`000`, connection refused) means it's still loopback-only.

## Security note

Once a gateway binds to `0.0.0.0`, it's reachable by anything on the LAN, the same tradeoff [privacy-case.md](privacy-case.md) discusses for Ollama and Open WebUI. Confirm the gateway has its own authentication before opening it up — an agent gateway with tool-execution or file-access capability is a considerably higher-value target than a chat API. Do not port-forward it to the public internet; use [remote-access.md](remote-access.md)'s Tailscale pattern for reaching it from outside the house instead.

## Devices don't pair themselves

Making the gateway reachable is necessary but not sufficient. Fish devices (see [fish-guide.md](fish-guide.md) for the core stack's client-connection pattern) still need to explicitly pair with the agent gateway — that is a separate, deliberate step per device, done after the bind-address fix, and it doesn't happen automatically just because the port is now open.

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
