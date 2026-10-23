# MD3E Skill

**[English](./README.md)** | **[中文](./README.zh-CN.md)**

A universal AI skill for building Android UI with **Material Design 3 Expressive (MD3E)** using **Jetpack Compose**. Works with native-skill assistants (CodeBuddy, Claude Code, any Agent-Skills-compatible tool) and with rules-based assistants (Cursor, Windsurf, Trae, Cline, GitHub Copilot, 通义灵码, 文心快码, CodeGeeX) through their rules entry.

## What is MD3E?

Material 3 Expressive is Google's 2025 evolution of Material Design 3, featuring:
- **Spring-based motion** (MotionScheme) replacing easing curves
- **Expanded color system** with 18 new Fixed color roles + 7 surface container roles
- **New components**: FloatingToolbar, ButtonGroup, SplitButton, WideNavigationRail, ToggleFloatingActionButton, FlexibleBottomAppBar, and more
- **Expressive design principles**: bolder colors, varied shapes, variable typography, container grouping

This skill covers **both MD3E and baseline M3** — many components only have M3 specs, so the skill uses MD3E where available and falls back to M3 otherwise.

**Knowledge baseline: 2026-10-23.** Full M3E component set requires `material3` **1.5.0-beta02**
(the 1.5.0 line entered beta on 2026-10-07); stable **1.4.0** ships M3 + MotionScheme + partial
Expressive only.

## Features

- **Complete API reference**: Full `androidx.compose.material3` package documentation (~8,000 lines)
- **Source-verified M3E signatures**: 1.5.0-line APIs (`MaterialExpressiveTheme`, 8-size `Shapes`,
  `MotionScheme`, `FloatingToolbar`, `ButtonGroup`, `SplitButtonLayout`, `LoadingIndicator`, …)
  checked file-by-file against `androidx/androidx`
- **Code patterns**: Ready-to-paste wiring for theming, adaptive navigation, floating toolbars,
  button groups, split buttons, search, loading, lists, motion and accessibility
- **Official samples map**: The 49 official `*Samples.kt` files, `compose-samples` apps,
  Now in Android and the official docs — tells you exactly which file to read per component
- **Design tokens**: All 48 color roles, 15 base + 15 `*Emphasized` type styles, 8 shape sizes,
  motion system values
- **Component catalog**: Every M3/M3E component organized by category with usage guidance
- **Version baseline**: Feature gates, 1.5.0-line churn, BOM coverage (2026-10-23)
- **Curated M3E notes**: Design system, color/type/shape, motion physics, components, Compose API
- **M3 vs M3E diff**: Clear comparison and migration guide
- **Official spec mirror**: 263 Markdown pages from m3.material.io — 249 spec + 14 overview (specs captured 2026-09-14, sitemap-verified 2026-10-08; M3E articles and platform guides added 2026-10-19)
- **Code templates**: Ready-to-use `MD3ETheme.kt`, `Color.kt`, `Type.kt`, `Shape.kt`
- **Theme generator**: Python script to generate a complete color scheme from a single seed color

### Installation

The skill is a plain folder — `SKILL.md` + `references/` + `assets/` + `scripts/`. Pick the mode
your assistant supports.

**Mode 1 — native skill support.** Copy `md3e/` into the skills directory, keeping `SKILL.md` at the
folder root:

| Assistant | Project-level | User-level |
| --- | --- | --- |
| CodeBuddy | `.codebuddy/skills/md3e/` | `~/.codebuddy/skills/md3e/` |
| Claude Code | `.claude/skills/md3e/` | `~/.claude/skills/md3e/` |
| Any Agent-Skills-compatible assistant | `<skills-dir>/md3e/` | `~/<skills-dir>/md3e/` |

**How it is used:** no slash command. The `description` in `SKILL.md` is the trigger — ask a normal
question ("build a floating toolbar", "what are the M3E color roles") and the assistant decides to
load the skill, then reads `references/*.md` on demand.

**Mode 2 — rules / custom instructions.** Put **only the body of `SKILL.md`** into the rules entry
and keep the `md3e/` folder in the repo, so the relative `references/...` paths still resolve. Never
inline the whole `references/` tree — that defeats progressive disclosure.

