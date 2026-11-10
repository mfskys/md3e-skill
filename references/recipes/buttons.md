# Buttons — 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`Button.kt`、`Button{XSmall,Small,Medium,Large,XLarge}Tokens.kt`、`ShapeTokens.kt`（源码常量）
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 变体全集

### 0.1 点击按钮 — 5 种样式

| # | 样式 | Composable | 状态 | 容器色 → 内容色 |
| --- | --- | --- | --- | --- |
| A | Elevated | `ElevatedButton` | ✅ | `surfaceContainerLow` → `primary`（elevation 1，disabled 0） |
| B | Filled | `Button` | ✅ | `primary` → `onPrimary` |
| C | Tonal | `FilledTonalButton` | ✅ | `secondaryContainer` → `onSecondaryContainer` |
| D | Outlined | `OutlinedButton` | ✅ | `surface` + `outline` 描边 → `onSurfaceVariant` |
| E | Text | `TextButton` | ✅ | 透明 → `primary` |

### 0.2 开关按钮 — 4 种样式

`ToggleButton` 家族有独立的选中态配色，且**没有 text 样式**（官方明确："Toggle buttons don't use the text style"）。

| 样式 | Composable | 未选中容器 → 内容 | 选中容器 → 内容 |
| --- | --- | --- | --- |
| Filled | `ToggleButton` | `surfaceContainer` → `onSurfaceVariant` | `primary` → `onPrimary` |
| Tonal | `FilledTonalToggleButton` | `secondaryContainer` → `onSecondaryContainer` | `secondary` → `onSecondary` |
| Elevated | `ElevatedToggleButton` | `surfaceContainerLow` → `primary` | `primary` → `onPrimary` |
| Outlined | `OutlinedToggleButton` | `outline` 描边 → `onSurfaceVariant` | `inverseSurface` → `inverseOnSurface` |

### 0.3 已淘汰 / 不推荐（保留说明，不删）

| 变体 | 状态 | 说明 |
| --- | --- | --- |
| Neutral text button | ⚠️ | M2 遗留的中性色 text button，M3E 起不再推荐；用标准 `TextButton` 的新色彩映射 |
| Small 按钮 24dp 内容内边距 | ⚠️ | 官方：`16dp` 推荐、`24dp` 不再推荐。`ButtonDefaults` 默认已是 16dp 体系 |
| 48dp 固定高度按钮 | ⚠️ | 旧 M3 单一尺寸；M3E 改为 32/40/56/96/136 五档 |

## 1. 尺寸矩阵（源码 token）

| Token | XS | S（默认） | M | L | XL |
| --- | --- | --- | --- | --- | --- |
| `ContainerHeight` | **32dp** | **40dp** | **56dp** | **96dp** | **136dp** |
| `LeadingSpace` / `TrailingSpace` | 16dp | 16dp | 24dp | 48dp | 64dp |
| `IconSize` | 20dp | 20dp | 24dp | 32dp | 40dp |
| `IconLabelSpace` | 8dp | 8dp | 8dp | 12dp | 16dp |
| `OutlinedOutlineWidth` | 1dp | 1dp | 1dp | 2dp | 3dp |

`ButtonDefaults` 里对应的常量：

```kotlin
ButtonDefaults.ExtraSmallContainerHeight   // 32.dp  (ButtonXSmallTokens)
ButtonDefaults.MinHeight                   // 40.dp  (ButtonSmallTokens) ← Small 档没有 SmallContainerHeight
ButtonDefaults.MediumContainerHeight       // 56.dp
ButtonDefaults.LargeContainerHeight        // 96.dp
ButtonDefaults.ExtraLargeContainerHeight   // 136.dp

ButtonDefaults.ExtraSmallIconSize / SmallIconSize / MediumIconSize / LargeIconSize / ExtraLargeIconSize
ButtonDefaults.ExtraSmallIconSpacing / IconSpacing / MediumIconSpacing / LargeIconSpacing / ExtraLargeIconSpacing
```

⚠️ `MinHeight` 不是常量 40dp，它按输入设备切换：

```kotlin
public val MinHeight: Dp
    get() = if (shouldUsePrecisionPointerComponentSizing.value) 36.dp
            else ButtonSmallTokens.ContainerHeight   // 40.dp
```

鼠标/触控笔场景（`LocalIsEmphasizedPointerInput` 之类精确指针）下小按钮会缩到 36dp。写死 40dp 会与框架不一致。

## 2. 形状矩阵

`ShapeTokens` 的实际 dp（`CornerFull = CircleShape`）：

