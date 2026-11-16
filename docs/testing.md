# Testing and review

Run the affected repository's checks and report their actual scope. A passing manifest is not a functional test, and an offscreen render is not proof of native desktop compatibility.

## Library and consumers

From a normal sibling workspace:

```bash
bash lib/scripts/check.sh
bash control-center/scripts/check.sh
VELUNORI_TEST_LAYOUT=symlink bash control-center/scripts/check.sh
```

Replace Control Center with your component. Use `VELUNORI_LIB_PATH` for a check harness sourcing the library from elsewhere. The harness must stage the real relative runtime layout; an environment override does not rewrite QML imports.

Test consumers with only the library and host imports present, without a `core` or `bar` checkout in the staged tree. Include the stock host facade and unavailable capabilities. Verify both copied installation paths and physically resolved symlinked sources. Do not add workspace shortcuts to make tests pass.

Library API changes need tests of existing consumers and backward compatibility. New components need meaningful behavior checks: popup lifecycle, keyboard/input, bounded placement geometry, state transitions, error paths and data handling. Avoid tests that merely repeat implementation constants.

## Backend isolation

Use temporary `XDG_DATA_HOME`, `XDG_CONFIG_HOME`, `XDG_STATE_HOME`, `XDG_CACHE_HOME` and/or `XDG_RUNTIME_DIR` as appropriate. Test data must not replace the developer's real calendars, notifications or credentials. Mock external commands/providers and keep fixtures free of personal data.

Calendar cloud dependencies belong in the private virtual environment. Use its Python for dependency-dependent checks and report any skipped tests. Do not install system packages as an incidental test step.

## Operations that tests must not perform

| Component | Safe validation |
| --- | --- |
| Lockscreen | Instantiate the presentation in a regular window; never lock the desktop or invoke real PAM/authentication |
| Update | Drive the stand-in under `tests`; never run a real Omarchy system update |
| Theme | Render templates and validate files in temporary locations; do not apply the live theme |
| Cloud/calendar | Use temporary data and stand-in accounts; live account connection is a separate explicit action |
| Library | Verify no bar activation, no shell-config changes and no workspace alias creation |

Do not restart the live shell as part of documentation checks. In particular, the local older sources still reference the now-removed core alias; complete their coordinated migration before treating a restart as a valid test of the new library layout.

## Previews

From the sibling workspace:

```bash
VELUNORI_PREVIEW_PATH=/tmp/velunori-component.png bash my-plugin/scripts/check.sh
bash lib/scripts/compose-preview.sh /tmp/velunori-component.png my-plugin/docs/preview.png
```

Use the component's own rendered sample data and shared compositor, not private desktop/account captures. Keep `docs/preview.png` and the README current when behavior or appearance changes.

## Live validation and reporting

After source/dependency versions are matched and deliberate installation is authorized, verify native click/IPC open/close, Escape, disable/re-enable, restart and removal. Cover actual monitor sizes/scales, wheel/touchpad scrolling, keyboard focus and normal text editing. Record the exact environment and commits.

State explicitly which of these are complete. Mocked provider calls do not establish live cloud synchronization; offscreen panels do not establish monitor anchoring; finite smoke tests do not establish that a timing-dependent Qt/Quickshell host crash is fixed. Preserve the relevant stability investigation and avoid claiming an upstream fix without evidence.

For documentation changes, validate local links/anchors, parse JSON/YAML examples, and lint any executable snippets/examples. There is no need to run the entire desktop suite for prose changes.
