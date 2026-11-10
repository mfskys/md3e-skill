# MD3E Skill

**[English](./README.md)** | **[中文](./README.zh-CN.md)**

一个 **Agent Skill**，用于在 **Android Jetpack Compose** 中构建 **Material Design 3 Expressive (MD3E)** 界面。

它遵循 [Agent Skills 规范](https://agentskills.io/specification)：一个精简的 `SKILL.md` 入口 +
按需加载的 `references/` 目录。原生支持已经相当广泛——官方客户端清单收录了 **46 个**，包括
Claude Code、Cursor、VS Code / GitHub Copilot、TRAE、Gemini CLI、Codex、JetBrains Junie、
Roo Code、Amp、OpenHands、Factory、Spring AI 和 CodeBuddy。在这些客户端里，助手会先用
`description` 匹配你的问题，加载 `SKILL.md`，再只打开这次问题真正需要的参考文件。

少数编辑器目前没有技能机制（Windsurf、Cline、通义灵码、文心快码）。它们可以通过规则文件接入，
但代价是实打实的：规则每轮都会被整体注入，且无法自行读取 `references/`，模型可能只按
`SKILL.md` 的摘要作答。

## 什么是 MD3E？

Material 3 Expressive 是 Google 于 2025 年推出的 Material Design 3 演进版本，核心特性包括：

- **弹簧物理动效**（MotionScheme）替代传统的缓动曲线
- **扩展色彩系统**：新增 18 个 Fixed 固定色角色 + 7 个 Surface Container 表面容器角色
- **全新组件**：FloatingToolbar（浮动工具栏）、ButtonGroup（按钮组）、`SplitButtonLayout`（分割按钮，注意没有 `SplitButton`）、WideNavigationRail（宽导航栏）、ShortNavigationBar（短底栏）、ToggleFloatingActionButton（切换悬浮按钮）、LoadingIndicator（加载指示器）等
- **表现力设计原则**：更大胆的色彩、多样化的形状、可变字体排版、容器分组

本技能**同时覆盖 MD3E 和基础 M3**——许多组件目前只有 M3 规范，因此技能在 MD3E 可用时优先使用，不可用时回退到 M3。

**知识基线：2026-11-10。** 完整 M3E 组件集需要 `material3` **1.5.0-rc01**（1.5.0 线已于 2026-10-07 进入 beta，2026-11-04 转为 RC）；稳定线 **1.4.0** 仅提供 M3 + MotionScheme + 部分 Expressive。

## 功能特性

- **实现规格（`references/recipes/`）**：按组件家族组织的代码化规格——变体全集（含已淘汰项）、
  从 `*Tokens.kt` 取的精确数值、颜色/形状/状态矩阵与可运行片段。官方页面的测量数据都在插图里，
  这一层补的正是"真正要填进代码的数字"
- **完整 API 参考**：完整的 `androidx.compose.material3` 包文档（约 8000 行）
- **源码核对的 M3E 签名**：1.5.0 线核心组件（`MaterialExpressiveTheme`、8 档 `Shapes`、
  `MotionScheme`、`FloatingToolbar`、`ButtonGroup`、`SplitButtonLayout`、`LoadingIndicator`…）
  逐文件对照 `androidx/androidx` 核对
- **代码模式库**：主题接线、自适应导航、浮动工具栏、按钮组、分割按钮、搜索、加载、列表、
  动效、无障碍的正确写法，可直接粘贴
- **官方示例地图**：49 个官方 `*Samples.kt` 文件 + `compose-samples` 项目 + Now in Android +
  官方文档，告诉你每个组件该读哪个文件
- **设计 Token**：48 个色彩角色、15 基础 + 15 `*Emphasized` 排版样式、8 档形状、动效系统的精确数值
- **组件目录**：按类别组织的全部 M3/M3E 组件，标注 M3/M3E 归属、用法与淘汰状态
- **淘汰清单**：M3E 明确不再推荐的基线组件——segmented button、navigation drawer、bottom app bar、
  基线 navigation bar/rail、40dp small FAB、medium/large top app bar——以及每一项的替代方案。
  避免生成的界面停留在纯 M3 观感
- **版本基线**：功能门槛、1.5.0 线变动日志、BOM 覆盖范围（2026-11-10）
- **M3E 精要笔记**：设计体系、色彩/排版/形状、动效物理、组件清单、Compose API
- **M3 vs M3E 差异**：清晰的对比表与迁移指南
- **官方规范已融合**：m3.material.io 的组件页面已提炼进 `references/recipes/`（变体、数值、代码、Do/Don't、无障碍），原始 263 页镜像已移除，只保留一处权威来源
- **代码模板**：可直接使用的 `MD3ETheme.kt`、`Color.kt`、`Type.kt`、`Shape.kt`
- **主题生成器**：Python 脚本，从单个种子色生成完整配色方案

## 安装

技能本体只是一个文件夹：`SKILL.md`（入口）+ `references/` + `assets/` + `scripts/`。
按助手支持的机制选一种方式。

**方式一：原生支持技能（Skill）的客户端（推荐）**。把 `md3e/` 复制进客户端的 skills 目录，
`SKILL.md` 保持在文件夹根目录；**目录名必须与 `name` 字段一致（`md3e`）**：

| 客户端 | 项目级 | 用户级 |
| --- | --- | --- |
| Claude Code | `.claude/skills/md3e/` | `~/.claude/skills/md3e/` |
| Cursor | `.cursor/skills/md3e/` | `~/.cursor/skills/md3e/` |
| VS Code / GitHub Copilot | `.github/skills/md3e/` | `~/.copilot/skills/md3e/` |
| CodeBuddy | `.codebuddy/skills/md3e/` | `~/.codebuddy/skills/md3e/` |
| 其他原生客户端 | 见[客户端清单](https://agentskills.io/clients)（共 46 个） | |

**怎么用**：不需要 slash 命令。`SKILL.md` 的 `description` 就是触发器——直接用自然语言提问
（“做一个浮动工具栏”“M3E 有哪些色彩角色”），助手会自行判断是否加载技能，再按需读取
`references/*.md`。

**方式二：规则文件（无技能机制时的兜底）**：只把 `SKILL.md` **正文**放进规则入口，`md3e/`
文件夹留在仓库，保证 `references/...` 相对路径可用。**不要把整个 `references/` 内联进去**——
规则文件每轮都会被注入，内联等于把 3000 行的技能变成永久上下文开销。

| 客户端 | 规则入口 |
| --- | --- |
| Windsurf | `.windsurf/rules/md3e.md` |
| Cline | `.clinerules/md3e.md` |
| 通义灵码 / 文心快码 | 该工具的自定义指令入口 |
| 其他 | 仓库根目录的 `AGENTS.md`（通用兜底） |

**代价**：这种方式下模型始终持有 `SKILL.md`，但**需要被提醒**才会去打开 `references/` 里的文件，
可能只按摘要作答。原生技能加载会自动完成这一步——客户端支持时优先用它。

### 让 AI 自己安装

支持终端的助手可以直接完成安装。把下面这段发给它：

> 从 `<md3e 所在路径>/` 安装 MD3E 技能：
> 1. 执行 `python <md3e 所在路径>/scripts/install_skill.py --target <skills 目录>`
> 2. 确认 `<skills 目录>/md3e/SKILL.md` 开头是 `name: md3e`
> 3. 确认 `references/component-index.md` 和 `references/m3e-api-signatures.md` 存在
> 4. 告诉我安装位置和验证方法

已内置常见位置：

```bash
python scripts/install_skill.py --assistant claude --home      # ~/.claude/skills/md3e
python scripts/install_skill.py --assistant cursor --home      # ~/.cursor/skills/md3e
python scripts/install_skill.py --assistant copilot            # .github/skills/md3e
python scripts/install_skill.py --assistant codebuddy --home   # ~/.codebuddy/skills/md3e
python scripts/install_skill.py --target ./skills              # ./skills/md3e
python scripts/install_skill.py --target ./skills --dry-run    # 只显示计划
```

脚本只复制技能内容（白名单），拒绝装进源码目录，目标已存在时需 `--force` 才覆盖。

如果助手不能执行命令，让它解压 `md3e.zip`、把 `md3e/` 复制到 skills 目录，再执行上面 4 项检查。

**验证安装**：问“MD3E 的知识基线是什么？”，应回答 `2026-11-10` 并引用
`references/version-baseline.md`；答错说明技能没有加载。

```
md3e/
├── SKILL.md
├── references/
├── assets/
└── scripts/
```

### 使用主题生成器

```bash
python scripts/generate_theme.py --seed #6750A4 --package com.example.app --output ./theme/
```

安装 `material-color-utilities` 可获得精确的 HCT 色彩生成：

```bash
pip install material-color-utilities
```

## 技能结构

```
md3e/
├── SKILL.md                          # 入口：触发条件、工作流、API 速查
├── references/
│   ├── version-baseline.md           # 版本矩阵、功能门槛、1.5.0 线变动（2026-11-10）
│   ├── recipes/                      # 实现规格 —— 唯一权威来源
│   │   ├── INDEX.md                  # 状态图例（✅/⚠️/🧪/🚫）、数据优先级、覆盖进度
│   │   ├── buttons.md                # 5 样式 × 5 尺寸 × 2 形状 + 4 种 toggle + 分割按钮
│   │   ├── button-groups.md          # standard（溢出菜单）/ connected（取代 segmented）
│   │   ├── icon-buttons.md           # 4 样式 × 默认/toggle × 5 尺寸
│   │   ├── fabs.md                   # 56/80/96 三档 + 扩展三档 + 菜单/切换形态
│   │   ├── app-bars.md               # Small / MediumFlexible / LargeFlexible / 停靠工具栏
│   │   ├── navigation.md             # 短底栏 / 宽导航轨 / 抽屉替代关系
│   │   ├── tabs.md                   # Primary / Secondary / 可滚动
│   │   ├── text-fields.md            # Filled / Outlined / 安全输入 / 搜索，两套 API
│   │   ├── selection.md              # Checkbox / Radio / Switch / Slider / Chips + 选型表
│   │   ├── feedback.md               # 进度 / 加载 / Snackbar / Tooltip / Badge / 分隔线
│   │   ├── containers.md             # 卡片 / 对话框 / 底部面板 / 菜单 / 列表项
│   │   ├── pickers.md                # 日期 / 日期范围 / 日期输入 / 时间
│   │   ├── carousel.md               # multi-browse / uncontained / hero
│   │   └── foundations.md            # 断点 / RTL / 交互模式 / 无障碍基线
│   ├── m3e/                          # M3E 精要笔记（中文 5 + 英文 *.en.md 镜像，核对 2026-10-23）
│   │   ├── design-system.md          # 主题体系、动态取色、系统 UI（另有 .en.md）
│   │   ├── color-typography-shape.md # 颜色 / 排版 / 形状（另有 .en.md）
│   │   ├── motion-physics.md         # MotionScheme 弹簧动效（另有 .en.md）
│   │   ├── components.md             # 按版本线标注的组件清单（另有 .en.md）
│   │   └── compose-api.md            # API 门槛、迁移、1.5.0 线变动（另有 .en.md）
│   ├── compose-api-full.md           # 完整官方 API 参考（约 8000 行，稳定线）
│   ├── m3e-api-signatures.md         # 源码核对的 1.5.0 线签名速查
│   ├── compose-patterns.md           # 可直接复制的代码模式（主题/导航/工具栏/搜索…）
│   ├── official-samples.md           # 官方示例地图（49 个 samples + 示例 App + 文档）
│   ├── component-index.md            # 组件 → 源码文件 → 官方示例 → recipes 章节
│   ├── design-tokens.md              # 色彩/排版/形状/动效/高度 token
│   ├── components-catalog.md         # 全组件目录（按类别，M3/M3E 标注）
│   ├── m3-vs-m3e-diff.md             # 差异对比 + 迁移指南 + IO2026 更新
│   ├── expressive-design-tactics.md  # 7 大表现力设计策略详解
│   └── design-research.md            # 色彩科学/可读性/动效模式/无障碍研究
├── assets/
│   └── templates/
│       ├── MD3ETheme.kt              # MaterialExpressiveTheme 配置模板
│       ├── Color.kt                  # 完整 48 角色配色方案模板
│       ├── Type.kt                   # 15 基础排版样式（另 15 个 Emphasized 槽位有注释说明）
│       └── Shape.kt                  # 8 档形状规格模板
└── scripts/
    ├── generate_theme.py             # 种子色 → 完整 Compose 主题
    ├── install_skill.py              # 安装到 skills 目录（可让 AI 直接执行）
    └── package_skill.py              # 生成 dist/md3e.zip 发布包（仅仓库，不随包发布）
```

## 核心 API

| 类别 | M3 | MD3E |
|------|----|------|
| 主题 | `MaterialTheme` | `MaterialExpressiveTheme` |
| 配色 | `lightColorScheme()` / `darkColorScheme()` | + `expressiveLightColorScheme()` |
| 动效 | 缓动曲线 + 持续时间 token | `MotionScheme.standard()` / `.expressive()` |
| 实验性注解 | `@ExperimentalMaterial3Api` | + `@ExperimentalMaterial3ExpressiveApi` |

## 使用示例

安装技能后，直接用自然语言向 AI 助手提问即可，技能会自动在相关请求时触发：

**主题配置：**
> "为我的 Compose 应用设置 Material 3 Expressive 主题，支持动态配色"

**组件创建：**
> "创建一个 MD3E 浮动工具栏，包含 3 个操作按钮"
> "用 MD3E 做一个带溢出菜单的按钮组"
> "按照 Material 3 规范做一个卡片列表"

**设计指导：**
> "MD3E 有哪些色彩角色？分别在什么场景使用？"
> "M3 和 M3E 的动效系统有什么区别？"
> "FAB 应该用哪个形状？"

**迁移：**
> "把我的应用从 MaterialTheme 迁移到 MaterialExpressiveTheme"
> "更新我的配色方案，加入 M3E 新增的 Fixed 固定色角色"

**主题生成：**
> "用种子色 #6750A4 生成一套 Compose 配色方案"

## 资料来源

- [m3.material.io](https://m3.material.io/) — Material Design 3 Expressive 官方设计指南
- [androidx.compose.material3](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary) — Compose Material 3 官方 API 参考
- [Compose Material 3 开发指南](https://developer.android.com/develop/ui/compose/designsystems/material3) — 官方开发者文档

## 免责声明

本技能仅供参考和学习使用。Material 3 Expressive 组件的实际行为可能因 Compose Material 3 库版本而异。在生产环境使用前，请务必在自己的环境中进行测试。

## 开源许可

[Apache License 2.0](./LICENSE) — 与 Material Design 组件和 AndroidX 库使用相同的许可证。
