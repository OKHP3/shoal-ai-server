# Fish Guide: Connecting Client Devices

Every device on your network is a fish. The only requirement is a modern web browser. No app installs. No client-side AI software. Just type the reef's URL and start chatting.

## The Universal Pattern

Open any browser on any device and go to:
```
http://[REEF-IP]:3000
```

Replace `[REEF-IP]` with your reef's local IP address (e.g., `192.168.1.50`). Sign in with the account the admin created for you (or sign up if registration is open). That is the entire setup for most devices.

## Platform-Specific Notes

### Windows Laptops and Desktops

Open Chrome, Edge, or Firefox. Navigate to the reef URL. Bookmark it. Done.

**Optional power move:** If you want to run an AI agent framework (like OpenClaw) on this Windows machine that routes to the reef for inference, install WSL2 and configure the agent to point at the reef's Ollama endpoint (`http://[REEF-IP]:11434`). This is the "gateway node" pattern: the Windows machine handles the agent logic (Discord bots, session management, persona files), the reef handles the thinking.

### Mac Laptops and Desktops

Open Safari, Chrome, or Firefox. Navigate to the reef URL. Done.

If the reef is also a Mac (e.g., a Mac Mini), you can install Open WebUI as a PWA from Safari for an app-like experience.

### Chromebooks

Open Chrome. Navigate to the reef URL. Done.

No Crostini or Linux required. The Chromebook's browser is the entire client. This is the lowest-cost fish in the shoal: a $200 Chromebook becomes a full AI workstation when paired with a reef on the network.

### iPads and iPhones

Open Safari. Navigate to the reef URL. Done.

For a native-app feel, use Safari's "Add to Home Screen" to create a PWA icon. Open WebUI's responsive layout works well on tablet and phone screens.

### Android Phones and Tablets

Open Chrome. Navigate to the reef URL. Done.

Same PWA option: Chrome menu, "Add to Home Screen."

### Smart Displays and Kiosks

Any device with a modern browser can theoretically be a fish. A wall-mounted tablet running a kiosk browser pointed at the reef URL becomes a shared office AI terminal.

## Finding Your Reef's IP Address

The reef needs a stable local IP. Options:

1. **Check the reef machine.** On macOS: System Settings, Network. On Linux: `ip addr`. On Windows: `ipconfig`.
2. **Set a static IP or DHCP reservation** in your router so the reef always gets the same address. This prevents the URL from changing after a reboot.
3. **Use a local hostname** if your router supports mDNS. On macOS, the reef is reachable at `[hostname].local` (e.g., `mac-mini.local:3000`).

## Troubleshooting

**"Connection refused" or page won't load:**
- Is Ollama running on the reef? (`curl http://[REEF-IP]:11434/api/tags`)
- Is Open WebUI running? (`curl http://[REEF-IP]:3000`)
- Is the firewall open? (Windows reefs need explicit firewall rules, see [reef-setup.md](reef-setup.md))
- Are both devices on the same network? (Guest Wi-Fi is often isolated)

**Slow responses:**
- Check how many users are active simultaneously
- Consider a larger model or more RAM on the reef
- Set `OLLAMA_NUM_PARALLEL` to match your user count (see [reef-setup.md](reef-setup.md))

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
