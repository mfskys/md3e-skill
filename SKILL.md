---
name: md3e
version: 1.4.0
description: "Material Design 3 Expressive (MD3E) design system skill for Android Jetpack Compose. This skill should be used when building Android UI with Material 3 / Material 3 Expressive design language, including theming (color schemes, typography, shapes, motion), component implementation (buttons, cards, navigation, FAB, floating toolbar, button group, etc.), and design guidance (when to use which component, M3 vs M3E differences, expressive design principles). Covers both MD3E (the evolution released 2025, targeting Android 16) and baseline M3 (many components only have M3 specs). Knowledge baseline 2026-10-23: material3 1.5.0-beta02 / stable 1.4.0. Triggers on requests like Material 3 Expressive, MD3E, Material Design 3, M3 theme, MaterialExpressiveTheme, Compose Material 3 component, or when designing/building Android UI that should follow Google Material design guidelines."
---

# Material Design 3 Expressive (MD3E) Skill

## Overview

Comprehensive knowledge of Google's Material Design 3 Expressive (MD3E) design system and its
implementation in Android Jetpack Compose (`androidx.compose.material3`). MD3E is the 2025 evolution
of M3, with research-backed updates to theming, components, motion, typography, and shapes. It targets
Android 16 but is available via the Compose Material 3 library (1.5.0-alpha+) for lower API levels.

**Knowledge baseline: 2026-10-23.** Recommended dependency for full M3E:
`androidx.compose.material3:material3:1.5.0-beta02` (2026-10-21; use the matching
`compose-bom-alpha`). Stable **1.4.0** provides M3 + `MotionScheme` + partial Expressive only — since
**1.4.0-beta01** the stable line removed public `ExperimentalMaterial3ExpressiveApi` APIs. The 1.5.0
line **entered beta on 2026-10-07**, so the Expressive APIs are stabilizing; Google still does not
recommend alpha/beta builds for production.

**Source of truth:** signatures in this skill were re-verified against the `androidx/androidx`
source tree on 2026-10-23. Where docs and source disagree, the source wins (see
`references/m3e-api-signatures.md`).

**M3 vs M3E:** MD3E is an *expansion* of M3, not a replacement. Many components still only have M3
specs. Prefer MD3E APIs where available; fall back to M3 for components not yet updated.

## When to Use This Skill

- Building Android UI with Jetpack Compose that should follow Material design guidelines
- Setting up Material theming (color scheme, typography, shapes, motion scheme)
- Implementing or customizing Material components (buttons, cards, navigation, FAB, etc.)
- Migrating from M2→M3 or M3→M3E (`MaterialExpressiveTheme`)
- Answering questions about Material 3 / M3E specs (color roles, type scale, shape scale)
- Designing expressive UI with new MD3E components (FloatingToolbar, ButtonGroup, WideNavigationRail, etc.)
- Reviewing UI for Material design compliance
- Checking version gates / 1.5.0-line API churn (SplitButton, SearchBar, renames)

## Quick Reference: Key MD3E APIs

| Category | M3 (baseline) | MD3E (expressive) |
|----------|---------------|-------------------|
| Theme | `MaterialTheme` | `MaterialExpressiveTheme` |
| Color scheme | `lightColorScheme()` / `darkColorScheme()` | `expressiveLightColorScheme()` |
| Motion | (easing + duration tokens) | `MotionScheme.standard()` / `MotionScheme.expressive()` |
| Shapes | `Shapes(extraSmall…extraLarge)` (5 sizes) | 8 sizes: + `largeIncreased`, `extraLargeIncreased`, `extraExtraLarge` |
| Experimental opt-in | `@ExperimentalMaterial3Api` | `@ExperimentalMaterial3ExpressiveApi` |

### MD3E-Only Components (version gates: see `references/version-baseline.md`)

On the **1.5.0** line (full set); several graduated non-experimental:

- `HorizontalFloatingToolbar` / `VerticalFloatingToolbar` — floating contextual toolbars, with
  `AppBarRow` / `AppBarColumn` overflow containers
- `ButtonGroup` — connected button row with overflow menu (`ButtonGroupScope` is a sealed interface)
- `SplitButtonLayout` + `SplitButtonDefaults.LeadingButton/TrailingButton` — **there is no
  `SplitButton` composable** (verified in source); splitting the halves is `SplitButtonLayout`
