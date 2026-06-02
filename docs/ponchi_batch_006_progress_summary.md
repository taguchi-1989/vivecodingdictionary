# ponchi-batch-006 progress summary

対象: `D-42` から `E-2` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| prompt 作成済み | 20 / 20 | D-42 - E-2 全件 |
| prompt lint pass | 20 / 20 | D-42 - E-2 全件 |
| 2:1 base 作成済み | 20 / 20 | D-42 - E-2 全件 |
| 2:1 base audit pass | 20 / 20 | D-42 - E-2 全件 |
| 公式ロゴ/公式アイコン要確認 | 18 / 20 | D-42 - D-71 |
| overlay_ready | 3 / 20 | D-50, D-52, D-71 |
| overlay_wait | 15 / 20 | D-42 - D-47, D-51, D-53 - D-58, D-60, D-70 |
| logo_avoid | 2 / 20 | E-1, E-2 |
| final candidate 化済み | 0 / 20 | 未生成 |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | official logo source | current status |
| --- | --- | --- | --- | --- | --- |
| D-42 | Gemma 系 | done | pass | waiting | overlay_wait |
| D-43 | Qwen 系 | done | pass | waiting | overlay_wait |
| D-44 | Kimi | done | pass | waiting | overlay_wait |
| D-45 | GLM | done | pass | waiting | overlay_wait |
| D-46 | DeepSeek V3 | done | pass | waiting | overlay_wait |
| D-47 | DeepSeek R1 | done | pass | waiting | overlay_wait |
| D-50 | DALL-E | done | pass | local OpenAI wordmark | overlay_ready |
| D-51 | Imagen | done | pass | waiting | overlay_wait |
| D-52 | Sora | done | pass | local OpenAI wordmark | overlay_ready |
| D-53 | Veo | done | pass | waiting | overlay_wait |
| D-54 | Stable Diffusion | done | pass | waiting | overlay_wait |
| D-55 | Nano Banana | done | pass | waiting | overlay_wait |
| D-56 | Seedance | done | pass | waiting | overlay_wait |
| D-57 | Flow | done | pass | waiting | overlay_wait |
| D-58 | Whisk | done | pass | waiting | overlay_wait |
| D-60 | AlphaGo | done | pass | waiting | overlay_wait |
| D-70 | Amical | done | pass | waiting | overlay_wait |
| D-71 | Whisper | done | pass | local OpenAI wordmark | overlay_ready |
| E-1 | SWE-Bench | done | pass | logo_avoid | brief exists; no overlay |
| E-2 | SWE-Bench Verified | done | pass | logo_avoid | brief exists; no overlay |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-006/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-006/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-006-base-image-audit.md`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-006-base-contact-sheet.png`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-006.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-006.md`

## Visual QA

Contact sheet review passed for the generated bases. D-58 was regenerated to
remove animal-like visual references, and E-1/E-2 were regenerated to avoid
red/green pass/fail color semantics.

## Next action

Batch 006 base generation is complete. Wave 002 now has 60 / 60 generated
2:1 bases and 60 / 60 base audit pass. Continue with official source review
and deterministic overlays for `overlay_ready` / `overlay_wait` entries, or
start Wave 003 / Batch 007 for the next 60-entry base generation wave. Do not
promote anything to `assets/ponchi/final/` without explicit approval.