| ShapeKey | 实际值 | 用在 |
| --- | --- | --- |
| `CornerExtraSmall` | 4dp | — |
| `CornerSmall` | **8dp** | pressed XS / S |
| `CornerMedium` | **12dp** | square XS / S，pressed M |
| `CornerLarge` | **16dp** | square M，pressed L / XL |
| `CornerExtraLarge` | **28dp** | square L / XL |
| `CornerExtraLargeIncreased` | 32dp | — |
| `CornerFull` | `CircleShape` | round 全部档位 |

**每档的 round / square / pressed 组合**（`Button*Tokens.kt` 原值）：

| | XS | S | M | L | XL |
| --- | --- | --- | --- | --- | --- |
| Round（默认） | Full | Full | Full | Full | Full |
| Square | `CornerMedium` 12dp | `CornerMedium` 12dp | `CornerLarge` 16dp | `CornerExtraLarge` 28dp | `CornerExtraLarge` 28dp |
| Pressed | `CornerSmall` 8dp | `CornerSmall` 8dp | `CornerMedium` 12dp | `CornerLarge` 16dp | `CornerLarge` 16dp |
| Selected（toggle） | Full | Full | Full | Full | Full |

这与官方设计规范 buttons 页的 corner sizes 表**逐格一致**，可互相印证。

## 3. 颜色矩阵（官方规范原表）

| 样式 | Default | Toggle 未选中 | Toggle 选中 |
| --- | --- | --- | --- |
| Elevated | container `surfaceContainerLow` / 内容 `primary` | 同 Default | container `primary` / 内容 `onPrimary` |
| Filled | container `primary` / 内容 `onPrimary` | container `surfaceContainer` / 内容 `onSurfaceVariant` | container `primary` / 内容 `onPrimary` |
| Tonal | container `secondaryContainer` / 内容 `onSecondaryContainer` | 同 Default | container `secondary` / 内容 `onSecondary` |
| Outlined | container `outline` 描边 / 内容 `onSurfaceVariant` | 同 Default | container `inverseSurface` / 内容 `inverseOnSurface` |
| Text | 内容 `primary` | —（toggle 无 text 样式） | — |

官方允许换角色，但**容器与文字对比度必须 ≥ 3:1**（例如 `tertiary` / `onTertiary`）。

## 4. 状态

| 状态 | 表现 |
| --- | --- |
| Enabled | 上述颜色 |
| Disabled | 内容色/容器色按 tokens 的 disabled opacity 淡化；elevated 的 elevation 从 1 降到 0 |
| Hovered | state layer 叠加（桌面端） |
| Focused | focus 环，叠加层更高 |
| Pressed | state layer 最高 + **形状收缩**（见第 2 节 pressed 列） |

状态叠加层由 `Surface` + `interactionSource` 自动处理，**不要手写 alpha 覆盖**。

## 5. 代码

### 5.1 最小可用

```kotlin
Button(onClick = {}) { Text("Filled") }
FilledTonalButton(onClick = {}) { Text("Tonal") }
ElevatedButton(onClick = {}) { Text("Elevated") }
OutlinedButton(onClick = {}) { Text("Outlined") }
TextButton(onClick = {}) { Text("Text") }
```

默认是 **Small 档**（40dp 高，round，`labelLarge`）。

### 5.2 五档尺寸 — 这是最容易写错的地方

`Button` **没有 `size` 参数**。M3E 的做法是：用高度常量 + `*For(height)` 工厂函数取全套参数。

```kotlin
@Composable
fun MdButton(
    onClick: () -> Unit,
    text: String,
    height: Dp = ButtonDefaults.MinHeight,   // 32 / 40 / 56 / 96 / 136
) {
    Button(
        onClick = onClick,
        shapes = ButtonDefaults.shapesFor(height),
        contentPadding = ButtonDefaults.contentPaddingFor(height),
        modifier = Modifier.heightIn(min = height),
    ) { Text(text) }
}
```

`height` 取 `ExtraSmallContainerHeight` / `MinHeight` / `MediumContainerHeight` /
`LargeContainerHeight` / `ExtraLargeContainerHeight` 就是五档。

三个工厂函数会把形状、内边距、图标尺寸一起算对：

```kotlin
ButtonDefaults.shapesFor(buttonHeight: Dp): ButtonShapes
ButtonDefaults.contentPaddingFor(buttonHeight: Dp, hasStartIcon: Boolean = false, hasEndIcon: Boolean = false): PaddingValues
ButtonDefaults.iconSizeFor(buttonHeight: Dp): Dp
ButtonDefaults.iconSpacingFor(buttonHeight: Dp): Dp
```

