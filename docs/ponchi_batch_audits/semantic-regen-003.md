# semantic-regen-003 audit

## Summary

- items: 5
- prompt files: 1
- prompt lint: `pass`
- base images: 5
- overlay images: 5
- contact sheets: 0
- base audit: `pass` 4, `review` 1

## Stage Counts

| stage | count |
| --- | ---: |
| `overlay_audit` | 5 |

## Prompt Lint Output

```text
ok: 1 file(s)
```

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `B-1` | Gemini | `overlay_audit` | no | yes | `pass` | yes | `semantic_blind_pass` |
| 2 | `B-2` | Claude | `overlay_audit` | no | yes | `pass` | yes | `semantic_blind_pass` |
| 3 | `B-3` | ChatGPT | `overlay_audit` | no | yes | `pass` | yes | `semantic_blind_pass` |
| 4 | `B-10` | Devin | `overlay_audit` | no | yes | `pass` | yes | `semantic_blind_pass` |
| 5 | `B-14` | Genspark | `overlay_audit` | no | yes | `review` | yes | `semantic_blind_pass` |
