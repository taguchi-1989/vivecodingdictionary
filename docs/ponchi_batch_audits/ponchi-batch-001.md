# ponchi-batch-001 audit

## Summary

- items: 20
- prompt files: 19
- prompt lint: `pass`
- base images: 20
- overlay images: 5
- contact sheets: 1

## Stage Counts

| stage | count |
| --- | ---: |
| `blocked_brand_asset` | 1 |
| `brief_needed` | 11 |
| `overlay_audit` | 5 |
| `overlay_wait` | 3 |

## Prompt Lint Output

```text
ok: 19 file(s)
```

## Items

| # | entry | title | stage | prompt | base | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `A-1` | まえがき | `brief_needed` | yes | yes | no | `not_reviewed` |
| 2 | `A-2` | この本の読み方 | `brief_needed` | yes | yes | no | `not_reviewed` |
| 3 | `A-3` | 図鑑の歩き方 | `brief_needed` | yes | yes | no | `not_reviewed` |
| 4 | `A-4` | 体験区分の凡例 | `brief_needed` | yes | yes | no | `not_reviewed` |
| 5 | `A-5` | 読者レベルの凡例 | `brief_needed` | yes | yes | no | `not_reviewed` |
| 6 | `A-6` | 評価日・時変情報の見方 | `brief_needed` | yes | yes | no | `not_reviewed` |
| 7 | `A-7` | 図のタイプ | `brief_needed` | yes | yes | no | `not_reviewed` |
| 8 | `A-8` | 色・記号の凡例 | `brief_needed` | yes | yes | no | `not_reviewed` |
| 9 | `A-9` | 索引 | `brief_needed` | yes | yes | no | `not_reviewed` |
| 10 | `A-10` | 更新履歴と更新方針 | `brief_needed` | yes | yes | no | `not_reviewed` |
| 11 | `A-11` | 略称表記 | `brief_needed` | yes | yes | no | `not_reviewed` |
| 12 | `B-1` | Gemini | `overlay_wait` | yes | yes | no | `not_reviewed` |
| 13 | `B-2` | Claude | `overlay_audit` | yes | yes | yes | `not_reviewed` |
| 14 | `B-3` | ChatGPT | `overlay_wait` | yes | yes | no | `not_reviewed` |
| 15 | `B-4` | Cursor | `overlay_audit` | yes | yes | yes | `not_reviewed` |
| 16 | `B-5` | GitHub Copilot | `overlay_audit` | no | yes | yes | `not_reviewed` |
| 17 | `B-6` | Windsurf | `blocked_brand_asset` | yes | yes | no | `not_reviewed` |
| 18 | `B-7` | Claude Code | `overlay_audit` | yes | yes | yes | `not_reviewed` |
| 19 | `B-8` | Codex | `overlay_wait` | yes | yes | no | `not_reviewed` |
| 20 | `B-9` | v0 | `overlay_audit` | yes | yes | yes | `not_reviewed` |