### 5.3 带图标

```kotlin
val height = ButtonDefaults.MediumContainerHeight
Button(
    onClick = {},
    shapes = ButtonDefaults.shapesFor(height),
    contentPadding = ButtonDefaults.contentPaddingFor(height, hasStartIcon = true),
    modifier = Modifier.heightIn(min = height),
) {
    Icon(
        Icons.Filled.Add,
        contentDescription = null,
        modifier = Modifier.size(ButtonDefaults.iconSizeFor(height)),
    )
    Spacer(Modifier.width(ButtonDefaults.iconSpacingFor(height)))
    Text("Add")
}
```

图标**不带** `contentDescription`（装饰性），语义由文字承担。

### 5.4 方角（square）

```kotlin
Button(
    onClick = {},
    shape = ButtonDefaults.squareShape,
    contentPadding = ButtonDefaults.MediumContentPadding,
    modifier = Modifier.heightIn(min = ButtonDefaults.MediumContainerHeight),
) { Text("Square") }
```

方角按钮的圆角随尺寸变化（12/12/16/28/28dp），**不要自己写 `RoundedCornerShape(16.dp)`**。

### 5.5 开关按钮

```kotlin
ToggleButton(
    checked = checked,
    onCheckedChange = onCheckedChange,
    buttonSize = ToggleButtonSize.Medium,   // Toggle 才有 buttonSize，一键切全套
    shapes = ToggleButtonDefaults.shapesFor(ToggleButtonSize.Medium),
) { Text("Favorite") }
```

`ToggleButtonSize` 五档见 `m3e-api-signatures.md`；默认是 `Small`。

### 5.6 按压变形（shapes 重载）

`Button` 有两个重载，**只有接受 `ButtonShapes` 的那个才有按压形变**：

```kotlin
// ✅ M3E：有按压收缩动画
Button(
    onClick = {},
    shapes = ButtonDefaults.shapesFor(ButtonDefaults.MediumContainerHeight),
) { Text("Expressive") }

// ⚠️ 旧重载：shape 是单个 Shape，按压不变形
Button(
    onClick = {},
    shape = ButtonDefaults.shape,
) { Text("Classic") }
```

后者不是错误，只是退回 stable 行为。要 M3E 观感就用 `shapes =`。

### 5.7 只有图标

用 `IconButton`，不要用空文字的 `Button`（见 `icon-buttons.md`）。

### 5.8 分割按钮（SplitButton）—— 没有 `SplitButton` 这个 composable

```kotlin
SplitButtonLayout(
    leadingButton = {
        SplitButtonDefaults.LeadingButton(onClick = { /* 主操作 */ }) {
            Text("发送")
        }
    },
    trailingButton = {
        SplitButtonDefaults.TrailingButton(
            checked = expanded,
            onCheckedChange = { expanded = it },
        ) {
            Icon(Icons.Filled.ArrowDropDown, contentDescription = "更多发送选项")
        }
    },
)
```

尺寸（`SplitButtonSmallTokens`，其余档位结构相同）：

| Token | Small |
| --- | --- |
| `ContainerHeight` | 40dp |
| `ContainerShape` | `CornerFull` |
| 两半之间的 `BetweenSpace` | **2dp** |
| leading 内边距 | 16dp 左 / 12dp 右 |
| trailing 图标 | 22dp |
| trailing 内边距 | 13dp 左右对称 |

- 两半各自有独立形状：左半是**左圆右方**，右半是**左方右圆**，由
  `SplitButtonDefaults.leadingButtonShapesFor(buttonHeight)` /
  `trailingButtonShapesFor(buttonHeight)` 给出，**不要手写圆角**。
- 变体：`Tonal*` / `Outlined*` / `Elevated*` 前缀的 `LeadingButton` / `TrailingButton`。
- 尺寸档：XSmall / Small / Medium / Large / XLarge 对应的 token 文件。

## 6. 选型与设计规则

融合自官方 buttons 的 guidelines 与 overview 页——图片丢掉后仍然成立的那部分。

### 6.1 什么时候用按钮

- 按钮用于**离散动作**（"Use buttons for discrete actions"）。
- 不要用按钮堆满界面。低优先级动作放 overflow menu、icon button 或 text link。
- 常见落位：对话框、模态、表单、卡片、工具栏，以及 standard 按钮组内部。

### 6.2 五个样式怎么选（按强调度从高到低）

