# Icon Buttons — 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`IconButton.kt`、`{XSmall,Small,Medium,Large,XLarge}IconButtonTokens.kt`、`ShapeTokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 变体全集（4 样式 × 2 模式 = 8 个 composable）

| 样式 | 一次性动作 | 可选中（toggle） | 状态 |
| --- | --- | --- | --- |
| Standard（无容器） | `IconButton` | `IconToggleButton` | ✅ |
| Filled | `FilledIconButton` | `FilledIconToggleButton` | ✅ |
| Filled tonal | `FilledTonalIconButton` | `FilledTonalIconToggleButton` | ✅ |
| Outlined | `OutlinedIconButton` | `OutlinedIconToggleButton` | ✅ |
| ~~Elevated~~ | **不存在** | — | 🚫 不要写 `ElevatedIconButton` |

`IconButton` 有**三个重载**（与 `Button` 同构）：

```kotlin
IconButton(onClick, modifier, enabled, colors, interactionSource, content)              // 最早，无 shape
IconButton(onClick, modifier, enabled, colors, interactionSource, shape, content)       // 单个 shape
IconButton(onClick, shapes: IconButtonShapes, ...)                                      // M3E，带按压形变
```

`IconButtonDefaults.standardShape` 是默认圆；要形变就用第三个重载。

## 1. 尺寸矩阵（源码 token）

| Token | XS | S（默认） | M | L | XL |
| --- | --- | --- | --- | --- | --- |
| `ContainerHeight` | **32dp** | **40dp** | **56dp** | **96dp** | **136dp** |
| `IconSize` | 20dp | 24dp | 24dp | 32dp | 40dp |
| `DefaultLeadingSpace` | 6dp | 8dp | 16dp | — | 48dp |
| `NarrowLeadingSpace` | 4dp | 4dp | 12dp | 16dp | 32dp |
| `WideLeadingSpace` | 10dp | 14dp | 24dp | — | 72dp |
| `OutlinedOutlineWidth` | 1dp | 1dp | 1dp | 2dp | 3dp |

`IconButton` **没有 `buttonSize` 参数**（只有 `ToggleButton` 有）。尺寸靠 `Modifier.size(...)`：

```kotlin
IconButton(
    onClick = {},
    modifier = Modifier.size(40.dp),   // = SmallIconButtonTokens.ContainerHeight
) { Icon(Icons.Filled.MoreVert, contentDescription = "More") }
```

Leading / Trailing 空间对应三种横向密度：`narrow`（最小点击区）、`default`、`wide`（更宽的内边距）。

## 2. 形状

| | XS | S | M | L | XL |
| --- | --- | --- | --- | --- | --- |
| Round（默认） | Full | Full | Full | Full | Full |
| Square | `CornerMedium` 12dp | `CornerMedium` 12dp | `CornerLarge` 16dp | `CornerExtraLarge` 28dp | `CornerExtraLarge` 28dp |
| Pressed | `CornerSmall` 8dp | `CornerSmall` 8dp | `CornerMedium` 12dp | `CornerLarge` 16dp | `CornerLarge` 16dp |
| **Selected（round）** | `CornerMedium` 12dp | `CornerMedium` 12dp | `CornerLarge` 16dp | `CornerExtraLarge` 28dp | `CornerExtraLarge` 28dp |
| **Selected（square）** | Full | Full | Full | Full | Full |

⚠️ 选中态是**形状翻转**：round 选中变方、square 选中变圆。这是 M3E 的有意设计，不是笔误。

## 3. 颜色矩阵（官方规范原表）

| 样式 | Default | Toggle 未选中 | Toggle 选中 |
| --- | --- | --- | --- |
| Standard | 无容器 / 图标 `onSurfaceVariant` | 同 Default | 无容器 / 图标 **`primary`** |
| Filled | 容器 `primary` / 图标 `onPrimary` | 容器 `surfaceContainer` / 图标 `onSurfaceVariant` | 容器 `primary` / 图标 `onPrimary` |
| Tonal | 容器 `secondaryContainer` / 图标 `onSecondaryContainer` | 同 Default | 容器 `secondary` / 图标 `onSecondary` |
| Outlined | `outline` 描边 / 图标 `onSurfaceVariant` | 同 Default | 容器 `inverseSurface` / 图标 `inverseOnSurface` |

`IconButtonDefaults` 还提供 `iconButtonVibrantColors()`（高饱和变体），用于需要更强表达力的场景。

## 4. 图标本身：filled vs outlined

| 场景 | 图标 |
| --- | --- |
| **默认（一次性动作）** | **filled** 图标 |
| Toggle 未选中 | **outlined** 图标 |
| Toggle 选中 | **filled** 图标 |
| 没有 filled 版本 | 选中时改用 **semibold** 字重 |

