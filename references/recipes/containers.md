# Containers — 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`Card.kt` + `{Filled,Elevated,Outlined}CardTokens.kt`、`DialogTokens.kt`、
> `SheetBottomTokens.kt`、`SegmentedMenuTokens.kt`、`MenuTokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 变体全集

| 类别 | Composable | 状态 |
| --- | --- | --- |
| Filled card | `Card` | ✅ |
| Elevated card | `ElevatedCard` | ✅ |
| Outlined card | `OutlinedCard` | ✅ |
| 基础对话框 | `AlertDialog` / `BasicAlertDialog` | ✅ |
| 全屏对话框 | 全屏 `Surface` + `Scaffold`（无专用 composable） | ✅ |
| 底部面板 | `ModalBottomSheet` / `BottomSheetScaffold` / `SheetDefaults` | ✅ |
| 拖拽手柄 | `VerticalDragHandle` + `VerticalDragHandleDefaults` | ✅ 见 §5.4 |
| 侧边面板 | **无** `SideSheet` API | 🚫 见 §8 |
| 标准菜单 | `DropdownMenu` / `ExposedDropdownMenu` / `DropdownMenuGroup` | ✅ |
| 分段菜单 | `SegmentedMenu`（M3E） | ✅ |
| 菜单项变体 | `DropdownMenuItem`（3 个重载）/ `CheckableDropdownMenuItem` / `SelectableDropdownMenuItem` | ✅ 见 §5.7 |
| 列表项 | `ListItem` / `SegmentedListItem` | ✅ |
| 滚动条 | `Modifier.nonInteractiveScrollbar` + `NonInteractiveScrollbarDefaults` | ✅ 见 §5.8 |

## 1. 尺寸矩阵（源码 token）

### 卡片

| 样式 | 容器色 | Elevation（静止） | 形状 |
| --- | --- | --- | --- |
| Filled | `surfaceContainerHighest` | **Level0 (0dp)** | `CornerMedium` **12dp** |
| Elevated | `surfaceContainerLow` | **Level1 (1dp)** | `CornerMedium` **12dp** |
| Outlined | `surface` + 1dp 描边 | **Level0 (0dp)** | `CornerMedium` **12dp** |

三者形状一致，区别只在容器色 / 高度 / 描边。交互态高度会变（拖拽到 `Level3`，聚焦/悬停各有一档）。

### 对话框

| Token | 值 |
| --- | --- |
| `ContainerShape` | `CornerExtraLarge` **28dp** |
| `ContainerElevation` | **`Level3` (6dp)** |
| `HeadlineFont` | `headlineSmall` |
| `SupportingTextFont` | `bodyMedium` |
| `ActionLabelTextFont` | `labelLarge` |
| `IconSize` | 24dp |

### 底部面板

| Token | 值 |
| --- | --- |
| Docked `ContainerShape` | `CornerExtraLargeTop`（**仅顶部 28dp**） |
| Docked `DragHandleWidth` × `Height` | **32dp × 4dp** |
| Docked 静止 Elevation | `Level1` (1dp) |
| 最小化后形状 | `CornerNone`（直角贴底） |

### 菜单

| Token | 值 |
| --- | --- |
| 分段菜单容器 | `CornerLarge` **16dp**，`Level2` (3dp) |
| 分段菜单项高 | **44dp** |
| 分段菜单单项形状 | `CornerMedium`（悬停/按下），选中态 `CornerFull` |
| 分段菜单组内 padding | 4dp |
| 分段菜单项间距 | 2dp（组内）/ 12dp（项间） |
| 分段菜单组形状 | `CornerSmall` **8dp** |

## 2. 形状

- Card：**12dp** 统一圆角（不是 16dp）。
- Dialog：**28dp**（`CornerExtraLarge`）。
- Modal bottom sheet：**仅顶部 28dp**；完全展开的最小化态变直角。
- Segmented menu：16dp 容器 + 8dp 分组 + 项在悬停时 12dp、选中时全圆。

## 3. 颜色

| 元素 | 颜色 |
| --- | --- |
| Filled card | `surfaceContainerHighest` |
| Elevated card | `surfaceContainerLow` + 1dp 阴影 |
| Outlined card | `surface` + `outlineVariant` 描边 |
| Dialog | `surfaceContainerHigh` |
| Bottom sheet | `surfaceContainerLow` |
| Menu | `surfaceContainer` |
| Scrim（遮罩） | `scrim` @ 32% |

## 4. 状态

| 状态 | Card | Dialog | Sheet |
| --- | --- | --- | --- |
| 静止 | Level0/1 | Level3 | Level1 |
| 拖拽 | Level3 | — | 跟手 + 吸附 |
| 禁用 | opacity **0.38** | — | — |
| 展开/收起 | — | 淡入淡出 + 缩放 | 拖拽手柄吸附 |

## 5. 代码

### 5.1 三种卡片

```kotlin
Card(onClick = {}) { Text("Filled") }              // 可点击用带 onClick 的重载
ElevatedCard { Text("Elevated") }
OutlinedCard { Text("Outlined") }
```

`CardDefaults.shape` = 12dp；`cardElevation()` 的交互态已按 token 配好，**不要手写 elevation 值**。

### 5.2 对话框（含两个动作的正确顺序）

```kotlin
AlertDialog(
    onDismissRequest = { open = false },
    icon = { Icon(Icons.Filled.Warning, contentDescription = null) },
    title = { Text("放弃未保存的修改？") },   // 具体问题，不要模糊
    text = { Text("离开后这些修改将无法恢复。") },
    confirmButton = {
        TextButton(onClick = { /* 放弃 */ open = false }) { Text("放弃") }
    },
    dismissButton = {
        TextButton(onClick = { open = false }) { Text("继续编辑") }
    },
)
```

**否定动作放左，确认放右**（`dismissButton` 在 `confirmButton` 左侧渲染）。

### 5.3 字段级错误不要用 dialog

```kotlin
// ✅ 行内
OutlinedTextField(isError = invalid, supportingText = { Text("邮箱格式不正确") })

