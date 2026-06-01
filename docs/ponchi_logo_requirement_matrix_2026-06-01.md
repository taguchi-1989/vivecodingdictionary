# Ponchi Logo Requirement Matrix 2026-06-01

## 目的

ポンチ絵再生成で、ロゴを入れるべき項目と入れない項目を先に分ける。ロゴが必要でも、公式素材と利用条件が確認できていないものは後合成しない。AI 生成でロゴ風の図形やブランドカラーを作らせることも禁止する。

対象は、現在 `assets/ponchi/prompts/` にある再生成プロンプト 12 件。

## ステータス定義

| status | 意味 |
| :-- | :-- |
| `logo_avoid` | ロゴ不要。汎用アイコンだけで説明する |
| `base_2to1_ready_logo_blocked` | 元絵の 2:1 ベースは再生成済み。ロゴは公式素材・利用条件・ローカルパスが未確定のため未反映 |
| `official_logo_source_available_needs_import` | 公式ソースは確認済み。まだローカル素材化・利用条件記録・合成監査が未完了 |
| `official_logo_source_review_required` | 公式ガイドは確認済みだが、この項目に使うべき具体ロゴ、取得経路、または許諾条件の追加確認が必要 |
| `official_logo_available` | 公式素材がローカルにあり、後合成に進められる |
| `official_logo_applied` | 公式素材を後合成済み。本番画像または確認画像まで作成済み |

## 判定方針

ブランド名・製品名・モデル系列名そのものが見出しになっている項目は、本文だけで足りるとしてロゴを避けない。公式ロゴ、公式 lockup、公式アイコンのソースが確認できる場合は、2:1 ベース再生成後に公式素材を取得し、未改変で後合成する。

ただし、AI 生成でロゴ風の図形を描かせることは引き続き禁止する。公式ソースが未確認、利用条件が不明、または具体的なロゴ選定が未確定なら、合成は止めて `official_logo_source_review_required` または `base_2to1_ready_logo_blocked` に置く。

## マーキング

