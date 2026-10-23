# 发布与同步流程

本文件记录 md3e-skill 仓库的 Git 推送、本地技能同步、发布包生成、GitHub Release 发布的完整流程。

> 工作区（源）：克隆到本地的仓库目录（下文用 `<repo>` 表示）
> 安装位置（目标）：`~/.codebuddy/skills/md3e`（Windows 为 `%USERPROFILE%\.codebuddy\skills\md3e`）
> 仓库地址：https://github.com/mfskys/md3e-skill
> 邮箱：使用 GitHub **noreply** 邮箱（在 GitHub → Settings → Emails 查看；避免 GH007）

以下示例中的 `<repo>` 仅为占位，请替换为你本机的实际克隆路径（不要在仓库文档里写真实路径）。

---

## 0. 前置检查

确认本地 Git 配置使用 noreply 邮箱（避免 GH007 邮箱隐私拦截）：

```powershell
cd <repo>
git config user.email "<your-id>+<your-login>@users.noreply.github.com"
git config user.name  "<your-github-login>"
```

---

## 1. 提交并推送代码到 GitHub

```powershell
cd <repo>
git add .
git commit -m "描述本次改动"
git push origin main
```

- 提交邮箱必须是 noreply 邮箱，否则 GitHub 会以 `GH007` 拒绝推送。
- 首次关联远程仓库时用 `git push -u origin main`，之后只需 `git push`。

---

## 2. 打 Tag 并推送（为 Release 准备）

```powershell
cd <repo>
git tag v1.4.0              # 本次发布
# 升级版本示例（当前为 v1.4.0）：
#   git tag v1.5.0          # 新功能
#   git tag v1.4.1          # 修 bug
git push origin v1.4.0
```

- Tag 是 Git 对某次 commit 的版本标记，Release 必须依赖一个 Tag。
- 推送 Tag 之后，Tag 出现在 GitHub，但还**不是** Release。

---

## 3. 生成发布包（md3e.zip）

发布包放在**仓库外**的目录（例如仓库同级的 `dist/`），避免污染仓库：

```powershell
cd <repo>
python scripts/package_skill.py --out ../dist
```

- 生成位置：`<repo的上级目录>/dist/md3e.zip`
- 脚本每次重建整个 zip，发布前重新运行即可。
- **不要用 PowerShell 的 `Compress-Archive`**：它写入的条目用反斜杠分隔（`references\a\b.md`），
  违反 ZIP 规范，在 macOS / Linux 上解压会被当成单个文件名，整棵目录树被压平；它也不会生成
  技能要求的顶层目录。
- 产出的 zip 结构固定为 `md3e/SKILL.md` + `md3e/references/` + `md3e/assets/` + `md3e/scripts/`，
  用户解压后可直接把 `md3e/` 拷进技能目录。
- 这个 zip 用于上传到 GitHub Release 的 "Attach binaries"，方便用户一键下载。
- **不要**把本机绝对路径、用户名等写进仓库内文档后再打包。

---

## 4. 创建 GitHub Release

1. 打开：https://github.com/mfskys/md3e-skill/releases/new
2. 填写：
   - **Choose a tag**：选刚推的 `v1.4.0`（或新版本号）
   - **Release title**：`MD3E Skill v1.4.0`
   - **Release description**：粘贴下方模板
   - **Attach binaries**：把上一步生成的 `md3e.zip` 拖进去
   - **Set as the latest**：勾上
3. 点 **Publish release**

### Release 描述模板

