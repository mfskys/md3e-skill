# MD3E Skill

**[English](./README.md)** | **[中文](./README.zh-CN.md)**

一个通用的 AI 技能包，用于在 **Android Jetpack Compose** 中构建 **Material Design 3 Expressive (MD3E)** 界面。兼容任何支持 skill 格式的 AI 编程助手（CodeBuddy、Cursor、Windsurf 等）。

## 什么是 MD3E？

Material 3 Expressive 是 Google 于 2025 年推出的 Material Design 3 演进版本，核心特性包括：

- **弹簧物理动效**（MotionScheme）替代传统的缓动曲线
- **扩展色彩系统**：新增 18 个 Fixed 固定色角色 + 7 个 Surface Container 表面容器角色
- **全新组件**：FloatingToolbar（浮动工具栏）、ButtonGroup（按钮组）、SplitButton（分割按钮）、WideNavigationRail（宽导航栏）、ToggleFloatingActionButton（切换悬浮按钮）、FlexibleBottomAppBar（弹性底部应用栏）等
- **表现力设计原则**：更大胆的色彩、多样化的形状、可变字体排版、容器分组

本技能**同时覆盖 MD3E 和基础 M3**——许多组件目前只有 M3 规范，因此技能在 MD3E 可用时优先使用，不可用时回退到 M3。

**知识基线：2026-10-08。** 完整 M3E 组件集需要 `material3` **1.5.0-beta01**（1.5.0 线已于 2026-10-07 进入 beta）；稳定线 **1.4.0** 仅提供 M3 + MotionScheme + 部分 Expressive。

## 功能特性

- **完整 API 参考**：完整的 `androidx.compose.material3` 包文档（约 8000 行）
- **设计 Token**：全部色彩角色、排版样式、形状规格、动效系统的精确数值
- **组件目录**：按类别组织的全部 M3/M3E 组件，标注 M3/M3E 归属与用法
- **版本基线**：功能门槛、1.5.0 线变动日志、BOM 覆盖范围（2026-10-08）
- **M3E 精要笔记**：设计体系、色彩/排版/形状、动效物理、组件清单、Compose API
- **M3 vs M3E 差异**：清晰的对比表与迁移指南
- **官方规范镜像**：256 页 Markdown（249 规范页 + 7 导航页；抓取于 2026-09-14，2026-10-08 经官方 sitemap 复核，无页面增删）
- **代码模板**：可直接使用的 `MD3ETheme.kt`、`Color.kt`、`Type.kt`、`Shape.kt`
- **主题生成器**：Python 脚本，从单个种子色生成完整配色方案

## 安装

将 `md3e/` 目录复制到你的 AI 助手的技能文件夹中。例如：

- **CodeBuddy**：`.codebuddy/skills/md3e/`（项目级）或 `~/.codebuddy/skills/md3e/`（用户级）
- **其他 AI 助手**：放入对应的 skills/plugins 目录

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
│   ├── version-baseline.md           # 版本矩阵、功能门槛、1.5.0 线变动（2026-10-08）
│   ├── m3e/                          # M3E 精要笔记（中文 5 + 英文 *.en.md 镜像，核对 2026-10-08）
│   │   ├── design-system.md          # 主题体系、动态取色、系统 UI（另有 .en.md）
│   │   ├── color-typography-shape.md # 颜色 / 排版 / 形状（另有 .en.md）
│   │   ├── motion-physics.md         # MotionScheme 弹簧动效（另有 .en.md）
│   │   ├── components.md             # 按版本线标注的组件清单（另有 .en.md）
│   │   └── compose-api.md            # API 门槛、迁移、1.5.0 线变动（另有 .en.md）
│   ├── compose-api-full.md           # 完整官方 API 参考（约 8000 行）
│   ├── design-tokens.md              # 色彩/排版/形状/动效/高度 token
│   ├── components-catalog.md         # 全组件目录（按类别，M3/M3E 标注）
│   ├── m3-vs-m3e-diff.md             # 差异对比 + 迁移指南 + IO2026 更新
│   ├── expressive-design-tactics.md  # 7 大表现力设计策略详解
│   ├── design-research.md            # 色彩科学/可读性/动效模式/无障碍研究
│   └── m3-content/                   # m3.material.io 官网镜像（256 页，2026-09-14）
│       ├── components/               # 36 个组件 × 概览/规格/指南/无障碍
│       ├── styles/                   # 色彩、动效、形状、排版、间距...
│       └── foundations/              # 布局、设计 token、手表、XR、无障碍
├── assets/
│   └── templates/
│       ├── MD3ETheme.kt              # MaterialExpressiveTheme 配置模板
│       ├── Color.kt                  # 完整 48 角色配色方案模板
│       ├── Type.kt                   # 15 种排版样式模板
│       └── Shape.kt                  # 5 级形状规格模板
└── scripts/
    └── generate_theme.py             # 种子色 → 完整 Compose 主题
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