| entry_id | title | logo_need | status | local official asset | action |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `B-1` | Gemini | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。Google Brand Resource Center の利用条件を前提に、Gemini に使う公式プロダクトアイコン/lockup と許諾要否を確認してから合成 |
| `B-2` | Claude | required | `official_logo_applied` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | B-focus ベースに公式 Claude ロゴを後合成済み。`overlay_candidates_contact_sheet.png` で目視確認 |
| `B-3` | ChatGPT | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。OpenAI 公式ブランドガイドを前提に、OpenAI wordmark と ChatGPT 固有表現のどちらを使うか決めてから合成 |
| `B-4` | Cursor | required | `official_logo_applied` | `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png` | B-focus ベースに公式 Cursor horizontal lockup を後合成済み。`overlay_candidates_contact_sheet.png` で目視確認 |
| `B-5` | GitHub Copilot | required | `official_logo_applied` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | 本番 `assets/ponchi/final/B-5.webp` に公式 lockup 合成済み |
| `B-7` | Claude Code | required | `official_logo_applied` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png` | B-focus ベースに公式 Claude Code ロゴを後合成済み。`overlay_candidates_contact_sheet.png` で目視確認 |
| `B-8` | Codex | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。OpenAI 公式ブランドガイドを前提に、Codex 固有 lockup があるか、OpenAI wordmark で扱うかを確認してから合成 |
| `B-9` | v0 | required | `official_logo_applied` | `assets/logos/vercel/v0-assets/v0/Light/v0-logo-light.png` | B-focus ベースに公式 v0 ロゴを後合成済み。180px配置で final 候補へ昇格 |
| `B-10` | Devin | required | `official_logo_source_review_required` | none | batch-002 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-11` | Bolt.new | required | `official_logo_source_review_required` | none | batch-002 対象。StackBlitz/Bolt の公式素材を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-12` | Perplexity | required | `official_logo_source_review_required` | none | batch-002 対象。公式 wordmark/icon と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-13` | ElevenLabs | required | `official_logo_source_review_required` | none | batch-002 対象。公式 wordmark/icon と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-14` | Genspark | required | `official_logo_source_review_required` | none | batch-002 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-15` | Microsoft Copilot | required | `official_logo_source_review_required` | none | batch-002 対象。Microsoft 公式ブランド/製品素材を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-16` | Microsoft 365 Copilot | required | `official_logo_source_review_required` | none | batch-002 対象。Microsoft 365 Copilot の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-17` | Edge Copilot | required | `official_logo_source_review_required` | none | batch-002 対象。Edge/Copilot のどちらの公式表現にするか決めるまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-18` | Aqua Voice | required | `official_logo_source_review_required` | none | batch-002 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-19` | Claude Cowork | required | `official_logo_source_review_required` | none | batch-002 対象。正式名称と Claude ロゴ適用可否を Anthropic 公式ソースで確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-20` | Vercel | required | `official_logo_applied` | `assets/logos/vercel/vercel-assets/Vercel/logotype/light/vercel-logotype-light.png` | batch-002 ベースに公式 Vercel ロゴを後合成済み。final 候補で目視確認 |
| `B-21` | Netlify | required | `official_logo_applied` | `assets/logos/netlify/netlify-logo-full/netlify-logo-full/large/lightmode/logo-netlify-large-monochrome-lightmode.png` | batch-002 ベースに公式 Netlify ロゴを後合成済み。`ponchi-batch-002-base-contact-sheet.png` と final 候補で目視確認 |
| `B-22` | Cloudflare | required | `official_logo_applied` | `assets/logos/cloudflare/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare logo/png/CF_logo_horizontal_singlecolor_blk.png` | batch-002 ベースに公式 Cloudflare ロゴを後合成済み。`ponchi-batch-002-base-contact-sheet.png` と final 候補で目視確認 |
| `B-23` | AWS | required | `official_logo_source_review_required` | none | batch-002 対象。ローカルの AWS Architecture Icons はブランド lockup と別扱い。公式ロゴ/利用条件を確認してから合成 |
| `B-24` | Google Cloud | required | `official_logo_source_review_required` | none | batch-002 対象。Google Cloud の公式ロゴ素材・利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-25` | Azure | required | `official_logo_source_review_required` | none | batch-002 対象。Microsoft Azure の公式ロゴ素材・利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-26` | Azure OpenAI | required | `official_logo_source_review_required` | none | batch-002 対象。Azure と OpenAI のどちらの公式表現にするか決めるまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-27` | Vertex AI | required | `official_logo_source_review_required` | none | batch-002 対象。Google Cloud/Vertex AI の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-28` | Render | required | `official_logo_applied` | `assets/logos/render/render-wordmark-from-press.png` | batch-002 ベースに公式 Render wordmark を後合成済み。final 候補で目視確認 |
| `B-29` | Supabase | required | `official_logo_applied` | `assets/logos/supabase/brand-assets/supabase-logo-wordmark--light.png` | batch-002 ベースに公式 Supabase ロゴを後合成済み。final 候補で目視確認 |
| `D-12` | Claude 4 系 | required | `official_logo_source_available_needs_import` | none | モデル系列名に Claude が入るためロゴ対象。Anthropic Newsroom の press kit から公式素材を取得・記録してから合成 |
| `F-1` | JavaScript | not_needed | `logo_avoid` | none | JS, TypeScript, React, Node.js などのロゴを使わない。汎用ファイル、ブラウザ、サーバ記号だけにする |
| `F-2` | TypeScript | not_needed | `logo_avoid` | none | TypeScript ロゴを使わない。Before/After の汎用型チェック表現で説明する |
| `F-60` | GitHub | required | `official_logo_applied` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | 本番 `assets/ponchi/final/F-60.webp` に公式 lockup 合成済み |
| `G-1` | Context | not_needed | `logo_avoid` | none | 概念図。ロゴ不要 |
| `J-14` | LLM | not_needed | `logo_avoid` | none | 概念図。ロゴ不要 |

## ローカル公式素材あり

現時点で、この台帳内で後合成に使える公式素材は GitHub 系、Claude 系、Cursor、v0、Vercel、Netlify、Cloudflare、Render、Supabase。

| brand | asset | entries |
| :-- | :-- | :-- |
| GitHub Copilot | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | `B-5` |
| GitHub | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | `F-60` |
| Claude | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | `B-2` |
| Claude Code | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png` | `B-7` |
| Cursor | `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png` | `B-4` |
| v0 | `assets/logos/vercel/v0-assets/v0/Light/v0-logo-light.png` | `B-9` |
| Vercel | `assets/logos/vercel/vercel-assets/Vercel/logotype/light/vercel-logotype-light.png` | `B-20` |
| Netlify | `assets/logos/netlify/netlify-logo-full/netlify-logo-full/large/lightmode/logo-netlify-large-monochrome-lightmode.png` | `B-21` |
| Cloudflare | `assets/logos/cloudflare/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare logo/png/CF_logo_horizontal_singlecolor_blk.png` | `B-22` |
| Render | `assets/logos/render/render-wordmark-from-press.png` | `B-28` |
| Supabase | `assets/logos/supabase/brand-assets/supabase-logo-wordmark--light.png` | `B-29` |

AWS Architecture Icons はローカルにあるが、B-23 にそのまま使うブランド lockup とは別扱いにする。B-23 は公式ロゴ/利用条件を確認するまで `official_logo_source_review_required` のまま止める。Ruby の素材は今回の対象には直接該当しない。

## 次の処理

1. この台帳を先にコミットする。
2. `official_logo_applied` は目視と寸法監査だけ行い、追加のロゴ生成はしない。
3. `official_logo_source_available_needs_import` は、公式素材の取得、`docs/brand_usage_audit.md` への記録、ローカル PNG/SVG 参照化、合成監査の順に進める。
4. `official_logo_source_review_required` は、具体ロゴ・取得経路・許諾条件を確認するまで本番ロゴ合成と本番差し替えを進めない。
5. `base_2to1_ready_logo_blocked` は、公式素材の取得・利用条件確認ができるまで、本番ロゴ合成と本番差し替えを進めない。
6. `logo_avoid` は、汎用図解として本番候補を進めてよい。

## 適用監査

`official_logo_applied` の確認結果は `docs/ponchi_logo_application_audit_2026-06-01.md` に記録する。

## 2:1 ベース再生成

ブランド系の元絵 2:1 ベース再生成結果は `docs/ponchi_brand_base_regeneration_2026-06-01.md` に記録する。
