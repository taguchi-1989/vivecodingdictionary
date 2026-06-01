# Ponchi Unused Image Trials 2026-05-31

## 目的

他ブランチの未使用作業を丸ごとマージする代わりに、現在の画像生成ルールで安全に試せる未使用寄りの題材を 3 枚だけ試作した。

## 保存先

`assets/ponchi/experiments/regeneration/unused-trials-2026-05-31/`

## 試作

| entry_id | file | status | note |
| :-- | :-- | :-- | :-- |
| `F-1` | `F-1_javascript_1254x627.png` | usable draft | ロゴなし、読める文字なし。JavaScript 黄色ロゴを避けた汎用構図 |
| `G-1` | `G-1_context_1254x627.png` | needs character fix | 2:1 と概念図は良いが、人物が Character A より男性寄り |
| `J-14` | `J-14_llm_1254x627.png` | needs character fix | LLM フローは分かりやすいが、人物が Character A より男性寄り |

## 監査

生成元は imagegen の標準出力で `1774x887`。プロジェクト内には標準確認サイズ `1254x627` のみ保存した。

```powershell
python scripts\audit_image_sizes.py --dir assets\ponchi\experiments\regeneration\unused-trials-2026-05-31 --suffix .png
```

結果:

- 3 images scanned
- `1254x627`: 3
- aspect `2:1`: 3

## 判断

この 3 枚は本番 `assets/ponchi/final/` にはまだ反映しない。次に進めるなら、`F-1` を第一候補として WebP 化して差し替え候補にし、`G-1` と `J-14` は Character A/B の指定を強めて再生成する。
