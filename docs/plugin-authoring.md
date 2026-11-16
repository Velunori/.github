# Create a Velunori plugin

Build a useful standalone component first. Using the shared library does not require installing Floating Bars or being accepted into the official suite. Read the [development setup](development.md) for the current library migration status before choosing source revisions.

## Pick the host contract

| Behavior | Manifest kind | Entry point |
| --- | --- | --- |
| Bar item, possibly with a popup | `bar-widget` | `barWidget` |
| Floating panel | `panel` | `panel` |
| On-demand overlay/window | `overlay` | `overlay` |
| Command menu | `menu` | `menu` |
| Headless service | `service` | `service` |
| Complete replacement bar | `bar` | `bar` |

Use only the kinds your component implements. A popup loaded by a bar widget does not automatically require a second `panel` declaration. Share the existing Omarchy shell process; do not launch another Quickshell process during normal plugin use.

Use your own namespaced ID, such as `yourname.hello`. Never use the reserved `omarchy.*` namespace, and do not claim a `velunori.*` ID until maintainers agree ownership. Each native entry point must be a safe relative path in the plugin directory.

## Declare the shared dependency

See the [example manifest](../examples/hello/manifest.json). The library requirement is explicit:

```json
{
  "velunori": {
    "dependencies": {
      "velunori.lib": {
        "apiVersion": 1,
        "minimumVersion": "1.0.0",
        "maximumExclusive": "2.0.0"
      }
    }
  }
}
```

This namespaced metadata is a Velunori contract, not a claim that Omarchy resolves dependencies automatically. The locally prepared shell installer resolves and checks a compatible library before activation; this behavior has not been published as a release yet. Current local installers validate the installed library and the real physical sibling layout. Missing/incompatible dependencies should produce a clear error before desktop configuration changes.

The directory is `lib/`; `velunori.lib` is its identity. Do not create a runtime manifest for the library merely to make it show up in the plugin list.

## Use shared UI

Start from [`examples/hello/Widget.qml`](../examples/hello/Widget.qml), which shows a complete widget and popup. A top-level QML file imports:

```qml
import "../lib/kit" as V

V.Theme { id: theme; bar: root.bar }
```

Use `Theme` tokens, `Panel`, `Button`, `Slider`, `Toggle`, `Surface`, `Choice` and `BrandMark`. Nested component files use `../../lib/kit`. Avoid copying the kit into each plugin, hard-coding replacement palettes, or importing files from `core`/`bar`.

The injected `bar` is Omarchy's scoped facade. Do not assume it is a private bar implementation. Read `bar.velunori` only when present, or let `Theme` handle detached styling/defaults. Library theme support does not require Floating Bars.

For popups, expose `opened`, `open()`, `close()` and `closeForPopoutSwitch()` from the widget. Coordinate with `bar.requestPopout` / `bar.releasePopout`; use `WidgetButton` for host click/tooltip/drag behavior and `PanelKeyCatcher` for Escape/panel navigation. Bound dimensions with the library panel helpers. Scroll overflowing content and keep essential actions reachable. Do not consume editing keys from text inputs as global navigation shortcuts.

## Respect capabilities and optional features

Use only documented injected APIs and scoped service proxies. `DesktopBridge` handles supported nightlight/quiet/idle proxies and reports unavailable operations; it never grants permissions. Do not traverse parent QML objects to reach the host's private shell or another plugin's state.

Some features are specific to Floating Bars: layout previews and its appearance-save callbacks should appear only when that bar supports them. Hiding a bar-specific control is acceptable; requiring Floating Bars to open an unrelated system panel is not.

Only declare `omarchy.clonedFrom` when your plugin genuinely replaces that built-in and its routing/restoration/capability behavior has been reviewed. It must not be used as a generic privilege flag. Lock/PAM authentication stays with Omarchy's unchanged service.

## Backend, accounts and data

Keep persistent user data under the appropriate XDG directory and document ownership, permissions, schema versions, migrations and removal behavior. Temporary/session state belongs in a runtime directory. Notification history and calendar events have different lifetimes; do not apply one retention policy to everything.

