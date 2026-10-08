#!/usr/bin/env python3
"""
generate_theme.py - Generate Compose `Color.kt` + `Theme.kt` from a single seed color.

Derives a complete Material 3 Expressive color scheme (48 roles x light/dark) from one
seed color.

Color engines, in order of preference
--------------------------------------
1. ``material-color-utilities`` — exact HCT. Two API generations are auto-detected:
     * **0.2.x** (Rust / pybind11): ``theme_from_argb_color()`` + ``Variant`` + ``Theme.schemes``
     * **0.1.x** (pure Python):     ``SchemeTonalSpot`` + ``MaterialDynamicColors``
2. Built-in approximation (HSL) — used only when the library is absent. It is a rough
   stand-in, **not** the official HCT algorithm, so values will not match Google's output.

Usage
-----
    python generate_theme.py --seed #6750A4 --package com.example.app --output ./theme/
    python generate_theme.py --seed 0xFF6750A4 --variant expressive --contrast 0.25

Requirements
------------
    pip install material-color-utilities
"""

import argparse
import re
import sys
from pathlib import Path

# --------------------------------------------------------------- 48 roles ---
# (HCT dynamic-scheme / snake_case key, Compose `ColorScheme` parameter)
PARAMS = [
    ('primary', 'primary'), ('on_primary', 'onPrimary'),
    ('primary_container', 'primaryContainer'), ('on_primary_container', 'onPrimaryContainer'),
    ('inverse_primary', 'inversePrimary'),
    ('primary_fixed', 'primaryFixed'), ('primary_fixed_dim', 'primaryFixedDim'),
    ('on_primary_fixed', 'onPrimaryFixed'), ('on_primary_fixed_variant', 'onPrimaryFixedVariant'),
    ('secondary', 'secondary'), ('on_secondary', 'onSecondary'),
    ('secondary_container', 'secondaryContainer'), ('on_secondary_container', 'onSecondaryContainer'),
    ('secondary_fixed', 'secondaryFixed'), ('secondary_fixed_dim', 'secondaryFixedDim'),
    ('on_secondary_fixed', 'onSecondaryFixed'), ('on_secondary_fixed_variant', 'onSecondaryFixedVariant'),
    ('tertiary', 'tertiary'), ('on_tertiary', 'onTertiary'),
    ('tertiary_container', 'tertiaryContainer'), ('on_tertiary_container', 'onTertiaryContainer'),
    ('tertiary_fixed', 'tertiaryFixed'), ('tertiary_fixed_dim', 'tertiaryFixedDim'),
    ('on_tertiary_fixed', 'onTertiaryFixed'), ('on_tertiary_fixed_variant', 'onTertiaryFixedVariant'),
    ('background', 'background'), ('on_background', 'onBackground'),
    ('surface', 'surface'), ('on_surface', 'onSurface'),
    ('surface_variant', 'surfaceVariant'), ('on_surface_variant', 'onSurfaceVariant'),
    ('surface_tint', 'surfaceTint'), ('inverse_surface', 'inverseSurface'),
    ('inverse_on_surface', 'inverseOnSurface'),
    ('error', 'error'), ('on_error', 'onError'),
    ('error_container', 'errorContainer'), ('on_error_container', 'onErrorContainer'),
    ('outline', 'outline'), ('outline_variant', 'outlineVariant'), ('scrim', 'scrim'),
    ('surface_bright', 'surfaceBright'), ('surface_container', 'surfaceContainer'),
    ('surface_container_high', 'surfaceContainerHigh'), ('surface_container_highest', 'surfaceContainerHighest'),
    ('surface_container_low', 'surfaceContainerLow'), ('surface_container_lowest', 'surfaceContainerLowest'),
    ('surface_dim', 'surfaceDim'),
]

# Roles not exposed by material-color-utilities 0.2.x — use an equivalent role instead.
ROLE_ALIASES = {'on_background': 'on_surface'}


