# 官方示例与官方源地图

核对日期：**2026-10-23**

写 UI 时优先抄官方示例，而不是凭记忆拼 API。本文说明**每个能力该去哪个官方源找**，
以及各源的权威等级和已知陷阱。

## 0. 权威等级（冲突时按此顺序）

1. **AndroidX 源码**（`androidx-main`）—— 函数签名、默认值、opt-in 注解的唯一事实源。
2. **官方 samples**（`material3/samples/`、`compose-samples`）—— 可运行的标准写法。
3. **官方 API 参考 / 版本说明** —— 签名汇总与版本门槛，可能滞后于源码。
4. **`m3.material.io` 设计规范**（本仓库 `m3-content/` 镜像）—— 尺寸、状态、anatomy。
   抓取于 2026-09-14；官网组件页的 `lastmod` 集中在 2026-07~09。新 Expressive 组件
   （floating toolbar、short navigation bar、scroll field）**暂无独立规范页**，此时以源码 + 示例为准。
5. 第三方博客/视频 —— 只作灵感，不作为 API 依据。

> 本文讲**源本身**；组件级的「源码 / 示例 / 规范」三处定位见 `component-index.md`。
> `m3-content/` 里的站内链接是官网绝对路径（如 `/components/buttons`），离线不能直接点；
> 按路径映射到本仓库的 `m3-content/components/...` 目录阅读。

> 本仓库的 `compose-api-full.md` 是 **1.4.0 稳定线**快照；1.5.0 线新组件看
> `m3e-api-signatures.md`。两者都没有的，直接读源码。

## 1. AndroidX 仓库：Material 3 samples

路径（相对 androidx 仓库根）：

```
compose/material3/material3/samples/src/main/java/androidx/compose/material3/samples/
```

若本地克隆了 `androidx/androidx`（建议放在本仓库之外的目录），用同样的相对路径。
线上单文件：

```
https://raw.githubusercontent.com/androidx/androidx/androidx-main/compose/material3/material3/samples/src/main/java/androidx/compose/material3/samples/<Name>Samples.kt
```

### 49 个 sample 文件（按能力分组）

| 分组 | 文件 | 什么时候读 |
| --- | --- | --- |
| 对话框/浮层 | `AlertDialogSamples.kt`、`BottomSheetSamples.kt`、`MenuSamples.kt`、`ExposedDropdownMenuSamples.kt`、`TooltipSamples.kt`、`DrawerSamples.kt`、`SearchBarSamples.kt` | 弹层交互、菜单锚点、搜索展开 |
| 应用栏/导航 | `AppBarSamples.kt`、`NavigationBarSamples.kt`、`NavigationRailSamples.kt`、`TabSamples.kt`、`ScaffoldSamples.kt`、`FloatingToolbarSamples.kt` | 顶栏折叠、底部/侧边导航、浮动工具栏 |
| 按钮 | `ButtonSamples.kt`、`ButtonGroupSamples.kt`、`SplitButtonSamples.kt`、`SegmentedButtonSamples.kt`、`ToggleButtonSamples.kt`、`IconButtonSamples.kt`、`FloatingActionButtonSamples.kt`、`FloatingActionButtonMenuSamples.kt` | 强调层级、连通按钮组、FAB morph |
| 选择控件 | `CheckboxSamples.kt`、`RadioButtonSamples.kt`、`SwitchSamples.kt`、`SliderSamples.kt`、`ChipSamples.kt`、`BadgeSamples.kt` | 表单与筛选 |
| 文本输入 | `TextSamples.kt`、`TextFieldSamples.kt`、`ScrollFieldSamples.kt`、`DatePickerSamples.kt`、`TimePickerSamples.kt` | 输入、自动字号、滚轮选择、日期时间 |
| 进度/手势 | `ProgressIndicatorSamples.kt`、`LoadingIndicatorSamples.kt`、`PullToRefreshSamples.kt`、`SwipeToDismissSamples.kt` | 加载、下拉刷新、滑动删除 |
| 主题 | `ThemeSamples.kt`、`ColorSchemeSamples.kt`、`TypographySamples.kt`、`MaterialShapesSamples.kt`、`InteractiveComponentSizeSamples.kt` | 主题接线、色板、字阶、形状 |
| 容器/布局 | `CardSamples.kt`、`SurfaceSamples.kt`、`ListSamples.kt`、`ScrollbarSamples.kt` | 卡片、列表项、滚动条 |
| 形状/动效 | `TransitionSamples.kt`、`RippleSamples.kt`、`CarouselSamples.kt`、`DragHandleSamples.kt` | 转场、涟漪、轮播、拖拽手柄 |

### samples 里最值得直接抄的 5 个写法

1. `ThemeSamples.kt` → `MaterialExpressiveTheme` + 动态取色 + `expressiveLightColorScheme()` 回退。
2. `FloatingToolbarSamples.kt` → 11 种工具栏形态（展开/溢出/滚动收起/带 FAB/放进 Scaffold FAB 槽），
   含焦点顺序与 `focusProperties { canFocus = expanded }`。
3. `ButtonGroupSamples.kt` → 基础组、`customItem` + `animateWidth`、单选/多选连通组、垂直组。
4. `LoadingIndicatorSamples.kt` → `progress` lambda、`ContainedLoadingIndicator`、PullToRefresh 集成。
5. `SearchBarSamples.kt` → `SearchBarState` + slot `SearchBar` + 展开态容器。

## 2. AndroidX 其他相关目录

