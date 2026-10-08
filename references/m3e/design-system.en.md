# Material 3 Expressive Design Language Overview

Verified: **2026-10-08** | Markers: ✅ checked against official text / ⚠️ verify yourself / 🚧 experimental API

| Source | Notes |
| --- | --- |
| Material Design 3 for Compose (official) ✅ | https://developer.android.com/develop/ui/compose/designsystems/material3 | Page updated 2026-09-08 |
| Compose Material 3 release notes (official) ✅ | https://developer.android.com/jetpack/androidx/releases/compose-material3 | Page updated 2026-09-09 |
| `m3.material.io` ⚠️ | CSR SPA — body text cannot be scraped; **spec details require manual review** |

---

## 1. What is M3E?

Official quote (Compose docs):

> "Jetpack Compose provides implementations of both Material You and Material 3 Expressive —
> the next generation of Material Design.
> M3 Expressive is an extended version of Material Design 3, with research-backed updates to
> **theming, components, animation, and typography**…
> It also supports Material You personalization features such as dynamic color.
> **M3 Expressive complements Android 16's visual styling and system UI**." ✅

Key takeaways:

| Relationship | Notes |
| --- | --- |
| M3 vs M3E | M3E is an **extension/superset of Material 3**, not a breaking new design language |
| M3E vs Material You | Material You solves **personalization** (dynamic color); M3E solves **expressiveness** (motion, shape, hierarchy) |
| M3E vs Android 16 | Pairs with Android 16 system visual styling for better consistency |
| Platform | Android implementation is `androidx.compose.material3`; **Wear OS must use Wear Compose Material 3**, not this library ✅ |

---

## 2. Theming (Material Theming)

M3/M3E theming is three subsystems, provided via `MaterialTheme` ✅:

```kotlin
MaterialTheme(
    colorScheme = ...,   // color scheme
    typography  = ...,   // typography
    shapes      = ...,   // shapes
) {
    // content
}
```

| Subsystem | Contents | Details |
| --- | --- | --- |
| ColorScheme | 5 key colors + 13-tone palettes each; role semantics (primary / onPrimary / primaryContainer …) | `color-typography-shape.en.md` |
| Typography | 5 categories × 3 sizes = 15 styles | same |
| Shapes | extraSmall → extraLarge five corner radii | same |
| Motion | Spring physics motion (new in M3E) | `motion-physics.en.md` |

---

## 3. Elevation & Emphasis

### Tonal elevation

- M3 **primarily expresses height with tonal color overlays**, not shadows.
- Dark-theme overlays are also tonal, **drawn from the primary color slot**.
- `Surface` supports both `tonalElevation` and `shadowElevation`.

### Component emphasis levels

Components that offer multiple emphasis levels for the same semantic role (strongest → weakest):
`ExtendedFloatingActionButton` → `Button` → `TextButton` ✅

### Text emphasis

1. Use neutral pairs: `Surface` / `surfaceVariant` with `onSurface` / `onSurfaceVariant`;
2. Vary font weight (e.g. `bodyLarge` Bold vs `bodyMedium` Normal).

> ⚠️ Version notes: from M3 **1.3.0**, components default to `SurfaceContainer` variants and
> are **no longer affected by tonal elevation**;
> from 1.2.0, `ColorScheme` is **immutable**. Coloring based on older behavior will break.

---

## 4. Dynamic Color

- Core Material You feature: **derives colors from the user's wallpaper** for app and system UI.
- **Available only on Android 12 (API 31, `Build.VERSION_CODES.S`) and above**.
- Must **fall back** to custom light/dark schemes when unavailable.

```kotlin
val dynamic = Build.VERSION.SDK_INT >= Build.VERSION_CODES.S
val colorScheme = when {
    dynamic && darkTheme  -> dynamicDarkColorScheme(LocalContext.current)
    dynamic && !darkTheme -> dynamicLightColorScheme(LocalContext.current)
    darkTheme             -> DarkColorScheme
    else                  -> LightColorScheme
}
```

**Accessibility hard constraint**: dynamic color itself meets contrast standards, but
**custom edits must keep pairs**: `primary`+`onPrimary`, `primaryContainer`+`onPrimaryContainer`.
Official counter-example: **`tertiaryContainer` + `primaryContainer` has insufficient contrast** ✅

---

## 5. System UI

| Item | Notes |
| --- | --- |
| Ripple | Compose Material ripple uses the platform `RippleDrawable` on Android, so **Android 12+ sparkle ripples apply to all Material components** ✅ |
| Stretch overscroll | `LazyColumn` / `LazyRow` / `LazyVerticalGrid` **enabled by default**, independent of API level, Foundation 1.1.0+ ✅ |
| `material3-ripple` library | Added in 1.5.0-alpha24: replaces opacity layers with an **embedded focus ring** ⚠️ (alpha — adopt carefully) |

---

## 6. Navigation & Window Sizes

Official selection table ✅:

| Component | Use when |
| --- | --- |
| `NavigationBar` | Compact devices, **≤ 5 destinations** |
| `NavigationRail` | Landscape small–medium tablets or phones |
| `PermanentNavigationDrawer` / `ModalNavigationDrawer` (combinable with `NavigationRail`) | Medium–large tablets with room for detail |

> The truly adaptive approach is **`NavigationSuiteScaffold` switching by window size class** —
> see `../m3-content/foundations/layout/scaffold/overview.md`; the table above maps the low-level components.

---

## 7. Accessibility & Type Scaling

- Dynamic color meets contrast targets; tonal palette method keeps defaults usable.
- M3 type scale is a **dynamic size-category framework that scales across devices**: e.g. `Display Small`
  **may resolve to different values** on phone vs tablet ✅
- Design goals cover low vision, blindness, hearing, cognitive, motor, and situational impairments.

---

## 8. M3E Adoption Strategy (aggressive track)

> 📌 This project uses **`material3 = 1.5.0-beta01`**, so **the full M3E component set is available**.
> See `../version-baseline.md`.

1. **Theme first**: wire the three subsystems via `MaterialTheme` + dynamic color —
   prerequisite for every M3E component.
2. **Motion via `MotionScheme`**: component animations switched to `MotionScheme` in 1.4.0;
   custom animations should read `MaterialTheme.motionScheme` instead of hard-coding `tween` durations.
3. **Components from the 1.5.0 line**: ToggleButton, ButtonGroup, SplitButton, FAB Menu,
   FlexibleTopAppBar, slot SearchBar, etc. are all available;
   but **confine call sites** to `ui/expressive/` and record an exit plan.
4. **Do not rely on old `ExperimentalMaterial3ExpressiveApi` signatures**: public APIs under it
   were removed in 1.4.0-beta01; the 1.5.0 line keeps renaming (see `compose-api.en.md` §4) —
   always read release notes before upgrading.
5. **Icon source switch**: from M3 1.4.0, `material-icons-core` is no longer a transitive dependency
   and `androidx.compose.material.icons` is discouraged; use Material Symbols vectors instead.
6. **Specs verified in browser**: exact motion curves / component dimensions marked ⚠️ here;
   confirm on `m3.material.io` or the Figma Material 3 Design Kit before coding.
