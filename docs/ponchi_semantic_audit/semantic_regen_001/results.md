# semantic-regen-001 Results

作成日: 2026-06-05

## Summary

Run 001 の P0 高確信誤認 9 件を再生成し、機械監査、公式 overlay、ブラインド再テストを実施した。

結論:

- P0 対象 9 件は全て top1 正解。
- P0 対象 9 件は全て confidence >= 70。
- 旧 P0 の高確信誤答は解消。
- `D-53 Veo` は v1/v2/v3 で不合格だったため v4 まで作り直し、v4 で合格。
- `D-70 Amical` は画像としては合格。ただし本文はまだ医療 AI ソリューション記述で、ブランド監査側の local-first dictation / note-taking app と不一致。final 昇格前に本文 reconciliation が必要。

## Files

- Plan: `docs/ponchi_semantic_audit/semantic_regen_retest_plan_2026-06-05.md`
- Scope ledger: `ledgers/ponchi_semantic_regen_scope_2026-06-05.csv`
- Prompt brief: `assets/ponchi/pipeline_prompts/semantic-regen-001/semantic-regen-001.md`
- Batch review: `ledgers/ponchi_batches/semantic-regen-001.md`
- Batch audit: `docs/ponchi_batch_audits/semantic-regen-001.md`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-001/`
- Final candidates audit: `docs/ponchi_batch_audits/semantic-regen-001-final-candidates.md`

## Mechanical Audit

Base images:

- size/density/clearspace: 9 / 9 pass
- color: 9 / 9 pass

Overlay images:

- Official overlays were added deterministically.
- Overlay image clearspace audit is expected to report `review` because official assets occupy the reserved region.
- Overlay color audit includes official asset colors and is not used as the body-palette gate. Body palette gate is the base color audit.

Relevant files:

- `ledgers/semantic_regen_001_base_audit.csv`
- `ledgers/semantic_regen_001_color_audit.csv`
- `ledgers/semantic_regen_001_overlay_audit.csv`
- `ledgers/semantic_regen_001_overlay_color_audit.csv`

## Blind Retest

### B Retest

Files:

- Sheet: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/B/blind_retest_B_sheet.png`
- Responses: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/B/agent_schrodinger_responses.csv`
- Scored: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/B/agent_schrodinger_scored.csv`
- Summary: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/B/agent_schrodinger_score_summary.md`

Result:

- total: 16
- top1: 16 / 16
- top3: 16 / 16
- P0 regen targets: 5 / 5 top1 correct

### D Retest

Files:

- Sheet: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/D/blind_retest_D_sheet.png`
- Responses: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/D/agent_ramanujan_responses.csv`
- Scored: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/D/agent_ramanujan_scored.csv`
- Summary: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/D/agent_ramanujan_score_summary.md`

Initial D result:

- `D-22`, `D-58`, `D-70`: pass
- `D-53`: failed as `D-56 Seedance` with confidence 80

Focused D-53 attempts:

- v2 failed as `D-57 Flow` with confidence 88.
- v3 failed as `D-56 Seedance` with confidence 62.
- v4 passed as `D-53 Veo` with confidence 86.

Focused v4 files:

- Sheet: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/D53_v4/blind_retest_D53_v4_sheet.png`
- Responses: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/D53_v4/agent_herschel_responses.csv`
- Scored: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/D53_v4/agent_herschel_scored.csv`
- Summary: `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest/D53_v4/agent_herschel_score_summary.md`

## P0 Pass Table

| entry | title | old wrong top1 | new top1 | confidence | decision | note |
| --- | --- | --- | --- | ---: | --- | --- |
| `B-26` | Azure OpenAI | `B-27` Vertex AI | `B-26` | 72 | pass | Azure managed/security architecture recovered the intended meaning |
| `B-31` | Excalidraw | `B-6` Windsurf | `B-31` | 98 | pass | hand-drawn board and rough diagram cues are clear |
| `B-5` | GitHub Copilot | `B-4` Cursor | `B-5` | 99 | pass | repo/PR/completion workflow differentiates from AI IDE |
| `B-52` | Gemini の料金プラン | `B-1` Gemini | `B-52` | 96 | pass | plan ladder and usage meters make pricing explicit |
| `B-6` | Windsurf | `B-4` Cursor | `B-6` | 99 | pass | project-wide cascade plus official wordmark differentiates from Cursor |
| `D-22` | o1 系 | `D-71` Whisper | `D-22` | 78 | pass | reasoning staircase removed audio miscue |
| `D-53` | Veo | `D-51` Imagen | `D-53` | 86 | pass | v4 uses synchronized video+audio and foundation-model structure |
| `D-58` | Whisk | `D-57` Flow | `D-58` | 88 | pass | image-mixing funnel differentiates from video workflow |
| `D-70` | Amical | `D-58` Whisk | `D-70` | 72 | pass_with_content_caveat | image matches brand audit scope, but entry text needs reconciliation |

## Remaining Risks

- `D-53 Veo` required multiple iterations. It is now identifiable, but the whole video-generation cluster still needs a future cluster-level pass.
- Focused D-53 v4 retest still showed non-target confusion among `D-51 Imagen` and `D-57 Flow`; this is outside this P0 fix but should be added to the next semantic queue.
- `D-70 Amical` must not be promoted to final without resolving the mismatch between `content/entries/model/D-70_amical[人書].md` and `docs/brand_usage_audit.md`.

## Promotion Recommendation

Promote candidates to `assets/ponchi/final/` only after user visual approval.

Ready for promotion after approval:

- `B-26`
- `B-31`
- `B-5`
- `B-52`
- `B-6`
- `D-22`
- `D-53`
- `D-58`

Hold until content reconciliation:

- `D-70`
