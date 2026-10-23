# M3E API 签名速查（源码核对版）

核对日期：**2026-10-23**
源码基线：`androidx/androidx` @ `androidx-main`（本地克隆逐文件核对，非文档摘要）
发布通道对照：`material3` **1.5.0-beta02**（2026-10-21）/ 稳定 **1.4.0**

> **和 `compose-api-full.md` 的分工**：那份是 **1.4.0 稳定线**的全量 API 快照（约 7900 行，
> 没有 1.5.0 线新组件的签名）。本文补的是 **1.5.0 线 / M3E 新组件**的准确签名。
> 查 API 的顺序：本文 → `compose-api-full.md` → `m3-content/` → 官方 samples。

## opt-in 说明（重要）

`androidx-main` 是最新主线，很多 Expressive 组件已经**不需要** `@ExperimentalMaterial3ExpressiveApi`。
但 **1.5.0-beta02 的发布产物可能仍要求**。实践规则：

1. 先不写 opt-in，编译；
2. 编译器报 "requires opt-in" 时再加 `@OptIn(ExperimentalMaterial3ExpressiveApi::class)`
   （或函数级 `@OptIn`），不要凭记忆预设。
3. 截至本文核对，主线里只有 `LoadingIndicator` / `ContainedLoadingIndicator` 仍带
   `@ExperimentalMaterial3ExpressiveApi`；`FloatingToolbar`、`ButtonGroup`、`ShortNavigationBar`、
   `ScrollField`、`ToggleFloatingActionButton`、`SplitButtonLayout`、`WideNavigationRail`、
   `SearchBar`、Flexible AppBar 系列均**无** Expressive opt-in 注解。

---

## 1. 主题

### MaterialExpressiveTheme

```kotlin
@Composable
public fun MaterialExpressiveTheme(
    colorScheme: ColorScheme? = null,
    motionScheme: MotionScheme? = null,
    shapes: Shapes? = null,
    typography: Typography? = null,
    content: @Composable () -> Unit,
)
```

- 全部主题参数可空：`null` 时回退到 `expressiveLightColorScheme()` / `MotionScheme.expressive()` /
  `Shapes()` / `Typography()`。
- 嵌套在已有 expressive 主题内时（内部 `LocalUsingExpressiveTheme == true`），`null` 会**继承外层**
  而不是重置成默认值。
- 所以「只覆盖动效」可以写 `MaterialExpressiveTheme(motionScheme = MotionScheme.expressive()) { ... }`。

### Shapes —— 8 档，不是 5 档

```kotlin
public class Shapes(
    public val extraSmall: CornerBasedShape = ShapeDefaults.ExtraSmall,
    public val small: CornerBasedShape = ShapeDefaults.Small,
    public val medium: CornerBasedShape = ShapeDefaults.Medium,
    public val large: CornerBasedShape = ShapeDefaults.Large,
    public val extraLarge: CornerBasedShape = ShapeDefaults.ExtraLarge,
    largeIncreased: CornerBasedShape = ShapeDefaults.LargeIncreased,
    extraLargeIncreased: CornerBasedShape = ShapeDefaults.ExtraLargeIncreased,
    extraExtraLarge: CornerBasedShape = ShapeDefaults.ExtraExtraLarge,
)
```

M3 的 5 档 + M3E 新增 3 档：`largeIncreased`、`extraLargeIncreased`、`extraExtraLarge`。
M3E 组件（FAB Menu、浮动工具栏）会用到后三档；自定义主题时至少给 `largeIncreased` 赋值。

### MotionScheme

```kotlin
public interface MotionScheme {
    public fun <T> defaultSpatialSpec(): FiniteAnimationSpec<T>
    public fun <T> fastSpatialSpec(): FiniteAnimationSpec<T>
    public fun <T> slowSpatialSpec(): FiniteAnimationSpec<T>
    public fun <T> defaultEffectsSpec(): FiniteAnimationSpec<T>
    public fun <T> fastEffectsSpec(): FiniteAnimationSpec<T>
    public fun <T> slowEffectsSpec(): FiniteAnimationSpec<T>

    public companion object {
        public fun standard(): MotionScheme
        public fun expressive(): MotionScheme
    }
}
```

