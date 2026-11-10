# Text Fields — 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`FilledTextFieldTokens.kt`、`OutlinedTextFieldTokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 变体全集

| 变体 | Composable | 状态 | 说明 |
| --- | --- | --- | --- |
| Filled | `TextField` | ✅ | 顶部圆角 + 下划线指示器 |
| Outlined | `OutlinedTextField` | ✅ | 全圆角 + 四周描边 |
| 密码 | `SecureTextField` / `OutlinedSecureTextField` | ✅ | 自带可见性切换 |
| 滚动选择 | `ScrollField` | ✅ | 滚轮式选择器，M3E 新增 |
| 搜索 | `SearchBar` / `AppBarWithSearch` | ✅ | 见 §5.5 |

**两套 API 并存**（这是最容易写错的地方）：

| API | 签名 | 建议 |
| --- | --- | --- |
| value-based（经典） | `TextField(value: String, onValueChange: (String) -> Unit, ...)` | 简单表单可用 |
| state-based（新） | `TextField(state: TextFieldState, ...)` | **优先**；支持异步校验、`InputTransformation` |

M3E 起 `DateInput` / `TimeInput` 已经迁到 state-based 的 text-field API。

## 1. 尺寸矩阵（源码 token）

| Token | Filled | Outlined |
| --- | --- | --- |
| `ContainerHeight` | 56dp（由内容撑开） | **56dp** |
| `ContainerShape` | **`CornerExtraSmallTop`**（仅顶部 4dp 圆角） | **`CornerExtraSmall`**（全 4dp） |
| 指示器 / 描边（静止） | 1dp 下划线 | 1dp 描边 |
| 指示器 / 描边（聚焦） | **2dp** | **2dp** |
| 指示器（悬停/禁用） | 1dp | 1dp |
| `LeadingIconSize` | 24dp | 24dp |
| `TrailingIconSize` | 24dp | 24dp |
| `InputFont` / `LabelFont` | `bodyLarge` | `bodyLarge` |
| `SupportingFont` | `bodySmall` | `bodySmall` |

**圆角只有 4dp** —— 输入框不是按钮，不要套 12/16dp 圆角，更不要套 pill。

## 2. 形状

- Filled：左上、右上 **4dp**，左下、右下 **0dp**（贴地）。
- Outlined：四角 **4dp**。
- 聚焦时**不改变形状**，只加粗描边/指示器（1dp → 2dp）。

## 3. 颜色

| 元素 | Filled | Outlined |
| --- | --- | --- |
| 容器 | `surfaceContainerHighest` | 透明 |
| 指示器 / 描边（静止） | `onSurfaceVariant` | `outline` |
| 指示器 / 描边（聚焦） | `primary` | `primary` |
| 输入文字 | `onSurface` | `onSurface` |
| Label（浮起后） | `onSurfaceVariant`（聚焦时 `primary`） | 同左 |
| Supporting text | `onSurfaceVariant` | `onSurfaceVariant` |
| 错误态 | `error` | `error` |

## 4. 状态

| 状态 | 表现 |
| --- | --- |
| Enabled | 1dp 指示器/描边，label 居中 |
| Focused | 2dp 指示器/描边，label 上移到顶部，指示器 `primary` |
| Hovered | 1dp，可加轻微色调 |
| Error | 指示器/描边 `error` + `supportingText` 换成错误文案 |
| Disabled | 全部降透明度，不可交互 |

## 5. 代码

### 5.1 最小可用（必须有 label）

```kotlin
var text by remember { mutableStateOf("") }

OutlinedTextField(
    value = text,
    onValueChange = { text = it },
    label = { Text("Email") },           // 必填，不能只靠 placeholder
    singleLine = true,
)
```

### 5.2 state-based（推荐）

```kotlin
val state = rememberTextFieldState()

TextField(
    state = state,
    label = { Text("Email") },
    supportingText = { Text("我们会发送确认邮件") },
    isError = false,
    singleLine = true,
)
```

### 5.3 错误态：**替换** supporting text，不要叠加

```kotlin
OutlinedTextField(
    value = text,
    onValueChange = { text = it },
    label = { Text("Email") },
    isError = emailInvalid,
    supportingText = {
        Text(if (emailInvalid) "请输入有效的邮箱地址" else "我们会发送确认邮件")
    },
)
```

同一时刻只显示一条辅助文案 —— 叠加会让下方内容整体跳动。

### 5.4 密码

