# ponchi-batch-010 audit

## Summary

- items: 20
- prompt files: 20
- prompt lint: `pass`
- base images: 20
- overlay images: 10
- contact sheets: 0
- base audit: `pass` 20

## Stage Counts

| stage | count |
| --- | ---: |
| `color_audit` | 10 |
| `overlay_audit` | 10 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-010-base-image-audit.md`
- contact sheet: `ponchi-batch-010-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `F-80` | Node.js | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 2 | `F-81` | bash | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 3 | `F-82` | WSL | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 4 | `F-83` | PowerShell | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 5 | `F-84` | Ghostty | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 6 | `F-85` | SuperClaude Framework | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 7 | `F-86` | ollama | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 8 | `F-87` | sudo | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 9 | `F-90` | Docker | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 10 | `F-91` | .env | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 11 | `F-100` | 拡張子早見表 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 12 | `F-101` | .ico | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 13 | `F-102` | .mp4 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 14 | `F-103` | .mp3 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 15 | `F-104` | .webp | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 16 | `F-110` | Lighthouse | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 17 | `F-111` | a11y | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 18 | `F-120` | PostgreSQL | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 19 | `F-121` | SQLite | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 20 | `F-122` | Prisma | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
