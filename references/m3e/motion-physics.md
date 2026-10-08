# M3E 动效物理系统（Motion Physics）

核对日期：**2026-10-08**

| 内容 | 来源 | 可信度 |
| --- | --- | --- |
| `MotionScheme` 存在、`MaterialTheme.motionScheme`、组件动画改用 `MotionScheme` | Compose Material 3 官方版本说明（2026-09-09） | ✅ |
| `MotionScheme.standard()` / `MotionScheme.expressive()` 命名 | 同上（1.4.0-alpha02 由 `standardMotionScheme`/`expressiveMotionScheme` 重命名） | ✅ |
| 动效物理系统的**概念**（spring 驱动、spatial/effects 分类） | m3.material.io 的标题与摘要，正文为 CSR 无法抓取 | ⚠️ |
| **具体 token 数值**（stiffness / dampingRatio / 时长） | **未从官方原文核对** | ⚠️⚠️ |

> 使用原则：**不要**把本文件里的任何数值抄进代码。
> 需要精确参数时，读代码里的 `MaterialTheme.motionScheme` API，或人工在
> `m3.material.io/styles/motion` 与 `MotionTokens` 源码中确认。

---

## 一、范式转变：从「时长 + 曲线」到「弹簧物理」

| 维度 | 传统模型 | M3E 物理模型 |
| --- | --- | --- |
| 驱动方式 | `durationMillis` + `easing` 曲线 | 弹簧模拟（`stiffness` + `dampingRatio`） |
| 结束条件 | 固定时长到点即停 | 由物理量衰减到静止，系统自动"结算" |
| 中断处理 | 需要手动算速度 | 天然携带速度，可无缝续接（速度继承） |
| 表现力 | 曲线决定观感 | 阻尼比决定是否有回弹 |

**推论**：弹簧动画**不能用时长去"卡"**。写 `tween(300)` 再套弹簧是没有意义的组合。

---

## 二、动效分类（官方概念，⚠️ 细节待核）

| 分类 | 涵盖的属性 | 阻尼取向 |
| --- | --- | --- |
| **Spatial（空间）** | 位置、尺寸、旋转等**位移类**变化 | 允许轻微回弹（欠阻尼）以体现表现力 |
| **Effects（效果）** | 透明度、颜色等**原地**变化 | 通常无回弹（临界阻尼），避免视觉噪点 |

**速度分级**：通常存在 fast / default / slow 三档，按**组件体量与叙事重要性**选择
（小组件用快档，大面积/重要转场用慢档）。

> ⚠️ 上述分类与分级的**命名与数量**属于设计规范层面，未从官方页面逐条核对；
> 代码中以 `MotionScheme` 暴露的具名 API 为准（如 `*SpatialSpec` / `*EffectsSpec` 形态的方法）。

---

## 三、Compose 侧用法

### 取用方式

```kotlin
// 主题中的动效方案（1.5.0-alpha27 起 LocalMotionScheme 已移除，只能用这个）
val scheme = MaterialTheme.motionScheme

// 典型形态：按"分类 + 速度档"取 spec，再交给动画 API
val spec = scheme.defaultSpatialSpec<Float>()      // 位移类默认档
val effects = scheme.fastEffectsSpec<Color>()      // 效果类快档

animateFloatAsState(targetValue = x, animationSpec = spec)
```

### 两套方案

| 方案 | 定位 |
| --- | --- |
| `MotionScheme.expressive()` | 更有表现力（默认取向） |
| `MotionScheme.standard()` | 更克制，接近传统观感 |

### 主题接入

- `MaterialExpressiveTheme`（1.5.0 线，自 alpha18 起）可一次性把 M3E 的颜色方案与动效方案接上 ⚠️。
- 组件动画在 **M3 1.4.0 起已改用 `MotionScheme` 定义** ✅ —— 因此自定义组件应与主题方案保持一致，
  不要自己写死时长，否则同屏动效节奏会打架。

---

## 四、迁移与使用规则

| 规则 | 说明 |
| --- | --- |
| **禁止用时长卡弹簧** | 不要 `tween(300)` 包弹簧；也不要为弹簧补 `delay` |
| **统一从主题取 spec** | 用 `MaterialTheme.motionScheme.xxxSpec<T>()`，不在各处 new spec |
| **分类要对** | 位移/尺寸/旋转归 spatial；透明度/颜色归 effects |
| **速度档要一致** | 同屏同类交互用同一档，避免"有的快有的慢" |
| **可中断** | 手势驱动的动画应支持中途接管（Compose 1.12 的 `DeferredAnimatedContent` / `DeferredAnimatedVisibility` 正是为此设计，支持速度传递与无缝交接）✅ |
| **降级** | 系统"移除动画"无障碍设置开启时，动画应退化为瞬时切换 |
| **测试** | 动画测试用 `runWithoutImplicitWait` + 手动推进时钟；只判断有无待处理工作用 `hasPendingWork` ✅ |

---

## 五、传统令牌体系（作为回退，⚠️ 数值待核）

M3E 并未删除旧的"时长 + 缓动"令牌，它们在弹簧不适用处（如需要精确编排的多段动画）仍在使用：

- **时长档**：short / medium / long / extra-long 各 4 级（约 50ms 起，extra-long 到约 1000ms）
- **缓动族**：emphasized、emphasized decelerate、emphasized accelerate，以及 standard /
  decelerate / accelerate 与 legacy 系列

> ⚠️ 以上档位与曲线**未从官方原文核对**（m3.material.io 需 JS 渲染）。
> 需要确切数值时读 Compose 里的 `MotionTokens`，或对照 Material 3 Design Kit。

---

## 六、待补充（需要人工在浏览器中核对）

1. `spring.fast/default/slow` × `spatial/effects` 的完整 token 名称与参数；
2. 各组件的**推荐动效分类**映射表（如 FAB 展开、页面转场分别属于哪一档）；
3. 形状形变（shape morph）与动效的配合规范；
4. 无障碍"移除动画"下的官方降级建议。
