# Ponchi Wave 004 audit

Wave 004 covers:

- `ponchi-batch-010`
- `ponchi-batch-011`
- `ponchi-batch-012`

## Current summary

| metric | count |
| --- | ---: |
| entries in wave | 60 |
| batch-010 prompt briefs | 20 |
| batch-010 prompt lint pass | 20 |
| batch-010 generated 2:1 bases | 20 |
| batch-010 base audit pass | 20 |
| batch-010 logo_avoid | 9 |
| batch-010 overlay_wait | 11 |
| batch-010 official logo/icon source review required | 11 |
| batch-011 prompt briefs | 0 |
| batch-011 prompt lint pass | 0 |
| batch-011 generated 2:1 bases | 0 |
| batch-011 base audit pass | 0 |
| batch-012 prompt briefs | 0 |
| batch-012 prompt lint pass | 0 |
| batch-012 generated 2:1 bases | 0 |
| batch-012 base audit pass | 0 |
| Wave 004 generated 2:1 bases | 20 / 60 |
| Wave 004 base audit pass | 20 / 60 |

## Batch 010 status

Batch 010 is command/runtime/database material:

- F-80 Node.js
- F-81 bash
- F-82 WSL
- F-83 PowerShell
- F-84 Ghostty
- F-85 SuperClaude Framework
- F-86 ollama
- F-87 sudo
- F-90 Docker
- F-91 .env
- F-100 拡張子早見表
- F-101 .ico
- F-102 .mp4
- F-103 .mp3
- F-104 .webp
- F-110 Lighthouse
- F-111 a11y
- F-120 PostgreSQL
- F-121 SQLite
- F-122 Prisma

Current status:

- 20 / 20 prompt briefs exist under
  `assets/ponchi/pipeline_prompts/ponchi-batch-010/`.
- Prompt lint passes:
  `python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-010\*.md`.
- 20 / 20 generated 2:1 bases exist under
  `assets/ponchi/experiments/batches/ponchi-batch-010/`.
- 20 / 20 base images passed image audit:
  `docs/ponchi_batch_audits/ponchi-batch-010-base-image-audit.md`.
- Contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-010-base-contact-sheet.png`.
- 9 entries are `logo_avoid`.
- 11 entries are `overlay_wait` and need official source review before
  deterministic logo/icon overlay.

## Immediate generation tasks

- Continue Wave 004 with `ponchi-batch-011`.
- Classify Batch 011 logo needs before generating prompts.
- Apply the Batch 010 pattern for brand-risky entries: generate a meaningful
  non-logo base image, keep upper-right clearspace only for official-overlay
  entries, and leave the entry in `overlay_wait` until source review is done.
- Do not promote or write any Wave 004 output to `assets/ponchi/final/`.

## Wave 004 completion target

Wave 004 is complete only when:

- Batches 010-012 have current batch audit files.
- Every entry has prompt, 2:1 base, and base audit results.
- Every brand/channel/logo item is either `official_logo_applied`,
  `overlay_wait` with reason, or `blocked_brand_asset` with reason.
- `docs/ponchi_wave_004_handoff.md` is updated with exact next actions.