- `WideNavigationRail` / `ModalWideNavigationRail` — expanded rail for large screens
- `ShortNavigationBar` — compact bottom bar for small/medium width (`ShortNavigationBarItem`)
- `ToggleFloatingActionButton` — FAB toggling two states with morph animation
- `FloatingActionButtonMenu` — FAB that expands into a menu
- `FlexibleBottomAppBar` — bottom app bar with flexible arrangement (graduated alpha23)
- `MediumFlexibleTopAppBar` / `LargeFlexibleTopAppBar` / `TwoRowsTopAppBar` — flexible top app bars (graduated alpha23)
- Slot-based `SearchBar` + `SearchBarState` (`animateToExpanded/Collapsed` are suspend);
  `AppBarWithSearch` replaces `TopSearchBar`
- `LoadingIndicator` / `ContainedLoadingIndicator` (`progress: () -> Float`), and
  `LinearWavyProgressIndicator` / `CircularWavyProgressIndicator`
- `ScrollField` (+ `rememberScrollFieldState`) — wheel-style picker input
- Expressive list items / menus, Expressive TimePicker (`VibrantTimePickerDialog` was `RichTimePickerDialog`)
- `ToggleButton` / `FilledTonalToggleButton` (was `TonalToggleButton`); `carouselParallaxScrollEffect` (alpha28)
- `PolygonShape` in-place `transform { }` / `copy()` — lives in
  `androidx.compose.foundation.shape`, **not** `material3`; `MaterialShapes` exposes 35 preset
  `RoundedPolygon`s + `toShape()`

## Workflow

Follow these steps when building or modifying Material UI:

1. **Set up theming** — Use `MaterialExpressiveTheme` instead of `MaterialTheme`. See the snippet
   below for the standard scaffold. Dynamic color requires API 31+ with fallback.
2. **Pin versions** — For full M3E use `material3` **1.5.0-beta02** (2026-10-21) or the matching
   `compose-bom-alpha`. Read `references/version-baseline.md` before choosing stable vs the 1.5.0
   line; declare `material-icons-core` explicitly (not transitive since 1.4.0) or use Material Symbols.
3. **Generate a theme from a brand color (optional)** — Run `scripts/generate_theme.py` to derive a
   full light/dark color scheme from one seed color. Copy `assets/templates/` into the project and
   customize, or let the script emit `Color.kt` + `Theme.kt`.
4. **Choose components** — Consult `references/components-catalog.md` for the categorized list with
   M3/MD3E tags and key parameters; `references/m3e/components.md` for version-line status. Then use
   `references/component-index.md` to jump to the source file, official sample and spec page.
5. **Apply design tokens** — Token values live in `references/design-tokens.md`. Access at runtime via
   `MaterialTheme.colorScheme.*` / `.typography.*` / `.shapes.*` / `.motionScheme.*` (never
   `LocalMotionScheme`, removed in alpha27).
6. **Start from official patterns** — `references/compose-patterns.md` has verified wiring for theme,
   adaptive navigation, floating toolbars, button groups, split buttons, search, loading and lists.
   For anything not covered there, find the official sample via `references/official-samples.md`
   (`compose/material3/material3/samples/.../{Component}Samples.kt`) and copy its structure.
7. **Look up API signatures** — 1.5.0-line components: `references/m3e-api-signatures.md`
   (source-verified). Stable-line full snapshot: grep `references/compose-api-full.md`
   (e.g. `### ComponentName`, `fun lightColorScheme`).
8. **Look up official specs** — For design specs (anatomy, states, measurements), read files under
   `references/m3-content/` (e.g. `m3-content/components/{name}/specs.md`,
   `m3-content/styles/{category}/`). Snapshot captured **2026-09-14**.

### Standard theme scaffold

```kotlin
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialExpressiveTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.expressiveLightColorScheme
import androidx.compose.material3.MotionScheme
import androidx.compose.runtime.Composable

@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit,
) {
    MaterialExpressiveTheme(
        colorScheme = if (darkTheme) darkColorScheme() else expressiveLightColorScheme(),
        motionScheme = MotionScheme.expressive(),  // or MotionScheme.standard()
        typography = AppTypography,
        shapes = AppShapes,
        content = content,
    )
}
```

### Theme generator

```bash
python scripts/generate_theme.py --seed #6750A4 --package com.example.app --output ./theme/
python scripts/generate_theme.py --seed #6750A4 --variant expressive --contrast 0.25 --output ./theme/
```

