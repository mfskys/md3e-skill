# M3E 组件清单

核对日期：**2026-10-08**
来源：Compose Material 3 官方版本说明（https://developer.android.com/jetpack/androidx/releases/compose-material3，
页面更新 2026-10-07）✅

**读法说明**：括号里的 `alphaNN` 是"该 API 从实验性毕业"的版本。
`1.4.0` 是当前**稳定线**，`1.5.0-betaNN` 是 **1.5.0 线**。
要判断某个组件能否用，先看它在哪条线上。

---

> 📌 **版本策略**：本项目**采用最新版本（含 Alpha/Beta/RC）**——
> `material3 = 1.5.0-beta01`，因此下文所有"1.5.0 线"组件**都在我们的可用范围内**。
> 见 `../version-baseline.md`。第 11 节的"采用建议"已按此更新。

## 一、按钮与操作

| 组件 | 状态 | 说明 |
| --- | --- | --- |
| `ToggleButton` 系列 | 1.4.0-alpha19 稳定 | M3E 新增的切换按钮 |
| `FilledTonalToggleButton` | alpha25 重命名 | 原名 `TonalToggleButton` |
| `ButtonGroup` | 1.4.0-alpha22 稳定 | 按钮组；alpha25 起 `ButtonGroupScope` 改为 **sealed interface**，`Modifier.animateWidth` 拆成两个重载 |
| `SplitButton` | 1.4.0-alpha20 转非实验 | alpha25 起 **弃用 `SplitButtonLayout`**，统一用 `SplitButton` |
| FAB 与 **FAB Menu** | 1.4.0-alpha19 毕业 | FAB 展开菜单是 M3E 的标志性交互 |
| `ExtendedFloatingActionButton` / `Button` / `TextButton` | 稳定 | 强调程度递减的三档（传统 M3） |

---

## 二、应用栏与工具栏

| 组件 | 状态 | 适用 |
| --- | --- | --- |
| `TopAppBar` | 稳定 | 传统小号 |
| `MediumFlexibleTopAppBar` | 1.5.0-alpha23 毕业 | 中大号 + 可折叠（flexible） |
| `LargeTopAppBar` | 稳定 | 大号 |
| `LargeFlexibleTopAppBar` | 1.5.0-alpha23 毕业 | 大号 + 可折叠 |
| `TwoRowsTopAppBar` | 1.5.0-alpha23 毕业 | 双行 |
| `FlexibleBottomAppBar` | 1.5.0-alpha23 毕业 | 可折叠底部栏 |
| `FloatingToolbar` | 1.5.0-alpha22 非实验 | 悬浮工具栏 |
| `AppBarWithSearch` | alpha02 引入 | **替代 `TopSearchBar`** |

> 1.5.0-alpha27：`TopAppBarDefaults` 中 `pinnedScrollBehavior` / `enterAlwaysScrollBehavior`
> 的**旧重载被移除**；`LocalMotionScheme` 移除，改用 `MaterialTheme.motionScheme`。

---

## 三、搜索

| 组件 | 状态 |
| --- | --- |
| `SearchBarState` + 基于 slot 的 `SearchBar` API | **1.5.0-alpha24 稳定**；旧的扩展 / `onExpandedChange` API 弃用 |
| `ExpandedDockedSearchBarWithGap` | 1.5.0-alpha23 非实验 |
| `ExpandedFullScreenContainedSearchBar` | 1.5.0-alpha23 非实验 |
| `rememberWithGapSearchBarState` | alpha18 重命名为 `rememberSearchBarWithGapState` |

---

## 四、时间与选择器

| 组件 | 状态 |
| --- | --- |
| Expressive `TimePicker` 滚动变体 | alpha03 引入；alpha24 新增滚动变体 |
| `VibrantTimePickerDialog` | alpha27 由 `RichTimePickerDialog` 重命名；`richColors` → `vibrantColors` |
| `Slider` / `RangeSlider` | alpha28：**无状态重载弃用**，改用有状态版本；`RangeSliderState.activeRangeStart/End` → `startValue/endValue` |

---

## 五、菜单

| 组件 | 状态 |
| --- | --- |
| `SelectableDropdownMenuItem` / `CheckableDropdownMenuItem` | 1.5.0-alpha27 新增 |
| `MenuDefaults.itemVibrantColors()` | 提供鲜艳的 `MenuItemColors` |
| Expressive 菜单 API | alpha19 起提升；**移除旧的实验性 `DropdownMenuItem`** |
| `ExposedDropdownMenu` | alpha26：由成员改为 `ExposedDropdownMenuBoxScope` 的**扩展函数**，需要更新 import |

---

## 六、列表项

| 组件 | 状态 |
| --- | --- |
| Expressive `ListItem` | 支持互动与分段样式；alpha11 新增 `ListItemColors` 字段 |
| 非互动变体 | alpha23 引入（标准 / 分段），**旧的非表达性版本弃用** |

---

## 七、容器与浮层

