# MD3E Design Tokens

Complete design token reference for Material Design 3 Expressive, extracted from the official
`androidx.compose.material3` API reference and m3.material.io guidelines.

---

## 1. Color System

### 1.1 Color Roles (Full List)

The M3E color scheme (`ColorScheme`) contains **48 color roles**. Each role has a light and dark
variant. Roles marked **[M3E]** are new additions in Material 3 Expressive.

#### Primary
| Role | Light Tone | Dark Tone | Description |
|------|-----------|-----------|-------------|
| `primary` | 40 | 80 | Main brand color, used for prominent buttons/active states |
| `onPrimary` | 100 | 20 | Content (text/icon) on primary |
| `primaryContainer` | 90 | 30 | Container variant of primary |
| `onPrimaryContainer` | 10 | 90 | Content on primaryContainer |
| `inversePrimary` | 80 | 40 | Inverted primary for inverse surfaces |
| `primaryFixed` **[M3E]** | 90 | 90 | Fixed primary (same in light/dark) |
| `primaryFixedDim` **[M3E]** | 80 | 80 | Dimmed fixed primary |
| `onPrimaryFixed` **[M3E]** | 10 | 10 | Content on fixed primary |
| `onPrimaryFixedVariant` **[M3E]** | 30 | 30 | Variant content on fixed primary |

#### Secondary
| Role | Light Tone | Dark Tone | Description |
|------|-----------|-----------|-------------|
| `secondary` | 40 | 80 | Less prominent accent |
| `onSecondary` | 100 | 20 | Content on secondary |
| `secondaryContainer` | 90 | 30 | Container variant |
| `onSecondaryContainer` | 10 | 90 | Content on container |
| `secondaryFixed` **[M3E]** | 90 | 90 | Fixed secondary |
| `secondaryFixedDim` **[M3E]** | 80 | 80 | Dimmed fixed secondary |
| `onSecondaryFixed` **[M3E]** | 10 | 10 | Content on fixed secondary |
| `onSecondaryFixedVariant` **[M3E]** | 30 | 30 | Variant content on fixed secondary |

#### Tertiary
| Role | Light Tone | Dark Tone | Description |
|------|-----------|-----------|-------------|
| `tertiary` | 40 | 80 | Contrast/balance accent |
| `onTertiary` | 100 | 20 | Content on tertiary |
| `tertiaryContainer` | 90 | 30 | Container variant |
| `onTertiaryContainer` | 10 | 90 | Content on container |
| `tertiaryFixed` **[M3E]** | 90 | 90 | Fixed tertiary |
| `tertiaryFixedDim` **[M3E]** | 80 | 80 | Dimmed fixed tertiary |
| `onTertiaryFixed` **[M3E]** | 10 | 10 | Content on fixed tertiary |
| `onTertiaryFixedVariant` **[M3E]** | 30 | 30 | Variant content on fixed tertiary |

#### Error
| Role | Light Tone | Dark Tone | Description |
|------|-----------|-----------|-------------|
| `error` | 40 | 80 | Error color |
| `onError` | 100 | 20 | Content on error |
| `errorContainer` | 90 | 30 | Container variant |
| `onErrorContainer` | 10 | 90 | Content on container |

#### Surface / Background
| Role | Light Tone | Dark Tone | Description |
|------|-----------|-----------|-------------|
| `background` | 99 | 10 | App background |
| `onBackground` | 10 | 90 | Content on background |
| `surface` | 99 | 10 | Base surface color |
| `onSurface` | 10 | 90 | Content on surface |
| `surfaceVariant` | 90 | 30 | Alternative surface |
| `onSurfaceVariant` | 30 | 80 | Content on surfaceVariant |
| `surfaceTint` | 40 | 80 | Tint applied to elevated surfaces (= primary) |
| `inverseSurface` | 20 | 90 | Inverted surface (snackbars) |
| `inverseOnSurface` | 95 | 20 | Content on inverseSurface |
| `outline` | 50 | 60 | Subtle borders/dividers |
| `outlineVariant` | 80 | 30 | Less prominent outline |
| `scrim` | 0 | 0 | Scrim overlay (dialogs/drawers) |

