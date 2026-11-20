# Design Research & Foundations

Research-backed knowledge from Google's Material Design blog, condensed for practical use.
Sources cited per section.

---

## 1. Color Science & HCT Color Space

Source: [The Science of Color & Design](https://m3.material.io/blog/science-of-color-design) (Feb 2022)

### Perceptually Accurate Color

M3's color system is built on **HCT** (Hue, Chroma, Tone) — a perceptually accurate color space
that matches how humans actually see colors. This was developed by Google color scientists to
solve fundamental problems:

- **Hue** — what angle on the color wheel (red vs purple, yellow vs green)
- **Chroma** — how vibrant or neutral (close to gray) a color looks
- **Tone** — how close to white or black (vertical axis, like floors in a building)

### Why HCT Matters

Traditional color spaces (RGB, HSL) don't match human perception — a "50% lightness" yellow
looks much brighter than a "50% lightness" blue to humans. HCT fixes this:

- **Smooth color distributions** — colors that are adjacent in HCT space look smoothly related
- **Predictable contrast** — tone values directly correspond to perceived lightness, so contrast
  ratios are accurate
- **Algorithmic color generation** — the entire M3 color scheme can be generated from a single
  seed color using HCT math, ensuring harmony

### Dynamic Color Algorithm

M3's dynamic color is **algorithmic** — all colors are generated from rules, not hand-picked.
Designers explore by hand first, then encode good results as algorithms. The HCT space enables:

1. Generate a tonal palette (tone 0-100) from a seed color
2. Assign color roles to specific tones (primary=40, primaryContainer=90, etc.)
3. Ensure contrast ratios meet WCAG standards automatically

---

## 2. Dynamic Color Harmony

Source: [Designing Harmony into Dynamic Color](https://m3.material.io/blog/dynamic-color-harmony) (Feb 2022)

### The Semantic Color Challenge

When dynamic color changes the entire scheme based on wallpaper, **semantic colors** (colors with
conventional meaning — red for stop, yellow for lights, blue for cooling) can clash with the
user's color scheme.

### Color Harmony Solution

Google's color science team developed harmony rules using **hue relationships** on the color wheel:

- **Complementary** — opposite hues (180° apart)
- **Analogous** — adjacent hues (within 30-60°)
- **Triadic** — evenly spaced (120° apart)

The algorithm adjusts semantic colors' hue and chroma so they remain identifiable while
harmonizing with the user's wallpaper-derived scheme. For example, a "yellow" for lighting
stays recognizably yellow but shifts slightly to complement a blue wallpaper scheme.

### Custom Colors

M3 supports **custom colors** — brand or semantic colors that are integrated into the dynamic
color system while maintaining their identity. This is the foundation for the M3E **Fixed color
roles** (primaryFixed, etc.) that don't change between light/dark modes.

---

## 3. Tone-based Surface Colors

Source: [Introducing Tone-based Surfaces in Material 3](https://m3.material.io/blog/tone-based-surface-color-m3) (Mar 2023)

### From Elevation Overlay to Surface Containers

Previously, tinted surfaces were achieved by assigning `surface` color + increasing elevation
(adding an opacity overlay). The update introduces **dedicated surface color roles** no longer
tied to elevation:

| Old (elevation-based) | New (tone-based) |
|----------------------|------------------|
| Surface at elevation 0 | `surface` |
| Surface at elevation +1 | `surfaceContainerLow` |
| Surface at elevation +2 | `surfaceContainer` |
| Surface at elevation +3 | `surfaceContainerHigh` |
| (new) | `surfaceContainerLowest` / `surfaceContainerHighest` |
| (new) | `surfaceDim` / `surfaceBright` |

### Benefits

- **Layout flexibility** — choose surface roles by containment needs, not elevation
- **Large screen support** — more surface levels for complex layouts
- **All Material Components** automatically updated to use new surface container roles

---

## 4. Variable Fonts: Roboto Flex

Source: [Roboto… But Make It Flex](https://m3.material.io/blog/roboto-flex) (May 2022)

### 12 Variable Axes

Roboto Flex is a variable font with **12 axes** — the most flexible typeface in Google Fonts.
Key axes:

| Axis | Description | Range |
|------|-------------|-------|
| `wght` (Weight) | Font weight | 100–1000 |
| `wdth` (Width) | Horizontal compression/expansion | 25%–151% |
| `opsz` (Optical Size) | Size-optimized glyph shapes | 8–144 |
| `GRAD` (Grade) | Subtle weight change without width change | -200–150 |
| `slnt` (Slant) | Italic angle | -10°–0° |
| Plus 7 parametric axes | Fine-tuning of glyph shapes | — |

### Why Variable Fonts Matter for M3E

M3E emphasizes **visually emphasized typography** — heavier weights, editorial layouts, and
dynamic adjustments. Variable fonts enable:

- **Optical sizing** — glyphs automatically optimize for display vs body text
- **Grade adjustment** — fine-tune weight for light/dark mode readability without layout shift
- **Expressive type** — bold editorial layouts with weight/width combinations
- `Typography` in Compose now supports a default font family merged with text styles

---

## 5. Readability Research: Grade for Light/Dark Mode

Source: [Adjusting Grade for Mode](https://m3.material.io/blog/readability-research) (May 2022)

### The Research Question

Is text in dark mode easier to read if it's slightly bolder? What font grade is equally readable
in light vs dark mode?

### Methodology

Google researchers conducted a study measuring reading speed and comprehension across:
- Light mode vs dark mode
- Multiple font grade values (using Roboto Flex's GRAD axis)

### Key Finding

Text in **dark mode benefits from slightly higher grade** (bolder) to achieve equal readability
to light mode. This is because:

- Light text on dark backgrounds appears visually "thinner" due to the **halo effect**
  (light spreads, making edges blur)
- Increasing grade compensates for this perceptual thinning

### Practical Application

When designing for both light and dark themes:
- Consider slightly increasing font weight/grade for dark mode
- Variable fonts with a `GRAD` axis allow this without changing layout (grade doesn't affect width)
- This research informs M3E's emphasis on **variable typography** that adapts to context

---

## 6. Motion Patterns

Source: [Building Beautiful Transitions with Material Motion](https://m3.material.io/blog/android-material-motion) (Sep 2020),
[Choosing the Right Transitions](https://m3.material.io/blog/motion-research-container-transform) (Jan 2022)

### Four Core Transition Patterns

These patterns, originally from M2, remain conceptually valid in M3E:

#### Container Transform
- **What**: one element transforms into another (list item → detail page, FAB → toolbar)
- **When**: hierarchical navigation between related elements
- **Effect**: maintains shared "outer" container while animating "inner" content swap
- **M3E equivalent**: enhanced with spring physics via MotionScheme

#### Shared Axis
- **What**: elements transition along a shared spatial axis (X, Y, or Z)
- **When**: peer-level navigation (tabs, sibling pages)
- **Effect**: reinforces spatial relationship between destinations

#### Fade Through
- **What**: outgoing element fades out completely, then incoming fades in
- **When**: top-level navigation (switching between unrelated destinations)
- **Effect**: signals a break in relationship; fresh start

#### Fade
- **What**: simple opacity transition
- **When**: subtle, quick transitions within the same surface
- **Effect**: minimal disruption

### Research: Animated Transitions Improve Usability

Google's motion research found that **animated transitions** (vs instant state changes):
- Help users maintain **navigational context**
- Improve understanding of **information hierarchy**
- Make interfaces feel more **"fancy"** (polished, intentional) — user's own word

The study showed users preferred interfaces with container transform animations when navigating
between list and detail views, as the animation reinforced the relationship between elements.

---

## 7. Accessibility Foundations

Source: [Design for everyone](https://m3.material.io/blog/m3-a11y) (May 2022)

### Core Principles

M3's accessibility approach is built on:

1. **Color contrast by default** — dynamic color generates schemes that meet WCAG contrast
   ratios automatically; no manual contrast checking needed for standard color role pairings
2. **Tonal palette system** — the HCT tone values (0-100) are designed so standard role pairings
   (e.g., primary tone 40 + onPrimary tone 100) always meet contrast requirements
3. **Component-level accessibility** — components include built-in touch target sizing,
   semantic properties, and screen reader support
4. **Design-to-implementation framework** — guidelines for documenting structure, flow, and
   elements essential for assistive technology navigation

### Contrast Requirements

| Element Type | Minimum Contrast |
|-------------|-----------------|
| Normal text (< 18pt) | 4.5:1 (WCAG AA) |
| Large text (≥ 18pt or ≥ 14pt bold) | 3.0:1 |
| Non-text elements (icons, borders) | 3.0:1 |
| AAA compliance (optional) | 7.0:1 for normal text |

### M3E Contrast Levels (Android 16)

Three system-level contrast settings:
- **Default** — standard contrast
- **Medium** — enhanced contrast
- **High** — maximum contrast

---

## 8. Large Screen Design

Source: [Material Design Guidance for Large Screens](https://m3.material.io/blog/material-design-for-large-screens) (May 2021)

### Responsive Layout Principles

- Layout and component responsiveness is **baked into Material guidelines**
- Apps should **adapt, not just stretch** — components reorganize for larger screens
- Use **canonical layouts** for common patterns (list-detail, supporting panel, feed)

### Component Adaptation

| Component | Compact (< 600dp) | Medium (600-839dp) | Expanded (≥ 840dp) |
|-----------|-------------------|--------------------|--------------------|
| Navigation | NavigationBar | NavigationRail | NavigationDrawer / WideNavigationRail [M3E] |
| Content | Single pane | List-detail | List-detail + supporting panel |
| FAB | Standard | Standard/Extended | Extended |

### IO 2026 Update

The Expressive layout system (announced Google I/O 2026) adds:
- **8dp spacing system** for programmatic adaptation
- Layout scaffold for mobile, desktop, spatial devices, and XR
- New design guidance for watches and immersive XR

---

## 9. Figma Design Kit

Source: [Material 3 Figma Design Kit](https://m3.material.io/blog/material-3-figma-design-kit)

The official **Material 3 Figma Design Kit** provides:
- All M3/M3E components as Figma components
- Color scheme variables (including M3E Fixed roles and surface containers)
- Type scale styles
- Shape system
- Dynamic color simulation

**Figma Community link**: [Material 3 Design Kit](https://www.figma.com/community/file/1035203688168086460)

For developers, the design kit is the reference for visual specs. The Compose library implements
these specs in code. When there's a question about how a component should look, check the Figma
kit first, then verify against the Compose API.

### Material Theme Builder

[Material Theme Builder](https://material.io/material-theme-builder) — official tool for:
- Generating color schemes from a seed color
- Exporting to Compose (Color.kt + Theme.kt)
- Previewing light/dark/dynamic color schemes
- The `scripts/generate_theme.py` in this skill replicates this functionality programmatically
