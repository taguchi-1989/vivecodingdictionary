# Semantic Regen 004 Results

更新日: 2026-06-06

## Status

Wave 4 started after commit `37c31606`.

Completed:

- `A-6` color fix staged.
- `D-35` semantic recompose staged.
- `I-10` color fix staged.
- `J-55` color fix staged.
- `J-76` color fix staged.

Blocked:

- `J-42` new image generation.

Blocker: the built-in image generation tool returned `TooManyRequests` for `J-42` on 2026-06-06. No lower-quality fallback was used.

## Artifacts

- Plan: `docs/ponchi_semantic_audit/semantic_regen_004_plan.md`
- Scope ledger: `ledgers/ponchi_semantic_regen_004_scope.csv`
- Batch images: `assets/ponchi/experiments/batches/semantic-regen-004/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-004/`
- Candidate sheet: `assets/ponchi/final_candidates/semantic-regen-004/final_candidates_contact_sheet.png`
- Base audit: `docs/ponchi_semantic_audit/semantic_regen_004/base_image_audit.md`
- Color audit: `docs/ponchi_semantic_audit/semantic_regen_004/color_audit.md`

## Audit Summary

| entry | action | image audit | color audit | candidate |
| --- | --- | --- | --- | --- |
| `A-6` | palette normalization | review | pass | staged |
| `I-10` | palette normalization | pass | pass | staged |
| `J-55` | palette normalization | pass | pass | staged |
| `J-76` | palette normalization | pass | pass | staged |
| `D-35` | semantic recompose | pass | pass | staged |
| `J-42` | semantic recompose | blocked | blocked | not staged |

`A-6` remains image-audit review because bbox coverage is 0.417. This is a known structure issue in the source composition; the color fix itself passes.

## Next Resume Step

When image generation capacity is available, resume with:

1. Generate `J-42` body with ownership, distributed ledger, and verification flow.
2. Run base/color audits.
3. Stage `J-42` as a review candidate.
4. Build titleless focus review for `D-35` and `J-42`.
