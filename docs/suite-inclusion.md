# Propose a plugin for the Velunori suite

A plugin can use Velunori Library without becoming an official suite component. Suite inclusion is a separate maintenance and compatibility decision; a marketplace listing does not automatically include it in the package.

## Start with a proposal

Open a feature request in the `velunori` repository. Describe:

- The user problem, intended workflow and how it differs from existing components.
- Repository, license, maintainer and expected maintenance commitment.
- Plugin kinds and a proposed namespace; use your own namespace until a Velunori ID is agreed.
- Library API/version range, supported Omarchy versions and additional dependencies.
- Services, privileged operations, network providers and credentials involved.
- User-data locations, persistence, migrations and removal behavior.
- How the plugin works without Floating Bars, including unavailable capabilities.
- Sample-data screenshots, completed checks and remaining live validation.

Discuss replacement behavior explicitly. An `omarchy.clonedFrom` declaration can affect routing, restoration and host capabilities; it is not a generic dependency field. Do not claim a built-in identity merely to gain unrelated service access.

## Build a standalone component

Use the [authoring guide](plugin-authoring.md) and shared library. Provide a valid root manifest, license, documented requirements, installer/removal flow and safe automated checks. Ordinary operation must not require the bar plugin.

Show that enabling, disabling, re-enabling, shell restart and removal leave unrelated configuration intact. Account connection must be explicit. Missing external services should produce an understandable state, retain cached data where applicable and avoid repeated requests for credentials.

Keep the README convention: title, one-line summary, `docs/preview.png`, Features, Requirements, Install, Development, Limits, component table and License. Include third-party notices. The maintainer reviews behavior and design, not only manifest validity.

## Review for inclusion

| Review area | Expected evidence |
| --- | --- |
| User value | Focused workflow and a clear fit in the suite |
| Independence | Core-free checks and native operation with stock Omarchy; Floating Bars optional |
| Shared UI | Library components and theme API rather than copied design primitives |
| Host integration | Correct entry points, scoped APIs and justified replacement identity |
| Installation | Explicit dependencies, stable source/data locations and conflict protection |
| Removal | No dangling links, lost unrelated settings or unexpected user-data deletion |
| Updates | Version compatibility, data migrations and recovery limits documented |
| Validation | Automated results, sample previews and separately recorded live checks |
| Maintenance | License, attribution, ownership and a maintainer prepared to handle regressions |

A failed or missing live check must be visible in the review. Mock accounts cannot establish real cloud interoperability, and an offscreen pass cannot establish monitor placement or native authentication behavior.

## Integrate after acceptance

Maintainers agree the component ID, repository ownership, dependency range and release scope. The integration PR then updates the suite catalogue/selection metadata, compatible source pins, dependency resolution, installation/removal handling, documentation, support routing and previews.

A local preview now implements the Guided website flow and shell installer. Its `installer/catalog.json` records component names, native IDs, required commands, placement and replacement behavior; the builder includes matched runtime sources. An accepted component needs coordinated catalogue, builder source, website selection and test updates. This preview is not a published stable extension API. Agree integration with maintainers rather than inventing an unrelated registration file or assuming automatic discovery. In-place upgrades/removal remain a separate implementation task.

A suite release must reference publicly available reviewed commits. It must not remove a library version required by another installed component. Record whether support is experimental or verified; inclusion does not imply compatibility with every Omarchy release.

## After inclusion

Maintain API compatibility or provide a coordinated migration. Keep checks and documentation current, handle reports in the component repository, and announce external service or licensing changes. Deprecation/removal needs a plan for installed users, their data and any remaining dependency consumers.
