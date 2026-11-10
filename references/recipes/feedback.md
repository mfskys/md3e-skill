# Feedback & Indicators — 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`ProgressIndicatorTokens.kt`、`{Linear,Circular}ProgressIndicatorTokens.kt`、
> `LoadingIndicatorTokens.kt`、`SnackbarTokens.kt`、`{Plain,Rich}TooltipTokens.kt`、`BadgeTokens.kt`、`DividerTokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 用哪个 —— 先看等待时长

| 预期等待 | 用什么 |
| --- | --- |
| 瞬时（< 200ms） | **不显示任何指示器**（闪一下反而更烦） |
| 短（200ms – 5s） | `LoadingIndicator`（不确定态，无进度百分比） |
| 长（> 5s） | `LinearProgressIndicator` / `CircularProgressIndicator`，能算进度就用 determinate |

规则是官方原表。判断依据是**时长**，不是"重要程度"。

## 1. 变体全集

| 类别 | Composable | 状态 | 用途 |
| --- | --- | --- | --- |
| 线性进度 | `LinearProgressIndicator` | ✅ | 长任务、可算进度 |
| 圆形进度 | `CircularProgressIndicator` | ✅ | 长任务、局部加载 |
| 线性波浪 | `LinearWavyProgressIndicator` | ✅ | M3E 表达力更强的线性进度 |
| 圆形波浪 | `CircularWavyProgressIndicator` | ✅ | 同上，圆形 |
| 加载（不定态） | `LoadingIndicator` | ✅ | M3E 新增，短时等待 |
| 容器内加载 | `ContainedLoadingIndicator` | ✅ | 放在按钮/卡片内部 |
| 提示条 | `Snackbar` + `SnackbarHost` | ✅ | 短暂反馈 + 一个动作 |
| 简单提示 | `PlainTooltip` | ✅ | 纯文字说明 |
| 富提示 | `RichTooltip` / `TooltipBox` | ✅ | 带标题 + 动作 |
| 角标 | `Badge` / `BadgedBox` | ✅ | 数量/状态点 |
| 分隔线 | `HorizontalDivider` / `VerticalDivider` | ✅ | 1dp |

## 2. 尺寸矩阵（源码 token）

### 线性进度

| Token | 值 |
| --- | --- |
| `Height` / `TrackThickness` / `ActiveThickness` | **4dp** |
| `TrackActiveSpace` | 4dp |
| `StopSize` | 4dp（末端圆点） |
| `ActiveWaveAmplitude` | 3dp |
| `ActiveWaveWavelength` | 40dp（不定态 20dp） |
| `WaveHeight` | 10dp |

### 圆形进度

| Token | 值 |
| --- | --- |
| `Size` | **40dp**（可 24–240dp） |
| `TrackThickness` / `ActiveThickness` | 4dp |
| `TrackActiveSpace` | 4dp |
| `ActiveWaveAmplitude` | 1.6dp |
| `ActiveWaveWavelength` | 15dp |
| `WaveSize` | 48dp |

### 加载指示器

| Token | 值 |
| --- | --- |
| `ContainerWidth` × `ContainerHeight` | **48dp × 48dp** |
| `ActiveSize` | 38dp |
| `ContainerShape` | `CornerFull` |

`ContainedLoadingIndicator` 是同一套尺寸，只是塞进父容器内部。

### Snackbar

| Token | 值 |
| --- | --- |
| `SingleLineContainerHeight` | **48dp** |
| `TwoLinesContainerHeight` | **68dp** |
| `ContainerShape` | `CornerExtraSmall` **4dp** |
| `ContainerElevation` | **`Level3`** (6dp) |
| `IconSize` | 24dp |
| 正文 / 动作字体 | `bodyMedium` / `labelLarge` |

### Tooltip

| | Plain | Rich |
| --- | --- | --- |
| `ContainerShape` | `CornerExtraSmall` **4dp** | `CornerMedium` **12dp** |
| `ContainerElevation` | — | `Level2` (3dp) |
| 标题字体 | — | `titleSmall` |
| 正文 | `bodySmall` | `bodyMedium` |
| 动作 | — | `labelLarge` |

### Badge / Divider

| Token | 值 |
| --- | --- |
| Badge `Size`（圆点） | **6dp** |
| Badge `LargeSize` | **16dp** |
| Badge 形状 / 字体 | `CornerFull` / `labelSmall` |
| Divider `Thickness` | **1dp** |

## 3. 形状

- 进度条 / 加载指示器：**全圆**（`CornerFull`）。
- Snackbar / PlainTooltip：**4dp**（`CornerExtraSmall`）。
- RichTooltip：**12dp**（`CornerMedium`）。
- Badge：全圆。

## 4. 颜色

| 元素 | 颜色 |
| --- | --- |
| Linear/Circular 已进度 | `primary` |
| 轨道 | `secondaryContainer`（线性）/ `surfaceContainerHighest`（部分场景） |
| Loading indicator | `primary` 或 `primaryContainer` |
| Snackbar 容器/文字 | `inverseSurface` / `inverseOnSurface` |
| Snackbar 动作 | `inversePrimary` |
| Tooltip（Plain） | `inverseSurface` / `inverseOnSurface` |
| Badge | `error` / `onError` |

## 5. 代码

### 5.1 进度：`progress` 是 **lambda**，不是 Float

```kotlin
// ✅ 确定进度
LinearProgressIndicator(progress = { 0.7f })

