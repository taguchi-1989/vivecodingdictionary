# Ponchi Brand Base Regeneration 2026-06-01

## 目的

ロゴを後付けする前に、元絵そのものを意味のある 2:1 構図として再生成する。公式ロゴが未取得の項目でも、AI 生成ではロゴを描かせず、右上に公式素材後合成用の白い余白を持つベース画像までは作る。

## 保存先

`assets/ponchi/experiments/regeneration/brand-base-trials-2026-06-01/`

## 生成結果

| entry_id | title | file | role | status | note |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `B-1` | Gemini | `B-1_gemini_base_2to1_1254x627.png` | logo-clearspace base | usable base | Gemini/Google 風ロゴ、ブランド色なし。右上余白あり |
| `B-2` | Claude | `B-2_claude_base_2to1_1254x627.png` | logo-clearspace base | usable base | Claude/Anthropic 風ロゴ、ブランド色なし。右上余白あり |
| `B-3` | ChatGPT | `B-3_chatgpt_base_2to1_1254x627.png` | logo-clearspace base | usable base | OpenAI/ChatGPT 風ロゴ、実 UI、ブランド色なし。右上余白あり |
| `B-4` | Cursor | `B-4_cursor_base_2to1_1254x627.png` | logo-clearspace base | usable base | Cursor 風ロゴ、実 UI、ブランド色なし。右上余白あり |
| `B-8` | Codex | `B-8_codex_base_2to1_1254x627.png` | logo-clearspace base | usable base | OpenAI/Codex/GitHub 風ロゴ、実 UI、ブランド色なし。右上余白あり |
| `D-12` | Claude 4 系 | `D-12_claude4_base_2to1_1254x627.png` | logo-avoid base | usable base | ロゴなしのモデル系列タイムラインとして生成 |

比較用 contact sheet:

`assets/ponchi/experiments/regeneration/brand-base-trials-2026-06-01/contact-sheets/brand_base_trials_contact_sheet.png`

## 監査

```powershell
python scripts\audit_image_sizes.py --dir assets\ponchi\experiments\regeneration\brand-base-trials-2026-06-01 --suffix .png
```

結果:

- 6 images scanned
- `1254x627`: 6
- aspect `2:1`: 6

## 判断

- ここで作った画像は、ロゴ後合成前の「元絵 2:1 ベース」。
- `B-1`, `B-2`, `B-3`, `B-4`, `B-8` は公式素材と利用条件が未確認なので、本番 `assets/ponchi/final/*.webp` への反映はまだ行わない。
- `D-12` はロゴ不要で進められるが、本番反映は別コミットで目視比較してから行う。
- ロゴが必要な項目でも、AI 生成でロゴ、公式アイコン、公式マーク、ブランドカラーを描かせない。
