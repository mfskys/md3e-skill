# M3 vs M3E Differences

Material 3 Expressive (M3E) is an **expansion** of Material Design 3, not a replacement. This
document covers what changed, what's new, and what stayed the same.

> **Version baseline (2026-10-08):** full M3E component set ships only on the **1.5.0 line**
> (`material3` **1.5.0-beta01**, which entered beta on 2026-10-07). Stable **1.4.0** = M3 +
> `MotionScheme` + partial Expressive. Since **1.4.0-beta01**, all public
> `ExperimentalMaterial3ExpressiveApi` APIs were **removed from the stable line**.
> Details: `references/version-baseline.md`, `references/m3e/compose-api.md`.

---

## Summary

| Aspect | M3 (baseline) | M3E (expressive) |
|--------|---------------|-------------------|
| Theme composable | `MaterialTheme` | `MaterialExpressiveTheme` (1.5.0-alpha18+) |
| Color scheme | `lightColorScheme()` / `darkColorScheme()` | + `expressiveLightColorScheme()` |
| Color roles | 30 roles | + 18 Fixed roles + 7 surface container roles = 48+ |
| Motion | Easing curves + duration tokens | `MotionScheme` (spring physics), stable since 1.4.0 |
| Shapes | 5-size scale (uniform usage) | 5-size scale (varied, mixed, morphing) |
| Typography | 15 styles (static) | 15 styles (variable fonts, emphasis) |
| Experimental API | `@ExperimentalMaterial3Api` | `@ExperimentalMaterial3ExpressiveApi` (removed from stable 1.4.0-beta01; still used on 1.5.0-alpha for some APIs) |
| Min Compose version | 1.0+ | 1.5.0-alpha+ (for full M3E) |
| Target Android | Any | Android 16 (visual style), but works on lower |
| Icons | `material-icons-core` was transitive | **Must declare explicitly since 1.4.0**; prefer Material Symbols |

---

## 1. What's New in M3E

### 1.1 Theming

- **`MaterialExpressiveTheme`** — new theme composable that accepts a `MotionScheme` parameter
  in addition to colorScheme/typography/shapes. Use this instead of `MaterialTheme` for M3E.
- **`expressiveLightColorScheme()`** — pre-built expressive light color scheme with M3E defaults.
- **`MotionScheme`** — new theming subsystem for spring-based motion. Two presets:
  `MotionScheme.standard()` and `MotionScheme.expressive()`.

### 1.2 Color Roles

18 new **Fixed** color roles that remain the same in light and dark mode:
`primaryFixed`, `primaryFixedDim`, `onPrimaryFixed`, `onPrimaryFixedVariant` (×3 for
primary/secondary/tertiary).

7 new **Surface Container** roles replacing the old elevation overlay system:
`surfaceDim`, `surfaceBright`, `surfaceContainerLowest/Low/Container/High/Highest`.

### 1.3 Motion System

- **Spring physics** replaces easing curves as the primary motion system
- `MotionScheme` provides spatial (position/size) and effects (color/opacity) animation specs
- Components automatically use `motionScheme` when inside `MaterialExpressiveTheme`
- Three speed tiers: default, fast, slow (for both spatial and effects)

### 1.4 New Components

| Component | Purpose |
|-----------|---------|
| `HorizontalFloatingToolbar` / `VerticalFloatingToolbar` (`FloatingToolbar`) | Contextual toolbar floating above content (1.5.0-alpha22+) |
| `ButtonGroup` | Connected button row with overflow menu and compression animation (1.4.0-alpha22+) |
| `SplitButton` | Primary action + overflow trigger (**use `SplitButton`, not `SplitButtonLayout`** — layout deprecated alpha25) |
| `WideNavigationRail` / `ModalWideNavigationRail` | Expanded navigation rail for medium/expanded screens |
| `ToggleFloatingActionButton` | FAB that morphs between two states |
| `FloatingActionButtonMenu` | FAB that expands into a vertical menu |
| `FlexibleBottomAppBar` | Bottom app bar with flexible content arrangement (graduated 1.5.0-alpha23) |
| `MediumFlexibleTopAppBar` / `LargeFlexibleTopAppBar` / `TwoRowsTopAppBar` | Flexible top app bars (graduated 1.5.0-alpha23) |
| `ToggleButton` / `FilledTonalToggleButton` | Toggle buttons (`TonalToggleButton` renamed → `FilledTonalToggleButton` alpha25) |
| Slot-based `SearchBar` + `SearchBarState` | Modern search API (stable 1.5.0-alpha24; old APIs deprecated) |
| `AppBarWithSearch` | Replaces `TopSearchBar` |
| Expressive list items / menus / TimePicker | Non-interactive list variants, vibrant menus, expressive TimePicker |
| `carouselParallaxScrollEffect` | Global carousel parallax modifier (1.5.0-alpha28) |

