# Remote Access: Using Your SHOAL Outside the House

By default, your SHOAL is only accessible on the local network. Tailscale extends access securely to any device, anywhere, without opening ports or configuring your router.

## Why Tailscale

Ollama has no built-in authentication. Exposing port 11434 to the public internet means anyone can query your models. Do not do this.

Tailscale creates a private mesh VPN. Only devices you have enrolled can see the reef. Traffic is encrypted end-to-end. No port forwarding required.

## Setup

1. Create a free Tailscale account at [tailscale.com](https://tailscale.com)
2. Install Tailscale on the reef machine
3. Install Tailscale on each device that needs remote access
4. All enrolled devices get a stable Tailscale IP (e.g., `100.x.y.z`)
5. Access Open WebUI at `http://[TAILSCALE-IP]:3000` from anywhere

Free tier includes up to 100 devices and 3 users, which covers most homes and small offices.

## The Plex Parallel

This is exactly how Plex handles remote media access. Your Plex server sits inside your home network. Plex's relay (or direct connection) lets you watch your movies from a hotel. Tailscale is the SHOAL equivalent: your AI server sits inside your network, Tailscale lets you chat with it from a coffee shop.

## Security Notes

- Tailscale traffic is encrypted (WireGuard under the hood)
- Only devices enrolled in your Tailscale network can reach the reef
- You can revoke device access from the Tailscale admin console
- Consider enabling Tailscale ACLs to restrict which devices can reach which ports

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
