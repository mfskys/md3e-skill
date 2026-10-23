package com.example.app.ui.theme

import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Shapes
import androidx.compose.ui.unit.dp

/**
 * M3E shape scale — 8 sizes (M3's 5 + 3 Expressive sizes).
 * Values mirror `ShapeTokens.kt` in androidx-main (verified 2026-10-23).
 *
 * The three M3E sizes exist only on the 1.5.0 line (`material3:1.5.0-beta02`).
 * On the stable 1.4.0 line, delete [largeIncreased] / [extraLargeIncreased] /
 * [extraExtraLarge] — the `Shapes` constructor there has 5 parameters.
 */
val AppShapes = Shapes(
    extraSmall = RoundedCornerShape(4.dp),
    small = RoundedCornerShape(8.dp),
    medium = RoundedCornerShape(12.dp),
    large = RoundedCornerShape(16.dp),
    extraLarge = RoundedCornerShape(28.dp),
    largeIncreased = RoundedCornerShape(20.dp),
    extraLargeIncreased = RoundedCornerShape(32.dp),
    extraExtraLarge = RoundedCornerShape(48.dp),
)
