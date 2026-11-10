# Compose + M3E 代码模式库

核对日期：**2026-10-23**　签名来源：`androidx-main` 源码（见 `m3e-api-signatures.md`）

本文是「需求 → 可编译代码」的桥。每个模式只给最小正确写法；完整变体去
`official-samples.md` 指到的官方 sample 文件看。

---

## 1. 主题接线（一次做对）

```kotlin
// ui/theme/Color.kt —— 由 scripts/generate_theme.py 生成，或手写
val LightColorScheme = lightColorScheme(primary = Color(0xFF65558F) /* ...48 roles */)
val DarkColorScheme = darkColorScheme(primary = Color(0xFFD0BCFF) /* ... */)

// ui/theme/Shape.kt —— M3E 是 8 档，不是 5 档
val AppShapes = Shapes(
    extraSmall = RoundedCornerShape(4.dp),
    small = RoundedCornerShape(8.dp),
    medium = RoundedCornerShape(12.dp),
    large = RoundedCornerShape(16.dp),
    extraLarge = RoundedCornerShape(28.dp),
    largeIncreased = RoundedCornerShape(20.dp),        // M3E
    extraLargeIncreased = RoundedCornerShape(32.dp),   // M3E
    extraExtraLarge = RoundedCornerShape(36.dp),       // M3E
)

// ui/theme/Theme.kt
@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit,
) {
    val context = LocalContext.current
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ->
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }
    MaterialExpressiveTheme(
        colorScheme = colorScheme,
        motionScheme = MotionScheme.expressive(),  // 想要克制就 standard()
        typography = AppTypography,
        shapes = AppShapes,
        content = content,
    )
}
```

要点：
- 用 `MaterialExpressiveTheme` 而不是 `MaterialTheme`；它默认给 expressive 色板 + expressive 动效。
- 动态色必须 API 31+，低版本回退到自己的 scheme。
- 不要用 `LocalMotionScheme`，读 `MaterialTheme.motionScheme`。

---

## 2. 屏幕骨架（边到边 + insets）

```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeScreen() {
    val scrollBehavior = TopAppBarDefaults.pinnedScrollBehavior()
    Scaffold(
        modifier = Modifier.nestedScroll(scrollBehavior.nestedScrollConnection),
        topBar = {
            TopAppBar(
                title = { Text("Inbox") },
                scrollBehavior = scrollBehavior,
                actions = { IconButton(onClick = {}) { Icon(Icons.Default.Search, "Search") } },
            )
        },
        floatingActionButton = {
            FloatingActionButton(onClick = {}) { Icon(Icons.Default.Add, "Compose") }
        },
    ) { innerPadding ->
        LazyColumn(
            contentPadding = innerPadding,          // 不要用 Modifier.padding 包整个列表
            verticalArrangement = Arrangement.spacedBy(8.dp),
            modifier = Modifier.fillMaxSize(),
        ) {
            items(count = 50) { index -> ListItem(headlineContent = { Text("Item $index") }) }
        }
    }
}
```

`contentPadding = innerPadding` 让内容能滚到系统栏下面；用 `Modifier.padding(innerPadding)`
会把滚动区域截断（常见错误）。

---

## 3. 自适应导航

### 3.1 用官方套件（推荐）

artifact：`androidx.compose.material3:material3-adaptive-navigation-suite`

```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AppScaffold(selected: Int, onSelect: (Int) -> Unit, content: @Composable () -> Unit) {
    val state = rememberNavigationSuiteScaffoldState()
    NavigationSuiteScaffold(
        state = state,
        navigationItems = {
            listOf("Songs", "Artists", "Playlists").forEachIndexed { index, label ->
                NavigationSuiteItem(
                    icon = { Icon(Icons.Default.Favorite, contentDescription = null) },
                    label = { Text(label) },
                    selected = selected == index,
                    onClick = { onSelect(index) },
                )
            }
        },
        content = content,
    )
}
```

它在 `COMPACT / MEDIUM / EXPANDED` 宽度下自动选 `ShortNavigationBar` / `NavigationRail` /
`WideNavigationRail`。`state.currentValue` 可读当前形态，`state.toggle()` 可收起/展开。

