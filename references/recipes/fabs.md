# FAB（Floating Action Button）— 实现规格

> 基线 **2026-11-10** / `material3` 1.5.0-rc01
> 数值来源：`FloatingActionButton.kt`、`Fab{Small,Baseline,Medium,Large}Tokens.kt`、
> `ExtendedFab{Small,Medium,Large}Tokens.kt`
> 设计意图：官方站点对应页面（已融合进本文件）

## 0. 变体全集

### 0.1 圆形 FAB（4 个 composable，其中 1 个不推荐）

| 尺寸档 | Composable | 实际尺寸 | 状态 |
| --- | --- | --- | --- |
| — | `FloatingActionButton` | **56dp** | ✅ 这就是 M3E 说的 "small FAB" |
| Small | `SmallFloatingActionButton` | **40dp** | ⚠️ **不再推荐**（保留 API） |
| Medium | `MediumFloatingActionButton` | **80dp** | ✅ M3E 新增，需 opt-in |
| Large | `LargeFloatingActionButton` | **96dp** | ✅ |

> 命名陷阱：M3E 设计语言里的 "small FAB" = **56dp**（`FloatingActionButton`），
> 不是 API 里的 `SmallFloatingActionButton`（40dp，已不推荐）。**认 dp 值，别认 API 名字。**

### 0.2 扩展 FAB（3 档 + 1 个基线）

| 尺寸档 | Composable | 高度 | 状态 |
| --- | --- | --- | --- |
| Small | `SmallExtendedFloatingActionButton` | **56dp** | ✅ |
| Medium | `MediumExtendedFloatingActionButton` | **80dp** | ✅ |
| Large | `LargeExtendedFloatingActionButton` | **96dp** | ✅ |
| 基线 | `ExtendedFloatingActionButton` | 56dp | ⚠️ **不再推荐** → 用 small |

### 0.3 复合形态

| Composable | 说明 |
| --- | --- |
| `FloatingActionButtonMenu` | FAB 展开成一组动作（`FloatingActionButtonMenuScope`） |
| `ToggleFloatingActionButton` | 两态切换 + 形态动画（`containerSize` / `containerCornerRadius` 都是 `(进度) -> 值`） |

## 1. 尺寸矩阵（源码 token）

### 圆形

| Token | Small(40) | Baseline(56) | Medium(80) | Large(96) |
| --- | --- | --- | --- | --- |
| `ContainerWidth` | 40dp | 56dp | 80dp | 96dp |
| `ContainerHeight` | 40dp | 56dp | 80dp | 96dp |
| `IconSize` | 24dp | 24dp | **28dp** | **32dp** |
| `ContainerShape` | `CornerMedium` 12dp | `CornerLarge` 16dp | 继承 16dp | `CornerExtraLarge` 28dp |

### 扩展

| Token | Small | Medium | Large |
| --- | --- | --- | --- |
| `ContainerHeight` | 56dp | 80dp | 96dp |
| `IconSize` | 24dp | 28dp | 32dp |
| `IconLabelSpace` | 8dp | 16dp | 20dp |
| `LeadingSpace` / `TrailingSpace` | 16dp | 26dp | 28dp |
| `ContainerShape` | `CornerLarge` 16dp | 继承 16dp | `CornerExtraLarge` 28dp |

FAB 的图标尺寸**随档位变化**（24/28/32dp），扩展 FAB 的内边距也是（16/26/28dp）。
不要给所有尺寸统一写 56dp / 24dp icon。

## 2. 形状

- 圆形 FAB 用 `FloatingActionButtonDefaults.shape`（随档位：12 / 16 / 16 / 28dp）。
- 扩展 FAB 用各自的 `smallExtendedFabShape` / `mediumExtendedFabShape` / `largeExtendedFabShape`
  或 `extendedFabShape`（基线）。
- 需要 squircle / 自定义形状时传 `shape`，但**保持与档位一致的大小**，否则视觉重量会错。

## 3. 颜色

| 样式 | 容器 | 内容 | 状态 |
| --- | --- | --- | --- |
| 默认（primary container） | `primaryContainer` | `onPrimaryContainer` | ✅ 推荐 |
| 其他容器色 | 任意，只要与背景对比足够 | 对应 on 色 | ✅ 允许 |
| **surface 色 FAB** | `surface` | — | ⚠️ **不再推荐** |

`FloatingActionButtonDefaults.containerColor` 是默认值；官方允许换容器色，
但 **surface 色已被明确淘汰**（会和背景糊在一起）。

## 4. 状态与动效

| 场景 | 行为 |
| --- | --- |
| 静止 | 按档位尺寸 |
| Hovered（Web） | 显示带图标的 tooltip；elevation 临时升一级 |
| Pressed | state layer |
| 切换页面 | FAB **先消失、再出现**；只在与新页面相关时出现 |
| 有 tab 的页面 | FAB 短暂消失，内容就位后再出现（表明它不属于某个 tab） |
| 变形 | 用 `FloatingActionButtonMenu` / `ToggleFloatingActionButton` 做形态动画 |

