# Material 3 Expressive 设计语言总览

核对日期：**2026-10-08** ｜ 标记约定：✅ 官方原文已核对 / ⚠️ 需自行复核 / 🚧 实验性 API

| 来源 | 说明 |
| --- | --- |
| Compose 中的 Material Design 3（官方）✅ | https://developer.android.com/develop/ui/compose/designsystems/material3 ｜ 页面更新 2026-09-08 |
| Compose Material 3 版本说明（官方）✅ | https://developer.android.com/jetpack/androidx/releases/compose-material3 ｜ 页面更新 2026-09-09 |
| `m3.material.io` ⚠️ | 站点为 CSR SPA，正文无法抓取，**规范细节需人工查阅** |

---

## 一、M3E 是什么

官方原文（Compose 文档）：

> "Jetpack Compose 提供了 Material You 和 Material 3 Expressive 的实现，后者是 Material Design 的下一代产品。
> M3 Expressive 是 Material Design 3 的扩展版本，包含在**主题、组件、动画、排版**等方面的研究支持更新……
> 它还支持动态配色等 Material You 个性化功能。**M3 Expressive 可与 Android 16 视觉样式和系统界面相得益彰**。" ✅

要点拆解：

| 关系 | 说明 |
| --- | --- |
| M3 vs M3E | M3E 是 **Material 3 的扩展/超集**，不是新的断裂式设计语言 |
| M3E vs Material You | Material You 解决**个性化**（动态取色）；M3E 解决**表现力**（动效、形状、层级表达） |
| M3E vs Android 16 | 与 Android 16 的系统视觉样式配套，视觉一致性更好 |
| 平台 | Android 侧由 `androidx.compose.material3` 实现；**Wear OS 必须用 Wear Compose Material 3 库**，不是本库 ✅ |

---

## 二、主题体系（Material Theming）

M3/M3E 主题由三个子系统构成，通过 `MaterialTheme` 下发 ✅：

```kotlin
MaterialTheme(
    colorScheme = ...,   // 配色方案
    typography  = ...,   // 排版
    shapes      = ...,   // 形状
) {
    // content
}
```

| 子系统 | 内容 | 详见 |
| --- | --- | --- |
| ColorScheme | 5 个关键色 + 各自的 13 色调调色板；角色语义（primary / onPrimary / primaryContainer …） | `color-typography-shape.md` |
| Typography | 5 类 × 3 号 = 15 个样式 | 同上 |
| Shapes | extraSmall → extraLarge 五档圆角 | 同上 |
| Motion | 弹簧物理动效（M3E 新增） | `motion-physics.md` |

---

## 三、层级与强调（Elevation & Emphasis）

### Tonal elevation（色调海拔）

- M3 **主要用色调颜色叠加表达高度**，而非阴影。
- 深色主题中的叠加层也改为色调叠加，**颜色取自主要颜色槽**。
- `Surface` 同时支持 `tonalElevation` 与 `shadowElevation`。

### 组件强调分级

同一语义提供多档强调程度的组件（从最强到最弱）：
`ExtendedFloatingActionButton` → `Button` → `TextButton` ✅

### 文本强调

1. 用 `Surface` / `surfaceVariant` + `onSurface` / `onSurfaceVariant` 的中性组合；
2. 用不同字重（如 `bodyLarge` Bold vs `bodyMedium` Normal）。

> ⚠️ 版本提示：M3 **1.3.0** 起组件默认使用 `SurfaceContainer` 变体，**不再受色调海拔影响**；
> 1.2.0 起 `ColorScheme` 变为**不可变**。按旧版行为调色时会踩坑。

---

## 四、动态取色（Dynamic Color）

- 属于 Material You 的核心：**从用户壁纸派生颜色**，应用到应用与系统界面。
- **仅 Android 12（API 31, `Build.VERSION_CODES.S`）及以上可用**。
- 不可用时必须**回退**到自定义的浅色/深色配色。