> 1.5.0 线若不支持 `navigationItems` + `NavigationSuiteItem`（新版 API），改用旧签名
> `NavigationSuiteScaffold(navigationSuiteItems = { ... })`，条目方法以源码为准。

### 3.2 手写选择（无套件依赖）

| 宽度 | 组件 | 目的地数 |
| --- | --- | --- |
| `< 600dp` | `ShortNavigationBar` 或 `NavigationBar` | 3–5 |
| `600–839dp` | `NavigationRail` | 3–7 |
| `≥ 840dp` | `WideNavigationRail` / `ModalWideNavigationRail` / `PermanentNavigationDrawer` | 不限 |

用 `currentWindowAdaptiveInfoV2().windowSizeClass.windowWidthSizeClass` 判断，
不要用 `LocalConfiguration.screenWidthDp` 自己算断点。

---

## 4. 浮动工具栏（含 FAB 与滚动收起）

```kotlin
@Composable
fun EditorScreen() {
    var expanded by rememberSaveable { mutableStateOf(true) }
    val exitBehavior = FloatingToolbarDefaults.exitAlwaysScrollBehavior(
        exitDirection = FloatingToolbarExitDirection.Bottom,
    )
    Scaffold(modifier = Modifier.nestedScroll(exitBehavior)) { innerPadding ->
        Box(Modifier.padding(innerPadding)) {
            HorizontalFloatingToolbar(
                expanded = expanded,
                floatingActionButton = {
                    FloatingToolbarDefaults.VibrantFloatingActionButton(
                        onClick = { expanded = !expanded }
                    ) { Icon(Icons.Filled.Add, contentDescription = "Add") }
                },
                modifier = Modifier
                    .align(Alignment.BottomEnd)
                    .offset(x = -FloatingToolbarDefaults.ScreenOffset,
                            y = -FloatingToolbarDefaults.ScreenOffset)
                    .zIndex(1f),
                colors = FloatingToolbarDefaults.vibrantFloatingToolbarColors(),
                scrollBehavior = exitBehavior,
                content = {
                    IconButton(onClick = {}, modifier = Modifier.focusProperties { canFocus = expanded }) {
                        Icon(Icons.Filled.Person, contentDescription = "Profile")
                    }
                    IconButton(onClick = {}, modifier = Modifier.focusProperties { canFocus = expanded }) {
                        Icon(Icons.Filled.Edit, contentDescription = "Edit")
                    }
                },
            )
            LazyColumn(Modifier.fillMaxSize()) { /* content */ }
        }
    }
}
```

规则（官方 sample 注释里写死的）：
1. 工具栏**先于内容**声明，保证 TalkBack/键盘焦点先到它。
2. `zIndex(1f)` 保证视觉在上层。
3. 折叠时用 `focusProperties { canFocus = expanded }` 把不可见按钮移出焦点。
4. 溢出项用 `trailingContent = { AppBarRow { clickableItem(...) } }`（垂直用 `AppBarColumn`）。

---

## 5. 按钮组：全变体（standard / connected）

M3E 的"按钮组"在代码里是**两种不同的东西**，选错样式完全不同：

| 变体 | 代码形态 | 行为 | 用在哪 |
| --- | --- | --- | --- |
| **standard** | `ButtonGroup { ... }` | 按下时自己变宽、相邻按钮被压缩（`expandedRatio`）；放不下自动进溢出菜单 | 一排操作按钮，常带"更多" |
| **connected** | `FlowRow` + `ToggleButton` + `connected*Shapes()` | 按钮连成一体，选中态变形，互不影响宽度 | 筛选 / 切换视图 / 排序（**取代 SegmentedButton**） |

设计侧的对应关系见 `recipes/button-groups.md`：`standard` 和 `connected` 是官方
两个变体，各有 XS–XL 五档、round / square 两种形状、单选 / 多选 / 必选三种选择模式。

### 5.1 standard：`ButtonGroup` + 溢出菜单

