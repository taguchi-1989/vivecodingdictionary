# 要直しキュー（revision queue）

*自動生成: 2026-04-29 20:33 / `scripts/update_review_queue.py`*

1 画面で「次やるべき・見直すべき・適合済み」が見えるダッシュボード。`scripts/validate_entry.py` のチェックを全件で走らせた結果を集計して再生成しています。手で編集しないでください。

## status 内訳

- **skeleton**: 270 件
- **drafting**: 33 件
- **needs_review**: 36 件
- **archived**: 13 件
- **合計**: 352 件

## ☆ 違反あり（最優先で直す）（0 件）

_なし_

## ⚠️ 警告あり（軽微超過 / 著者か entry-writer で手当て）（33 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-1 | Gemini | needs_review | ⚠ 58 字（目安 20-50、+8 字超過） |
| B-52 | Gemini の料金プラン | drafting | ⚠ 252 字（目安 155-250、+2 字超過） |
| D-21 | GPT-4 系 | drafting | ⚠ 311 字（目安 155-250、+61 字超過） |
| D-22 | o1 系 | drafting | ⚠ 273 字（目安 155-250、+23 字超過） |
| D-30 | Grok 系 | drafting | ⚠ 256 字（目安 155-250、+6 字超過） |
| D-40 | Llama 系 | drafting | ⚠ 296 字（目安 155-250、+46 字超過） |
| E-20 | MMLU | drafting | ⚠ 73 字（目安 25-60、+13 字超過）; ⚠ 265 字（目安 155-250、+15 字超過） |
| F-1 | JavaScript | drafting | ⚠ 255 字（目安 155-250、+5 字超過）; ⚠ です・ます外れの疑いあり（(?<![すまりぞ])だ[。\s] のパターン、要目視確認） |
| F-10 | React | drafting | ⚠ 245 字（目安 120-240、+5 字超過） |
| F-11 | Next.js | needs_review | ⚠ 197 字（目安 80-180、+17 字超過）; ⚠ 268 字（目安 155-250、+18 字超過）; ⚠ 469 字（目安 220-430、+39 字超過） |
| F-30 | VS Code | drafting | ⚠ 294 字（目安 155-250、+44 字超過） |
| F-4 | HTML | drafting | ⚠ 70 字（目安 25-60、+10 字超過）; ⚠ 200 字（目安 80-180、+20 字超過）; ⚠ 318 字（目安 155-250、+68 字超過） |
| F-5 | CSS | drafting | ⚠ 24 字（目安 25-50、-1 字不足）; ⚠ 257 字（目安 155-250、+7 字超過） |
| F-6 | Markdown | drafting | ⚠ 271 字（目安 155-250、+21 字超過） |
| F-60 | GitHub | drafting | ⚠ 298 字（目安 155-250、+48 字超過） |
| G-1 | Context | needs_review | ⚠ 65 字（目安 20-50、+15 字超過） |
| G-10 | Prompt Engineering | drafting | ⚠ 275 字（目安 120-240、+35 字超過）; ⚠ 293 字（目安 155-250、+43 字超過）; ⚠ 489 字（目安 220-430、+59 字超過） |
| G-11 | Context Engineering | drafting | ⚠ 51 字（目安 25-50、+1 字超過）; ⚠ 52 字（目安 20-50、+2 字超過）; ⚠ 275 字（目安 155-250、+25 字超過） |
| G-20 | CLAUDE.md | drafting | ⚠ 185 字（目安 80-180、+5 字超過）; ⚠ 263 字（目安 155-250、+13 字超過） |
| G-30 | Tool Use | drafting | ⚠ 297 字（目安 155-250、+47 字超過） |
| G-4 | System Prompt | drafting | ⚠ 181 字（目安 80-180、+1 字超過）; ⚠ 329 字（目安 155-250、+79 字超過） |
| G-5 | Context Window | drafting | ⚠ 58 字（目安 25-50、+8 字超過）; ⚠ 266 字（目安 155-250、+16 字超過） |
| H-50 | Bard → Gemini | drafting | ⚠ 277 字（目安 155-250、+27 字超過） |
| I-1 | MCP | needs_review | ⚠ 262 字（目安 155-250、+12 字超過） |
| I-10 | Filesystem MCP | drafting | ⚠ 57 字（目安 25-50、+7 字超過）; ⚠ 198 字（目安 80-180、+18 字超過）; ⚠ 436 字（目安 220-430、+6 字超過） |
| I-11 | GitHub MCP | needs_review | ⚠ 296 字（目安 155-250、+46 字超過） |
| I-2 | MCP Server | drafting | ⚠ 51 字（目安 25-50、+1 字超過）; ⚠ 218 字（目安 80-180、+38 字超過）; ⚠ 325 字（目安 155-250、+75 字超過） |
| I-20 | Playwright MCP | drafting | ⚠ 59 字（目安 25-50、+9 字超過）; ⚠ 292 字（目安 155-250、+42 字超過） |
| I-3 | MCP Client | drafting | ⚠ 55 字（目安 25-50、+5 字超過）; ⚠ 185 字（目安 80-180、+5 字超過） |
| J-10 | Machine Learning | drafting | ⚠ 61 字（目安 25-50、+11 字超過）; ⚠ 264 字（目安 155-250、+14 字超過） |
| J-11 | Deep Learning | drafting | ⚠ 56 字（目安 25-50、+6 字超過）; ⚠ 261 字（目安 155-250、+11 字超過）; ⚠ 433 字（目安 220-430、+3 字超過） |
| J-51 | Hallucination | drafting | ⚠ 51 字（目安 25-50、+1 字超過）; ⚠ 183 字（目安 80-180、+3 字超過）; ⚠ 267 字（目安 155-250、+17 字超過） |
| J-77 | GPU (概念) | drafting | ⚠ `title` 末尾に括弧書きが含まれます — 読み・展開は `title_reading` フィー; ⚠ 255 字（目安 155-250、+5 字超過） |

## ✍️ 書きかけ（drafting・全パス済み・自動昇格漏れ）（4 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| D-1 | Gemini 2 系 | drafting | — |
| E-2 | SWE-Bench Verified | drafting | — |
| E-50 | Chatbot Arena | drafting | — |
| J-13 | Transformer | drafting | — |

## 📝 著者レビュー待ち（needs_review・全パス）（30 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-2 | Claude | needs_review | — |
| B-20 | Vercel | needs_review | — |
| B-23 | AWS | needs_review | — |
| B-3 | ChatGPT | needs_review | — |
| B-4 | Cursor | needs_review | — |
| B-5 | GitHub Copilot | needs_review | — |
| B-50 | Claude の料金プラン | needs_review | — |
| B-51 | ChatGPT の料金プラン | needs_review | — |
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
| F-51 | git push | needs_review | — |
| F-52 | git pull | needs_review | — |
| F-53 | branch | needs_review | — |
| F-54 | commit | needs_review | — |
| F-55 | merge | needs_review | — |
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
