# ponchi-batch-003 audit

## Summary

- items: 20
- prompt files: 20
- prompt lint: `pass`
- base images: 20
- overlay images: 2
- contact sheets: 0
- base audit: `pass` 20

## Stage Counts

| stage | count |
| --- | ---: |
| `overlay_audit` | 2 |
| `overlay_wait` | 18 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-003-base-image-audit.md`
- contact sheet: `ponchi-batch-003-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `B-30` | Amazon Bedrock | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 2 | `B-31` | Excalidraw | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 3 | `B-32` | Figma | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 4 | `B-33` | Canva | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 5 | `B-40` | Reddit | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 6 | `B-41` | arXiv | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 7 | `B-50` | Claude の料金プラン | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 8 | `B-51` | ChatGPT の料金プラン | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 9 | `B-52` | Gemini の料金プラン | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 10 | `B-60` | Suno | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 11 | `B-61` | ACE-Step 1.5 | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 12 | `C-1` | OpenAI | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 13 | `C-2` | Anthropic | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 14 | `C-3` | Google DeepMind | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 15 | `C-4` | Meta AI | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 16 | `C-5` | xAI | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 17 | `C-6` | Mistral AI | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 18 | `C-7` | Hugging Face | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 19 | `C-8` | Microsoft AI | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 20 | `C-9` | NVIDIA | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
