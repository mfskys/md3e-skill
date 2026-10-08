---
name: md3e
version: 1.3.0
description: "Material Design 3 Expressive (MD3E) design system skill for Android Jetpack Compose. This skill should be used when building Android UI with Material 3 / Material 3 Expressive design language, including theming (color schemes, typography, shapes, motion), component implementation (buttons, cards, navigation, FAB, floating toolbar, button group, etc.), and design guidance (when to use which component, M3 vs M3E differences, expressive design principles). Covers both MD3E (the evolution released 2025, targeting Android 16) and baseline M3 (many components only have M3 specs). Knowledge baseline 2026-10-08: material3 1.5.0-beta01 / stable 1.4.0. Triggers on requests like Material 3 Expressive, MD3E, Material Design 3, M3 theme, MaterialExpressiveTheme, Compose Material 3 component, or when designing/building Android UI that should follow Google Material design guidelines."
---

# Material Design 3 Expressive (MD3E) Skill

## Overview

Comprehensive knowledge of Google's Material Design 3 Expressive (MD3E) design system and its
implementation in Android Jetpack Compose (`androidx.compose.material3`). MD3E is the 2025 evolution
of M3, with research-backed updates to theming, components, motion, typography, and shapes. It targets
Android 16 but is available via the Compose Material 3 library (1.5.0-alpha+) for lower API levels.

**Knowledge baseline: 2026-10-08.** Recommended dependency for full M3E:
`androidx.compose.material3:material3:1.5.0-beta01` (or `compose-bom-alpha:2026.10.00`). Stable
**1.4.0** provides M3 + `MotionScheme` + partial Expressive only — since **1.4.0-beta01** the stable
line removed public `ExperimentalMaterial3ExpressiveApi` APIs. The 1.5.0 line **entered beta on
2026-10-07**, so the Expressive APIs are stabilizing; Google still does not recommend alpha/beta
builds for production.

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
| Shapes | `Shapes(extraSmall, small, medium, large, extraLarge)` | (same, with more varied usage) |
| Experimental opt-in | `@ExperimentalMaterial3Api` | `@ExperimentalMaterial3ExpressiveApi` |

### MD3E-Only Components (version gates: see `references/version-baseline.md`)

On the **1.5.0** line (full set); several graduated non-experimental:

- `HorizontalFloatingToolbar` / `VerticalFloatingToolbar` — floating contextual toolbars (alpha22+)
- `ButtonGroup` — connected button row with overflow menu (APIs stable alpha22+; `ButtonGroupScope` sealed alpha25+)
- `SplitButton` — split button with primary + overflow (**not** `SplitButtonLayout`, deprecated alpha25)
- `WideNavigationRail` / `ModalWideNavigationRail` — expanded rail for large screens
- `ToggleFloatingActionButton` — FAB toggling two states with morph animation
- `FloatingActionButtonMenu` — FAB that expands into a menu
- `FlexibleBottomAppBar` — bottom app bar with flexible arrangement (graduated alpha23)
- `MediumFlexibleTopAppBar` / `LargeFlexibleTopAppBar` / `TwoRowsTopAppBar` — flexible top app bars (graduated alpha23)
- Slot-based `SearchBar` + `SearchBarState` (stable alpha24); `AppBarWithSearch` replaces `TopSearchBar`
- Expressive list items / menus, Expressive TimePicker (`VibrantTimePickerDialog` was `RichTimePickerDialog`)
- `ToggleButton` / `FilledTonalToggleButton` (was `TonalToggleButton`); `carouselParallaxScrollEffect` (alpha28)
- `PolygonShape` in-place transform API — `transform { }` / `copy()`, `CornerRounding.dp()` / `.fraction()` (beta01)

## Workflow

Follow these steps when building or modifying Material UI:

1. **Set up theming** — Use `MaterialExpressiveTheme` instead of `MaterialTheme`. See the snippet
   below for the standard scaffold. Dynamic color requires API 31+ with fallback.
2. **Pin versions** — For full M3E use `material3` **1.5.0-beta01** (or `compose-bom-alpha:2026.10.00`).
   Read `references/version-baseline.md` before choosing stable vs the 1.5.0 line; declare
   `material-icons-core` explicitly (not transitive since 1.4.0) or use Material Symbols.
3. **Generate a theme from a brand color (optional)** — Run `scripts/generate_theme.py` to derive a
   full light/dark color scheme from one seed color. Copy `assets/templates/` into the project and
   customize, or let the script emit `Color.kt` + `Theme.kt`.
4. **Choose components** — Consult `references/components-catalog.md` for the categorized list with
   M3/MD3E tags and key parameters; `references/m3e/components.md` for version-line status.
5. **Apply design tokens** — Token values live in `references/design-tokens.md`. Access at runtime via
   `MaterialTheme.colorScheme.*` / `.typography.*` / `.shapes.*` / `.motionScheme.*` (never
   `LocalMotionScheme`, removed in alpha27).
6. **Look up API signatures** — For any composable/function, grep `references/compose-api-full.md`
   (e.g. `### ComponentName`, `fun lightColorScheme`, `MaterialExpressiveTheme`, `MotionScheme`).
7. **Look up official specs** — For design specs (anatomy, states, measurements), read files under
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

- `references/version-baseline.md` — Version matrix, feature gates, 1.5.0-line churn log (2026-10-08).
- `references/m3e/` — Curated latest M3E notes (verified 2026-10-08), Chinese primary with
  English mirrors (`*.en.md`): `design-system.md`, `color-typography-shape.md`,
  `motion-physics.md`, `components.md`, `compose-api.md`.
- `references/compose-api-full.md` — Full `androidx.compose.material3` API reference (~8000 lines).
  Use for exact signatures.
- `references/design-tokens.md` — All color roles, type scale (15 styles), shape scale (5 sizes),
  motion system. Use for token values.
- `references/components-catalog.md` — Component list by category with M3/MD3E tags. Use to pick a
  component.
- `references/m3-vs-m3e-diff.md` — M3↔M3E differences, migration, I/O 2026 updates.
- `references/expressive-design-tactics.md` — The 7 official M3E design tactics with examples.
- `references/design-research.md` — HCT color science, variable fonts, motion/accessibility research.
- `references/m3-content/` — Mirror of m3.material.io (**256 pages** = 249 spec pages + 7 hub pages;
  captured 2026-09-14, re-verified against the official sitemap on 2026-10-08 — no page added or
  removed; clean Markdown + front matter). Authoritative design specs; read
  `m3-content/components/{name}/specs.md` or `m3-content/styles/{category}/`.
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
