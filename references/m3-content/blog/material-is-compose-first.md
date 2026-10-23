# Material Android is Compose-first

> 来源: https://m3.material.io/blog/material-is-compose-first
> 抓取: 2026-10-19

---

Start migrating to Compose to get the latest from Material

![Material Android](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmpgoi79o-unnamed%20(1).jpg?alt=media)

At [Google I/O 2026](https://io.google/2026), we announced that [Material Android is “all-in” on Compose](https://io.google/2026/explore/technical-session-30), alongside the official [Android Compose-first announcement](https://android-developers.googleblog.com/2026/05/android-ui-development-is-compose-first.html), marking a new chapter in Android development.

Later in 2026, we’ll promote M3 Expressive experimental APIs, making [Material Compose](https://developer.android.com/develop/ui/compose/designsystems/material3?_gl=1*1gllpir*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0Mzk2ODQkajU0JGwwJGgw) 1.5.0 stable. Additionally, we’ll be integrating the new [Styles API](https://developer.android.com/develop/ui/compose/styles?_gl=1*1gllpir*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0Mzk2ODQkajU0JGwwJGgw)for easier, more flexible customization, and have already integrated [Navigation3](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation?_gl=1*1gfyy5b*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0Mzk2ODQkajU0JGwwJGgw) into the Material adaptive library.

To focus on Compose going forward, [Material Views 1.14.0](https://github.com/material-components/material-components-android/releases/tag/1.14.0) (MDC-Android) will be our final stable release for the Views library. There’s never been a better time to migrate to [Jetpack Compose](https://developer.android.com/develop/ui/compose/migrate/migrate-xml-views-to-jetpack-compose).

![Text: Compose Material 3 is going stable.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmov66zhn-02-IO26_133_TSV.png?alt=media)

## The final Material Views release

For years, Material Design has been on a journey to redefine how to build UI on Android. We’ve seen [Jetpack Compose](https://developer.android.com/compose) grow from an ambitious idea into the engine behind the world’s most beautiful apps. As Android’s modern, declarative toolkit, it’s designed to simplify and accelerate UI development with less code and powerful native tools.

While Compose continues to accelerate, our updates for Views have become more focused. For the last few years, we’ve been preparing for a fundamental shift in Android development.

[▶ Video](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmpgotv3m-16x9_Homepage_Hero_050825.mp4?alt=media)

Earlier this month, we reached a major milestone: the stable release of [Material Views 1.14.0](https://github.com/material-components/material-components-android/releases/tag/1.14.0) (MDC-Android). This release officially brings Material 3 Expressive to the Views framework, as well as other improvements, unlocking more delightful experiences for Android makers:

- Expressive themes

- Expressive list component

- Emphasized type scale

- Expressive styles for 11 existing components, like buttons, sliders, progress indicators, and more

With this release, the Material Views library is now entering **maintenance mode**. It won’t get any new features, but will receive critical bug fixes.

## Going Compose-first

Moving forward, Material Android is transitioning to focus all feature development on the [Material Compose library](https://developer.android.com/develop/ui/compose/designsystems/material3?_gl=1*wkss8e*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDAyMjUkajYwJGwwJGgw).

Later in 2026, Material Android will release Compose 1.5.0, which will promote M3 experimental APIs to stable, including M3 Expressive. M3 Expressive APIs are like an expansion pack to M3; you can opt in to them to deliver more premium Android experiences. This includes Material 3 Expressive components, motion systems, and more from the Expressive update. [Read about M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive?utm_source=blog&utm_medium=referral&utm_campaign=IO26)

For designers, the [Material 3 Figma Design Kit](https://www.figma.com/community/file/1035203688168086460/material-3-design-kit) and our [design guidelines](https://m3.material.io/) will continue to reflect the latest of what’s available in the Material Compose library.

## Styles API & adaptive navigation

We also announced the upcoming integration of Compose [Styles](https://developer.android.com/develop/ui/compose/styles?_gl=1*u33d9*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA4NzUkajQzJGwwJGgw) and the recently-launched [Adaptive Navigation](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation?_gl=1*1o80alu*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA4ODAkajM4JGwwJGgw)update [with the new Navigation3 library](https://developer.android.com/guide/navigation/navigation-3?_gl=1*1ka87s6*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA5MDAkajE4JGwwJGgw).

[▶ Video](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmowkaw0g-03-Shapes%20(1).mp4?alt=media)

The [Compose Styles API](https://developer.android.com/develop/ui/compose/styles?_gl=1*1ycph1f*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA5MTkkajYwJGwwJGgw) on Android will make it easier than ever to customize Material components. This will improve overall app performance by skipping the composition phase during style updates and will simplify creating cohesive brand experiences. Integration is ongoing, so stay tuned!

[▶ Video](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmpgrimcu-04-Shrine%20Color%20Change%20(2%20Loops).mp4?alt=media)

For a long time, building adaptive layouts for foldables, tablets, and desktops was complex, requiring makers to manage and switch between navigation frameworks throughout the app. To solve this, we’ve deeply integrated the Material Adaptive library with [Navigation3](https://developer.android.com/guide/navigation/navigation-3?_gl=1*1qvzpce*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA5OTYkajYwJGwwJGgw). Since the navigation library now understands the intent of your screens through metadata, it handles the heavy lifting for you, making implementation much more efficient. [Build adaptive UIs with Material components today](https://developer.android.com/develop/adaptive-apps)

[▶ Video](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmowkgbwx-05-ADAPTIVE_REFLOW_BUILD_RENDER%20(2).mp4?alt=media)

## Migrating from Views to Compose

We know how much you’ve built on Views, but there’s never been a better time to [migrate to Jetpack Compose](https://developer.android.com/develop/ui/compose/migrate/migrate-xml-views-to-jetpack-compose). Get started by migrating your apps screen-by-screen with our [new migration Android skill](https://github.com/android/skills), which you can use with Android Studio, Android CLI, or any other AI tool.

Stay tuned for more updates coming to Material Compose!
