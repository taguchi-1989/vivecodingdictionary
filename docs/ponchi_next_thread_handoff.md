# Ponchi next thread handoff

This is the quick restart note for the next Codex thread.

## State at handoff

- Working branch: `main`.
- Previous checkpoint commit before this handoff merge: `173903b`.
- Current tracked 2:1 base progress: 200 / 350.
- Wave 004 is complete: 60 / 60 generated bases, 60 / 60 base audit pass.
- Latest completed batch: `ponchi-batch-012`.
- Next generation target: Wave 005 / `ponchi-batch-013`.

## Files to read first

- `docs/ponchi_progress_overview.md`
- `docs/ponchi_wave_004_handoff.md`
- `docs/ponchi_wave_004_audit.md`
- `docs/brand_usage_audit.md`
- `ledgers/ponchi_generation_batches.csv`

## Current stage counts

| stage | count |
| --- | ---: |
| `brief_needed` | 207 |
| `overlay_wait` | 112 |
| `overlay_audit` | 14 |
| `overlay_ready` | 12 |
| `prompt_review` | 4 |
| `blocked_brand_asset` | 1 |

## Restart plan

1. Continue `ponchi-batch-013`.
2. Keep Batch 012 best practices:
   - use abstract non-brand metaphors for `logo_avoid`;
   - keep white clearspace only where an official overlay is required;
   - never ask image generation to invent logos, product UI, icons, or brand marks.
3. Generate Batch 013 as `1254x627` 2:1 bases.
4. Run image audit, batch audit, batch report, and dashboard refresh.
5. Stop for a commit/handoff checkpoint whenever the visible成果物 count grows past the next heavy threshold.

## Handoff merge contents

The handoff merge commit should include:

- pending `assets/ponchi/final/*.webp` changes, because the user requested all current changes to be merged for transfer;
- meaningful newly imported official logo assets still visible in `git status`;
- `.gitignore` cleanup for ZIP metadata and temporary logo download files;
- this restart note.

Ignored local clutter such as `__MACOSX`, `.DS_Store`, AppleDouble `._*`, the
Anthropic temporary response blob, and non-logo Anthropic leadership media is
not part of the handoff commit.
