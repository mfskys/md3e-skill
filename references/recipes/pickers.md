# Pickers（日期 / 时间选择）— 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`DatePickerModalTokens.kt`、`DateInputModalTokens.kt`、`TimePickerTokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 变体全集

| 控件 | Composable | 模态尺寸 | 状态 |
| --- | --- | --- | --- |
| 日期选择（日历） | `DatePickerDialog` + `DatePicker` | **360 × 568dp** | ✅ |
| 日期范围（日历） | `DatePickerDialog` + `DateRangePicker` | 360 × 568dp | ✅ |
| 日期输入（文字） | `DatePickerDialog` + `DateInput` | **328 × 512dp** | ✅ |
| 停靠日期选择 | `DatePicker`（非模态，嵌在页面里） | 跟随容器 | ✅ |
| 时间选择（表盘） | `TimePickerDialog` + `TimePicker` | 跟随内容 | ✅ |
| 时间输入（文字） | `TimePickerDialog` + `TimeInput` | 跟随内容 | ✅ |

⚠️ `DateInput` / `TimeInput` 在 **alpha29** 起迁到了 `TextFieldState` API，旧签名已变。

## 1. 尺寸矩阵（源码 token）

### 日期选择（模态日历）

| Token | 值 |
| --- | --- |
| 容器 | **360dp × 568dp** |
| `ContainerShape` | `CornerExtraLarge` **28dp** |
| `ContainerElevation` | **`Level3` (6dp)** |
| `HeaderContainerHeight` | **120dp** |
| Header 标题字体 | `headlineLarge` |
| Header 辅助文字 | `labelLarge` |
| 单个日期格 | **40dp × 40dp**，全圆 |
| 日期文字 | `bodyLarge` |
| 今天（today）描边 | 1dp |
| 年份格 | **72dp × 36dp** |
| 星期标签 | `bodyLarge` |

### 日期输入（文字模态）

| Token | 值 |
| --- | --- |
| 容器 | **328dp × 512dp** |
| 形状 / 高度 | 28dp / `Level3` |
| Header | 328dp × 120dp |

比日历版**窄 32dp、矮 56dp** —— 因为它没有日历网格。

### 时间选择（表盘）

| Token | 值 |
| --- | --- |
| `ClockDialContainerSize` | **256dp** |
| 表盘形状 | `CornerFull` |
| 选择器手柄 | **48dp**，全圆 |
| 选择器中心点 | **8dp** |
| 轨道宽度 | **2dp** |
| 容器形状 / 高度 | 28dp / `Level3` |
| 头部字体 | `labelMedium` |

## 2. 形状

- 日期 / 时间弹窗容器：**28dp**（`CornerExtraLarge`）。
- 日期格、年份格、表盘、手柄：**全圆**（`CornerFull`）。
- 停靠日期选择不套弹窗容器，直接嵌进页面。

## 3. 颜色

| 元素 | 颜色 |
| --- | --- |
| 弹窗容器 | `surfaceContainerHigh` |
| Header 背景 | `surfaceContainerHigh`（范围选择时另有 `primaryContainer` 强调） |
| 选中日期格 | `primary` / `onPrimary` |
| 今天（未选中） | 1dp `primary` 描边 |
| 范围选择中间段 | `secondaryContainer` / `onSecondaryContainer` |
| 星期标签 | `onSurfaceVariant` |
| 表盘 | `surfaceContainerHighest`，指针 `primary` |

## 4. 状态

| 状态 | 表现 |
| --- | --- |
| 未选中 | 透明容器 + 数字 |
| 悬停/聚焦 | state layer 40dp 全圆 |
| 今天 | 1dp 描边 |
| 选中 | `primary` 填充 + 全圆 |
| 范围 | 两端圆角、中间连成带状 |
| 禁用日期 | 降透明度，不可点 |

## 5. 代码

### 5.1 日历选择

