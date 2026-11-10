# Tabs — 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`PrimaryNavigationTabTokens.kt`、`SecondaryNavigationTabTokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 变体全集

| 变体 | Composable | 状态 | 用途 |
| --- | --- | --- | --- |
| Primary | `PrimaryTabRow` + `Tab` | ✅ | 页面级主分区切换（有底部指示条） |
| Secondary | `SecondaryTabRow` + `Tab` | ✅ | 页面内的次级分区（无指示条，靠文字/色强调） |
| Scrollable | 上两者 + `Modifier.scrollableTabRow` 语义 | ✅ | 分区超过 3–5 个 |
| 基线 | `TabRow` | ⚠️ 旧写法 | 保留兼容，新代码用 Primary/Secondary |

## 1. 尺寸矩阵（源码 token）

### Primary

| Token | 值 |
| --- | --- |
| `ContainerHeight` | **48dp** |
| 带图标 + 文字时 | **64dp** |
| `ActiveIndicatorHeight` | **3dp** |
| `IconSize` | 24dp |
| `LabelTextFont` | `titleSmall` |
| `ContainerElevation` | `Level0` |
| 容器形状 | **直角**（`CornerNone`） |

### Secondary

| Token | 值 |
| --- | --- |
| `ContainerHeight` | **48dp** |
| `DividerHeight` | **1dp**（分区下方的分隔线） |
| `IconSize` | 24dp |
| `LabelTextFont` | `titleSmall` |
| 容器形状 | 直角 |

Primary 的指示器是**底部 3dp 实条**；Secondary 没有指示器，改在整体下方画 1dp 分隔线。

## 2. 形状

- tab 容器与指示条都是**直角**（`CornerNone`）。不要套圆角——圆角属于 chip / 按钮，不是 tab。

## 3. 颜色

| 元素 | 颜色 |
| --- | --- |
| 选中 tab 的文字/图标 | `primary` |
| 未选中 | `onSurfaceVariant` |
| Primary 指示条 | `primary` |
| Secondary 分隔线 | `outlineVariant` |
| 容器背景 | `surface`（透明） |

## 4. 状态

| 状态 | 表现 |
| --- | --- |
| 未选中 | `onSurfaceVariant` 文字/图标 |
| 选中 | `primary` 文字/图标 + Primary 有 3dp 指示条 |
| 按下 | state layer（全 tab 区域） |
| 禁用 | 降透明度，不可点 |

切换 tab 时**指示条平滑滑动**到新位置，不要瞬间跳变。

## 5. 代码

### 5.1 Primary

```kotlin
var selected by remember { mutableIntStateOf(0) }
val tabs = listOf("概览", "详情", "评论")

PrimaryTabRow(selectedTabIndex = selected) {
    tabs.forEachIndexed { i, label ->
        Tab(
            selected = selected == i,
            onClick = { selected = i },
            text = { Text(label) },
        )
    }
}
```

### 5.2 带图标

```kotlin
Tab(
    selected = selected == i,
    onClick = { selected = i },
    icon = { Icon(Icons.Filled.Home, contentDescription = null) },
    text = { Text("首页") },
)   // 高度自动变 64dp
```

### 5.3 Secondary

```kotlin
SecondaryTabRow(selectedTabIndex = selected) {
    tabs.forEachIndexed { i, label ->
        Tab(selected = selected == i, onClick = { selected = i }, text = { Text(label) })
    }
}
```

### 5.4 可滚动（分区多）

```kotlin
ScrollableTabRow(selectedTabIndex = selected, edgePadding = 16.dp) {
    tabs.forEachIndexed { i, label ->
        Tab(selected = selected == i, onClick = { selected = i }, text = { Text(label) })
    }
}
```

## 6. 选型与设计规则

- **2–5 个**分区用固定 tab；超过 5 个考虑可滚动或改用导航栏。
- 少于 3 个 destination 时：底部导航用 tab 更好（官方对 navigation bar 的建议），但页面内分区 2 个也可以。
- 分区之间是**平级**关系，不要表达层级。
- tab 标签**短**（1–2 个词），不要换行。
- Primary 用于页面主分区（切换整个内容区）；Secondary 用于页面内次级分区。
- 不要用 tab 承载需要滚动浏览的长内容——tab 是"切换"，不是"分页滚动"。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| 角色 | 每个 `Tab` 自带 `Role.Tab`；选中态由 `selected` 表达 |
| 标签 | 文字必须可见；纯图标 tab 需要 `contentDescription` |
| 键盘 | `Tab` 移动到 tab 组，左右方向键切换 |
| 触控目标 | 48dp 高度满足；可滚动 tab 注意宽度不要小于 48dp |
| 对比度 | 选中/未选中文字 ≥ 4.5:1；指示条 ≥ 3:1 |
| 状态保持 | 切换 tab 后返回应保留各 tab 的滚动位置 |

## 8. 淘汰与替代

| 项 | 说明 |
| --- | --- |
| `TabRow`（基线） | 新代码用 `PrimaryTabRow` / `SecondaryTabRow` |
| 圆角 tab | tab 是直角，圆角是 chip 的特征 |
| 用 tab 做分页 | tab 是分区切换，不是分页器 |

## 9. 陷阱

1. Primary 带图标时高度变 **64dp**（48 + 图标行），布局预留高度要跟着变。
2. Secondary **没有指示条**，它靠 1dp 分隔线，别写反。
3. tab 容器是直角，套 `RoundedCornerShape` 会和 chip 混淆。
4. `ScrollableTabRow` 的 `edgePadding` 默认不是 16dp，需要自己设。
5. 切换 tab 不要销毁内容状态（用 `rememberSaveable` 或 `pagerState` 保留）。