```markdown
MD3E Skill v1.4.0 — Material Design 3 Expressive (MD3E) AI 技能包

适用于 Android Jetpack Compose。可直接放入支持 Agent Skills 的助手（CodeBuddy、Claude Code 等），
也可通过规则 / AGENTS.md 接入 Cursor、Windsurf、Trae、Cline、GitHub Copilot、通义灵码、
文心快码、CodeGeeX 等。

## 功能
- 完整 androidx.compose.material3 API 参考（约 8000 行，稳定线）
- 源码核对的 1.5.0 线签名 + 可直接复制的代码模式 + 49 个官方示例地图
- 263 个 m3.material.io 官方页面（249 规范页 + 14 概览/博客页）
- 48 个色彩角色、30 个排版槽位（15 + 15 Emphasized）、8 档形状、弹簧动效系统
- 全组件目录 + M3/M3E 差异对比 + 迁移指南
- 7 大表现力设计策略 + 设计研究文档
- 4 个 Kotlin 代码模板 + 主题生成器脚本
- 中英双语 README + M3E 笔记英文镜像

## 安装
- 原生技能：把 `md3e/` 放进助手的 skills 目录（CodeBuddy：`.codebuddy/skills/md3e/`；
  Claude Code：`~/.claude/skills/md3e/`）
- 规则驱动：把 `SKILL.md` 内容放进规则入口（`.cursor/rules/`、`.windsurf/rules/`、
  `AGENTS.md`、`.github/copilot-instructions.md` 等），并保留 `md3e/` 文件夹

仓库: https://github.com/mfskys/md3e-skill
```

升级版本时改写 "新版本" 段落，列出本次新增/修复内容。

---

## 5. 同步到本地技能目录（以 CodeBuddy 为例）

源码改动后，需要同步到本地安装位置才能生效。**推荐直接解压发布包**——发布包按白名单构建，
天然不含本地源码克隆、临时目录等任何非技能文件：

```powershell
$dest = Join-Path $env:USERPROFILE '.codebuddy\skills\md3e'
Remove-Item $dest -Recurse -Force -ErrorAction SilentlyContinue
Expand-Archive '<repo>\..\dist\md3e.zip' -Destination (Split-Path $dest) -Force
```

也可以做增量镜像（仓库里若有本地源码克隆等非技能目录，务必用 `/XD` 追加排除）：

```powershell
$src  = '<repo>'
$dest = Join-Path $env:USERPROFILE '.codebuddy\skills\md3e'
robocopy $src $dest /E /XD .git .github dist __pycache__ /XF .gitignore .gitattributes *.pyc *.zip /NFL /NDL /NJH /NJS /NP
```

- 安装位置：`%USERPROFILE%\.codebuddy\skills\md3e\`（用户级技能目录，对所有项目生效）
- **不要用 `Copy-Item "$src\*"`**：它会把隐藏的 `.git` 整个复制进技能目录（几十 MB 的无用数据，
  还会把本地历史带出去）。上面用 robocopy 排除 `.git`、`dist`、`__pycache__` 等再同步。
- robocopy 退出码 **0–7 都是成功**（1 = 复制了文件），≥ 8 才是错误。
- 每次 `md3e/` 内容有更新，重新执行此命令即可镜像同步（robocopy 只复制有变化的部分）。
- 同步后新开一个对话即可使用最新版本。

---

## 完整发布流程（一键顺序执行）

```powershell
$repo = '<repo>'
cd $repo

# 1. 提交代码
git add .
git commit -m "release: v1.4.0"
git push origin main

# 2. 打 Tag
git tag v1.4.0
git push origin v1.4.0

# 3. 生成发布包
python scripts/package_skill.py --out ../dist

# 4. 同步到本地技能目录
$dest = Join-Path $env:USERPROFILE '.codebuddy\skills\md3e'
robocopy $repo $dest /E /XD .git .github dist __pycache__ /XF .gitignore .gitattributes *.pyc *.zip /NFL /NDL /NJH /NJS /NP

Write-Host "完成。接下来去 https://github.com/mfskys/md3e-skill/releases/new 创建 Release。"
```

---

## 版本号约定（SemVer）

当前版本：**v1.4.0**。

- `v1.4.0` → `v1.5.0`：新增功能（向下兼容）
- `v1.4.0` → `v1.4.1`：修 bug（向下兼容）
- `v1.4.0` → `v2.0.0`：破坏性改动（不向下兼容）

---

## 隐私注意

- 仓库内文档**不要**写入本机绝对路径、Windows 用户名、真实邮箱。
- Git 提交一律使用 GitHub noreply 邮箱。
- 发布 zip 前可快速自查：解压后搜索本机用户目录路径、盘符路径、真实姓名。
