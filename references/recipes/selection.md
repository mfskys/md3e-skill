# Selection Controls — 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`CheckboxTokens.kt`、`RadioButtonTokens.kt`、`SwitchTokens.kt`、`SliderTokens.kt`、`ChipsTokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 用哪个控件 —— 先看这张表

选错控件是最常见的错误，比参数写错更致命。

| 场景 | 正确控件 | 反例 |
| --- | --- | --- |
| 列表里**多选**（0–N 个） | `Checkbox` | ❌ 用 `Switch` |
| 列表里**单选**（1 个） | `RadioButton` | ❌ 用 `Switch` |
| 单个功能**开/关**，立即生效 | `Switch` | ❌ 用 `Checkbox` |
| 在**两个对立选项**间切换 | **connected `ButtonGroup`** | ❌ 用 `Switch` |
| **触发一个动作**（CTA） | `Button` | ❌ 用 `Switch` |
| 连续/区间数值 | `Slider` / `RangeSlider` | ❌ 用 Chip 堆 |
| 筛选、标记、输入标签 | `FilterChip` / `InputChip` / `AssistChip` / `SuggestionChip` | ❌ 用 Button |

三条官方原话，直接决定了上表：

- "Avoid using switches to toggle between opposing options" → 用 connected button group。
- "A switch can't replace a button" → 用户预期 CTA 是按钮。
- "If a list consists of multiple options, don't use switches. Instead, use checkboxes."

## 1. 变体全集

| 控件 | Composable | 状态 |
| --- | --- | --- |
| 复选框 | `Checkbox`、`TriStateCheckbox` | ✅ |
| 单选 | `RadioButton` | ✅ |
| 开关 | `Switch` | ✅ |
| 滑块 | `Slider`、`RangeSlider`、`SliderState`、`RangeSliderState` | ✅ |
| 筛选条 | `FilterChip` | ✅ |
| 输入条 | `InputChip` | ✅ |
| 辅助条 | `AssistChip` | ✅ |
| 建议条 | `SuggestionChip` | ✅ |

## 2. 尺寸矩阵（源码 token）

### 复选框

| Token | 值 |
| --- | --- |
| `ContainerSize` | **18dp** |
| `IconSize` | 18dp |
| `StateLayerSize` | **40dp**（触控反馈范围） |
| `UnselectedOutlineWidth` | 2dp |
| `SelectedOutlineWidth` | 0dp（选中后无描边） |

### 单选

| Token | 值 |
| --- | --- |
| `IconSize` | **20dp** |
| `StateLayerSize` | 40dp |

### 开关

| Token | 值 |
| --- | --- |
| `TrackWidth` × `TrackHeight` | **52dp × 32dp** |
| `TrackShape` / `HandleShape` | `CornerFull` |
| `TrackOutlineWidth` | 2dp |
| 未选中 handle | **16dp** |
| 选中 handle | **24dp** |
| 按下 handle | **28dp** |
| 带图标 handle | 24dp（`IconHandle*`） |
| handle 内图标 | 16dp |

开关的手柄尺寸**随状态变化**（16 → 24 → 28dp），这是 M3E 的形态动效，不要写死 24dp。

### 滑块（M3E 改成了"细手柄 + 粗轨道"）

| Token | 值 |
| --- | --- |
| `HandleWidth` × `HandleHeight` | **4dp × 44dp** |
| `ActiveHandleWidth` | 4dp |
| 按下 / 聚焦 / 悬停 / 禁用手柄宽 | 2dp / 2dp / 4dp / 4dp |
| `ActiveTrackHeight` / `InactiveTrackHeight` | **16dp** |
| `ActiveHandlePadding` | 6dp |
| `ActiveHandleLeadingSpace` / `TrailingSpace` | 6dp |
| `HandleShape` / `TrackShape` | `CornerFull` |

手柄是**竖直细条**（4×44dp），轨道是**16dp 粗条** —— 与 M2 的小圆点完全不同。

### Chip

| Token | 值 |
| --- | --- |
| `Height` | **32dp** |
| `LabelText` | `labelLarge` |
| `LeadingIconSize` / `TrailingIconSize` | 18dp |
| `AvatarSize` | 24dp（全圆） |
| `UnselectedShape` | `CornerMedium` **12dp** |
| `SelectedShape` | `CornerFull`（全圆） |
| `PressedShape` | `CornerSmall` **8dp** |
| `UnselectedOutlineWidth` | 1dp |
| `SelectedOutlineWidth` | 0dp |
| `ContainerElevation` | `Level0`（拖拽时 `Level4`） |

## 3. 形状

- Checkbox / Radio：容器 18dp / 20dp，未选中是 2dp 描边圆角方 / 圆。
- Switch：整条轨道全圆，手柄全圆。
- Slider：手柄与轨道都全圆。
- Chip：**未选中 12dp 圆角 → 选中变全圆**（形状参与选中态表达）。

## 4. 颜色

| 控件 | 未选中 | 选中 |
| --- | --- | --- |
| Checkbox | `onSurfaceVariant` 描边 | `primary` 填充 + `onPrimary` 勾 |
| Radio | `onSurfaceVariant` 描边 | `primary` 填充 + `onPrimary` 圆点 |
| Switch | `surfaceContainerHighest` 轨道 + `outline` 描边 | `primary` 轨道 + `onPrimary` 手柄 |
| Slider | `secondaryContainer` 轨道 + `primary` 已选区 | 同左 + `primary` 手柄 |
| FilterChip | 描边 + `onSurfaceVariant` | `secondaryContainer` + `onSecondaryContainer` |

## 5. 代码

