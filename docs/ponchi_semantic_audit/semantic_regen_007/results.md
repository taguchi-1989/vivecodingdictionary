# semantic-regen-007 results

Date: 2026-06-06

Cluster: `B-ms-copilot`
Pass mode: `exact_entry`

## Scope

| entry | title | action | result |
| --- | --- | --- | --- |
| `B-15` | Microsoft Copilot | recompose | staged candidate uses personal chat/search/Windows-style everyday task flow |
| `B-16` | Microsoft 365 Copilot | recompose | staged candidate uses work graph, documents, mail, calendar, meetings, and task flow |
| `B-17` | Edge Copilot | hold | existing candidate keeps stronger browser frame/sidebar distinction |

## Distinction Check

- `B-15` should read as general Microsoft Copilot: user question, search/help cards, Windows-style app/task assistance, and everyday non-Office tasks.
- `B-16` should read as Microsoft 365 Copilot: work graph from document/mail/calendar/meeting inputs into productivity outputs.
- `B-17` remains visually separated by browser page plus side panel; no new generation was needed in this unit.

## Files

- Batch images: `assets/ponchi/experiments/batches/semantic-regen-007/`
- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-007/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-007/`
- Batch ledger: `ledgers/ponchi_generation_batches.csv`
- Base audit: `docs/ponchi_semantic_audit/semantic_regen_007/base_image_audit.md`
- Overlay audit: `docs/ponchi_semantic_audit/semantic_regen_007/overlay_image_audit.md`
- Color audits: `docs/ponchi_semantic_audit/semantic_regen_007/color_audit.md` and `docs/ponchi_semantic_audit/semantic_regen_007/overlay_color_audit.md`

## Judgment

`B-15` and `B-16` are staged as review-pending final candidates. Mechanical audit passed:

- Base image audit: 2/2 pass, clearspace ink 0.0000.
- Base color audit: 2/2 pass.
- Overlay image audit: 2/2 pass, clearspace ink 0.0600 with official icon.
- Overlay color audit: 2/2 pass.

They should be tested in a title-hidden `B-ms-copilot` sheet against `B-17`, then folded into the broader `B-ai-assistants-core` review after U003.
