# Ponchi Wave 006 handoff

Use this file to continue after Wave 006 in a fresh Codex thread if the current
thread gets heavy.

## Objective

Continue toward the full 350-entry goal. Wave 006 closes the current ledger's
late J-chapter sweep, but it is not the final success condition because
`ponchi-batch-001` and `ponchi-batch-002` remain.

Full goal:

> Regenerate all 350 ponchi images as meaningful 2:1 illustrations, and apply
> official logos or official icons only after official source review and
> deterministic post-compositing. Keep progress and audits numerically visible.

## Current workspace

- Repository: `D:\dev\VibeCodingDictionary`
- Main overview: `docs/ponchi_progress_overview.md`
- Wave audit: `docs/ponchi_wave_006_audit.md`
- Batch 016 summary: `docs/ponchi_batch_016_progress_summary.md`
- Batch 017 summary: `docs/ponchi_batch_017_progress_summary.md`
- Batch 018 summary: `docs/ponchi_batch_018_progress_summary.md`
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

- Batch 016 has 20/20 prompt briefs, generated bases, and base audit pass.
- Batch 017 has 20/20 prompt briefs, generated bases, and base audit pass.
- Batch 018 has 10/10 prompt briefs, generated bases, and base audit pass.
- Wave 006 base generation is complete: 50/50 generated 2:1 bases and 50/50
  base audit pass.
- Total numerically tracked generated bases are now 310/350.
- Remaining tracked base work is `ponchi-batch-001` and `ponchi-batch-002`.

## Next best actions

1. Continue with `ponchi-batch-001`:
   - Inspect `ledgers/ponchi_generation_batches.csv` for `ponchi-batch-001`.
   - Classify A/B introductory entries as `logo_avoid` unless a concrete
     official logo requirement is justified.
   - Add scaffold overrides for entries that are too abstract.
   - Scaffold prompts, lint, generate bases, and audit.

2. Continue with `ponchi-batch-002`:
   - Re-check existing official logo/source status before using any overlay.
   - For entries where a source is unclear, keep `overlay_wait` or
     `blocked_brand_asset`.
   - Generate non-logo 2:1 bases first; overlay only official local assets after
     source review/import.

3. Refresh tracking:
   - Run `python scripts\ponchi_batch_audit.py <batch>`.
   - Run `python scripts\ponchi_batch_report.py <batch>`.
   - Run `python scripts\ponchi_pipeline_dashboard.py`.
   - Update `docs/ponchi_progress_overview.md` and this handoff note.
