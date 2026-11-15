# Security policy

## Report privately

Please do not disclose suspected vulnerabilities, exploit details or credentials in public issues or pull requests.

Use **Security → Advisories → Report a vulnerability** in the affected Velunori repository. If you are unsure which component is affected, [report privately to the bundle repository](https://github.com/Velunori/velunori/security/advisories/new).

Include the affected repository and commit or bundle revision, Omarchy version, reproduction steps using test data, expected security boundary and potential impact. A small proof of concept is useful. Never send real passwords, OAuth tokens, app-specific passwords, private calendar data or session credentials.

Examples include credential exposure, unsafe remote event handling, unexpected command execution, and changes that weaken the lock screen or authentication boundary. Ordinary visual, installation and usability bugs belong in public issues once private information has been removed.

## Versions and handling

Velunori is under active development. Fixes target current development versions and updated bundle pins; there is no maintained long-term support branch or guaranteed backport policy. Reports against older pinned versions are still useful: include the exact revision rather than silently changing it before reporting.

Maintainers will assess the report, discuss a fix privately and coordinate disclosure where appropriate. No response deadline, fix deadline or bug bounty is promised. Please allow coordination before publishing details that could put users at risk.

If the cause is in Omarchy, Qt, Quickshell or another dependency, the report may need coordination with that upstream project's security process. Velunori's lock screen intentionally retains Omarchy's session-lock and PAM service; a presentation change must not bypass it.
