# ponchi-batch-003 progress summary

対象: `B-30` から `C-9` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| prompt 作成済み | 20 / 20 | B-30 - C-9 全件 |
| prompt lint pass | 20 / 20 | B-30 - C-9 全件 |
| 2:1 base 作成済み | 20 / 20 | B-30 - C-9 全件 |
| 2:1 base audit pass | 20 / 20 | B-30 - C-9 全件 |
| 公式ロゴ/公式アイコン要確認 | 19 / 20 | B-30 - C-7, C-9 |
| 公式ロゴなし確認済み | 1 / 20 | C-8 |
| official overlay ready | 0 / 20 | overlay_ready は C-1/C-2 の後合成完了により解消 |
| overlay_audit | 19 / 20 | B-30, B-31, B-32, B-33, B-40, B-41, B-50, B-51, B-52, B-60, B-61, C-1, C-2, C-3, C-4, C-5, C-6, C-7, C-9 |
| overlay_wait | 0 / 20 | none |
| final candidate 化済み | 20 / 20 | B-30 - C-9 全件 |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | official logo source | logo overlay | current status |
| --- | --- | --- | --- | --- | --- | --- |
| B-30 | Amazon Bedrock | done | pass | applied | review_pending | overlay_audit |
| B-31 | Excalidraw | done | pass | applied | review_pending | overlay_audit |
| B-32 | Figma | done | pass | applied | review_pending | overlay_audit |
| B-33 | Canva | done | pass | applied | review_pending | overlay_audit |
| B-40 | Reddit | done | pass | applied | review_pending | overlay_audit |
| B-41 | arXiv | done | pass | applied | review_pending | overlay_audit |
| B-50 | Claude の料金プラン | done | pass | applied | review_pending | overlay_audit |
| B-51 | ChatGPT の料金プラン | done | pass | official OpenAI wordmark applied | review_pending | overlay_audit |
| B-52 | Gemini の料金プラン | done | pass | applied | review_pending | overlay_audit |
| B-60 | Suno | done | pass | applied | review_pending | overlay_audit |
| B-61 | ACE-Step 1.5 | done | pass | official ACE-Step repo logo applied | review_pending | overlay_audit |
| C-1 | OpenAI | done | pass | local official asset applied | review_pending | overlay_audit |
| C-2 | Anthropic | done | pass | local official asset applied | review_pending | overlay_audit |
| C-3 | Google DeepMind | done | pass | applied | review_pending | overlay_audit |
| C-4 | Meta AI | done | pass | applied | review_pending | overlay_audit |
| C-5 | xAI | done | pass | applied | review_pending | overlay_audit |
| C-6 | Mistral AI | done | pass | applied | review_pending | overlay_audit |
| C-7 | Hugging Face | done | pass | applied | review_pending | overlay_audit |
| C-8 | Microsoft AI | done | pass | confirmed no dedicated image logo/lockup | logo_avoid | color_audit |
| C-9 | NVIDIA | done | pass | applied | review_pending | overlay_audit |

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

Review the 19 overlay candidates and the C-8 logo-less base candidate before
any final promotion. C-8 Microsoft AI is staged as a confirmed logo-less
candidate because the official Microsoft AI page confirms the page/title and
text brand link but no dedicated Microsoft AI image logo or lockup. Do not
promote to `assets/ponchi/final/` until candidates are visually reviewed and
explicitly approved.
