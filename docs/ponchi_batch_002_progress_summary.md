# ponchi-batch-002 progress summary

対象: `B-10` から `B-29` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| 2:1 base 作成済み | 20 / 20 | B-10 - B-29 全件 |
| 公式ロゴ確認済み | 18 / 20 | B-10, B-11, B-12, B-13, B-14, B-15, B-16, B-17, B-18, B-20, B-21, B-22, B-24, B-25, B-26, B-27, B-28, B-29 |
| 公式ロゴなし確認済み | 2 / 20 | B-19, B-23 |
| ロゴ後合成済み | 18 / 20 | B-10, B-11, B-12, B-13, B-14, B-15, B-16, B-17, B-18, B-20, B-21, B-22, B-24, B-25, B-26, B-27, B-28, B-29 |
| final candidate 化済み | 20 / 20 | B-10 - B-29 全件 |
| overlay_wait 残り | 0 / 20 | none |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | 2:1 base | official logo source | logo overlay | final candidate | current status |
| --- | --- | --- | --- | --- | --- | --- |
| B-10 | Devin | done | done | done | review_pending | overlay_audit |
| B-11 | Bolt.new | done | done | done | review_pending | overlay_audit |
| B-12 | Perplexity | done | done | done | review_pending | overlay_audit |
| B-13 | ElevenLabs | done | done | done | review_pending | overlay_audit |
| B-14 | Genspark | done | done | done | review_pending | overlay_audit |
| B-15 | Microsoft Copilot | done | official Copilot icon applied | done | review_pending | overlay_audit |
| B-16 | Microsoft 365 Copilot | done | official Copilot-family icon applied; dedicated lockup not confirmed | done | review_pending | overlay_audit |
| B-17 | Edge Copilot | done | official Copilot-family icon applied; Edge-specific lockup not confirmed | done | review_pending | overlay_audit |
| B-18 | Aqua Voice | done | done | done | review_pending | overlay_audit |
| B-19 | Claude Cowork | done | confirmed no distinct product logo | logo_avoid | review_pending | color_audit |
| B-20 | Vercel | done | done | done | review_pending | overlay_audit |
| B-21 | Netlify | done | done | done | review_pending | overlay_audit |
| B-22 | Cloudflare | done | done | done | review_pending | overlay_audit |
| B-23 | AWS | done | confirmed no clean primary logo overlay path | logo_avoid | review_pending | color_audit |
| B-24 | Google Cloud | done | done | done | review_pending | overlay_audit |
| B-25 | Azure | done | done | done | review_pending | overlay_audit |
| B-26 | Azure OpenAI | done | done | done | review_pending | overlay_audit |
| B-27 | Vertex AI | done | done | done | review_pending | overlay_audit |
| B-28 | Render | done | done | done | review_pending | overlay_audit |
| B-29 | Supabase | done | done | done | review_pending | overlay_audit |

## Generated locations

- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-002/*_base_1254x627.png`
- Logo overlay images: `assets/ponchi/experiments/batches/ponchi-batch-002/*_overlay_1254x627.png`
- Final candidates: `assets/ponchi/final_candidates/ponchi-batch-002/`
- Candidate contact sheet: `assets/ponchi/final_candidates/ponchi-batch-002/final_candidates_contact_sheet.png`

## Latest note

B-15, B-16, and B-17 use the official Copilot icon extracted from the official
Copilot homepage `https://copilot.microsoft.com/`. B-16 and B-17 remain
review-pending because dedicated Microsoft 365 Copilot and Edge Copilot lockups
were not confirmed locally; do not treat the generic Copilot-family icon as
final approval.

B-19 Claude Cowork was moved to the confirmed logo-less lane after official
source review found Claude Team / Team plan language but no distinct
`Claude Cowork` product logo. The generated base is staged as a strict-palette
review-pending candidate; do not apply a generic Claude or Anthropic logo.

B-23 AWS was moved to the confirmed logo-less lane after official source review
found that AWS trademark guidance and the architecture-icons page do not provide
a clean primary AWS logo overlay path for this dictionary image. The generated
base is staged as a strict-palette review-pending candidate; do not apply the
AWS Smile Logo, architecture icons as a primary brand lockup, or third-party
logo mirrors.