// ⚠️ 只有与字段无关的错误才用 dialog
```

### 5.4 底部面板

```kotlin
val sheetState = rememberModalBottomSheetState(skipPartiallyExpanded = false)
var open by remember { mutableStateOf(false) }

if (open) {
    ModalBottomSheet(onDismissRequest = { open = false }, sheetState = sheetState) {
        // content；默认带拖拽手柄
    }
}
```

需要自定义手柄时用 `SheetDefaults.DragHandle()`（32×4dp）。

**手柄有独立的公开组件 `VerticalDragHandle`**（`DragHandle.kt`，358 行），比 `SheetDefaults.DragHandle()`
多出完整的尺寸/颜色/形状三维配置：

```kotlin
VerticalDragHandle(
    sizes = VerticalDragHandleDefaults.sizes(),
    colors = VerticalDragHandleDefaults.colors(),
    shapes = VerticalDragHandleDefaults.shapes(),
)
```

| 维度 | 类型 | 默认值对象 |
| --- | --- | --- |
| 尺寸 | `DragHandleSizes` | `VerticalDragHandleDefaults.sizes()` |
| 颜色 | `DragHandleColors` | `.colors()` / `.colors(color, pressedColor, draggedColor)` |
| 形状 | `DragHandleShapes` | `.shapes()` |

**尺寸不是 32×4dp。** 它和 bottom sheet 顶部那个横条手柄完全是两回事：

| | `SheetDefaults.DragHandle()` | `VerticalDragHandle` |
| --- | --- | --- |
| 形态 | **横向胶囊** | **竖向细条** |
| 静止 | 32dp × 4dp | **4dp × 48dp** |
| 按下 | — | **12dp × 52dp** |
| 拖动 | — | **12dp × 52dp** |
| 形状 | 全圆 | 静止 `CornerFull`，按下/拖动 `CornerMedium` |

数值来自 `DragHandleTokens`（`Width=4dp`、`Height=48dp`、`Pressed/DraggedWidth=12dp`、
`Pressed/DraggedHeight=52dp`、`ContainerWidth=24dp`）。所以 `VerticalDragHandle` 是给
**垂直边缘**用的拖动指示条，不是 bottom sheet 的顶部手柄；放错位置会显得又细又高。

它内部已经调用了 `minimumInteractiveComponentSize()`，**不必再手动补 48dp**；
同时也处理了 pressed / dragged 两种状态（`isDragged` 来自 interactionSource）。

### 5.5 菜单

```kotlin
Box {
    Button(onClick = { expanded = true }) { Text("选项") }
    DropdownMenu(expanded = expanded, onDismissRequest = { expanded = false }) {
        DropdownMenuItem(text = { Text("重命名") }, onClick = { })
        DropdownMenuItem(text = { Text("删除") }, onClick = { })
    }
}
```

### 5.6 列表项

```kotlin
ListItem(
    headlineContent = { Text("标题") },
    supportingContent = { Text("副标题") },
    leadingContent = { Icon(Icons.Filled.Person, contentDescription = null) },
    trailingContent = { Icon(Icons.Filled.MoreVert, contentDescription = "更多") },
)

