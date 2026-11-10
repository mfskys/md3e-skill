# Recipes — 实现规格（代码化）

这个目录是**唯一的组件实现规格来源**。历史上这里曾同时存在一份 263 页的官网静态镜像，
现在它的内容已全部提炼进这里，镜像本身已删除（可在 git 历史中追溯）。

**为什么要以源码为准**：官方规范的尺寸/间距数据几乎全在插图里，文本抓取拿不到数字；而
`androidx.compose.material3.tokens` 里的常量是精确、可编译的。所以这里的数值一律取自
`*Tokens.kt`，规范页只贡献设计意图、颜色语义、无障碍要求和淘汰声明。

| 维度 | 旧镜像的做法 | 现在的做法 |
| --- | --- | --- |
| 形态 | 人读的规范描述（图片 + 散文） | 实现规格：枚举、数值表、可运行代码 |
| 回答 | "长什么样" | "怎么写出来、参数填多少、为什么不这么写" |
| 数值 | 在图片里，抓不到 | `*Tokens.kt` 常量，逐个核对 |

## 状态图例

每个变体都会标一个状态，**淘汰的也保留、不删**，只是标清楚：

| 标记 | 含义 | 怎么处理 |
| --- | --- | --- |
| ✅ | 官方推荐，M3E 现行 | 直接用 |
| ⚠️ | 官方不再推荐（M3E 淘汰），但 API 仍可用 | 仅在维护旧代码 / 面向 stable M3 时用；新代码换替代 |
| 🧪 | 实验性，需要 `@OptIn(ExperimentalMaterial3ExpressiveApi::class)` | 可用，注意 opt-in |
| 🚫 | 规范有、Compose 无 API | 不要编造，改用替代或自建 |

## 数据优先级（冲突时）

1. `*Tokens.kt` 常量（尺寸、圆角、间距、图标大小）
2. 组件源码签名（参数名、默认值、必填项）
3. 官方规范页的设计意图（颜色语义、状态定义、无障碍、淘汰声明）
4. 官方 sample（组合写法）

## 覆盖进度

| 文件 | 组件 | 状态 |
| --- | --- | --- |
| `buttons.md` | Button 家族（5 样式 × 5 尺寸 × 2 形状 × 状态 + Toggle 4 变体 + SplitButton） | ✅ |
| `button-groups.md` | ButtonGroup（standard / connected × 5 尺寸 × 选中形变） | ✅ |
| `icon-buttons.md` | IconButton 家族（4 样式 × default/toggle × 5 尺寸） | ✅ |
| `fabs.md` | FAB（56/80/96 三档 + Extended 三档 + 菜单/切换形态） | ✅ |
| `app-bars.md` | Small / MediumFlexible / LargeFlexible / TwoRows / docked toolbar | ✅ |
| `navigation.md` | Short bar / Wide rail / drawer 替代关系 | ✅ |
| `tabs.md` | Primary / Secondary / 可滚动 | ✅ |
| `text-fields.md` | TextField / Outlined / Secure / ScrollField / 搜索 | ✅ |
| `selection.md` | Checkbox / Radio / Switch / Slider / Chips + 选型决策表 | ✅ |
| `pickers.md` | Date / DateRange / DateInput / Time | ✅ |
| `containers.md` | Card / Dialog / BottomSheet / Menu / ListItem | ✅ |
| `feedback.md` | Progress / Loading / Snackbar / Tooltip / Badge / Divider | ✅ |
| `carousel.md` | multi-browse / uncontained / hero | ✅ |
| `foundations.md` | 断点 / RTL / 交互模式 / 无障碍基线（跨组件） | ✅ |

36 个官方组件目录已全部覆盖：`components/` 下的每个组件要么在表中单独成节，要么作为变体
并入上述文件（如 `side-sheets` 并入 `containers.md`、`segmented-buttons` 并入
`button-groups.md` 的淘汰替代、`split-button` 并入 `buttons.md`、`fab-menu` 并入 `fabs.md`、
`toolbars` 并入 `app-bars.md`、`search` 并入 `text-fields.md`）。

> 找不到具体组件时，先读 `components-catalog.md` 定位，再读 `m3e-api-signatures.md` 取签名。

## 怎么写一个新文件

照 `buttons.md` 的骨架（7 节）：

0. 变体全集矩阵（含 ✅ / ⚠️ / 🚫）
1. 尺寸矩阵（贴 token 常量名 + 实际值）
2. 形状矩阵（`ShapeTokens` 映射）
3. 颜色矩阵（设计规范的 color roles 表）
4. 状态（elevation / overlay / alpha）
5. 代码（每种变体的最小可运行片段）
6. 淘汰与替代
7. 无障碍 + 陷阱

数值必须来自源码；取不到就写"见 X"，**不要估算**。
