# Contributing to Velunori

Bug reports, documentation improvements, design feedback and focused pull requests are welcome. These guidelines apply across the Velunori organization; a repository's README describes its specific requirements and checks.

## Choose the repository

| Repository | Scope |
| --- | --- |
| [velunori](https://github.com/Velunori/velunori) | Bundle installer, pinned component versions, installation and recovery documentation |
| [core](https://github.com/Velunori/core) | Floating bars, shared design kit, appearance and branding |
| [clock](https://github.com/Velunori/clock) | Calendar, events and Google/iCloud synchronization |
| [control-center](https://github.com/Velunori/control-center) | Audio, displays, network, capture and reminders |
| [notifications](https://github.com/Velunori/notifications) | Notification cards and history |
| [menu](https://github.com/Velunori/menu) | Launcher, command menu and prompts |
| [weather](https://github.com/Velunori/weather) | Cities, current conditions and forecasts |
| [update](https://github.com/Velunori/update) | Update window and progress reporting |
| [lockscreen](https://github.com/Velunori/lockscreen) | Serene lock screen presentation |
| [theme](https://github.com/Velunori/theme) | Palette, wallpaper and window styling |
| [.github](https://github.com/Velunori/.github) | Organization profile, shared templates and community guidelines |

If the component is unclear, use the bundle repository and describe where the problem appears. Search existing issues first. For larger changes or new dependencies, open an issue to discuss the approach before spending substantial effort.

Use the issue forms to include reproduction steps, expected and actual behavior, Omarchy version, component commit and relevant logs. Screenshots help with visual problems. Remove tokens, passwords, calendar contents and other personal information. Report vulnerabilities privately as described in [SECURITY.md](https://github.com/Velunori/.github/blob/main/SECURITY.md).

## Set up a checkout

Fork the repository you intend to change. For a component, clone your fork beside a checkout of `core` so QML's sibling imports work:

```bash
mkdir -p ~/dev/velunori-contributions
cd ~/dev/velunori-contributions
git clone https://github.com/Velunori/core.git
git clone https://github.com/YOUR-USERNAME/clock.git
cd clock
git switch -c fix/calendar-navigation
```

Replace `clock` with your component. If you are changing core, clone your core fork instead. Read the component's README and nearby implementation before editing. Preserve the sibling layout and compatibility with both copied and symlinked installations.

For the bundle, clone your fork with its submodules:

```bash
git clone --recurse-submodules https://github.com/YOUR-USERNAME/velunori.git
cd velunori
git switch -c fix/install-message
```

Submodules are separate repositories, usually checked out at detached commits. Send component changes to the component repository first. A bundle pointer update should reference a commit available in the public upstream component repository; do not point it at a local-only or fork-only commit. Include the reason for each pointer update.

Source checkouts do not require installation on your desktop. Read any installer before running it. Never modify `/usr/share/omarchy/` as part of development, and do not alter live user configuration as a side effect of checks.

## Implementation and design

- Reuse `core/kit`, shared typography, spacing and theme APIs. Keep settings and management flows inside Velunori where supported.
- Bound panels to the monitor, scroll overflowing content and keep essential actions reachable on smaller screens. Support mouse wheels, touchpads, keyboard navigation and normal text editing.
- Keep changes focused and preserve unrelated work. Avoid adding dependencies or refactoring unrelated code without a concrete reason.
- Keep calendar data persistent and notification history session-only. Calendar all-day end dates are exclusive; preserve time zones, recurrence and unrelated remote properties. Retain cached events after failed synchronization and check conflicts before remote writes.
- Connect accounts only through explicit user actions. Never commit credentials or print them in arguments, diagnostics or test output.

## Validate your changes

Run the affected repository's documented checks. Most plugins provide these commands, run from that plugin's directory:

```bash
bash scripts/check.sh
VELUNORI_TEST_LAYOUT=symlink bash scripts/check.sh
```

Core and theme have their own checks; follow their README rather than assuming every option applies. The QML checks require the Qt/Quickshell and Omarchy dependencies listed by each component. Calendar cloud checks use the private environment created by `bash scripts/setup-deps.sh`; use `.venv/bin/python` when running those Python checks directly. Backend tests must use temporary XDG data directories and stand-in accounts so they cannot change a real calendar.

For the bundle, run from its root:

```bash
bash -n scripts/install.sh
python3 -m unittest discover -s tests -v
bash scripts/install.sh --dry-run
```

For documentation-only changes, check links, paths, Markdown and any YAML you edited; a full desktop test is generally unnecessary.

Keep validation safe and report its limits:

- Lock screen tests instantiate only the view in a regular window. Never lock the desktop or invoke real authentication as a test.
- Update tests use the stand-in under `update/tests`; never run a real system update to test the UI.
- Theme checks render and validate in temporary locations; do not apply the theme to the live desktop as a development side effect.
- Automated QML tests do not verify real desktop placement, scrolling, authentication or live cloud synchronization. State which checks ran and which still need desktop verification.
- When investigating host crashes, consult [core's stability notes](https://github.com/Velunori/core/blob/main/docs/stability.md). Do not claim an upstream Qt/Quickshell crash is fixed based on an offscreen smoke test.

## Documentation and previews

Plugin READMEs share this layout: title, one-line summary, `docs/preview.png`, Features, Requirements, Install, Development, Limits, the shared plugin table and License. Keep documentation and previews aligned when behavior or appearance changes.

Generate a preview using the affected plugin's own check and the shared compositor. For example, from the parent directory containing `core` and `clock`:

```bash
VELUNORI_PREVIEW_PATH=/tmp/velunori-clock.png bash clock/scripts/check.sh
bash core/scripts/compose-preview.sh /tmp/velunori-clock.png clock/docs/preview.png
```

Use sample data in screenshots. Do not include account details, private events, notifications or tokens.

## Submit a pull request

Send the PR to the repository's default branch (`main` for most components; check the repository rather than assuming). Explain the problem and the resulting behavior, link an issue if one exists, and list completed checks with their results. Add before/after screenshots for visual changes and mention any remaining live checks or compatibility limitations.

You do not need to open an issue for a small, clear fix. Avoid committing virtual environments, caches, generated user data or unrelated formatting changes. Keep existing license and attribution notices; third-party code and assets need appropriate license information. Contributions are submitted under the affected repository's existing license.

Follow our [Code of Conduct](https://github.com/Velunori/.github/blob/main/CODE_OF_CONDUCT.md). Maintainers may request revisions or decline changes that do not fit the project; no response or release deadline is guaranteed.
