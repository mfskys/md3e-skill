# M3E Component Inventory

Verified: **2026-10-08**
Source: Compose Material 3 official release notes (https://developer.android.com/jetpack/androidx/releases/compose-material3,
page updated 2026-10-07) ✅

**How to read**: `alphaNN` in parentheses is the version where the API **graduated from experimental**.
`1.4.0` is the current **stable line**; `1.5.0-betaNN` is the **1.5.0 line**.
To judge availability, first check which line it is on.

---

> 📌 **Version policy**: this project **adopts the newest versions (including Alpha/Beta/RC)** —
> `material3 = 1.5.0-beta01` — so all "1.5.0 line" components below **are in scope**.
> See `../version-baseline.md`. §11 adoption advice already reflects this.

## 1. Buttons & Actions

| Component | Status | Notes |
| --- | --- | --- |
| `ToggleButton` family | Stable since 1.4.0-alpha19 | M3E toggle button |
| `FilledTonalToggleButton` | Renamed in alpha25 | Formerly `TonalToggleButton` |
| `ButtonGroup` | Stable since 1.4.0-alpha22 | Button group; from alpha25 `ButtonGroupScope` is a **sealed interface**; `Modifier.animateWidth` split into two overloads |
| `SplitButton` | Non-experimental since 1.4.0-alpha20 | From alpha25 **`SplitButtonLayout` deprecated** — use `SplitButton` only |
| FAB and **FAB Menu** | Graduated 1.4.0-alpha19 | Expanded FAB menu is a signature M3E interaction |
| `ExtendedFloatingActionButton` / `Button` / `TextButton` | Stable | Three decreasing emphasis levels (classic M3) |

---

## 2. App Bars & Toolbars

| Component | Status | Use |
| --- | --- | --- |
| `TopAppBar` | Stable | Classic small |
| `MediumFlexibleTopAppBar` | Graduated 1.5.0-alpha23 | Medium + collapsible (flexible) |
| `LargeTopAppBar` | Stable | Large |
| `LargeFlexibleTopAppBar` | Graduated 1.5.0-alpha23 | Large + collapsible |
| `TwoRowsTopAppBar` | Graduated 1.5.0-alpha23 | Two rows |
| `FlexibleBottomAppBar` | Graduated 1.5.0-alpha23 | Collapsible bottom bar |
| `FloatingToolbar` | Non-experimental 1.5.0-alpha22 | Floating toolbar |
| `AppBarWithSearch` | Added in alpha02 | **Replaces `TopSearchBar`** |

> 1.5.0-alpha27: old overloads of `pinnedScrollBehavior` / `enterAlwaysScrollBehavior` in
> `TopAppBarDefaults` **removed**; `LocalMotionScheme` removed — use `MaterialTheme.motionScheme`.

---

## 3. Search

| Component | Status |
| --- | --- |
| `SearchBarState` + slot-based `SearchBar` API | **Stable in 1.5.0-alpha24**; old extension / `onExpandedChange` APIs deprecated |
| `ExpandedDockedSearchBarWithGap` | Non-experimental 1.5.0-alpha23 |
| `ExpandedFullScreenContainedSearchBar` | Non-experimental 1.5.0-alpha23 |
| `rememberWithGapSearchBarState` | Renamed `rememberSearchBarWithGapState` in alpha18 |

---

## 4. Time & Pickers

| Component | Status |
| --- | --- |
| Expressive `TimePicker` scroll variants | Added alpha03; scroll variants in alpha24 |
| `VibrantTimePickerDialog` | Renamed from `RichTimePickerDialog` in alpha27; `richColors` → `vibrantColors` |
| `Slider` / `RangeSlider` | alpha28: **stateless overloads deprecated** — use stateful versions; `RangeSliderState.activeRangeStart/End` → `startValue/endValue` |

---

## 5. Menus

| Component | Status |
| --- | --- |
| `SelectableDropdownMenuItem` / `CheckableDropdownMenuItem` | Added 1.5.0-alpha27 |
| `MenuDefaults.itemVibrantColors()` | Provides vibrant `MenuItemColors` |
| Expressive menu APIs | Improved since alpha19; **old experimental `DropdownMenuItem` removed** |
| `ExposedDropdownMenu` | alpha26: moved from member to **extension function** on `ExposedDropdownMenuBoxScope` — update imports |

---

## 6. List Items

| Component | Status |
| --- | --- |
| Expressive `ListItem` | Supports interactive and segmented styles; `ListItemColors` fields added alpha11 |
| Non-interactive variants | Added alpha23 (standard / segmented); **old non-expressive versions deprecated** |

---

## 7. Containers & Overlays