```kotlin
val dynamic = Build.VERSION.SDK_INT >= Build.VERSION_CODES.S
val colorScheme = when {
    dynamic && darkTheme  -> dynamicDarkColorScheme(LocalContext.current)
    dynamic && !darkTheme -> dynamicLightColorScheme(LocalContext.current)
    darkTheme             -> DarkColorScheme
    else                  -> LightColorScheme
}
```

**无障碍硬约束**：动态配色本身满足对比度标准，但**自定义编辑时必须成对使用**：
`primary`+`onPrimary`、`primaryContainer`+`onPrimaryContainer`。
官方明确给出反例：**`tertiaryContainer` + `primaryContainer` 对比度不足** ✅

---

## 五、系统界面（System UI）

| 项 | 说明 |
| --- | --- |
| 涟漪（Ripple） | Compose Material 涟漪在 Android 上使用平台 `RippleDrawable`，因此 **Android 12+ 的火花涟漪对所有 Material 组件生效** ✅ |
| 滚动回弹（Stretch Overscroll） | `LazyColumn` / `LazyRow` / `LazyVerticalGrid` **默认开启**，与 API 级别无关，Compose Foundation 1.1.0+ ✅ |
| `material3-ripple` 新库 | 1.5.0-alpha24 新增：用**内嵌焦点环**替代不透明度层 ⚠️（alpha，谨慎采用） |

---

## 六、导航组件与屏幕尺寸

官方给出的选型表 ✅：

| 组件 | 适用场景 |
| --- | --- |
| `NavigationBar` | 紧凑设备，**目的地 ≤ 5 个** |
| `NavigationRail` | 横屏的小型到中型平板或手机 |
| `PermanentNavigationDrawer` / `ModalNavigationDrawer`（可与 `NavigationRail` 组合） | 中型到大型平板，有足够空间展示细节 |

> 真正的自适应做法是**用 `NavigationSuiteScaffold` 按窗口尺寸类自动切换**，
> 见 `../m3-content/foundations/layout/scaffold/overview.md`；上面是底层组件对应关系。

---

## 七、无障碍与可缩放排版

- 动态配色满足对比度标准；色调调色板方法保证默认配色可用。
- M3 字体比例是**可跨设备缩放的动态尺寸类别框架**：例如 `Display Small`
  在手机与平板上下文中**可分配不同值** ✅
- 设计目标覆盖：弱视、失明、听力障碍、认知障碍、运动障碍、情境式障碍（如手臂骨折）。

---

## 八、M3E 落地策略建议（已按"激进策略"更新）

> 📌 本项目采用 **`material3 = 1.5.0-beta01`**，即 **M3E 全套组件都可用**。
> 见 `../version-baseline.md`。

1. **主题先行**：先用 `MaterialTheme` + 动态取色把三大子系统接好，
   这是所有 M3E 组件的前提。
2. **动效用 `MotionScheme`**：组件动画 1.4.0 起已切到 `MotionScheme`，自定义动画应显式取
   `MaterialTheme.motionScheme`，不要自己写死 `tween` 时长。
3. **组件直接用 1.5.0 线**：ToggleButton、ButtonGroup、SplitButton、FAB Menu、
   FlexibleTopAppBar、slot 版 SearchBar 等全部可用；
   但**调用点收敛**到 `ui/expressive/`，并登记退出计划。
4. **不要依赖 `ExperimentalMaterial3ExpressiveApi` 的旧签名**：1.4.0-beta01 已移除该项下的公共 API；
   1.5.0 线持续重命名（见 `compose-api.md` 第四节），升级前必读 release notes。
5. **图标来源切换**：M3 1.4.0 起不再传递 `material-icons-core`，
   且 `androidx.compose.material.icons` 不再推荐，改用 Material Symbols 矢量图。
6. **规范细节以浏览器查阅为准**：动效曲线、组件规格表等精确数值本库标注 ⚠️，
   编码前在 `m3.material.io` 或 Figma Material 3 Design Kit 中确认。