| 路径 | 内容 |
| --- | --- |
| `compose/material3/adaptive/samples/` | `ListDetailPaneScaffold`、`SupportingPaneScaffold`、ThreePane 导航 |
| `compose/material3/adaptive-navigation-suite/` | `NavigationSuiteScaffold`（自适应导航套件） |
| `compose/material3/integration-tests/` | 演示/基准宿主（demo、macrobenchmark、a2ui） |
| `compose/material3/benchmark/` | 性能基准，判断组件开销时参考 |
| `compose/foundation/foundation/src/commonMain/.../shape/PolygonShape.kt` | `PolygonShape` 真实定义（不在 material3） |
| `compose/material3/material3-lint/` | M3 的 Lint 规则，可用于自查反模式 |
| `compose/material3/material3-a2ui/` | Agent-to-UI 渲染（`material3-a2ui`，实验） |

## 3. `android/compose-samples`（官方示例应用）

| 项目 | 展示重点 | 对 M3 的价值 |
| --- | --- | --- |
| **Jetchat** | 聊天 UI、状态模式、文本输入 | M3 主题 + Material You 动态取色、返回处理、动画 |
| **Reply** | 邮件客户端（Material Study） | 手机/平板/折叠屏**自适应导航**（NavigationBar + Rail + Drawer）、M3 组件 |
| **JetNews** | 新闻阅读器 | 列表/详情、亮暗主题、Window Size Classes、UI 测试 |
| **Jetsnack** | 零食订购 | 自定义设计系统与自定义布局、底栏动画 |
| **Jetcaster** | 播客 | 基于封面图的动态主题、Room、TV/Wear 变体 |
| **JetLagged** | 睡眠追踪 | 自定义 Layout 与 Path 绘图 |
| **Now in Android**（外链仓库） | 完整生产级架构 | 模块化（`core:designsystem` 集中主题）、Dynamic + Default 双主题、自适应布局 |
| **Now in Android Catalog**（`app-nia-catalog`） | 组件目录 | 组件清单式展示，适合抄列表/卡片结构 |
| **Material Catalog**（AOSP） | 组件与主题演示 | 运行时可切主题，验证组件外观 |

已从 `compose-samples` 删除（不要引用）：`Crane`、`Owl`、`Jetsurvey`、`Rally`。

### 依赖版本（raw 快照，2026-10-23 核对）

| 仓库 / 示例 | Compose BOM | `material3` | Kotlin | AGP |
| --- | --- | --- | --- | --- |
| `compose-samples`（Jetchat / Reply / Jetsnack，三者一致） | **2026.09.00**（稳定） | 由 BOM 管理 → **1.4.0** | **2.4.20** | **9.3.1** |
| `nowinandroid`（`main`） | **2025.09.01**（`compose-bom-alpha`） | 由 BOM 管理 | **2.3.0** | **9.3.2** |

由此得三条结论：

1. **官方示例用的是稳定 BOM**，`material3` 落在 1.4.0，因此示例里**看不到 1.5.0 线的
   Expressive 组件**（`FloatingToolbar`、`ButtonGroup`、`ShortNavigationBar`、`LoadingIndicator`
   等）。验证这些组件要读 `androidx-main` 的 `material3/samples`，别拿 `compose-samples` 当依据。
2. **Now in Android 更旧**（alpha BOM 2025.09.01）。官方示例不追最新版，版本一律以
   `version-baseline.md` 为准。
3. 两个仓库的 `material3` 都**不写显式版本**（交给 BOM），不是漏写；`compose-samples` 的
   `gradle/libs.versions.toml` 由全局目录复制到各示例，所以三个示例版本完全一致。

抓取来源：
`raw.githubusercontent.com/android/compose-samples/main/{Jetchat,Reply,Jetsnack}/gradle/libs.versions.toml`、
`raw.githubusercontent.com/android/nowinandroid/main/gradle/libs.versions.toml`。

## 4. 官方文档与设计规范

| 源 | 用途 | 备注 |
| --- | --- | --- |
| `developer.android.com/develop/ui/compose/designsystems/material3` | M3 in Compose 主指南 | 最后更新 **2026-10-19**；含动态取色、类型表、无障碍对比、系统 UI |
| `developer.android.com/jetpack/androidx/releases/compose-material3` | 版本门槛与变更 | 当前 beta02（2026-10-21） |
| `developer.android.com/reference/kotlin/androidx/compose/material3/package-summary` | API 参考 | 与源码可能不同步，签名以源码为准 |
| `m3.material.io`（本仓库 `references/m3-content/`） | 设计规范 | 263 页镜像，`components/{name}/specs.md` |
| `fonts.google.com/icons` | Material Symbols | `material-icons-*` 已不推荐 |

## 5. 阅读与搬运规则

1. **先定位再读**：按组件名找 `{Component}Samples.kt`，只读需要的那个函数，不要整文件搬运。
2. **抄结构，不抄占位符**：sample 里的 `"Localized description"`、`LoremIpsum()`、
   `/* doSomething() */` 是占位，必须替换成真实文案与行为。
3. **抄 opt-in 现状**：sample 文件顶部的 `@file:OptIn(...)` 是它编译所需的注解；
   主线已毕业的 API 可能不需要，以编译器为准。
4. **图标依赖**：sample 常用 `material-icons-extended`；生产建议换 Material Symbols 矢量图，
   `material-icons-core` 自 1.4.0 起不再传递依赖。
5. **`androidx-main` 领先发布版**：主线可能含未发布 API/改名。落地前确认
   `m3e-api-signatures.md` 的版本门槛与 `version-baseline.md` 的通道状态。
6. **不要复制版权头**：sample 代码是 Apache-2.0，抄进项目时按需保留归属，不要整段带
   `Copyright 2024 The Android Open Source Project` 注释。
