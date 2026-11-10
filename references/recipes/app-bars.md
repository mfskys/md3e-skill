# App Bars（应用栏）— 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`AppBar{Small,Medium,Large}Tokens.kt`、`AppBar{Medium,Large}FlexibleTokens.kt`、
> `AppBarTokens.kt`、`BottomAppBarTokens.kt`、`DockedToolbarTokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 变体全集

| 变体 | Composable | 状态 | 说明 |
| --- | --- | --- | --- |
| Small | `TopAppBar` | ✅ | 64dp，标题单行 |
| Center aligned | `CenterAlignedTopAppBar` | ✅ | 64dp，标题居中 |
| Medium flexible | `MediumFlexibleTopAppBar` | ✅ | 112 ↔ 136dp，可带副标题 |
| Large flexible | `LargeFlexibleTopAppBar` | ✅ | 120 ↔ 152dp，可带副标题 |
| Two rows | `TwoRowsTopAppBar` | ✅ | 双行标题 |
| ~~Medium~~ | `MediumTopAppBar` | ⚠️ **不再推荐** | 112dp 固定，被 medium flexible 取代 |
| ~~Large~~ | `LargeTopAppBar` | ⚠️ **不再推荐** | 152dp 固定，被 large flexible 取代 |
| ~~Bottom~~ | `BottomAppBar` | ⚠️ **不再推荐** | 80dp，改用 docked `HorizontalFloatingToolbar`（64dp） |
| Bottom flexible | `FlexibleBottomAppBar` | ✅ | 保留的动态底栏 |

M3E 的判断很直接：**固定高度会折叠的 app bar 全部让位给 flexible 版本**。

## 1. 尺寸矩阵（源码 token）

### 顶部

| 变体 | 折叠高度 | 展开高度 | 标题字体 | 副标题字体 |
| --- | --- | --- | --- | --- |
| Small | **64dp** | — | `titleLarge` | `labelMedium` |
| Medium（淘汰） | 112dp | — | `headlineSmall` | — |
| Large（淘汰） | 152dp | — | `headlineMedium` | — |
| **MediumFlexible** | **112dp** | **136dp** | `headlineMedium` | `labelLarge` |
| **LargeFlexible** | **120dp** | **152dp** | `displaySmall` | `titleMedium` |

注意 flexible 版**折叠高度比旧版还矮**（Large: 120 vs 152），展开后才回到旧高度。
这是"内容优先"的取舍：静止时省空间，滚动时才展开。

通用内部尺寸（`AppBarTokens`）：

| Token | 值 |
| --- | --- |
| `IconSize` | 24dp |
| `AvatarSize` | 32dp |
| `LeadingSpace` / `TrailingSpace` | 4dp |
| `IconButtonSpace` | 0dp |
| `ContainerElevation` | `Level0`（滚动后 `Level2`） |

### 底部

| 变体 | 高度 | 状态 |
| --- | --- | --- |
| `BottomAppBar` | **80dp** | ⚠️ 不再推荐 |
| Docked `HorizontalFloatingToolbar` | **64dp** | ✅ 官方替代 |

Docked toolbar 的左右内边距 16dp、元素间距 4–32dp、**直角**容器。

## 2. 形状

**全部用直角（`CornerNone`）**。官方明确写了原因：圆角会暗示"这个容器可以被展开"，
而 app bar 不能展开。不要给它套 `RoundedCornerShape`。

## 3. 颜色与滚动行为

- 静止时**与背景同色**（无容器感）。
- **滚动后填充对比色**（`surfaceContainer` 一档），把内容和 app bar 分开。
- 折叠/展开跟随 `TopAppBarScrollBehavior`，不要手动动画容器高度。

```kotlin
TopAppBar(
    title = { Text("Title") },
    scrollBehavior = TopAppBarDefaults.pinnedScrollBehavior(),   // 或 enterAlways / exitUntilCollapsed
)
```

四个滚动行为：`pinnedScrollBehavior`、`enterAlwaysScrollBehavior`、
`enterAlwaysCollapsedScrollBehavior`、`exitUntilCollapsedScrollBehavior`。

## 4. 状态

| 状态 | 表现 |
| --- | --- |
| 顶部静止 | 无色调、无阴影、与背景同色 |
| 滚动中 | 填充对比色 + `Level2` elevation |
| 折叠（flexible） | 收缩到 `collapsedHeight`，标题降级为 small 布局 |
| 搜索态 | 见 `recipes/text-fields.md` 的 `AppBarWithSearch` |

## 5. 代码

### 5.1 Small

```kotlin
TopAppBar(
    title = { Text("Inbox") },
    navigationIcon = {
        IconButton(onClick = {}) { Icon(Icons.Filled.Menu, contentDescription = "Menu") }
    },
    actions = {
        IconButton(onClick = {}) { Icon(Icons.Filled.Search, contentDescription = "Search") }
    },
    scrollBehavior = TopAppBarDefaults.pinnedScrollBehavior(),
)
```

### 5.2 Medium / Large Flexible（带副标题）

```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
MediumFlexibleTopAppBar(
    title = { Text("Flight to Osaka") },
    subtitle = { Text("Boarding at 14:20") },
    navigationIcon = { /* ... */ },
    actions = { /* 最多两个 */ },
    scrollBehavior = TopAppBarDefaults.exitUntilCollapsedScrollBehavior(),
)
```

不要传自定义 `collapsedHeight` / `expandedHeight`，默认值就是 token 里的 112/136 与 120/152。
自定义会破坏"滚动变形"的节奏。

### 5.3 需要双行标题

```kotlin
TwoRowsTopAppBar(
    title = { Text("Title") },
    subtitle = { Text("Subtitle") },
    /* ... */
)
```

### 5.4 底栏：用 docked toolbar 而不是 BottomAppBar

```kotlin
// ✅ M3E
HorizontalFloatingToolbar(
    expanded = true,
    modifier = Modifier
        .align(Alignment.BottomCenter)
        .padding(16.dp),
    content = { /* actions */ }
)