Separate presentation from backend operations. Use structured arguments and responses; do not construct shell commands from arbitrary user/provider text. Avoid secrets in command arguments, output or repository fixtures. Establish accounts only from an explicit UI action and use appropriate OAuth/keyring mechanisms; do not ask users to paste tokens into issues.

For editable calendar synchronization, support create/edit/delete in both directions rather than silently substituting a read-only feed. All-day end dates are exclusive. Preserve unrelated remote properties, use conflict checks, handle local time zones, daylight-saving transitions and recurrence, and retain cached events after failure. Distinguish mock-based coverage from actual provider verification.

## Validate before installing

Read the [testing guide](testing.md). From a staged example directory beside `lib`, validate the manifest and QML using the installed host imports:

```bash
omarchy plugin validate .
```

For linting, create temporary import mappings **inside the test harness**, rather than workspace aliases:

```bash
work=$(mktemp -d)
mkdir -p "$work/imports/qs"
ln -s "${OMARCHY_PATH:-/usr/share/omarchy}/shell/Commons" "$work/imports/qs/Commons"
ln -s "${OMARCHY_PATH:-/usr/share/omarchy}/shell/Ui" "$work/imports/qs/Ui"
/usr/lib/qt6/bin/qmllint -I "$work/imports" \
  --unqualified info --missing-property warning --incompatible-type info Widget.qml
rm -rf "$work"
```

These temporary host-import mappings do not install a plugin or create `velunori.core`/`velunori.lib` shortcuts. A production check script should use a cleanup trap, preserve the command's exit status, stage a core-free layout and exercise actual component behavior, not just lint.

Test copied and symlinked consumer layouts, stock Omarchy and Floating Bars compatibility, missing dependencies/capabilities, small windows, keyboard input, and error/recovery behavior. Automated checks use temporary user data and stand-in services. Native lifecycle, placement and account interoperability require separately recorded live checks.

## Try a checked plugin on your desktop

This is a deliberate installation step, not part of automated checks. Use a matched library/plugin revision and preserve your current configuration first. The plugin source must be a Git repository for Omarchy's add command.

From your plugin checkout, with the real library source beside it:

```bash
bash ../lib/scripts/install-local.sh
omarchy plugin add /ABSOLUTE/PATH/TO/YOUR/PLUGIN-GIT-REPOSITORY --enable
omarchy-shell shell summon yourname.hello '{}'
omarchy-shell shell hide yourname.hello
```

Replace the path and plugin ID with your own. If a compatible library is already installed, skip its install command; the current library installer intentionally refuses to overwrite an existing dependency. The add command clones your plugin, so commit the intended test source in your own repository first; uncommitted edits are not included in that clone.

Omarchy's add command does not recursively initialize submodules or install this library for you. Its cloned plugin will import the real sibling installed `lib/` directory. Test the actual click, Escape, lifecycle and display placement before describing them as verified. Disabling/removing the component should preserve the library while other components still use it:

```bash
omarchy plugin disable yourname.hello
omarchy plugin enable yourname.hello
omarchy plugin remove yourname.hello
```

The Hello example has no backend data to erase. A real plugin needs its own documented data-retention and recovery behavior. Do not apply these commands to the local legacy Velunori desktop as a substitute for completing its coordinated library migration.

## Document installation and removal

Specify external tools, library API/range, supported Omarchy versions and every desktop change. Preserve unrelated configuration, reject conflicting paths, and provide meaningful recovery for partial installation. Keep source paths valid after disabling/removing an installer entry. Never silently delete user data or disconnect accounts during removal.

The Guided website selection and shell installer are prepared locally; the in-place upgrade/removal contract is not implemented yet. Do not rely on invented lifecycle hooks or promise that a marketplace update will migrate your backend data. Implement and document the behavior supported by the actual host/package revision.

When ready, use the [suite inclusion process](suite-inclusion.md). A component may remain independently maintained even if it never joins the package.