取用方式：`MaterialTheme.motionScheme.defaultSpatialSpec<Float>()`。
**不要**用 `LocalMotionScheme`（1.5.0-alpha27 已移除）。自定义组件动画：

```kotlin
val spec = MaterialTheme.motionScheme.fastSpatialSpec<Float>()
animateFloatAsState(targetValue = target, animationSpec = spec)
```

Spatial = 位置/尺寸/形状变化；Effects = 颜色/透明度/内容淡入淡出。

---

## 2. 形状与 MaterialShapes

### 预设形状

`MaterialShapes` 提供 35 个 `RoundedPolygon`（`androidx.compose.material3.MaterialShapes`）：
`Circle`、`Square`、`Slanted`、`Arch`、`Fan`、`Arrow`、`SemiCircle`、`Oval`、`Pill`、`Triangle`、
`Diamond`、`ClamShell`、`Pentagon`、`Gem`、`Sunny`、`VerySunny`、`Cookie4Sided`、`Cookie6Sided`、
`Cookie7Sided`、`Cookie9Sided`、`Cookie12Sided`、`Ghostish`、`Clover4Leaf`、`Clover8Leaf`、`Burst`、
`SoftBurst`、`Boom`、`SoftBoom`、`Flower`、`Puffy`、`PuffyDiamond`、`PixelCircle`、`PixelTriangle`、
`Bun`、`Heart`。

```kotlin
Icon(
    imageVector = ...,
    contentDescription = null,
    modifier = Modifier.background(MaterialShapes.Cookie9Sided.toShape(), color = ...),
)

// RoundedPolygon 扩展
public fun RoundedPolygon.toShape(startAngle: Int = 0): Shape
public fun RoundedPolygon.toPath(startAngle: Int = 0): Path
```

### PolygonShape（注意包名）

`PolygonShape` **不在** `androidx.compose.material3`，而在
**`androidx.compose.foundation.shape.PolygonShape`**（1.5.0-beta01 起为就地变换 API）：

```kotlin
public sealed class PolygonShape : Shape {
    public fun transform(block: PolygonShapeTransformScope.() -> Unit)  // 就地修改，可动画
    public fun copy(): PolygonShape                                      // 需要保留基础形状时先 copy
}
```

`transform` 的 block 在 **outline 解析时**执行（不在 composition 中），因此动画中读取的状态
不会触发重组。旧 API `transformed()` / `scaledToFit()` 已删除。

---

## 3. 浮动工具栏

```kotlin
@Composable
public fun HorizontalFloatingToolbar(
    expanded: Boolean,
    modifier: Modifier = Modifier,
    colors: FloatingToolbarColors = FloatingToolbarDefaults.standardFloatingToolbarColors(),
    contentPadding: PaddingValues = FloatingToolbarDefaults.ContentPadding,
    scrollBehavior: FloatingToolbarScrollBehavior? = null,
    shape: Shape = FloatingToolbarDefaults.ContainerShape,
    leadingContent: @Composable (RowScope.() -> Unit)? = null,
    trailingContent: @Composable (RowScope.() -> Unit)? = null,
    expandedShadowElevation: Dp = ...,
    collapsedShadowElevation: Dp = ...,
    content: @Composable RowScope.() -> Unit,
)

// 带 FAB 的重载（多出两个参数）
public fun HorizontalFloatingToolbar(
    expanded: Boolean,
    floatingActionButton: @Composable () -> Unit,
    modifier: Modifier = Modifier,
    colors: FloatingToolbarColors = ...,
    contentPadding: PaddingValues = ...,
    scrollBehavior: FloatingToolbarScrollBehavior? = null,
    shape: Shape = ...,
    floatingActionButtonPosition: FloatingToolbarHorizontalFabPosition =
        FloatingToolbarHorizontalFabPosition.End,
    animationSpec: FiniteAnimationSpec<Float> = FloatingToolbarDefaults.animationSpec(),
    expandedShadowElevation: Dp = FloatingToolbarDefaults.ContainerExpandedElevationWithFab,
    collapsedShadowElevation: Dp = FloatingToolbarDefaults.ContainerCollapsedElevationWithFab,
    content: @Composable RowScope.() -> Unit,
)
```

