# MD3E Components Catalog

Organized catalog of all Material 3 / Material 3 Expressive components available in
`androidx.compose.material3`. Components marked **[M3E]** are Expressive-specific; some still
require `@ExperimentalMaterial3ExpressiveApi` on the **1.5.0** line — others graduated
non-experimental (Flexible AppBars, FloatingToolbar, ButtonGroup APIs, SearchBarState).

**Version baseline (2026-10-08):** full M3E = `material3` **1.5.0-beta01**; stable **1.4.0**
lacks the full Expressive set. See `references/version-baseline.md` and `references/m3e/components.md`.

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

Key params: `onClick`, `modifier`, `enabled`, `shape`, `colors` (ButtonColors), `elevation`
(ButtonElevation), `border`, `contentPadding`, `interactionSource`.

Default button shape: `RoundedCornerShape(20.dp)` (pill shape).

### Icon Buttons (M3 — stable)
`IconButton`, `IconToggleButton`, `FilledIconButton`, `FilledIconToggleButton`,
`FilledTonalIconButton`, `FilledTonalIconToggleButton`, `OutlinedIconButton`,
`OutlinedIconToggleButton`.

### FABs (M3 — stable)
| Composable | Size | Usage |
|------------|------|-------|
| `FloatingActionButton` | 56dp | Primary screen action |
| `SmallFloatingActionButton` | 40dp | Secondary action |
| `LargeFloatingActionButton` | 96dp | Prominent action |
| `ExtendedFloatingActionButton` | Extended | Action with label |

**[M3E]** `ToggleFloatingActionButton` — FAB that morphs between two states with animation.
Uses `ToggleFloatingActionButtonScope`. Requires `@ExperimentalMaterial3ExpressiveApi`.

**[M3E]** `FloatingActionButtonMenu` — FAB that expands into a vertical menu.
Uses `FloatingActionButtonMenuScope`.

### Segmented Buttons (M3 — stable)
- `SingleChoiceSegmentedButtonRow` + `SegmentedButton` — mutually exclusive options
- `MultiChoiceSegmentedButtonRow` + `SegmentedButton` — multiple toggle options

### Button Group **[M3E]**
- `ButtonGroup` — connected button row with overflow menu and compression animation (APIs stable since 1.5.0-alpha22)
- `ButtonGroupScope` — sealed interface; `weight()` and `animateWidth()` overloads (alpha25+)
- `ButtonGroupMenuState` — overflow menu state
- `ButtonGroupDefaults` — default values

### Split Button **[M3E]**
- `SplitButton` — primary action + overflow trigger (**preferred**; `SplitButtonLayout` deprecated since alpha25)
- `SplitButtonDefaults`, `SplitButtonShapes`

---

## Navigation

### Navigation Bar (M3 — stable)
`NavigationBar` + `NavigationBarItem` — bottom navigation, compact screens (≤599dp), 3-5 destinations.

### Navigation Rail (M3 — stable)
`NavigationRail` + `NavigationRailItem` — side navigation, medium screens (600-839dp).

### Wide Navigation Rail **[M3E]**
`WideNavigationRail` / `ModalWideNavigationRail` — expanded rail for medium/expanded screens.
State: `WideNavigationRailState`. Colors: `WideNavigationRailColors`.
Properties: `ModalWideNavigationRailProperties`.

### Navigation Drawer (M3 — stable)
| Composable | Usage |
|------------|-------|
| `ModalNavigationDrawer` + `ModalDrawerSheet` | Overlay drawer (compact) |
| `PermanentNavigationDrawer` + `PermanentDrawerSheet` | Always-visible (expanded) |
| `DismissibleNavigationDrawer` + `DismissibleDrawerSheet` | Dismissible drawer |
| `NavigationDrawerItem` | Standard drawer item |

### Top App Bar (M3 stable; Flexible [M3E])
| Composable | Height | Notes |
|------------|--------|-------|
| `TopAppBar` | 64dp | Standard top bar |
| `CenterAlignedTopAppBar` | 64dp | Centered title |
| `MediumTopAppBar` | 112dp | Collapsing title |
| `LargeTopAppBar` | 152dp | Full collapsing |
| `MediumFlexibleTopAppBar` **[M3E]** | Flexible | Flexible content |
| `LargeFlexibleTopAppBar` **[M3E]** | Flexible | Flexible content |

Scroll behaviors: `pinnedScrollBehavior`, `enterAlwaysScrollBehavior`,
`enterAlwaysCollapsedScrollBehavior`, `exitUntilCollapsedScrollBehavior`.
Also: `TopAppBarScrollBehavior`, `TopAppBarDefaults`.

### Bottom App Bar (M3 stable; Flexible [M3E])
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
New component for expressive loading states. Part of the 14 M3E components announced May 2025.

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
