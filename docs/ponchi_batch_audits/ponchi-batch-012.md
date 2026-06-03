# ponchi-batch-012 audit

## Summary

- items: 20
- prompt files: 20
- prompt lint: `pass`
- base images: 20
- overlay images: 0
- contact sheets: 0
- base audit: `pass` 20

## Stage Counts

| stage | count |
| --- | ---: |
| `color_audit` | 20 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-012-base-image-audit.md`
- contact sheet: `ponchi-batch-012-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `G-2` | Token | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 2 | `G-3` | Dictation | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 3 | `G-4` | System Prompt | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 4 | `G-5` | Context Window | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 5 | `G-6` | One-shot | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 6 | `G-7` | 指示追従性 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 7 | `G-8` | 決定論的／非決定論的 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 8 | `G-9` | effort レベル | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 9 | `G-10` | Prompt Engineering | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 10 | `G-11` | Context Engineering | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 11 | `G-12` | Agent Design | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 12 | `G-13` | Few-shot Learning | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 13 | `G-14` | Thinking モデル | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 14 | `G-15` | RAG | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 15 | `G-16` | Embedding | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 16 | `G-17` | ベクトル DB | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 17 | `G-18` | Chain of Thought | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 18 | `G-19` | Prompt Caching | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 19 | `G-20` | CLAUDE.md | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 20 | `G-21` | AGENTS.md | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
