# Ponchi Logo Size Trials 2026-05-31

## 目的

公式ロゴ後合成のサイズ感を確認するため、同じ B-5 ベース画像に GitHub Copilot 公式 lockup を 5 段階で合成した。

## 保存先

`assets/ponchi/experiments/regeneration/logo-size-trials-2026-05-31/`

## 試作

| file | logo width | x | y | 判定 |
| :-- | --: | --: | --: | :-- |
| `B-5_v6_logo_440px.png` | `440px` | `766` | `36` | 小さめ比較。原則不採用 |
| `B-5_v6_logo_480px.png` | `480px` | `726` | `36` | 下限候補 |
| `B-5_v6_logo_520px.png` | `520px` | `686` | `36` | 標準候補 |
| `B-5_v6_logo_560px.png` | `560px` | `646` | `36` | 強め候補 |
| `B-5_v6_logo_600px.png` | `600px` | `606` | `36` | 最大候補。余白が広い場合のみ |

## 監査

```powershell
python scripts\audit_image_sizes.py --dir assets\ponchi\experiments\regeneration\logo-size-trials-2026-05-31 --suffix .png
```

結果:

- 5 images scanned
- `1254x627`: 5
- aspect `2:1`: 5

## 採用方針

標準は `520px`。画像ごとの余白が狭ければ `480px`、ロゴを強めたいサービス回では `560px` までを通常範囲にする。`600px` は比較用の最大候補で、構図が広告っぽく見える場合は使わない。
