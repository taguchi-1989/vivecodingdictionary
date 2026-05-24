# 画像生成ポリシー v2 — 改訂ブリーフ ＆ リサーチ TODO

GPT / Gemini Image 等で 1 回目の画像生成を回した結果、いくつか方針を改める必要が出てきた。本ドキュメントは：

- 現状の観察と改訂点の列挙
- 著作権・トレードマークまわりのリサーチ項目
- Codex（あるいは別のエージェント）に渡せる調査ブリーフ

をひとまとめにしたもの。最終的には [drafts/IMAGE_GEN_TODO.md](IMAGE_GEN_TODO.md) を v2 に書き換える前提。

## 1. 改訂ポイント（4 つ）

### 1-1. アスペクト比を広げる

- **現状**: 1:1 正方形で出している
- **問題**: 見開きレイアウトの中で図表エリアは横長（A 系縦書籍判）。1:1 だと縦に押し込まれて高さの収まりが悪い
- **提案**: **16:9** または **3:2**（横長）／メインビジュアル枠は **4:3** がバランス良いはず
- **使い分け案**:
  | 用途 | アスペクト比 | 例 |
  |:--|:--|:--|
  | 見開き左ページ メイン図（Before/After 等） | **4:3 (1200×900)** | F-2 TypeScript の対比図 |
  | 扉・概念図（横ワイド） | **16:9 (1920×1080)** | 章扉のヒーロー |
  | ポンチ絵スロット（人物 1 名） | **1:1 (1024×1024)** | 既存通り、現状維持で可 |
  | 章地図（A-3）等の俯瞰図 | **3:2 (1500×1000)** | ノードを横並びに見せる構成 |

→ プロンプト末尾に `--ar 4:3` や `aspect_ratio: 4:3` を明示すること。

### 1-2. 背景は白（に近い）に統一

- **現状**: グラデーションや薄い色背景になることが多い
- **問題**: 本書は「白地・濃紺・薄青」の 3 色基調が大原則。背景に色が乗ると印刷時にトーンが揃わない／本文との分離が悪い
- **提案**: 全画像で背景を **純白 #FFFFFF** か **極薄青 #F3F6FB** のみに限定
- **プロンプト追加文（共通）**:
  ```
  Pure white background (#FFFFFF) or extremely subtle pale blue (#F3F6FB) at most.
  No gradients, no patterns, no textured backgrounds. Flat editorial style.
  ```

### 1-3. 企業ロゴ・サービスロゴの取り扱い（要リサーチ）

これが一番大きい論点。**現状ロゴをそのまま画像生成させているか、生成 AI が学習した形で混じり込んでいる**可能性があり、権利関係を整理する必要がある。

#### 1-3-1. 法的論点

- **トレードマーク（商標）vs 著作権**: ロゴは多くの場合「商標」として保護される（著作権だけではない）
- **公正使用（フェアユース・名目的使用）**: 米国法では辞書・解説目的の引用は名目的使用（nominative use）として認められる場合がある。**ただし日本法は別**
- **日本の状況**:
  - 著作権法 30 条の 4（AI 学習目的）は学習用には適用可、商用配布物への複製は別
  - 商標法 26 条（指示的使用）: 商品・サービス名を**普通名称的に使う場合**は商標権の効力が及ばない
  - つまり「Claude のロゴ画像」を本に載せる場合、Anthropic の商標として認識される使用は OK だが、ロゴそのものを画像生成で「再現」して載せるのは商標権侵害のリスクあり
- **ブランドガイドライン**: 各社が独自ガイドラインを持つ
  - Anthropic: <https://www.anthropic.com/brand>
  - OpenAI: <https://openai.com/brand>
  - Google: <https://about.google/brand-resource-center/>
  - Microsoft: <https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks>

#### 1-3-2. 取りうる方針（3 択）

| 方針 | 説明 | リスク | おすすめ度 |
|:--|:--|:--|:--:|
| A. **公式ブランド素材を取得して使用** | 各社の brand resource ページから公式 SVG/PNG をダウンロード。ガイドラインに従って利用 | 低（ガイドライン違反でなければ OK） | ★★★ |
| B. **画像生成で「ロゴ風」を再現** | プロンプトで「Anthropic logo」等を指示し AI に描かせる | 高（商標侵害リスク） | ✗ |
| C. **ロゴ不使用・テキストとカラーバー等で代用** | ブランドカラーの帯と社名テキストだけで識別 | 最低 | ★★（最も安全） |

**現実的な落とし所**: **A + C の組み合わせ**。
- メインで言及するサービス（Claude, ChatGPT, Gemini, Cursor, Claude Code 等）は **A 公式素材を使用**
- 言及程度の他社サービスは **C 社名テキスト + カラーバー** で識別

#### 1-3-3. リサーチ TODO（→ Codex に投げる）