`VerticalFloatingToolbar` 同构，槽位是 `ColumnScope`，FAB 位置默认
`FloatingToolbarVerticalFabPosition.Bottom`。

关键配套（都在 `FloatingToolbarDefaults` / `FloatingToolbarExitDirection`）：

```kotlin
FloatingToolbarDefaults.ScreenOffset                       // 距屏幕边缘的标准偏移
FloatingToolbarDefaults.vibrantFloatingToolbarColors()     // 配 FAB 的鲜艳配色
FloatingToolbarDefaults.VibrantFloatingActionButton(onClick) { Icon(...) }
FloatingToolbarDefaults.exitAlwaysScrollBehavior(exitDirection = Bottom | End)
Modifier.floatingToolbarVerticalNestedScroll(expanded, onExpand, onCollapse)
```

官方示例强约束：工具栏**声明在内容之前**（焦点顺序），并加 `Modifier.zIndex(1f)`；
折叠时按钮用 `Modifier.focusProperties { canFocus = expanded }`，避免焦点落在不可见元素上。

### 溢出菜单容器

`AppBarRow { clickableItem(onClick, icon, label) }`（水平）/
`AppBarColumn { ... }`（垂直）——`clickableItem` 是 `AppBarRowScope` / `AppBarColumnScope` 成员，
放不下时自动进溢出菜单。它们是 `FloatingToolbar` 的 `trailingContent` 标准搭档。

---

## 4. 按钮族

### ButtonGroup

```kotlin
@Composable
public fun ButtonGroup(
    overflowIndicator: @Composable (ButtonGroupMenuState) -> Unit,
    modifier: Modifier = Modifier,
    @FloatRange(0.0) expandedRatio: Float = ButtonGroupDefaults.ExpandedRatio, // 0.15f
    horizontalArrangement: Arrangement.Horizontal = ButtonGroupDefaults.HorizontalArrangement,
    verticalAlignment: Alignment.Vertical = Alignment.Top,
    content: ButtonGroupScope.() -> Unit,
)
```

`ButtonGroupScope` 只提供两个 DSL 方法：

```kotlin
public fun clickableItem(
    onClick: () -> Unit,
    label: String,
    icon: (@Composable () -> Unit)? = null,
    weight: Float = Float.NaN,
    enabled: Boolean = true,
)

public fun customItem(
    buttonGroupContent: @Composable () -> Unit,
    menuContent: @Composable (ButtonGroupMenuState) -> Unit,
)

public fun Modifier.animateWidth(interactionSource: InteractionSource): Modifier
public fun Modifier.animateWidth(interactionSource: InteractionSource, compressionLimit: Dp): Modifier
```

`ButtonGroupDefaults` 常用成员：

| 成员 | 值 / 用途 |
| --- | --- |
| `ExpandedRatio` | `0.15f` |
| `ConnectedSpaceBetween` | 负间距，让按钮咬合 |
| `connectedLeadingButtonShapes()` / `connectedMiddleButtonShapes()` / `connectedTrailingButtonShapes()` | 连体形状（首/中/尾） |
| `connectedButtonCheckedShape` | 选中态形状 |
| `OverflowIndicator(menuState)` | 标准溢出按钮 |

`ButtonGroupMenuState` 有 `show()` / `dismiss()`。

单选连通组的标准做法是 `FlowRow` + `ToggleButton` + 上面三个 shapes + `Role.RadioButton` 语义，
见 `compose-patterns.md`。

### ToggleButton