**不要**让 FAB 跟正文一起做过渡动画（官方明文）。

## 5. 代码

### 5.1 三档圆形

```kotlin
FloatingActionButton(onClick = {}) { Icon(Icons.Filled.Add, contentDescription = "Add") }

@OptIn(ExperimentalMaterial3ExpressiveApi::class)
MediumFloatingActionButton(onClick = {}) { Icon(Icons.Filled.Add, contentDescription = "Add") }

LargeFloatingActionButton(onClick = {}) { Icon(Icons.Filled.Add, contentDescription = "Add") }
```

### 5.2 扩展 FAB（图标 + 文字）

```kotlin
SmallExtendedFloatingActionButton(onClick = {}) {
    Icon(Icons.Filled.Edit, contentDescription = null)
    Spacer(Modifier.width(8.dp))
    Text("Compose")
}
```

也可以只给文字（官方允许扩展 FAB **不带图标**）：

```kotlin
MediumExtendedFloatingActionButton(onClick = {}) { Text("Compose") }
```

**但不能只有图标没有文字** —— 那就退回圆形 FAB。

### 5.3 与其他组件组合

```kotlin
Scaffold(
    floatingActionButton = {
        FloatingActionButton(onClick = {}) { Icon(Icons.Filled.Add, contentDescription = "Add") }
    },
) { padding -> /* content */ }
```

FAB 也可以嵌在 `WideNavigationRail` 这类导航组件里（官方允许）；
但**卡片等单个组件不该有自己的 FAB**。

### 5.4 展开菜单

```kotlin
FloatingActionButtonMenu(...) {
    // FloatingActionButtonMenuScope
}
```

参数细节见 `m3e-api-signatures.md`（`containerSize` / `containerCornerRadius` 是进度函数）。

## 6. 选型与设计规则

融合自官方 floating-action-button 与 extended-fab 的 guidelines 页。

### 6.1 什么时候用

- 用于**主要的、正向的动作**（创建、添加、编辑、发消息）。
- **不是每个屏幕都需要 FAB**；当主操作已经由图片或内容本身表达时，不要加。
- **不要用于**次要动作、溢出动效、含义不清晰的动作、**破坏性动作**（删除等）。

### 6.2 每屏一个

- **一屏只放一个 FAB**。多个 FAB 会摧毁层级。
- 扩展 FAB 同样：**一次只强调一个动作**；不要用它表达"一组动作中的一个选项"（那用 `Button`）。
- 建议扩展 FAB 内文字尽量短，必要信息交给图标。

### 6.3 图标

- 用**简单明确**的图标：add / message / edit / share。
- 用 **filled** 图标，不用 outlined。
- 含义应一目了然；含义不明的图标不要用在 FAB 上。

### 6.4 位置与生命周期

- FAB 相对独立于内容层，会**单独移动**，因为它代表更高优先级。
- 切页时：消失 → 重新出现（同位置优先）；**不要**让它跟着正文一起动。
- 有 tab 时：切 tab 时短暂消失，内容就位后再出现。

### 6.5 对比度

FAB 容器与它所在的 surface 必须**对比足够**（否则会"陷"进背景）。这也是 surface 色被淘汰的原因。

## 7. 无障碍

| 项 | 要求 |
| --- | --- |
| 语义标签 | 图标需 `contentDescription`；扩展 FAB 的文字本身就是标签 |
| 触控目标 | 至少 **48×48dp**（40dp 的 `SmallFloatingActionButton` 本就不推荐，部分原因在此） |
| 对比度 | 容器与背景对比足够；图标与容器 ≥ 3:1 |
| Tooltip | Web 上 hover 应显示**带图标**的 tooltip（可含文字标签） |
| 键盘 | `Tab` 到达，`Space` / `Enter` 激活 |

## 8. 淘汰与替代

| 淘汰项 | 替代 | 依据 |
| --- | --- | --- |
| `SmallFloatingActionButton`（40dp） | 56dp `FloatingActionButton` | `floating-action-button/overview`：small FAB no longer recommended |
| `ExtendedFloatingActionButton`（基线） | `SmallExtendedFloatingActionButton` | `extended-fab/overview` |
| surface 色 FAB | 其他容器色（默认 `primaryContainer`） | `floating-action-button/overview` |

## 9. 陷阱

1. M3E 的 "small FAB" 是 **56dp**（`FloatingActionButton`），不是 `SmallFloatingActionButton`（40dp）。
2. `MediumFloatingActionButton` 需要 `@OptIn(ExperimentalMaterial3ExpressiveApi::class)`。
3. 三档图标尺寸不同（24/28/32dp），统一 24dp 会让大 FAB 显得空。
4. 扩展 FAB 可以没有图标，但**不能有图标没有文字**。
5. 不要给卡片、列表项单独加 FAB。
6. 切页动画别把 FAB 和正文绑在一起。
