# Ponchi Wave 003 audit

Wave 003 covers the next 60 active entries:

- `ponchi-batch-007`: E-3 - F-3
- `ponchi-batch-008`: next 20 ledger entries
- `ponchi-batch-009`: next 20 ledger entries

## Current summary

| metric | count |
| --- | ---: |
| entries in wave | 60 |
| batch-007 prompt briefs | 20 |
| batch-007 prompt lint pass | 20 |
| batch-007 generated 2:1 bases | 20 |
| batch-007 base audit pass | 20 |
| batch-007 logo_avoid | 20 |
| batch-007 official logo/icon source review required | 0 |
| batch-008 prompt briefs | 20 |
| batch-008 prompt lint pass | 20 |
| batch-008 generated 2:1 bases | 20 |
| batch-008 base audit pass | 20 |
| batch-008 logo_avoid | 6 |
| batch-008 overlay_wait | 14 |
| batch-008 official logo/icon source review required | 14 |
| batch-009 prompt briefs | 20 |
| batch-009 prompt lint pass | 20 |
| batch-009 generated 2:1 bases | 20 |
| batch-009 base audit pass | 20 |
| batch-009 logo_avoid | 11 |
| batch-009 overlay_wait / overlay_audit | 9 |
| batch-009 official logo/icon source review required | 9 |
| Wave 003 generated 2:1 bases | 60 / 60 |
| Wave 003 base audit pass | 60 / 60 |

## Batch 007 status

Batch 007 is benchmark and language material:

- E-3 Terminal-Bench
- E-4 HumanEval
- E-20 MMLU
- E-21 MMLU-Pro
- E-22 GPQA
- E-23 GSM8K
- E-24 MATH
- E-25 AIME
- E-26 Humanity's Last Exam
- E-27 IQ Bench
- E-30 TAU-Bench
- E-31 WebArena
- E-32 GAIA
- E-33 AgentBench
- E-34 OSWorld
- E-50 Chatbot Arena
- E-51 LMSYS Arena
- F-1 JavaScript
- F-2 TypeScript
- F-3 Python

Current status:

- 20 / 20 prompt briefs exist under
  `assets/ponchi/pipeline_prompts/ponchi-batch-007/`.
- Prompt lint passes:
  `python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-007\*.md`.
- 20 / 20 generated 2:1 bases exist under
  `assets/ponchi/experiments/batches/ponchi-batch-007/`.
- 20 / 20 base images passed image audit:
  `docs/ponchi_batch_audits/ponchi-batch-007-base-image-audit.md`.
- Contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-007-base-contact-sheet.png`.
- All 20 entries are `logo_avoid`; no official overlay is needed for this
  batch.

## Immediate generation tasks

- Wave 003 base generation is complete: Batches 007-009 all have 20 / 20
  generated 2:1 bases and 20 / 20 base audit pass.
- Start Wave 004 / `ponchi-batch-010` if continuing base generation.
- Continue official source review for Batch 008 `overlay_wait` entries:
  F-10 - F-17, F-20, F-21, F-30, F-34 - F-36.
- Continue official source review for Batch 009 `overlay_wait` entries:
  F-37, F-38, F-40, F-41, F-44, F-50, F-61, F-62.
- F-60 has a local GitHub official asset and remains in `overlay_audit`; review
  placement before any candidate or final promotion.
- Continue using Batch 007's stricter text controls for benchmark/language
  entries: no readable labels, no red/green pass/fail colors, no product UI,
  and no official-logo substitutes.
- Do not promote or write any Wave 003 output to `assets/ponchi/final/`.

## Wave 003 completion target

Wave 003 is complete only when:

- Batches 007-009 have current batch audit files. Done.
- Every entry has prompt, 2:1 base, and base audit results. Done.
- Every brand/channel/logo item is either `official_logo_applied`,
  `overlay_wait` with reason, or `blocked_brand_asset` with reason.
- `docs/ponchi_wave_003_handoff.md` is updated with exact next actions.
