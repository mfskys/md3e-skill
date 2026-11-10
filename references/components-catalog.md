# MD3E Components Catalog

Organized catalog of all Material 3 / Material 3 Expressive components available in
`androidx.compose.material3`. Components marked **[M3E]** are Expressive-specific; some still
require `@ExperimentalMaterial3ExpressiveApi` on the **1.5.0** line — others graduated
non-experimental (Flexible AppBars, FloatingToolbar, ButtonGroup APIs, SearchBarState).

**Version baseline (2026-11-10):** full M3E = `material3` **1.5.0-rc01**; stable **1.4.0**
lacks the full Expressive set. See `references/version-baseline.md` and `references/m3e/components.md`.
Signatures in this catalog were re-checked against the `androidx-main` source on 2026-10-23
(API surface re-checked from `api/current.txt` on 2026-11-10).

⚠️ **Entries marked "retired in M3E" are still valid composables but are no longer recommended by
the Expressive design language.** Picking one for an Expressive target produces M3-looking UI.
Summary table with replacements: `SKILL.md` → "Deprecated in M3E".

For full API signatures, search `references/compose-api-full.md` with the component name.

---

## Buttons

### Common Buttons (M3 — stable)
| Composable | Emphasis | Container Color | Usage |
|------------|----------|----------------|-------|
| `Button` | High (filled) | `primary` | Primary actions |
| `FilledTonalButton` | Medium (filled tonal) | `secondaryContainer` | Secondary actions |
| `ElevatedButton` | Medium (elevated) | `surface` + elevation | Secondary with shadow |
| `OutlinedButton` | Low (outlined) | `surface` + border | Important but not primary |
| `TextButton` | Lowest (text) | transparent | Low-emphasis, text links |

Key params: `onClick`, `modifier`, `enabled`, `shape` **或** `shapes`（两个重载，后者才有按压形变）,
`colors` (ButtonColors), `elevation` (ButtonElevation), `border`, `contentPadding`, `interactionSource`.

Default shape: `ButtonDefaults.shape` → `CornerFull`（`CircleShape`，真 pill，不是 `RoundedCornerShape(20.dp)`）。
方角用 `ButtonDefaults.squareShape`，圆角随尺寸变化 12/12/16/28/28dp。

**五档尺寸（32/40/56/96/136dp）、形状矩阵、颜色矩阵与完整写法见
`references/recipes/buttons.md`** —— `Button` 没有 `size` 参数，靠 `shapesFor(height)` +
`contentPaddingFor(height)` + `Modifier.heightIn(min = height)` 组合。

### Icon Buttons (M3 — stable)
`IconButton`, `IconToggleButton`, `FilledIconButton`, `FilledIconToggleButton`,
`FilledTonalIconButton`, `FilledTonalIconToggleButton`, `OutlinedIconButton`,
`OutlinedIconToggleButton`.

### FABs (M3 stable; M3E re-based the size scale)
| Composable | Size | Status | Usage |
|------------|------|--------|-------|
| `FloatingActionButton` | 56dp | ✅ 推荐 — 这就是 M3E 说的 "small FAB" | Primary screen action |
| `MediumFloatingActionButton` | 80dp | ✅ **[M3E] 新增** (`@ExperimentalMaterial3ExpressiveApi`) | |
| `LargeFloatingActionButton` | 96dp | ✅ 推荐 | Prominent action |
| `SmallFloatingActionButton` | 40dp | ⚠️ **M3E 不再推荐** | 仅面向 stable M3 的旧代码 |
| `ExtendedFloatingActionButton` | small 56 / medium 80 / large 96 | ⚠️ baseline 56dp 不再推荐，用 small extended FAB | Action with label |

> 命名陷阱：M3E 设计语言里的 "small FAB" 指 **56dp**（即 `FloatingActionButton`），
> 不是 API 里的 `SmallFloatingActionButton`（40dp，已不推荐）。按设计稿选尺寸时认 dp 值，别认 API 名字。

