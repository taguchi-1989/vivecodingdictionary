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