```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun SortButtonGroup(selected: Int, onSelect: (Int) -> Unit) {
    ButtonGroup(
        overflowIndicator = { menuState ->
            ButtonGroupDefaults.OverflowIndicator(menuState)
        },
        modifier = Modifier.padding(horizontal = 8.dp),
    ) {
        toggleableItem(
            checked = selected == 0,
            label = "Recent",
            onCheckedChange = { onSelect(0) },
        )
        toggleableItem(
            checked = selected == 1,
            label = "Popular",
            onCheckedChange = { onSelect(1) },
        )
        clickableItem(onClick = { /* more */ }, label = "More")
    }
}
```

`ButtonGroupScope` 只有三个 DSL 方法，别去别处找：

| 方法 | 用途 |
| --- | --- |
| `clickableItem(onClick, label, icon, weight, enabled)` | 一次性动作按钮 |
| `toggleableItem(checked, label, onCheckedChange, icon, weight, enabled)` | 可选中按钮（standard 组的选择态） |
| `customItem(buttonGroupContent, menuContent)` | 自定义外观，自己处理溢出菜单 |

- `weight` 控制相对宽度（`Float.NaN` = 按内容）；也有 `Modifier.weight()` / `Modifier.align()` 版本。
- 按压压缩幅度由 `expandedRatio`（默认 `0.15f`）控制；0f 完全不联动，1f 按到 200% 宽。
- 需要自定义压缩动画时用 `customItem` + `Modifier.animateWidth(interactionSource, compressionLimit)`，
  并给 `Text(softWrap = false, maxLines = 1)`。

### 5.2 connected：单选 / 多选 / 必选

```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun FilterRow(options: List<String>, selectedIndex: Int, onSelect: (Int) -> Unit) {
    FlowRow(
        modifier = Modifier.fillMaxWidth().padding(horizontal = 8.dp),
        horizontalArrangement = Arrangement.spacedBy(ButtonGroupDefaults.ConnectedSpaceBetween),
        verticalArrangement = Arrangement.spacedBy(2.dp),
    ) {
        options.forEachIndexed { index, label ->
            ToggleButton(
                checked = selectedIndex == index,
                onCheckedChange = { onSelect(index) },
                shapes = when (index) {
                    0 -> ButtonGroupDefaults.connectedLeadingButtonShapes()
                    options.lastIndex -> ButtonGroupDefaults.connectedTrailingButtonShapes()
                    else -> ButtonGroupDefaults.connectedMiddleButtonShapes()
                },
                modifier = Modifier.semantics { role = Role.RadioButton },
            ) { Text(label) }
        }
    }
}
```

三种选择模式的差异只有两处：`role` 语义和 `checked` 的状态形状。

| 模式 | 语义 | 状态处理 |
| --- | --- | --- |
| 单选 | `Role.RadioButton` | 单个 `selectedIndex`，选中时走 `connectedButtonCheckedShape` |
| 多选 | `Role.Checkbox` | `Set<Int>` 或 `List<Boolean>`，可同时选中多个 |
| 必选（不可取消） | `Role.RadioButton` | `onCheckedChange` 里拒绝取消当前项 |

`ButtonGroupDefaults.ConnectedSpaceBetween` = **2dp**（`ConnectedButtonGroupSmallTokens.BetweenSpace`，正数）。
按钮之所以"咬合"是 `connected*ButtonShapes()` 给的**互补圆角**，不是负间距——靠负 margin 拼是错的。

### 5.3 尺寸与形状（五档 × 两种）

尺寸由组内**按钮**决定，不在 `ButtonGroup` 上：

```kotlin
ToggleButton(
    checked = checked,
    onCheckedChange = onCheckedChange,
    buttonSize = ToggleButtonSize.Medium,   // ExtraSmall / Small(默认) / Medium / Large / ExtraLarge
    shapes = ToggleButtonDefaults.shapesFor(ToggleButtonSize.Medium),
) { Text("Medium") }
```

