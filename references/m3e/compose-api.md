# M3E 在 Compose 中的 API 与迁移

核对日期：**2026-10-08**
来源：Compose Material 3 官方版本说明（页面更新 2026-10-07）✅ +
Compose 中的 Material Design 3（页面更新 2026-09-08）✅

---

> 📌 **版本策略**：本项目**采用最新版本（含 Alpha/Beta/RC）**——
> 即 `material3 = 1.5.0-beta01`，见 `../version-baseline.md`。
> 本文件中"稳定线（1.4.0）"的表述只是**官方通道状态说明**，不代表我们的选择。

## 一、版本门槛速查

| 能力 | 最低版本 | 稳定性 |
| --- | --- | --- |
| `MaterialTheme`（colorScheme / typography / shapes） | M3 早期 | ✅ 稳定 |
| 动态取色（`dynamicLightColorScheme` 等） | M3 早期，需 **API 31+** | ✅ 稳定 |
| 组件动画切换到 `MotionScheme` | **1.4.0** | ✅ 稳定 |
| `MotionScheme.standard()` / `expressive()` | 1.4.0-alpha02 起（由 `standardMotionScheme`/`expressiveMotionScheme` 重命名） | 随版本 |
| `MaterialExpressiveTheme`、`expressiveLightColorScheme` | 1.5.0-alpha18 | ⚠️ 1.5.0 线 |
| `ToggleButton` / FAB Menu | 1.4.0-alpha19 | ⚠️ 1.5.0 线 |
| `ButtonGroup` | 1.4.0-alpha22 | ⚠️ 1.5.0 线 |
| `SplitButton` | 1.4.0-alpha20 | ⚠️ 1.5.0 线 |
| Flexible TopAppBar 系列 / `FlexibleBottomAppBar` | 1.5.0-alpha23 | ⚠️ 1.5.0 线 |
| `FloatingToolbar` | 1.5.0-alpha22 | ⚠️ 1.5.0 线 |
| `SearchBarState` + slot 版 `SearchBar` | 1.5.0-alpha24 | ⚠️ 1.5.0 线 |
| `carouselParallaxScrollEffect` | 1.5.0-alpha28 | ⚠️ 1.5.0 线 |
| `material3-ripple` | 1.5.0-alpha24 | ⚠️ 1.5.0 线（独立库） |
| `PolygonShape` 就地 transform API | 1.5.0-beta01 | ⚠️ 1.5.0 线 |
| `CarouselDefaults.ItemSpacing` / `.ContentPadding` | 1.5.0-beta01 | ⚠️ 1.5.0 线 |

**关键结论**：**M3E 的完整组件集目前只在 1.5.0 线**（该线已于 2026-10-07 进入 beta）。
稳定线（1.4.0）提供的是"M3 + MotionScheme + 部分 Expressive"，不包含全套 M3E 新组件。

---

## 二、稳定线（1.4.0）的破坏性变更

| 变更 | 影响与处理 |
| --- | --- |
| **移除 `material-icons-core` 传递依赖** | 用到图标必须**显式声明**依赖（I735ff, b/349894318） |
| **`androidx.compose.material.icons` 不再推荐** | 官方建议改用 fonts.google.com/icons 的 Material Symbols 矢量图 |
| `NavigationBarItem` / `NavigationRailItem` 选中标签色 | `onSurface` → **`secondary`**；恢复需手动设 `selectedTextColor = MaterialTheme.colorScheme.onSurface` |
| 组件动画机制 | 全部改用新的 **`MotionScheme`** |
| **1.4.0-beta01 移除了所有 `ExperimentalMaterial3ExpressiveApi` / `ExperimentalMaterial3ComponentOverrideApi` 的公共 API** | 想继续用必须切到 **1.5.0 线** |

---

## 三、迁移到 M3E 的步骤

```
1. 锁定版本策略
   ├─ 稳：material3 = 1.4.0（BOM 决定），只用稳定组件 + MotionScheme
   └─ 全：material3 = 1.5.0-betaNN（compose-bom-alpha 已覆盖 material3，一般无需单独写版本）

2. 主题层
   ├─ 浅/深色 ColorScheme（Material Theme Builder 生成 Color.kt / Theme.kt）
   ├─ 动态取色：API 31+ 判断 + 回退
   └─ （可选）MaterialExpressiveTheme + expressiveLightColorScheme ⚠️alpha

3. 动效层
   └─ 所有自定义动画改从 MaterialTheme.motionScheme 取 spec
      ❌ 删除散落的 tween(300) / spring(stiffness=...) 硬编码

4. 图标层
   ├─ 显式声明 material-icons 依赖，或
   └─ 改用 Material Symbols 生成的矢量（推荐）

5. 组件层（渐进）
   ├─ 先替换：TopAppBar → Flexible 系列、SearchBar → slot 版、底部栏
   └─ 再新增：ToggleButton / ButtonGroup / SplitButton / FAB Menu / Carousel

6. 校验
   ├─ 深色模式 + 动态取色 + 大字号
   ├─ 各窗口尺寸（见 ../m3-content/foundations/layout/breakpoints/ 的设备矩阵）
   └─ 视觉回归：重点看 surfaceContainer 相关层级（1.3.0 起行为变了）
```

