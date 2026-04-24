---
id: B-1
title: Gemini
category: service
subtype: ai_assistant
experience_level: research_only
reader_level: 2
figure_type: structure
page_layout: spread_v1
start_date: 2024-02
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-24
related_terms:
  - Google DeepMind
  - Gemini 2.5 系
  - Bard → Gemini
  - Vertex AI
  - Google Workspace
  - AI Studio
status: needs_review
---

# Gemini

## tagline

Google が提供する AI アシスタントのブランドです。2024 年に Bard から改名しました。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## ひとことで

Gemini は、Google が作る AI アシスタントのブランド名です。ウェブ版のチャット、Android の標準 AI、Google Workspace 統合、開発者向け API まで、複数の入口を持ちます。中身は Gemini 2.5 系（2026-04 時点）のモデル群です。

## 何をしてくれるか

自然言語で話しかけると、文章の要約・調査・ドラフト作成・コード生成・画像理解・音声入出力などを返してくれます。同じ「Gemini」でも、**入口で体験が違います**。

主な入口は 4 つです。

- **gemini.google.com** — ブラウザで使う無料チャット（Pro プランで上位モデルに拡張）
- **Android の標準 AI アシスタント** — スマホの Google アシスタントが Gemini に置き換わった状態
- **Google Workspace 統合** — Gmail、Docs、Sheets、Slides などで「横に AI がいる」体験
- **開発者向け API** — 素の API 窓口の **AI Studio** と、業務利用向けの **Vertex AI**（Google Cloud 経由）

モデルのラインナップは、**Pro（最も賢い）／ Flash（中間）／ Flash-Lite（軽量）** の 3 段階が基本です。Claude の Opus／Sonnet／Haiku とほぼ対応するマッピングで覚えられます。

長文処理に強みがあります。100 万トークン超の Context Window（文脈に入れられる量）を実用化した最初のサービスで、「大きな資料をそのまま投げて要約させる」用途で一歩抜け出したと評されています。

## バイブコーディングでの位置づけ

Claude と並ぶ主役級のサービスです。企画者は Workspace の Docs／Gmail で下書き支援に、開発者は Vertex AI で業務システム組み込みに、個人は Android の標準 AI として、と使い手ごとに別の顔を見せます。

「Gemini を使っている」と言ったとき、**どの入口の話か**を揃えると会話が噛み合いやすくなります。ウェブ版のチャットと、Vertex AI での業務利用では、同じモデル名でも使い手も料金もまったく違います。

Google Workspace を組織で使っている場合、**特別な導入なしで Gemini がすでに手元にある**ことがあります。打ち合わせで「AI 使ってる？」と聞かれたら、Gmail や Docs の画面で銀色の星マーク（Gemini アイコン）が出ているか確認してみると発見があります。

## メイン図

### 図の狙い

中央に「Gemini」ブランドを置き、4 つの入口（チャット／Android／Workspace／API）と、それぞれの使い手を 1 枚に収めます。「同じ Gemini が、誰の手元でどう見えるか」を足場にします。

### B. 登場シーン（figure_type: structure）

- シーン1: 個人ユーザーが gemini.google.com で日常の質問や資料要約 — 「昨日のニュースまとめて」
- シーン2: 企画者が Workspace の Docs／Gmail で下書き支援 — 「この議事録、要約して」
- シーン3: 開発者が AI Studio ／ Vertex AI でアプリに組み込み — 「問い合わせを自動分類したい」
- シーン4: Android ユーザーが標準 AI に話しかける — 「明日 7 時にアラーム」
- 並べる基準: 使う人の立場別（個人 ／ 企画 ／ 開発 ／ スマホ常用）

## 関連用語

- Google DeepMind — Gemini を作っている組織（C-3）
- Gemini 2.5 系 — 現行のモデル世代（D-2）
- Bard → Gemini — 2024-02 の改名の歴史（H-50）
- Vertex AI — Google Cloud 上で Gemini を業務利用する窓口（B-27）
- Google Workspace — Docs／Gmail への統合入口
- AI Studio — Google の開発者向け API 窓口

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Google 製の汎用 AI アシスタント・ブランドです。個人／業務／開発の全方位に入口があります。

