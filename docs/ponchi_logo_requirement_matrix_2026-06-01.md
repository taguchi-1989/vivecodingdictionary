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
| `B-2` | Claude | required | `official_logo_source_available_needs_import` | none | 2:1 ベース生成済み。Anthropic Newsroom の press kit から公式素材を取得・記録してから合成 |
| `B-3` | ChatGPT | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。OpenAI 公式ブランドガイドを前提に、OpenAI wordmark と ChatGPT 固有表現のどちらを使うか決めてから合成 |
| `B-4` | Cursor | required | `official_logo_source_available_needs_import` | none | 2:1 ベース生成済み。Cursor 公式 brand assets から horizontal lockup を取得・記録してから合成 |
| `B-5` | GitHub Copilot | required | `official_logo_applied` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | 本番 `assets/ponchi/final/B-5.webp` に公式 lockup 合成済み |
| `B-8` | Codex | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。OpenAI 公式ブランドガイドを前提に、Codex 固有 lockup があるか、OpenAI wordmark で扱うかを確認してから合成 |
| `D-12` | Claude 4 系 | required | `official_logo_source_available_needs_import` | none | モデル系列名に Claude が入るためロゴ対象。Anthropic Newsroom の press kit から公式素材を取得・記録してから合成 |
| `F-1` | JavaScript | not_needed | `logo_avoid` | none | JS, TypeScript, React, Node.js などのロゴを使わない。汎用ファイル、ブラウザ、サーバ記号だけにする |
| `F-2` | TypeScript | not_needed | `logo_avoid` | none | TypeScript ロゴを使わない。Before/After の汎用型チェック表現で説明する |
| `F-60` | GitHub | required | `official_logo_applied` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | 本番 `assets/ponchi/final/F-60.webp` に公式 lockup 合成済み |
| `G-1` | Context | not_needed | `logo_avoid` | none | 概念図。ロゴ不要 |
| `J-14` | LLM | not_needed | `logo_avoid` | none | 概念図。ロゴ不要 |

## ローカル公式素材あり

現時点で、この台帳内で後合成に使える公式素材は GitHub 系のみ。

| brand | asset | entries |
| :-- | :-- | :-- |
| GitHub Copilot | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | `B-5` |
| GitHub | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | `F-60` |

AWS と Ruby の素材はローカルにあるが、今回の 12 件の対象プロンプトには直接該当しない。

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
