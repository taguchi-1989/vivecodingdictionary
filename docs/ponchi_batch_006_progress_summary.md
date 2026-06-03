# ponchi-batch-006 progress summary

対象: `D-42` から `E-2` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| prompt 作成済み | 20 / 20 | D-42 - E-2 全件 |
| prompt lint pass | 20 / 20 | D-42 - E-2 全件 |
| 2:1 base 作成済み | 20 / 20 | D-42 - E-2 全件 |
| 2:1 base audit pass | 20 / 20 | D-42 - E-2 全件 |
| 公式ロゴ/公式アイコン要確認 | 0 / 20 | none |
| overlay_audit | 17 / 20 | D-42, D-43, D-44, D-45, D-46, D-47, D-50, D-51, D-52, D-53, D-54, D-55, D-57, D-58, D-60, D-70, D-71 |
| overlay_wait | 0 / 20 | none |
| logo_avoid | 3 / 20 | D-56, E-1, E-2 |
| final candidate 化済み | 20 / 20 | D-42, D-43, D-44, D-45, D-46, D-47, D-50, D-51, D-52, D-53, D-54, D-55, D-56, D-57, D-58, D-60, D-70, D-71, E-1, E-2 |
| color audit pass | 20 / 20 staged candidates | D-42, D-43, D-44, D-45, D-46, D-47, D-50, D-51, D-52, D-53, D-54, D-55, D-56, D-57, D-58, D-60, D-70, D-71, E-1, E-2 |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | official logo source | current status |
| --- | --- | --- | --- | --- | --- |
| D-42 | Gemma 系 | done | pass | official Google DeepMind icon applied | overlay_audit |
| D-43 | Qwen 系 | done | pass | official applied | overlay_audit |
| D-44 | Kimi | done | pass | official applied | overlay_audit |
| D-45 | GLM | done | pass | official Z.ai icon applied | overlay_audit |
| D-46 | DeepSeek V3 | done | pass | official applied | overlay_audit |
| D-47 | DeepSeek R1 | done | pass | official applied | overlay_audit |
| D-50 | DALL-E | done | pass | local OpenAI wordmark | overlay_audit |
| D-51 | Imagen | done | pass | official Google DeepMind icon applied | overlay_audit |
| D-52 | Sora | done | pass | local OpenAI wordmark | overlay_audit |
| D-53 | Veo | done | pass | official Google DeepMind icon applied | overlay_audit |
| D-54 | Stable Diffusion | done | pass | official Stability AI org logo applied | overlay_audit |
| D-55 | Nano Banana | done | pass | official Gemini sparkle applied | overlay_audit |
| D-56 | Seedance | done | pass | confirmed no distinct Seedance product logo; palette-normalized base candidate | color_audit |
| D-57 | Flow | done | pass | official Flow favicon applied | overlay_audit |
| D-58 | Whisk | done | pass | official Whisk favicon applied | overlay_audit |
| D-60 | AlphaGo | done | pass | official Google DeepMind icon applied | overlay_audit |
| D-70 | Amical | done | pass | official Amical app icon applied; entry/source mismatch remains review note | overlay_audit |
| D-71 | Whisper | done | pass | local OpenAI wordmark | overlay_audit |
| E-1 | SWE-Bench | done | pass | logo_avoid | brief exists; no overlay |
| E-2 | SWE-Bench Verified | done | pass | logo_avoid | brief exists; no overlay |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-006/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-006/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-006-base-image-audit.md`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-006-base-contact-sheet.png`
- Overlay audit: `docs/ponchi_batch_audits/ponchi-batch-006-overlay-image-audit.md`
- Final candidates: `assets/ponchi/final_candidates/ponchi-batch-006/`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-006.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-006.md`

## Visual QA

Contact sheet review passed for the generated bases. D-58 was regenerated to
remove animal-like visual references, and E-1/E-2 were regenerated to avoid
red/green pass/fail color semantics. D-51 Imagen and D-60 AlphaGo were rebuilt
as local strict-palette diagrams to remove photo/natural-color and orange
drift; both now pass base, overlay, and color audits. D-56 Seedance was also
palette-normalized after color audit review found off-palette body drift; it
now passes the mechanical color gate as a logo-less candidate.

## Next action

Batch 006 base generation is complete. D-42 Gemma, D-43 Qwen, D-44 Kimi,
D-45 GLM, D-46 DeepSeek V3, D-47 DeepSeek R1, D-50 DALL-E, D-51 Imagen, D-52 Sora,
D-53 Veo, D-54 Stable Diffusion, D-55 Nano Banana, D-57 Flow, D-58 Whisk, D-60 AlphaGo, D-70 Amical, and D-71 Whisper now have
deterministic official-logo overlays staged as review-pending final candidates.
Batch 006 now has 20 / 20 staged review-pending candidates. D-56 Seedance is a
confirmed logo-less candidate because the official Seedance page did not
confirm a distinct product logo or lockup. D-70 uses the official Amical
GitHub/website app icon, but the entry prose still describes a different
Korean/NHN medical AI solution, so reconcile that before final promotion. Do
not promote anything to
`assets/ponchi/final/` without explicit approval.
