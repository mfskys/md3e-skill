# Navigation（导航）— 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`NavigationBarTokens.kt`、`NavigationRail{Collapsed,Expanded}Tokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 变体全集与替代关系

M3E 把导航组件整体重排了一遍。**三个基线组件被淘汰**，替代者不是同类项：

| 基线（淘汰） | 替代 | 说明 |
| --- | --- | --- |
| `NavigationBar` | `ShortNavigationBar` | 底部栏 → 更矮的短栏 |
| `NavigationRail` | `WideNavigationRail` | 窄轨 → 可展开的宽轨 |
| `NavigationDrawer`（Modal / Permanent / Dismissible） | `WideNavigationRail` / `ModalWideNavigationRail` | 抽屉 → 展开式导航轨 |

| 变体 | Composable | 状态 |
| --- | --- | --- |
| Short navigation bar | `ShortNavigationBar` + `ShortNavigationBarItem` | ✅ |
| Navigation bar（基线） | `NavigationBar` + `NavigationBarItem` | ⚠️ 不再推荐 |
| Wide navigation rail | `WideNavigationRail` / `ModalWideNavigationRail` | ✅ |
| Navigation rail（基线） | `NavigationRail` + `NavigationRailItem` | ⚠️ 不再推荐 |
| Navigation drawer | `ModalNavigationDrawer` 等 | ⚠️ 不再推荐 |
| Suite scaffold | `NavigationSuiteScaffold` | ✅ 跨断点自动切换（推荐用它省事） |

## 1. 尺寸矩阵（源码 token）

### 底部栏

| Token | 值 |
| --- | --- |
| `ContainerHeight` | **64dp** |
| `TallContainerHeight` | **80dp**（带更多内容时） |
| `ContainerElevation` | `Level2` |
| `ItemActiveIndicatorShape` | `CornerFull` |
| `ItemActiveIndicatorIconLabelSpace` | 4dp |
| `ItemBetweenSpace` | 0dp |
| `LabelTextFont` | `labelMedium` |

### 导航轨

| Token | Collapsed | Expanded |
| --- | --- | --- |
| `ContainerWidth` | **96dp**（narrow 变体 **80dp**） | **220dp – 360dp** |
| `TopSpace` | 44dp | 44dp |
| `ItemVerticalSpace` | 4dp | — |
| `ContainerElevation` | `Level0` | `Level0`（**modal 时 `Level2`**） |
| `ContainerShape` | `CornerNone` | `CornerNone`（**modal 时 `CornerLarge` 16dp**） |

`ShortNavigationBar` 没有独立 token 文件，复用 `NavigationBarTokens`（64dp）。

## 2. 形状

- 底部栏 / 导航轨容器：**直角**（`CornerNone`）。
- 激活指示器（active indicator）：**全圆角**（`CornerFull`）。
- Modal 宽轨：容器 **16dp 圆角** + `Level2` elevation，悬浮在内容之上。

## 3. 颜色

| 元素 | 规则 |
| --- | --- |
| 容器 | `surfaceContainer` 一档；不要用多个颜色区分 item |
| 激活图标 | `onSecondaryContainer`（在 `secondaryContainer` 指示器内） |
| 未激活图标/文字 | `onSurfaceVariant` |
| 激活指示器 | `secondaryContainer`，**只出现在当前 destination 上** |

激活/未激活图标与容器对比度**至少 3:1**。

## 4. 状态

| 状态 | 表现 |
| --- | --- |
| 未激活 | outlined 图标 + label |
| 激活 | filled 图标 + 指示器 + label |
| 无 filled 图标版本 | 图标改 **semibold** 字重 |
| 重新点击当前项 | 页面**滚回顶部** |
| 指示器动画 | **只在一个轴上移动**（表现同一平面） |

## 5. 代码

### 5.1 短导航栏（M3E 推荐）

```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
ShortNavigationBar {
    ShortNavigationBarItem(
        selected = selected == 0,
        onClick = { selected = 0 },
        icon = { Icon(Icons.Filled.Home, contentDescription = null) },
        label = { Text("Home") },
    )
    // 2–4 个更多
}
```

### 5.2 宽导航轨（M3E 推荐）

```kotlin
val state = rememberWideNavigationRailState()
WideNavigationRail(state = state) {
    NavigationRailItem(
        selected = selected == 0,
        onClick = { selected = 0 },
        icon = { Icon(Icons.Filled.Home, contentDescription = null) },
        label = { Text("Home") },
    )
    // 可再放一个 ExtendedFloatingActionButton（官方允许）
}
```

### 5.3 Modal 宽轨

