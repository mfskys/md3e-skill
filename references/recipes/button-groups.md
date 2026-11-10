# Button Groups — 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`ButtonGroup.kt`、`ButtonGroupSmallTokens.kt`、`ConnectedButtonGroupSmallTokens.kt`、`ShapeTokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 两个变体 —— 代码形态完全不同

这不是"一个组件的两种样式"，而是**两套实现**。选错的话交互和外观都不对。

| | standard | connected |
| --- | --- | --- |
| 代码入口 | `ButtonGroup { ... }` | `FlowRow` + `ToggleButton` + `connected*ButtonShapes()` |
| 按下行为 | 自己变宽、**相邻按钮被压缩**（`expandedRatio`） | 只改自己的形状，邻居不动 |
| 溢出 | 放不下自动进溢出菜单（`overflowIndicator` **必填**） | 自己处理换行 |
| 选择模式 | 点击 + 可选中的 toggle | 单选 / 多选 / 必选 |
| 用途 | 一排**动作**按钮（含"更多"） | **选择**类：筛选、切换视图、排序 |

| 变体 | 状态 |
| --- | --- |
| standard `ButtonGroup` | ✅ 推荐 |
| connected（`FlowRow` + `ToggleButton`） | ✅ 推荐，**SegmentedButton 的官方替代** |
| `SegmentedButton` / `Single/`MultiChoiceSegmentedButtonRow | ⚠️ M3E 不再推荐，保留说明见 §8 |

## 1. 尺寸

`ButtonGroup` **没有 `size` 参数** —— 组的高度由**组内按钮**决定，见 `recipes/buttons.md`。

组自身的 token（`ButtonGroup*Tokens` / `ConnectedButtonGroup*Tokens`）：

| Token | XS（specs 站内值） | S（源码值） |
| --- | --- | --- |
| standard `ContainerHeight` | 32dp | **40dp** |
| standard `BetweenSpace` | 18dp | **12dp** |
| connected `BetweenSpace` | — | **2dp** |
| connected `ContainerShape` | — | `CornerFull` |

对应 `ButtonGroupDefaults`：

```kotlin
ButtonGroupDefaults.HorizontalArrangement      // = spacedBy(ButtonGroupSmallTokens.BetweenSpace) → 12dp
ButtonGroupDefaults.ConnectedSpaceBetween      // = ConnectedButtonGroupSmallTokens.BetweenSpace → 2dp（正数）
ButtonGroupDefaults.ExpandedRatio              // 0.15f
```

⚠️ `ConnectedSpaceBetween` 是 **+2dp**，不是负间距。按钮"咬合"靠的是形状互补，不是靠负 margin 拼。

五档尺寸的完整高度/内边距/图标值见 `recipes/buttons.md` §1，连通组用同一套按钮尺寸。

## 2. 形状

```kotlin
// standard 组：整组统一一种形状
ButtonDefaults.shape          // round（CornerFull）
ButtonDefaults.squareShape    // square（随尺寸 12/12/16/28/28dp）

// connected 组：按位置取互补圆角，三件套必须齐全
ButtonGroupDefaults.connectedLeadingButtonShapes()
ButtonGroupDefaults.connectedMiddleButtonShapes()
ButtonGroupDefaults.connectedTrailingButtonShapes()
ButtonGroupDefaults.connectedButtonCheckedShape   // CornerFull
```

**M3E 的选中态会翻转形状**：round 的按钮选中后变方、方的选中后变圆。这不是 bug，是官方的
"selected buttons should change shape"。所以不要自己写死一个 `RoundedCornerShape` 了事。

## 3. 颜色

- **按钮组本身没有颜色属性**。容器透明，颜色全来自组内的按钮（filled / tonal / outlined / elevated）。
- standard 组内可以混颜色，但**形状和尺寸要保持统一**。
- connected 组**不要混色**，否则选中态和强调关系会看不出来（官方明文）。

## 4. 状态

| 状态 | standard | connected |
| --- | --- | --- |
| Enabled | 按内容宽度 | 等分或按内容 |
| Pressed | 自己变宽 `+expandedRatio`，邻居被压缩 | 形状切到 pressed 形状 |
| Selected | 选中项形状翻转 + 变色 | 选中项形状翻转 + 变色 |
| Disabled | 整组或单项 `enabled = false` | 同左 |
| Overflow | 超出宽度进菜单 | 换到下一行 |

## 5. 代码

### 5.1 standard + 溢出菜单

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

`ButtonGroupScope` 只有三个方法：

| 方法 | 用途 |
| --- | --- |
| `clickableItem(onClick, label, icon, weight, enabled)` | 一次性动作 |
| `toggleableItem(checked, label, onCheckedChange, icon, weight, enabled)` | 可选中 |
| `customItem(buttonGroupContent, menuContent)` | 自定义外观 + 自己接溢出菜单 |

