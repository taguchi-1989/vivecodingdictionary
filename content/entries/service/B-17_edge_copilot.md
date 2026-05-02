---
id: B-17
title: Edge Copilot
title_reading: エッジ コパイロット
category: service
subtype: ai_assistant
experience_level: hands_on
reader_level: 1-2
importance: C
figure_type: comparison
page_layout: spread_v1
start_date: 2023-02-01
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Microsoft Copilot
  - Microsoft 365 Copilot
  - ChatGPT
  - DALL·E
status: needs_review
---

# Edge Copilot

<!-- バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠） -->

## tagline

Edge ブラウザに組み込まれた AI サイドバーです。いま開いているページをそのまま AI に渡せます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

表示中のページの要約・翻訳・質問応答のほか、Compose タブで文章の下書きや画像生成（DALL·E 3）も行います。ブラウザを閉じずに AI 補助が完結するのが特徴です。

## どこで出会うか

Edge 右上のサイドバーアイコンをクリックするか、テキストを選択して右クリックすると呼び出せます。Microsoft Copilot（B-15）の入口の 1 つで、実態は同じモデルが動いています。

## メイン図

### 図の狙い

「Edge サイドバーからそのまま AI に聞ける」という操作の流れを、ブラウザ画面と会話の対比で示す。

### B. 登場シーン（figure_type: comparison）

- シーン1: ニュース記事を開いたままサイドバーで「この記事を 3 行で要約して」と送る
- シーン2: 英語ページを表示中に「日本語に訳してポイントを教えて」と依頼する
- シーン3: Compose タブで「この内容でメール下書きを作って」と入力して文章を生成する
- 並べる基準: ブラウジング中に生じるニーズの種類（理解／翻訳／作成）

## 会話での使い方例

「Edge のサイドバーで Copilot に開いたままの記事を要約させました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Edge に内蔵された AI サイドバーで、ページ内容を渡せます。

### 2. うれしさ

タブ切り替えなしにページ要約・翻訳・文章生成が完結します。

### 3. 注意点

実態は Microsoft Copilot（B-15）で、Edge 専用の独立モデルではありません。

### 4. どこで役立つか

Web 調査中に内容を即整理したい場面で効果が出やすいです。

### 5. はじめに

「Edge の入口から使う Copilot」と理解するとブランド整理がしやすいです。

### 6. 深掘り先

Microsoft Copilot、Microsoft 365 Copilot、ChatGPT

## 開発フローでの位置（必須）

1. 情報収集 — Edge で参考記事を開き、サイドバーで要点を即要約させる
2. 内容理解 — 英語ドキュメントをその場で翻訳・質問して理解を深める
3. 文章下書き — Compose タブでメールや報告書の下書きをその場で生成する
4. 確認・共有 — 生成したテキストをそのままコピーして資料や返信に使う

## 関連用語

- Microsoft Copilot
- Microsoft 365 Copilot
- ChatGPT
- DALL·E


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- 入力内容が学習に使われるか分かりづらく、業務情報を入れてよいか毎回迷います（既定はオン、設定でオフにできます）
- 賢さ自体は最新のフロンティアモデルに届かず、込み入った相談だと回答が浅く感じます
- 会話の文脈をうまく持ち越してくれないため、続きを聞こうとするたびにゼロから経緯を説明し直す必要があります

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: Bing Image Creator の時代に触ったとき、ブラウザでここまで遊べるのかとすごいと思いました
- 👍 良い点: 無料で誰でもすぐに触れる手軽さです
- 👎 ダメな点: 賢さは最新モデルに比べると物足りなく感じます
- 👥 誰向けか: お金を絶対にかけたくない無課金ユーザー向けです


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: Edge ブラウザの画面右側に AI サイドバーが開いている状態。左にニュース記事、右にサイドバーの要約結果を並べる
- 登場人物（いれば）: デスクに座るオフィスワーカーが画面を見ながら「ここで要約できるんだ」と気づいた表情
- 吹き出し・心の声: 「タブ切り替えなしに記事を整理できました。」
- 中央に置くキーワード/ラベル: Edge サイドバー ＋ Copilot
- Before / After の場合の対比ポイント: 比較型なので不要

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（情報収集）
- Step 2 のアイコン/絵柄: 地球儀（翻訳・内容理解）
- Step 3 のアイコン/絵柄: 鉛筆（文章下書き）
- Step 4 のアイコン/絵柄: 共有矢印（確認・共有）
- 矢印で示す流れの意図: 「調べて → 理解して → まとめて → 渡す」というブラウジングから成果物への流れ


## コミュニティ補完メモ

- B-17（本エントリ）と B-15 Microsoft Copilot の住み分け：B-17 は Edge ブラウザという特定の入口に焦点を当てたエントリ。B-15 は Windows・スマホ・Edge すべてを包括する汎用サービス。「Edge から呼ぶ Copilot」の操作感を説明したいときは B-17、Copilot ブランド全体を説明したいときは B-15 を参照
- B-16 Microsoft 365 Copilot との住み分け：B-16 は Word・Excel・Teams などの業務アプリに統合された有料版。B-17 はブラウザ上での無料利用が中心
- B-3 ChatGPT との住み分け：ChatGPT は専用サービスへのアクセスが必要。Edge Copilot はブラウザ起動だけで呼び出せる点が異なる

## 出典メモ

- <https://www.microsoft.com/ja-jp/edge/features/copilot> — checked 2026-04-30
- <https://blogs.microsoft.com/blog/2023/09/21/announcing-microsoft-copilot-your-everyday-ai-companion/> — checked 2026-04-30

## 備考

- 2023-02: Bing Chat として Edge サイドバーに実装（GPT-4 ベース）
- 2023-11: Microsoft Copilot に統合・改名。「Edge Copilot」は通称として残存
- Edge の「ワークスペース」「コレクション」と組み合わせると、保存済みページを横断して Copilot に質問できる機能がある（2026-04-30 時点で提供状況は地域により異なる可能性あり）
- 料金は Microsoft Copilot（B-15）と同様。無料利用あり、Copilot Pro で機能拡張