| Component | Status |
| --- | --- |
| Multi-aspect **Carousel** | Official in alpha10; simplified to global `carouselParallaxScrollEffect` modifier in alpha28 |
| **Scrim** | Added alpha15, for modal components |
| Standalone static **Sheet** | Added alpha15 |
| `ModalBottomSheet` | alpha20: `rememberModalBottomSheetState` / `rememberStandardBottomSheetState` **deprecated** — unified `rememberBottomSheetState`; old experimental APIs removed alpha09 |
| `material3-ripple` | New library alpha24: **embedded focus ring instead of opacity layers** |

---

## 8. Classic M3 components (stable baseline)

`Scaffold`, `Surface`, `Card` (incl. `CardDefaults.cardColors/cardElevation`),
`Button` / `OutlinedButton` / `TextButton` / `IconButton` / `FilledIconButton`,
`Chip` (`AssistChip` / `FilterChip` / `InputChip`), `Checkbox` / `RadioButton` / `Switch`,
`Slider`, `Divider`, `Badge`, `Snackbar`, `AlertDialog`,
`DropdownMenu`, `ExposedDropdownMenuBox`, `ModalBottomSheet`,
`NavigationBar` / `NavigationRail` / `NavigationDrawer` / `PermanentNavigationDrawer`,
`PullToRefreshBox` / `Modifier.pullToRefresh`, `LinearProgressIndicator` / `CircularProgressIndicator`.

> ⚠️ PullToRefresh was overhauled in **1.3.0**: `PullToRefreshState` simplified (fraction, not `Dp`),
> `isRefreshing` user-controlled, nested scroll split into `PullToRefreshBox` or `Modifier.pullToRefresh`.

---

## 9. Adaptive components (core of this project's foundation)

| Component | Library | Notes |
| --- | --- | --- |
| `NavigationSuiteScaffold` | `material3-adaptive-navigation-suite` | Switches form by window size. ⚠️ **From 1.5.0-alpha28 it actually renders new components**: Compact → `ShortNavigationBarCompact` (`ShortNavigationBar` vertical items); others → `WideNavigationRailCollapsed`; old `NavigationBar`/`NavigationRail`/`NavigationDrawer` types are "not recommended". See `../m3-content/foundations/layout/scaffold/overview.md` |
| `ListDetailPaneScaffold` / `NavigableListDetailPaneScaffold` | `adaptive-layout` / `adaptive-navigation` | List-detail canonical layout |
| `SupportingPaneScaffold` / `NavigableSupportingPaneScaffold` | same | Main + supporting panes |
| `ThreePaneScaffold` abstraction | `adaptive-layout` | Three-pane scaffold (navigator / state / predictive back) |
| `AnimatedPane` | `adaptive-layout` | Default pane animation; shapes supported since 1.4.0-alpha01 |
| `HingeInfo` / `Posture` | `adaptive` | Hinge and device posture (foldables) |

> Adaptive layout specs: `../m3-content/foundations/layout/`.

---

## 10. Quick selection table

| Need | First choice | Notes |
| --- | --- | --- |
| Primary action | `Button` / `FilledTonalButton` | **One** strongest-emphasis button per screen |
| Related action group | `ButtonGroup` | 1.5.0 line |
| Primary + overflow menu | `SplitButton` | Same |
| Top title + scroll collapse | `MediumFlexibleTopAppBar` / `LargeFlexibleTopAppBar` | Decide collapse by window height (see `../m3-content/foundations/layout/breakpoints/overview.md`) |
| Persistent bottom action bar | `FlexibleBottomAppBar` | Easier thumb reach than TopAppBar on small screens |
| Full-screen / side navigation | `NavigationSuiteScaffold` | Do not hand-write three-nav branching |
| Search | slot `SearchBar` + `SearchBarState` | Old APIs deprecated |
| Toggle state (e.g. show hidden files) | `Switch` (settings) / `ToggleButton` (toolbar) | — |
| Contextual actions (multi-select) | contextual top bar + `Scaffold` | Toggle with `AnimatedVisibility` |

---

## 11. Adoption advice (aggressive track)

1. **Use the full 1.5.0-line M3E set** (`material3 = 1.5.0-beta01`):
   ToggleButton / ButtonGroup / SplitButton / FAB Menu / Flexible AppBar /
   slot SearchBar all available — no more "not on stable" gaps.
2. **Confine call sites**: keep M3E components in `ui/expressive/` (or `ui/components/`)
   to absorb 1.5.0-line renames/removals.
3. **Exit plan for every preview dependency**: delete shims when moving to stable;
   mapping in `../version-baseline.md`.
4. **Icons from Material Symbols**: from M3 1.4.0, `material-icons-core` is no longer transitive
   and `androidx.compose.material.icons` is discouraged.
5. **Always read release notes before upgrades**: the 1.5.0 line churns often
   (see `compose-api.en.md` §4).
