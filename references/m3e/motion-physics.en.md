# M3E Motion Physics System

Verified: **2026-10-08**

| Content | Source | Confidence |
| --- | --- | --- |
| `MotionScheme` exists, `MaterialTheme.motionScheme`, component animations moved to `MotionScheme` | Compose Material 3 official release notes (2026-09-09) | ✅ |
| `MotionScheme.standard()` / `MotionScheme.expressive()` naming | Same (renamed from `standardMotionScheme`/`expressiveMotionScheme` in 1.4.0-alpha02) | ✅ |
| Motion physics **concepts** (spring-driven, spatial/effects taxonomy) | m3.material.io titles/summaries; body is CSR — not scrapable | ⚠️ |
| **Concrete token values** (stiffness / dampingRatio / durations) | **Not verified against official text** | ⚠️⚠️ |

> Usage rule: **do not** copy any number from this file into code.
> For exact parameters, read `MaterialTheme.motionScheme` API in code, or manually confirm on
> `m3.material.io/styles/motion` and the `MotionTokens` sources.

---

## 1. Paradigm shift: from "duration + easing" to spring physics

| Dimension | Traditional model | M3E physics model |
| --- | --- | --- |
| Driver | `durationMillis` + `easing` curve | Spring simulation (`stiffness` + `dampingRatio`) |
| End condition | Stops when fixed duration elapses | Settles when physics decays to rest — system "settles" automatically |
| Interruption | Manual velocity handling | Naturally carries velocity — seamless continuation (velocity handoff) |
| Expressiveness | Curve determines feel | Damping ratio determines bounce |

**Corollary**: spring animations **cannot be clamped with duration**. Wrapping `tween(300)`
around a spring is meaningless.

---

## 2. Motion taxonomy (official concepts, ⚠️ details TBD)

| Category | Properties covered | Damping bias |
| --- | --- | --- |
| **Spatial** | Position, size, rotation and other **displacement** changes | Allows slight undershoot/bounce for expressiveness |
| **Effects** | Opacity, color and other **in-place** changes | Typically critically damped (no bounce) to avoid visual noise |

**Speed tiers**: usually fast / default / slow — chosen by **component size and narrative importance**
(small components → fast; large/important transitions → slow).

> ⚠️ Naming and counts of the above taxonomy are design-spec level and not line-by-line verified;
> code follows the named `MotionScheme` APIs (methods shaped like `*SpatialSpec` / `*EffectsSpec`).

---

## 3. Compose usage

### Obtaining specs

```kotlin
// Motion scheme from the theme (LocalMotionScheme removed in 1.5.0-alpha27 — this is the only way)
val scheme = MaterialTheme.motionScheme

// Typical shape: take a spec by "category + speed tier", then feed animation APIs
val spec = scheme.defaultSpatialSpec<Float>()      // spatial, default tier
val effects = scheme.fastEffectsSpec<Color>()      // effects, fast tier

animateFloatAsState(targetValue = x, animationSpec = spec)
```

### Two schemes

| Scheme | Positioning |
| --- | --- |
| `MotionScheme.expressive()` | More expressive (default direction) |
| `MotionScheme.standard()` | More restrained, closer to traditional feel |

### Theme wiring

- `MaterialExpressiveTheme` (1.5.0 line, since alpha18) can wire M3E color + motion schemes in one call ⚠️.
- Component animations **have used `MotionScheme` since M3 1.4.0** ✅ — custom components should
  match the theme's scheme; hard-coded durations will fight on-screen rhythm.

---

## 4. Migration and usage rules

| Rule | Notes |
| --- | --- |
| **Never clamp springs with duration** | Do not wrap springs in `tween(300)`; do not add `delay` for springs |
| **Always take specs from the theme** | `MaterialTheme.motionScheme.xxxSpec<T>()`; no local spec creation |
| **Correct category** | Displacement/size/rotation → spatial; opacity/color → effects |
| **Consistent speed tier** | Same-tier for same-kind interactions on one screen |
| **Interruptible** | Gesture-driven animations should support mid-flight takeover (Compose 1.12 `DeferredAnimatedContent` / `DeferredAnimatedVisibility` are designed for this — velocity handoff, seamless takeover) ✅ |
| **Degradation** | When the system "remove animations" accessibility setting is on, fall back to instant switches |
| **Testing** | Animation tests use `runWithoutImplicitWait` + manual clock; `hasPendingWork` only checks pending work ✅ |

---

## 5. Legacy token system (fallback, ⚠️ values TBD)

M3E did not delete the old "duration + easing" tokens; they remain where springs do not fit
(e.g. precisely choreographed multi-step animations):

- **Duration tiers**: short / medium / long / extra-long × 4 steps (from ~50ms; extra-long up to ~1000ms)
- **Easing families**: emphasized, emphasized decelerate, emphasized accelerate, plus standard /
  decelerate / accelerate and legacy series

> ⚠️ Tiers and curves **not verified against official text** (m3.material.io requires JS).
> For exact values read Compose `MotionTokens`, or compare with the Material 3 Design Kit.

---

## 6. Open items (need manual browser verification)

1. Full token names/parameters for `spring.fast/default/slow` × `spatial/effects`;
2. Recommended motion-category map per component (e.g. FAB expansion vs page transitions);
3. Shape morph + motion interaction rules;
4. Official degradation guidance under "remove animations".
