# ponchi-batch-010 progress summary

Target: 20 entries from `F-80` through `F-122`.

## Numeric summary

| stage | count | target |
| --- | ---: | --- |
| prompt briefs created | 20 / 20 | F-80 - F-122 all entries |
| prompt lint pass | 20 / 20 | F-80 - F-122 all entries |
| 2:1 base images created | 20 / 20 | F-80 - F-122 all entries |
| 2:1 base audit pass | 20 / 20 | F-80 - F-122 all entries |
| logo_avoid / confirmed logo-less | 10 / 20 | F-81, F-85, F-87, F-91, F-100 - F-104, F-111 |
| overlay_audit | 10 / 20 | F-80, F-82, F-83, F-84, F-86, F-90, F-110, F-120, F-121, F-122 |
| overlay_wait | 0 / 20 | none |
| color_audit | 10 / 20 | F-81, F-85, F-87, F-91, F-100 - F-104, F-111 |
| final candidate created | 20 / 20 | all batch entries staged as review_pending |
| color audit pass | 20 / 20 | all staged candidates |
| final promoted | 0 / 20 | do not copy to `assets/ponchi/final/` yet |

## Entry list

| entry | title | prompt | 2:1 base | logo policy | current status |
| --- | --- | --- | --- | --- | --- |
| F-80 | Node.js | done | pass | applied | overlay_audit |
| F-81 | bash | done | pass | logo_avoid | color_audit |
| F-82 | WSL | done | pass | applied | overlay_audit |
| F-83 | PowerShell | done | pass | applied | overlay_audit |
| F-84 | Ghostty | done | pass | applied | overlay_audit |
| F-85 | SuperClaude Framework | done | pass | confirmed logo-less after official repo review | color_audit |
| F-86 | ollama | done | pass | applied | overlay_audit |
| F-87 | sudo | done | pass | logo_avoid | color_audit |
| F-90 | Docker | done | pass | applied | overlay_audit |
| F-91 | .env | done | pass | logo_avoid | color_audit |
| F-100 | 拡張子早見表 | done | pass | logo_avoid | color_audit |
| F-101 | .ico | done | pass | logo_avoid | color_audit |
| F-102 | .mp4 | done | pass | logo_avoid | color_audit |
| F-103 | .mp3 | done | pass | logo_avoid | color_audit |
| F-104 | .webp | done | pass | logo_avoid | color_audit |
| F-110 | Lighthouse | done | pass | applied | overlay_audit |
| F-111 | a11y | done | pass | logo_avoid | color_audit |
| F-120 | PostgreSQL | done | pass | applied | overlay_audit |
| F-121 | SQLite | done | pass | applied | overlay_audit |
| F-122 | Prisma | done | pass | applied | overlay_audit |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-010/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-010/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-010-base-image-audit.md`
- Base audit CSV: `ledgers/ponchi_batch_010_base_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-010-base-contact-sheet.png`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-010.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-010.md`

## Visual QA

Contact sheet review passed for all 20 generated bases. F-102, F-110, and
F-111 were regenerated to remove text-like marks, brand-like UI, and animal
imagery. The 11 official-logo entries have deterministic blank upper-right
clearspace for later official-source compositing or confirmed logo-less review.
F-85 is confirmed logo-less after official repository review found no
SuperClaude-specific logo, icon, or lockup; do not synthesize a wordmark or use
Claude/Anthropic/GitHub marks.

## Next action

Batch 010 base generation is complete, and all 20 entries are staged as
review-pending candidates. Return to the remaining older `overlay_wait` rows.
Do not promote anything to `assets/ponchi/final/` without explicit approval.