// 分段列表项：多段内容各自成块，段与段之间有形状分隔
SegmentedListItem(
    headlineContent = { Text("标题") },
    supportingContent = { Text("副标题") },
    leadingContent = { Icon(Icons.Filled.Person, contentDescription = null) },
    trailingContent = { Icon(Icons.Filled.MoreVert, contentDescription = "更多") },
)
```

### 5.7 菜单项：`DropdownMenuItem` 有三个重载

不是三个不同组件，是**同一个名字**按参数区分（`api/current.txt` 里被编译成
`DropdownMenuItem` / `DropdownMenuItemChecked` / `DropdownMenuItemSelected` 三个符号）：

```kotlin
// ① 普通动作项
DropdownMenuItem(onClick = { }, text = { Text("重命名") })

// ② 可勾选（checked + onCheckedChange，带勾选语义）
DropdownMenuItem(
    checked = checked,
    onCheckedChange = { checked = it },
    text = { Text("显示网格") },
    leadingIcon = { Icon(Icons.Filled.GridView, null) },
    checkedLeadingIcon = { Icon(Icons.Filled.Check, null) },   // 勾选时替换前导图标
)

// ③ 选中态（selected + onClick，点击仍触发动作）
DropdownMenuItem(
    selected = selected,
    onClick = { selected = true },
    text = { Text("按日期排序") },
    selectedLeadingIcon = { Icon(Icons.Filled.Check, null) },
)
```

`CheckableDropdownMenuItem(...)` 与 ②、`SelectableDropdownMenuItem(...)` 与 ③ **参数完全一致**，
是并存的别名。用哪个都行，但别在同一份代码里混用两种写法。

菜单分组与新弹窗：

```kotlin
DropdownMenuPopup(
    expanded = expanded,
    onDismissRequest = { expanded = false },
    popupPositionProvider = /* DropdownMenuPopupPositionProvider */,
) {
    DropdownMenuGroup(shapes = MenuDefaults.shapes()) {
        DropdownMenuItem(onClick = { }, text = { Text("复制") })
        DropdownMenuItem(onClick = { }, text = { Text("粘贴") })
    }
}
```

`MenuDefaults` 是菜单形状的唯一来源（**不叫** `MenuItemDefaults`）：

| 成员 | 用途 |
| --- | --- |
| `leadingGroupShape` / `middleGroupShape` / `trailingGroupShape` | 分组在首/中/尾时的外观 |
| `standaloneGroupShape` / `inactiveGroupShape` | 独立分组 / 未激活 |
| `leadingItemShape` / `middleItemShape` / `trailingItemShape` / `standaloneItemShape` | 菜单项的四种位置形态 |
| `selectedItemShape` | 选中态形状（与 chip 一样，形状参与选中表达） |
| `GroupSpacing` | 组间距 |
| `TonalElevation` / `ShadowElevation` | `Level0` / `MenuTokens.ContainerElevation` |

### 5.8 滚动条（`Modifier.nonInteractiveScrollbar`）

M3 的滚动条是**纯视觉**的，不能拖拽（名字里的 `nonInteractive` 就是这个意思）：

```kotlin
val listState = rememberLazyListState()
val indicator = listState.scrollIndicatorState        // 类型是 ScrollIndicatorState?（可空！）
val scrollbar = if (indicator != null) {
    Modifier.nonInteractiveScrollbar(indicator, orientation = Orientation.Vertical)
} else {
    Modifier
}

