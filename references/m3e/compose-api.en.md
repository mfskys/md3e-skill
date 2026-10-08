# M3E Compose API & Migration

Verified: **2026-10-08**
Sources: Compose Material 3 official release notes (page updated 2026-10-07) ✅ +
Material Design 3 for Compose (page updated 2026-09-08) ✅

---

> 📌 **Version policy**: this project **adopts the newest versions (including Alpha/Beta/RC)** —
> i.e. `material3 = 1.5.0-beta01`, see `../version-baseline.md`.
> Mentions of the "stable line (1.4.0)" below are **channel status notes only**, not our choice.

## 1. Version gates quick reference

| Capability | Minimum version | Stability |
| --- | --- | --- |
| `MaterialTheme` (colorScheme / typography / shapes) | Early M3 | ✅ Stable |
| Dynamic color (`dynamicLightColorScheme` etc.) | Early M3, needs **API 31+** | ✅ Stable |
| Component animations switch to `MotionScheme` | **1.4.0** | ✅ Stable |
| `MotionScheme.standard()` / `expressive()` | Since 1.4.0-alpha02 (renamed from `standardMotionScheme`/`expressiveMotionScheme`) | Version-dependent |
| `MaterialExpressiveTheme`, `expressiveLightColorScheme` | 1.5.0-alpha18 | ⚠️ 1.5.0 line |
| `ToggleButton` / FAB Menu | 1.4.0-alpha19 | ⚠️ 1.5.0 line |
| `ButtonGroup` | 1.4.0-alpha22 | ⚠️ 1.5.0 line |
| `SplitButton` | 1.4.0-alpha20 | ⚠️ 1.5.0 line |
| Flexible TopAppBar family / `FlexibleBottomAppBar` | 1.5.0-alpha23 | ⚠️ 1.5.0 line |
| `FloatingToolbar` | 1.5.0-alpha22 | ⚠️ 1.5.0 line |
| `SearchBarState` + slot `SearchBar` | 1.5.0-alpha24 | ⚠️ 1.5.0 line |
| `carouselParallaxScrollEffect` | 1.5.0-alpha28 | ⚠️ 1.5.0 line |
| `material3-ripple` | 1.5.0-alpha24 | ⚠️ 1.5.0 line (separate library) |
| `PolygonShape` in-place transform API | 1.5.0-beta01 | ⚠️ 1.5.0 line |
| `CarouselDefaults.ItemSpacing` / `.ContentPadding` | 1.5.0-beta01 | ⚠️ 1.5.0 line |

**Key conclusion**: **the full M3E component set currently exists only on the 1.5.0 line**
(which entered beta on 2026-10-07).
The stable line (1.4.0) ships "M3 + MotionScheme + partial Expressive" without the full M3E new components.

---

## 2. Breaking changes on the stable line (1.4.0)

| Change | Impact / handling |
| --- | --- |
| **`material-icons-core` transitive dependency removed** | Declare icon dependencies **explicitly** (I735ff, b/349894318) |
| **`androidx.compose.material.icons` discouraged** | Officially recommend Material Symbols vectors from fonts.google.com/icons |
| `NavigationBarItem` / `NavigationRailItem` selected label color | `onSurface` → **`secondary`**; to restore set `selectedTextColor = MaterialTheme.colorScheme.onSurface` manually |
| Component animation mechanism | All moved to **`MotionScheme`** |
| **1.4.0-beta01 removed all public APIs under `ExperimentalMaterial3ExpressiveApi` / `ExperimentalMaterial3ComponentOverrideApi`** | To keep using them, switch to the **1.5.0 line** |

---

## 3. Migration steps to M3E