#### Surface Container Roles **[M3E]**
These replace the old elevation overlay system with discrete tonal surface levels:

| Role | Light Tone | Dark Tone | Usage |
|------|-----------|-----------|-------|
| `surfaceDim` | 87 | 6 | Lowest prominence surface |
| `surfaceBright` | 98 | 24 | High prominence surface |
| `surfaceContainerLowest` | 100 | 4 | Card/dialog lowest layer |
| `surfaceContainerLow` | 96 | 10 | Card/dialog low layer |
| `surfaceContainer` | 94 | 12 | Card/dialog default layer |
| `surfaceContainerHigh` | 92 | 17 | Card/dialog high layer |
| `surfaceContainerHighest` | 90 | 22 | Card/dialog highest layer |

### 1.2 Color Scheme Builders

```kotlin
// M3 baseline
fun lightColorScheme(primary, onPrimary, primaryContainer, ...): ColorScheme
fun darkColorScheme(primary, onPrimary, primaryContainer, ...): ColorScheme

// MD3E expressive defaults
fun expressiveLightColorScheme(): ColorScheme  // M3E default light scheme

// Dynamic color (Android 12+, from wallpaper)
fun dynamicLightColorScheme(context: Context): ColorScheme
fun dynamicDarkColorScheme(context: Context): ColorScheme
```

### 1.3 Contrast Levels (Android 16)

MD3E supports three contrast levels accessible via system settings:
- **Default** — standard contrast
- **Medium** — enhanced contrast
- **High** — maximum contrast

### 1.4 Color Usage Guidelines

- **primary**: prominent buttons (Filled Button), active states, high-emphasis surfaces
- **secondary**: filter chips, less prominent interactive elements
- **tertiary**: balance/contrast accent, can highlight specific elements
- **error**: error states, destructive actions
- **surfaceContainer\***: cards, dialogs, sheets — choose level by prominence
- **\*Fixed** [M3E]: use when a color must NOT change between light/dark (e.g., brand logo, illustrations)
- Always pair container colors with their `on*Container` counterparts for accessible contrast

---

## 2. Typography Scale

**30 typography slots on the 1.5.0 line** = 15 base styles (5 groups × 3 sizes) + 15
`*Emphasized` variants (e.g. `titleLargeEmphasized`). Default font: Roboto. The base 15 exist on
every M3 version; the Emphasized variants are M3E-only (`Typography` on stable 1.4.0 has 15).

| Style | Font Size / Line Height | Weight | Letter Spacing | Usage |
|-------|------------------------|--------|----------------|-------|
| `displayLarge` | 57 / 64 | Regular (400) | -0.25sp | Hero text, large numbers |
| `displayMedium` | 45 / 52 | Regular (400) | 0sp | Large display |
| `displaySmall` | 36 / 44 | Regular (400) | 0sp | Medium display |
| `headlineLarge` | 32 / 40 | Regular (400) | 0sp | Large headline |
| `headlineMedium` | 28 / 36 | Regular (400) | 0sp | Medium headline |
| `headlineSmall` | 24 / 32 | Regular (400) | 0sp | Small headline |
| `titleLarge` | 22 / 28 | Medium (500) | 0sp | Large title |
| `titleMedium` | 16 / 24 | Medium (500) | 0.15sp | Medium title |
| `titleSmall` | 14 / 20 | Medium (500) | 0.1sp | Small title |
| `bodyLarge` | 16 / 24 | Regular (400) | 0.5sp | Primary body text |
| `bodyMedium` | 14 / 20 | Regular (400) | 0.25sp | Secondary body text |
| `bodySmall` | 12 / 16 | Regular (400) | 0.4sp | Tertiary body text |
| `labelLarge` | 14 / 20 | Medium (500) | 0.1sp | Button text, labels |
| `labelMedium` | 12 / 16 | Medium (500) | 0.5sp | Small labels |
| `labelSmall` | 11 / 16 | Medium (500) | 0.5sp | Tiny labels, captions |