LazyColumn(
    state = listState,
    modifier = Modifier.fillMaxSize().then(scrollbar),
) { items(100) { Text("Item $it") } }
```

**必须判空**：`scrollIndicatorState` 是 `ScrollIndicatorState?`，而 `nonInteractiveScrollbar`
的第一个参数非空。这是官方 sample 的写法，不是可选的防御。

`NonInteractiveScrollbarDefaults`（`scrollbar` 无实验注解，不需要 opt-in）：

| 成员 | 值 |
| --- | --- |
| `Thickness` | **4dp** |
| `ThumbMinLength` | 24dp |
| `ThumbMaxLengthFraction` | 0.9f |
| `ThumbOpacity` | 0.7f |
| `thumbColor` | `outline` @ 70% |
| `ThumbFadeDurationMillis` | 250 |
| `ThumbFadeDelayMillis` | 400 |

行为要点：

- 垂直内容画在 **end 边缘**（尊重 RTL），水平内容画在底部。
- 内容**严格大于**视口时才出现。
- 默认滚动时显示、停止后淡出；`isFadeEnabled = false` 可常显。
- 内部用的是 `androidx.compose.foundation.ScrollIndicatorState`
  （`LazyListState` / `ScrollState` 等通过 `.scrollIndicatorState` 暴露），不是 material3 自己定义的。

## 6. 选型与设计规则

融合自官方 dialogs、bottom-sheets、cards、menus 页面。

### 6.1 Dialog 还是 Snackbar？官方给了判据

| 组件 | 重要性 | 是否需要动作 |
| --- | --- | --- |
| **Snackbar** | 低 | **可选**：可以没有按钮，可以自动消失 |
| **Dialog** | 高 | **必需**：阻塞主内容直到用户确认 |

所以：

- **低/中优先级信息不要用 dialog**，用 snackbar。
- dialog 只用于需要明确决策、确认或关键阻塞信息。

### 6.2 Dialog 的具体要求

- 标题要是**具体问题**（"放弃未保存的修改？"），不要模糊（"确定吗？"）。
- 全屏对话框的 app bar 里**不要放长标题**（会截断导致误解），长标题放内容区。
- **确认动作在用户做出选择前要禁用**；**否定动作永不禁用**。
- **否定在左、确认在右**；堆叠布局时确认在上、否定在下。
- 单一动作只在"确认已知信息"时使用；有明显两个选择时必须给两个。
- 字段相关错误显示在**行内**，只有与字段无关的错误才放进 dialog。
- 不要让确认动作去关闭全屏对话框。

### 6.3 Bottom sheet

- 适合放"与当前上下文相关的次级内容/操作"，不要放阻塞式确认（那是 dialog）。
- 拖拽手柄 32×4dp，别自己画。
- 部分展开（peek）与完全展开之间用 `skipPartiallyExpanded` 控制。

### 6.4 Card

- 卡片承载"单一主题"的内容 + 该主题的操作。
- 三种卡片**只选一种表达层级**，不要在同一列表里混用三种。
- 可点击卡片用带 `onClick` 的重载（自带涟漪与语义），不要在外面套 `Modifier.clickable`。

### 6.5 Menu

- 菜单项文案用动词（重命名、删除），不要用名词。
- 危险操作（删除）放在末尾，并考虑用 `error` 色。
- 超过 ~7 项应考虑改用底部面板或独立页面。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| Dialog | 打开后焦点移入 dialog，关闭后归还触发元素；必须有 `onDismissRequest` 或显式关闭按钮 |
| Scrim | 点击遮罩关闭的行为要和 `onDismissRequest` 一致 |
| Sheet | 读屏应能识别"底部面板"；拖拽手柄需要可操作语义 |
| Card | 可点击卡片必须有 `onClick` 语义（否则读屏不认为是按钮） |
| Menu | `DropdownMenuItem` 自带 `Role.MenuItem`；不要用裸 `Text` 拼菜单 |
| ListItem | `headlineContent` 必须存在；行内图标给 `contentDescription` 或 `null` |
| 对比度 | 卡片内容与容器 ≥ 4.5:1；描边 ≥ 3:1 |
| 触控目标 | 菜单项、列表项都 ≥ 48dp（44dp 的分段菜单项要补足） |

## 8. 淘汰与替代

| 项 | 说明 |
| --- | --- |
| `SideSheet` / `ModalSideSheet` | **Compose 没有这个 API**（已核对 `api/current.txt`）。宽屏用 `WideNavigationRail`，需要面板就用 bottom sheet 换布局或自建 |
| 卡片 16dp 圆角 | 官方是 **12dp**（`CornerMedium`） |
| 用 dialog 承载低优先级提示 | 改用 snackbar |
| 自己给卡片套 `Modifier.clickable` | 用带 `onClick` 的卡片重载 |

## 9. 陷阱

1. `SideSheet` 不存在，凭直觉写会直接编译失败。
2. 卡片圆角是 **12dp**，不是 16dp 也不是 28dp。
3. Dialog 圆角是 **28dp**，比卡片大得多。
4. Bottom sheet 只有**顶部** 28dp 圆角，底部是直角。
5. Dialog 的确认/否定按钮顺序：`dismissButton` 在左，`confirmButton` 在右。
6. 给 Card 传 `elevation = CardDefaults.cardElevation(6.dp)` 会破坏交互态高度，用默认值。
7. 44dp 的分段菜单项低于 48dp 触控标准，外层要补。
8. `ModalBottomSheet` 忘记 `onDismissRequest` 会导致无法关闭。
9. **滚动条必须判空**：`listState.scrollIndicatorState` 类型是 `ScrollIndicatorState?`，
   而 `Modifier.nonInteractiveScrollbar` 的第一个参数非空。直接传会编译失败。
10. **滚动条不可拖拽**。它是纯视觉的（`nonInteractive`），想拖拽得自己实现 pointerInput。
11. `DropdownMenuItem` 的三个重载靠**参数名**区分：`onClick` / `checked + onCheckedChange` /
    `selected + onClick`。传错组合会匹配到不想用的那个，或直接编译失败。
12. 菜单默认值对象是 **`MenuDefaults`**，没有 `MenuItemDefaults` / `MenuGroupDefaults`。
13. `SegmentedListItem` 与 `ListItem` 参数一致，但外观是分段块状；别在有分隔线的紧凑列表里用它。