```kotlin
var password by remember { mutableStateOf("") }
var visible by remember { mutableStateOf(false) }

OutlinedTextField(
    value = password,
    onValueChange = { password = it },
    label = { Text("Password") },
    visualTransformation = if (visible) VisualTransformation.None else PasswordVisualTransformation(),
    trailingIcon = {
        IconButton(onClick = { visible = !visible }) {
            Icon(
                if (visible) Icons.Filled.VisibilityOff else Icons.Filled.Visibility,
                contentDescription = if (visible) "隐藏密码" else "显示密码",
            )
        }
    },
)
```

`SecureTextField` 可省掉这套手写逻辑。

### 5.5 搜索

```kotlin
// 顶部搜索栏（M3E）
AppBarWithSearch(
    state = rememberSearchBarState(),
    inputField = {
        SearchBarDefaults.InputField(
            searchBarState = rememberSearchBarState(),
            textFieldState = rememberTextFieldState(),
            onSearch = { },
        )
    },
) { /* 结果区 */ }
```

## 6. 选型与设计规则

融合自官方 text-fields guidelines 页。

### 6.1 两种变体不要混在同一区域

- 一个界面可以同时用 filled 和 outlined，但必须**按区域划分**。
- **不要在同一个表单里相邻混用**两种变体。

### 6.2 Label（硬性要求）

- **每个输入框都必须有 label**。placeholder 不能代替 label（输入后 placeholder 就消失了）。
- label 与输入文字左对齐，**始终可见**；聚焦时从中间移到顶部。
- **不要截断、不要换行**，保持短而清晰。
- 相邻输入框的 label 要对齐到容器左边缘。

### 6.3 单行 / 多行 / 文本区域

| 类型 | 行为 | 适用 |
| --- | --- | --- |
| 单行 | 文字超出时向左滚动 | 短输入（邮箱、姓名） |
| 多行 | 容器向下扩展、文字换行 | 中等长度（备注） |
| 文本区域 | 固定高度 + 垂直滚动 | Web 上的长回答 |

单行字段**不适合**长文本；需要长输入就用多行或文本区域。

### 6.4 辅助文本与错误

- 辅助文本理想是一行，说明"这个字段用来做什么"。
- 错误文本只描述**如何避免错误**；有多个可能的错误时，针对**最可能**的那个写。
- 错误文本**替换**辅助文本，不要并列显示。
- 长错误可能换行，要把输入框之间的竖直间距留够，避免挤压布局。

### 6.5 宽度与断点

- compact 断点可全宽。
- medium / expanded 断点要**用弹性边距或容器约束**，不要让输入框横跨整个大屏。
- 不要同时固定 margin 和固定排版 —— 流体布局下会拉出超长输入框。

### 6.6 密度

- **不要默认给输入框加 density**。density 会把触控目标压到 48px 以下。
- 需要更紧凑时，提供**用户可选**的密度设置（换主题/换布局），而不是默认压缩。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| Label | 必须可被读屏关联到输入框（用 `label` 参数，而不是旁边放个 `Text`） |
| 错误播报 | `isError = true` + `supportingText` 里的错误文案；必要时 `liveRegion` |
| 触控目标 | ≥ 48×48dp；**不要靠 density 压小** |
| 图标语义 | 尾部图标按钮必须有 `contentDescription`（如"显示密码"） |
| 键盘类型 | `keyboardOptions` 设对类型（`Email` / `Password` / `Number`） |
| 字符限制 | 有上限时显式展示计数器，并在接近上限时提示 |
| 对比度 | label / 辅助文本与容器 ≥ 4.5:1 |

## 8. 淘汰与替代

| 项 | 说明 |
| --- | --- |
| placeholder 当 label | 官方要求每个字段都有 label |
| `TopSearchBar` | → `AppBarWithSearch` |
| `DateInput` / `TimeInput` 旧签名 | alpha29 起迁到 `TextFieldState` API |
| 默认 density | 会把目标压到 48px 以下，改为用户可选 |
| filled 底部大圆角 | 官方是**仅顶部** 4dp 圆角 |

## 9. 陷阱

1. 输入框圆角是 **4dp**，不是按钮那种 12/16dp，更不是 pill。
2. Filled 变体只有**顶部**有圆角（`CornerExtraSmallTop`），底部是直角。
3. 聚焦时只加粗描边（1dp→2dp），**不改形状**。
4. 错误文本与辅助文本要**互斥**，同时显示会让下方内容跳动。
5. `placeholder` 在输入后消失，不能当 label 用。
6. value-based 与 state-based 两套 API 别混着写；新代码优先 state-based。
7. 给 `TextField` 套 `Modifier.height(...)` 固定高度会截断多行内容。
