# API 索引（官方 package-summary）

> 来源：`developer.android.com/reference/kotlin/androidx/compose/material3/package-summary`
> 抓取 **2026-11-17**，对应 `material3` 1.5.0-rc01 线（该线已于 **2026-11-18** 转为正式稳定版 `1.5.0`，API 无变化）。
>
> 这份文件是**官方 API 总表**：每个条目带 KDoc 原始描述与对应的 m3.material.io 设计页。
> 用途：① 校验 `recipes/` 覆盖度；② 查某个 composable 对应哪份设计规范；
> ③ 上游新增组件时重抓此页即可发现。实现细节不在这里，去 `recipes/`。
>
> ⚠️ 官网 KDoc 里有 5 个设计页链接已失效（站点重构后路径变化），本文件已按
> 2026-11-17 的实际 sitemap 修正：`bottom-app-bar` / `top-app-bar` → `app-bars`，
> `icon-button` → `icon-buttons`，`switch` → `switch/overview`。

## 统计

| 分类 | 条目 |
| --- | --- |
| Composables | 176 |
| Modifiers | 2 |
| Classes | 101 |
| Objects | 67 |
| Interfaces | 30 |
| Enums | 7 |
| Annotations | 2 |
| Type aliases | 1 |
| **合计** | **386** |

## Composables（176）

