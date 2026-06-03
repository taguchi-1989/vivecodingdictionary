# Ponchi Wave 005 handoff

Use this file to continue after Wave 005 in a fresh Codex thread if the current
thread gets heavy.

## Objective

Continue toward the full 350-entry goal. Wave 005 is the fifth 60-entry
checkpoint, not the final success condition.

Full goal:

> Regenerate all 350 ponchi images as meaningful 2:1 illustrations, and apply
> official logos or official icons only after official source review and
> deterministic post-compositing. Keep progress and audits numerically visible.

## Current workspace

- Repository: `D:\dev\VibeCodingDictionary`
- Main overview: `docs/ponchi_progress_overview.md`
- Wave audit: `docs/ponchi_wave_005_audit.md`
- Batch 013 summary: `docs/ponchi_batch_013_progress_summary.md`
- Batch 014 summary: `docs/ponchi_batch_014_progress_summary.md`
- Batch 015 summary: `docs/ponchi_batch_015_progress_summary.md`
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

- Batch 013 has 20/20 prompt briefs generated:
  `assets/ponchi/pipeline_prompts/ponchi-batch-013/`.
- Batch 013 prompt lint passes.
- Batch 013 has 20/20 generated base images.
- G-22 - H-1 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-013/` and passed base audit.
- Batch 013 contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-013-base-contact-sheet.png`.
- Batch 013 is 20 `logo_avoid` entries and requires no official overlays.
- Batch 014 has 20/20 prompt briefs generated:
  `assets/ponchi/pipeline_prompts/ponchi-batch-014/`.
- Batch 014 prompt lint passes.
- Batch 014 has 20/20 generated base images.
- H-2 - H-62 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-014/` and passed base audit.
- Batch 014 contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-014-base-contact-sheet.png`.
- Batch 014 is 20 `logo_avoid` entries and requires no official overlays.
- Batch 015 has 20/20 prompt briefs generated:
  `assets/ponchi/pipeline_prompts/ponchi-batch-015/`.
- Batch 015 prompt lint passes.
- Batch 015 has 20/20 generated base images.
- H-63 - I-81 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-015/` and passed base audit.
- Batch 015 contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-015-base-contact-sheet.png`.
- Batch 015 is 20 `logo_avoid` entries and requires no official overlays.
- Wave 005 base generation is complete: 60/60 generated 2:1 bases and 60/60
  base audit pass.
- Total numerically tracked generated bases are now 260/350.

## Next best actions

1. Continue Wave 006 / Batch 016:
   - Inspect `ledgers/ponchi_generation_batches.csv` for `ponchi-batch-016`.
   - Classify logo needs before generation.
   - Add scaffold overrides where the entry text is too abstract or brand-risky.
   - Scaffold prompts and run prompt lint.

2. Generate and audit Batch 016:
   - Generate `1254x627` 2:1 bases.
   - Keep clearspace only for official-overlay entries.
   - Run `scripts\ponchi_image_audit.py` with the bundled Python runtime.
   - Run `python scripts\ponchi_batch_audit.py ponchi-batch-016`.
   - Run `python scripts\ponchi_batch_report.py ponchi-batch-016`.
   - Run `python scripts\ponchi_pipeline_dashboard.py`.

3. Continue official source review:
   - Batch 008 overlay_wait: F-10 - F-17, F-20, F-21, F-30, F-34 - F-36.
   - Batch 009 overlay_wait: F-37, F-38, F-40, F-41, F-44, F-50, F-61, F-62.
   - Batch 010 overlay_wait: F-80, F-82 - F-86, F-90, F-110, F-120 - F-122.
   - Batch 011 overlay_wait: F-140, F-141, F-153, F-170 - F-172, F-180,
     F-181, F-200.
   - Record source decisions in `docs/brand_usage_audit.md`.
   - Overlay only official local assets after source review/import.
   - Keep unresolved sources in `overlay_wait`.
