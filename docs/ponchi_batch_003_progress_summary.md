# ponchi-batch-003 progress summary

対象: `B-30` から `C-9` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| prompt 作成済み | 20 / 20 | B-30 - C-9 全件 |
| prompt lint pass | 20 / 20 | B-30 - C-9 全件 |
| 2:1 base 作成済み | 20 / 20 | B-30 - C-9 全件 |
| 2:1 base audit pass | 20 / 20 | B-30 - C-9 全件 |
| 公式ロゴ/公式アイコン要確認 | 20 / 20 | B-30 - C-9 全件 |
| official overlay ready | 0 / 20 | overlay_ready は C-1/C-2 の後合成完了により解消 |
| overlay_audit | 2 / 20 | C-1 OpenAI, C-2 Anthropic |
| overlay_wait | 18 / 20 | B-30 - B-61, C-3 - C-9 |
| final candidate 化済み | 2 / 20 | C-1 OpenAI, C-2 Anthropic review_pending |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | official logo source | logo overlay | current status |
| --- | --- | --- | --- | --- | --- | --- |
| B-30 | Amazon Bedrock | done | pass | waiting | not yet | overlay_wait |
| B-31 | Excalidraw | done | pass | waiting | not yet | overlay_wait |
| B-32 | Figma | done | pass | waiting | not yet | overlay_wait |
| B-33 | Canva | done | pass | waiting | not yet | overlay_wait |
| B-40 | Reddit | done | pass | waiting | not yet | overlay_wait |
| B-41 | arXiv | done | pass | waiting | not yet | overlay_wait |
| B-50 | Claude の料金プラン | done | pass | source available, placement/use pending | not yet | overlay_wait |
| B-51 | ChatGPT の料金プラン | done | pass | waiting | not yet | overlay_wait |
| B-52 | Gemini の料金プラン | done | pass | waiting | not yet | overlay_wait |
| B-60 | Suno | done | pass | waiting | not yet | overlay_wait |
| B-61 | ACE-Step 1.5 | done | pass | waiting | not yet | overlay_wait |
| C-1 | OpenAI | done | pass | local official asset applied | review_pending | overlay_audit |
| C-2 | Anthropic | done | pass | local official asset applied | review_pending | overlay_audit |
| C-3 | Google DeepMind | done | pass | waiting | not yet | overlay_wait |
| C-4 | Meta AI | done | pass | waiting | not yet | overlay_wait |
| C-5 | xAI | done | pass | waiting | not yet | overlay_wait |
| C-6 | Mistral AI | done | pass | waiting | not yet | overlay_wait |
| C-7 | Hugging Face | done | pass | waiting | not yet | overlay_wait |
| C-8 | Microsoft AI | done | pass | waiting | not yet | overlay_wait |
| C-9 | NVIDIA | done | pass | waiting | not yet | overlay_wait |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-003/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-003/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-003-base-image-audit.md`
- Base contact sheet: `docs/ponchi_batch_audits/ponchi-batch-003-base-contact-sheet.png`
- Logo overlays: `assets/ponchi/experiments/batches/ponchi-batch-003/*_overlay_1254x627.png`
- Review candidates: `assets/ponchi/final_candidates/ponchi-batch-003/`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-003.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-003.md`

## Next action

Review C-1/C-2 overlay candidates, then continue official logo source review
and deterministic overlays for the remaining 18 `overlay_wait` entries. Do not
promote to `assets/ponchi/final/` until overlays are audited and explicitly
approved.