| API | 说明 | 设计页 |
| --- | --- | --- |
| `AlertDialog` | Basic alert dialog dialog | /components/dialogs/overview |
| `AppBarColumn` | An AppBarColumn arranges its children in a vertical sequence, and if any children overflow the constraints, an overflow indicator is displayed. | — |
| `AppBarOverflowIndicator` | Default overflow indicator for an AppBarRow and AppBarColumn. | — |
| `AppBarRow` | An AppBarRow arranges its children in a horizontal sequence, and if any children overflow the constraints, an overflow indicator is displayed. | — |
| `AppBarWithSearch` | Material Design search | /components/search/overview |
| `AssistChip` | Material Design assist chip | /components/chips/overview |
| `Badge` | A badge represents dynamic information such as a number of pending requests in a navigation bar. | — |
| `BadgedBox` | Material Design badge box. | — |
| `BasicAlertDialog` | Basic alert dialog dialog | /components/dialogs/overview |
| `BottomAppBar` | Material Design bottom app bar | /components/app-bars/overview |
| `BottomSheet` | Material Design bottom sheet | /components/bottom-sheets/overview |
| `BottomSheetScaffold` | Material Design standard bottom sheet scaffold | /components/bottom-sheets/overview |
| `Button` | Material Design button | /components/buttons/overview |
| `ButtonGroup` | A layout composable that places its children in a horizontal sequence. | — |
| `Card` | Material Design filled card | /components/cards/overview |
| `CenterAlignedTopAppBar` | Material Design center-aligned small top app bar | /components/app-bars/overview |
| `CheckableDropdownMenuItem` | Material Design dropdown menu | /components/menus/overview |
| `Checkbox` | Material Design checkbox | /components/checkbox/overview |
| `CircularProgressIndicator` | Material Design determinate circular progress indicator | /components/progress-indicators/overview |
| `CircularWavyProgressIndicator` | Material Design indeterminate circular progress indicator | /components/progress-indicators/overview |
| `ContainedLoadingIndicator` | A Material Design contained loading indicator. | — |
| `contentColorFor` | The Material color system contains pairs of colors that are typically used for the background and content color inside a component. | — |
| `DatePicker` | Material Design date picker | /components/date-pickers/overview |
| `DatePickerDialog` | Material Design date picker dialog | /components/date-pickers/overview |
| `DateRangePicker` | Material Design date range picker | /components/date-pickers/overview |
| `DismissibleDrawerSheet` | Content inside of a dismissible navigation drawer. | — |
| `DismissibleNavigationDrawer` | Material Design navigation drawer | /components/navigation-drawer/overview |
| `Divider` | — | — |
| `DockedSearchBar` | Material Design search | /components/search/overview |
| `DropdownMenu` | Material Design dropdown menu | /components/menus/overview |
| `DropdownMenuGroup` | Material Design dropdown menu | /components/menus/overview |
| `DropdownMenuItem` | Material Design dropdown menu | /components/menus/overview |
| `DropdownMenuPopup` | Material Design dropdown menu | /components/menus/overview |
| `ElevatedAssistChip` | Material Design elevated assist chip | /components/chips/overview |
| `ElevatedButton` | Material Design elevated button | /components/buttons/overview |
| `ElevatedCard` | Material Design elevated card | /components/cards/overview |
| `ElevatedFilterChip` | Material Design elevated filter chip | /components/chips/overview |
| `ElevatedSuggestionChip` | Material Design elevated suggestion chip | /components/chips/overview |
| `ElevatedToggleButton` | Material Design toggle button | /components/buttons/overview |
| `ExpandedDockedSearchBar` | ExpandedDockedSearchBar represents a search bar that is currently expanding or in the expanded state, showing search results. | — |
| `ExpandedDockedSearchBarWithGap` | ExpandedDockedSearchBarWithGap represents a search bar that is currently expanding or in the expanded state, showing search results. | — |
| `ExpandedFullScreenContainedSearchBar` | ExpandedFullScreenContainedSearchBar represents a search bar that is currently expanding or in the expanded state, showing search results, preserving the collapsed shape of the inputField without divider. | — |
| `ExpandedFullScreenSearchBar` | ExpandedFullScreenSearchBar represents a search bar that is currently expanding or in the expanded state, showing search results. | — |
| `ExposedDropdownMenu` | The composable defining the exposed dropdown menu popup. | — |
| `ExposedDropdownMenuBox` | Material Design exposed dropdown menu | /components/menus/overview |
| `ExtendedFloatingActionButton` | Material Design extended floating action button | /components/extended-fab/overview |
| `FilledIconButton` | Material Design filled icon button | /components/icon-buttons/overview |
| `FilledIconToggleButton` | Material Design filled icon button | /components/icon-buttons/overview |
| `FilledTonalButton` | Material Design filled tonal button | /components/buttons/overview |
| `FilledTonalIconButton` | Material Design filled tonal icon button | /components/icon-buttons/overview |
| `FilledTonalIconToggleButton` | Material Design filled tonal icon toggle button | /components/icon-buttons/overview |
| `FilledTonalToggleButton` | Material Design toggle button | /components/buttons/overview |
| `FilterChip` | Material Design filter chip | /components/chips/overview |
| `FlexibleBottomAppBar` | Material Design flexible bottom app bar | /components/app-bars/overview |
| `FloatingActionButton` | Material Design floating action button | /components/floating-action-button/overview |
| `FloatingActionButtonMenu` | FAB Menus should be used in conjunction with a ToggleFloatingActionButton to provide additional choices to the user after clicking a FAB. | — |
| `FloatingActionButtonMenuItem` | FAB Menu Items should be used within a FloatingActionButtonMenu to provide additional choices to the user after clicking a FAB. | — |
| `HorizontalDivider` | Material Design divider | /components/divider/overview |
| `HorizontalFloatingToolbar` | A horizontal floating toolbar displays navigation and key actions in a Row. | — |
| `Icon` | A Material Design icon component that draws bitmap using tint, with a default value of LocalContentColor. | — |
| `IconButton` | Material Design standard icon button | /components/icon-buttons/overview |
| `IconToggleButton` | Material Design standard icon toggle button | /components/icon-buttons/overview |
| `InputChip` | Material Design input chip | /components/chips/overview |
| `Label` | Label component that will append a label to content. | — |
| `LargeExtendedFloatingActionButton` | Material Design large extended floating action button | /components/extended-fab/overview |
| `LargeFlexibleTopAppBar` | Material Design large flexible top app bar | /components/app-bars/overview |
| `LargeFloatingActionButton` | Material Design large floating action button | /components/floating-action-button/overview |
| `LargeTopAppBar` | Material Design large top app bar | /components/app-bars/overview |
| `LeadingIconTab` | Material Design tab | /components/tabs/overview |
| `LinearProgressIndicator` | Material Design indeterminate linear progress indicator | /components/progress-indicators/overview |
| `LinearWavyProgressIndicator` | Material Design indeterminate linear wavy progress indicator | /components/progress-indicators/overview |
| `ListItem` | Material Design list item | /components/lists/overview |
| `LoadingIndicator` | A Material Design loading indicator. | — |
| `MaterialExpressiveTheme` | Material Expressive Theming refers to the customization of your Material Design app to better reflect your product’s brand. | — |
| `MaterialTheme` | Material Theming refers to the customization of your Material Design app to better reflect your product’s brand. | — |
| `MediumExtendedFloatingActionButton` | Material Design medium extended floating action button | /components/extended-fab/overview |
| `MediumFlexibleTopAppBar` | Material Design medium flexible top app bar | /components/app-bars/overview |
| `MediumFloatingActionButton` | Material Design medium floating action button | /components/floating-action-button/overview |
| `MediumTopAppBar` | Material Design medium top app bar | /components/app-bars/overview |
| `ModalBottomSheet` | Material Design modal bottom sheet | /components/bottom-sheets/overview |
| `ModalDrawerSheet` | Content inside of a modal navigation drawer. | — |
| `ModalNavigationDrawer` | Material Design navigation drawer | /components/navigation-drawer/overview |
| `ModalWideNavigationRail` | Material design modal wide navigation rail. | — |
| `MultiChoiceSegmentedButtonRow` | Material Design segmented button | /components/segmented-buttons/overview |
| `NavigationBar` | Material Design bottom navigation bar | /components/navigation-bar/overview |
| `NavigationBarItem` | Material Design navigation bar item. | — |
| `NavigationDrawerItem` | Material Design navigation drawer item. | — |
| `NavigationRail` | Material Design bottom navigation rail | /components/navigation-rail/overview |
| `NavigationRailItem` | Material Design navigation rail item. | — |
| `nonInteractiveScrollbar` | A visual-only scrollbar that represents the current scroll position of a scrolling component. | — |
| `OutlinedButton` | Material Design outlined button | /components/buttons/overview |
| `OutlinedCard` | Material Design outlined card | /components/cards/overview |
| `OutlinedIconButton` | Material Design outlined icon button | /components/icon-buttons/overview |
| `OutlinedIconToggleButton` | Material Design outlined icon toggle button | /components/icon-buttons/overview |
| `OutlinedSecureTextField` | Material Design outlined text field for secure content | /components/text-fields/overview |
| `OutlinedTextField` | Material Design outlined text field | /components/text-fields/overview |
| `OutlinedToggleButton` | Material Design toggle button | /components/buttons/overview |
| `PermanentDrawerSheet` | Content inside of a permanent navigation drawer. | — |
| `PermanentNavigationDrawer` | Material Design navigation permanent drawer | /components/navigation-drawer/overview |
| `PlainTooltip` | Plain tooltip that provides a descriptive message. | — |
| `PrimaryScrollableTabRow` | Material Design scrollable primary tabs | /components/tabs/overview |
| `PrimaryTabRow` | Material Design fixed primary tabs | /components/tabs/overview |
| `ProvideTextStyle` | This function is used to set the current value of LocalTextStyle, merging the given style with the current style values for any missing attributes. | — |
| `RadioButton` | Material Design radio button | /components/radio-button/overview |
| `RangeSlider` | Material Design range slider | /components/sliders/overview |
| `rememberBottomAppBarState` | Creates a BottomAppBarState that is remembered across compositions. | — |
| `rememberBottomSheetScaffoldState` | Create and remember a BottomSheetScaffoldState. | — |
| `rememberBottomSheetState` | Create and remember a SheetState for BottomSheet, ModalBottomSheet, or BottomSheetScaffold. | — |
| `rememberContainedSearchBarState` | Create and remember a SearchBarState to use in conjunction with ExpandedFullScreenContainedSearchBar. | — |
| `rememberDatePickerState` | — | — |
| `rememberDateRangePickerState` | — | — |
| `rememberDrawerState` | Create and remember a DrawerState. | — |
| `rememberFloatingToolbarState` | Creates a FloatingToolbarState that is remembered across compositions. | — |
| `rememberModalBottomSheetState` | Create and remember a SheetState for ModalBottomSheet. | — |
| `rememberRangeSliderState` | Creates a RangeSliderState that is remembered across compositions. | — |
| `rememberScrollFieldState` | Creates and remembers a ScrollFieldState to be used with a ScrollField. | — |
| `rememberSearchBarScrollState` | Creates a SearchBarScrollState that is remembered across compositions. | — |
| `rememberSearchBarState` | Create and remember a SearchBarState. | — |
| `rememberSearchBarWithGapState` | Create and remember a SearchBarState to use in conjunction with ExpandedDockedSearchBarWithGap. | — |
| `rememberSliderState` | Creates a SliderState that is remembered across compositions. | — |
| `rememberStandardBottomSheetState` | Create and remember a SheetState for BottomSheetScaffold. | — |
| `rememberSwipeToDismissBoxState` | Create and remember a SwipeToDismissBoxState. | — |
| `rememberTimePickerState` | Creates a TimePickerState for a time picker that is remembered across compositions and configuration changes. | — |
| `rememberTooltipState` | Create and remember the default TooltipState for TooltipBox. | — |
| `rememberTopAppBarState` | Creates a TopAppBarState that is remembered across compositions. | — |
| `rememberWideNavigationRailState` | Create and remember a WideNavigationRailState. | — |
| `RichTooltip` | Rich text tooltip that allows the user to pass in a title, text, and action. | — |
| `Scaffold` | Material Design layout | /foundations/layout/understanding-layout/ |
| `Scrim` | A Scrim that obscures content behind a modal surface. | — |
| `ScrollableTabRow` | Material Design tabs | /components/tabs/overview |
| `ScrollField` | ScrollField's can be used to provide a more interactive way to select a time or other numerical value. | — |
| `SearchBar` | Material Design search | /components/search/overview |
| `SecondaryScrollableTabRow` | Material Design scrollable secondary tabs | /components/tabs/overview |
| `SecondaryTabRow` | Material Design fixed secondary tabs | /components/tabs/overview |
| `SecureTextField` | Material Design filled text field for secure content | /components/text-fields/overview |
| `SegmentedButton` | Material Design segmented Button | /components/segmented-buttons/overview |
| `SegmentedListItem` | Material Design segmented list item | /components/lists/overview |
| `SelectableDropdownMenuItem` | Material Design dropdown menu | /components/menus/overview |
| `ShortNavigationBar` | Material Design short navigation bar. | — |
| `ShortNavigationBarItem` | Material Design short navigation bar item. | — |
| `SingleChoiceSegmentedButtonRow` | Material Design segmented button | /components/segmented-buttons/overview |
| `Slider` | Material Design slider | /components/sliders/overview |
| `SmallExtendedFloatingActionButton` | Material Design small extended floating action button | /components/extended-fab/overview |
| `SmallFloatingActionButton` | Material Design small floating action button | /components/floating-action-button/overview |
| `Snackbar` | Material Design snackbar | /components/snackbar/overview |
| `SnackbarHost` | Host for Snackbars to be used in Scaffold to properly show, hide and dismiss items based on Material specification and the hostState. | — |
| `SplitButtonLayout` | A SplitButtonLayout lets users define a button group consisting of 2 buttons. | — |
| `SuggestionChip` | Material Design suggestion chip | /components/chips/overview |
| `Surface` | Material surface is the central metaphor in material design. | — |
| `SwipeToDismissBox` | A composable that can be dismissed by swiping left or right. | — |
| `Switch` | Material Design switch | /components/switch/overview |
| `Tab` | Material Design tab | /components/tabs/overview |
| `TabRow` | Material Design tabs | /components/tabs/overview |
| `Text` | High level element that displays text and provides semantics / accessibility information. | — |
| `TextButton` | Material Design text button | /components/buttons/overview |
| `TextField` | Material Design filled text field | /components/text-fields/overview |
| `TimeInput` | Time pickers help users select and set a specific time. | — |
| `TimePicker` | Material Design time picker | /components/time-pickers/overview |
| `TimePickerDialog` | Material Design time picker dialog | /components/time-pickers/overview |
| `TimeScroll` | Time pickers help users select and set a specific time. | — |
| `ToggleButton` | Material Design toggle button | /components/buttons/overview |
| `ToggleFloatingActionButton` | Toggleable FAB supports animating its container size, corner radius, and color when it is toggled, and should be used in conjunction with a FloatingActionButtonMenu to provide additional choices to the user after clicking the FAB. | — |
| `TooltipBox` | Material TooltipBox that wraps a composable with a tooltip. | — |
| `TopAppBar` | Material Design small top app bar | /components/app-bars/overview |
| `toPath` | Returns a Path that is remembered across compositions for this RoundedPolygon. | — |
| `TopSearchBar` | Material Design search | /components/search/overview |
| `toShape` | Returns a Shape that is remembered across compositions for this RoundedPolygon. | — |
| `TriStateCheckbox` | Material Design checkbox | /components/checkbox/guidelines |
| `TwoRowsTopAppBar` | A basic two-rows Material Design top app bar. | — |
| `VerticalDivider` | Material Design divider | /components/divider/overview |
| `VerticalDragHandle` | Material Design drag handle | /foundations/layout/understanding-layout/parts-of-layout |
| `VerticalFloatingToolbar` | A vertical floating toolbar displays navigation and key actions in a Column. | — |
| `VerticalSlider` | Material Design slider | /components/sliders/overview |
| `VibrantTimePickerDialog` | Material Design vibrant time picker dialog | /components/time-pickers/overview |
| `WideNavigationRail` | Material design wide navigation rail. | — |
| `WideNavigationRailItem` | Material Design wide navigation rail item. | — |

