# Ponchi Wave 001 handoff

Use this file to continue Wave 001 in a fresh Codex thread if the current thread
gets heavy.

## Objective

Continue toward the full 350-entry goal. Do not redefine success around Wave
001. Wave 001 is only the first 60-entry checkpoint.

Full goal:

> Regenerate all 350 ponchi images as meaningful 2:1 illustrations, and apply
> official logos or official icons only after official source review and
> deterministic post-compositing. Keep progress and audits numerically visible.

## Current workspace

- Repository: `D:\dev\VibeCodingDictionary`
- Main overview: `docs/ponchi_progress_overview.md`
- Wave audit: `docs/ponchi_wave_001_audit.md`
- Batch 002 detailed summary: `docs/ponchi_batch_002_progress_summary.md`
- Brand audit: `docs/brand_usage_audit.md`
- Pipeline ledger: `ledgers/ponchi_generation_batches.csv`

## Non-negotiable rules

- Do not write to `assets/ponchi/final/` without explicit user confirmation.
- Do not revert unrelated dirty worktree changes.
- Do not use third-party logo downloads when official sources are unclear.
- Do not generate fake logos, app icons, product UI, mascots, or brand-style
  substitutes.
- Generate base images with clean white clearspace for future official overlays.
- Keep final candidates under `assets/ponchi/final_candidates/`.

## Current known state

- Batch 002 has 20/20 2:1 base images.
- Batch 002 has 8 accepted final candidates:
  B-11, B-12, B-13, B-20, B-21, B-22, B-28, B-29.
- Batch 002 still has 12 `overlay_wait` items.
- Batch 003 has 20/20 prompt briefs generated through the new batch-002
  best-practice pipeline:
  `assets/ponchi/pipeline_prompts/ponchi-batch-003/`.
- Batch 003 prompt lint passes.
- Batch 003 has 20/20 generated base images.
- B-30 - C-9 base images are saved under
  `assets/ponchi/experiments/batches/ponchi-batch-003/` and passed base audit.
- Batch 003 base contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-003-base-contact-sheet.png`.
- Batch 003 has 2 review-pending overlay candidates:
  C-1 OpenAI and C-2 Anthropic under
  `assets/ponchi/final_candidates/ponchi-batch-003/`.
- Batch 003 ledger state is 18 `overlay_wait` and 2 `overlay_ready`:
  C-1 OpenAI and C-2 Anthropic are logo-source ready; all other Batch 003
  entries are waiting for official source review/import.

## Next best actions

1. B-continuation path:
   - Continue official source review for Batch 002 remaining 14 items.
   - Record every source decision in `docs/brand_usage_audit.md`.
   - Overlay only official local assets.
   - Re-run batch audit, dashboard, and final candidate staging after each
     accepted overlay.

2. All-chapters-forward path:
   - Continue Batch 003, then continue through all remaining batches in ledger
     order using `docs/ponchi_agent_all_chapters_handoff.md`.
   - Review C-1 OpenAI and C-2 Anthropic overlay candidates.
   - Continue official source review/import for the remaining Batch 003
     `overlay_wait` entries.
   - Audit overlay placement, fake logos, fake text, and 2:1 dimensions.
   - Stage only accepted base/logo candidates outside final.

3. Integration path:
   - Keep `docs/ponchi_progress_overview.md` current.
   - Keep wave audit counts current.
   - At 60 completed/audited entries, write final Wave 001 handoff and decide
     whether to continue in a new thread.
