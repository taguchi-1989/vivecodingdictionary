---
id: E-34
title: OSWorld
title_reading: オーエスワールド
category: benchmark
subtype: agent
experience_level: research_only
reader_level: 4-5
importance: E
figure_type: comparison
page_layout: spread_v1
start_date: 2024-04-01
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - WebArena
  - GAIA
  - AgentBench
  - VLM
status: needs_review
---

# OSWorld

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
- 左ページ：読者が初めて読む側。短い段落で物語的に書く。
- 右ページ：辞書引き側。6視点の見どころ → つまずき／私のコメント → 開発フロー → 関連用語 → 参考 URL。
-->

## tagline

OS 全体を操作できるかを測るエージェント向けベンチマークです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

2024 年 4 月公開のベンチマークで、実 OS 環境で 369 タスクの到達度を測ります。スクリーンショットを入力してキーやマウス操作で答える形が特徴です。

## どこで出会うか

Computer Use の性能比較記事で登場します。公開時は GPT-4V 約 12% に対し人間 約 72% でしたが、Computer Use や Operator の登場でスコアが伸びています。

## メイン図

### 図の狙い

スコア比較によって「AI が人間の操作にどれだけ近づいているか」を一目で伝える。

### B. 登場シーン（figure_type: comparison）

- シーン1: 研究者が AI エージェントの新バージョンを公開し、OSWorld スコアで他モデルと比較する
- シーン2: AI ツール選定時に「OSWorld 何%か」を確認し、デスクトップ操作の信頼性を判断する
- シーン3: ブログ記事で Computer Use 系の進歩を振り返る際、スコア推移の根拠として引用される
- 並べる基準（モデル別スコア比較）:


## 会話での使い方例

「OSWorld で Computer Use が 30% を超え、Operator と接戦している印象です。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

OS 全体の操作を 369 タスクで定量評価します。

### 2. うれしさ

「画面を見て操作する AI」の進歩を数値で追えます。

### 3. 注意点

VLM 版とテキストのみ版でスコアが異なり、比較条件を揃える必要があります。

### 4. どこで役立つか

Computer Use 系ツール選定の参考指標として役立ちます。

### 5. はじめに

369 タスク・実 OS 環境・スクリーンショット入力の 3 点が要点です。

### 6. 深掘り先

WebArena、AgentBench、VLM


## 開発フローでの位置（必須）

1. モデル選定 — Computer Use 機能を持つモデルの OSWorld スコアを比較する
2. 環境構築 — Ubuntu・Windows・macOS の実環境またはスナップショットを用意する
3. タスク実行 — スクリーンショットを入力し、キー・マウス操作を出力させる
4. スコア集計 — 369 タスクの正答率を算出し、他モデルや人間スコアと対照する


## 関連用語

- WebArena
- GAIA
- AgentBench
- VLM


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
-
-
-
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象:
- 👍 良い点:
- 👎 ダメな点:
- 👥 誰向けか:
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 棒グラフ形式でモデル別スコアを並べる（GPT-4V 12% / Claude Computer Use / Operator / 人間 72%）
- 登場人物: 研究者が画面を指差しながら「ここまで来た」と驚く姿
- 吹き出し・心の声: 「人間 72%、AI 30% 超えてきた」「OS ごと操作できるって本当？」
- 中央に置くキーワード/ラベル: 「OSWorld スコア比較」
- Before / After の場合の対比ポイント: 2024 年公開時（12%）→ 2025 年（30% 超）の推移

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: スコア表を見る人物
- Step 2 のアイコン/絵柄: Ubuntu・Windows・macOS のロゴ 3 つ
- Step 3 のアイコン/絵柄: スクリーンショット → AI → マウス/キーボード の流れ図
- Step 4 のアイコン/絵柄: 正答率グラフ
- 矢印で示す流れの意図: 「選定 → 環境 → 実行 → 評価」の一巡が分かるよう左から右へ

## コミュニティ補完メモ

- WebArena（E-31）との住み分け：WebArena はブラウザ内タスクに特化。OSWorld はファイル操作・アプリ起動・GUI 操作まで含む OS 全体が対象で、スコープが広い。
- AgentBench（E-33）との住み分け：AgentBench は OS・DB・Web など複数環境の総合評価。OSWorld は実 OS のデスクトップ操作に絞った専門ベンチマーク。
- GAIA（E-32）との住み分け：GAIA は複数ツールを組み合わせた汎用タスク。OSWorld は GUI 操作・スクリーンショット入力に特化。
- VLM（J-15）版とテキストのみ版の差異は備考に記載。


## 出典メモ

- OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments (arXiv 2404.07972) — checked 2026-04-30
- Anthropic Computer Use 発表 (2024-10) — checked 2026-04-30


## 備考

- VLM（Vision Language Model）使用版とテキストのみ版では条件が異なるため、同一条件での比較が重要。スコア引用時は「VLM 版スコア」かどうかを確認すること。
- GPT-4V スコア約 12%・人間スコア約 72% は公開時（2024 年 4 月）のデータ。Anthropic Computer Use（2024 年 10 月）・OpenAI Operator（2025 年）登場後にスコアが大幅に伸びており、evaluation_date 時点の最新値は個別に要確認。