// ⚠️ 旧写法，M3E 不推荐
BottomAppBar { /* ... */ }
```

## 6. 选型与设计规则

融合自官方 app-bars guidelines 页。

### 6.1 高度

- **不要做得比默认高度更矮** —— 默认高度是按可读性定的。
- 标题长时用 medium/large flexible，**最多允许两行**。
- **small app bar 里不要换行**（会挤掉动作区）。

### 6.2 动作数量

- **一个动作，最多两个**。
- 主操作应当是改变/离开整页的动作（Send / Save / Edit）。
- **不要放多个 filled 或 tonal 按钮**（会把层级拉平）。

### 6.3 图标

- 用 **filled** 图标；outlined 只在 toggle 场景或确实需要时用。
- leading 按钮用于产品内导航（返回、打开抽屉/侧栏）。

### 6.4 搜索型 app bar

- 搜索容器填满 leading 与 trailing 之间的空间，**直到 312dp**；超过后只继续增长到该空间的 **50%**。
- 大屏上 trailing 图标**最多 4 个**；小屏要更少。
- 官方反例：search app bar 里放三个图标 + 一个头像。

### 6.5 滚动与变形

- 初始与背景同色，**滚动后填充对比色**。
- 滚动时 medium/large flexible **可以变形为 small app bar**，并保持 small 直到滚回顶部。
- **不要**把 app bar 变形成 search app bar。
- 不要改变容器的位置或形状。

### 6.6 其他

- 不要用 logo 直接打开 expanded navigation rail。
- 背景图要高质量且不干扰功能。
- app bar 里的信息应是页面相关，也可以放全局控件（搜索、通知）。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| 标题 | 必须能作为页面标题被读屏识别；`title` 里不要塞按钮 |
| 图标按钮 | 每个都需要 `contentDescription` |
| 触控目标 | 图标按钮 ≥ 48×48dp |
| 对比度 | 滚动后填充色与文字 ≥ 4.5:1（正文级） |
| 缩放 | 200% 字号下标题不超过两行，超出时降级为 small 布局而非截断 |
| 焦点顺序 | leading → title → actions，与视觉顺序一致 |

## 8. 淘汰与替代

| 淘汰项 | 替代 | 依据 |
| --- | --- | --- |
| `MediumTopAppBar` | `MediumFlexibleTopAppBar` | `app-bars/overview`：no longer recommended |
| `LargeTopAppBar` | `LargeFlexibleTopAppBar` | 同上 |
| `BottomAppBar` | docked `HorizontalFloatingToolbar`（64dp，更矮） | `toolbars/overview` |

旧的三种仍然能编译、能用，只是面向 stable M3 的旧界面；新设计不要选。

## 9. 陷阱

1. app bar **不要圆角**，圆角会暗示可展开。
2. flexible 版的折叠高度比旧版**更矮**（Large 120 vs 152），别以为"换了个名字"。
3. 不要传自定义 `collapsedHeight` / `expandedHeight`，默认值已是 token 值。
4. `BottomAppBar` 和 `FlexibleBottomAppBar` 是两个东西，后者没被淘汰。
5. 滚动变色靠 `scrollBehavior`，不要自己监听滚动去改 `containerColor`。
6. 小屏 search app bar 别堆 4 个图标。
