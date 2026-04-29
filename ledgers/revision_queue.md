# 要直しキュー（revision queue）

*自動生成: 2026-04-29 09:07 / `scripts/update_review_queue.py`*

1 画面で「次やるべき・見直すべき・適合済み」が見えるダッシュボード。`scripts/validate_entry.py` のチェックを全件で走らせた結果を集計して再生成しています。手で編集しないでください。

## status 内訳

- **skeleton**: 310 件
- **drafting**: 1 件
- **needs_review**: 28 件
- **archived**: 8 件
- **合計**: 347 件

## ☆ 違反あり（最優先で直す）（0 件）

_なし_

## ⚠️ 警告あり（軽微超過 / 著者か entry-writer で手当て）（3 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-1 | Gemini | needs_review | ⚠ 58 字（目安 20-50、+8 字超過） |
| G-1 | Context | needs_review | ⚠ 65 字（目安 20-50、+15 字超過） |
| I-1 | MCP | needs_review | ⚠ 262 字（目安 155-250、+12 字超過） |

## ✍️ 書きかけ（drafting・全パス済み・自動昇格漏れ）（0 件）

_なし（drafting で全パスしたものは自動で needs_review に上がります）_

## 📝 著者レビュー待ち（needs_review・全パス）（24 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-2 | Claude | needs_review | — |
| B-20 | Vercel | needs_review | — |
| B-23 | AWS | needs_review | — |
| B-3 | ChatGPT | needs_review | — |
| B-4 | Cursor | needs_review | — |
| B-5 | GitHub Copilot | needs_review | — |
| B-50 | Claude の料金プラン | needs_review | — |
| C-1 | OpenAI | needs_review | — |
| C-2 | Anthropic | needs_review | — |
| C-3 | Google DeepMind | needs_review | — |
| C-50 | Sam Altman | needs_review | — |
| C-51 | Dario Amodei | needs_review | — |
| C-9 | NVIDIA | needs_review | — |
| D-11 | Claude 3.5 系 | needs_review | — |
| D-12 | Claude 4 系 | needs_review | — |
| D-13 | Claude 4.5 系 | needs_review | — |
| D-20 | GPT-5 系 | needs_review | — |
| E-1 | SWE-Bench | needs_review | — |
| F-3 | Python | needs_review | — |
| F-50 | git | needs_review | — |
| G-2 | Token | needs_review | — |
| G-40 | バイブコーディング | needs_review | — |
| H-53 | ChatGPT 登場 | needs_review | — |
| J-14 | LLM | needs_review | — |

## ✅ 完成（ready・全パス）（0 件）

_なし_

## 動線

- **☆ 違反**: その場で entry-writer を呼んで直す（status は drafting のままにする）
- **⚠️ 警告**: 軽微なら手で削る／溜まったらまとめて対応
- **needs_review**: 著者本人が「非エンジニアのつまずき」「私のコメント」を埋めて `status: ready` に上げる
- このキューは `Edit/Write` のたびに自動更新されます。手動更新は `python3 scripts/update_review_queue.py`