| 组件 | 状态 |
| --- | --- |
| 多宽高比 **Carousel** | alpha10 正式支持；alpha28 简化为全局 `carouselParallaxScrollEffect` 修饰符 |
| **Scrim** | alpha15 引入，用于模态组件 |
| 独立静态 **Sheet** | alpha15 引入 |
| `ModalBottomSheet` | alpha20：`rememberModalBottomSheetState` / `rememberStandardBottomSheetState` **弃用**，统一为 `rememberBottomSheetState`；alpha09 移除旧的实验性 API |
| `material3-ripple` | alpha24 新增独立库：**用内嵌焦点环替代不透明度层** |

---

## 八、传统 M3 组件（稳定可用的基本盘）

`Scaffold`、`Surface`、`Card`（含 `CardDefaults.cardColors/cardElevation`）、
`Button` / `OutlinedButton` / `TextButton` / `IconButton` / `FilledIconButton`、
`Chip`（`AssistChip` / `FilterChip` / `InputChip`）、`Checkbox` / `RadioButton` / `Switch`、
`Slider`、`Divider`、`Badge`、`Snackbar`、`AlertDialog`、
`DropdownMenu`、`ExposedDropdownMenuBox`、`ModalBottomSheet`、
`NavigationBar` / `NavigationRail` / `NavigationDrawer` / `PermanentNavigationDrawer`、
`PullToRefreshBox` / `Modifier.pullToRefresh`、`LinearProgressIndicator` / `CircularProgressIndicator`。

> ⚠️ PullToRefresh 在 **1.3.0** 大改：`PullToRefreshState` 简化（用小数而非 `Dp`）、
> `isRefreshing` 由用户控制、嵌套滚动分离到 `PullToRefreshBox` 或 `Modifier.pullToRefresh`。

---

## 九、自适应相关组件（本项目底座的核心）

| 组件 | 库 | 说明 |
| --- | --- | --- |
| `NavigationSuiteScaffold` | `material3-adaptive-navigation-suite` | 按窗口尺寸自动切换形态。⚠️ **1.5.0-alpha28 起实际渲染的是新组件**：Compact → `ShortNavigationBarCompact`（`ShortNavigationBar` 竖排条目）、其余 → `WideNavigationRailCollapsed`；旧的 `NavigationBar`/`NavigationRail`/`NavigationDrawer` 三个类型已标注"不推荐"。详见 `../m3-content/foundations/layout/scaffold/overview.md` |
| `ListDetailPaneScaffold` / `NavigableListDetailPaneScaffold` | `adaptive-layout` / `adaptive-navigation` | 列表-详情规范布局 |
| `SupportingPaneScaffold` / `NavigableSupportingPaneScaffold` | 同上 | 主窗格 + 支持窗格 |
| `ThreePaneScaffold` 抽象 | `adaptive-layout` | 三窗格基架（含 navigator / state / predictive back handler） |
| `AnimatedPane` | `adaptive-layout` | 窗格默认动画；1.4.0-alpha01 起支持形状 |
| `HingeInfo` / `Posture` | `adaptive` | 铰链与设备姿态（折叠屏） |

> 自适应布局规范见 `../m3-content/foundations/layout/`。

---

## 十、选型速查

| 需求 | 首选 | 备注 |
| --- | --- | --- |
| 主操作 | `Button` / `FilledTonalButton` | 一个屏幕**只放一个**最强强调按钮 |
| 相关操作组合 | `ButtonGroup` | 1.5.0 线 |
| 主操作 + 附加菜单 | `SplitButton` | 同上 |
| 顶部标题 + 滚动折叠 | `MediumFlexibleTopAppBar` / `LargeFlexibleTopAppBar` | 需按窗口高度决定是否折叠（见 `../m3-content/foundations/layout/breakpoints/overview.md`） |
| 底部常驻操作栏 | `FlexibleBottomAppBar` | 小屏比 TopAppBar 更易触达 |
| 全屏/侧边导航 | `NavigationSuiteScaffold` | 不要手写三种导航的判断 |
| 搜索 | slot 版 `SearchBar` + `SearchBarState` | 旧 API 已弃用 |
| 切换态（如"显示隐藏文件"） | `Switch`（设置项）/ `ToggleButton`（工具条） | — |
| 上下文操作（多选） | 顶部 contextual bar + `Scaffold` | 用 `AnimatedVisibility` 切换 |

---

## 十一、采用建议（已按"激进策略"更新）

1. **直接用 1.5.0 线的 M3E 全套**（`material3 = 1.5.0-beta01`）：
   ToggleButton / ButtonGroup / SplitButton / FAB Menu / Flexible AppBar /
   slot 版 SearchBar 全部可用，不再有"稳定线拿不到"的问题。
2. **调用点收敛**：M3E 组件集中放在 `ui/expressive/`（或 `ui/components/`），
   便于应对 1.5.0 线的重命名与移除。
3. **每个预览版依赖登记退出计划**：升级到 stable 时删除兼容层；
   回落映射见 `../version-baseline.md`。
4. **图标从 Material Symbols 取**：M3 1.4.0 起不再传递 `material-icons-core`，
   且 `androidx.compose.material.icons` 不再推荐。
5. **升级前必读 release notes**：1.5.0 线变动频繁（见 `compose-api.md` 第四节）。