| 样式 | 强调度 | 选用规则 |
| --- | --- | --- |
| Filled | 最高 | **一页只放一个**主操作；过度使用会破坏视觉层级 |
| Tonal | 中高 | 次要动作，比 filled 弱、比 outlined 稳 |
| Elevated | 中 | 仅在需要与背景拉开距离时使用；阴影已经很强，别滥用 |
| Outlined | 中低 | ⚠️ 与 chips 视觉非常接近，能用 filled/tonal 就别用；**叠在图片/视频上必须自定义对比容器色** |
| Text | 最低 | 多个选项并列时的最低优先级动作；容器只在 hover/focus/pressed 时出现，因此文字色必须能与普通正文区分 |

补充：elevated 与 filled 都应放在**简洁背景**上，不要压在图片、视频这类复杂视觉上。

### 6.3 文字

- **sentence case**：只有首词和专有名词大写（`Book with Flights`，不是 `BOOK WITH FLIGHTS`）。
- 长度 **1–3 个词**最理想。
- **不要换行、不要截断**，label 始终单行完整可见。
- 字号放大到 200% 后仍应控制在两行内；超了就必须提供"一次点击即可访问完整内容"的替代方式。

### 6.4 图标

- 图标放在 label **之前**（LTR）/ **之后**（RTL）。
- **最多一个图标**，绝不放两个。
- 图标与文字**成组居中**，不要让它们分贴按钮两端。
- 图标语义要直白，能独立被理解。

### 6.5 尺寸与布局

- 容器宽度**随 label 自适应**，不能窄于文字宽度（文字溢出容器是错的）。
- 可以响应式拉伸，但**不要拉成"又长又扁、内容很少"的条**。
- 大窗口里限制按钮宽度，或让它与其他元素并排。
- 大屏与小屏之间**保持元素顺序一致**，读屏和键盘导航依赖这个顺序。

### 6.6 Toggle 按钮专题

- 用于**二元选择**（Save / Favorite），按下时颜色、形状、label 都可变化。
- 未选中用 **outlined 图标**，选中用 **filled 图标**；没有 filled 版本就**加粗**图标。
- 两个状态的 **label 长度要接近**，否则按钮宽度会跳。

## 7. 无障碍

融合自官方 buttons 的 accessibility 页。

| 项 | 要求 |
| --- | --- |
| 对比度 | 启用态与背景 **≥ 3:1**。elevated / filled / tonal 量的是**容器**；outlined / text 量的是**文字** |
| 语义标签 | 必须与可见文字一致（`Done` / `Send` / `Reply`）；可以追加语境，但不能替换可见文字 |
| 键盘 | `Tab` 到达按钮，`Space` / `Enter` 激活 |
| 触控目标 | **48×48dp**。XS(32dp) / S(40dp) 必须用 `Modifier.minimumInteractiveComponentSize()` 补足 |
| 200% 字号 | label 控制在两行内；如被截断，提供单次点击可获取完整内容的路径 |
| 快速连点（Web） | 预期连续点击时使用修改过的 motion curve，避免重叠动画产生共振 |
| 装饰图标 | 文字按钮内的图标 `contentDescription = null`；纯图标按钮必须给标签（走 `IconButton`） |

## 8. 淘汰与替代

| 淘汰项 | 替代 | 依据 |
| --- | --- | --- |
| Neutral text button | 标准 `TextButton`（新色彩映射） | `buttons/overview` |
| Small 按钮 24dp 内容内边距 | 16dp（`ButtonDefaults` 默认体系） | `buttons/specs` |
| 单一 48dp 尺寸 | 五档 32/40/56/96/136dp | `buttons/specs` |
| Toggle 的 text 样式 | **不存在**，别硬造 | `buttons/specs` |

## 9. 陷阱

1. `Button` 没有 `size` 参数 —— 那是 `ToggleButton` 才有的。五档靠 `shapesFor(height)` + `contentPaddingFor(height)` + `Modifier.heightIn(min = height)`。
2. `ButtonDefaults.MinHeight` 在精确指针模式下是 **36dp**，不是 40dp。
3. 不存在 `ButtonDefaults.SmallContainerHeight`；Small 档就是 `MinHeight`。
4. 只传 `contentPadding` 不传 `Modifier.heightIn`，高度仍被内部 `defaultMinSize(40dp)` 兜底 —— 大档位"看起来没变大"就是这个原因。
5. `shape` 与 `shapes` 是两个不同重载；用 `shape` 会丢掉按压收缩动画。
6. 未选中 toggle 的容器色**不是透明**（`surfaceContainer` / `secondaryContainer` / `surfaceContainerLow`），照抄 M2 写法会错。
7. 默认形状是 `CornerFull`（`CircleShape`），不是 `RoundedCornerShape(20.dp)`。
