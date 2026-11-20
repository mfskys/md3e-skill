# Expressive Design Tactics

The 7 design tactics from Google's official M3E launch (May 2025), extracted from the
"Start building with Material 3 Expressive" blog. These guide how to make UI more engaging
and direct user attention.

---

## 1. Use a Variety of Shapes

Shape is a powerful communication tool. At the base level, the shapes of components, containers,
and content set the tone at first glance.

### Principles
- Combine shapes and corner radii to create **visual tension or cohesion**
- Use a combination of **classic and abstract shapes** to create unique silhouettes or groupings
- Use the shape library and new corner-radii options to **mix round and square** for contrast

### Do / Caution
- **Do**: break from the surrounding shape style to draw attention to a particular element
- **Caution**: smaller shapes can make essential actions look less important

### M3E Shape Features
- **35 shape variants** in the official shape library for image crops, avatars, decorative elements
- **Shape-morph animation**: smooth transitions from one shape to another (e.g., square → circle)
- **Component shape classes**: `ButtonShapes`, `ChipShapes`, `SplitButtonShapes`

---

## 2. Apply Rich and Nuanced Colors

Material's dynamic color system offers colors for primary, secondary, and tertiary elements and
surfaces. Mixing these for key components helps emphasize the main takeaway of a screen.

### Principles
- Create **visual hierarchy with surface tones** — use surface container roles (surfaceDim through
  surfaceContainerHighest) to layer content
- Use **contrast between primary, secondary, and tertiary** color roles to prioritize actions
  and simplify navigation
- M3E adds **Fixed color roles** that don't change between light/dark — use for brand elements,
  illustrations, or content that must look identical in both themes

### Do / Caution
- **Do**: use contrast to emphasize the main takeaway or element
- **Caution**: without contrast, elements can blend together

### M3E Color Features
- 18 new Fixed color roles (primaryFixed, secondaryFixed, tertiaryFixed + dim/variant)
- 7 surface container roles (surfaceDim, surfaceBright, surfaceContainerLowest through Highest)
- Three contrast levels (Default, Medium, High) on Android 16

---

## 3. Guide Attention with Typography

Use emphasized text styles to draw attention to important UI elements like headlines and actions.

### Principles
- Create **editorial-like moments** by emphasizing typography
- **Heavier weights, larger sizes, color, and spacing** can direct attention and make key
  information more engaging
- Use additional type styles from the Material type scale to create appropriate hierarchy within
  and between blocks of content

### M3E Typography Features
- **Emphasized text styles** — new type styles for variable and static fonts expressing emotional
  states
- **Variable fonts** — dynamically adjust weight, width for readability
- **Bold editorial layouts** — support for magazine-style content hierarchy
- `Typography` now supports a default font family merged with provided styles

---

## 4. Contain Content for Emphasis

Organize content into logical groupings or containers. Give the most important content, tasks,
or actions visual prominence through ample space and the brightest surface mapping.

### Principles
- Use **size, spacing, rhythm, similarity**, or other grouping principles to make important
  elements more distinct
- Apply **surface container roles** to visually separate groups
- Use **ample space** (the brightest surface mapping) for the most important content

### Do / Caution
- **Do**: group similar content into informative groupings
- **Caution**: ungrouped information can blend together

### Implementation
```kotlin
// Group content using surface container roles
Surface(color = MaterialTheme.colorScheme.surfaceContainer) {
    // Related content group
}
Surface(color = MaterialTheme.colorScheme.surfaceContainerHigh) {
    // Higher-emphasis group
}
```

---

## 5. Add Fluid and Natural Motion

Make interactions feel alive and spirited through shape morph or surface effects.

### Principles
- Apply **expressive motion springs** (`MotionScheme.expressive()`)
- Use **custom micro animations** for delightful details
- **Shape morph** — animate shape transitions for engaging state changes
- **Surface effects** — subtle visual feedback on interaction

### Implementation
```kotlin
// Use MotionScheme for consistent spring-based motion
MaterialExpressiveTheme(
    motionScheme = MotionScheme.expressive(),
    // ...
)

// Custom components should use motionScheme specs
val scale by animateFloatAsState(
    targetValue = if (isPressed) 0.95f else 1f,
    animationSpec = MaterialTheme.motionScheme.defaultSpatialSpec(),
    label = "scale"
)
```

See `design-tokens.md` section 4 for full MotionScheme API details.

---

## 6. Leverage Component Flexibility

UI should adapt to the user context. Shift components or controls depending on the environment
to make completing tasks easier.

### Principles
- Adapt content to **foldable and large screens** through custom tweaks or canonical layouts
- Use **adaptive navigation**: NavigationBar (compact) → NavigationRail/WideNavigationRail
  (medium) → NavigationDrawer (expanded)
- Components should **reorganize, not just stretch**, on larger screens

### Window Size Class Mapping
| Width | dp Range | Navigation Component |
|-------|----------|---------------------|
| Compact | 0–599dp | `NavigationBar` |
| Medium | 600–839dp | `NavigationRail` / `WideNavigationRail` [M3E] |
| Expanded | 840dp+ | `WideNavigationRail` [M3E] / `PermanentNavigationDrawer` |

### IO 2026 Update: Expressive Layout System
- New **spacing system** on an 8dp scale for programmatic adaptation
- New layout scaffold for mobile, desktop, spatial devices, and XR
- Design guidance for watches and immersive XR

---

## 7. Combine Tactics to Create Hero Moments

Hero moments use multiple expressive tactics to break from predictable or uniformly applied
design ideas.

### Principles
- Make a **stand-alone statement** or frame essential information in a fresh, editorial way
- Hero moments are a **focusing mechanism** — invest time in making critical interactions sing
- These moments are the **heart of your product**

### Guidelines
- Keep hero moments **short but delightful**
- Make them **unexpected** (e.g., a small easter egg when completing a payment)
- **1-2 per product maximum** — too many will分散 attention

### How to Find Your Hero Moment
Ask yourself:
1. **Can this interaction tap into user emotion?**
   - Amplify achievement (e.g., celebration animation when hitting a fitness goal)
   - Reinforce familiarity (e.g., red packet opening sound in WeChat)
2. **Is this a key product action?**
   - Does a step need enhanced clarity?
   - Make important buttons more prominent, or let key information "jump out" to guide the eye

### Example: Combining Tactics
A hero moment might combine:
- **Shape variety** (a morphing FAB)
- **Rich color** (vibrant tertiary accent)
- **Emphasized typography** (bold headline)
- **Fluid motion** (spring-based expansion)
- **Container grouping** (content organized in surface containers)

---

## Research Backing

These tactics are based on Google's most researched design system update since 2014:
- **46 independent studies** with **18,000+ participants**
- Key findings:
  1. Expressive designs are preferred by people of **all ages**
  2. Expressive designs score higher on **playfulness, energy, creativity, and friendliness**
  3. Users are **more likely to switch** to products using M3E components
  4. Expressive designs are **easier to use** — participants spotted key UI elements up to
     **4x faster** in expressive screens

Source: [Start building with Material 3 Expressive](https://m3.material.io/blog/building-with-m3-expressive) (May 2025)
