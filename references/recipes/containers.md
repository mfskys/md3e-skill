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
| 侧边面板 | **无** `SideSheet` API | 🚫 见 §8 |
| 标准菜单 | `DropdownMenu` / `ExposedDropdownMenu` | ✅ |
| 分段菜单 | `SegmentedMenu`（M3E） | ✅ |
| 列表项 | `ListItem` | ✅ |

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
```

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
