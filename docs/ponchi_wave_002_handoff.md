# Ponchi Wave 002 handoff

Use this file to continue Wave 002 in a fresh Codex thread if the current
thread gets heavy.

## Objective

Continue toward the full 350-entry goal. Wave 002 is the second 60-entry
checkpoint, not the final success condition.

Full goal:

> Regenerate all 350 ponchi images as meaningful 2:1 illustrations, and apply
> official logos or official icons only after official source review and
> deterministic post-compositing. Keep progress and audits numerically visible.

## Current workspace

- Repository: `D:\dev\VibeCodingDictionary`
- Main overview: `docs/ponchi_progress_overview.md`
- Wave audit: `docs/ponchi_wave_002_audit.md`
- Batch 004 summary: `docs/ponchi_batch_004_progress_summary.md`
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

- Batch 004 has 20/20 prompt briefs generated:
  `assets/ponchi/pipeline_prompts/ponchi-batch-004/`.
- Batch 004 prompt lint passes.
- Batch 004 has 20/20 generated base images.
- C-10 - C-14, C-50 - C-60, and C-80 - C-83 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-004/` and passed base audit.
- Batch 004 contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-004-base-contact-sheet.png`.
- Batch 004 ledger state is 9 `overlay_wait` and 11 `prompt_review`.
- `overlay_wait`: C-10 - C-14 and C-80 - C-83.
- `prompt_review` / `logo_avoid`: C-50 - C-60.
- Batch 005 has 20/20 prompt briefs generated:
  `assets/ponchi/pipeline_prompts/ponchi-batch-005/`.
- Batch 005 prompt lint passes.
- Batch 005 has 20/20 generated base images.
- D-1 - D-41 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-005/` and passed base audit.
- Batch 005 contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-005-base-contact-sheet.png`.
- Batch 005 ledger state is 7 `overlay_ready` and 13 `overlay_wait`.
- Batch 005 summary:
  `docs/ponchi_batch_005_progress_summary.md`.
- Batch 006 has 20/20 prompt briefs generated:
  `assets/ponchi/pipeline_prompts/ponchi-batch-006/`.
- Batch 006 prompt lint passes.
- Batch 006 has 20/20 generated base images.
- D-42 - D-71 and E-1 - E-2 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-006/` and passed base audit.
- Batch 006 contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-006-base-contact-sheet.png`.
- Batch 006 ledger state is 3 `overlay_ready`, 15 `overlay_wait`, and
  2 `brief_needed` entries with `logo_avoid` prompts/bases complete.
- Batch 006 summary:
  `docs/ponchi_batch_006_progress_summary.md`.
- Wave 002 base generation is complete: 60/60 generated 2:1 bases and 60/60
  base audit pass.

## Next best actions

1. Continue Wave 003 base generation:
   - Start `ponchi-batch-007`.
   - Scaffold and lint prompts.
   - Generate `1254x627` base images with clearspace only for entries that need
     official overlays.
   - Do not synthesize provider logos, model logos, app icons, brand colors,
     product UI, or readable text.

2. Continue official source review:
   - Record source decisions in `docs/brand_usage_audit.md`.
   - Overlay only official local assets after source review/import.
   - Keep unresolved sources in `overlay_wait`.

3. Audit after each batch:
   - Run `scripts\ponchi_image_audit.py` with the bundled Python runtime.
   - Run `python scripts\ponchi_batch_audit.py <batch-id>`.
   - Run `python scripts\ponchi_batch_report.py <batch-id>`.
   - Run `python scripts\ponchi_pipeline_dashboard.py`.
