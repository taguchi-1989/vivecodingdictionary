# Ponchi Image Generation Rules

## 基本方針

ポンチ絵の本番画像は、図鑑全体で同じシリーズに見えることを優先する。個別画像の派手さより、一覧で並べた時の統一感を重視する。

## 色ルール

**白・黒・グレー・青系以外は使わない。**

許可する色:

- `#FFFFFF` pure white: main background
- `#F7F9FC` off-white / paper white: very subtle surface fill only
- `#1A1A1A` black: main linework and official black logos
- `#6B7280` neutral gray: secondary lines, inactive UI strokes, shadows
- `#EAF1FB` pale blue 1: active AI suggestion fill, very light focus area
- `#D6E6FA` pale blue 2: stronger active suggestion line or selected row
- `#8DB7E8` soft blue: small glow ticks, accepted path, connector highlight
- `#3F7FD1` medium blue: small icon accent or active cursor accent only
- `#123E82` deep navy: rare emphasis, arrows, or structural accent

禁止する色:

- 黄
- 緑
- 赤
- 紫
- 茶
- オレンジ
- 虹色
- ブランドカラー
- カラフルなUIやグラフ

色の役割:

- 背景は白を基本にする。薄い紙色や極薄青を使う場合も、面全体を染めない。
- 黒は線画、人物、机、PC、図形の主線に使う。
- グレーは未選択、Before 側、非アクティブな UI 線、軽い影に使う。
- 青は以下の 5 色だけを使う。中間色を増やさない。
  - `#EAF1FB`: 面のごく薄いハイライト、AI 補完候補の背景
  - `#D6E6FA`: 補完候補の行、選択中の薄い帯
  - `#8DB7E8`: 経路、接続線、小さな発光線
  - `#3F7FD1`: 小さいアクティブ点、カーソル、アイコンの一点アクセント
  - `#123E82`: 重要矢印、主ノード、章アクセント。ただし面積は小さくする
- 淡い青は「AI が効いている箇所」「補完候補」「選択中の経路」だけに使う。
- 濃紺は矢印、重要ノード、章ごとのごく小さいアクセントに限定する。
- 青い装飾線、青いスパークル、ランダムな発光、青い背景面は避ける。
- 企業・サービスのブランドカラーは、公式ロゴ素材そのものを後合成する場合を除いて使わない。

画像生成プロンプトでは、以下を必ず入れる。

```text
Color palette: strict white/black/gray plus the approved blue palette only.
Use pure white background (#FFFFFF), optional off-white (#F7F9FC), black
linework (#1A1A1A), neutral gray secondary strokes (#6B7280), and only these
blue values: #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82. Use #EAF1FB or
#D6E6FA for active AI suggestion fills, #8DB7E8 for selected paths or small
glow ticks, #3F7FD1 for tiny active accents, and #123E82 only for rare
structural emphasis. Do not use any other blue, cyan, teal, purple-blue, or
brand blue. Do not use yellow, green, red, purple, brown, orange, rainbow
colors, decorative blue sparkles, blue background fills, or brand colors.
```

## ロゴルール

AI 生成では会社ロゴ・サービスロゴ・公式アイコン・公式マークを描かせない。ロゴやアイコンが読者理解に必要な場合だけ、公式ブランド素材を取得し、生成後に決定論的に合成する。詳細は `docs/ponchi_brand_asset_rules.md` に従う。

ロゴ合成の共通ルール:

- 公式 SVG/PNG/PDF 由来の素材だけを使う。
- ロゴの形、色、縦横比、余白を変えない。
- 白背景に黒ロゴ、または公式が許可する単色版を優先する。
- ロゴの周囲に独自の枠、カード、吹き出し、バッジ、影を足さない。
- 画像生成プロンプトでは、ロゴ用の白い余白だけを予約する。
- `1254x627` の 2:1 ポンチ絵では、主要サービスロゴの目安を横幅 `500-520px` にする。
- 小さな補助ロゴや画面内の二次的なロゴは使わない。必要なら本文・キャプションで補う。
- 公式アイコンや公式マークもロゴと同じ扱いにする。AI 生成で似せない。
- 汎用アイコンは使ってよいが、実在ブランドのアイコンに見える形・色にはしない。

ロゴ合成用のプロンプト文:

```text
Logo rule: do not generate, imitate, redraw, or approximate any company or
service logo. Reserve a clean white clearspace area for a later official logo
overlay. Do not draw a box, border, badge, label, icon, shadow, or placeholder
around this area. On a 1254x627 canvas, leave enough clearspace for an official
logo lockup about 500-520px wide.
```

ブランド素材禁止の追加プロンプト文:

```text
Brand asset rule: do not generate, imitate, redraw, approximate, or stylize any
company logo, service logo, app icon, product icon, official mark, mascot,
trademarked symbol, brand color scheme, or real product UI. If brand
identification is required, reserve a clean white clearspace area for a later
official asset overlay. Generic non-branded icons such as folders, arrows,
browser frames, server boxes, abstract nodes, and simple clouds are allowed
only if they do not resemble any real brand asset.
```

## スタイル

- 白い紙に黒・グレーのシンプルな線画。
- 鉛筆スケッチ風、ラフな手描き線、ハッチング、ざらついた筆致は避ける。
- 線は均一で読みやすく、やや図解・アイコン寄りのクリーンなタッチにする。
- 青系は補助色として使う。ただし意味のある箇所だけに限定する。
- 影やグラデーションは控えめ。
- 200px程度のサムネイルでも意味が分かる。
- ロゴ、商標、実在UIの AI 生成での再現は避ける。
- 人物・ロボットの一貫性は `docs/ponchi_character_bible.md` に従う。

画像生成プロンプトでは、スタイル指定に以下を入れる。

```text
Style: clean simple editorial line illustration, not pencil sketch. Use smooth
uniform black lines, flat light gray fills, minimal shading, no hatching, no
scratchy hand-drawn texture, no marker texture, and no painterly look. The
image should feel like a clear technical-book diagram with friendly human
figures, not a rough drawing.
```

## 禁則

- 読める文字を画像内に入れない。
- 会社ロゴ・サービスロゴを AI 生成で入れない。
- 実在人物の顔を似せない。
- 暗い背景にしない。
- 1枚だけ目立つカラフルな絵にしない。

## 再生成時の確認

再生成候補を見る時は、まず以下を確認する。

1. 白黒青系だけで成立しているか。
2. 概念を誤解させる小物がないか。
3. 既存シリーズと線の密度が近いか。
4. 被写体が小さすぎないか。
5. 画像内の文字・ロゴ・ブランド色が混ざっていないか。