### MD3E Typography Enhancements

- **Variable fonts**: MD3E encourages variable fonts for dynamic weight/width adjustments
- **Emphasized slots (M3E)**: `Typography` gains 15 parallel slots — `displayLargeEmphasized`,
  `headlineSmallEmphasized`, `titleLargeEmphasized`, `bodyMediumEmphasized`, `labelSmallEmphasized`,
  … Read them with `MaterialTheme.typography.titleLargeEmphasized`. Their token values live in
  `TypographyTokens` (they are not simply "bold"); on stable 1.4.0 these properties do not exist.
- **Emphasis styles**: use heavier weights and larger sizes to create editorial-style hierarchy
- **Font family**: M3 `Typography` has no `defaultFontFamily` parameter — set `fontFamily` on each `TextStyle` (or use a shared constant) instead

### Compose API

```kotlin
val typography = Typography(
    titleLarge = TextStyle(
        fontWeight = FontWeight.SemiBold,
        fontSize = 22.sp,
        lineHeight = 28.sp,
        letterSpacing = 0.sp
    ),
    // ... customize other styles as needed
)
```

Access via `MaterialTheme.typography.titleLarge`, etc.

---

## 3. Shape Scale

8 shape sizes in the 1.5.0 line (M3's 5 + 3 M3E sizes), from square to fully rounded.
Values verified against `ShapeTokens.kt` in `androidx-main` (2026-10-23):

| Shape | Corner Radius | Typical Usage |
|-------|-------------|---------------|
| `extraSmall` | 4dp | Small elements, text field corners |
| `small` | 8dp | Chips, small buttons, tooltip |
| `medium` | 12dp | Cards, dialogs, FAB (small) |
| `large` | 16dp | FAB (standard), large cards, sheets |
| `largeIncreased` | 20dp | **M3E**: between `large` and `extraLarge` |
| `extraLarge` | 28dp | FAB (extended), large containers, search bar |
| `extraLargeIncreased` | 32dp | **M3E**: between `extraLarge` and `extraExtraLarge` |
| `extraExtraLarge` | 48dp | **M3E**: near-circular containers |

### Additional Shapes
- `RectangleShape` — no corner radius (full-bleed images, dividers)
- `CircleShape` — fully circular (avatar, icon button, FAB variants)

### Compose API

```kotlin
val shapes = Shapes(
    extraSmall = RoundedCornerShape(4.dp),
    small = RoundedCornerShape(8.dp),
    medium = RoundedCornerShape(12.dp),
    large = RoundedCornerShape(16.dp),
    extraLarge = RoundedCornerShape(28.dp),
    // M3E (1.5.0 line) — optional on M3, used by new components
    largeIncreased = RoundedCornerShape(20.dp),
    extraLargeIncreased = RoundedCornerShape(32.dp),
    extraExtraLarge = RoundedCornerShape(48.dp),
)
```

Access via `MaterialTheme.shapes.medium`, etc.

### MD3E Shape Principles

- **Break uniformity**: mix shapes to create visual tension and guide attention
- **Shape morphing**: MD3E supports animated shape transitions (e.g., toggle FAB morphing)
- **35 shape variants**: official spec includes 35 shapes for image cropping, avatars, etc.
- **Component-specific shapes**: `ButtonShapes`, `ChipShapes`, `SplitButtonShapes` classes
  allow per-component shape customization

---

## 4. Motion System

### 4.1 M3 Baseline: Easing & Duration

#### Easing Curves
| Token | Cubic Bezier | Usage |
|-------|-------------|-------|
| `Emphasized` | (0.2, 0.0, 0.0, 1.0) | Primary motion curve |
| `EmphasizedDecelerate` | (0.05, 0.7, 0.1, 1.0) | Enter/exiting elements |
| `EmphasizedAccelerate` | (0.3, 0.0, 0.8, 0.15) | Exiting elements |
| `Standard` | (0.2, 0.0, 0.0, 1.0) | Standard motion |
| `StandardDecelerate` | (0.0, 0.0, 0.0, 1.0) | Visible at end |
| `StandardAccelerate` | (0.3, 0.0, 1.0, 1.0) | Visible at start |
| `Linear` | (0.0, 0.0, 1.0, 1.0) | Steady progress |

#### Duration Tokens
| Token | Duration | Usage |
|-------|----------|-------|
| `Short1`–`Short4` | 50–200ms | Small UI element transitions |
| `Medium1`–`Medium4` | 250–400ms | Medium transitions |
| `Long1`–`Long4` | 450–600ms | Large/complex transitions |

### 4.2 MD3E: Spring-Based Motion

MD3E replaces easing curves with **spring physics** driven by three parameters:
- **Stiffness** — controls overall animation speed
- **DampingRatio** — controls bounce/overshoot
- **InitialVelocity** — starting velocity

### 4.3 MotionScheme

`MotionScheme` is an interface providing `FiniteAnimationSpec` values for a `MaterialTheme`.
Two presets available:

```kotlin
// Standard: subtle, professional motion (less bounce, eases into final values)
MotionScheme.standard()

// Expressive: lively, bouncy motion (overshoots final values to add bounce)
// This is Material's recommended default. Used when MaterialExpressiveTheme is set.
MotionScheme.expressive()
```

Choose the scheme once at the theme level — all Material Components with built-in movement
will inherit the selected spec automatically.

```kotlin
@Composable
fun YourTheme(content: @Composable () -> Unit) {
    MaterialExpressiveTheme(
        motionScheme = MotionScheme.expressive(), // or MotionScheme.standard()
        content = content
    )
}
```

### 4.4 MotionScheme Spec Categories

MotionScheme provides specs in two categories:

#### Spatial Specs
Used to animate changes in an object's **position, orientation, size, and shape**.
The spring overshoots the final value and bounces into place.

| Spec | Usage |
|------|-------|
| `defaultSpatialSpec` | Partial screen coverage: bottom sheets, expanded navigation rails |
| `fastSpatialSpec` | Small components: switches, buttons |
| `slowSpatialSpec` | Full-screen animations, large transitions |

#### Effects Specs
Used to animate an object's **color and opacity** — where there should be NO overshoot.

| Spec | Usage |
|------|-------|
| `defaultEffectsSpec` | Content opacity within navigation rail |
| `fastEffectsSpec` | Color change of switch handle |
| `slowEffectsSpec` | Full-screen content refresh |

### 4.5 Speed Tiers Cross-Device

Speed tokens work **across devices**. For example, the Spatial "fast" token will always be
faster than "default" or "slow," but the exact values differ depending on whether the device
is a wearable, phone, or tablet. This ensures movement feels fast in the context of the device.
This is because springs specify damping and stiffness, not time — they naturally adapt.

### 4.6 Why Springs Over Tween/Easing?

- **Natural interruption**: when interrupted and retargeted, springs use current velocity for
  a seamless transition; tween animations jump awkwardly
- **Cross-device adaptivity**: spring tokens adapt to device context automatically
- **No time-based specs**: damping + stiffness define feel, not duration
- **Predictable feel**: Expressive and Standard are opinionated presets — swap schemes without
  changing property names

### 4.7 Accessing Motion in Compose

```kotlin
// Via MaterialTheme
MaterialTheme.motionScheme.defaultSpatialSpec<Float>()
MaterialTheme.motionScheme.defaultEffectsSpec<Color>()

// Components automatically use motionScheme when inside MaterialExpressiveTheme
```

### 4.8 Custom Component Animation with MotionScheme

For custom components, use `MaterialTheme.motionScheme` specs to stay consistent:

```kotlin
val interactionSource = remember { MutableInteractionSource() }
val isPressed by interactionSource.collectIsPressedAsState()

// Spatial motion (position/size changes) -> use spatial spec
val scale by animateFloatAsState(
    targetValue = if (isPressed) 0.9f else 1f,
    animationSpec = MaterialTheme.motionScheme.defaultSpatialSpec<Float>(),
    label = "scale"
)

// Effects motion (color/opacity changes) -> use effects spec
val color by animateColorAsState(
    targetValue = if (isPressed) Color.Green else Color.Red,
    animationSpec = MaterialTheme.motionScheme.defaultEffectsSpec<Color>(),
    label = "color"
)
```

### 4.9 Creating a Custom MotionScheme

For fine-grained control, create a custom `MotionScheme` object:

```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
fun playfulMotionScheme(): MotionScheme = object : MotionScheme {
    override fun <T> defaultEffectsSpec(): FiniteAnimationSpec<T> =
        spring(dampingRatio = Spring.DampingRatioNoBouncy, stiffness = 1600f)
    override fun <T> defaultSpatialSpec(): FiniteAnimationSpec<T> =
        spring(dampingRatio = 0.6f, stiffness = 700f)
    override fun <T> fastEffectsSpec(): FiniteAnimationSpec<T> =
        spring(dampingRatio = Spring.DampingRatioNoBouncy, stiffness = 3800f)
    override fun <T> fastSpatialSpec(): FiniteAnimationSpec<T> =
        spring(dampingRatio = 0.6f, stiffness = 1400f)
    override fun <T> slowEffectsSpec(): FiniteAnimationSpec<T> =
        spring(dampingRatio = Spring.DampingRatioNoBouncy, stiffness = 800f)
    override fun <T> slowSpatialSpec(): FiniteAnimationSpec<T> =
        spring(dampingRatio = 0.6f, stiffness = 300f)
}

// Usage
MaterialExpressiveTheme(motionScheme = playfulMotionScheme()) { /* content */ }
```

### 4.10 Motion Guidelines

- Use `MotionScheme.expressive()` for consumer-facing, personality-driven apps (recommended)
- Use `MotionScheme.standard()` for professional/utility apps
- `MaterialExpressiveTheme` defaults to `MotionScheme.expressive()`
- Spring motion is more natural and predictable than easing curves
- Combine with haptic feedback (vibration) at key interaction moments (release, threshold cross)
- BottomSheet components respect `MaterialTheme.motionScheme` during scroll/drag
- Available since Compose Material 3 `1.4.0-alpha11`; APIs stabilize in `1.5.0`

---

## 5. Elevation

M3 uses **tonal elevation** (color tone overlay) in addition to shadow elevation.

### Elevation Levels (dp)

| Level | dp | Usage |
|-------|----|----|
| Level 0 | 0dp | Flat surfaces (base) |
| Level 1 | 1dp | Cards (resting), text fields |
| Level 2 | 3dp | FAB (resting), raised buttons |
| Level 3 | 6dp | Snackbars, menus |
| Level 4 | 8dp | Dialogs, pickers |
| Level 5 | 12dp | Scrim overlays |

### Compose API

```kotlin
Surface(
    tonalElevation = 6.dp,   // adds tonal color overlay
    shadowElevation = 6.dp,  // adds drop shadow
) { /* content */ }
```

- In **light** mode: tonal elevation darkens the surface tone slightly
- In **dark** mode: tonal elevation lightens the surface using primary color tint
- `shadowElevation` adds a drop shadow in both modes

### MD3E Elevation Changes

MD3E increasingly uses `surfaceContainer*` color roles instead of tonal elevation to distinguish
surface layers. Prefer surface container roles for layering; reserve elevation for true depth.

---

## 6. Window Size Classes

For adaptive layouts across phone/tablet/foldable:

| Width Size Class | dp Range | Typical Navigation |
|-----------------|----------|-------------------|
| Compact | 0–599dp | `NavigationBar` |
| Medium | 600–839dp | `NavigationRail` |
| Expanded | 840dp+ | `WideNavigationRail` / `NavigationDrawer` |

```kotlin
val windowSizeClass = calculateWindowSizeClass(activity)
when (windowSizeClass.widthSizeClass) {
    WindowWidthSizeClass.Compact -> { /* NavigationBar */ }
    WindowWidthSizeClass.Medium -> { /* NavigationRail */ }
    WindowWidthSizeClass.Expanded -> { /* WideNavigationRail */ }
}
```