```kotlin
val state = rememberDatePickerState(
    initialSelectedDateMillis = null,
    selectableDates = object : SelectableDates {
        override fun isSelectableDate(utcTimeMillis: Long): Boolean =
            utcTimeMillis >= todayMillis
    },
)

if (showDialog) {
    DatePickerDialog(
        onDismissRequest = { showDialog = false },
        confirmButton = {
            TextButton(
                onClick = { /* 读取 state.selectedDateMillis */ showDialog = false },
            ) { Text("确定") }
        },
        dismissButton = {
            TextButton(onClick = { showDialog = false }) { Text("取消") }
        },
    ) {
        DatePicker(state = state)
    }
}
```

### 5.2 日期范围

```kotlin
val rangeState = rememberDateRangePickerState()
DatePickerDialog(onDismissRequest = { }, confirmButton = { }) {
    DateRangePicker(state = rangeState)
}
```

### 5.3 日期输入（不需要日历视图时）

```kotlin
DatePickerDialog(onDismissRequest = { }, confirmButton = { }) {
    DateInput(state = rememberDatePickerState())   // 328×512dp，比日历窄
}
```

### 5.4 时间选择

```kotlin
val timeState = rememberTimePickerState(
    initialHour = 14,
    initialMinute = 20,
    is24Hour = true,
)

TimePicker(state = timeState)        // 表盘 256dp

// 或纯输入
TimeInput(state = timeState)
```

### 5.5 停靠式（嵌在页面里，不弹窗）

```kotlin
DatePicker(
    state = rememberDatePickerState(),
    title = null,
    headline = null,
    modifier = Modifier.padding(16.dp),
)
```

停靠式不套 28dp 弹窗容器，直接跟随父容器形状。

## 6. 选型与设计规则

融合自官方 date-pickers 与 time-pickers 页面。

### 6.1 日历还是输入

- **不需要日历视图**的场景（表单里填日期），**模态日期输入可作默认**。
- 更简单时，直接用带 hint 的 `TextField` 让人输入日期。
- 需要浏览/比较多个日期、选范围 → 日历。

### 6.2 远距离日期不要用日历

- **不要用模态日期选择器去选远期日期**（如生日、几十年前的日期）。
- 这类场景用**日期输入**或**停靠式**选择器 —— 日历翻页翻到崩溃。

### 6.3 尺寸

- **不要响应式放大日期选择器**。它固定 360×568dp（输入版 328×512dp）。
- 需要更大就改用停靠式，而不是把弹窗拉大。

### 6.4 时间

- 12/24 小时制跟随系统区域设置（`is24Hour`），不要硬编码。
- 表盘 256dp 是固定值，不要缩。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| 日期格语义 | 每格需播报完整日期（"2026 年 11 月 10 日，星期二"），不能只念"10" |
| 选中状态 | 用 `selected` 语义，不要只靠颜色 |
| 今天 | 用 `semantics` 标注"今天"，不要只靠描边 |
| 键盘 | 网格内用方向键移动，`Enter` 选中 |
| 触控目标 | 日期格 40dp < 48dp，外层要补或保证间隔足够 |
| 时间 | 表盘需要可键盘操作，且播报当前时分 |
| 对比度 | 数字与容器 ≥ 4.5:1；今天描边 ≥ 3:1 |

## 8. 淘汰与替代

| 项 | 说明 |
| --- | --- |
| `DateInput` / `TimeInput` 旧签名 | alpha29 起迁到 `TextFieldState` |
| 用模态日历选生日/远期日期 | 改用日期输入或停靠式 |
| 响应式放大日期弹窗 | 固定尺寸，需要大就换停靠式 |
| `DateInputModal` 的 328dp 当成 360dp | 两者宽度差 32dp，不要混用 |

## 9. 陷阱

1. `DatePicker` 与 `DateRangePicker` 是**两个不同 composable**，state 也不同。
2. `DateInput` 的弹窗尺寸（328×512）比 `DatePicker`（360×568）小，写死 360 会错。
3. 所有日期 API 用 **UTC 毫秒**，展示时要换算本地时区。
4. `TimePicker` 的 `is24Hour` 要跟随系统，别硬编码 `true`。
5. 日期格只有 40dp，低于 48dp 触控标准。
6. 停靠式选择器不要套弹窗的 28dp 圆角。