```kotlin
ModalWideNavigationRail(
    state = rememberWideNavigationRailState(),
    properties = ModalWideNavigationRailProperties(),
) { /* items */ }
```

### 5.4 基线写法（仅维护旧代码）

```kotlin
// ⚠️ M3E 不再推荐
NavigationBar {
    NavigationBarItem(selected = ..., onClick = ..., icon = { ... }, label = { Text("Home") })
}
```

### 5.5 跨断点自动切换

```kotlin
NavigationSuiteScaffold(
    navigationSuiteItems = {
        item(selected = ..., onClick = ..., icon = { ... }, label = { Text("Home") })
    },
) { padding -> /* content */ }
```

`NavigationSuiteScaffold` 来自独立 artifact `material3-adaptive-navigation-suite`，
会根据窗口宽度自动在 bar / rail 之间切换 —— 不想手写断点判断就用它。

## 6. 选型与设计规则

融合自官方 navigation-bar、navigation-drawer、navigation-rail 页面。

### 6.1 按窗口宽度选

| 宽度 | 用什么 |
| --- | --- |
| compact（< 600dp） | `ShortNavigationBar`（≤5 项）或 `Tab`（3 项以下） |
| medium（600–839dp） | `NavigationRail` / `WideNavigationRail` |
| expanded（≥ 840dp） | `WideNavigationRail`；**不要用底部栏** |
| 5+ 个顶级 destination 或 > 1 级层级 | `WideNavigationRail` 展开态（原 drawer 场景） |

### 6.2 项目数量

- 底部栏**最多 5 项**。
- **少于 3 项不要用底部栏**，用 tabs。
- destination 的位置**固定**，不要滚动、不要重排。

### 6.3 标签

- **所有 item 都必需 label**，1–2 个词。
- **不要换行、不要截断、不要缩小字号**去凑一行。
- label 是图标含义的第二重表达，不能省。

### 6.4 图标

- 激活用 **filled**，未激活用 **outlined**。
- 没有 filled 版本时，激活态给图标加 **semibold** 字重。
- 不要用多个颜色或低对比色区分 item —— 会让人分不清哪个是当前页。

### 6.5 布局约束

- 底部栏固定在窗口底部、**占满宽度**，item 居中且各断点 padding 一致。
- **FAB 右对齐悬在底部栏上方，不要遮挡它**。
- 同一屏**不要用两个导航组件**。
- 底部栏可以被 dialog / bottom sheet / 键盘**临时**遮挡，但不能永久被挡。

### 6.6 交互

- **不要支持左右滑动切换 destination**（滑动留给 carousel、列表项等）。
- 重新点击当前 destination → **滚回页面顶部**。
- 指示器动画**只走一个轴**。
- 频繁切换的场景要保留各页状态（rememberSaveable / ViewModel）。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| 对比度 | 激活/未激活图标与容器 **≥ 3:1** |
| 标签 | 每个 item 都必须有可见 label，读屏依赖它 |
| 角色 | 底部栏用 `Role.Tab`，选中态由 `selected` 表达 |
| 触控目标 | 每个 item ≥ 48×48dp |
| 焦点顺序 | 按 destination 视觉顺序，不要跳 |
| 状态保持 | 切换页面后返回应恢复滚动位置（除非重新点击当前项） |

## 8. 淘汰与替代

| 淘汰项 | 替代 | 依据 |
| --- | --- | --- |
| `NavigationBar`（基线） | `ShortNavigationBar` | `navigation-bar/overview` |
| `NavigationRail`（基线） | `WideNavigationRail` | `navigation-rail/overview` |
| `Modal/Permanent/DismissibleNavigationDrawer` | `WideNavigationRail` / `ModalWideNavigationRail` | `navigation-drawer/overview` |

这三个仍可编译，但新设计不要选。**drawer 的"正确用法"也一并失效**——需要 5+ 个目的地时，
官方现在建议展开式导航轨，而不是抽屉。

## 9. 陷阱

1. `NavigationDrawer` 不是"可以继续用" —— 官方整段写的是 no longer recommended。
2. 底部栏 `NavigationBar` 和 `ShortNavigationBar` 都叫"导航栏"，但前者淘汰、后者推荐。
3. `WideNavigationRail` 的展开宽度是 **220–360dp 区间**，不是固定值。
4. Modal 宽轨才有 16dp 圆角和 `Level2`；内嵌宽轨是直角 + `Level0`。
5. 少于 3 个 destination 用底部栏是反例，应该用 tabs。
6. 不要给底部栏做横滑切换。
7. `NavigationSuiteScaffold` 在独立 artifact 里，忘加依赖会找不到。
