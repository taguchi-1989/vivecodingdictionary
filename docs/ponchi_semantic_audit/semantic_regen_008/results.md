# semantic-regen-008 results

Date: 2026-06-06

Cluster: `B-coding-assistants`
Pass mode: `exact_entry`

## Scope

| entry | title | action | result |
| --- | --- | --- | --- |
| `B-4` | Cursor | recompose | staged candidate uses editor-first UI: file tree, inline edit, chat side panel, preview/test area |
| `B-5` | GitHub Copilot | keep | existing semantic-regen-001 candidate already shows GitHub/repo/PR/completion flow |
| `B-6` | Windsurf | keep | existing semantic-regen-001 candidate already shows agentic cascade across files/tests/browser |
| `B-7` | Claude Code | recompose | staged candidate uses terminal-first CLI command/edit/test loop |
| `B-8` | Codex | hold | existing candidate remains understandable but should be retested in broader assistant core cluster |
| `D-35` | Cursor Composer | hold | existing semantic-regen-004 candidate remains the Cursor multi-file composer contrast case |

## Distinction Check

- `B-4` should read as Cursor because the main surface is an AI editor with inline code edits and a side chat panel.
- `B-7` should read as Claude Code because the main surface is a local terminal/CLI loop with command execution, patch/diff, and tests.
- `D-35` remains distinguishable from `B-4` because it is a composer-style multi-file plan/diff/apply flow rather than a single-project editor surface.
- `B-5` and `B-6` remain held because their regenerated candidates already show GitHub Copilot and Windsurf-specific workflows.

## Files

- Batch images: `assets/ponchi/experiments/batches/semantic-regen-008/`
- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-008/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-008/`
- Cluster review pack: `docs/ponchi_semantic_audit/coding_assistants_cluster_2026-06-06/`
- Batch ledger: `ledgers/ponchi_generation_batches.csv`
- Base audit: `docs/ponchi_semantic_audit/semantic_regen_008/base_image_audit.md`
- Overlay audit: `docs/ponchi_semantic_audit/semantic_regen_008/overlay_image_audit.md`
- Color audits: `docs/ponchi_semantic_audit/semantic_regen_008/color_audit.md` and `docs/ponchi_semantic_audit/semantic_regen_008/overlay_color_audit.md`

## Judgment

`B-4` and `B-7` are staged as review-pending final candidates. Mechanical audit passed:

- Base image audit: 2/2 pass, bbox 0.522 and 0.621, clearspace ink 0.0000.
- Base color audit: 2/2 pass.
- Overlay image audit: 2/2 pass, clearspace ink 0.0735 and 0.0684 with official logos.
- Overlay color audit: 2/2 pass.

The updated title-hidden sheet keeps the primary confusers adjacent: `B-4` vs `D-35`, and `B-7` vs `B-8`.
