# Development setup and architecture

## Choose compatible sources

Pick any permanent parent directory. No particular `~/dev` path is required. Clone the library beside your plugin. Use a library release compatible with the plugin's declared API range:

```bash
git clone https://github.com/Velunori/lib.git lib
git clone 'YOUR_PLUGIN_FORK_URL' my-plugin
cd my-plugin
git switch -c feature/my-change
```

The intended layout uses real directories:

```text
workspace/
  lib/
    library.json
    kit/
    components/
    design/
    assets/
  my-plugin/
    manifest.json
    Widget.qml
    scripts/
    tests/
```

A top-level plugin imports `../lib/kit`; a file in `components/` imports `../../lib/kit`. The library's metadata identifies `velunori.lib`; that identifier is not a folder alias and must not be treated as a runtime plugin. Do not create `velunori.core` or `velunori.lib` workspace shortcuts to make mismatched sources appear compatible.

You can start a new plugin by copying the files from [`examples/hello`](../examples/hello/README.md) into a real sibling directory beside `lib`. Replace its example namespace before publishing. The example does not install or enable anything merely by being copied.

## Ownership boundaries

| Layer | Owns | Must not do |
| --- | --- | --- |
| Shared library | Reusable controls, palette, branding, panel geometry, scoped adapters | Activate a bar, connect accounts, own authentication or bypass host permissions |
| Floating Bars | Island/Orbit layout and its own appearance controls | Become a mandatory dependency for unrelated feature plugins |
| Feature plugin | Its widget, panels, backend and user data | Reach into another plugin's private objects or silently switch the user's bar |
| Suite installer | Selection, dependency resolution, compatible revisions, install/update/removal plan | Remove dependencies still required by installed components or claim unsupported upgrades |
| Omarchy host | Discovery, scoped APIs, panel lifecycle and trusted services | Be patched under `/usr/share/omarchy` by a plugin's developer checks |

A plugin must operate on the stock Omarchy bar when Floating Bars is absent. Bar-specific controls may be unavailable, but the plugin must keep its ordinary features working and explain missing host capabilities. The theme is independent of the QML library.

## Develop without changing the desktop

Read and run repository checks before installation. Source development must not write live configuration, apply a theme, lock a session, perform authentication or invoke a real system update. Keep backend fixtures in temporary XDG directories. Never modify packaged files under `/usr/share/omarchy/`.

The library check is read-only:

```bash
bash ../lib/scripts/check-install.sh
```

Consumer checks may accept an explicit path:

```bash
VELUNORI_LIB_PATH=/absolute/path/to/lib bash scripts/check.sh
```

This override is for the check harness; it does not change runtime imports. A harness can stage a real sibling library in a temporary directory. Do not conceal missing source layout with an alias.

Installing the library copies it into `${XDG_CONFIG_HOME:-$HOME/.config}/omarchy/plugins/lib`; it has no plugin manifest, so no bar or runtime service is activated. Consumer installers validate both the installed dependency and the physical source layout. Symlinked consumer installations resolve imports beside their physical source checkout; copied installations resolve them beside the installed plugin. Both must be tested, without requiring manifest-ID aliases.

## Suite and submodules

The [`velunori`](https://github.com/Velunori/velunori) repository composes the suite. It pins `lib`, `bar`, every feature component and the theme as Git submodules, and builds the self-contained installer published on the website from exactly those pins.

Make a component PR in that component's repository first. A later bundle pointer must reference a reviewed commit available in the upstream component repository, not a local-only or fork-only commit. Rebuild the installer after updating pins and keep the website download in step.

The installer supports full-suite or per-component selection, resolves the library dependency automatically and offers `plan`, `check`, `install` and `status` actions. Managed in-place upgrades and selection-aware removal are not implemented yet.