**[M3E]** `ToggleFloatingActionButton` — FAB that morphs between two states with animation.
Uses `ToggleFloatingActionButtonScope`. Requires `@ExperimentalMaterial3ExpressiveApi`.

**[M3E]** `FloatingActionButtonMenu` — FAB that expands into a vertical menu.
Uses `FloatingActionButtonMenuScope`.

### Segmented Buttons (M3 — retired in M3E)
- `SingleChoiceSegmentedButtonRow` + `SegmentedButton` — mutually exclusive options
- `MultiChoiceSegmentedButtonRow` + `SegmentedButton` — multiple toggle options
- ⚠️ **M3E 起官方不再推荐**（`segmented-buttons/overview`: "no longer recommended"）。新代码请用
  connected `ButtonGroup`；仅在面向 stable M3（1.4.0，无 `MaterialExpressiveTheme`）时才保留。

### Button Group **[M3E]**
两个变体，代码形态完全不同（完整写法见 `compose-patterns.md` 第 5 节）：

- **standard** — `ButtonGroup { clickableItem / toggleableItem / customItem }`；按压时自己变宽、
  相邻按钮被压缩（`expandedRatio`，默认 0.15f），放不下自动进溢出菜单（`overflowIndicator` 必填）
- **connected** — `FlowRow` + `ToggleButton` + `ButtonGroupDefaults.connected{Leading,Middle,Trailing}ButtonShapes()`，
  靠负间距 `ConnectedSpaceBetween` 咬合；**这是 SegmentedButton 的官方替代**
- 尺寸：`ToggleButtonSize` 五档（ExtraSmall / Small 默认 / Medium / Large / ExtraLarge）
- 形状：round / square 两套（圆角随尺寸变化 12/12/16/28/28dp，见 `recipes/buttons.md` §2）
- 选择模式：单选 / 多选 / 必选
- 配套：`ButtonGroupScope`（sealed interface）、`ButtonGroupMenuState`（`show()` / `dismiss()`）、
  `ButtonGroupDefaults`（`ExpandedRatio`、`ConnectedSpaceBetween`、`OverflowIndicator`）

### Split Button **[M3E]**
- `SplitButtonLayout(leadingButton, trailingButton, modifier, spacing)` — the only container API;
  there is **no** `SplitButton` composable (source-verified 2026-10-23)
- `SplitButtonDefaults.LeadingButton` / `TrailingButton` (+ `Tonal*`, `Outlined*`, `Elevated*` variants)
- `SplitButtonShapes`, `leadingButtonShapesFor(buttonHeight)`, `trailingButtonShapesFor(buttonHeight)`

---

## Navigation

### Navigation Bar (M3 — baseline retired in M3E)
`NavigationBar` + `NavigationBarItem` — bottom navigation, compact screens (≤599dp), 3-5 destinations.
⚠️ **M3E 不再推荐 baseline navigation bar**（`navigation-bar/overview`）。新代码用 `ShortNavigationBar`。

### Navigation Rail (M3 — baseline retired in M3E)
`NavigationRail` + `NavigationRailItem` — side navigation, medium screens (600-839dp).
⚠️ **M3E 不再推荐 baseline navigation rail**（`navigation-rail/overview`）。新代码用 `WideNavigationRail`。

### Wide Navigation Rail **[M3E]**
`WideNavigationRail` / `ModalWideNavigationRail` — expanded rail for medium/expanded screens.
State: `WideNavigationRailState` (`rememberWideNavigationRailState()`), colors:
`WideNavigationRailColors`, properties: `ModalWideNavigationRailProperties`.

### Short Navigation Bar **[M3E]**
`ShortNavigationBar` + `ShortNavigationBarItem` — compact bottom bar for small/medium width;
`ShortNavigationBarArrangement`, `ShortNavigationBarDefaults`.

### Navigation Drawer (M3 — retired in M3E)
⚠️ **M3E 不再推荐 navigation drawer**（`navigation-drawer/overview`）；官方给的替代是 **expanded
navigation rail**（`WideNavigationRail` / `ModalWideNavigationRail`）。仅在面向 stable M3 时使用下表。

