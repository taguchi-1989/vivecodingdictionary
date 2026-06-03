# Ponchi Wave 006 audit

Wave 006 covers:

- `ponchi-batch-016`
- `ponchi-batch-017`
- `ponchi-batch-018`

## Current summary

| metric | count |
| --- | ---: |
| entries in wave | 50 |
| batch-016 prompt briefs | 20 |
| batch-016 prompt lint pass | 20 |
| batch-016 generated 2:1 bases | 20 |
| batch-016 base audit pass | 20 |
| batch-016 logo_avoid | 20 |
| batch-016 overlay_wait | 0 |
| batch-016 official logo/icon source review required | 0 |
| batch-017 prompt briefs | 20 |
| batch-017 prompt lint pass | 20 |
| batch-017 generated 2:1 bases | 20 |
| batch-017 base audit pass | 20 |
| batch-017 logo_avoid | 20 |
| batch-017 overlay_wait | 0 |
| batch-017 official logo/icon source review required | 0 |
| batch-018 prompt briefs | 10 |
| batch-018 prompt lint pass | 10 |
| batch-018 generated 2:1 bases | 10 |
| batch-018 base audit pass | 10 |
| batch-018 logo_avoid | 10 |
| batch-018 overlay_wait | 0 |
| batch-018 official logo/icon source review required | 0 |
| Wave 006 generated 2:1 bases | 50 / 50 |
| Wave 006 base audit pass | 50 / 50 |

## Batch 016 status

Batch 016 covers J-1 through J-32.

Current status:

- 20 / 20 prompt briefs exist under
  `assets/ponchi/pipeline_prompts/ponchi-batch-016/`.
- Prompt lint passes:
  `python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-016\*.md`.
- 20 / 20 generated 2:1 bases exist under
  `assets/ponchi/experiments/batches/ponchi-batch-016/`.
- 20 / 20 base images passed image audit:
  `docs/ponchi_batch_audits/ponchi-batch-016-base-image-audit.md`.
- Contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-016-base-contact-sheet.png`.
- 20 entries are `logo_avoid`.

## Batch 017 status

Batch 017 covers J-33 through J-76.

Current status:

- 20 / 20 prompt briefs exist under
  `assets/ponchi/pipeline_prompts/ponchi-batch-017/`.
- Prompt lint passes:
  `python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-017\*.md`.
- 20 / 20 generated 2:1 bases exist under
  `assets/ponchi/experiments/batches/ponchi-batch-017/`.
- 20 / 20 base images passed image audit:
  `docs/ponchi_batch_audits/ponchi-batch-017-base-image-audit.md`.
- Contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-017-base-contact-sheet.png`.
- 20 entries are `logo_avoid`.

## Batch 018 status

Batch 018 covers J-77 through J-100.

Current status:

- 10 / 10 prompt briefs exist under
  `assets/ponchi/pipeline_prompts/ponchi-batch-018/`.
- Prompt lint passes:
  `python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-018\*.md`.
- 10 / 10 generated 2:1 bases exist under
  `assets/ponchi/experiments/batches/ponchi-batch-018/`.
- 10 / 10 base images passed image audit:
  `docs/ponchi_batch_audits/ponchi-batch-018-base-image-audit.md`.
- Contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-018-base-contact-sheet.png`.
- 10 entries are `logo_avoid`.

## Immediate generation tasks

- Wave 006 base generation is complete: Batches 016-018 all have current prompt,
  base, and audit artifacts.
- Continue remaining tracked base work in `ponchi-batch-001` and
  `ponchi-batch-002`.
- Batch 001 is mostly A/B introductory material and should be classified before
  prompt generation.
- Batch 002 is B-service material and needs official logo/source review where
  deterministic overlays are required.
- Do not promote or write any Wave 006 output to `assets/ponchi/final/`.

## Wave 006 completion target

Wave 006 is complete for base generation:

- Batches 016-018 have current batch audit files. Done.
- Every entry has prompt, 2:1 base, and base audit results. Done.
- Every entry in this wave is `logo_avoid`; no official overlay is required.
- `docs/ponchi_wave_006_handoff.md` is updated with exact next actions. Done.
