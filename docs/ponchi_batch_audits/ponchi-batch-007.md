# ponchi-batch-007 audit

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
| `brief_needed` | 18 |
| `prompt_review` | 2 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-007-base-image-audit.md`
- contact sheet: `ponchi-batch-007-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `E-3` | Terminal-Bench | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 2 | `E-4` | HumanEval | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 3 | `E-20` | MMLU | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 4 | `E-21` | MMLU-Pro | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 5 | `E-22` | GPQA | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 6 | `E-23` | GSM8K | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 7 | `E-24` | MATH | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 8 | `E-25` | AIME | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 9 | `E-26` | Humanity's Last Exam | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 10 | `E-27` | IQ Bench | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 11 | `E-30` | TAU-Bench | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 12 | `E-31` | WebArena | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 13 | `E-32` | GAIA | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 14 | `E-33` | AgentBench | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 15 | `E-34` | OSWorld | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 16 | `E-50` | Chatbot Arena | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 17 | `E-51` | LMSYS Arena | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
| 18 | `F-1` | JavaScript | `prompt_review` | yes | yes | `pass` | no | `not_reviewed` |
| 19 | `F-2` | TypeScript | `prompt_review` | yes | yes | `pass` | no | `not_reviewed` |
| 20 | `F-3` | Python | `brief_needed` | yes | yes | `pass` | no | `not_reviewed` |
