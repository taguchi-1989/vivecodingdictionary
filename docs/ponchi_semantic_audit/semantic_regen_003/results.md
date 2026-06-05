# semantic-regen-003 results

Wave 3 regenerated five B-chapter semantic failures:

- `B-1` Gemini
- `B-2` Claude
- `B-3` ChatGPT
- `B-10` Devin
- `B-14` Genspark

## Gate Summary

| entry | final candidate | mechanical body color | blind result | decision |
| --- | --- | --- | --- | --- |
| `B-1` Gemini | `assets/ponchi/final_candidates/semantic-regen-003/B-1_candidate.png` | pass | body focus top1 `B-1`, confidence 96 | pass |
| `B-2` Claude | `assets/ponchi/final_candidates/semantic-regen-003/B-2_candidate.png` | pass | body focus top1 `B-2`, confidence 88 | pass |
| `B-3` ChatGPT | `assets/ponchi/final_candidates/semantic-regen-003/B-3_candidate.png` | pass | body focus top1 `B-3`, confidence 74 | pass |
| `B-10` Devin | `assets/ponchi/final_candidates/semantic-regen-003/B-10_candidate.png` | pass | focus v6 top1 `B-10`, confidence 88 | pass |
| `B-14` Genspark | `assets/ponchi/final_candidates/semantic-regen-003/B-14_candidate.png` | pass | body focus top1 `B-14`, confidence 82 | pass |

## Iteration Notes

- `B-2` first improved overlay was correct with the official logo, but body-only testing still read as search/Perplexity. v3 removed search/citation cues and centered long-document reasoning plus artifact outputs. It passed the focused body test at `88`.
- `B-10` required several iterations. Earlier versions were confused with Cursor, Codex, or Claude Code because the scene looked like broad coding-agent orchestration. v6 reduced misleading icon cues and emphasized human issue handoff, repo/file edits, tests, and completed review handoff. It passed the coding-agent focus test at `88`.
- `B-14` first body was read as Perplexity. v2 shifted the image to multi-agent research lanes, a Sparkpage/report canvas, and slide/task output branches. It passed the focused body test at `82`.
- `B-1` and `B-3` passed without additional post-blind regeneration in this wave, though both remain logo-assisted in the normal overlay setting.
- During generation, `image_gen` rate limits occurred. No Pillow-generated fallback image was accepted as an official candidate; all final candidates are based on `image_gen` outputs. Local image processing was used only for normalized sizing, logo clearspace cleanup, small symbol cleanup, contact sheets, and official logo compositing.

## Mechanical Audit

Base images:

- size/density/clearspace: 4 / 5 pass, `B-14` review on bbox density only (`0.496` vs threshold `0.50`)
- color: 5 / 5 pass

Overlay images:

- Official logo overlays were added deterministically.
- Overlay clearspace audit reports `review` for official logos occupying the reserved region; this is expected.
- Overlay color audit is not the body-palette gate because official logo colors can be outside the ponchi body palette. Current overlay color audit is 4 / 5 pass, 1 review (`B-1` official Gemini colors).

## Blind Retest Evidence

Primary focused passes:

- `B-2` / `B-14` assistant-service focus: `docs/ponchi_semantic_audit/semantic_regen_003/blind_retest/B_body_focus_v4/agent_nietzsche_score_summary.md`
- `B-10` coding-agent focus: `docs/ponchi_semantic_audit/semantic_regen_003/blind_retest/B_focus_v6/agent_zeno_score_summary.md`

Earlier diagnostic tests are retained for audit history:

- mixed B retest v2: `docs/ponchi_semantic_audit/semantic_regen_003/blind_retest/B_v2/agent_bacon_score_summary.md`
- body-only v2: `docs/ponchi_semantic_audit/semantic_regen_003/blind_retest/B_body_v2/agent_mencius_score_summary.md`
- coding-agent focus v3-v5: `docs/ponchi_semantic_audit/semantic_regen_003/blind_retest/B_focus_v3/`, `B_focus_v4/`, `B_focus_v5/`

## Artifacts

- Prompt brief: `assets/ponchi/pipeline_prompts/semantic-regen-003/semantic-regen-003.md`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-003/`
- Final candidates contact sheet: `assets/ponchi/final_candidates/semantic-regen-003/final_candidates_contact_sheet.png`
- Batch audit: `docs/ponchi_batch_audits/semantic-regen-003.md`
- Final candidate audit: `docs/ponchi_batch_audits/semantic-regen-003-final-candidates.md`
- Base image audit: `docs/ponchi_semantic_audit/semantic_regen_003/base_image_audit.md`
- Base color audit: `docs/ponchi_semantic_audit/semantic_regen_003/color_audit.md`
- Overlay image audit: `docs/ponchi_semantic_audit/semantic_regen_003/overlay_image_audit.md`
- Overlay color audit: `docs/ponchi_semantic_audit/semantic_regen_003/overlay_color_audit.md`

## Residual Review Notes

- `B-14` is mechanically `review` on bbox density by a narrow margin. It passed semantic focus testing and color audit; visual approval should confirm whether the lower density is acceptable.
- `B-1` includes a generated sparkle-like central hub plus official Gemini overlay. It passed focus testing, but user visual review should decide whether the generated hub mark feels too logo-like.
- Final candidates remain staged only. They do not overwrite `assets/ponchi/final/`.

## Promotion Recommendation

Promote the following only after user visual approval:

- `B-1`
- `B-2`
- `B-3`
- `B-10`
- `B-14`
