# Contributing

Thanks for your interest in improving the **MD3E** skill! This document explains how
to contribute.

## Ways to Contribute

- **Fix errors** in design tokens, API references, or component specs.
- **Add content** for new MD3E components or updated Material guidelines.
- **Improve templates** (`assets/templates/*.kt`) or the theme generator
  (`scripts/generate_theme.py`).
- **Translate** docs or add examples.

## Workflow

1. Fork the repo and create a branch: `git checkout -b fix/short-description`.
2. Make your changes. Keep `SKILL.md` concise — only add context the model lacks.
3. Verify the theme generator runs:
   ```bash
   pip install material-color-utilities   # optional; without it an HSL approximation is used
   python scripts/generate_theme.py --seed #6750A4 --output ./theme/
   ```
4. Run the repository self-audit — it must exit 0:
   ```bash
   python audit_run.py
   ```
5. If you touched anything that ships, rebuild the release package:
   ```bash
   python scripts/package_skill.py --out ../dist
   ```
6. Commit with a clear message, then open a Pull Request against `main`.

## Content Guidelines

- Reference **official** sources: [m3.material.io](https://m3.material.io/) and the
  [androidx.compose.material3](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary)
  API reference.
- Prefer MD3E APIs where available; fall back to baseline M3 and say so explicitly.
- Update `CHANGELOG.md` under the appropriate version (SemVer, see `PUBLISH.md`).
- When refreshing the version baseline, update the date in `SKILL.md`, `README.md`,
  `README.zh-CN.md`, `references/version-baseline.md` and every `references/m3e/*.md`
  (including the `*.en.md` mirrors), then re-run `python audit_run.py`.

## License

By contributing, you agree your contributions are licensed under the
[Apache License 2.0](./LICENSE), the same as this project.
