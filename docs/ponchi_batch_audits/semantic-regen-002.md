# semantic-regen-002 audit

## Summary

- items: 5
- prompt files: 1
- prompt lint: `pass`
- base images: 7
- overlay images: 4
- contact sheets: 0
- base audit: `pass` 1, `review` 4

## Stage Counts

| stage | count |
| --- | ---: |
| `color_audit` | 2 |
| `overlay_audit` | 3 |

## Prompt Lint Output

```text
ok: 1 file(s)
```

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `J-72` | H100 | `color_audit` | no | yes | `review` | no | `generated_base_pass` |
| 2 | `J-73` | Blackwell | `color_audit` | no | yes | `review` | no | `generated_base_pass` |
| 3 | `F-84` | Ghostty | `overlay_audit` | no | yes | `review` | yes | `generated_base_pass` |
| 4 | `D-51` | Imagen | `overlay_audit` | no | yes | `pass` | yes | `generated_base_pass` |
| 5 | `D-57` | Flow | `overlay_audit` | no | yes | `review` | yes | `generated_base_pass` |
