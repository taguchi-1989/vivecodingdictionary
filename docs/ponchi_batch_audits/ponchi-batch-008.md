# ponchi-batch-008 audit

## Summary

- items: 20
- prompt files: 20
- prompt lint: `pass`
- base images: 20
- overlay images: 14
- contact sheets: 0
- base audit: `pass` 20

## Stage Counts

| stage | count |
| --- | ---: |
| `color_audit` | 6 |
| `overlay_audit` | 14 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-008-base-image-audit.md`
- contact sheet: `ponchi-batch-008-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `F-4` | HTML | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 2 | `F-5` | CSS | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 3 | `F-6` | Markdown | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 4 | `F-7` | YAML | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 5 | `F-8` | JSON | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 6 | `F-9` | SVG | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 7 | `F-10` | React | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 8 | `F-11` | Next.js | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 9 | `F-12` | Electron | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 10 | `F-13` | Tauri | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 11 | `F-14` | three.js | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 12 | `F-15` | shadcn/ui | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 13 | `F-16` | Tailwind CSS | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 14 | `F-17` | Astro | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 15 | `F-20` | ESLint | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 16 | `F-21` | Prettier | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 17 | `F-30` | VS Code | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 18 | `F-34` | VS Code 拡張機能 | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 19 | `F-35` | Markdown Preview Enhanced | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 20 | `F-36` | Git Graph | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
