# ponchi-batch-002 audit

## Summary

- items: 20
- prompt files: 20
- prompt lint: `pass`
- base images: 20
- overlay images: 18
- contact sheets: 1
- base audit: `pass` 20

## Stage Counts

| stage | count |
| --- | ---: |
| `color_audit` | 1 |
| `overlay_audit` | 18 |
| `overlay_wait` | 1 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Legacy Final Image Audit

Existing `assets/ponchi/final/` images are legacy evidence only. Use this audit to decide whether to regenerate; do not treat these files as approved final candidates.

- image audit: `ponchi-batch-002-legacy-final-image-audit.md`
- contact sheet: `ponchi-batch-002-legacy-final-contact-sheet.png`

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-002-base-image-audit.md`
- contact sheet: `ponchi-batch-002-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `B-10` | Devin | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 2 | `B-11` | Bolt.new | `overlay_audit` | yes | yes | `pass` | yes | `accept_overlay` |
| 3 | `B-12` | Perplexity | `overlay_audit` | yes | yes | `pass` | yes | `accept_overlay` |
| 4 | `B-13` | ElevenLabs | `overlay_audit` | yes | yes | `pass` | yes | `accept_overlay` |
| 5 | `B-14` | Genspark | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 6 | `B-15` | Microsoft Copilot | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 7 | `B-16` | Microsoft 365 Copilot | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 8 | `B-17` | Edge Copilot | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 9 | `B-18` | Aqua Voice | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 10 | `B-19` | Claude Cowork | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 11 | `B-20` | Vercel | `overlay_audit` | yes | yes | `pass` | yes | `accept_overlay` |
| 12 | `B-21` | Netlify | `overlay_audit` | yes | yes | `pass` | yes | `accept_overlay` |
| 13 | `B-22` | Cloudflare | `overlay_audit` | yes | yes | `pass` | yes | `accept_overlay` |
| 14 | `B-23` | AWS | `overlay_wait` | yes | yes | `pass` | no | `not_reviewed` |
| 15 | `B-24` | Google Cloud | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 16 | `B-25` | Azure | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 17 | `B-26` | Azure OpenAI | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 18 | `B-27` | Vertex AI | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 19 | `B-28` | Render | `overlay_audit` | yes | yes | `pass` | yes | `accept_overlay` |
| 20 | `B-29` | Supabase | `overlay_audit` | yes | yes | `pass` | yes | `accept_overlay` |
