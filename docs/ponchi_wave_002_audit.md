# Ponchi Wave 002 audit

Wave 002 covers the next 60 active entries:

- `ponchi-batch-004`: C-10 - C-83
- `ponchi-batch-005`: next 20 ledger entries
- `ponchi-batch-006`: next 20 ledger entries

## Current summary

| metric | count |
| --- | ---: |
| entries in wave | 60 |
| batch-004 prompt briefs | 20 |
| batch-004 prompt lint pass | 20 |
| batch-004 generated 2:1 bases | 20 |
| batch-004 base audit pass | 20 |
| batch-004 overlay_wait | 9 |
| batch-004 prompt_review | 11 |
| batch-004 logo_avoid | 11 |
| batch-004 official logo/icon source review required | 9 |
| batch-005 prompt briefs | 20 |
| batch-005 prompt lint pass | 20 |
| batch-005 generated 2:1 bases | 20 |
| batch-005 base audit pass | 20 |
| batch-005 overlay_ready | 7 |
| batch-005 overlay_wait | 13 |
| batch-006 prompt briefs | 20 |
| batch-006 prompt lint pass | 20 |
| batch-006 generated 2:1 bases | 20 |
| batch-006 base audit pass | 20 |
| batch-006 overlay_ready | 3 |
| batch-006 overlay_wait | 15 |
| batch-006 logo_avoid | 2 |
| Wave 002 generated 2:1 bases | 60 / 60 |
| Wave 002 base audit pass | 60 / 60 |

## Batch 004 status

Batch 004 is mixed company, person, and creator/channel material:

- C-10 Moonshot AI
- C-11 Z.ai
- C-12 TSMC
- C-13 Groq
- C-14 AMD
- C-50 Sam Altman
- C-51 Dario Amodei
- C-52 Demis Hassabis
- C-53 Andrej Karpathy
- C-54 Ilya Sutskever
- C-55 Mira Murati
- C-56 Yann LeCun
- C-57 Geoffrey Hinton
- C-58 Elon Musk
- C-59 Jensen Huang
- C-60 Ray Kurzweil
- C-80 AI大学
- C-81 にゃんた
- C-82 まさお
- C-83 AI の羅針盤

Current prompt status:

- 20 / 20 prompt briefs exist under
  `assets/ponchi/pipeline_prompts/ponchi-batch-004/`.
- Prompt lint passes:
  `python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-004\*.md`.
- 9 / 20 entries are `overlay_wait` and need official logo/icon source review
  before overlay.
- 11 / 20 entries are `prompt_review` with `logo_avoid`; generate as
  no-logo person concept diagrams and avoid real-person likeness.
- 20 / 20 generated 2:1 bases exist under
  `assets/ponchi/experiments/batches/ponchi-batch-004/`.
- C-10 - C-14, C-50 - C-60, and C-80 - C-83 passed base audit:
  `docs/ponchi_batch_audits/ponchi-batch-004-base-image-audit.md`.
- Contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-004-base-contact-sheet.png`.

## Immediate generation tasks

- Wave 002 base generation is complete: Batches 004-006 all have 20 / 20
  generated 2:1 bases and 20 / 20 base audit pass.
- Start Wave 003 / `ponchi-batch-007` if continuing base generation.
- Continue official source review for Batch 004 `overlay_wait` entries:
  C-10 - C-14 and C-80 - C-83.
- Continue official source review for Batch 005 `overlay_wait` entries:
  D-1 - D-14, D-30, D-35, D-40 - D-41.
- Continue official source review for Batch 006 `overlay_wait` entries:
  D-42 - D-47, D-51, D-53 - D-58, D-60, D-70.
- Batch 006 `overlay_ready` entries D-50, D-52, and D-71 can move to
  deterministic OpenAI wordmark overlay after placement review.
- For Batch 004 person entries C-50 - C-60, keep them as no-logo concept
  diagrams unless later review changes the classification.
- Do not promote or write any Wave 002 output to `assets/ponchi/final/`.

## Wave 002 completion target

Wave 002 is complete only when:

- Batches 004-006 have current batch audit files.
- Every entry has prompt, 2:1 base, and base audit results.
- Every brand/channel/logo item is either `official_logo_applied`,
  `overlay_wait` with reason, or `blocked_brand_asset` with reason.
- `docs/ponchi_wave_002_handoff.md` is updated with exact next actions.