```kotlin
@Composable
public fun ToggleButton(
    checked: Boolean,
    onCheckedChange: (Boolean) -> Unit,
    modifier: Modifier = Modifier,
    buttonSize: ToggleButtonSize = ToggleButtonDefaults.size,
    enabled: Boolean = true,
    icon: (@Composable () -> Unit)? = null,
    shapes: ToggleButtonShapes = ToggleButtonDefaults.shapesFor(buttonSize),
    colors: ToggleButtonColors = ToggleButtonDefaults.colors(),
    elevation: ToggleButtonElevation? = ToggleButtonDefaults.elevation(),
    border: BorderStroke? = null,
    contentPadding: PaddingValues =
        ToggleButtonDefaults.contentPaddingFor(buttonSize, hasStartIcon = icon != null),
    interactionSource: MutableInteractionSource? = null,
    content: @Composable RowScope.() -> Unit,
)
```

配套：`FilledTonalToggleButton`、`ElevatedToggleButton`、`OutlinedToggleButton`；
`ToggleButtonDefaults.IconSpacing`、`.pressedShape`、`.shapesFor(size)`。

### SplitButton —— 没有 `SplitButton` 这个 composable

⚠️ 源码核对结论：`androidx-main` 里只有 **`SplitButtonLayout`**，搜索不到 `fun SplitButton(`。
网上/发行说明里的 "SplitButton" 指的是这套组合，不要写 `SplitButton(...)`。

```kotlin
@Composable
public fun SplitButtonLayout(
    leadingButton: @Composable () -> Unit,
    trailingButton: @Composable () -> Unit,
    modifier: Modifier = Modifier,
    spacing: Dp = SplitButtonDefaults.Spacing,
)

// 前后按钮由 SplitButtonDefaults 提供：
SplitButtonDefaults.LeadingButton(onClick, modifier, enabled, shapes, colors, elevation,
    border, contentPadding, interactionSource) { content }
SplitButtonDefaults.TrailingButton(...)              // 还有 checked/onCheckedChange 重载
SplitButtonDefaults.TonalLeadingButton / TonalTrailingButton
SplitButtonDefaults.OutlinedLeadingButton / OutlinedTrailingButton
SplitButtonDefaults.ElevatedLeadingButton / ElevatedTrailingButton
SplitButtonDefaults.leadingButtonShapesFor(buttonHeight) / trailingButtonShapesFor(buttonHeight)
SplitButtonDefaults.leadingButtonContentPaddingFor(buttonHeight) / trailingButtonContentPaddingFor(buttonHeight)
```

---

## 5. FAB 家族

```kotlin
@Composable
public fun ToggleFloatingActionButton(
    checked: Boolean,
    onCheckedChange: (Boolean) -> Unit,
    modifier: Modifier = Modifier,
    containerColor: (Float) -> Color = ToggleFloatingActionButtonDefaults.containerColor(),
    contentAlignment: Alignment = Alignment.TopEnd,
    containerSize: (Float) -> Dp = ToggleFloatingActionButtonDefaults.containerSize(),
    containerCornerRadius: (Float) -> Dp = ToggleFloatingActionButtonDefaults.containerCornerRadius(),
    content: @Composable ToggleFloatingActionButtonScope.() -> Unit,
)

@Composable
public fun FloatingActionButtonMenu(
    expanded: Boolean,
    button: @Composable () -> Unit,
    modifier: Modifier = Modifier,
    horizontalAlignment: Alignment.Horizontal = Alignment.End,
    content: @Composable FloatingActionButtonMenuScope.() -> Unit,
)
```

`containerColor` / `containerSize` / `containerCornerRadius` 都是 `(动画进度) -> 值`，
所以颜色和尺寸会随 morph 连续变化，不是二选一。

---

## 6. 导航

### WideNavigationRail / ModalWideNavigationRail

