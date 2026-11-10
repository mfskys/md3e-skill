# Foundations — 实现规格（断点 / RTL / 交互）

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 来源：`foundations/layout/`（RTL）、`foundations/interaction/`（手势、输入、选择）+ Compose 自适应 API
> 这一层是**跨组件**的：它不属于任何单个组件，但对每个组件都生效。

## 1. 窗口尺寸类与断点

| 尺寸类 | 宽度 | 典型布局 |
| --- | --- | --- |
| compact | **< 600dp** | 单栏；底部导航（`ShortNavigationBar`）；全宽输入框 |
| medium | **600 – 839dp** | 导航轨；列表-详情双栏（canonical） |
| expanded | **840 – 1199dp** | 常驻导航轨（`WideNavigationRail`）；双栏 |
| large | **1200 – 1599dp** | 三栏；支持面板 |
| extra-large | **≥ 1600dp** | 多面板，内容居中限宽 |

Compose 侧判断：

```kotlin
val widthSizeClass = currentWindowAdaptiveInfo().windowSizeClass.windowWidthSizeClass
when (widthSizeClass) {
    WindowWidthSizeClass.COMPACT -> { /* 底部导航 */ }
    WindowWidthSizeClass.MEDIUM -> { /* 导航轨 */ }
    else -> { /* 展开轨 + 双栏 */ }
}
```

`currentWindowAdaptiveInfo()` 来自 `material3-adaptive` 或 `material3-window-size-class`。

**断点相关的硬性提醒**（来自各组件页）：

- compact 下**不要**用底部栏以外的复杂导航；expanded 下**不要**用底部栏。
- medium / expanded 下输入框**不要横跨全宽**，要用弹性边距或容器约束。
- 大屏上不要让卡片/列表拉成一条超长的横条。

## 2. RTL（双向布局）

### 2.1 镜像什么、不镜像什么

| 元素 | RTL 下 |
| --- | --- |
| 布局对齐与顺序 | **镜像**（左右反转，阅读从右上开始） |
| 方向性图标（back / forward / send） | **镜像** |
| 帮助类图标 | 部分语言镜像（乌尔都语、波斯语） |
| 图表 / 曲线 | **不镜像**（波斯语、乌尔都语保持 LTR） |
| 圆形进度 | **不镜像**（仍顺时针） |
| 线性进度 | **镜像**（从右往左）；**希伯来语例外，保持 LTR** |
| 媒体控件 / 时间线（希伯来语） | **保持 LTR** |
| 圆形选择器 / 时钟表盘 | 不镜像 |

### 2.2 文字

- RTL 语言文本**右对齐**，元素**从右往左**流动。
- 同时需要 **alignment（对齐）** 和 **directionality（方向）** 两者都正确。
- 只改对齐不改方向（或反之）会把词序打乱。

### 2.3 四个高频出错点

| 场景 | 正确做法 |
| --- | --- |
| 邮箱 `user@google.com` | **不要反转** username 与 domain 的顺序；domain 始终在右 |
| 电话号码 / URL | 整体按 LTR 渲染，不要跟随段落方向 |
| 光标位置 | 用户名可 RTL 书写，但光标向左移动 |
| 标点 | 跟随段落方向，不要单独反转 |

### 2.4 Compose 实现

```kotlin
// 用 start/end 而不是 left/right
Modifier.padding(start = 16.dp, end = 16.dp)      // ✅
Modifier.padding(left = 16.dp, right = 16.dp)     // ❌ 不会镜像

// 镜像方向性图标
val autoMirrored = Icons.AutoMirrored.Filled.ArrowBack
Icon(autoMirrored, contentDescription = "返回")

// 判断当前方向
val isRtl = LocalLayoutDirection.current == LayoutDirection.Rtl
```

`Icons.AutoMirrored.*` 会在 RTL 下自动翻转；手写的 `painterResource` 需要自己处理。

## 3. 交互模式

### 3.1 手势

| 手势 | 约定 |
| --- | --- |
| 点击 | 触发主操作 |
| 长按 | 进入多选 / 上下文菜单；**不要**用长按做唯一入口 |
| 拖拽 | 重排、拉伸；必须有吸附与取消 |
| 滑动 | **只用于相关内容的切换**（carousel、列表项归档） |
| 边缘滑动 | 系统返回手势区，应用不要抢占 |

**禁止**：用左右滑动在顶部导航的 destination 之间切换（官方明确不支持）。

### 3.2 输入方式

- 触控目标 ≥ **48×48dp**（所有组件的最低下限）。
- 精确指针（鼠标/触控笔）下部分组件会缩小，例如 `ButtonDefaults.MinHeight` 从 40dp 变 **36dp** —— 这是框架行为，不要写死。
- 键盘可见时底部组件会被顶起，用 `WindowInsets` 处理，不要硬编码 padding。

### 3.3 选择模式

| 模式 | 语义角色 | 典型控件 |
| --- | --- | --- |
| 单选（互斥） | `Role.RadioButton` | RadioButton / connected ButtonGroup |
| 多选 | `Role.Checkbox` | Checkbox / FilterChip |
| 开关（即时生效） | `Role.Switch` | Switch |
| 批量选择 | 长按进入 + `Role.Checkbox` | 列表 + 顶部 contextual bar |

批量选择时，选中数量要有一个**显式的计数与退出入口**（通常放 app bar）。

## 4. 状态与动效（跨组件）

- 交互状态统一由 `InteractionSource` + `Surface` 提供，**不要手写 alpha 覆盖**。
- 状态层（state layer）叠加顺序：hover < focus < pressed。
- 减少动效（`LocalMotionDurationScale`）开启时，弹簧与波浪应弱化或关闭。
- 组件形变（按钮按压、chip 选中）属于**形状**维度，不是纯颜色变化 —— 与 `ShapeTokens` 一致。

## 5. 无障碍基线（所有组件共同）

| 项 | 要求 |
| --- | --- |
| 触控目标 | ≥ 48×48dp |
| 对比度 | 正文 ≥ 4.5:1；大字与图形 ≥ 3:1 |
| 语义 | 每个可交互元素都要有 role + label |
| 焦点 | 焦点顺序与视觉顺序一致；弹层打开时焦点移入，关闭后归还 |
| 缩放 | 200% 字号下布局不截断关键信息 |
| 动效 | 尊重"减少动效"设置 |
| 语言 | 不硬编码 LTR 假设（用 start/end、AutoMirrored） |

## 6. 陷阱

1. 用 `left`/`right` 做内边距 → RTL 下不镜像，必须用 `start`/`end`。
2. 把图表、圆形进度镜像了 → 官方明确不镜像。
3. 希伯来语的线性进度本来是 LTR，跟着"RTL 就镜像"会错。
4. 邮箱/URL 跟着段落方向反了 → 认知负担直接上升。
5. 假设所有设备都是 48dp 触控目标 → 精确指针下框架会缩到 36dp。
6. 用左右滑动切顶部导航 → 官方不支持，且会和 carousel/列表手势冲突。