官方要求选中态**至少通过两个属性**表达（形状 + 颜色/填充），不能只靠颜色。这条只针对 toggle，
普通一次性按钮不适用。

## 5. 代码

### 5.1 最小可用

```kotlin
IconButton(onClick = {}) { Icon(Icons.Filled.MoreVert, contentDescription = "More") }
FilledIconButton(onClick = {}) { Icon(Icons.Filled.Add, contentDescription = "Add") }
FilledTonalIconButton(onClick = {}) { Icon(Icons.Filled.Edit, contentDescription = "Edit") }
OutlinedIconButton(onClick = {}) { Icon(Icons.Filled.Share, contentDescription = "Share") }
```

`contentDescription` **必填**（除非外层已有等价语义）。

### 5.2 带 tooltip

```kotlin
TooltipBox(
    positionProvider = TooltipDefaults.rememberPlainTooltipPositionProvider(),
    tooltip = { PlainTooltip { Text("Add to favorites") } },
    state = rememberTooltipState(),
) {
    IconToggleButton(
        checked = favorite,
        onCheckedChange = { favorite = it },
    ) {
        Icon(
            imageVector = if (favorite) Icons.Filled.Favorite else Icons.Outlined.FavoriteBorder,
            contentDescription = "Favorite",
        )
    }
}
```

### 5.3 带角标

```kotlin
BadgedBox(badge = { Badge { Text("3") } }) {
    IconButton(onClick = {}) { Icon(Icons.Filled.Notifications, contentDescription = "Alerts") }
}
```

### 5.4 五档尺寸

```kotlin
IconButton(
    onClick = {},
    shapes = IconButtonDefaults.shapes(shape = IconButtonDefaults.standardShape),
    modifier = Modifier.size(56.dp),   // MediumIconButtonTokens.ContainerHeight
) { Icon(Icons.Filled.MoreVert, contentDescription = "More", modifier = Modifier.size(24.dp)) }
```

图标尺寸取对应档位的 `IconSize`（20/24/24/32/40dp），不要统一写 24dp。

## 6. 选型与设计规则

融合自官方 icon-buttons guidelines 页。

### 6.1 用哪种样式

- **有容器的样式**（filled / tonal / outlined）在复杂背景上更容易辨识 —— 背景是图片、视频、彩色块时优先用它们。
- **filled 样式不要滥用**，一屏给一个主操作就够。
- 混用多个样式时，靠**颜色样式**把主操作区分出来。
- 重要性相同的按钮用**相同尺寸**；全部同等重要时就全用同一档。

### 6.2 强调与层级

- 用**尺寸和宽度**建立层级，而不只是颜色：主操作应当是最大、最宽或最醒目的那个。
- 不是每个页面都需要区分主次 —— 平级操作就统一尺寸。

### 6.3 toggle 的使用边界

- 只有**确实存在选中状态**时才用 toggle（收藏、点赞、静音）。
- **没有选中态的动作不要用 toggle**（如"更多/overflow"菜单），那是 `IconButton`。

### 6.4 图标与 tooltip

- 图标含义必须**无歧义**（心形 = 收藏）。
- 默认按钮用 filled 图标；toggle 按 §4 的规则切换。
- 配 tooltip 时，文案要**简短明确**。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| 对比度 | 图标与背景 **≥ 3:1**，低于 3:1 的颜色不要用 |
| 触控目标 | 至少 **48×48dp**；XS(32dp) / S(40dp) 必须补 `Modifier.minimumInteractiveComponentSize()` |
| 语义标签 | `contentDescription` 必填；纯装饰时可传 `null` 但要有其他语义来源 |
| 选中态 | 至少两个属性表达（形状 + 颜色/填充），不能只靠颜色 |
| 键盘 | `Tab` 到达，`Space` / `Enter` 激活 |

## 8. 淘汰与替代

| 项 | 说明 |
| --- | --- |
| `ElevatedIconButton` | **从未存在**，别写；要阴影用 `FilledIconButton` + `Modifier.shadow()` 或改用 `Button` |
| 单一 48dp 尺寸 | M3E 改为 32/40/56/96/136 五档 |
| `IconButton` 里套文字 | 图标按钮只放图标；要文字用 `Button` 或 `ExtendedFAB` |

## 9. 陷阱

1. `IconButton` 没有 `buttonSize`，别照抄 `ToggleButton` 的写法。
2. 五档尺寸不是自动的，必须显式 `Modifier.size(...)`，否则走默认 40dp 的 `defaultMinSize`。
3. 图标尺寸随档位变化（20/24/24/32/40dp），统一 24dp 会在大档位上显得很空。
4. 选中态形状是**翻转**的，不是"保持圆形只变色"。
5. `contentDescription` 漏写会让读屏念不出发音，且无法被 UI 测试定位。
6. `IconToggleButton` 的 `checked` 与 `onCheckedChange` 是**必填**，只传 `onClick` 会编译失败。