```kotlin
@Composable
public fun WideNavigationRail(
    modifier: Modifier = Modifier,
    state: WideNavigationRailState = rememberWideNavigationRailState(),
    shape: Shape = WideNavigationRailDefaults.shape,
    colors: WideNavigationRailColors = WideNavigationRailDefaults.colors(),
    header: (@Composable () -> Unit)? = null,
    windowInsets: WindowInsets = WideNavigationRailDefaults.windowInsets,
    arrangement: Arrangement.Vertical = WideNavigationRailDefaults.arrangement,
    contentPadding: PaddingValues = WideNavigationRailDefaults.ContentPadding,
    content: @Composable () -> Unit,
)

@Composable
public fun ModalWideNavigationRail(
    modifier: Modifier = Modifier,
    state: WideNavigationRailState = rememberWideNavigationRailState(),
    hideOnCollapse: Boolean = false,
    collapsedShape: Shape = WideNavigationRailDefaults.modalCollapsedShape,
    expandedShape: Shape = WideNavigationRailDefaults.modalExpandedShape,
    colors: WideNavigationRailColors = WideNavigationRailDefaults.colors(),
    header: (@Composable () -> Unit)? = null,
    expandedHeaderTopPadding: Dp = 0.dp,
    windowInsets: WindowInsets = WideNavigationRailDefaults.windowInsets,
    arrangement: Arrangement.Vertical = WideNavigationRailDefaults.arrangement,
    expandedProperties: ModalWideNavigationRailProperties =
        WideNavigationRailDefaults.ModalExpandedProperties,
    contentPadding: PaddingValues = WideNavigationRailDefaults.ContentPadding,
    content: @Composable () -> Unit,
)
```

两者都有省略 `contentPadding` 的重载。折叠状态由 `WideNavigationRailState` 管，
`rememberWideNavigationRailState()` 创建。

### ShortNavigationBar（M3E 紧凑底栏）

```kotlin
@Composable
public fun ShortNavigationBar(
    modifier: Modifier = Modifier,
    containerColor: Color = ShortNavigationBarDefaults.containerColor,
    contentColor: Color = ShortNavigationBarDefaults.contentColor,
    windowInsets: WindowInsets = ShortNavigationBarDefaults.windowInsets,
    arrangement: ShortNavigationBarArrangement = ShortNavigationBarDefaults.arrangement,
    content: @Composable () -> Unit,
)

@Composable
public fun ShortNavigationBarItem(
    selected: Boolean,
    onClick: () -> Unit,
    icon: @Composable () -> Unit,
    label: (@Composable () -> Unit)?,
    modifier: Modifier = Modifier,
    enabled: Boolean = true,
    iconPosition: NavigationItemIconPosition = NavigationItemIconPosition.Top,
    colors: NavigationItemColors = ShortNavigationBarItemDefaults.colors(),
    interactionSource: MutableInteractionSource? = null,
)
```

场景：手机/折叠屏外屏的「短」底栏，3–5 个目的地；大屏仍用 `NavigationRail` / `WideNavigationRail`。

### NavigationSuiteScaffold

在独立 artifact `androidx.compose.material3:material3-adaptive-navigation-suite`（包
`androidx.compose.material3.adaptive.navigationsuite`），按窗口宽度自动在
`NavigationBar` / `NavigationRail` / `NavigationDrawer` 之间切换。签名见该库 API 文档，
不要从 `compose-api-full.md` 找（该快照只覆盖 `material3.adaptive.*` 的布局包）。

---

## 7. 应用栏