### 1.5 Shape System

- **Shape morphing**: animated transitions between shapes (e.g., square→circle)
- **Mixed shapes**: encouraged to break uniformity — use different shapes for different components
- **35 shape variants**: official spec includes decorative shapes for images/avatars
- **Per-component shapes**: `ButtonShapes`, `ChipShapes`, `SplitButtonShapes` classes

### 1.6 Typography

- **Variable fonts**: support for dynamic weight/width adjustments
- **Font family**: M3 `Typography` has no `defaultFontFamily` parameter — set `fontFamily` on each `TextStyle` (or use a shared constant) instead
- **Emphasis**: bolder weights and editorial-style layouts for attention guidance

### 1.7 Text Field Enhancements

- `roundedShape` and `tonalColors()` in `TextFieldDefaults` / `OutlinedTextFieldDefaults`
  for expressive text field styling
- New label position options: `Inside` and `Cutout` (replacing deprecated `Attached`)
- New content padding APIs: `contentPaddingWithLabel()` / `contentPaddingWithoutLabel()`

### 1.8 Contrast Levels

Three system-level contrast settings (Android 16):
- Default, Medium, High — accessible via system display settings

---

## 2. What Stayed the Same (M3 Baseline)

These components and APIs work identically in M3 and M3E. They are NOT experimental and do not
require `@ExperimentalMaterial3ExpressiveApi`:

- All standard buttons: `Button`, `OutlinedButton`, `TextButton`, `FilledTonalButton`, `ElevatedButton`
- All FABs: `FloatingActionButton`, `SmallFloatingActionButton`, `LargeFloatingActionButton`, `ExtendedFloatingActionButton`
- All cards: `Card`, `ElevatedCard`, `OutlinedCard`
- `Checkbox`, `TriStateCheckbox`, `RadioButton`, `Switch`
- All chips: `AssistChip`, `FilterChip`, `InputChip`, `SuggestionChip` (+ elevated variants)
- `Slider`, `RangeSlider`
- `NavigationBar` / `NavigationBarItem`, `NavigationRail` / `NavigationRailItem`
- `ModalNavigationDrawer`, `PermanentNavigationDrawer`, `DismissibleNavigationDrawer`
- `TopAppBar`, `CenterAlignedTopAppBar`, `MediumTopAppBar`, `LargeTopAppBar`
- `BottomAppBar`
- `Scaffold`, `Surface`
- `ModalBottomSheet`, `BottomSheetScaffold`
- `AlertDialog`
- `Snackbar`
- `Tab`, `TabRow`, `PrimaryTabRow`, `SecondaryTabRow`
- `LinearProgressIndicator`, `CircularProgressIndicator`
- `Badge`, `BadgedBox`
- `Divider` (`HorizontalDivider`, `VerticalDivider`)
- `ListItem`
- `SearchBar`, `DockedSearchBar`
- `SegmentedButton` (+ single/multi choice rows)
- `DatePicker`, `DatePickerDialog`, `DateRangePicker`
- `TimePicker`, `TimeInput`
- `DropdownMenu`, `DropdownMenuItem`, `ExposedDropdownMenuBox`
- `Tooltip` (`PlainTooltip`, `RichTooltip`, `TooltipBox`)
- `SwipeToDismissBox`
- `Icon`, `Text`
- `ripple()` indication

---

## 3. Migration: M3 → M3E

### Step 1: Switch Theme

```kotlin
// Before (M3)
MaterialTheme(
    colorScheme = if (darkTheme) darkColorScheme() else lightColorScheme(),
    typography = typography,
    shapes = shapes
) { content() }

// After (M3E)
MaterialExpressiveTheme(
    colorScheme = if (darkTheme) darkColorScheme() else expressiveLightColorScheme(),
    motionScheme = MotionScheme.expressive(),
    typography = typography,
    shapes = shapes
) { content() }
```

### Step 2: Use Surface Container Colors

Replace tonal elevation with surface container roles where appropriate:

```kotlin
// Before (M3) — tonal elevation
Surface(tonalElevation = 6.dp) { /* card content */ }

// After (M3E) — surface container role
Surface(color = MaterialTheme.colorScheme.surfaceContainerHigh) { /* card content */ }
```

### Step 3: Adopt M3E Components (Optional)