| Composable | Usage |
|------------|-------|
| `ModalNavigationDrawer` + `ModalDrawerSheet` | Overlay drawer (compact) |
| `PermanentNavigationDrawer` + `PermanentDrawerSheet` | Always-visible (expanded) |
| `DismissibleNavigationDrawer` + `DismissibleDrawerSheet` | Dismissible drawer |
| `NavigationDrawerItem` | Standard drawer item |

### Top App Bar (M3 stable; Flexible [M3E])
| Composable | Height | Notes |
|------------|--------|-------|
| `TopAppBar` | 64dp | Standard top bar（仍推荐） |
| `CenterAlignedTopAppBar` | 64dp | Centered title（仍推荐） |
| `MediumTopAppBar` | 112dp | ⚠️ **M3E 不再推荐** → `MediumFlexibleTopAppBar` |
| `LargeTopAppBar` | 152dp | ⚠️ **M3E 不再推荐** → `LargeFlexibleTopAppBar` |
| `MediumFlexibleTopAppBar` **[M3E]** | Flexible | ✅ 替代 medium top app bar |
| `LargeFlexibleTopAppBar` **[M3E]** | Flexible | ✅ 替代 large top app bar |
| `TwoRowsTopAppBar` **[M3E]** | Flexible | 双行标题 + 副标题 |

Scroll behaviors: `pinnedScrollBehavior`, `enterAlwaysScrollBehavior`,
`enterAlwaysCollapsedScrollBehavior`, `exitUntilCollapsedScrollBehavior`.
Also: `TopAppBarScrollBehavior`, `TopAppBarDefaults`.

### Bottom App Bar (M3 — retired in M3E)
⚠️ **M3E 不再推荐 bottom app bar**（`toolbars/overview`）：改用 **docked `HorizontalFloatingToolbar`**，
功能相近但更矮、更贴合表达式视觉。下面两项仅在面向 stable M3 时使用。

- `BottomAppBar` — standard bottom bar with FAB slot
- `FlexibleBottomAppBar` **[M3E]** — flexible arrangement
  - `FlexibleContentPadding`, `FlexibleBottomAppBarHeight`
  - `FlexibleHorizontalArrangement`, `FlexibleFixedHorizontalArrangement`
- State: `BottomAppBarState`, `BottomAppBarScrollBehavior`

### Floating Toolbar **[M3E]**
| Composable | Orientation | Usage |
|------------|-------------|-------|
| `HorizontalFloatingToolbar` | Horizontal | Contextual tools above content |
| `VerticalFloatingToolbar` | Vertical | Contextual tools (side) |

Supporting types: `FloatingToolbarScrollBehavior`, `FloatingToolbarState`,
`FloatingToolbarColors`, `FloatingToolbarExitDirection`, `FloatingToolbarDefaults`,
`FloatingToolbarHorizontalFabPosition`, `FloatingToolbarVerticalFabPosition`.