```kotlin
@Composable
public fun MediumFlexibleTopAppBar(
    title: @Composable () -> Unit,
    modifier: Modifier = Modifier,
    subtitle: (@Composable () -> Unit)? = null,
    navigationIcon: @Composable () -> Unit = {},
    actions: @Composable RowScope.() -> Unit = {},
    titleHorizontalAlignment: Alignment.Horizontal = Alignment.Start,
    collapsedHeight: Dp = TopAppBarDefaults.MediumAppBarCollapsedHeight,
    expandedHeight: Dp = /* 有 subtitle 时用 WithSubtitle 常量 */,
    windowInsets: WindowInsets = TopAppBarDefaults.windowInsets,
    colors: TopAppBarColors = TopAppBarDefaults.topAppBarColors(),
    scrollBehavior: TopAppBarScrollBehavior? = null,
)

public fun LargeFlexibleTopAppBar(/* 同上，height 常量换成 Large* */)

public fun TwoRowsTopAppBar(
    title: @Composable (expanded: Boolean) -> Unit,
    subtitle: (@Composable (expanded: Boolean) -> Unit)? = null,
    /* 其余同上，collapsedHeight/expandedHeight 默认 Dp.Unspecified */
)

public fun FlexibleBottomAppBar(
    modifier: Modifier = Modifier,
    containerColor: Color = BottomAppBarDefaults.containerColor,
    contentColor: Color = contentColorFor(containerColor),
    contentPadding: PaddingValues = BottomAppBarDefaults.FlexibleContentPadding,
    horizontalArrangement: Arrangement.Horizontal = BottomAppBarDefaults.FlexibleHorizontalArrangement,
    expandedHeight: Dp = BottomAppBarDefaults.FlexibleBottomAppBarHeight,
    windowInsets: WindowInsets = BottomAppBarDefaults.windowInsets,
    scrollBehavior: BottomAppBarScrollBehavior? = null,
    content: @Composable RowScope.() -> Unit,
)
```

注意 `TwoRowsTopAppBar` 的 title/subtitle 带 `expanded: Boolean` 参数（随折叠变化重绘）。

---

## 8. 搜索

`SearchBar` 有三个重载，**新代码用第一个**（slot + state）：

```kotlin
@Composable
public fun SearchBar(
    state: SearchBarState,
    inputField: @Composable () -> Unit,
    modifier: Modifier = Modifier,
    shape: Shape = SearchBarDefaults.inputFieldShape,
    colors: SearchBarColors = SearchBarDefaults.colors(),
    tonalElevation: Dp = SearchBarDefaults.TonalElevation,
    shadowElevation: Dp = SearchBarDefaults.ShadowElevation,
)

@Composable
public fun rememberSearchBarState(
    initialValue: SearchBarValue = SearchBarValue.Collapsed,
    animationSpecForExpand: AnimationSpec<Float> = MotionSchemeKeyTokens.SlowSpatial.value(),
    animationSpecForCollapse: AnimationSpec<Float> = MotionSchemeKeyTokens.DefaultSpatial.value(),
): SearchBarState
```

`SearchBarValue` 是 enum：`Collapsed` / `Expanded`。展开态用配套的
`ExpandedFullScreenSearchBar` / `ExpandedDockedSearchBar`（在 `SearchBar.kt` 同包）。
旧的两参数 API（`expanded` / `onExpandedChange` 和 `query` / `active`）仍存在但已弃用。

---

## 9. 加载与进度

```kotlin
@Composable
public fun LoadingIndicator(                     // 不确定进度
    modifier: Modifier = Modifier,
    color: Color = LoadingIndicatorDefaults.indicatorColor,
    polygons: List<RoundedPolygon> = LoadingIndicatorDefaults.IndeterminateIndicatorPolygons,
)

@Composable
public fun LoadingIndicator(                     // 确定进度
    progress: () -> Float,
    modifier: Modifier = Modifier,
    color: Color = LoadingIndicatorDefaults.indicatorColor,
    polygons: List<RoundedPolygon> = LoadingIndicatorDefaults.DeterminateIndicatorPolygons,
)

@Composable
public fun ContainedLoadingIndicator(            // 带容器背景
    progress: () -> Float,
    modifier: Modifier = Modifier,
    containerColor: Color = LoadingIndicatorDefaults.containedContainerColor,
    indicatorColor: Color = LoadingIndicatorDefaults.containedIndicatorColor,
    containerShape: Shape = LoadingIndicatorDefaults.containerShape,
    polygons: List<RoundedPolygon> = LoadingIndicatorDefaults.DeterminateIndicatorPolygons,
)
```