# ---------------------------------------------------------- seed parsing ---
def parse_seed(seed_str: str) -> int:
    """Accept ``#RGB``, ``#RRGGBB``, ``#AARRGGBB``, ``0x...`` or bare hex -> ARGB int."""
    s = seed_str.strip().lstrip('#')
    if s[:2].lower() == '0x':
        s = s[2:]
    if len(s) == 3:
        s = ''.join(ch * 2 for ch in s)
    if len(s) == 6:
        s = 'FF' + s
    if len(s) != 8 or not re.fullmatch(r'[0-9a-fA-F]{8}', s):
        raise ValueError(
            f'invalid seed color {seed_str!r}: expected 3, 6 or 8 hex digits '
            f'(e.g. #6750A4, #fff, 0xFF6750A4)'
        )
    return int(s, 16)


def argb_to_compose(argb: int) -> str:
    return f'Color(0x{argb:08X})'


# --------------------------------------------------------------- engines ---
def _engine_mcu_02(mcu, variant_name: str, contrast: float):
    """material-color-utilities >= 0.2 (Rust / pybind11)."""
    variants = {n.lower(): getattr(mcu.Variant, n) for n in dir(mcu.Variant) if n.isupper()}
    if variant_name not in variants:
        raise ValueError(f'unknown variant (available: {", ".join(sorted(variants))})')
    variant = variants[variant_name]

    def gen(seed_argb: int, dark: bool) -> dict:
        theme = mcu.theme_from_argb_color(seed_argb, contrast_level=contrast, variant=variant)
        scheme = theme.schemes.dark if dark else theme.schemes.light
        out = {}
        for key, _ in PARAMS:
            attr = key if hasattr(scheme, key) else ROLE_ALIASES.get(key)
            if attr and hasattr(scheme, attr):
                value = getattr(scheme, attr)
                out[key] = mcu.argb_from_hex(value) if isinstance(value, str) else int(value)
        return out

    return gen, sorted(variants)


def _engine_mcu_01(contrast: float):
    """material-color-utilities 0.1.x (pure Python)."""
    from material_color_utilities.hct import Hct
    from material_color_utilities.scheme.scheme_tonal_spot import SchemeTonalSpot
    from material_color_utilities.dynamiccolor.material_dynamic_colors import MaterialDynamicColors

    def gen(seed_argb: int, dark: bool) -> dict:
        scheme = SchemeTonalSpot(Hct.from_int(seed_argb), dark, contrast)
        colors = MaterialDynamicColors()
        out = {}
        for key, camel in PARAMS:
            color = getattr(colors, camel, None)
            if color is not None:
                out[key] = color.get_argb(scheme)
        return out

    return gen


def resolve_engine(variant_name: str, contrast: float):
    """Return ``(engine_label, gen)``; ``(None, None)`` when the library is unavailable."""
    try:
        import material_color_utilities as mcu
    except ImportError:
        return None, None

    if hasattr(mcu, 'theme_from_argb_color'):
        try:
            gen, _ = _engine_mcu_02(mcu, variant_name, contrast)
            return f'material-color-utilities 0.2.x (HCT, Rust), variant={variant_name}', gen
        except ValueError:
            raise
        except Exception:
            pass  # fall through to the legacy API

    if variant_name != 'tonalspot':
        print(f'Warning: variant {variant_name!r} requires material-color-utilities >= 0.2; '
              f'using tonal-spot instead.', file=sys.stderr)
    try:
        return 'material-color-utilities 0.1.x (HCT, pure Python)', _engine_mcu_01(contrast)
    except Exception:
        return None, None


# ----------------------------------------------- built-in approximation ---
# NOTE: HSL-based, *not* HCT. Only used when material-color-utilities is unavailable.
def _rgb_to_hsl(r: int, g: int, b: int):
    r, g, b = r / 255, g / 255, b / 255
    mx, mn = max(r, g, b), min(r, g, b)
    d = mx - mn
    if d == 0:
        h = 0.0
    elif mx == r:
        h = 60 * (((g - b) / d) % 6)
    elif mx == g:
        h = 60 * (((b - r) / d) + 2)
    else:
        h = 60 * (((r - g) / d) + 4)
    return h, d * 100, (mx + mn) / 2 * 100


