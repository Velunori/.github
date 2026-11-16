# Contributing to Velunori

Help improve existing components, documentation and accessibility, or build a new plugin that works on its own and can be proposed for the Velunori suite.

## Start here

- [Development setup and architecture](https://github.com/Velunori/.github/blob/main/docs/development.md)
- [Create a plugin with Velunori Library](https://github.com/Velunori/.github/blob/main/docs/plugin-authoring.md)
- [Propose a plugin for the suite](https://github.com/Velunori/.github/blob/main/docs/suite-inclusion.md)
- [Testing and review](https://github.com/Velunori/.github/blob/main/docs/testing.md)
- [Working example: Hello](https://github.com/Velunori/.github/blob/main/examples/hello/README.md)

**Architecture:** shared UI lives in `lib` (`velunori.lib`, API 1). Floating Bars is the optional `bar` plugin (`velunori.bar`); every feature plugin also works on the stock Omarchy bar. See [development setup and architecture](https://github.com/Velunori/.github/blob/main/docs/development.md).

## Where to contribute

| Repository | Responsibility |
| --- | --- |
| `velunori` | Suite composition, pinned versions, guided installer and recovery |
| `lib` | Shared QML controls, tokens, assets, geometry and scoped host adapters |
| `bar` | Optional Island/Orbit Floating Bars, workspace rendering and bar appearance |
| `clock` | Clock, editable calendars and Google/iCloud synchronization |
| `control-center` | Audio, displays, network, capture and reminders |
| `notifications` | Notification cards and history |
| `menu` | Command menu, launcher and prompts |
| `weather` | Cities and forecasts |
| `update` | Presentation for Omarchy's updater |
| `lockscreen` | Serene presentation; Omarchy owns lock/PAM authentication |
| `theme` | Standalone palette, wallpaper and window styling |
| `.github` | Shared contributor docs, issue forms and community policies |

A new plugin may begin in your own repository and namespace; discuss its ownership before proposing it under `Velunori`.

## Report a problem or suggest a change

Search existing issues. Include reproduction steps, expected/actual behavior, Omarchy and component versions, and relevant sanitized diagnostics. Component problems belong in that component's repository; suite installation and dependency problems belong in `velunori`. For a larger feature or new dependency, discuss its purpose and approach before substantial implementation. Small, clear fixes do not require a preliminary issue.

Remove account details, tokens, passwords, private calendar events and notification contents. Suspected vulnerabilities belong in [private security reporting](https://github.com/Velunori/.github/blob/main/SECURITY.md), not a public issue.

## Make a focused change

Fork the repository, work on a branch, and read its README, checks and nearby implementation. Keep unrelated work intact. Reuse the shared library; feature plugins must not depend on Floating Bars for ordinary operation. Changes to the library API require compatibility notes and consumer checks.

Keep panels bounded to the monitor, scroll overflow, retain essential actions and support keyboard, wheel and touchpad input. Text fields must receive normal editing keys. Settings and account-management flows should stay in the plugin where supported.

Calendar all-day end dates are exclusive; preserve time zones, recurrence, unrelated remote properties and cached events after failed synchronization. Editable cloud calendars need bidirectional create/edit/delete support.

Keep credentials out of repositories, arguments and logs. Connect accounts only through explicit user actions. Persistent user data needs a documented location, permissions, migration and removal policy; notification history has a session-only lifetime.

## Submit a pull request

Use the repository's default branch; do not assume its name. Describe the concrete problem and resulting behavior, link relevant issues, and list checks actually completed. Provide sample-data previews for visual changes. State remaining live checks, supported environments and known limitations honestly.

Follow the [testing guide](https://github.com/Velunori/.github/blob/main/docs/testing.md). Keep READMEs, dependency metadata and previews in step with the code. Preserve licenses and third-party notices, and do not commit virtual environments, caches, credentials or user data. Contributions use the affected repository's license.

Follow the [Code of Conduct](https://github.com/Velunori/.github/blob/main/CODE_OF_CONDUCT.md). Maintainers may request revisions or decline work outside the project scope; a proposal does not guarantee acceptance or a release date. For general help, read [SUPPORT.md](https://github.com/Velunori/.github/blob/main/SUPPORT.md).
