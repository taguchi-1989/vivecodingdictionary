# Codex 依頼ブリーフ — 画像生成ポリシー関連の調査 2 件

このファイルを Codex（または同等のエージェント）に渡してください。
詳しい背景は [drafts/IMAGE_GEN_POLICY_v2.md](IMAGE_GEN_POLICY_v2.md) §6 を参照。

---

## 依頼 1: 主要 20 社のブランドガイドライン調査

### 背景

書籍「バイブコーディング図鑑」(VibeCodingDictionary) を CC BY-SA 4.0 で公開予定。日本国内で**紙書籍出版＋電子配布**、**商用配布あり**を想定。本書には企業名・サービス名・ロゴが頻出するため、各社のガイドラインを確認したい。

### 調査対象（20 社）

| 章 | 企業・サービス |
|:-:|:--|
| B | Anysphere (Cursor) / Codeium (Windsurf) / Vercel / Replit / Devin AI |
| C | Anthropic / OpenAI / Google / Microsoft / Meta / xAI / Apple / Amazon (AWS) |
| C・J | NVIDIA / AMD |
| D | DeepSeek / Mistral AI / Alibaba (Qwen) / Moonshot AI / Zhipu AI |

### 各社について調べる項目（5 つ）

a. **教育・解説目的での名称使用** は許可されているか（必要な帰属表示は？）
b. **ロゴの使用** は許可か（変形不可・色変更不可などの制約は？）
c. **商用書籍（紙＋電子）への掲載可否**
d. **必要な trademark notation** の文言例（例：`Claude™ is a trademark of Anthropic`）
e. **公式ブランドアセット**（SVG/PNG）のダウンロード URL

### 期待アウトプット

`docs/brand_usage_audit.md` に以下の構造で出力：

```markdown
# ブランド利用可否監査

| 社名 | サービス | ガイドライン URL | 名称使用 | ロゴ使用 | 商用書籍 | trademark 表記 | 公式アセット URL | 備考 |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| Anthropic | Claude | ... | ⭕ 帰属表示要 | ⭕ 変形不可 | ⭕ | "Claude™ ..." | ... | ... |
| ...
```

### 末尾に追記してほしい「安全な利用方針 3 原則」

調査結果から導かれる、本書での共通運用原則 3 つを箇条書きで（例：「ロゴは原寸・原色で使用」「初出に商標表記を入れる」「商用配布時は各社サイトで最新ガイドラインを再確認」）。

### 参考にすべき法的フレームワーク

- 日本著作権法 30 条の 4（AI 学習目的の利用）
- 日本商標法 26 条（指示的使用）
- 米国フェアユース・名目的使用法理（参考）

### 補足

「不明・要弁護士確認」項目もそのまま出してください。出せなかった列は `—` で。

---

## 依頼 2: 画像生成ツールのアスペクト比上限の実測

### 背景

本書の図解は**横長レイアウト**（最大 21:9）で出したい。複数の画像生成ツールで、実際に対応できる最大アスペクト比を確認したい。

### 調査対象ツール（6 つ）

- Gemini Image (Imagen 4)
- Nano Banana (Gemini 2.5 Flash Image)
- GPT Image (gpt-image-1)
- Midjourney v7
- Flux.1 Pro
- Stable Diffusion 3.5

### 各ツールについて調べる項目（4 つ）

a. **公式ドキュメントで宣言されている対応アスペクト比一覧**
b. **「21:9」「16:9」「3:2」「4:3」のリクエストが通るか**
c. **実際に同じプロンプトで 21:9 / 16:9 / 4:3 / 1:1 を出してみて、品質が破綻するアスペクト比はどこか**（実測）
d. **API 料金 / 商用利用条件**

### テスト用プロンプト（共通で使う）

```
A small humanoid pet robot standing next to a male teacher figure and
a female reader figure, all rendered as a minimalist line drawing in
deep navy ink (#123E82) on pure white background. No gradients, no
textures, generous whitespace. Three characters arranged side by side.
```

### 期待アウトプット

`docs/image_tool_audit.md` に以下の構造で出力：

```markdown
# 画像生成ツール比較（アスペクト比と商用利用）

| ツール | 宣言値 | 21:9 | 16:9 | 3:2 | 4:3 | 1:1 | 商用利用 | 1 枚あたり料金 | 備考 |
|:--|:--|:-:|:-:|:-:|:-:|:-:|:--|:--|:--|
| Gemini Image | 1:1 / 16:9 / 4:3 / 3:4 / 9:16 | ❌ | ✓ | △ | ✓ | ✓ | OK | $0.04 | ... |
| ...

## 本書での推奨ツール
- 1 候補に絞って理由を 3 行で
```

### 補足

実画像を生成して比較する場合は、画像も `docs/image_tool_samples/` 配下に保存しリンクしてください。

---

## まとめ

両依頼とも、最終アウトプットは `docs/` 配下の md ファイルにしてください。完了したら main にコミット＆ push、もしくは PR を上げてください。

著者の決定（配色は青の濃淡のみ、3 キャラ固定、団体画像あり）は本書全体の方針なので、調査時にもこの前提を踏まえて評価してください。

---

参考リポジトリ: <https://github.com/Taguchi-1989/ViveCodingDictionary>
ライセンス: コード MIT / 本文 CC BY-SA 4.0
