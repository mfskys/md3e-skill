# MD3E Skill

**[English](./README.md)** | **[中文](./README.zh-CN.md)**

一个通用的 AI 技能包，用于在 **Android Jetpack Compose** 中构建 **Material Design 3 Expressive (MD3E)** 界面。可用于原生技能型助手（CodeBuddy、Claude Code 等），也可通过规则入口接入 Cursor、Windsurf、Trae、Cline、GitHub Copilot、通义灵码、文心快码、CodeGeeX 等。

## 什么是 MD3E？

Material 3 Expressive 是 Google 于 2025 年推出的 Material Design 3 演进版本，核心特性包括：

- **弹簧物理动效**（MotionScheme）替代传统的缓动曲线
- **扩展色彩系统**：新增 18 个 Fixed 固定色角色 + 7 个 Surface Container 表面容器角色
- **全新组件**：FloatingToolbar（浮动工具栏）、ButtonGroup（按钮组）、SplitButton（分割按钮）、WideNavigationRail（宽导航栏）、ToggleFloatingActionButton（切换悬浮按钮）、FlexibleBottomAppBar（弹性底部应用栏）等
- **表现力设计原则**：更大胆的色彩、多样化的形状、可变字体排版、容器分组

本技能**同时覆盖 MD3E 和基础 M3**——许多组件目前只有 M3 规范，因此技能在 MD3E 可用时优先使用，不可用时回退到 M3。

**知识基线：2026-10-23。** 完整 M3E 组件集需要 `material3` **1.5.0-beta02**（1.5.0 线已于 2026-10-07 进入 beta）；稳定线 **1.4.0** 仅提供 M3 + MotionScheme + 部分 Expressive。

## 功能特性

- **完整 API 参考**：完整的 `androidx.compose.material3` 包文档（约 8000 行）
- **源码核对的 M3E 签名**：1.5.0 线核心组件（`MaterialExpressiveTheme`、8 档 `Shapes`、
  `MotionScheme`、`FloatingToolbar`、`ButtonGroup`、`SplitButtonLayout`、`LoadingIndicator`…）
  逐文件对照 `androidx/androidx` 核对
- **代码模式库**：主题接线、自适应导航、浮动工具栏、按钮组、分割按钮、搜索、加载、列表、
  动效、无障碍的正确写法，可直接粘贴
- **官方示例地图**：49 个官方 `*Samples.kt` 文件 + `compose-samples` 项目 + Now in Android +
  官方文档，告诉你每个组件该读哪个文件
- **设计 Token**：48 个色彩角色、15 基础 + 15 `*Emphasized` 排版样式、8 档形状、动效系统的精确数值
- **组件目录**：按类别组织的全部 M3/M3E 组件，标注 M3/M3E 归属与用法
- **版本基线**：功能门槛、1.5.0 线变动日志、BOM 覆盖范围（2026-10-23）
- **M3E 精要笔记**：设计体系、色彩/排版/形状、动效物理、组件清单、Compose API
- **M3 vs M3E 差异**：清晰的对比表与迁移指南
- **官方规范镜像**：263 页 Markdown（249 规范页 + 14 概览页；规范页抓取于 2026-09-14，2026-10-08 经官方 sitemap 复核无增删，2026-10-19 补充 M3E 文章与平台开发指南）
- **代码模板**：可直接使用的 `MD3ETheme.kt`、`Color.kt`、`Type.kt`、`Shape.kt`
- **主题生成器**：Python 脚本，从单个种子色生成完整配色方案

## 安装

技能本体只是一个文件夹：`SKILL.md`（入口）+ `references/` + `assets/` + `scripts/`。
按助手支持的机制选一种方式。

**方式一：原生支持技能（Skill）的助手**（保持 `SKILL.md` 在文件夹根目录）：