```
Codex タスク: 以下の主要企業のブランドガイドラインを調査し、
本書での使用可否を一覧表にまとめてください。

調査対象（B 章 / C 章で登場するもの優先）:
- Anthropic / Claude
- OpenAI / ChatGPT / Codex
- Google / Gemini / Google Cloud
- Microsoft / Copilot / Azure / GitHub
- Meta / Llama
- Anysphere / Cursor
- Windsurf
- Vercel / Next.js
- xAI / Grok
- NVIDIA
- AMD
- DeepSeek / Mistral / Alibaba (Qwen) / Moonshot AI (Kimi)

各社について:
- ブランドガイドラインのURL
- 「教育・解説目的での名称・ロゴ使用」が許可されるか
- ロゴを変形・再着色せず使えるか
- 必要な記載・帰属表示（trademark notation 等）
- 商用書籍への掲載可否

出力形式: docs/brand_usage_audit.md（テーブル形式）
```

### 1-4. 人物造形の一貫性

- **現状**: ロボット・男性・女性キャラクターのデザインがエントリ間で揺れている
- **問題**: 本全体でキャラクターの再現性がなく、別人物のように見える
- **提案**: **共通キャラクター 3 名**を定義してリファレンス画像を作る
  - **キャラクター A**: 「読者」抽象人物（性別・年齢を出さない、線画）
  - **キャラクター B**: 「エンジニア」象徴（メガネ + ノート PC、性別中性的）
  - **キャラクター C**: 「AI」象徴（半透明のヒトガタ + キラめき）
- **再現性確保の方法**:
  - 各キャラの**リファレンス画像 1 枚**を先に確定させる
  - 以降の生成では「Same character as reference_A.png」のように seed/character_reference 機能を使う
  - Midjourney なら `--cref`、Nano Banana なら character consistency 機能、Gemini Image 3 も同様

### 1-5.（追加）団体・グループ画像も出してほしい

- 単独人物だけでなく「3〜4 人で会話している」「会議室で議論」のような団体シーンも出力対象に
- 用途: H 章（歴史）、I 章（MCP / 連携）、開発フロー図
- **アスペクト比**: 横長（16:9 or 3:2）が必須

## 2. 改訂版プロンプトのテンプレート

これを各画像生成タスクの共通プレフィックスに付ける：

```
Style: minimalist editorial line drawing, navy ink (#123E82) on pure white
background (#FFFFFF). Optional accent: extremely pale blue (#F3F6FB) only.
No gradients, no textures, no decorative backgrounds. Generous whitespace,
clean technical book aesthetic. Aspect ratio: {ASPECT_RATIO}.

Characters: Use the established reference characters (A=reader, B=engineer,
C=AI silhouette) maintaining consistent design across all images.

Brand/Logo: Do NOT generate any company logos or trademarked symbols.
Reference companies by text label and brand color only.
```

各タスクで `{ASPECT_RATIO}` を `4:3` `16:9` `3:2` `1:1` から選ぶ。

## 3. Codex に渡す調査タスク（依頼テンプレ）

以下を 1 つの md ファイル `docs/brand_usage_audit.md` として出力してもらう想定：

```
タスク: 商標・著作権ポリシー調査と一覧化

背景:
書籍「バイブコーディング図鑑」(VibeCodingDictionary, CC BY-SA 4.0
公開予定) の本文・図解に企業名・サービス名・ロゴが頻出する。
本書は日本国内での出版・電子配布を想定。商用配布も視野。

調査依頼:
1. 主要 20 社（リスト別添）のブランドガイドライン URL を収集
2. 各社について以下を確認:
   a. 教育・解説目的での名称使用は許可か（必要な帰属表示は？）
   b. ロゴの使用は許可か（変形不可・色変更不可など制約）
   c. 商用書籍（紙＋電子）への掲載可否
   d. 必要な trademark notation の文言例
3. 結果を 1 件 = 1 行のテーブルで docs/brand_usage_audit.md に出力
4. 「不明・要弁護士確認」の項目もそのまま出してよい

調査対象 20 社:
Anthropic / OpenAI / Google / Microsoft / Meta / xAI /
Anysphere(Cursor) / Codeium(Windsurf) / Vercel / Replit /
Devin AI / NVIDIA / AMD / Apple / Amazon (AWS) /
DeepSeek / Mistral AI / Alibaba (Qwen) / Moonshot AI /
Zhipu AI

参考:
- 日本著作権法 30 条の 4（AI 学習）
- 日本商標法 26 条（指示的使用）
- 米国フェアユース・名目的使用法理

期待アウトプット:
docs/brand_usage_audit.md として、各社 1 行のテーブル＋
末尾に「安全な利用方針 3 原則」を箇条書きで。
```

## 4. 著者が決めるべき事項（→ 私からの確認）

| 項目 | 選択肢 | 推奨 |
|:--|:--|:--|
| ロゴ方針 | A 公式素材／C テキスト＋色／A+C 混合 | **A+C 混合** |
| 人物リファレンス枚数 | 1〜3 名（読者・エンジニア・AI） | **3 名** |
| 団体画像 | あり／なし | **あり**（H・I 章で必須） |
| アスペクト比デフォルト | 1:1 維持／4:3 へ移行／用途別 | **用途別**（§1-1 表） |
| 背景制約 | 純白のみ／薄青可／グラデ可 | **純白＋薄青のみ** |
| 商用配布視野 | あり／なし | **あり** ← この前提で全方針を組む |

## 5. 履歴

- 2026-05-24: v2 初版。GPT/Gemini 初回出力レビュー後の改訂方針を集約
