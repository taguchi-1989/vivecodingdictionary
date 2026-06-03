# ponchi-batch-009 audit

## Summary

- items: 20
- prompt files: 20
- prompt lint: `pass`
- base images: 20
- overlay images: 9
- contact sheets: 0
- base audit: `pass` 20

## Stage Counts

| stage | count |
| --- | ---: |
| `color_audit` | 11 |
| `overlay_audit` | 9 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-009-base-image-audit.md`
- contact sheet: `ponchi-batch-009-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `F-37` | Japanese Language Pack for VS Code | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 2 | `F-38` | Markdown All in One | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 3 | `F-40` | npm | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 4 | `F-41` | Vite | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 5 | `F-42` | ビルド | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 6 | `F-44` | pnpm | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 7 | `F-50` | git | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 8 | `F-51` | git push | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 9 | `F-52` | git pull | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 10 | `F-53` | branch | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 11 | `F-54` | commit | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 12 | `F-55` | merge | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 13 | `F-56` | .gitignore | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 14 | `F-57` | リポジトリ | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 15 | `F-58` | git stash | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 16 | `F-59` | README.md | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 17 | `F-60` | GitHub | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 18 | `F-61` | Pull Request | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 19 | `F-62` | GitHub Actions | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 20 | `F-71` | ripgrep (rg) | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
