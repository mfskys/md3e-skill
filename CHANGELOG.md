# Changelog

All notable changes to this skill are documented here. The format is based on
[Semantic Versioning](https://semver.org/lang/zh-CN/) and the skill follows the
`MAJOR.MINOR.PATCH` scheme described in `PUBLISH.md`.

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