```
1. Lock the version policy
   ├─ Stable: material3 = 1.4.0 (via BOM), stable components + MotionScheme only
   └─ Full:   material3 = 1.5.0-betaNN (compose-bom-alpha already covers material3; usually no explicit version)

2. Theme layer
   ├─ Light/dark ColorScheme (Material Theme Builder → Color.kt / Theme.kt)
   ├─ Dynamic color: API 31+ check + fallback
   └─ (optional) MaterialExpressiveTheme + expressiveLightColorScheme ⚠️alpha

3. Motion layer
   └─ All custom animations take specs from MaterialTheme.motionScheme
      ❌ remove scattered tween(300) / spring(stiffness=...) hard-codes

4. Icons layer
   ├─ Explicitly declare material-icons dependency, or
   └─ switch to Material Symbols vectors (recommended)

5. Component layer (incremental)
   ├─ Replace first: TopAppBar → Flexible family, SearchBar → slot version, bottom bars
   └─ Then add: ToggleButton / ButtonGroup / SplitButton / FAB Menu / Carousel

6. Verify
   ├─ Dark mode + dynamic color + large font scale
   ├─ Window sizes (device matrix in ../m3-content/foundations/layout/breakpoints/)
   └─ Visual regression: focus on surfaceContainer hierarchy (behavior changed in 1.3.0)
```

---

## 4. 1.5.0-line API churn (risk notice)

The 1.5.0 line saw **many renames and removals** over months, e.g.:

| Version | Change |
| --- | --- |
| beta01 | `TopAppBarDefaults.enterAlwaysScrollBehavior` `reverseLayout` overload restored as deprecated; `SliderState` `DraggableState` restored (binary compat); `PolygonShape` now in-place `transform {}` / `copy()`, `CornerRounding` moved to top level with `dp()` / `fraction()`; `HorizontalCenteredHeroCarousel` `maxItemWidth` → `preferredItemWidth`; new `CarouselDefaults.ItemSpacing` / `.ContentPadding` |
| alpha29 | **Source-breaking**: `Slider`/`RangeSlider` `onValueChange` now required and reordered; `TimeInput`/`DateInput` moved to the new `TextFieldState` text-field API |
| alpha28 | Stateless `Slider`/`RangeSlider` overloads deprecated; `RangeSliderState` field renames |
| alpha27 | Old `TopAppBarDefaults` scrollBehavior overloads removed; `LocalMotionScheme` removed; `RichTimePickerDialog` → `VibrantTimePickerDialog` |
| alpha26 | `ExposedDropdownMenu` becomes an extension function (**update imports**) |
| alpha25 | `TonalToggleButton` → `FilledTonalToggleButton`; ComponentOverride API removed; `SplitButtonLayout` deprecated |
| alpha24 | `SearchBarState` stable; `material3-ripple` new library |
| alpha23 | ComponentOverride API removed; Expressive AppBar graduated; `TextFieldLabelPosition.Attached` deprecated |
| alpha20 | BottomSheet remember APIs unified |
| alpha18 | `rememberWithGapSearchBarState` renamed; opt-in-free `Material3ExpressiveApi` provided |

**Conclusion**: when using alpha components, **read that version's release notes before upgrading**,
and keep call sites centralized (wrap in your own facade) to limit rename fallout.

---

## 5. Theme wiring skeleton

```kotlin
// Theme.kt
private val DarkColorScheme = darkColorScheme(/* Material Theme Builder output */)
private val LightColorScheme = lightColorScheme(/* ... */)

@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,          // allow users to turn dynamic color off
    content: @Composable () -> Unit,
) {
    val context = LocalContext.current
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ->
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = AppTypography,
        shapes = AppShapes,
        content = content,
    )
}
```

**Motion wiring** (1.4.0+):

```kotlin
val motion = MaterialTheme.motionScheme
val spec = motion.defaultSpatialSpec<Float>()
animateFloatAsState(targetValue = target, animationSpec = spec)
```

---

## 6. Accessibility hard constraints

| Constraint | Notes |
| --- | --- |
| Color pairs | `primary`+`onPrimary`, `primaryContainer`+`onPrimaryContainer`; official counter-example: `tertiaryContainer` + `primaryContainer` insufficient contrast |
| Font scale | After system font scaling, verify no overflow/clipping |
| Remove animations | When system "remove animations" is on, fall back to instant switches |
| Semantics | All interactive controls need `contentDescription` / semantics |

---

## 7. Open verification items ⚠️

1. Component **spec tables** on `m3.material.io` (sizes, spacing, state layer opacity) — site needs JS;
2. **Full signatures and token values** of `MotionScheme` spec methods;
3. Exact availability of `MaterialShapes` / shape morph APIs in the current Compose version;
4. Ownership/stability of M3E **LoadingIndicator** etc. in `material3`
   (no clear entry verified in release notes for this file).