`progress` 是 **lambda `() -> Float`**（deferred read），不要传普通 Float 变量——那样每帧都会重组。
下拉刷新用 `PullToRefreshDefaults.LoadingIndicator(state, isRefreshing)`。

```kotlin
@Composable
public fun LinearWavyProgressIndicator(          // 确定进度
    progress: () -> Float,
    modifier: Modifier = Modifier,
    color: Color = WavyProgressIndicatorDefaults.indicatorColor,
    trackColor: Color = WavyProgressIndicatorDefaults.trackColor,
    stroke: Stroke = WavyProgressIndicatorDefaults.linearIndicatorStroke,
    trackStroke: Stroke = WavyProgressIndicatorDefaults.linearTrackStroke,
    gapSize: Dp = WavyProgressIndicatorDefaults.LinearIndicatorTrackGapSize,
    stopSize: Dp = WavyProgressIndicatorDefaults.LinearTrackStopIndicatorSize,
    amplitude: (progress: Float) -> Float = WavyProgressIndicatorDefaults.indicatorAmplitude,
    wavelength: Dp = WavyProgressIndicatorDefaults.LinearDeterminateWavelength,
    waveSpeed: Dp = wavelength,
)

public fun LinearWavyProgressIndicator(          // 不确定进度
    modifier: Modifier = Modifier,
    color: Color = ...,
    trackColor: Color = ...,
    stroke: Stroke = ...,
    trackStroke: Stroke = ...,
    gapSize: Dp = ...,
    @FloatRange(from = 0.0, to = 1.0) amplitude: Float = 1f,
    wavelength: Dp = WavyProgressIndicatorDefaults.LinearIndeterminateWavelength,
    waveSpeed: Dp = wavelength,
)
```

`CircularWavyProgressIndicator` 同构（没有 `stopSize`）。
函数名是 `Linear/CircularWavyProgressIndicator`，**不是** `WavyProgressIndicator`。

---

## 10. 滚动选择输入

```kotlin
@Composable
public fun ScrollField(
    state: ScrollFieldState,
    contentDescription: String?,
    modifier: Modifier = Modifier,
    enabled: Boolean = true,
    colors: ScrollFieldColors = ScrollFieldDefaults.colors(),
    fieldAccessibilityDescription: (index: Int) -> String = { index -> index.toLocalString() },
    interactionSource: MutableInteractionSource? = null,
    field: @Composable (index: Int, selected: Boolean, enabled: Boolean) -> Unit =
        { index, selected, enabled -> ScrollFieldDefaults.Item(index, selected, enabled, colors) },
)

@Composable
public fun rememberScrollFieldState(itemCount: Int, index: Int = 0): ScrollFieldState
```

用法：日期/时间/数字的滚轮选择（M3E 时间选择器内部同款交互）。`ScrollFieldState` 构造器是
`internal`，只能用 `rememberScrollFieldState`。

---

## 11. 常见 API 陷阱

| 陷阱 | 正确写法 |
| --- | --- |
| 以为 `Shapes` 只有 5 档 | 8 档，含 `largeIncreased` / `extraLargeIncreased` / `extraExtraLarge` |
| 写 `SplitButton { }` | 只有 `SplitButtonLayout(leadingButton = ..., trailingButton = ...)` |
| 写 `WavyProgressIndicator()` | `LinearWavyProgressIndicator` / `CircularWavyProgressIndicator` |
| 写 `LocalMotionScheme.current` | `MaterialTheme.motionScheme`（已移除 Local） |
| `LoadingIndicator(progress = value)` | `LoadingIndicator(progress = { value })` |
| 在 `androidx.compose.material3` 找 `PolygonShape` | `androidx.compose.foundation.shape.PolygonShape` |
| 用 `MaterialTheme` 期望 Expressive 默认值 | 用 `MaterialExpressiveTheme`（默认 expressive 色板 + expressive 动效） |
| `TopAppBarDefaults.pinnedScrollBehavior()` 旧重载 | alpha27 已移除，改传 `ScrollableState` 的新重载 |