### App Bar Overflow Containers **[M3E]**
`AppBarRow` / `AppBarColumn` + `clickableItem(icon, label, onClick)` — overflow containers used as
`trailingContent` of floating toolbars (items that don't fit move into an overflow menu).

### Search Bar (prefer slot API on 1.5.0-alpha)
- `SearchBarState` + slot-based `SearchBar` **[M3E]** — stable since **1.5.0-alpha24** (old
  extension / `onExpandedChange` APIs deprecated)
- `ExpandedDockedSearchBarWithGap`, `ExpandedFullScreenContainedSearchBar` — non-experimental alpha23+
- `AppBarWithSearch` **[M3E]** — replaces `TopSearchBar`
- Legacy: `SearchBar`, `DockedSearchBar` (M3); `SearchBarScrollBehavior`, `SearchBarColors`
- `rememberSearchBarWithGapState` (renamed from `rememberWithGapSearchBarState` in alpha18)

---

## Cards & Containers

### Cards (M3 — stable)
| Composable | Style | Usage |
|------------|-------|-------|
| `Card` | Filled | Default card |
| `ElevatedCard` | Elevated | Card with shadow |
| `OutlinedCard` | Outlined | Card with border |

Params: `shape`, `colors` (CardColors), `elevation` (CardElevation), `border`, `onClick`.
Color roles: `containerColor` = surfaceVariant (default) / primaryContainer (selected),
`contentColor` = onSurfaceVariant / onPrimaryContainer.

### Surface (M3 — stable)
`Surface` — backing composable. Params: `modifier`, `shape`, `color`, `contentColor`,
`tonalElevation`, `shadowElevation`, `border`.

### Badge (M3 — stable)
`Badge`, `BadgedBox` — small status indicator.

### Divider (M3 — stable)
`HorizontalDivider`, `VerticalDivider`.

### Carousel (M3 — stable)
`HorizontalMultiBrowseCarousel`, `HorizontalUncontainedCarousel`, `HorizontalCenteredHeroCarousel`
— `CarouselState` (`rememberCarouselState()`), `CarouselDefaults` (`ItemSpacing`,
`ContentPadding`, `MediumMotionScheme`).
Since **beta01** the centered-hero carousel uses `preferredItemWidth` (was `maxItemWidth`).
布局选择与规则见 `recipes/carousel.md`。

### Side Sheet (M3 规范有 — **Compose 无对应 API**)
官方规范里 side sheet 有 standard / modal 两种（实现细节见 `recipes/containers.md`）。
但 `androidx.compose.material3` 的 API 清单里**没有 `SideSheet` / `ModalSideSheet`**
（2026-11-10 核对 `api/current.txt`）—— 不要凭空写 `SideSheet(...)`。
宽屏侧边场景优先用 `WideNavigationRail` / `ModalWideNavigationRail`；确实需要可拖拽面板时
用 `ModalBottomSheet` 并按需换布局方向，或自己基于 `Surface` + 手势实现。

---

## Input & Selection

### Text Fields (M3 stable; Expressive [M3E])
| Composable | Style | Usage |
|------------|-------|-------|
| `TextField` | Filled | Standard input |
| `OutlinedTextField` | Outlined | Input with border |

Params: `value`/`state`, `onValueChange`, `label`, `placeholder`, `leadingIcon`,
`trailingIcon`, `isError`, `enabled`, `shape`, `colors` (TextFieldColors),
`keyboardOptions`, `interactionSource`, `contentPadding`.

**[M3E]** Expressive styles: `TextFieldDefaults.roundedShape`, `tonalColors()`,
`OutlinedTextFieldDefaults.roundedShape`, `tonalColors()`. New label positions: `Inside`,
`Cutout`. New padding: `contentPaddingWithLabel()`, `contentPaddingWithoutLabel()`.

### Checkbox (M3 — stable)
`Checkbox`, `TriStateCheckbox`. Colors: `CheckboxColors`.

### Radio Button (M3 — stable)
`RadioButton`. Colors: `RadioButtonColors`.

### Switch (M3 — stable)
`Switch`. Colors: `SwitchColors`.

### Slider (M3 — stable)
`Slider`, `RangeSlider`. Colors: `SliderColors`.

### Chips (M3 — stable)
| Composable | Type |
|------------|------|
| `AssistChip` / `ElevatedAssistChip` | Assist |
| `FilterChip` / `ElevatedFilterChip` | Filter (toggle) |
| `InputChip` | Input (tags) |
| `SuggestionChip` / `ElevatedSuggestionChip` | Suggestion |

Colors: `ChipColors`, `SelectableChipColors`. Elevation: `ChipElevation`,
`SelectableChipElevation`. Shapes: `ChipShapes`.

### Scroll Field **[M3E]**
`ScrollField` + `rememberScrollFieldState(itemCount, index)` — wheel-style picker input
(used by the Expressive time picker).

### Date/Time Pickers (M3 stable; Expressive TimePicker [M3E])
`DatePicker`, `DatePickerDialog`, `DateRangePicker`, `TimePicker`, `TimeInput`.
State: `DatePickerState`, `DateRangePickerState`, `TimePickerState`.
Colors: `DatePickerColors`, `TimePickerColors`.
Formatter: `DatePickerFormatter`. Selectable dates: `SelectableDates`.
**[M3E]** Expressive TimePicker with redesigned styling.

### Dropdown Menus (M3 — stable)
`DropdownMenu` + `DropdownMenuItem`, `ExposedDropdownMenuBox`.
State: `ExposedDropdownMenuAnchorType`, `ExposedDropdownMenuBoxScope`.

### List Items (M3 stable; Expressive [M3E])
`ListItem` — standard list item. Colors: `ListItemColors`.
**[M3E]** Non-interactive expressive variants.

---

## Feedback & Indicators

### Progress Indicators (M3 — stable)
`LinearProgressIndicator`, `CircularProgressIndicator`.

### Loading Indicator **[M3E]**
- `LoadingIndicator` / `ContainedLoadingIndicator` — no-arg overloads are indeterminate;
  `progress: () -> Float` makes them determinate. Requires `@ExperimentalMaterial3ExpressiveApi`.
- `LinearWavyProgressIndicator` / `CircularWavyProgressIndicator` — wavy track styles
  (function names are `*WavyProgressIndicator`, not `WavyProgressIndicator`).
- `PullToRefreshDefaults.LoadingIndicator(state, isRefreshing)` for pull-to-refresh.

### Snackbar (M3 — stable)
`Snackbar`, `SnackbarHost` + `SnackbarHostState`.
Interfaces: `SnackbarData`, `SnackbarVisuals`.

### Dialog (M3 — stable)
`AlertDialog`.

### Bottom Sheet (M3 — stable)
`ModalBottomSheet`, `BottomSheetScaffold`.
State: `BottomSheetScaffoldState`, `rememberBottomSheetState` (unified API).

### Tooltip (M3 — stable)
`PlainTooltip`, `RichTooltip`, `TooltipBox` + `TooltipState`.
Scope: `TooltipScope`. Shape: `DefaultTooltipCaretShape`.

### Swipe to Dismiss (M3 — stable)
`SwipeToDismissBox` + `SwipeToDismissBoxState`.

---

## Layout & Scaffold

### Scaffold (M3 — stable)
`Scaffold` — top-level layout with slots for topBar, bottomBar, FAB, snackbarHost, content.
Params: `topBar`, `bottomBar`, `floatingActionButton`, `floatingActionButtonPosition`
(FabPosition), `snackbarHost`, `contentWindowInsets`, `contentColor`, `containerColor`.

### Drag Handle **[M3E]**
`DragHandleColors`, `DragHandleShapes`, `DragHandleSizes` — for expressive drag handles.

---

## Window Size Classes (M3 — stable)

`WindowSizeClass`, `WindowWidthSizeClass`, `WindowHeightSizeClass`.
`calculateWindowSizeClass(activity)` — calculates size class for adaptive layouts.

| Width Size Class | dp Range | Navigation |
|-----------------|----------|------------|
| Compact | 0–599dp | NavigationBar |
| Medium | 600–839dp | NavigationRail / WideNavigationRail |
| Expanded | 840dp+ | WideNavigationRail / PermanentNavigationDrawer |

---

## Icons & Text

- `Icon` — Material icon from `Icons.Default.*` / `Icons.Outlined.*` / `Icons.Rounded.*`
- `Text` — Material text with auto-size support (`TextAutoSize`)
- `androidx.compose.material.icons` package — full Material icon set

---

## Adaptive Layout (M3 — stable)

`androidx.compose.material3.adaptive` package:
- `PaneScaffoldScope`, `ThreePaneScaffoldRole`, `PaneAdaptedValue`
- `ThreePaneScaffoldValue`, `calculateThreePaneScaffoldValue`
- `AnimatedPane` — animated pane with shape support
- `ThreePaneScaffoldAdaptStrategies` — adaptation strategies for list-detail layouts