Outputs `Color.kt` + `Theme.kt`. Uses Material Color Utilities (HCT) when installed — the script
auto-detects both the 0.2.x (`theme_from_argb_color`) and the legacy 0.1.x APIs. Without the library
it falls back to a built-in **HSL approximation** (not HCT — values will differ). `--variant` picks
the HCT variant (`tonalspot` = M3 baseline, `expressive`, `vibrant`, …); `--contrast` sets 0.0–1.0.

## Resources (read on demand)

Only open these when the workflow above points to them — they are large and not needed every turn.

- `references/compose-patterns.md` — Verified code patterns: theming, adaptive navigation,
  floating toolbars, button groups, split buttons, search, loading, lists, motion, a11y.
- `references/official-samples.md` — Map of the 49 official `*Samples.kt` files, `compose-samples`
  apps, Now in Android, and the official docs; says which file to read for each component.
- `references/component-index.md` — Component → source file → official sample → spec page.
  Use it whenever the question is "where is this implemented / how is it used / how should it look".
- `references/m3e-api-signatures.md` — Source-verified signatures for 1.5.0-line components
  (`MaterialExpressiveTheme`, 8-step `Shapes`, `MotionScheme`, `FloatingToolbar`, `ButtonGroup`,
  `SplitButtonLayout`, `LoadingIndicator`, `Wavy*`, `ShortNavigationBar`, `ScrollField`, …).
- `references/version-baseline.md` — Version matrix, feature gates, 1.5.0-line churn log (2026-10-23).
- `references/m3e/` — Curated latest M3E notes (verified 2026-10-23), Chinese primary with
  English mirrors (`*.en.md`): `design-system.md`, `color-typography-shape.md`,
  `motion-physics.md`, `components.md`, `compose-api.md`.
- `references/compose-api-full.md` — Full `androidx.compose.material3` **stable-line (1.4.0)** API
  reference (~8000 lines). Use for exact signatures not covered by `references/m3e-api-signatures.md`.
- `references/design-tokens.md` — All 48 color roles, type scale (15 base + 15 `*Emphasized`),
  shape scale (M3 5 + M3E 3), motion system. Use for token values.
- `references/components-catalog.md` — Component list by category with M3/MD3E tags. Use to pick a
  component.
- `references/m3-vs-m3e-diff.md` — M3↔M3E differences, migration, I/O 2026 updates.
- `references/expressive-design-tactics.md` — The 7 official M3E design tactics with examples.
- `references/design-research.md` — HCT color science, variable fonts, motion/accessibility research.
- `references/m3-content/` — Mirror of m3.material.io (**263 pages** = 249 spec pages + 14
  overview pages; specs captured 2026-09-14 and sitemap-verified 2026-10-08, M3E articles and
  platform guides added 2026-10-19). Read
  `m3-content/components/{name}/specs.md`, `m3-content/styles/{category}/`, or the M3E articles in
  `m3-content/blog/`. Treat it as the **visual/measurement** reference, not API truth: upstream
  component pages last changed 2026-07~09, and new Expressive components (floating toolbar, short
  navigation bar, scroll field) have no standalone spec page yet — fall back to source + samples.
- `assets/templates/` — Ready-to-use `MD3ETheme.kt`, `Color.kt`, `Type.kt`, `Shape.kt`. Copy into
  `ui/theme/` and customize.
- `scripts/generate_theme.py` — Seed color → complete Compose theme (see Workflow step 3).

## Design Principles (MD3E)

1. **Color as hierarchy** — Use color roles (primary/secondary/tertiary + containers + surface tones)
   for visual layers. MD3E adds `*Fixed` roles that stay constant across light/dark.
2. **Shape variety** — Mix rounded/pill/angular shapes to create tension and guide attention.
3. **Spring-based motion** — Use spring physics; `MotionScheme.expressive()` for lively,
   `MotionScheme.standard()` for subtle.
4. **Variable typography** — Use weight/size/color/spacing for editorial hierarchy.
5. **Container grouping** — Group related content in surface-toned containers to reduce load.
6. **Adaptive components** — Adapt to screen size (`WideNavigationRail` large, `NavigationBar` compact).
7. **Highlight moments** — Create 1-2 delightful interaction moments that connect emotionally.
8. **Icons** — Prefer Material Symbols from fonts.google.com/icons; declare `material-icons-core`
   explicitly if still using `androidx.compose.material.icons` (not transitive since M3 1.4.0).
