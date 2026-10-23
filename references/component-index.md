# 组件索引：源码 / 官方示例 / 设计规范

核对日期：**2026-10-23**

查一个组件时，按 **源码（签名） → 官方 sample（写法） → 设计规范（外观）** 三处定位。
本文只给**文件名和目录**，不写完整 URL——路径模板见文末，避免链接随重构失效。

## 1. 按钮与操作

| 组件 | 源码（`compose/material3/material3/src/commonMain/.../material3/`） | 官方 sample（`.../material3/samples/`） | 设计规范（`references/m3-content/components/`） |
| --- | --- | --- | --- |
| `Button` / `FilledTonalButton` / `OutlinedButton` / `TextButton` / `ElevatedButton` | `Button.kt` | `ButtonSamples.kt` | `buttons/` |
| `IconButton` 家族 | `IconButton.kt`、`IconButtonDefaults.kt` | `IconButtonSamples.kt` | `icon-buttons/` |
| `FloatingActionButton` / `Small…` / `Large…` / `Extended…` | `FloatingActionButton.kt` | `FloatingActionButtonSamples.kt` | `floating-action-button/`、`extended-fab/` |
| `ToggleFloatingActionButton` | `FloatingActionButtonMenu.kt` | `FloatingActionButtonMenuSamples.kt` | `fab-menu/` |
| `FloatingActionButtonMenu` | `FloatingActionButtonMenu.kt` | `FloatingActionButtonMenuSamples.kt` | `fab-menu/` |
| `SegmentedButton` | `SegmentedButton.kt` | `SegmentedButtonSamples.kt` | `segmented-buttons/` |
| `ToggleButton` / `FilledTonalToggleButton` / `Elevated…` / `Outlined…` | `ToggleButton.kt` | `ToggleButtonSamples.kt` | `buttons/`（含 toggle 变体） |
| `ButtonGroup` | `ButtonGroup.kt` | `ButtonGroupSamples.kt` | `button-groups/` |
| `SplitButtonLayout`（无 `SplitButton`） | `SplitButton.kt` | `SplitButtonSamples.kt` | `split-button/` |

## 2. 应用栏与工具栏

| 组件 | 源码 | 官方 sample | 设计规范 |
| --- | --- | --- | --- |
| `TopAppBar` / `CenterAligned…` / `Medium…` / `Large…` | `AppBar.kt` | `AppBarSamples.kt` | `app-bars/` |
| `MediumFlexibleTopAppBar` / `LargeFlexibleTopAppBar` / `TwoRowsTopAppBar` | `AppBar.kt` | `AppBarSamples.kt` | `app-bars/` |
| `BottomAppBar` / `FlexibleBottomAppBar` | `AppBar.kt` | `AppBarSamples.kt` | `app-bars/` |
| `HorizontalFloatingToolbar` / `VerticalFloatingToolbar` | `FloatingToolbar.kt` | `FloatingToolbarSamples.kt` | `toolbars/`（未单独覆盖 floating 变体） |
| `AppBarRow` / `AppBarColumn` | `AppBarRow.kt`、`AppBarColumn.kt`、`AppBarDsl.kt` | `FloatingToolbarSamples.kt` | `toolbars/` |

## 3. 导航

| 组件 | 源码 | 官方 sample | 设计规范 |
| --- | --- | --- | --- |
| `NavigationBar` / `NavigationBarItem` | `NavigationBar.kt`、`NavigationItem.kt` | `NavigationBarSamples.kt` | `navigation-bar/` |
| `ShortNavigationBar`（M3E） | `ShortNavigationBar.kt` | —（无独立 sample；参考 `NavigationBarSamples.kt` 的结构 + 签名速查） | `navigation-bar/`（官网暂无独立页） |
| `NavigationRail` / `NavigationRailItem` | `NavigationRail.kt`、`NavigationItem.kt` | `NavigationRailSamples.kt` | `navigation-rail/` |
| `WideNavigationRail` / `ModalWideNavigationRail` | `WideNavigationRail.kt`、`WideNavigationRailState.kt` | —（无独立 sample；参考 `NavigationRailSamples.kt`） | `navigation-rail/` |
| `ModalNavigationDrawer` / `Permanent…` / `Dismissible…` | `NavigationDrawer.kt` | `DrawerSamples.kt` | `navigation-drawer/` |
| `NavigationSuiteScaffold` | 独立 artifact：`material3-adaptive-navigation-suite` | 该模块自带 `samples/` | —（跨组件，见 `m3-content/foundations/layout/`） |
| `Tab` / `TabRow` / `PrimaryTabRow` / `SecondaryTabRow` | `Tab.kt`、`TabRow.kt` | `TabSamples.kt` | `tabs/` |

