# ponchi-batch-006 audit

## Summary

- items: 20
- prompt files: 20
- prompt lint: `pass`
- base images: 20
- overlay images: 17
- contact sheets: 0
- base audit: `pass` 20

## Stage Counts

| stage | count |
| --- | ---: |
| `color_audit` | 2 |
| `overlay_audit` | 17 |
| `overlay_wait` | 1 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-006-base-image-audit.md`
- contact sheet: `ponchi-batch-006-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `D-42` | Gemma 系 | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 2 | `D-43` | Qwen 系 | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 3 | `D-44` | Kimi | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 4 | `D-45` | GLM | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 5 | `D-46` | DeepSeek V3 | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 6 | `D-47` | DeepSeek R1 | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 7 | `D-50` | DALL-E | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 8 | `D-51` | Imagen | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 9 | `D-52` | Sora | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 10 | `D-53` | Veo | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 11 | `D-54` | Stable Diffusion | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 12 | `D-55` | Nano Banana | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 13 | `D-56` | Seedance | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 14 | `D-57` | Flow | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 15 | `D-58` | Whisk | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 16 | `D-60` | AlphaGo | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 17 | `D-70` | Amical | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 18 | `D-71` | Whisper | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 19 | `E-1` | SWE-Bench | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 20 | `E-2` | SWE-Bench Verified | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
