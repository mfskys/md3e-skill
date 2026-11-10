# Carousel — 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`Carousel.kt` / `CarouselDefaults`、`CarouselState`（无独立 token 文件，尺寸由布局参数决定）
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 五种布局 —— 先按内容选

| 布局 | Composable | 适用 | 不适合 |
| --- | --- | --- | --- |
| Multi-browse | `HorizontalMultiBrowseCarousel` | 一次浏览大量视觉项（照片、活动流）、动态设计 | 文字多、图片复杂 |
| Uncontained | `HorizontalUncontainedCarousel` | 高度定制、图文堆叠、传统轮播行为 | 需要自动吸附对齐的场景 |
| Hero | `HorizontalCenteredHeroCarousel`（居中变体） | 突出超大视觉项（电影海报、精选应用） | 项太多 |
| Center-aligned hero | 同上 + 居中对齐 | 居中的大图 | — |
| Full-screen | 垂直滚动容器（非 carousel 组件） | 沉浸式视频/图片流 | 自由滚动 |

## 1. 关键参数

| 参数 | 说明 |
| --- | --- |
| `itemWidth` | 大项的宽度上限，**决定其余项如何排布** |
| `preferredItemWidth` | 居中 hero 用（**beta01 起从 `maxItemWidth` 改名**） |
| `itemSpacing` | 项间距，`CarouselDefaults.ItemSpacing` |
| `contentPadding` | 内容内边距，`CarouselDefaults.ContentPadding` |
| `flingBehavior` | `CarouselDefaults.multiBrowseFlingBehavior()` / `singleAdvanceFlingBehavior()` / `noSnapFlingBehavior()` |

`CarouselState`（`rememberCarouselState()`）暴露 `currentPage` / `pagerState` 一类的滚动状态，
用于和指示器联动。

## 2. 尺寸与形状

Carousel **没有固定 token 尺寸** —— 项的大小由 `itemWidth` + 容器宽度决定：

- multi-browse 会同时显示**至少一个 large + 一个 medium + 一个 small** 项。
- 大项有**最大宽度**（`itemWidth`），调它会连带改变 medium/small 的排布。
- 项的形状由内容决定（通常 `Card` 12dp 或图片自身圆角），组件不强制。

## 3. 颜色

Carousel 不自带配色，颜色来自项内内容（`Card` / `Surface` / 图片）。

## 4. 状态

| 状态 | 表现 |
| --- | --- |
| 静止 | 项按 large/medium/small 排布，**全部完整可见** |
| 滚动中 | 项**自动改变尺寸**并吸附到位，维持同一布局 |
| 吸附后 | 回到 large/medium/small 的稳定排布 |

"滚动时自动变尺寸"是 M3E carousel 的核心行为，不要关掉它去做纯平移。

## 5. 代码

### 5.1 Multi-browse（最常用）

```kotlin
val state = rememberCarouselState()

HorizontalMultiBrowseCarousel(
    state = state,
    itemWidth = 220.dp,                  // 大项宽度上限
    modifier = Modifier.fillMaxWidth(),
    flingBehavior = CarouselDefaults.multiBrowseFlingBehavior(state),
) { index ->
    Card(modifier = Modifier.fillMaxHeight()) {
        // 图片 + 标题
    }
}
```

### 5.2 Uncontained（文字多、图文堆叠）

```kotlin
HorizontalUncontainedCarousel(
    state = rememberCarouselState(),
    itemWidth = 200.dp,
    itemSpacing = 8.dp,
) { index ->
    Column {
        Image(...)
        Text("标题", maxLines = 2)
    }
}
```

uncontained 是唯一**允许项滚到容器边缘外**的布局，项尺寸不随滚动变化。

### 5.3 居中 hero

```kotlin
@OptIn(ExperimentalMaterial3Api::class)
HorizontalCenteredHeroCarousel(
    state = rememberCarouselState(),
    preferredItemWidth = 280.dp,   // beta01 起：原 maxItemWidth
    modifier = Modifier.fillMaxWidth(),
) { index ->
    // 大图项
}
```

### 5.4 带指示器

```kotlin
val state = rememberCarouselState()
HorizontalMultiBrowseCarousel(state = state, ...) { ... }

Row(horizontalArrangement = Arrangement.Center) {
    repeat(pageCount) { i ->
        Box(
            Modifier
                .padding(4.dp)
                .size(8.dp)
                .clip(CircleShape)
                .background(
                    if (state.currentPage == i) MaterialTheme.colorScheme.primary
                    else MaterialTheme.colorScheme.surfaceVariant
                )
        )
    }
}
```

## 6. 选型与设计规则

融合自官方 carousel guidelines 页。

### 6.1 布局选择

| 内容特征 | 选 |
| --- | --- |
| 一堆图片，快速扫 | multi-browse |
| 图 + 多行文字、需要自定义 | uncontained |
| 单个超大海报/精选 | hero（居中） |
| 垂直沉浸流 | full-screen（用垂直容器，不是 carousel） |

**文字多或图片复杂的，不要用 multi-browse** —— 缩小的项看不清。

### 6.2 可见性

- 项必须**完整可见**（uncontained 例外）。
- 滚动时项**自动改尺寸并吸附**，保持同一布局。
- 大项必须有足够宽度，保证内容可读 —— **不要为了塞更多项而缩到看不清**。

### 6.3 断点

- **compact 断点下超过 3 项时**，必须保证每项都容易辨认。
- compact 下项内文字**不超过两行**，除非背景足够简单（纯色）。
- hero 在 compact 下应显示 **1 个大的 + 1 个小的**。

### 6.4 滚动行为

- multi-browse 推荐 **snap scrolling**（`CarouselDefaults.multiBrowseFlingBehavior`）。
- **full-screen 布局必须用 snap**，不要用默认自由滚动。
- 全屏轮播**不要自由滚动**。

### 6.5 头部

- 有 header 时可以用箭头图标按钮替代拖拽暗示（官方允许）。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| 项语义 | 每项要有可读标签（图片 `contentDescription` 或标题文字） |
| 指示器 | 播报"第 N 项，共 M 项" |
| 键盘 | 支持左右方向键在项间移动 |
| 自动播放 | **不要**自动轮播；如需，必须可暂停且不自动切换焦点 |
| 触控 | 项可点区域 ≥ 48dp 高 |
| 文字 | 项内文字与图片背景对比 ≥ 4.5:1（必要时加遮罩） |

## 8. 淘汰与替代

| 项 | 说明 |
| --- | --- |
| `maxItemWidth`（居中 hero） | beta01 改名 **`preferredItemWidth`** |
| 用 `default` 滚动做 full-screen | 必须用 snap |
| 把 carousel 项缩得看不清 | 官方反例：项要够大 |

## 9. 陷阱

1. `maxItemWidth` 已改名为 **`preferredItemWidth`**，旧名编译不过。
2. 三种布局是**三个不同 composable**，不是一个组件的参数。
3. `itemWidth` 改的是"大项上限"，会连带改变 medium/small 的排布 —— 不是单纯的"每项宽度"。
4. 关掉自动变尺寸（用 `noSnapFlingBehavior`）会让布局失去 M3E 特征。
5. `CarouselDefaults.ItemSpacing` / `ContentPadding` 在 beta01 才成为公开成员。
6. 项内文字超两行要自己截断（`maxLines = 2`），组件不会替你处理。
7. 不要用 carousel 承载需要逐项精确操作的表单内容。