### 5.1 复选框（含三态 + 父级全选）

```kotlin
Checkbox(checked = checked, onCheckedChange = { checked = it })

// 三态：父级
TriStateCheckbox(
    state = if (allSelected) ToggleableState.On
            else if (noneSelected) ToggleableState.Off
            else ToggleableState.Indeterminate,
    onClick = { /* 全选/全不选 */ },
)
```

### 5.2 单选（一组必须配 RadioGroup 语义）

```kotlin
Column(Modifier.selectableGroup()) {
    options.forEachIndexed { i, label ->
        Row(
            Modifier.selectable(
                selected = selected == i,
                onClick = { selected = i },
                role = Role.RadioButton,
            )
        ) {
            RadioButton(selected = selected == i, onClick = null)  // null：由外层处理
            Text(label)
        }
    }
}
```

`RadioButton` 单独用没有互斥语义，必须靠外层 `selectableGroup()` + `selectable(role = Role.RadioButton)`。

### 5.3 开关（立即生效 + 明确图标）

```kotlin
Switch(
    checked = enabled,
    onCheckedChange = { enabled = it /* 立刻生效，不要等保存 */ },
    thumbContent = if (enabled) {
        { Icon(Icons.Filled.Check, contentDescription = null, modifier = Modifier.size(16.dp)) }
    } else {
        { Icon(Icons.Filled.Close, contentDescription = null, modifier = Modifier.size(16.dp)) }
    },
)
```

外部配一行内联 label，描述"打开后会怎样"。

### 5.4 滑块

```kotlin
Slider(
    value = value,
    onValueChange = { value = it },   // alpha29 起必填
    valueRange = 0f..100f,
)

// 带状态对象
val state = rememberSliderState(value = 0.5f)
Slider(state = state)
```

### 5.5 Chip

```kotlin
FilterChip(
    selected = selected,
    onClick = { selected = !selected },
    label = { Text("Filters") },
    leadingIcon = { Icon(Icons.Filled.Done, contentDescription = null, modifier = Modifier.size(18.dp)) },
)
```

## 6. 选型与设计规则

融合自官方 checkbox、switch、sliders、chips 的 guidelines 页。

### 6.1 复选框

- 用于"一个或多个"选项；父级复选框一键全选/全不选。
- 列表多选**必须**用 checkbox，不要用 switch（占空间且语义错）。

### 6.2 开关

- 只在**立即生效**的开/关场景用（无需"保存"按钮）。
- **对立选项**（A vs B）用 connected button group，不是 switch。
- 不能替代按钮。
- 需要多选且要保存的，用 checkbox。
- 手柄图标要**明确二元**（✓ / ✕）；**不要**用月亮、编辑这类暧昧图标。
- 开关里**不要塞文字**（字号会小到不可读），用图标。
- 必须配**行内 label**，描述"打开时的效果"。

### 6.3 滑块

- 用于连续或区间取值；离散档位少（≤5）时优先考虑 chips 或分段控制。
- M3E 的滑块是"细手柄 + 粗轨道"，别按 M2 的小圆点样式去写。
- 需要显示当前值时，把数值放在外部文字上，不要塞进手柄。

### 6.4 Chip

- `FilterChip`：多选筛选，选中态用形状 + 颜色双重表达。
- `InputChip`：展示已输入内容（如标签），可带删除按钮。
- `AssistChip`：辅助性动作/提示，不表达选中态。
- `SuggestionChip`：动态建议（如搜索联想），不要用于固定选项。
- chip 高度固定 32dp，**不要**手动拉高来"对齐按钮"；要更大就用按钮。

## 7. 无障碍

| 控件 | 要求 |
| --- | --- |
| Checkbox | 必须有 `onCheckedChange` 或外层 `toggleable(role = Role.Checkbox)`；独立 label 用 `Modifier.clickable` 把整行可点 |
| Radio | 必须 `selectableGroup()` + `Role.RadioButton`，否则读屏报"按钮"而不是"单选" |
| Switch | `Role.Switch`；label 描述开启后的状态，不要写成动作名 |
| Slider | 提供 `stateDescription` 或语义 `progressBarRangeInfo`，让读屏能播报当前值 |
| Chip | `Role.Checkbox`（FilterChip）/ `Role.Button`（AssistChip） |
| 触控目标 | 所有控件 ≥ 48×48dp；checkbox/radio 的 state layer 是 40dp，需外层补到 48dp |
| 对比度 | 未选中描边与背景 ≥ 3:1；选中填充与勾/点 ≥ 4.5:1 |

## 8. 淘汰与替代

| 项 | 说明 |
| --- | --- |
| M2 小圆点 Slider | M3E 改为 4×44dp 细手柄 + 16dp 轨道 |
| `Slider`/`RangeSlider` 可选 `onValueChange` | alpha29 起**必填**且参数位置变化，旧写法编译失败 |
| 用 switch 表达对立选项 | 改用 connected `ButtonGroup` |

## 9. 陷阱

1. `RadioButton` 的 `onClick = null` 是**正常写法**（由外层 `selectable` 处理），不是漏参。
2. 忘了 `selectableGroup()` → 多组单选互相干扰。
3. Switch 手柄尺寸随状态变化（16/24/28dp），写死会丢动效。
4. Slider 手柄是 4dp 宽的竖条，不是圆点。
5. Chip 选中态会**变形状**（12dp → 全圆），只改颜色不够。
6. `Checkbox` 的 state layer 只有 40dp，小于 48dp 的触控目标要求，外层要补。
7. 静态列表里用 `Modifier.clickable` 让整行可点，比只让 18dp 的方框可点好得多。