Gradually introduce M3E components as needed:
- Replace `BottomAppBar` with `FlexibleBottomAppBar` for more layout flexibility
- Use `ButtonGroup` for connected action groups
- Use `FloatingToolbar` for contextual tools
- Use `WideNavigationRail` on expanded screens
- Use `ToggleFloatingActionButton` for state-toggle actions

### Step 4: Add Expressive Motion

Components inside `MaterialExpressiveTheme` automatically use `MotionScheme`. For custom
animations, access specs via `MaterialTheme.motionScheme`:

```kotlin
val animSpec = MaterialTheme.motionScheme.defaultSpatialSpec()
```

### Notes

- `MaterialExpressiveTheme` is backwards compatible — all M3 components work inside it
- Some M3E APIs still use `@ExperimentalMaterial3ExpressiveApi` on the 1.5.0 line; on **stable
  1.4.0-beta01+** those public experimental APIs were removed — stay on the **1.5.0** line for full M3E
- Graduated non-experimental (as of 1.5.0-alpha22/23): Flexible AppBar family, `FloatingToolbar`,
  `ButtonGroup` stable APIs, slot `SearchBarState` (alpha24)
- Dynamic color works the same in M3 and M3E
- **Icons:** declare `material-icons-core` explicitly or switch to Material Symbols
- **Preview-line churn:** read release notes before every material3 alpha/beta bump — see
  `references/version-baseline.md` §4 (`LocalMotionScheme` removed, `ExposedDropdownMenu` import
  change, Slider stateless overloads deprecated, etc.)

---

## 4. Google I/O 2026 Updates (May 2026)

At Google I/O 2026, Material announced several major updates beyond the initial M3E release:

### 4.1 Expressive Layout System

A new layout scaffold helps adapt interfaces for **mobile, desktop, spatial devices, and more**:
- New **spacing system** built on an **8dp scale** — apply spacing tokens to margins, padding,
  and gaps so layouts programmatically adapt to device type or density settings
- Updated layout principles: Scaffold, Grids & spacing, Breakpoints, Bidirectionality & RTL
- Canonical layout examples for adaptive design

### 4.2 Design for Watches & XR

New form factor design guidance:
- **Watches**: physics-based motion system, arc text styles, edge-hugging containers
- **Immersive XR**: spatial panels, depth-based elevation

### 4.3 Expressive Lists & Menus

Vibrant new styles and flexible configurations for:
- Expressive lists (non-interactive variants, vibrant styling)
- Expressive menus (flexible configurations, new visual styles)

### 4.4 Expressive Search & Search App Bar

- New visual style, motion, more flexibility for trailing icons
- **Contained search style**: persistent, filled search container
- Available for Jetpack Compose

### 4.5 Material Android is Compose-First

Major strategic announcement (Google I/O 2026):
- **Material Views 1.14.0** is the **final stable release** for the Views library (MDC-Android)
- Material Views is now in **maintenance mode** — no new features, only critical bug fixes
- All future feature development focuses on **Material Compose library**
- **Material Compose 1.5.0** (later 2026) will promote M3E experimental APIs to stable
- New **Styles API** integration for easier component customization
- **Navigation3** integrated into Material adaptive library
- Now is the best time to migrate from Views to Compose

### 4.6 14 Expressive Components (Complete List)

From the initial M3E release (May 2025), these 14 components were new or updated:

| Component | Status |
|-----------|--------|
| App bars | Updated |
| Button groups | **New** |
| Common buttons | Updated |
| Extended FAB | Updated |
| FAB menu | **New** |
| FABs | Updated |
| Icon buttons | Updated |
| Loading indicator | **New** |
| Navigation bar | Updated |
| Navigation rail | Updated |
| Progress indicators | Updated |
| Sliders | Updated |
| Split button | **New** |
| Toolbars | **New** |

### 4.7 7 Expressive Design Tactics

From the official M3E launch blog (May 2025):

1. **Use a variety of shapes** — mix round and square for tension and visual contrast; break
   from surrounding shape style to draw attention
2. **Apply rich and nuanced colors** — use contrast between primary/secondary/tertiary roles to
   prioritize actions and simplify navigation
3. **Guide attention with typography** — emphasized text styles, heavier weights, larger sizes,
   editorial-like moments
4. **Contain content for emphasis** — group similar content into containers; use size, spacing,
   rhythm, similarity for grouping
5. **Add fluid and natural motion** — shape morph, surface effects, expressive motion springs
6. **Leverage component flexibility** — adapt to foldable and large screens; canonical layouts
7. **Combine tactics for hero moments** — 1-2 memorable moments per product that break from
   predictable design; invest in making critical interactions sing

See `references/expressive-design-tactics.md` for detailed guidance on each tactic.
