# ponchi-batch-005 audit

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
| `overlay_ready` | 7 |
| `overlay_wait` | 13 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-005-base-image-audit.md`
- contact sheet: `ponchi-batch-005-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `D-1` | Gemini 2 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 2 | `D-2` | Gemini 2.5 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 3 | `D-3` | Gemini 3 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 4 | `D-4` | Gemini 3.1 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 5 | `D-10` | Claude 3 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 6 | `D-11` | Claude 3.5 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 7 | `D-12` | Claude 4 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 8 | `D-13` | Claude 4.5 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 9 | `D-14` | Claude Mythos Preview | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 10 | `D-20` | GPT-5 系 | `overlay_ready` | yes | yes | `pass` | no | `not_reviewed` |
| 11 | `D-21` | GPT-4 系 | `overlay_ready` | yes | yes | `pass` | no | `not_reviewed` |
| 12 | `D-22` | o1 系 | `overlay_ready` | yes | yes | `pass` | no | `not_reviewed` |
| 13 | `D-23` | o3 系 | `overlay_ready` | yes | yes | `pass` | no | `not_reviewed` |
| 14 | `D-24` | GPT-3 系 | `overlay_ready` | yes | yes | `pass` | no | `not_reviewed` |
| 15 | `D-25` | GPT-1 / GPT-2 系 | `overlay_ready` | yes | yes | `pass` | no | `not_reviewed` |
| 16 | `D-26` | gpt-oss | `overlay_ready` | yes | yes | `pass` | no | `not_reviewed` |
| 17 | `D-30` | Grok 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 18 | `D-35` | Cursor Composer | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 19 | `D-40` | Llama 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 20 | `D-41` | Mistral 系 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