## 4. 搜索与文本输入

| 组件 | 源码 | 官方 sample | 设计规范 |
| --- | --- | --- | --- |
| `SearchBar` / `SearchBarState` / `Expanded*SearchBar` / `AppBarWithSearch` | `SearchBar.kt` | `SearchBarSamples.kt` | `search/` |
| `TextField` / `OutlinedTextField` | `TextField.kt`、`OutlinedTextField.kt`、`TextFieldDefaults.kt` | `TextFieldSamples.kt` | `text-fields/` |
| `SecureTextField` / `OutlinedSecureTextField` | `SecureTextField.kt` | `TextFieldSamples.kt` | `text-fields/` |
| `ScrollField`（M3E） | `ScrollField.kt` | `ScrollFieldSamples.kt` | —（官网暂无独立页） |
| `Text`（含 autoSize） | `Text.kt` | `TextSamples.kt` | `m3-content/styles/typography/` |

## 5. 选择与输入控件

| 组件 | 源码 | 官方 sample | 设计规范 |
| --- | --- | --- | --- |
| `Checkbox` / `TriStateCheckbox` | `Checkbox.kt` | `CheckboxSamples.kt` | `checkbox/` |
| `RadioButton` | `RadioButton.kt` | `RadioButtonSamples.kt` | `radio-button/` |
| `Switch` | `Switch.kt` | `SwitchSamples.kt` | `switch/` |
| `Slider` / `RangeSlider` / `SliderState` | `Slider.kt` | `SliderSamples.kt` | `sliders/` |
| `AssistChip` / `FilterChip` / `InputChip` / `SuggestionChip` | `Chip.kt` | `ChipSamples.kt` | `chips/` |
| `DatePicker` / `DateRangePicker` / `DatePickerDialog` | `DatePicker.kt`、`DateRangePicker.kt`、`DatePickerDialog.kt` | `DatePickerSamples.kt` | `date-pickers/` |
| `TimePicker` / `TimeInput` / `TimePickerDialog` | `TimePicker.kt`、`TimePickerDialog.kt`、`TimeFormat.kt` | `TimePickerSamples.kt` | `time-pickers/` |

## 6. 容器、列表与浮层

| 组件 | 源码 | 官方 sample | 设计规范 |
| --- | --- | --- | --- |
| `Card` / `ElevatedCard` / `OutlinedCard` | `Card.kt` | `CardSamples.kt` | `cards/` |
| `Surface` | `Surface.kt` | `SurfaceSamples.kt` | —（基础组件） |
| `ListItem` | `ListItem.kt`、`ListItemDefaults.kt` | `ListSamples.kt` | `lists/` |
| `Scaffold` | `Scaffold.kt` | `ScaffoldSamples.kt` | —（见 `foundations/layout/`） |
| `ModalBottomSheet` / `BottomSheetScaffold` / `SheetDefaults` | `ModalBottomSheet.kt`、`BottomSheet.kt`、`BottomSheetScaffold.kt`、`SheetDefaults.kt` | `BottomSheetSamples.kt` | `bottom-sheets/`、`side-sheets/` |
| `AlertDialog` / `BasicAlertDialog` | `AlertDialog.kt` | `AlertDialogSamples.kt` | `dialogs/` |
| `DropdownMenu` / `ExposedDropdownMenu` | `Menu.kt`、`MenuDefaults.kt`、`ExposedDropdownMenu.kt` | `MenuSamples.kt`、`ExposedDropdownMenuSamples.kt` | `menus/` |
| `Snackbar` / `SnackbarHost` | `Snackbar.kt`、`SnackbarHost.kt` | —（见 `ScaffoldSamples.kt`） | `snackbar/` |
| `PlainTooltip` / `RichTooltip` / `TooltipBox` | `Tooltip.kt` | `TooltipSamples.kt` | `tooltips/` |
| `Badge` / `BadgedBox` | `Badge.kt` | `BadgeSamples.kt` | `badges/` |
| `HorizontalDivider` / `VerticalDivider` | `Divider.kt` | — | `divider/` |

