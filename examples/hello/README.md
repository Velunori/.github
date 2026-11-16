# Hello Velunori — authoring example

A minimal bar widget and popup built with Library API 1, with no Floating Bars dependency.

Copy `manifest.json` and `Widget.qml` into a **real sibling directory** beside a compatible `lib/` checkout. They are templates, not an installed plugin; imports are relative to that target layout, not this documentation directory. Replace `yourname.hello`, author and repository details before publishing.

```text
workspace/
  lib/
  hello/
    manifest.json
    Widget.qml
```

The example declares a scoped native `bar-widget`, forwards the popup lifecycle, uses shared components, and provides close/Escape/panel navigation. It contains no commands, network access or account integration. It does not register or enable itself.

Validate from `hello/`, using the installed Omarchy imports as described in the [authoring guide](../../docs/plugin-authoring.md#validate-before-installing). A local check has validated the manifest and QML imports/types; native placement and input still need desktop verification. Do not treat this example as a complete production plugin: add license/attribution, requirements, installer/removal documentation, tests and sample-data previews.

The example code is MIT licensed; see [LICENSE](LICENSE).