---

## 四、1.5.0 线的 API 变动频率（风险提示）

1.5.0 线在多个月内发生了**大量重命名与移除**，例如：

| 版本 | 变动 |
| --- | --- |
| beta01 | `TopAppBarDefaults.enterAlwaysScrollBehavior` 的 `reverseLayout` 重载以弃用形式恢复；`SliderState` 的 `DraggableState` 恢复（二进制兼容）；`PolygonShape` 改为就地 `transform {}` / `copy()`，`CornerRounding` 上移并新增 `dp()` / `fraction()`；`HorizontalCenteredHeroCarousel` 的 `maxItemWidth` → `preferredItemWidth`；新增 `CarouselDefaults.ItemSpacing` / `.ContentPadding` |
| alpha29 | **源码破坏**：`Slider`/`RangeSlider` 的 `onValueChange` 变为**必填**且参数顺序变化；`TimeInput`/`DateInput` 改用新 `TextFieldState` 文本字段 API |
| alpha28 | `Slider`/`RangeSlider` 无状态重载弃用；`RangeSliderState` 字段重命名 |
| alpha27 | `TopAppBarDefaults` 旧 scrollBehavior 重载移除；`LocalMotionScheme` 移除；`RichTimePickerDialog` → `VibrantTimePickerDialog` |
| alpha26 | `ExposedDropdownMenu` 改为扩展函数（**需改 import**） |
| alpha25 | `TonalToggleButton` → `FilledTonalToggleButton`；ComponentOverride API 移除；`SplitButtonLayout` 弃用 |
| alpha24 | `SearchBarState` 稳定；`material3-ripple` 新库 |
| alpha23 | ComponentOverride API 移除；Expressive AppBar 毕业；`TextFieldLabelPosition.Attached` 弃用 |
| alpha20 | BottomSheet remember 系列统一 |
| alpha18 | `rememberWithGapSearchBarState` 重命名；`Material3ExpressiveApi` 提供免 OptIn 版本 |

**结论**：使用 alpha 组件时，**升级前必须读一遍该版本的 release notes**，
并保证组件调用点集中（包一层自己的封装），降低重命名带来的改动面。

---

## 五、主题接入代码骨架

```kotlin
// Theme.kt
private val DarkColorScheme = darkColorScheme(/* Material Theme Builder 产出 */)
private val LightColorScheme = lightColorScheme(/* ... */)

@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,          // 允许用户关闭动态取色
    content: @Composable () -> Unit,
) {
    val context = LocalContext.current
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ->
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = AppTypography,
        shapes = AppShapes,
        content = content,
    )
}
```

**动效接入**（1.4.0+）：

```kotlin
val motion = MaterialTheme.motionScheme
val spec = motion.defaultSpatialSpec<Float>()
animateFloatAsState(targetValue = target, animationSpec = spec)
```

---

## 六、无障碍与主题的硬约束

| 约束 | 说明 |
| --- | --- |
| 颜色成对使用 | `primary`+`onPrimary`、`primaryContainer`+`onPrimaryContainer`；官方反例：`tertiaryContainer` + `primaryContainer` 对比度不足 |
| 字号放大 | 系统字号放大后必须验证布局不溢出、不截断 |
| 移除动画 | 系统开启"移除动画"时应退化为瞬时切换 |
| 语义 | 所有可交互控件提供 `contentDescription` / semantics |

---

## 七、待人工核对项 ⚠️

1. `m3.material.io` 上的组件**规格表**（尺寸、间距、状态层不透明度）——站点需 JS 渲染；
2. `MotionScheme` 中各 spec 方法的**完整签名与 token 值**；
3. `MaterialShapes` / 形状形变 API 在当前 Compose 版本中的确切可用性；
4. M3E 的**加载指示器（LoadingIndicator）** 等组件在 `material3` 中的归属与稳定性
   （本文件未从 release notes 中核对到明确条目）。
