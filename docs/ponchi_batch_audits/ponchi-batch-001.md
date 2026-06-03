# ponchi-batch-001 audit

## Summary

- items: 20
- prompt files: 20
- prompt lint: `pass`
- base images: 20
- overlay images: 9
- contact sheets: 1
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

- image audit: `ponchi-batch-001-base-image-audit.md`
- contact sheet: `ponchi-batch-001-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `A-1` | まえがき | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 2 | `A-2` | この本の読み方 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 3 | `A-3` | 図鑑の歩き方 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 4 | `A-4` | 体験区分の凡例 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 5 | `A-5` | 読者レベルの凡例 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 6 | `A-6` | 評価日・時変情報の見方 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 7 | `A-7` | 図のタイプ | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 8 | `A-8` | 色・記号の凡例 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 9 | `A-9` | 索引 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 10 | `A-10` | 更新履歴と更新方針 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 11 | `A-11` | 略称表記 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 12 | `B-1` | Gemini | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 13 | `B-2` | Claude | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 14 | `B-3` | ChatGPT | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 15 | `B-4` | Cursor | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 16 | `B-5` | GitHub Copilot | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 17 | `B-6` | Windsurf | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 18 | `B-7` | Claude Code | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 19 | `B-8` | Codex | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 20 | `B-9` | v0 | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
