# Ponchi Wave 003 handoff

Use this file to continue Wave 003 in a fresh Codex thread if the current
thread gets heavy.

## Objective

Continue toward the full 350-entry goal. Wave 003 is the third 60-entry
checkpoint, not the final success condition.

Full goal:

> Regenerate all 350 ponchi images as meaningful 2:1 illustrations, and apply
> official logos or official icons only after official source review and
> deterministic post-compositing. Keep progress and audits numerically visible.

## Current workspace

- Repository: `D:\dev\VibeCodingDictionary`
- Main overview: `docs/ponchi_progress_overview.md`
- Wave audit: `docs/ponchi_wave_003_audit.md`
- Batch 007 summary: `docs/ponchi_batch_007_progress_summary.md`
- Brand audit: `docs/brand_usage_audit.md`
- Pipeline ledger: `ledgers/ponchi_generation_batches.csv`

## Non-negotiable rules

- Do not write to `assets/ponchi/final/` without explicit user confirmation.
- Do not revert unrelated dirty worktree changes.
- Do not use third-party logo downloads when official sources are unclear.
- Do not generate fake logos, app icons, product UI, mascots, readable text, or
  brand-style substitutes.
- Generate base images with clean white clearspace for future official overlays
  only when the entry needs a logo or official icon.
- Keep final candidates under `assets/ponchi/final_candidates/`.

## Current known state

- Batch 007 has 20/20 prompt briefs generated:
  `assets/ponchi/pipeline_prompts/ponchi-batch-007/`.
- Batch 007 prompt lint passes.
- Batch 007 has 20/20 generated base images.
- E-3 - F-3 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-007/` and passed base audit.
- Batch 007 contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-007-base-contact-sheet.png`.
- Batch 007 is 20 `logo_avoid` entries and requires no official overlays.
- Batch 008 has 20/20 prompt briefs generated:
  `assets/ponchi/pipeline_prompts/ponchi-batch-008/`.
- Batch 008 prompt lint passes.
- Batch 008 has 20/20 generated base images.
- F-4 - F-36 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-008/` and passed base audit.
- Batch 008 contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-008-base-contact-sheet.png`.
- Batch 008 is 6 `logo_avoid` entries and 14 `overlay_wait` entries that need
  official source review before deterministic logo/icon overlay.
- Batch 009 has 20/20 prompt briefs generated:
  `assets/ponchi/pipeline_prompts/ponchi-batch-009/`.
- Batch 009 prompt lint passes.
- Batch 009 has 20/20 generated base images.
- F-37 - F-71 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-009/` and passed base audit.
- Batch 009 contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-009-base-contact-sheet.png`.
- Batch 009 is 11 `logo_avoid`, 8 `overlay_wait`, and 1 `overlay_audit`
  entry. F-60 has a local official GitHub asset already recorded, but no
  Batch 009 final promotion has been done.
- Wave 003 base generation is complete: 60/60 generated 2:1 bases and 60/60
  base audit pass.
- Total numerically tracked generated bases are now 140/350.

## Next best actions

1. Start Wave 004 / Batch 010:
   - Inspect `ledgers/ponchi_generation_batches.csv` for `ponchi-batch-010`.
   - Classify logo needs before generation.
   - Add scaffold overrides where the entry text is too abstract or brand-risky.
   - Scaffold prompts and run prompt lint.

2. Generate and audit Batch 010:
   - Generate `1254x627` 2:1 bases.
   - Keep clearspace only for official-overlay entries.
   - Run `scripts\ponchi_image_audit.py` with the bundled Python runtime.
   - Run `python scripts\ponchi_batch_audit.py ponchi-batch-010`.
   - Run `python scripts\ponchi_batch_report.py ponchi-batch-010`.
   - Run `python scripts\ponchi_pipeline_dashboard.py`.

3. Continue official source review:
   - Batch 008 overlay_wait: F-10 - F-17, F-20, F-21, F-30, F-34 - F-36.
   - Batch 009 overlay_wait: F-37, F-38, F-40, F-41, F-44, F-50, F-61, F-62.
   - Record source decisions in `docs/brand_usage_audit.md`.
   - Overlay only official local assets after source review/import.
   - Keep unresolved sources in `overlay_wait`.