## Modifiers（2）

| API | 说明 |
| --- | --- |
| `animateFloatingActionButton` | Apply this modifier to a FloatingActionButton to show or hide it with an animation, typically based on the app's main content scrolling. |
| `minimumInteractiveComponentSize` | Reserves at least 48.dp in size to disambiguate touch interactions if the element would measure smaller. |

## Classes（101）

| API | 说明 |
| --- | --- |
| `AppBarMenuState` | State class for the overflow menu in AppBarRow and AppBarColumn. |
| `AppBarWithSearchColors` | Represents the colors used by an AppBarWithSearch. |
| `BottomSheetScaffoldState` | State of the BottomSheetScaffold composable. |
| `ButtonColors` | Represents the container and content colors used in a button in different states. |
| `ButtonElevation` | Represents the elevation for a button in different states. |
| `ButtonGroupMenuState` | State class for the overflow menu in ButtonGroup. |
| `ButtonShapes` | The shapes that will be used in buttons. |
| `CalendarLocale` | Represents a Locale for the calendar. |
| `CardColors` | Represents the container and content colors used in a card in different states. |
| `CardElevation` | Represents the elevation for a card in different states. |
| `CheckboxColors` | Represents the colors used by the three different sections (checkmark, box, and border) of a Checkbox or TriStateCheckbox in different states. |
| `ChipBorder` | This class is deprecated. Maintained for binary compatibility. |
| `ChipColors` | Represents the container and content colors used in a clickable chip in different states. |
| `ChipElevation` | Represents the elevation used in a selectable chip in different states. |
| `ChipShapes` | The shapes that will be used in chips. |
| `ColorScheme` | A color scheme holds all the named color parameters for a MaterialTheme. |
| `DatePickerColors` | Represents the colors used by the date picker. |
| `DefaultTooltipCaretShape` | Default Shape of the caret used by tooltips. |
| `DisplayMode` | Represents the different modes that a date picker can be at. |
| `DragHandleColors` | Specifies the colors that will be used in a drag handle in different states. |
| `DragHandleShapes` | Specifies the shapes that will be used in a drag handle in different states. |
| `DragHandleSizes` | Specifies the sizes that will be used in a drag handle in different states. |
| `DrawerState` | State of the ModalNavigationDrawer and DismissibleNavigationDrawer composable. |
| `ExposedDropdownMenuAnchorType` | The type of anchor for an exposed dropdown menu. |
| `ExposedDropdownMenuBoxScope` | Scope for ExposedDropdownMenuBox. |
| `FabPosition` | The possible positions for a FloatingActionButton attached to a Scaffold. |
| `FloatingActionButtonElevation` | Represents the tonal and shadow elevation for a floating action button in different states. |
| `FloatingToolbarColors` | Represents the container and content colors used in the various floating toolbars. |
| `FloatingToolbarExitDirection` | The possible directions for a HorizontalFloatingToolbar or VerticalFloatingToolbar, used to determine the exit direction when a FloatingToolbarScrollBehavior is attached. |
| `FloatingToolbarHorizontalFabPosition` | The possible positions for a FloatingActionButton attached to a HorizontalFloatingToolbar |
| `FloatingToolbarVerticalFabPosition` | The possible positions for a FloatingActionButton attached to a VerticalFloatingToolbar |
| `IconButtonColors` | Represents the container and content colors used in an icon button in different states. |
| `IconButtonDefaults.IconButtonWidthOption` | Class that describes the different supported widths of the IconButton. |
| `IconButtonShapes` | The shapes that will be used in icon buttons. |
| `IconToggleButtonColors` | Represents the container and content colors used in a toggleable icon button in different states. |
| `IconToggleButtonShapes` | The shapes that will be used in toggle buttons. |
| `ListItemColors` | Represents the colors of a list item in different states. |
| `ListItemElevation` | Represents the elevation of a list item in different states. |
| `ListItemShapes` | Represents the shapes of a list item in different states. |
| `MaterialShapes` | Holds predefined Material Design shapes as RoundedPolygons that can be used at various components as they are, or as part of a Morph. |
| `MaterialTheme.Values` | Material 3 contains different theme subsystems to allow visual customization across a UI hierarchy. |
| `MenuAnchorPosition` | Class that determines the position of a menu relative to its anchor. |
| `MenuGroupShapes` | Represents the shapes used for a DropdownMenuGroup. |
| `MenuItemColors` | Represents the text and icon colors used in a menu item at different states. |
| `MenuItemShapes` | Represents the shapes used for a DropdownMenuItem in its various states. |
| `ModalBottomSheetProperties` | Properties used to customize the behavior of a ModalBottomSheet. |
| `ModalWideNavigationRailProperties` | Properties used to customize the behavior of a ModalWideNavigationRail. |
| `NavigationBarItemColors` | Represents the colors of the various elements of a navigation item. |
| `NavigationItemColors` | Represents the colors of the various elements of a navigation item. |
| `NavigationItemIconPosition` | Class that describes the different supported icon positions of the navigation item. |
| `NavigationRailItemColors` | Represents the colors of the various elements of a navigation item. |
| `RadioButtonColors` | Represents the color used by a RadioButton in different states. |
| `RangeSliderState` | Class that holds information about RangeSlider's active range. |
| `RichTooltipColors` | — |
| `RippleConfiguration` | Local per-ripple configuration for the ripple appearance, provided using LocalRippleConfiguration. |
| `RippleConfiguration.Focus` | The configuration options for the focus indication for RippleConfiguration. |
| `RippleConfiguration.Focus.InsetRing` | An inset ring focus indication. |
| `RippleThemeConfiguration` | The overall ripple theme in use by all built-in components and ripple. |
| `RippleThemeConfiguration.Focus` | The configuration options for the focus indication for RippleThemeConfiguration. |
| `RippleThemeConfiguration.Focus.InsetRing` | An inset ring focus indication. |
| `ScrollFieldColors` | Represents the colors used by a ScrollField in different states. |
| `ScrollFieldState` | A state object that can be hoisted to observe and control the scrolling behavior of a ScrollField. |
| `SearchBarColors` | Represents the colors used by a search bar. |
| `SearchBarScrollState` | A state object that can be hoisted to control and observe the search bar's scroll state. |
| `SearchBarState` | The state of a search bar. |
| `SegmentedButtonColors` | The different colors used in parts of the SegmentedButton in different states |
| `SelectableChipColors` | Represents the container and content colors used in a selectable chip in different states. |
| `SelectableChipElevation` | Represents the elevation used in a selectable chip in different states. |
| `SelectableMenuItemColors` | Represents the text, icon, and container colors used in a selectable DropdownMenuItem at different states. |
| `Shapes` | Material surfaces can be displayed in different shapes. |
| `SheetState` | State of a sheet composable, such as ModalBottomSheet |
| `ShortNavigationBarArrangement` | Class that describes the different supported item arrangements of the ShortNavigationBar. |
| `SliderColors` | Represents the color used by a Slider in different states. |
| `SliderPositions` | This class is deprecated. Not necessary with the introduction of Slider state |
| `SliderState` | Class that holds information about Slider's active range. |
| `SnackbarHostState` | State of the SnackbarHost, which controls the queue and the current Snackbar being shown inside the SnackbarHost. |
| `SplitButtonShapes` | The shapes that will be used in SplitButtonLayout. |
| `SwipeToDismissBoxState` | State of the SwipeToDismissBox composable. |
| `SwitchColors` | Represents the colors used by a Switch in different states |
| `TabPosition` | Data class that contains information about a tab's position on screen, used for calculating where to place the indicator that shows which tab is selected. |
| `TextFieldColors` | Represents the colors of the input text, container, and content (including label, placeholder, leading and trailing icons) used in a text field in different states. |
| `TextFieldLabelPosition` | The position of the label with respect to the text field. |
| `TextFieldLabelPosition.Above` | The label is positioned above and outside the text field container. |
| `TextFieldLabelPosition.Attached` | This class is deprecated. Use Inside for the default filled TextField behavior, or Cutout for the default OutlinedTextField behavior. |
| `TextFieldLabelPosition.Cutout` | The label is positioned inside the text field container when expanded and cuts into the border when minimized. |
| `TextFieldLabelPosition.Inside` | The label is positioned inside the text field container. |
| `TimeInputColors` | Represents the colors used by a TimeInput in different states. |
| `TimePickerColors` | Represents the colors used by a TimePicker in different states. |
| `TimePickerDisplayMode` | Represents the display mode for the content of a TimePickerDialog. |
| `TimePickerLayoutType` | Represents the different configurations for the layout of the Time Picker |
| `TimePickerSelectionMode` | The selection mode for the time picker |
| `TimePickerShapes` | The shapes that will be used in time pickers. |
| `ToggleButtonColors` | Represents the container and content colors used in a toggle button in different states. |
| `ToggleButtonElevation` | Represents the elevation used in a toggle button in different states. |
| `ToggleButtonShapes` | The shapes that will be used in toggle buttons. |
| `ToggleButtonSize` | Represents the size of a ToggleButton and its variants. |
| `TooltipAnchorPosition` | — |
| `TopAppBarColors` | Represents the colors used by a top app bar in different states. |
| `TopAppBarState` | A state object that can be hoisted to control and observe the top app bar state. |
| `Typography` | The Material Design type scale includes a range of contrasting styles that support the needs of your product and its content. |
| `WideNavigationRailColors` | Represents the colors of the various elements of a wide navigation rail. |