| `ToggleButtonSize` | 高度来源 | 说明 |
| --- | --- | --- |
| `ExtraSmall` | `ButtonDefaults.ExtraSmallContainerHeight` | XS，`md.comp.button-group.standard.xsmall.container.height` = **32dp** |
| `Small` | `ButtonSmallTokens.ContainerHeight` | **默认值**（`ToggleButtonDefaults.size`） |
| `Medium` | `ButtonDefaults.MediumContainerHeight` | |
| `Large` | `ButtonDefaults.LargeContainerHeight` | |
| `ExtraLarge` | `ButtonDefaults.ExtraLargeContainerHeight` | XL |

round / square 两种形状的圆角（官方 buttons corner sizes 表）：

| | XS | S | M | L | XL |
| --- | --- | --- | --- | --- | --- |
| Round button | Full | Full | Full | Full | Full |
| Square button | 12dp | 12dp | 16dp | 28dp | 28dp |
| Pressed state | 8dp | 8dp | 12dp | 16dp | 16dp |

连通组的形状不是"每档一个值"，而是三个形状构成一组 `ToggleButtonShapes`
（default / pressed / checked），所以永远用 `connected*ButtonShapes()` 工厂方法而不是手写圆角。

### 5.4 常见坑

- `ButtonGroup` 的 `overflowIndicator` 是**必填参数**，不是可选项；忘了就编译不过。
- connected 组不要用 `ButtonGroup` 包，它只负责 standard 变体。
- `ToggleButtonDefaults.size` 默认是 **Small**，不是 Medium；设计稿看起来更矮就是这个原因。
- 选中的形状来自 `shapes.checkedShape`，不要手填 `ButtonGroupDefaults.connectedButtonCheckedShape`。

---

## 6. 分割按钮（正确 API）

```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun SendSplitButton(onSend: () -> Unit, onMore: () -> Unit) {
    SplitButtonLayout(
        leadingButton = {
            SplitButtonDefaults.LeadingButton(onClick = onSend) { Text("Send") }
        },
        trailingButton = {
            SplitButtonDefaults.TrailingButton(onClick = onMore) {
                Icon(Icons.Filled.ArrowDropDown, contentDescription = "More send options")
            }
        },
    )
}
```

⚠️ **没有 `SplitButton(...)` 这个 composable**。容器只有 `SplitButtonLayout`，
前后两半由 `SplitButtonDefaults.LeadingButton / TrailingButton` 提供（还有
`Tonal*` / `Outlined*` / `Elevated*` 变体）。写错名字会直接编译失败。

---

## 7. 搜索（slot + state）

```kotlin
@Composable
fun SearchScreen() {
    val searchState = rememberSearchBarState()
    val textFieldState = rememberTextFieldState()
    val scope = rememberCoroutineScope()

    val inputField = @Composable {
        SearchBarDefaults.InputField(
            textFieldState = textFieldState,
            searchBarState = searchState,
            onSearch = { scope.launch { searchState.animateToCollapsed() } },
            placeholder = { Text("Search songs") },
            leadingIcon = {
                IconButton(onClick = { scope.launch { searchState.animateToCollapsed() } }) {
                    Icon(Icons.Default.ArrowBack, contentDescription = "Close search")
                }
            },
            trailingIcon = { Icon(Icons.Default.Search, contentDescription = null) },
        )
    }

    SearchBar(state = searchState, inputField = inputField)
    ExpandedFullScreenSearchBar(state = searchState, inputField = inputField) {
        // 搜索结果列表
    }
}
```

- `SearchBarState` 的公开成员只有 `progress` / `isAnimating` / `targetValue` / `currentValue`
  以及两个 **suspend** 方法 `animateToExpanded()` / `animateToCollapsed()`。
  **没有** `show()` / `hide()` / `isExpanded`——必须放在 `scope.launch { }` 里调用。
- 触摸模式下输入框获得焦点会自动展开，不需要手动调 `animateToExpanded()`。
- 展开态容器：`ExpandedFullScreenSearchBar` / `ExpandedDockedSearchBar` /
  `ExpandedFullScreenContainedSearchBar` / `ExpandedDockedSearchBarWithGap`。
  顶部常驻搜索用 `AppBarWithSearch` + `SearchBarDefaults.enterAlwaysSearchBarScrollBehavior()`。

---

## 8. 加载与下拉刷新