def _hsl_to_rgb(h: float, s: float, l: float):
    h = h % 360
    s = min(s / 100, 1)
    l = l / 100
    cv = (1 - abs(2 * l - 1)) * s
    x = cv * (1 - abs((h / 60) % 2 - 1))
    m = l - cv / 2
    if h < 60:
        r, g, b = cv, x, 0
    elif h < 120:
        r, g, b = x, cv, 0
    elif h < 180:
        r, g, b = 0, cv, x
    elif h < 240:
        r, g, b = 0, x, cv
    elif h < 300:
        r, g, b = x, 0, cv
    else:
        r, g, b = cv, 0, x
    return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)


def _tone_argb(hue: float, saturation: float, lightness: float) -> int:
    r, g, b = _hsl_to_rgb(hue, saturation, lightness)
    return (0xFF << 24) | (r << 16) | (g << 8) | b


def gen_approx(seed_argb: int, dark: bool) -> dict:
    """Coarse HSL approximation of an M3 scheme (best effort, not HCT)."""
    r = (seed_argb >> 16) & 0xFF
    g = (seed_argb >> 8) & 0xFF
    b = seed_argb & 0xFF
    h, c, _t = _rgb_to_hsl(r, g, b)
    sec_h = (h + 30) % 360
    tert_h = (h + 60) % 360
    err_h = 25

    roles = {
        'primary': (h, c, 40 if not dark else 80),
        'on_primary': (h, c, 100 if not dark else 20),
        'primary_container': (h, c, 90 if not dark else 30),
        'on_primary_container': (h, c, 10 if not dark else 90),
        'inverse_primary': (h, c, 80 if not dark else 40),
        'secondary': (sec_h, min(c, 24), 40 if not dark else 80),
        'on_secondary': (sec_h, min(c, 24), 100 if not dark else 20),
        'secondary_container': (sec_h, min(c, 24), 90 if not dark else 30),
        'on_secondary_container': (sec_h, min(c, 24), 10 if not dark else 90),
        'tertiary': (tert_h, min(c, 48), 40 if not dark else 80),
        'on_tertiary': (tert_h, min(c, 48), 100 if not dark else 20),
        'tertiary_container': (tert_h, min(c, 48), 90 if not dark else 30),
        'on_tertiary_container': (tert_h, min(c, 48), 10 if not dark else 90),
        'background': (h, 4, 99 if not dark else 10),
        'on_background': (h, 4, 10 if not dark else 90),
        'surface': (h, 4, 99 if not dark else 10),
        'on_surface': (h, 4, 10 if not dark else 90),
        'surface_variant': (h, 4, 90 if not dark else 30),
        'on_surface_variant': (h, 4, 30 if not dark else 80),
        'surface_tint': (h, c, 40 if not dark else 80),
        'inverse_surface': (h, 0, 20 if not dark else 90),
        'inverse_on_surface': (h, 0, 95 if not dark else 20),
        'error': (err_h, 60, 40 if not dark else 80),
        'on_error': (err_h, 60, 100 if not dark else 20),
        'error_container': (err_h, 60, 90 if not dark else 30),
        'on_error_container': (err_h, 60, 10 if not dark else 90),
        'outline': (h, c * 0.3, 50 if not dark else 60),
        'outline_variant': (h, c * 0.3, 80 if not dark else 30),
        'scrim': (0, 0, 0),
        'surface_bright': (h, 4, 98 if not dark else 24),
        'surface_container': (h, 4, 94 if not dark else 12),
        'surface_container_high': (h, 4, 92 if not dark else 17),
        'surface_container_highest': (h, 4, 90 if not dark else 22),
        'surface_container_low': (h, 4, 96 if not dark else 10),
        'surface_container_lowest': (h, 4, 100 if not dark else 4),
        'surface_dim': (h, 4, 87 if not dark else 6),
    }
    fixed = {
        'primary_fixed': (h, c, 90),
        'primary_fixed_dim': (h, c, 80),
        'on_primary_fixed': (h, c, 10),
        'on_primary_fixed_variant': (h, c, 30),
        'secondary_fixed': (sec_h, min(c, 24), 90),
        'secondary_fixed_dim': (sec_h, min(c, 24), 80),
        'on_secondary_fixed': (sec_h, min(c, 24), 10),
        'on_secondary_fixed_variant': (sec_h, min(c, 24), 30),
        'tertiary_fixed': (tert_h, min(c, 48), 90),
        'tertiary_fixed_dim': (tert_h, min(c, 48), 80),
        'on_tertiary_fixed': (tert_h, min(c, 48), 10),
        'on_tertiary_fixed_variant': (tert_h, min(c, 48), 30),
    }
    return {k: _tone_argb(*v) for k, v in {**roles, **fixed}.items()}