| Assistant | Rules entry |
| --- | --- |
| Cursor | `.cursor/rules/md3e.mdc` |
| Windsurf | `.windsurf/rules/md3e.md` |
| Trae | `.trae/rules/md3e.md` |
| Cline | `.clinerules/md3e.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Continue | `.continue/rules/md3e.md` |
| Codex CLI / Gemini CLI / Qwen Code | `AGENTS.md` / `GEMINI.md` / `QWEN.md` |
| 通义灵码 / 文心快码 / CodeGeeX | the tool's custom-instruction entry |
| Anything else | `AGENTS.md` at the repo root (widely recognised) |

**How it is used:** rules are always-on; the same natural-language questions work.

### Let the assistant install it

Most assistants with terminal access can install the skill themselves. Paste this prompt:

> Install the MD3E skill from `<path-to-md3e>/`:
> 1. run `python <path-to-md3e>/scripts/install_skill.py --target <skills-dir>`
> 2. verify `<skills-dir>/md3e/SKILL.md` starts with `name: md3e`
> 3. verify `references/component-index.md` and `references/m3e-api-signatures.md` exist
> 4. tell me the install path and how to verify it

Known locations are built in:

```bash
python scripts/install_skill.py --assistant codebuddy --home   # ~/.codebuddy/skills/md3e
python scripts/install_skill.py --assistant claude --home      # ~/.claude/skills/md3e
python scripts/install_skill.py --target ./skills              # ./skills/md3e
python scripts/install_skill.py --target ./skills --dry-run    # show the plan only
```

The script installs skill content only (allow-list), refuses to install inside the source folder,
and refuses to overwrite an existing install without `--force`.

If the assistant cannot run commands, ask it to extract `md3e.zip`, copy the `md3e/` folder into the
skills directory, and then run the same four checks.

**Verify the install**: ask "What is the MD3E knowledge baseline?" — the expected answer is
`2026-10-23`, citing `references/version-baseline.md`. Any other answer means the skill is not loaded.

```
md3e/
├── SKILL.md
├── references/
├── assets/
└── scripts/
```

### Using the Theme Generator

```bash
python scripts/generate_theme.py --seed #6750A4 --package com.example.app --output ./theme/
```

Install `material-color-utilities` for accurate HCT color generation — both the 0.2.x and the legacy
0.1.x APIs are auto-detected. Without it the script falls back to a built-in HSL approximation:

```bash
pip install material-color-utilities
```

## Skill Structure

```
md3e/
├── SKILL.md                          # Entry point: triggers, workflow, quick reference
├── references/
│   ├── version-baseline.md           # Version matrix, feature gates, 1.5.0 churn (2026-10-23)
│   ├── m3e/                          # Curated M3E notes (5 zh + 5 en mirrors, verified 2026-10-23)
│   │   ├── design-system.md          # Theming, dynamic color, system UI (+ design-system.en.md)
│   │   ├── color-typography-shape.md # Color / type / shape (+ color-typography-shape.en.md)
│   │   ├── motion-physics.md         # MotionScheme spring physics (+ motion-physics.en.md)
│   │   ├── components.md             # Component inventory by version line (+ components.en.md)
│   │   └── compose-api.md            # API gates, migration, 1.5.0 churn (+ compose-api.en.md)
│   ├── compose-api-full.md           # Complete official API reference (~8,000 lines, stable line)
│   ├── m3e-api-signatures.md         # Source-verified 1.5.0-line signatures
│   ├── compose-patterns.md           # Verified code patterns (theme/nav/toolbar/search/...)
│   ├── official-samples.md           # Where the official samples live + what each shows
│   ├── component-index.md            # Component -> source file -> sample -> spec page
│   ├── design-tokens.md              # Color/typography/shape/motion/elevation tokens
│   ├── components-catalog.md         # All components by category with M3/M3E tags
│   ├── m3-vs-m3e-diff.md             # Differences + migration guide + IO2026 updates
│   ├── expressive-design-tactics.md  # 7 expressive design tactics with guidance
│   ├── design-research.md            # Color science, readability, motion patterns, a11y
│   └── m3-content/                   # Mirror of m3.material.io (263 pages)
│       ├── components/               # 36 components × overview/specs/guidelines/a11y
│       ├── styles/                   # color, motion, shape, typography, spacing...
│       ├── foundations/              # layout, design tokens, watches, XR, a11y
│       ├── blog/                     # M3E / I-O 2026 articles (2026-10-19)
│       └── develop/                  # Compose / MDC-Android / Flutter / Web guides
├── assets/
│   └── templates/
│       ├── MD3ETheme.kt              # MaterialExpressiveTheme setup template
│       ├── Color.kt                  # Full 48-role color scheme template
│       ├── Type.kt                   # 15 base type styles (+ 15 Emphasized slots documented)
│       └── Shape.kt                  # 8-size shape scale template
└── scripts/
    ├── generate_theme.py             # Seed color -> complete Compose theme
    ├── install_skill.py              # Install into a skills directory (AI can run this)
    └── package_skill.py              # Build dist/md3e.zip (repository only, not shipped)
```

## Key APIs

| Category | M3 | MD3E |
|----------|----|------|
| Theme | `MaterialTheme` | `MaterialExpressiveTheme` |
| Color | `lightColorScheme()` / `darkColorScheme()` | + `expressiveLightColorScheme()` |
| Motion | Easing + duration tokens | `MotionScheme.standard()` / `.expressive()` |
| Opt-in | `@ExperimentalMaterial3Api` | + `@ExperimentalMaterial3ExpressiveApi` |

## Usage Examples

After installing the skill, just ask your AI assistant naturally. The skill auto-triggers on relevant requests:

**Theming setup:**
> "Set up Material 3 Expressive theming for my Compose app with dynamic color support"

**Component creation:**
> "Create a Material 3 Expressive floating toolbar with 3 action buttons"
> "Build a button group with overflow menu using MD3E"
> "Make a Material 3 card list following the design spec"

**Design guidance:**
> "What are the MD3E color roles and when to use each?"
> "What's the difference between M3 and M3E motion system?"
> "Which shape should I use for a FAB?"

**Migration:**
> "Migrate my app from MaterialTheme to MaterialExpressiveTheme"
> "Update my color scheme to include the new M3E fixed color roles"

**Theme generation:**
> "Generate a Compose color scheme from the seed color #6750A4"

## Sources

- [m3.material.io](https://m3.material.io/) — Official Material Design 3 Expressive guidelines
- [androidx.compose.material3](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary) — Official Compose Material 3 API reference
- [Compose Material 3 guide](https://developer.android.com/develop/ui/compose/designsystems/material3) — Official developer guide

## Disclaimer

This skill is for reference and educational purposes. The actual behavior of Material 3 Expressive components may vary depending on the Compose Material 3 library version. Always test in your own environment before relying on it for production.

## License

[Apache License 2.0](./LICENSE) — same as the Material Design components and AndroidX libraries.

## Contributing

See [CONTRIBUTING.md](https://github.com/mfskys/md3e-skill/blob/main/CONTRIBUTING.md) for how to
report issues, propose changes, and submit pull requests. The file is repository-only and is not
included in the release zip.

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for the version history (SemVer).

