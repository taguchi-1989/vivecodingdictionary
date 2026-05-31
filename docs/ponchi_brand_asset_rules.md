# Ponchi Brand Asset Rules

作成日: 2026-05-31

## 目的

ポンチ絵の再生成時に、会社ロゴ、サービスロゴ、公式アイコン、公式マークを AI に描かせないための運用ルール。`drafts/IMAGE_GEN_POLICY_v2.md` の著者決定を、実作業向けに短く固定する。

## 結論

ブランドを識別するための視覚要素は、AI 生成しない。

AI 生成してはいけないもの:

- 会社ロゴ
- サービスロゴ
- アプリアイコン
- 製品アイコン
- 公式マーク
- 公式キャラクター、マスコット
- 公式 UI スクリーンショット風の画面
- ブランドカラーを使った「それっぽい」代用品

使う場合は、公式素材を取得して、後工程で決定論的に合成する。

## 用語

| 種別 | 例 | 扱い |
| :-- | :-- | :-- |
| 公式ロゴ | GitHub lockup, OpenAI mark, Claude logo | 公式素材のみ。AI 生成禁止 |
| 公式アイコン | Copilot icon, app icon, cloud service icon | 公式素材のみ。AI 生成禁止 |
| 公式マーク | Octocat, Gemini star など識別性のある記号 | 公式素材のみ。AI 生成禁止 |
| 汎用アイコン | フォルダ、雲、ブラウザ枠、サーバ箱、矢印 | AI 生成可。ただしブランド風にしない |
| 抽象図形 | ノード、線、箱、点、抽象ブラケット | AI 生成可 |

## 基本方針

1. ブランド識別が必要なエントリは、公式素材を後合成する。
2. 公式素材が未取得なら `blocked_brand_asset` にする。
3. AI 生成プロンプトでは、公式素材用の白い余白だけを予約する。
4. 公式素材の形、色、縦横比、余白を変えない。
5. 公式素材の周囲に独自の枠、カード、バッジ、影、発光を足さない。
6. 公式素材の利用条件とローカルパスを `docs/brand_usage_audit.md` に記録する。

## 合成サイズ

標準ポンチ絵キャンバスは `1254x627`。公式素材は小さな飾りではなく、読者が縮小プレビューでも識別できる大きさで置く。

| 用途 | 対象 | 目安サイズ | 使い方 |
| :-- | :-- | :-- | :-- |
| 主ブランド lockup | サービス名入りの横長ロゴ、例: GitHub Copilot lockup | 横幅 `500-520px` | 原則として上部右側の白い余白に置く。公式素材の余白込みで縮小し、切り抜かない |
| 主ブランド単体ロゴ | サービス名なしの公式マークを主役にする場合 | 横幅または高さ `180-240px` | lockup が無い場合だけ使う。読者理解に必要なとき以外は避ける |
| 補助的な公式アイコン | 画面内の小さな補助記号 | 原則使わない。必要時も `120-160px` 程度まで | 複数ロゴの羅列や小さなブランドアイコン散布は避ける |
| 汎用アイコン | フォルダ、雲、サーバ箱、矢印など | 構図に合わせる | ブランド素材ではないため、公式サイズ規定の対象外 |

主ブランド lockup を `500-520px` にする理由:

- `1254x627` の横幅に対して約 40% で、誌面プレビューや 200px 前後のサムネイルでも識別しやすい。
- 小さすぎるロゴは「飾り」や「読めないノイズ」になり、公式素材を使う意味が薄くなる。
- 公式素材を大きく扱う代わりに、画像生成側ではロゴ風の図形やブランドカラーを一切描かせない。

配置ルール:

- lockup は原則として上部右側の白い余白に置く。
- 余白は、合成後の公式素材が窮屈に見えない程度に広く確保する。
- ロゴの周囲に独自の枠、カード、ラベル、影、発光、吹き出しを足さない。
- 公式素材に含まれる clearspace は切り落とさない。
- 縦横比を変えず、横幅基準で縮小する。
- 文字入り lockup が読めないサイズになる場合は、その画像ではロゴを使わず本文・キャプション側で補う。

## プロンプト共通ブロック

```text
Brand asset rule: do not generate, imitate, redraw, approximate, or stylize any
company logo, service logo, app icon, product icon, official mark, mascot,
trademarked symbol, brand color scheme, or real product UI. If brand
identification is required, reserve a clean white clearspace area for a later
official asset overlay. Generic non-branded icons such as folders, arrows,
browser frames, server boxes, abstract nodes, and simple clouds are allowed
only if they do not resemble any real brand asset.
```

公式素材の余白指定が必要なプロンプトでは、次も入れる。

```text
Official asset clearspace: reserve a clean blank white area in the upper right
for a later official lockup overlay. On a 1254x627 canvas, the primary official
lockup should be composited at about 500-520px wide, preserving the official
asset's aspect ratio and built-in clearspace. Do not draw a box, card, label,
badge, border, shadow, glow, placeholder, or icon in that area.
```

## チェックリスト

生成画像を見るときは、次を確認する。

- 公式ロゴ・公式アイコンに似たものが入っていないか。
- ブランドカラーだけで特定サービスに見える表現になっていないか。
- GitHub の Octocat、Copilot アイコン、Gemini の星、OpenAI knot などに見える図形が混ざっていないか。
- アプリ画面やクラウドコンソールの実 UI に見えるものがないか。
- 汎用アイコンが、特定ブランドのサービスアイコンに寄っていないか。

## 既知の注意

- `B-5 GitHub Copilot` は、AI 生成ではロゴもアイコンも描かせず、公式 GitHub 素材を後合成する方針。
- `F-1 JavaScript` はブランド素材回避。JS の黄色いロゴ、React、Node.js、TypeScript などの公式/準公式アイコンは使わない。
- `B-1` から `B-8` のサービス系は、公式素材の確認が終わるまで再生成差し替えしない。