## Objects（67）

| API | 说明 |
| --- | --- |
| `AlertDialogDefaults` | Contains default values used for AlertDialog and BasicAlertDialog. |
| `AssistChipDefaults` | Contains the baseline values used by AssistChip. |
| `BadgeDefaults` | Default values used for Badge implementations. |
| `BottomAppBarDefaults` | Contains default values used for the bottom app bar implementations. |
| `BottomSheetDefaults` | Contains the default values used by ModalBottomSheet and BottomSheetScaffold. |
| `ButtonDefaults` | Contains the default values used by all 5 button types. |
| `ButtonGroupDefaults` | Default values used by ButtonGroup |
| `CardDefaults` | Contains the default values used by all card types. |
| `CheckboxDefaults` | Defaults used in Checkbox and TriStateCheckbox. |
| `ComposeMaterial3Flags` | The object holding the feature flags. |
| `DatePickerDefaults` | Contains default values used by the DatePicker. |
| `DateRangePickerDefaults` | Contains default values used by the DateRangePicker. |
| `DividerDefaults` | Default values for Divider |
| `DrawerDefaults` | Object to hold default values for ModalNavigationDrawer |
| `ElevatedToggleButtonDefaults` | Contains default values used by ElevatedToggleButton. |
| `ExposedDropdownMenuDefaults` | Contains default values used by Exposed Dropdown Menu. |
| `FilledTonalToggleButtonDefaults` | Contains default values used by FilledTonalToggleButton. |
| `FilterChipDefaults` | Contains the baseline values used by FilterChip. |
| `FloatingActionButtonDefaults` | Contains the default values used by FloatingActionButton |
| `FloatingToolbarDefaults` | Contains default values used for the floating toolbar implementations. |
| `IconButtonDefaults` | Contains the default values for all four icon and icon toggle button types. |
| `InputChipDefaults` | Contains the baseline values used by an InputChip. |
| `ListItemDefaults` | Contains the default values used by list items. |
| `LoadingIndicatorDefaults` | Contains default values by the LoadingIndicator. |
| `MaterialTheme` | Contains functions to access the current theme values provided at the call site's position in the hierarchy. |
| `MenuDefaults` | Contains default values used for DropdownMenu and DropdownMenuItem. |
| `ModalBottomSheetDefaults` | Default values for ModalBottomSheet |
| `NavigationBarDefaults` | Defaults used in NavigationBar. |
| `NavigationBarItemDefaults` | Defaults used in NavigationBarItem. |
| `NavigationDrawerItemDefaults` | Defaults used in NavigationDrawerItem. |
| `NavigationRailDefaults` | Defaults used in NavigationRail |
| `NavigationRailItemDefaults` | Defaults used in NavigationRailItem. |
| `NonInteractiveScrollbarDefaults` | Contains the default values used by Modifier.nonInteractiveScrollbar. |
| `OutlinedTextFieldDefaults` | Contains the default values used by OutlinedTextField. |
| `OutlinedToggleButtonDefaults` | Contains default values used by OutlinedToggleButton. |
| `ProgressIndicatorDefaults` | Contains the default values used for LinearProgressIndicator and CircularProgressIndicator. |
| `RadioButtonDefaults` | Defaults used in RadioButton. |
| `RippleConfiguration.Focus.Opacity` | An opacity-based focus indication. |
| `RippleDefaults` | Default values used by ripple. |
| `RippleThemeConfiguration.Focus.Opacity` | An opacity-based focus indication. |
| `ScaffoldDefaults` | Object containing various default values for Scaffold component. |
| `ScrimDefaults` | Object containing default values for the Scrim component. |
| `ScrollFieldDefaults` | Object to hold defaults used by ScrollField. |
| `SearchBarDefaults` | Defaults used in SearchBar and DockedSearchBar. |
| `SegmentedButtonDefaults` | — |
| `ShapeDefaults` | Contains the default values used by Shapes |
| `ShortNavigationBarDefaults` | Defaults used in ShortNavigationBar. |
| `ShortNavigationBarItemDefaults` | Defaults used in ShortNavigationBarItem. |
| `SliderDefaults` | Object to hold defaults used by Slider |
| `SnackbarDefaults` | Contains the default values used for Snackbar. |
| `SplitButtonDefaults` | Contains default values used by SplitButtonLayout and its style variants. |
| `SuggestionChipDefaults` | Contains the baseline values used by SuggestionChip. |
| `SwipeToDismissBoxDefaults` | Contains default values for SwipeToDismissBox and SwipeToDismissBoxState. |
| `SwitchDefaults` | Contains the default values used by Switch |
| `TabRowDefaults` | Contains default implementations and values used for TabRow. |
| `TextFieldDefaults` | Contains the default values used by TextField. |
| `TimeInputDefaults` | Default values used by TimeInput |
| `TimePickerDefaults` | Contains the default values used by TimePicker |
| `TimePickerDialogDefaults` | Default properties for a TimePickerDialog |
| `ToggleButtonDefaults` | Contains the default values and utility functions used by ToggleButton. |
| `ToggleFloatingActionButtonDefaults` | Contains the default values used by ToggleFloatingActionButton |
| `TooltipDefaults` | Tooltip defaults that contain default values for both PlainTooltip and RichTooltip |
| `TopAppBarDefaults` | Contains default values used for the top app bar implementations. |
| `VerticalDragHandleDefaults` | Contains the baseline values used by a VerticalDragHandle. |
| `WavyProgressIndicatorDefaults` | Contains the default values used for wavy progress indicators |
| `WideNavigationRailDefaults` | Defaults used in WideNavigationRail. |
| `WideNavigationRailItemDefaults` | Defaults used in WideNavigationRailItem. |