### 2. うれしさ

Google Workspace と深く統合され、Docs／Gmail の中で自然に呼べます。長文処理にも強みがあります。

### 3. 注意点

サービス名・モデル名・API 窓口が同じ「Gemini」の下に並ぶので、どの話かを確認しないと会話がずれます。

### 4. どこで役立つか

会議メモの要約、大きな PDF の読み込み、Android での音声操作、Google Cloud での業務組み込み。

### 5. 最初に理解する範囲

4 つの入口（チャット／Android／Workspace／API）と、Pro／Flash／Flash-Lite の 3 段階です。

### 6. 深掘り先

Gemini 2.5 系の世代差、Vertex AI、AI Studio、Google Workspace の個別機能、Context Window の扱い。

## 開発フローでの位置（必須）

1. 目的を決める — 個人の調べ物／業務文書／アプリ実装のどれか
2. 入口を選ぶ — gemini.google.com ／ Workspace ／ AI Studio ／ Vertex AI
3. モデルを選ぶ — Pro（重い仕事）／Flash（日常）／Flash-Lite（軽量大量）
4. 実行 → 結果を評価し、必要なら入口やモデルを切り替え

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニア視点のつまずき

-
-
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:
- 👍 良い点:
- 👎 ダメな点:
- 🎯 誰に向くか:

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Gemini」のノード（銀色の星マーク）。4 方向に枝が伸び、4 人のキャラクターに繋がる。各キャラの周りに入口を示すアイコン（ブラウザ／Android スマホ／Docs＋Gmail ／クラウド）
- 登場人物: 個人ユーザー（ノート PC で検索）／企画者（Docs／Gmail 画面を操作）／開発者（ターミナル＋クラウドコンソール）／Android ユーザー（スマホに話しかける）
- 吹き出し・心の声: 各人 1 行ずつ（「昨日のニュースまとめて」「議事録要約して」「問い合わせ自動分類したい」「7 時アラーム」）
- 中央に置くキーワード/ラベル: Gemini ＝ 4 つの入口を持つブランド
- シーン比較のポイント: 同じ AI を、それぞれの立場と機器でどう呼ぶか

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: 目的アイコン（標的）
- Step 2: 4 つの入口アイコン（ブラウザ／Android／Docs＋Gmail／クラウド）を並べる
- Step 3: 3 バッジ（Pro／Flash／Flash-Lite）
- Step 4: 評価アイコン（目＋チェック）＋切替の矢印
- 矢印: 目的 → 入口選択 → モデル選択 → 評価・切替 のループ

## コミュニティ補完メモ

- Gemini 2.5 系のモデル詳細（Pro ／ Flash ／ Flash-Lite の個別仕様）は D-2 Gemini 2.5 系で扱います
- Bard からの改名経緯は H-50 Bard → Gemini で時系列扱い
- Vertex AI は B-27 で独立エントリ
- Google Workspace の個別機能（Gemini in Gmail、Gemini in Docs など）は別エントリ候補
- 本エントリは「Gemini というブランド全体の見取り図」に絞ります

## 出典メモ

- gemini.google.com — checked 2026-04-24
- deepmind.google/technologies/gemini — checked 2026-04-24
- cloud.google.com/vertex-ai — checked 2026-04-24
- blog.google（Bard → Gemini の改名告知、2024-02）— checked 2026-04-24

## 備考

- モデル世代・料金・提供状況は時変情報です。evaluation_date を必ず持たせます
- 料金プランは B-52 Gemini の料金プランを参照
- 旧 3 桁 ID の `content/entries/service/101_gemini.md` は新テンプレ移行に伴い `status: archived` に落とします（素材として本エントリに取り込み済み）