// ✅ 不确定进度
LinearProgressIndicator()          // 不传 progress

CircularProgressIndicator(progress = { 0.35f })
```

这是 M3 1.3 之后的变化：`progress: () -> Float`。写 `progress = 0.7f` 会编译失败。

### 5.2 波浪变体

```kotlin
LinearWavyProgressIndicator(progress = { 0.6f })
CircularWavyProgressIndicator(progress = { 0.6f })
```

波浪变体与普通变体**参数一致**，只是外观带振幅。整个产品**只用一种**（官方要求同一流程用同一变体）。

### 5.3 加载指示器

```kotlin
// 独立使用
LoadingIndicator()

// 塞进按钮/卡片内部
ContainedLoadingIndicator()
```

M3E 里这两个**不再需要 opt-in**（1.5.0-rc01）。

### 5.4 Snackbar

```kotlin
val hostState = remember { SnackbarHostState() }
val scope = rememberCoroutineScope()

Scaffold(
    snackbarHost = { SnackbarHost(hostState) },
) { padding ->
    Button(onClick = {
        scope.launch {
            hostState.showSnackbar(
                message = "已保存",
                actionLabel = "撤销",
                withDismissAction = true,
            )
        }
    }) { Text("保存") }
}
```

### 5.5 Tooltip

```kotlin
TooltipBox(
    positionProvider = TooltipDefaults.rememberPlainTooltipPositionProvider(),
    tooltip = { PlainTooltip { Text("添加收藏") } },
    state = rememberTooltipState(),
) {
    IconButton(onClick = {}) { Icon(Icons.Filled.Favorite, "收藏") }
}
```

### 5.6 Badge

```kotlin
BadgedBox(badge = { Badge { Text("12") } }) {
    IconButton(onClick = {}) { Icon(Icons.Filled.Email, "邮件") }
}

Badge()   // 无数字的小圆点（6dp）
```

### 5.7 Divider

```kotlin
HorizontalDivider()                                   // 1dp
HorizontalDivider(thickness = 1.dp, color = MaterialTheme.colorScheme.outlineVariant)
VerticalDivider()
```

## 6. 选型与设计规则

融合自官方 progress-indicators 与 loading-indicator 页面。

### 6.1 一致性

- 一个流程全程用**同一种变体**：某处刷新用圆形，别处也用圆形。
- 不要给列表里每个按钮都挂一个进度指示器。
- 表示**一组任务的整体进度**，不要逐个显示每个子任务。

### 6.2 确定 vs 不确定

- determinate 的数值必须**真实反映进度**，不能"假装跑到 90% 卡住"。
- 过程信息逐渐明确时，应该从 **indeterminate 切换到 determinate**。
- 低百分比时 active 段会退化成**一个点**，这是正常表现。

### 6.3 布局

- 圆形进度应**居中在正在加载的元素上**（按钮、卡片）。
- 线性进度**横跨所在元素的宽度**。
- 线性进度两端 padding **至少 4dp**。
- 圆形尺寸可 24–240dp，**不要超出这个范围**；波浪振幅随尺寸缩放。
- 线性进度在 RTL 语言下要**水平镜像**；圆形不需要。

### 6.4 对比度与 stop indicator

- 有 stop indicator（末端圆点）时，容器对比不足才需要它。
- **只有与周围 surface 对比 ≥ 3:1 时**才能去掉 stop indicator。
- 对比不够的另一种解法：active 色改成与按钮图标/文字同色，并**去掉 track**。

### 6.5 Snackbar

- 一条消息 + 最多一个动作。
- 动作要能撤销或恢复（Undo / Retry），不要放主流程动作。
- 不要用它承载必须阅读的信息（会被忽略）。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| 进度语义 | 用 `progressBarRangeInfo` / `stateDescription` 播报百分比 |
| 不确定态 | 明确 `indeterminate` 语义，读屏不要反复播报同一个值 |
| Snackbar | 通过 `liveRegion` 播报；动作按钮需可聚焦 |
| Tooltip | 不能承载**唯一**的关键信息，必须能通过其他方式获得 |
| Badge | 数字要有语义（"12 条未读"），不要只念"12" |
| 对比度 | active 与 track ≥ 3:1；Snackbar/Tooltip 文字 ≥ 4.5:1 |
| 动画 | 减少动效模式下，波浪振幅应关闭或弱化 |

## 8. 淘汰与替代

| 项 | 说明 |
| --- | --- |
| `progress = 0.7f`（Float） | 改为 `progress = { 0.7f }`（lambda），1.3 起 |
| `WavyProgressIndicator` 统称 | 实际是 `LinearWavyProgressIndicator` / `CircularWavyProgressIndicator` |
| 用 progress indicator 表示 < 5s 的等待 | 改用 `LoadingIndicator` |
| 给每个按钮挂进度 | 反例，只在一处表示整体进度 |

## 9. 陷阱

1. `progress` 是 **lambda**，写 `0.7f` 编译不过。
2. `LoadingIndicator` 的 `progress` 也是 `() -> Float`。
3. `LinearProgressIndicator` 与 `LinearWavyProgressIndicator` 是**两个** composable，参数一样但别混用。
4. Snackbar 高度 48dp（单行）/ 68dp（双行），不要用 `Modifier.height` 覆盖。
5. Snackbar 圆角只有 4dp，不是 pill。
6. RichTooltip 是 12dp 圆角，PlainTooltip 是 4dp —— 别写反。
7. Divider 默认是 `outlineVariant`，不是 `outline`。