| 助手 | 项目级 | 用户级 |
| --- | --- | --- |
| CodeBuddy | `.codebuddy/skills/md3e/` | `~/.codebuddy/skills/md3e/` |
| Claude Code | `.claude/skills/md3e/` | `~/.claude/skills/md3e/` |
| 其他兼容 Agent Skills 的助手 | `<skills 目录>/md3e/` | `~/<skills 目录>/md3e/` |

**怎么用**：不需要 slash 命令。`SKILL.md` 的 `description` 就是触发器——直接用自然语言提问
（“做一个浮动工具栏”“M3E 有哪些色彩角色”），助手会自行判断是否加载技能，再按需读取
`references/*.md`。

**方式二：规则 / 自定义指令驱动**：只把 `SKILL.md` 正文放进规则入口，`md3e/` 文件夹留在仓库，
保证 `references/...` 相对路径可用。**不要把整个 `references/` 内联进去**，否则破坏渐进披露。

| 助手 | 规则入口 |
| --- | --- |
| Cursor | `.cursor/rules/md3e.mdc` |
| Windsurf | `.windsurf/rules/md3e.md` |
| Trae | `.trae/rules/md3e.md` |
| Cline | `.clinerules/md3e.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Continue | `.continue/rules/md3e.md` |
| Codex CLI / Gemini CLI / Qwen Code | `AGENTS.md` / `GEMINI.md` / `QWEN.md` |
| 通义灵码 / 文心快码 / CodeGeeX | 该工具的自定义指令入口 |
| 其他 | 仓库根目录的 `AGENTS.md`（通用兜底） |

**怎么用**：规则常驻，同样用自然语言提问即可。

### 让 AI 自己安装

支持终端的助手可以直接完成安装。把下面这段发给它：

> 从 `<md3e 所在路径>/` 安装 MD3E 技能：
> 1. 执行 `python <md3e 所在路径>/scripts/install_skill.py --target <skills 目录>`
> 2. 确认 `<skills 目录>/md3e/SKILL.md` 开头是 `name: md3e`
> 3. 确认 `references/component-index.md` 和 `references/m3e-api-signatures.md` 存在
> 4. 告诉我安装位置和验证方法

已内置常见位置：

```bash
python scripts/install_skill.py --assistant codebuddy --home   # ~/.codebuddy/skills/md3e
python scripts/install_skill.py --assistant claude --home      # ~/.claude/skills/md3e
python scripts/install_skill.py --target ./skills              # ./skills/md3e
python scripts/install_skill.py --target ./skills --dry-run    # 只显示计划
```

脚本只复制技能内容（白名单），拒绝装进源码目录，目标已存在时需 `--force` 才覆盖。

如果助手不能执行命令，让它解压 `md3e.zip`、把 `md3e/` 复制到 skills 目录，再执行上面 4 项检查。

**验证安装**：问“MD3E 的知识基线是什么？”，应回答 `2026-10-23` 并引用
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
│   ├── version-baseline.md           # 版本矩阵、功能门槛、1.5.0 线变动（2026-10-23）
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
│   ├── component-index.md            # 组件 → 源码文件 → 官方示例 → 规范页
│   ├── design-tokens.md              # 色彩/排版/形状/动效/高度 token
│   ├── components-catalog.md         # 全组件目录（按类别，M3/M3E 标注）
│   ├── m3-vs-m3e-diff.md             # 差异对比 + 迁移指南 + IO2026 更新
│   ├── expressive-design-tactics.md  # 7 大表现力设计策略详解
│   ├── design-research.md            # 色彩科学/可读性/动效模式/无障碍研究
│   └── m3-content/                   # m3.material.io 官网镜像（263 页）
│       ├── components/               # 36 个组件 × 概览/规格/指南/无障碍
│       ├── styles/                   # 色彩、动效、形状、排版、间距...
│       ├── foundations/              # 布局、设计 token、手表、XR、无障碍
│       ├── blog/                     # M3E / I-O 2026 文章（2026-10-19）
│       └── develop/                  # Compose / MDC-Android / Flutter / Web 指南
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
