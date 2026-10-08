# 发布与同步流程

本文件记录 md3e-skill 仓库的 Git 推送、本地技能同步、发布包生成、GitHub Release 发布的完整流程。

> 工作区（源）：克隆到本地的仓库目录（下文用 `<repo>` 表示）
> 安装位置（目标）：`~/.codebuddy/skills/md3e`（Windows 为 `%USERPROFILE%\.codebuddy\skills\md3e`）
> 仓库地址：https://github.com/mfskys/md3e-skill
> 邮箱：使用 GitHub **noreply** 邮箱（在 GitHub → Settings → Emails 查看；避免 GH007）

以下示例中的 `D:\path\to\md3e` 仅为占位，请替换为你本机的实际克隆路径。

---

## 0. 前置检查

确认本地 Git 配置使用 noreply 邮箱（避免 GH007 邮箱隐私拦截）：

```powershell
cd D:\path\to\md3e
git config user.email "<your-id>+<your-login>@users.noreply.github.com"
git config user.name  "<your-github-login>"
```

---

## 1. 提交并推送代码到 GitHub

```powershell
cd D:\path\to\md3e
git add .
git commit -m "描述本次改动"
git push origin main
```

- 提交邮箱必须是 noreply 邮箱，否则 GitHub 会以 `GH007` 拒绝推送。
- 首次关联远程仓库时用 `git push -u origin main`，之后只需 `git push`。

---

## 2. 打 Tag 并推送（为 Release 准备）

```powershell
cd D:\path\to\md3e
git tag v1.3.0              # 本次发布
# 升级版本示例（当前为 v1.3.0）：
#   git tag v1.4.0          # 新功能
#   git tag v1.3.1          # 修 bug
git push origin v1.3.0
```

- Tag 是 Git 对某次 commit 的版本标记，Release 必须依赖一个 Tag。
- 推送 Tag 之后，Tag 出现在 GitHub，但还**不是** Release。

---

## 3. 生成发布包（md3e.zip）

发布包放在**仓库外**的目录（例如仓库同级的 `dist/`），避免污染仓库：

```powershell
cd D:\path\to\md3e
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
   - **Choose a tag**：选刚推的 `v1.3.0`（或新版本号）
   - **Release title**：`MD3E Skill v1.3.0`
   - **Release description**：粘贴下方模板
   - **Attach binaries**：把上一步生成的 `md3e.zip` 拖进去
   - **Set as the latest**：勾上
3. 点 **Publish release**

### Release 描述模板

```markdown
MD3E Skill v1.3.0 — Material Design 3 Expressive (MD3E) AI 技能包

适用于 Android Jetpack Compose，兼容 CodeBuddy / Cursor / Windsurf 等支持 Skill 格式的 AI 编程助手。

## 功能
- 完整 androidx.compose.material3 API 参考（约 8000 行）
- 256 个 m3.material.io 官方设计规范文件（249 规范页 + 7 导航页）
- 48 个色彩角色、15 种排版、5 级形状、弹簧动效系统
- 全组件目录 + M3/M3E 差异对比 + 迁移指南
- 7 大表现力设计策略 + 设计研究文档
- 4 个 Kotlin 代码模板 + 主题生成器脚本
- 中英双语 README + M3E 笔记英文镜像

## 安装
将 `md3e/` 目录复制到 AI 助手的技能文件夹：
- CodeBuddy: `.codebuddy/skills/md3e/`

仓库: https://github.com/mfskys/md3e-skill
```

升级版本时改写 "新版本" 段落，列出本次新增/修复内容。

---

## 5. 同步到本地 CodeBuddy 技能目录

源码改动后，需要同步到本地安装位置才能生效：

```powershell
$src  = 'D:\path\to\md3e'
$dest = Join-Path $env:USERPROFILE '.codebuddy\skills\md3e'
New-Item -ItemType Directory -Path $dest -Force | Out-Null
Copy-Item -Path (Join-Path $src '*') -Destination $dest -Recurse -Force
```

- 安装位置：`%USERPROFILE%\.codebuddy\skills\md3e\`（用户级技能目录，对所有项目生效）
- 每次 `md3e/` 内容有更新，重新执行此命令即可覆盖更新。
- 同步后新开一个对话即可使用最新版本。

---

## 完整发布流程（一键顺序执行）

```powershell
$repo = 'D:\path\to\md3e'
cd $repo

# 1. 提交代码
git add .
git commit -m "release: v1.3.0"
git push origin main

# 2. 打 Tag
git tag v1.3.0
git push origin v1.3.0

# 3. 生成发布包
python scripts/package_skill.py --out ../dist

# 4. 同步到本地技能目录
$dest = Join-Path $env:USERPROFILE '.codebuddy\skills\md3e'
New-Item -ItemType Directory -Path $dest -Force | Out-Null
Copy-Item -Path (Join-Path $repo '*') -Destination $dest -Recurse -Force

Write-Host "完成。接下来去 https://github.com/mfskys/md3e-skill/releases/new 创建 Release。"
```

---

## 版本号约定（SemVer）

当前版本：**v1.3.0**。

- `v1.3.0` → `v1.4.0`：新增功能（向下兼容）
- `v1.3.0` → `v1.3.1`：修 bug（向下兼容）
- `v1.3.0` → `v2.0.0`：破坏性改动（不向下兼容）

---

## 隐私注意

- 仓库内文档**不要**写入本机绝对路径、Windows 用户名、真实邮箱。
- Git 提交一律使用 GitHub noreply 邮箱。
- 发布 zip 前可快速自查：解压后搜索 `C:\Users`、本机盘符路径、真实姓名。
