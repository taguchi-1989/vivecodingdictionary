# ponchi-batch-010 progress summary

Target: 20 entries from `F-80` through `F-122`.

## Numeric summary

| stage | count | target |
| --- | ---: | --- |
| prompt briefs created | 20 / 20 | F-80 - F-122 all entries |
| prompt lint pass | 20 / 20 | F-80 - F-122 all entries |
| 2:1 base images created | 20 / 20 | F-80 - F-122 all entries |
| 2:1 base audit pass | 20 / 20 | F-80 - F-122 all entries |
| logo_avoid | 9 / 20 | F-81, F-87, F-91, F-100 - F-104, F-111 |
| official logo/icon source review required | 11 / 20 | F-80, F-82 - F-86, F-90, F-110, F-120 - F-122 |
| overlay_wait | 11 / 20 | F-80, F-82 - F-86, F-90, F-110, F-120 - F-122 |
| final candidate created | 0 / 20 | not generated |
| final promoted | 0 / 20 | do not copy to `assets/ponchi/final/` yet |

## Entry list

| entry | title | prompt | 2:1 base | logo policy | current status |
| --- | --- | --- | --- | --- | --- |
| F-80 | Node.js | done | pass | waiting | overlay_wait |
| F-81 | bash | done | pass | logo_avoid | base complete |
| F-82 | WSL | done | pass | waiting | overlay_wait |
| F-83 | PowerShell | done | pass | waiting | overlay_wait |
| F-84 | Ghostty | done | pass | waiting | overlay_wait |
| F-85 | SuperClaude Framework | done | pass | waiting | overlay_wait |
| F-86 | ollama | done | pass | waiting | overlay_wait |
| F-87 | sudo | done | pass | logo_avoid | base complete |
| F-90 | Docker | done | pass | waiting | overlay_wait |
| F-91 | .env | done | pass | logo_avoid | base complete |
| F-100 | 拡張子早見表 | done | pass | logo_avoid | base complete |
| F-101 | .ico | done | pass | logo_avoid | base complete |
| F-102 | .mp4 | done | pass | logo_avoid | base complete |
| F-103 | .mp3 | done | pass | logo_avoid | base complete |
| F-104 | .webp | done | pass | logo_avoid | base complete |
| F-110 | Lighthouse | done | pass | waiting | overlay_wait |
| F-111 | a11y | done | pass | logo_avoid | base complete |
| F-120 | PostgreSQL | done | pass | waiting | overlay_wait |
| F-121 | SQLite | done | pass | waiting | overlay_wait |
| F-122 | Prisma | done | pass | waiting | overlay_wait |

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
clearspace for later official-source compositing.

## Next action

Batch 010 base generation is complete. Wave 004 now has 20 / 60 generated
2:1 bases and 20 / 60 base audit pass. Continue with `ponchi-batch-011`, or
return to official source review and deterministic overlays. Do not promote
anything to `assets/ponchi/final/` without explicit approval.
