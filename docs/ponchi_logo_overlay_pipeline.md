# Ponchi Logo Overlay Pipeline

## 結論

ロゴは画像生成に描かせない。生成画像には白い余白だけを作り、公式素材を後工程で同じ座標に合成する。

## 標準座標

標準キャンバスは `1254x627`。

主ブランド lockup の標準配置:

| 項目 | 値 |
| :-- | --: |
| logo width | `520px` |
| right margin | `48px` |
| x | `686px` |
| y | `36px` |

`x = 1254 - 48 - 520 = 686`

この座標は、上部右側に公式 lockup を大きく置く前提。ロゴは小さな飾りではなく、縮小プレビューでも読めるサイズにする。

## コマンド

```powershell
python scripts\composite_official_logo.py `
  --input assets\ponchi\experiments\regeneration\B-5_v6_clean_diagram_base_1254x627.png `
  --logo "assets\logos\github\GitHub_Logos\GitHub Logos\PNG\GitHub_Copilot_Lockup_Black_Clearspace.png" `
  --out assets\ponchi\experiments\regeneration\logo-overlay-trials-2026-05-31\B-5_v6_scripted_github_copilot_logo.png
```

必要なら `--width`, `--x`, `--y`, `--right-margin` を明示する。

## ルール

- 公式素材だけを使う。
- 公式素材の形、色、縦横比、余白を変えない。
- 画像生成側でロゴ風文字、公式アイコン風マーク、ブランドカラーを作らせない。
- ロゴの周囲にカード、枠、バッジ、影、発光、吹き出しを足さない。
- 公式素材の取得元とローカルパスを `docs/brand_usage_audit.md` に記録する。
- 合成後に `scripts/audit_image_sizes.py` で 2:1 を確認する。

## 採用判断

生成画像にロゴを入れるのではなく、以下の 2 ファイルをセットで管理する。

- base image: ロゴなしの白い余白つき画像
- composited image: 公式素材を後合成した確認画像

本番 `assets/ponchi/final/*.webp` に入れるのは、目視監査済みの composited image だけにする。
