# Velunori

A complete desktop suite for **Omarchy**, with floating bars, coordinated panels and a graphite, lavender and mint palette.

![Velunori appearance settings and floating bar layouts](https://raw.githubusercontent.com/Velunori/velunori/main/docs/preview.png)

### Start here

**[Install the full Velunori suite →](https://github.com/Velunori/velunori#install-the-whole-suite)**

The main repository brings together all nine components, an installation script, requirements, update instructions and recovery steps.

```bash
git clone --recurse-submodules https://github.com/Velunori/velunori.git ~/dev/velunori
cd ~/dev/velunori
bash scripts/install.sh --dry-run
bash scripts/install.sh
```

Run from an unlocked Omarchy desktop terminal, without `sudo`. Installation replaces the corresponding shell components, restarts the shell and applies the theme. Read the [requirements and options](https://github.com/Velunori/velunori#install-the-whole-suite) first; you can keep your current theme or lock screen. Keep the checkout in place: installed plugins link to it.

### The suite

| Repository | What it provides |
| --- | --- |
| **[velunori](https://github.com/Velunori/velunori)** | **Start here: full installation, updates and recovery** |
| [core](https://github.com/Velunori/core) | Island and Orbit bars, appearance settings and the shared design kit |
| [clock](https://github.com/Velunori/clock) | Clock, calendar and local/Google/iCloud events |
| [control-center](https://github.com/Velunori/control-center) | Sound, displays, network, capture and reminders |
| [notifications](https://github.com/Velunori/notifications) | Notification cards and session history |
| [menu](https://github.com/Velunori/menu) | Two-pane Omarchy menu and prompts |
| [weather](https://github.com/Velunori/weather) | Saved cities and a weekly forecast |
| [update](https://github.com/Velunori/update) | A window for Omarchy's system updater |
| [lockscreen](https://github.com/Velunori/lockscreen) | Serene lock screen using Omarchy's lock service |
| [theme](https://github.com/Velunori/theme) | Palette, Dusk wallpaper and window styling |

### Contribute

Report installation issues in [velunori](https://github.com/Velunori/velunori/issues), or open an issue or pull request in the relevant component repository. Each component documents its development checks and current limitations.