### 5.2 connected：单选

```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun FilterRow(options: List<String>, selectedIndex: Int, onSelect: (Int) -> Unit) {
    Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.spacedBy(ButtonGroupDefaults.ConnectedSpaceBetween),
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
                modifier = Modifier.weight(1f).semantics { role = Role.RadioButton },
            ) { Text(label, maxLines = 1, softWrap = false) }
        }
    }
}
```

连通组通常**撑满可用宽度**（`Modifier.weight(1f)`），不要让它按内容缩在一边。

### 5.3 connected：多选 / 必选

| 模式 | 语义 | 状态 |
| --- | --- | --- |
| 单选 | `Role.RadioButton` | `selectedIndex: Int` |
| 多选 | `Role.Checkbox` | `Set<Int>` |
| 必选（不可取消） | `Role.RadioButton` | `onCheckedChange` 里拒绝取消当前项 |

### 5.4 跟随尺寸

```kotlin
val size = ToggleButtonSize.Medium
ToggleButton(
    checked = checked,
    onCheckedChange = onCheckedChange,
    buttonSize = size,
    shapes = ButtonGroupDefaults.connectedMiddleButtonShapes(),
) { Text("Label") }
```

注意：这里 `shapes` 用连通组工厂，尺寸才用 `buttonSize`。两者独立，别只改一个。

## 6. 选型与设计规则

融合自官方 button-groups 的 guidelines 与 accessibility 页。

### 6.1 什么时候用哪一类

- 需要**一排动作**（含"更多"）→ standard `ButtonGroup`。
- 需要**选择**（单选/多选/切换视图/排序）→ connected。
- **按钮都不能被 toggle 时，不要用连通组**（官方明文）。
- connected 是 `SegmentedButton` 的官方替代，M3E 项目不要再新建 segmented button。

### 6.2 统一性

- standard 组内所有按钮**同尺寸、同形状**（统一 XS–XL，统一 round 或 square），只通过宽度和颜色区分。
- 形状差异**只留给关键交互**（选中、强调），不要随手给某个按钮换个形状。
- connected 组**不要混色**。
- 不要频繁混搭尺寸；主操作应当在所有断点下都是最大/最宽/最显眼的那个。

### 6.3 布局

- 按钮组**单行排列，不换行**；多个组可以纵向堆叠，但组与组之间**没有纵向联动**。
- connected 组应撑满所在页面/面板宽度；大窗口下给它加 `Modifier.widthIn(max = ...)` 防止过宽。
- 手动调宽度时，**icon button 不要超过 wide 档**。
- 屏幕变窄时，多余按钮**进溢出菜单**；组外按钮（如"结束通话"）不受影响。

### 6.4 溢出行为

- 溢出的是"次要动作"，主操作永远保留在组内。
- 溢出菜单由 `ButtonGroupDefaults.OverflowIndicator(menuState)` 渲染，`menuState` 有 `show()` / `dismiss()`。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| 触控目标 | 组内**每个按钮**至少 **48×48dp** |
| XS / S 组 | 这两个尺寸**内边距本来就更大**，用来凑够触控目标，**不要手动减小** |
| 焦点 | 容器本身**不可聚焦**；初始焦点落在组内**第一个按钮**，之后逐个移动 |
| 键盘 | `Tab` 在按钮间移动，`Arrow keys` 在组件内部导航，`Space` / `Enter` 激活 |
| 语义 | 单选组用 `Role.RadioButton`，多选组用 `Role.Checkbox` |
| 标签 | 容器不需要标签；**每个按钮**按自身内容命名 |

## 8. 淘汰与替代

| 淘汰项 | 替代 | 依据 |
| --- | --- | --- |
| `SegmentedButton` + `Single/MultiChoiceSegmentedButtonRow` | connected `ButtonGroup` | `segmented-buttons/overview`：no longer recommended |
| 独立 segmented 的"必选一项"语义 | connected 组 + `Role.RadioButton` + 拒绝取消 | 同上 |

仅用于维护旧代码；新代码不要引入。

## 9. 陷阱

1. `overflowIndicator` 是 `ButtonGroup` 的**必填参数**，不是可选；漏了直接编译不过。
2. `ButtonGroup` 只负责 **standard** 变体；connecting 的逻辑不在它里面。
3. `ConnectedSpaceBetween` 是正 2dp，用负 margin 硬拼会错位。
4. `ToggleButtonDefaults.size` 默认 `Small`（40dp），不是 Medium。
5. 连通组三件套 shapes（leading / middle / trailing）必须按位置齐全，全用同一个会导致两端圆角错误。
6. 选中态的形状是**翻转**（round↔square），照抄 M2 的"只变颜色"会显得很平。
7. 不要给 `ButtonGroup` 传 `size` —— 它没有这个参数，尺寸靠组内按钮。
