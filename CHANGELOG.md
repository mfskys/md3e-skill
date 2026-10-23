# Changelog

All notable changes to this skill are documented here. The format is based on
[Semantic Versioning](https://semver.org/lang/zh-CN/) and the skill follows the
`MAJOR.MINOR.PATCH` scheme described in `PUBLISH.md`.

## [1.4.0] - 2026-10-23

Source-verified refresh: M3E signatures were checked against the actual `androidx/androidx`
source tree, and the skill gained the "how to actually write it" layer it was missing.

### Added
- `references/m3e-api-signatures.md` — source-verified signatures for 1.5.0-line components:
  `MaterialExpressiveTheme`, 8-size `Shapes`, `MotionScheme`, `Horizontal/VerticalFloatingToolbar`,
  `ButtonGroup`, `ToggleButton`, `SplitButtonLayout`, `ToggleFloatingActionButton`,
  `FloatingActionButtonMenu`, `WideNavigationRail`, `ShortNavigationBar`, `SearchBar`/`SearchBarState`,
  Flexible AppBars, `LoadingIndicator`, wavy progress, `ScrollField`, `MaterialShapes`.
- `references/compose-patterns.md` — 11 verified code patterns (theming, scaffold, adaptive
  navigation, floating toolbar, connected button group, split button, search, loading, lists,
  motion, accessibility) with anti-pattern table.
- `references/official-samples.md` — map of the 49 official `*Samples.kt` files, the six
  `android/compose-samples` apps, Now in Android, Material Catalog and the official docs,
  plus rules for copying from them.
- `references/m3-content/blog/` — 4 M3E / I/O 2026 articles; `references/m3-content/develop/` —
  Compose, MDC-Android, Flutter and Web guides. Mirror is now **263 pages = 249 spec + 14 hub**.
- `references/component-index.md` — component → source file → official sample → spec page, plus URL
  templates and a "which source wins on conflict" table.
- `scripts/install_skill.py` — one-command install for native-skill assistants: allow-list copy,
  refuses to install inside the source tree, supports `--target` / `--assistant` / `--home` /
  `--dry-run` / `--force`, and prints the verification question.

### Fixed
- **`SplitButton` does not exist**: the container is `SplitButtonLayout` + `SplitButtonDefaults.
  LeadingButton` / `TrailingButton`. Corrected in `SKILL.md`, the component catalog, the M3E notes
  (zh + en) and the diff doc.
- **`Shapes` has 8 sizes**, not 5: `largeIncreased` / `extraLargeIncreased` / `extraExtraLarge` were
  missing; `extraLarge` is **28dp** (was documented as 24dp). Synced in `design-tokens.md`,
  `Shape.kt` and the SKILL quick reference.
- **`Typography` has 30 slots** on the 1.5.0 line: the 15 base styles + 15 `*Emphasized` variants.
- **`LoadingIndicator` / `ContainedLoadingIndicator` exist** (`progress: () -> Float`); the
  wavy indicators are named `LinearWavyProgressIndicator` / `CircularWavyProgressIndicator`.
- **`PolygonShape` lives in `androidx.compose.foundation.shape`**, not `material3`;
  `MaterialShapes` only provides 35 `RoundedPolygon` presets + `toShape()` / `toPath()`.
- **`SearchBarState`** transitions are the suspend `animateToExpanded()` / `animateToCollapsed()`;
  there is no `show()` / `hide()` / `isExpanded`.
- Catalog gaps filled: `ShortNavigationBar`, `ScrollField`, `AppBarRow` / `AppBarColumn`,
  `LoadingIndicator`, wavy progress.

### Changed
- Version baseline → **2026-10-23**: `material3` **1.5.0-beta02** (2026-10-21),
  `material3-a2ui` 1.0.0-alpha02; beta02 carries no documented API changes.
- `SKILL.md` workflow is now 8 steps and explicitly says "start from official patterns";
  `official-samples.md` / `compose-patterns.md` / `m3e-api-signatures.md` added to resources.
- `version-baseline.md` gained a "source-verified facts" section; `m3e/compose-api.md` replaced its
  open-verification list with verified results.
- README (en/zh) feature lists and structure trees updated.

### Docs
- `official-samples.md` now records **verified** dependency versions (raw files, 2026-10-23):
  `compose-samples` (Jetchat / Reply / Jetsnack, identical) uses stable BOM **2026.09.00**
  (→ `material3` 1.4.0), Kotlin **2.4.20**, AGP **9.3.1**; Now in Android uses
  `compose-bom-alpha` **2025.09.01**, Kotlin **2.3.0**, AGP **9.3.2**. Consequence documented:
  official samples do **not** exercise the 1.5.0-line Expressive components.
- Installation docs now cover both native-skill assistants (CodeBuddy, Claude Code, any
  Agent-Skills-compatible tool) and rules-based assistants (Cursor, Windsurf, Trae, Cline,
  GitHub Copilot, 通义灵码, 文心快码, CodeGeeX).
- `PUBLISH.md`: release template, tag examples and version policy bumped to **v1.4.0**;
  drive-letter placeholders replaced with `<repo>`; install section generalized.

### Packaging
- `audit_run.py`: knowledge baseline → 2026-10-23; nested Git checkouts are pruned from the
  Markdown scan, so a local source clone never slows the audit.
- `scripts/package_skill.py`: switched to an **allow-list** (`SKILL.md`, `README*`,
  `CHANGELOG.md`, `LICENSE`, `references/`, `assets/`, `scripts/`) — anything else in the working
  tree is ignored by construction.
- Local reference checkouts and scratch dirs stay out of Git through `.git/info/exclude`
  (machine-local, never committed) and out of the archive through the allow-list.

## [1.3.0] - 2026-10-08

Version/dependency refresh to the **2026-10-08** baseline, plus a tooling and consistency pass.

### Changed
- **Version baseline advanced to 2026-10-08**: `material3` **1.5.0-beta01** (2026-10-07 — the 1.5.0
  line left alpha), `compose-bom-alpha` **2026.10.00**, Compose core **1.13.0-beta01**,
  `androidx.compose.material3.adaptive:adaptive` **1.4.0-alpha03**,
  `lifecycle-runtime-compose` **2.12.0-alpha04**, `activity-compose` **1.14.0-alpha03**, and
  Navigation 3 **1.2.0** (now graduated to stable). Stable `material3` remains **1.4.0**; the stable
  BOM remains `2026.09.00`. New artifact noted: `material3-a2ui` 1.0.0-alpha01.
- `references/version-baseline.md` rewritten: refreshed version matrix, BOM coverage re-verified from
  the published POM, and the "alpha-line churn log" is now the **1.5.0-line** churn log including
  **beta01** (PolygonShape in-place transform, `preferredItemWidth`, carousel defaults) and
  **alpha29** (source-breaking `Slider`/`RangeSlider` `onValueChange`).
- Re-dated to 2026-10-08 and re-worded ("alpha line" → "the 1.5.0 line") across `SKILL.md`,
  `README.md`, `README.zh-CN.md`, `references/components-catalog.md`, `references/m3-vs-m3e-diff.md`
  and all `references/m3e/*.md` (+ the `*.en.md` mirrors).
- `references/m3-content/` re-verified against the official `m3.material.io/sitemap.xml`: all 249
  spec pages still resolve and no page was added or removed. The 8 pages whose `lastmod` moved to
  2026-09-16 (`button-groups/*`, `segmented-buttons/*`) were rendered in a real browser and compared
  against the mirror — the content is identical, so no re-fetch was needed.

### Fixed
- **`scripts/generate_theme.py` never actually used HCT**: it imported
  `material_color_utilities.python.scheme.scheme_tonal_spot`, a module path that exists in **no**
  released version, so the "accurate HCT" branch always failed into the HSL fallback. The script now
  auto-detects both API generations — 0.2.x (`theme_from_argb_color` + `Variant` + `Theme.schemes`)
  and legacy 0.1.x (`SchemeTonalSpot` + `MaterialDynamicColors`) — and reproduces Google's M3
  baseline exactly (seed `#6750A4` → `primary = #65558F`). Added `--variant` (`tonalspot` default,
  plus `expressive`, `vibrant`, …) and `--contrast`; `on_background` (absent from the 0.2.x scheme
  object) now falls back to `on_surface`; the HSL fallback is documented as an approximation instead
  of being described as HCT.
- **`scripts/generate_theme.py` seed parsing**: 3-digit shorthand (`#FFF`) produced a fully
  transparent color, and invalid input crashed with a traceback — both now raise a clear error.
- `audit_run.py`: removed the hard-coded release date (`datetime.date(2026,9,22)`), which guaranteed a
  permanent failure — the zip is now compared against the source mtimes. Dropped the implicit PyYAML
  dependency (replaced by a minimal frontmatter parser), removed dead code, replaced brittle
  hard-coded line-number assertions with content assertions, made the zip checks tolerate a leading
  directory, and turned the missing-zip case into a skip instead of a failure. Added cross-document
  checks (stale baseline strings, contradictory line-count claims, m3-content spec/hub split).
  It now also validates agent-skill conformance (`name` hyphen-case, no angle brackets in
  `description`) and the distribution zip layout (single top-level folder, POSIX separators), and
  resolves archive entries regardless of the top-level folder name.

### Packaging
- **Added `scripts/package_skill.py`** — builds `dist/md3e.zip` with a single top-level `md3e/`
  folder and POSIX (`/`) separators, matching the agent-skill distribution format. `PUBLISH.md` now
  uses it instead of `Compress-Archive`.
- **Fixed the release zip**: PowerShell's `Compress-Archive` wrote entries with **backslashes**
  (`references\m3-content\...`) — a ZIP-spec violation that flattens the whole tree into oddly-named
  files when extracted on macOS/Linux — and omitted the required top-level `md3e/` folder.
- `assets/templates/MD3ETheme.kt`: the light branch referenced the built-in
  `expressiveLightColorScheme()` while `Color.kt` (and `generate_theme.py`) provide
  `LightColorScheme`; the template now uses `LightColorScheme` and documents the built-in
  alternative.
- The release zip now ships only what the skill needs at run time: repository-maintenance files
  (`audit_run.py`, `CONTRIBUTING.md`, `PUBLISH.md`, `scripts/package_skill.py`) are excluded;
  `README.md` / `CHANGELOG.md` / `LICENSE` stay for attribution and version history.

### Docs
- Unified the `m3-content` page count at **256 Markdown files = 249 spec pages + 7 hub pages**
  (the repo previously said "249" and "256" in different places).
- Unified `compose-api-full.md` at **~8,000 lines** (measured 7,949); the Chinese README said
  "10000+ 行" and the English structure tree said "10K+ lines".
- Corrected the `m3-content/components/` count to 36 (was 37) and replaced the outdated
  "first release" wording in `PUBLISH.md` with the current `v1.3.0` flow.

### Notes
- The 1.5.0 line is now **beta**, but Google still does not recommend alpha/beta builds for
  production — stable `material3` **1.4.0** remains the production choice.

## [1.2.0] - 2026-09-22

Latest-content refresh from the verified knowledge base (baseline **2026-09-14**).

### Added
- `references/version-baseline.md` — version matrix, feature gates, BOM coverage, alpha-line
  churn log (`material3` 1.5.0-alpha28 / stable 1.4.0; icons, MotionScheme, ColorScheme rules).
- `references/m3e/` — five curated M3E notes (核对 2026-09-14): `design-system.md`,
  `color-typography-shape.md`, `motion-physics.md`, `components.md`, `compose-api.md`,
  plus English mirrors (`*.en.md`) for open-source accessibility.
- SKILL.md workflow step for version pinning; icon guidance (Material Symbols / explicit
  `material-icons-core`).

### Changed
- **`references/m3-content/` fully re-synced**: 249 pages replaced with clean browser-rendered
  Markdown from m3.material.io (front matter `source` / `captured: 2026-09-14`); removed old
  encoding artifacts and TOC noise. Navigation hub pages (`index`, `components`, `styles`, …) kept.
- `m3-vs-m3e-diff.md` — baseline banner; SplitButton / FilledTonalToggleButton / slot SearchBar /
  AppBarWithSearch; experimental-API removal on stable 1.4.0-beta01; alpha churn notes.
- `components-catalog.md` — version-line header; ButtonGroup/SplitButton/SearchBar updates.
- SKILL.md → **1.2.0**; README / README.zh-CN structure and feature lists updated.

### Fixed
- `m3e/compose-api.md` migration note: alpha line **is** covered by `compose-bom-alpha`
  (material3 / adaptive included in BOM POM — was incorrectly marked "not via BOM").

### Notes
- Full M3E still requires the **1.5.0-alpha** line; official warning: alpha/beta BOMs are not
  for production.

## [1.1.0] - 2026-08-03

Maintenance and quality pass to prepare the skill for public release.

### Changed
- **SKILL.md refined** for the official `skill-creator` "Concise is Key" principle: dropped the
  ~23-line `m3-content/` directory tree and ~55 lines of redundant resource summaries from the
  always-loaded context; reduced SKILL.md from 232 to 133 lines (~43% less trigger context).
- **Structured Workflow**: reorganized into a clear 6-step sequence with explicit script invocation
  (Step 2 + "Theme generator" block) and a standard `MaterialExpressiveTheme` scaffold.
- **Unified doc numbers**: `compose-api-full.md` cited as ~8,000 lines (measured 7,949) and
  `m3-content/` as 256 files across README / SKILL.md / PUBLISH.md (previously contradictory).
- **Fixed `assets/templates/` listing**: now correctly lists all 4 files (MD3ETheme / Color / Type /
  Shape) — `Shape.kt` was previously missing.

### Added
- `version: 1.1.0` field in SKILL.md frontmatter.
- `CONTRIBUTING.md`, `CHANGELOG.md`.
- `.gitignore` entries for `dist/`, `*.zip`, `output/`.

## [1.0.0] - 2026-08-03

First public release — Material Design 3 Expressive (MD3E) AI skill for Android
Jetpack Compose. Compatible with CodeBuddy, Cursor, Windsurf, and other assistants
that support the agent skill format.

### Added
- `SKILL.md` entry point: triggers, workflow, quick reference, and design principles.
- `references/compose-api-full.md` — full `androidx.compose.material3` API reference
  (~8,000 lines).
- `references/design-tokens.md` — color roles, type scale, shape scale, motion system.
- `references/components-catalog.md` — every M3/M3E component organized by category.
- `references/m3-vs-m3e-diff.md` — differences, migration guide, I/O 2026 updates.
- `references/expressive-design-tactics.md` — the 7 official M3E design tactics.
- `references/design-research.md` — color science, readability, motion, accessibility.
- `references/m3-content/` — mirror of m3.material.io (256 files).
- `assets/templates/` — ready-to-use `MD3ETheme.kt`, `Color.kt`, `Type.kt`, `Shape.kt`.
- `scripts/generate_theme.py` — seed color → complete Compose theme (HCT, with fallback).
- Bilingual README (`README.md` / `README.zh-CN.md`).
- Apache License 2.0.

[1.0.0]: https://github.com/mfskys/md3e-skill/releases/tag/v1.0.0