## Interfaces（30）

| API | 说明 |
| --- | --- |
| `AppBarColumnScope` | DSL scope for building the content of an AppBarColumn. |
| `AppBarRowScope` | DSL scope for building the content of an AppBarRow. |
| `AppBarScope` | DSL scope for building the content of an AppBarRow and AppBarColumn. |
| `BottomAppBarScrollBehavior` | A BottomAppBarScrollBehavior defines how a bottom app bar should behave when the content under it is scrolled. |
| `BottomAppBarState` | A state object that can be hoisted to control and observe the bottom app bar state. |
| `ButtonGroupScope` | Button group scope used to indicate a Modifier.weight and Modifier.animateWidth of a child element. |
| `DatePickerFormatter` | A date formatter interface used by DatePicker. |
| `DatePickerState` | A state object that can be hoisted to observe the date picker state. |
| `DateRangePickerState` | A state object that can be hoisted to observe the date range picker state. |
| `DropdownMenuPopupPositionProvider` | PopupPositionProvider that communicates the TransformOrigin to dropdown menu's implementation. |
| `FloatingActionButtonMenuScope` | Scope for the children of FloatingActionButtonMenu |
| `FloatingToolbarScrollBehavior` | A FloatingToolbarScrollBehavior defines how a floating toolbar should behave when the content under it is scrolled. |
| `FloatingToolbarState` | A state object that can be hoisted to control and observe the floating toolbar state. |
| `MenuPositionScope` | Provides context for calculating candidate menu positioning coordinates relative to window bounds. |
| `MotionScheme` | A motion scheme provides all the FiniteAnimationSpecs for a MaterialTheme. |
| `MultiChoiceSegmentedButtonRowScope` | Scope for the children of a MultiChoiceSegmentedButtonRow |
| `NavigationDrawerItemColors` | Represents the colors of the various elements of a drawer item. |
| `SearchBarScrollBehavior` | A SearchBarScrollBehavior defines how a search bar should behave when the content beneath it is scrolled. |
| `SelectableDates` | An interface that controls the selectable dates and years in the date pickers UI. |
| `SingleChoiceSegmentedButtonRowScope` | Scope for the children of a SingleChoiceSegmentedButtonRow |
| `SnackbarData` | Interface to represent the data of one particular Snackbar as a piece of the SnackbarHostState. |
| `SnackbarVisuals` | Interface to represent the visuals of one particular Snackbar as a piece of the SnackbarData. |
| `TabIndicatorScope` | Scope for the composable used to render a Tab indicator, this can be used for more complex indicators requiring layout information about the tabs like TabRowDefaults.PrimaryIndicator and TabRowDefaults.SecondaryIndicator |
| `TextFieldLabelScope` | Scope for the label of a TextField or OutlinedTextField. |
| `TimePickerState` | A state object that can be hoisted to observe the time picker state. |
| `ToggleFloatingActionButtonScope` | Scope for the children of ToggleFloatingActionButton |
| `TooltipScope` | Tooltip scope for TooltipBox to be used to obtain the LayoutCoordinates of the anchor content, and to draw a caret for the tooltip. |
| `TooltipState` | The state that is associated with a TooltipBox. |
| `TopAppBarScrollBehavior` | A TopAppBarScrollBehavior defines how an app bar should behave when the content under it is scrolled. |
| `WideNavigationRailState` | A state object that can be hoisted to observe the wide navigation rail state. |

## Enums（7）

| API | 说明 |
| --- | --- |
| `DrawerValue` | Possible values of DrawerState. |
| `SearchBarValue` | Possible values of SearchBarState. |
| `SheetValue` | Possible values of SheetState. |
| `SnackbarDuration` | Possible durations of the Snackbar in SnackbarHost |
| `SnackbarResult` | Possible results of the SnackbarHostState.showSnackbar call |
| `SwipeToDismissBoxValue` | The directions in which a SwipeToDismissBox can be dismissed. |
| `WideNavigationRailValue` | Possible values of WideNavigationRailState. |

## Annotations（2）

| API | 说明 |
| --- | --- |
| `ExperimentalMaterial3Api` | — |
| `ExperimentalMaterial3ExpressiveApi` | — |

## Type aliases（1）

| API | 说明 |
| --- | --- |
| `CalendarLocale` | Represents a Locale for the calendar. |
