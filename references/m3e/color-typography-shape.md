# M3E 颜色 / 排版 / 形状

核对日期：**2026-10-08**
来源：Compose 中的 Material Design 3（官方，页面更新 2026-09-08）✅ +
Compose Material 3 版本说明（页面更新 2026-09-09）✅

---

# 一、颜色系统

## 1.1 结构

- 基础是 **5 种关键颜色**（primary / secondary / tertiary / error / neutral 系），
  每种对应一个**含 13 种色调（tone）的调色板** ✅
- 角色语义：

| 角色 | 用途 |
| --- | --- |
| `primary` | 主要组件（主按钮、选中态、强调） |
| `secondary` | 次要组件（过滤标签等不显眼处） |
| `tertiary` | 对比强调色 |
| `error` | 错误态 |
| `surface` / `surfaceVariant` / `surfaceContainer*` | 容器与背景 |
| `onXxx` | 叠在 `Xxx` **之上**的前景色（文本/图标） |
| `XxxContainer` / `onXxxContainer` | 容器样式组件（FilledCard、Chip 等） |

- 访问：`MaterialTheme.colorScheme.primary`。

## 1.2 动态取色

见 `design-system.md` 第四节（API 31+、`dynamicLightColorScheme` / `dynamicDarkColorScheme`、
必须回退、成对使用）。

## 1.3 生成配色方案

官方工具 **Material Theme Builder** 可从品牌源色生成并导出 Compose 代码，产物为两个文件 ✅：

- `Color.kt`：浅色/深色主题的全部颜色与角色定义；
- `Theme.kt`：`lightColorScheme` / `darkColorScheme` 与主题设置。

## 1.4 版本相关的颜色行为变更（踩坑清单）

| 版本 | 变更 | 影响 |
| --- | --- | --- |
| 1.2.0-alpha08 | `ColorScheme` 变为**不可变** | 不能再在运行时改字段，必须重建 |
| 1.3.0 | 组件默认使用 **`SurfaceContainer` 变体，不再受色调海拔影响** | 旧版靠 `tonalElevation` 拉开的层级差会消失，需改用正确的 `surfaceContainer` 角色 |
| 1.3.0 | 焦点态叠加层改为 **0.1f**；`lightColorScheme`/`darkColorScheme` 的 Surface 与背景色微调 | 视觉回归时先怀疑这里 |
| 1.4.0 | `NavigationBarItem` / `NavigationRailItem` 选中标签色从 **`onSurface` → `secondary`** | 需恢复时手动设 `selectedTextColor = MaterialTheme.colorScheme.onSurface` |
| 1.5.0-alpha18 | 新增 `expressiveLightColorScheme` | alpha，谨慎采用 |

---

# 二、排版系统

## 2.1 字阶

**5 类 × 3 号 = 15 个样式** ✅：Display / Headline / Title / Body / Label，各含 Large / Medium / Small。

默认值示例（官方文档列出）✅：

| 样式 | 字体 | 字号 / 行高 |
| --- | --- | --- |
| `displayLarge` | Roboto | 57 / 64 |
| `bodyLarge` | Roboto | 16 / 24 |
| `labelSmall` | Roboto Medium | 11 / 16 |

访问：`MaterialTheme.typography.titleLarge`。

## 2.2 关键差异与变更

| 项 | 说明 |
| --- | --- |
| **M3 `Typography` 没有 `defaultFontFamily`** | 与 M2 不同，必须**逐个 `TextStyle`** 设置 `fontFamily` ✅ |
| 1.2.0-alpha03 起 | `includeFontPadding` 默认 **`false`**；行高样式改为 `Trim.None` + `Alignment.Center` ✅ |
| 动态尺寸类别 | 同一字阶在不同设备上下文**可分配不同值**（如手机 vs 平板），是 M3 跨设备缩放的基础 ✅ |
| 可变字体轴 | M3E 的排版更简单，靠**可变字体轴**增强表现力 ⚠️（来自 Wear 文档的 M3E 描述，移动侧规范细节待查） |
| font variation settings | Compose 1.12 起可下载字体支持 **font variation settings** ✅ |
| 大字号适配 | 无障碍要求下必须验证系统字号放大后的布局（截断、溢出） |

---

# 三、形状系统

## 3.1 五档圆角

| 档位 | 示例值（官方文档） |
| --- | --- |
| `extraSmall` | 4dp |
| `small` | 8dp |
| `medium` | 12dp |
| `large` | 16dp |
| `extraLarge` | 24dp |

均为 `RoundedCornerShape`；另有 `RectangleShape`、`CircleShape`。
访问：`MaterialTheme.shapes.medium`，或按组件单独指定。

## 3.2 M3E 的形状表现力

- M3E 把**形状**提升为重要的表现手段（形状对形状的过渡/形变）。
- 规范侧的"35 种形状集"等细节 ⚠️ 需在 `m3.material.io` 的 Shape 章节确认。
- Compose 侧相关能力：
  - `MaterialShapes`（形状集合）与 `MaterialShapes.toShape()` 等 API 属较新版本能力，
    **使用前先确认当前 `material3` 版本是否包含** ⚠️；
  - 1.4.0-alpha01 起 `AnimatedPane` 支持形状（伴随窗格转场做形变）✅。

## 3.3 实践约定

- **只用主题里的五档**，不在业务代码里写 `RoundedCornerShape(7.dp)` 之类的魔法值。
- 组件级自定义通过 `XxxDefaults.shape` / 组件参数覆盖，不修改全局 `MaterialTheme.shapes`。
- 需要形变动画时，用 `animate*AsState` 配合 `Shape` 类型的插值，不要在每次重组时新建 `Shape` 对象。

---

# 四、三者的组合原则

| 原则 | 说明 |
| --- | --- |
| 颜色表达**语义** | 用角色名（primary / error）而不是具体色值，保证动态取色与深色模式自动生效 |
| 排版表达**层级** | 用字阶建立信息层级，不靠增大字号硬调 |
| 形状表达**分组与亲和度** | 容器越大用越大圆角；同一层级的卡片圆角必须一致 |
| 动效表达**因果** | 元素从哪里来回到哪里去（见 `motion-physics.md`） |
| 三者都要**可被主题覆盖** | 业务组件禁止硬编码色值/字号/圆角 |