```kotlin
// 不确定进度
LoadingIndicator()
ContainedLoadingIndicator()

// 确定进度：progress 必须是 lambda，避免每帧重组
LoadingIndicator(progress = { animatedProgress })
ContainedLoadingIndicator(progress = { animatedProgress })

// 波浪进度（M3E 视觉）
LinearWavyProgressIndicator(progress = { animatedProgress })
CircularWavyProgressIndicator(progress = { animatedProgress })
```

下拉刷新用 `Modifier.pullToRefresh(state, isRefreshing, onRefresh)` +
`PullToRefreshDefaults.LoadingIndicator(state, isRefreshing)`，并且**在 TopAppBar 里放一个
刷新 IconButton** 作为无障碍替代触发方式（官方 sample 明确要求）。

---

## 9. 卡片 / 列表 / 选择态

```kotlin
Card(
    onClick = { onSelect() },
    colors = CardDefaults.cardColors(
        containerColor = if (isSelected) MaterialTheme.colorScheme.primaryContainer
                         else MaterialTheme.colorScheme.surfaceContainer,
        contentColor = if (isSelected) MaterialTheme.colorScheme.onPrimaryContainer
                       else MaterialTheme.colorScheme.onSurface,
    ),
) {
    ListItem(
        headlineContent = { Text("Dinner club") },
        supportingContent = { Text("Wed · 7:00 PM") },
        leadingContent = { Icon(Icons.Outlined.DateRange, contentDescription = null) },
    )
}
```

- 容器层级用 `surfaceContainerLowest → Low → (默认) → High → Highest`，不要自己调 alpha。
- `on*` 色只配对应容器色；反例：`tertiaryContainer` + `primaryContainer`（对比度不足）。
- 选中态同时改容器色 + 内容色，别只改一边。

---

## 10. 自定义动效（MotionScheme）

```kotlin
val spec = MaterialTheme.motionScheme.fastSpatialSpec<Float>()
val offset by animateFloatAsState(
    targetValue = if (expanded) 0f else 24f,
    animationSpec = spec,
    label = "offset",
)
```

- **Spatial**：位置、尺寸、形状、旋转 → 用 `*SpatialSpec`。
- **Effects**：颜色、透明度、内容淡入淡出 → 用 `*EffectsSpec`。
- 速度档：`fast` / `default` / `slow`。不要硬编码 `spring(dampingRatio = ...)`，
  否则与主题动效体系脱节。
- 系统开启「移除动画」时，弹簧会自动退化；不要自己再加 `if (animationsDisabled)` 分支。

---

## 11. 无障碍与常见反模式

必须做：

| 项 | 做法 |
| --- | --- |
| 图标语义 | 可点击图标必须给 `contentDescription`；纯装饰给 `null` |
| 单选/多选语义 | `Modifier.semantics { role = Role.RadioButton }`，或依赖 `ToggleButton` 默认 Checkbox 语义 |
| 触控尺寸 | 不小于 48dp；用 `minimumInteractiveComponentSize()`，不要肉眼调 padding |
| 焦点顺序 | 浮层/工具栏先声明；隐藏元素 `canFocus = false` |
| 字号缩放 | 用 `sp` 和 `MaterialTheme.typography`；测 200% 字号不截断 |
| 对比度 | 只使用成对角色（`primary`/`onPrimary`、`*Container`/`on*Container`） |
| 动画开关 | 用 `MotionScheme`，不要硬编码时长 |

反模式：

| 反模式 | 后果 |
| --- | --- |
| `Modifier.padding(innerPadding)` 包 LazyColumn | 内容被裁，无法滚到系统栏下 |
| 手写 `Color(0xFF...)` 直接用 | 深色模式/动态色失效 |
| `Text(color = MaterialTheme.colorScheme.primary)` 放在 primaryContainer 上 | 对比度不足 |
| `LoadingIndicator(progress = value)` | 每帧重组 |
| `LocalMotionScheme.current` | 已移除，编译失败 |
| 自己算屏幕断点 | 与 WindowSizeClass / 折叠屏姿态不一致 |
| `SplitButton { }` | 该 composable 不存在 |
