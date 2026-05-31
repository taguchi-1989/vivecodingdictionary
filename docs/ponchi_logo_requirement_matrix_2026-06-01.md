# Ponchi Logo Requirement Matrix 2026-06-01

## 目的

ポンチ絵再生成で、ロゴを入れるべき項目と入れない項目を先に分ける。ロゴが必要でも、公式素材と利用条件が確認できていないものは後合成しない。AI 生成でロゴ風の図形やブランドカラーを作らせることも禁止する。

対象は、現在 `assets/ponchi/prompts/` にある再生成プロンプト 12 件。

## ステータス定義

| status | 意味 |
| :-- | :-- |
| `logo_avoid` | ロゴ不要。汎用アイコンだけで説明する |
| `logo_optional_avoid` | 題材にブランド名はあるが、本文・キャプションで足りるため画像内ロゴは使わない |
| `official_logo_required_blocked` | ロゴが必要だが、公式素材・利用条件・ローカルパスが未確定 |
| `official_logo_available` | 公式素材がローカルにあり、後合成に進められる |
| `official_logo_applied` | 公式素材を後合成済み。本番画像または確認画像まで作成済み |

## マーキング

| entry_id | title | logo_need | status | local official asset | action |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `B-1` | Gemini | required | `official_logo_required_blocked` | none | Gemini 公式素材と利用条件を確認するまで停止。AI 生成で星マーク、Google 系アイコン、ブランドカラーを作らない |
| `B-2` | Claude | required | `official_logo_required_blocked` | none | Claude 公式素材と利用条件を確認するまで停止。AI 生成で Claude 風マークやブランド色を作らない |
| `B-3` | ChatGPT | required | `official_logo_required_blocked` | none | OpenAI / ChatGPT 公式素材と利用条件を確認するまで停止。AI 生成で OpenAI knot 風マークや ChatGPT UI を作らない |
| `B-4` | Cursor | required | `official_logo_required_blocked` | none | Cursor 公式素材と利用条件を確認するまで停止。AI 生成で Cursor アイコンやエディタ UI を似せない |
| `B-5` | GitHub Copilot | required | `official_logo_applied` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | 本番 `assets/ponchi/final/B-5.webp` に公式 lockup 合成済み |
| `B-8` | Codex | required | `official_logo_required_blocked` | none | OpenAI / Codex 公式素材と利用条件を確認するまで停止。GitHub PR など周辺ロゴも生成しない |
| `D-12` | Claude 4 系 | optional | `logo_optional_avoid` | none | モデル系列の説明は図解で足りる。画像内ロゴは使わず、Claude 名は本文・キャプション側で扱う |
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
3. `official_logo_required_blocked` は公式素材の取得・利用条件確認ができるまで、画像生成や本番差し替えを進めない。
4. `logo_avoid` と `logo_optional_avoid` は、汎用図解として本番候補を進めてよい。

## 適用監査

`official_logo_applied` の確認結果は `docs/ponchi_logo_application_audit_2026-06-01.md` に記録する。