# ------------------------------------------------------------- emitters ---
def gen_color_kt(cl: dict, cd: dict, pkg: str, name: str) -> str:
    L = [f'package {pkg}', '', 'import androidx.compose.material3.ColorScheme',
         'import androidx.compose.material3.darkColorScheme', 'import androidx.compose.material3.lightColorScheme',
         'import androidx.compose.ui.graphics.Color', '',
         f'// Auto-generated M3E color scheme for {name} ({len(PARAMS)} roles x 2 schemes)', '']
    L.append('val LightColorScheme: ColorScheme = lightColorScheme(')
    for sn, pn in PARAMS:
        L.append(f'    {pn} = {argb_to_compose(cl.get(sn, 0xFF000000))},')
    L.append(')')
    L.append('')
    L.append('val DarkColorScheme: ColorScheme = darkColorScheme(')
    for sn, pn in PARAMS:
        L.append(f'    {pn} = {argb_to_compose(cd.get(sn, 0xFF000000))},')
    L.append(')')
    L.append('')
    return '\n'.join(L)


def gen_theme_kt(pkg: str, name: str) -> str:
    fn = re.sub(r'[^a-zA-Z0-9]', '', name) + 'Theme'
    return f'''package {pkg}

import android.os.Build
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialExpressiveTheme
import androidx.compose.material3.MotionScheme
import androidx.compose.material3.dynamicDarkColorScheme
import androidx.compose.material3.dynamicLightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext

@Composable
fun {fn}(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {{
    val context = LocalContext.current
    val colorScheme = when {{
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ->
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }}
    MaterialExpressiveTheme(
        colorScheme = colorScheme,
        motionScheme = MotionScheme.expressive(),
        content = content
    )
}}
'''


# ------------------------------------------------------------------ main ---
def main():
    p = argparse.ArgumentParser(description='Generate a Compose M3E color scheme from a seed color.')
    p.add_argument('--seed', required=True, help='Seed color, e.g. #6750A4 / 0xFF6750A4')
    p.add_argument('--package', default='com.example.app')
    p.add_argument('--name', default='App')
    p.add_argument('--output', default='./theme')
    p.add_argument('--variant', default='tonalspot',
                   help='HCT variant: tonalspot (M3 default), expressive, vibrant, content, '
                        'fidelity, monochrome, neutral, rainbow, fruitsalad')
    p.add_argument('--contrast', type=float, default=0.0,
                   help='Contrast level: 0.0 = M3 baseline (default), up to 1.0 = high contrast')
    a = p.parse_args()

    try:
        seed = parse_seed(a.seed)
    except ValueError as exc:
        p.error(str(exc))

    variant = a.variant.lower().replace('-', '').replace('_', '')
    try:
        label, gen = resolve_engine(variant, a.contrast)
    except ValueError as exc:
        p.error(str(exc))

    if gen is None:
        print('Warning: material-color-utilities not installed — using the built-in')
        print('approximation (HSL, not HCT). Colors will not match Google output exactly.')
        print('For accurate HCT colors: pip install material-color-utilities\n')
        label, gen = 'built-in HSL approximation', gen_approx

    light, dark = gen(seed, False), gen(seed, True)

    out = Path(a.output)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'Color.kt').write_text(gen_color_kt(light, dark, a.package, a.name), encoding='utf-8')
    (out / 'Theme.kt').write_text(gen_theme_kt(a.package, a.name), encoding='utf-8')

    print(f'Seed:    0x{seed:08X}')
    print(f'Engine:  {label}')
    print(f'Output:  {out.resolve()}')
    print(f'  Color.kt ({len(PARAMS)} roles x 2 schemes)')
    print('  Theme.kt (MaterialExpressiveTheme + MotionScheme.expressive)')


if __name__ == '__main__':
    main()
