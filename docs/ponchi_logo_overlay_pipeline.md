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

## サイズレンジ

主ブランド lockup は `520px` を標準にする。実画像の余白に応じて、以下の範囲だけで調整する。

| logo width | 使い方 | 判定 |
| :-- | :-- | :-- |
| `440px` | 比較用の小さめ確認 | 原則は小さい。採用しない |
| `480px` | 余白が狭い画像の下限 | 読める場合のみ採用可 |
| `520px` | 標準 | 第一候補 |
| `560px` | ロゴを強めに見せたい場合 | 余白が十分なら採用可 |
| `600px` | 大きめ確認、ブランド回の最大候補 | 余白が広い場合のみ。窮屈なら不採用 |

標準の右上配置では、`x = 1254 - 48 - logo_width` として右端をそろえる。`y` は原則 `36px`。上下が窮屈な場合だけ `32-44px` の範囲で微調整する。

生成時に確保する白い余白は、実際に使うロゴ幅に合わせて必要最小限にする。標準 `520px` lockup の場合、右上の実効 clearspace はおおむね横 `520-580px`、縦 `150-220px` までを目安にする。ロゴのための枠、カード、プレースホルダーは描かない。

この余白は、2:1 の画像を後から壊さずにロゴを入れるための設計領域として扱う。ベース画像の段階で、ロゴ予定領域の下に人物、顔、手、重要ノード、矢印、主図解、模様、薄いアイコンを置かない。画面全体は完成した 2:1 の誌面に見せるが、右上 clearspace は静かな negative space として残す。ロゴ予定地以外の右半分や上半分まで空けてしまう画像は不採用にする。

ベース画像の採用基準:

- ロゴなしでも構図が破綻していない。
- ロゴを合成しても重要な情報を隠さない。
- ロゴ周囲に枠、カード、ラベル、広告枠のような扱いがない。
- ロゴが入ることでブランド識別が完成し、主図解の意味が変わらない。
- 主図解、人物、フローのまとまりがキャンバス幅の半分以上を使っている。
- `1254x627` のベース画像で、非白領域の概算 bounding box が少なくとも 50% 程度はある。ただし、線が細かいだけで面積を稼いでいる画像は目視で不採用にできる。

不採用にする例:

- 主題が左下または中央だけに小さく寄り、右側が大きな空き地に見える。
- ロゴ clearspace を言い訳にして、図解カードや人物を縮小しすぎている。
- 小さいカードや細い矢印が多く、200px 程度のサムネイルで意味が消える。

## コマンド

```powershell
python scripts\composite_official_logo.py `
  --input assets\ponchi\experiments\regeneration\B-5_v6_clean_diagram_base_1254x627.png `
  --logo "assets\logos\github\GitHub_Logos\GitHub Logos\PNG\GitHub_Copilot_Lockup_Black_Clearspace.png" `
  --out assets\ponchi\experiments\regeneration\logo-overlay-trials-2026-05-31\B-5_v6_scripted_github_copilot_logo.png
```

必要なら `--width`, `--x`, `--y`, `--right-margin` を明示する。

ベース画像の空きすぎも同時に確認する場合:

```powershell
python scripts\composite_official_logo.py `
  --input assets\ponchi\experiments\regeneration\B-1_gemini_base_1254x627.png `
  --logo assets\logos\gemini\official_lockup.png `
  --out assets\ponchi\experiments\regeneration\B-1_gemini_logo_1254x627.png `
  --audit-density `
  --min-bbox-coverage 0.50
```

`--audit-density` はロゴ合成前のベース画像を概算監査する。主題が小さく、非白領域の bounding box が小さい場合は失敗させる。意図的に広い空間を使う特殊構図だけ、`--warn-only-density` を付けて警告扱いにする。

サイズ比較を作る場合:

```powershell
foreach ($w in 440,480,520,560,600) {
  python scripts\composite_official_logo.py `
    --input assets\ponchi\experiments\regeneration\B-5_v6_clean_diagram_base_1254x627.png `
    --logo "assets\logos\github\GitHub_Logos\GitHub Logos\PNG\GitHub_Copilot_Lockup_Black_Clearspace.png" `
    --width $w `
    --out "assets\ponchi\experiments\regeneration\logo-size-trials-2026-05-31\B-5_v6_logo_${w}px.png"
}
```

## ルール

- 公式素材だけを使う。
- 公式素材の形、色、縦横比、余白を変えない。
- 画像生成側でロゴ風文字、公式アイコン風マーク、ブランドカラーを作らせない。
- ロゴの周囲にカード、枠、バッジ、影、発光、吹き出しを足さない。
- 公式素材の取得元とローカルパスを `docs/brand_usage_audit.md` に記録する。
- 合成後に `scripts/audit_image_sizes.py` で 2:1 を確認する。
- 合成前に、ベース画像がロゴ余白を取りすぎていないか確認する。

## 採用判断

生成画像にロゴを入れるのではなく、以下の 2 ファイルをセットで管理する。

- base image: ロゴなしの白い余白つき画像
- composited image: 公式素材を後合成した確認画像

本番 `assets/ponchi/final/*.webp` に入れるのは、目視監査済みの composited image だけにする。
