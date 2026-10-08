# M3E Color / Typography / Shape

Verified: **2026-10-08**
Sources: Material Design 3 for Compose (official, page updated 2026-09-08) ✅ +
Compose Material 3 release notes (page updated 2026-09-09) ✅

---

# 1. Color System

## 1.1 Structure

- Foundation: **5 key colors** (primary / secondary / tertiary / error / neutral families),
  each with a **13-tone palette** ✅
- Role semantics:

| Role | Use |
| --- | --- |
| `primary` | Primary components (main buttons, selection, emphasis) |
| `secondary` | Secondary components (filter chips, less prominent UI) |
| `tertiary` | Contrast emphasis |
| `error` | Error states |
| `surface` / `surfaceVariant` / `surfaceContainer*` | Containers and backgrounds |
| `onXxx` | Foreground **on top of** `Xxx` (text/icons) |
| `XxxContainer` / `onXxxContainer` | Container-style components (FilledCard, Chip, …) |

- Access: `MaterialTheme.colorScheme.primary`.

## 1.2 Dynamic color

See `design-system.en.md` §4 (API 31+, `dynamicLightColorScheme` / `dynamicDarkColorScheme`,
mandatory fallback, keep pairs).

## 1.3 Generating a scheme

Official **Material Theme Builder** generates and exports Compose code from brand seed colors — two files ✅:

- `Color.kt`: all light/dark colors and role definitions;
- `Theme.kt`: `lightColorScheme` / `darkColorScheme` and theme setup.

## 1.4 Version-related color behavior changes (pitfall list)

| Version | Change | Impact |
| --- | --- | --- |
| 1.2.0-alpha08 | `ColorScheme` becomes **immutable** | Cannot mutate fields at runtime; rebuild instead |
| 1.3.0 | Components default to **`SurfaceContainer` variants, no longer affected by tonal elevation** | Hierarchy previously created via `tonalElevation` disappears; use correct `surfaceContainer` roles |
| 1.3.0 | Focus overlay **0.1f**; Surface/background tweaks in `lightColorScheme`/`darkColorScheme` | Suspect this first on visual regressions |
| 1.4.0 | `NavigationBarItem` / `NavigationRailItem` selected label **`onSurface` → `secondary`** | To restore: set `selectedTextColor = MaterialTheme.colorScheme.onSurface` manually |
| 1.5.0-alpha18 | Adds `expressiveLightColorScheme` | Alpha — adopt carefully |

---

# 2. Typography System

## 2.1 Type scale

**5 categories × 3 sizes = 15 styles** ✅: Display / Headline / Title / Body / Label,
each Large / Medium / Small.

Default examples (listed in official docs) ✅:

| Style | Font | Size / Line height |
| --- | --- | --- |
| `displayLarge` | Roboto | 57 / 64 |
| `bodyLarge` | Roboto | 16 / 24 |
| `labelSmall` | Roboto Medium | 11 / 16 |

Access: `MaterialTheme.typography.titleLarge`.

## 2.2 Key differences and changes

| Item | Notes |
| --- | --- |
| **M3 `Typography` has no `defaultFontFamily`** | Unlike M2, set `fontFamily` **on each `TextStyle`** ✅ |
| Since 1.2.0-alpha03 | `includeFontPadding` defaults to **`false`**; line-height styles use `Trim.None` + `Alignment.Center` ✅ |
| Dynamic size categories | Same step **may resolve differently** per device context (phone vs tablet) — basis of M3 cross-device scaling ✅ |
| Variable font axes | M3E typography is simpler, expressive via **variable font axes** ⚠️ (from Wear M3E description; mobile-side details TBD) |
| font variation settings | From Compose 1.12, downloadable fonts support **font variation settings** ✅ |
| Large type scale | Accessibility requires verifying layout after system font scaling (clipping, overflow) |

---

# 3. Shape System

## 3.1 Five corner radii

| Step | Example values (official docs) |
| --- | --- |
| `extraSmall` | 4dp |
| `small` | 8dp |
| `medium` | 12dp |
| `large` | 16dp |
| `extraLarge` | 24dp |

All are `RoundedCornerShape`; also `RectangleShape`, `CircleShape`.
Access: `MaterialTheme.shapes.medium`, or override per component.

## 3.2 M3E shape expressiveness

- M3E elevates **shape** as a primary expressive tool (shape-to-shape morphs/transitions).
- Spec-side details like the "35 shape set" ⚠️ must be confirmed on `m3.material.io` Shape chapter.
- Compose-side capabilities:
  - `MaterialShapes` (shape collections) and `MaterialShapes.toShape()` etc. are newer APIs —
    **verify your `material3` version includes them before use** ⚠️;
  - From 1.4.0-alpha01, `AnimatedPane` supports shapes (morphs with pane transitions) ✅.

## 3.3 Practice rules

- **Only use the five theme steps**; never write magic values like `RoundedCornerShape(7.dp)` in business code.
- Component-level customization goes through `XxxDefaults.shape` / component params, not global `MaterialTheme.shapes`.
- For morph animations, use `animate*AsState` with `Shape` interpolation; do not allocate new `Shape` objects on every recomposition.

---

# 4. Combining the Three

| Principle | Notes |
| --- | --- |
| Color expresses **semantics** | Use role names (primary / error), not raw hex — dynamic color and dark mode work automatically |
| Type expresses **hierarchy** | Build hierarchy with the type scale, not ad-hoc larger fonts |
| Shape expresses **grouping and affinity** | Larger containers → larger radii; cards at the same level must share radii |
| Motion expresses **cause and effect** | Elements return where they came from (see `motion-physics.en.md`) |
| All three must be **theme-overridable** | Business components must not hard-code colors / sizes / radii |