## 7. 反馈、进度与手势

| 组件 | 源码 | 官方 sample | 设计规范 |
| --- | --- | --- | --- |
| `LinearProgressIndicator` / `CircularProgressIndicator` | `ProgressIndicator.kt` | `ProgressIndicatorSamples.kt` | `progress-indicators/` |
| `LoadingIndicator` / `ContainedLoadingIndicator` | `LoadingIndicator.kt` | `LoadingIndicatorSamples.kt` | `loading-indicator/` |
| `LinearWavyProgressIndicator` / `CircularWavyProgressIndicator` | `WavyProgressIndicator.kt` | `ProgressIndicatorSamples.kt` | `progress-indicators/` |
| `PullToRefreshBox` / `Modifier.pullToRefresh` | `pulltorefresh/` 包 | `PullToRefreshSamples.kt` | — |
| `SwipeToDismissBox` | `SwipeToDismissBox.kt` | `SwipeToDismissSamples.kt` | — |
| `Carousel` 系列 | `carousel/` 包 | `CarouselSamples.kt` | `carousel/` |

## 8. 主题、形状与动效

| 能力 | 源码 | 官方 sample | 设计规范 |
| --- | --- | --- | --- |
| 主题接线 | `MaterialTheme.kt` | `ThemeSamples.kt` | `m3-content/styles/` |
| 配色 | `ColorScheme.kt`、`TonalPalette.kt` | `ColorSchemeSamples.kt` | `styles/color/` |
| 排版（15 + 15 Emphasized） | `Typography.kt` | `TypographySamples.kt` | `styles/typography/` |
| 形状（8 档） | `Shapes.kt` | `ThemeSamples.kt` | `styles/shape/` |
| 预设形状（35 个 `RoundedPolygon`） | `MaterialShapes.kt` | `MaterialShapesSamples.kt` | `styles/shape/shape-morph.md` |
| 动效 | `MotionScheme.kt` | —（见 `TransitionSamples.kt`、`LoadingIndicatorSamples.kt`） | `styles/motion/` |
| 涟漪 | `Ripple.kt` | `RippleSamples.kt` | — |
| 拖拽手柄 | `DragHandle.kt` | `DragHandleSamples.kt` | — |
| 最小触控尺寸 | `InteractiveComponentSize.kt` | `InteractiveComponentSizeSamples.kt` | — |

## 9. URL 模板（需要粘贴链接时用）

仓库：`https://github.com/androidx/androidx/blob/androidx-main/`

```
源码:  compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/<File>.kt
示例:  compose/material3/material3/samples/src/main/java/androidx/compose/material3/samples/<Name>Samples.kt
规范:  https://m3.material.io/components/<slug>/specs        # slug 见 m3-content/components/<dir>
```

**用法建议**：给用户回答时优先贴 `源码路径 + 行号` 或 `sample 函数名`，而不是整条 GitHub URL。
URL 只在用户明确要链接时给，且优先给 `m3.material.io` 的规范页或官方 API 参考页——
`androidx-main` 的文件路径会随重构变化。

## 10. 三源冲突时怎么裁决

| 问题 | 信谁 |
| --- | --- |
| 参数名、默认值、opt-in 注解 | **源码**（本文第 1 列） |
| 一段可运行的写法 | **官方 sample**（第 2 列）；`androidx-main` 的 sample 可能领先发布版 |
| 尺寸、间距、状态层、anatomy | **设计规范**（第 3 列）；镜像抓取于 2026-09-14，官网组件页最后更新集中在 2026-07~09 |
| 版本门槛、当前发布通道 | `version-baseline.md` |
| 设计规范与源码冲突 | 源码优先，并在回答里说明规范可能滞后 |
