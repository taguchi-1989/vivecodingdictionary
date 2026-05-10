---
id: B-16
title: Microsoft 365 Copilot
title_reading: マイクロソフト サンロクゴ コパイロット
category: service
subtype: ai_assistant
experience_level: hands_on
reader_level: 2-3
importance: B
figure_type: structure
page_layout: spread_v1
start_date: 2023-11-01
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-04-30
related_terms:
  - Microsoft Copilot
  - Microsoft
  - GitHub Copilot
  - Azure
status: ready
---

# Microsoft 365 Copilot

<!-- バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠） -->

## tagline

Word・Excel・Teams などに組み込まれた業務統合 AI です。月額 $30 の有料追加サービスになります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Microsoft 365 の各アプリ内で AI が動きます。Word でドラフト・要約、Excel で関数提案・分析、PowerPoint でスライド生成、Outlook でメール下書き、Teams で会議要約ができます。

## どこで出会うか

Microsoft 365 を使う職場で「Copilot を契約した」と案内された時が出会いです。Microsoft Graph で自社メールやファイルを参照する点が無料 B-15 との違いです。

## メイン図

### 図の狙い

「Microsoft 365 の各アプリの中に AI が入っている」構造を、アプリと Copilot の関係図で示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Microsoft 365 Copilot
- 周辺の要素（4個）: Word ／ Excel ／ PowerPoint ／ Teams
- 関係の描き方: 中央の Copilot から各アプリへ矢印が伸びる放射状

## 会話での使い方例

「Excel の Copilot で売上を分析して、PowerPoint で資料化までやらせました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Microsoft 365 アプリに組み込まれた業務向け AI アシスタントです。

### 2. うれしさ

使い慣れた Office アプリのまま AI 支援が受けられます。

### 3. 注意点

無料の Microsoft Copilot（B-15）とは別サービスで、月額 $30 が追加でかかります。

### 4. どこで役立つか

会議要約・スライド作成・メール下書きなど日常業務の自動化に向きます。

### 5. はじめに

「業務アプリ統合の有料版 Copilot」と認識すると B-15 との混乱が避けられます。

### 6. 深掘り先

Microsoft Copilot、Microsoft Graph、Azure

## 開発フローでの位置（必須）

1. 情報収集 — Teams の会議録を Copilot に要約させ、要点を整理する
2. 分析 — Excel で売上データを渡し、関数提案と傾向分析を依頼する
3. 資料作成 — PowerPoint に「スライド自動生成」を指示してたたき台を作る
4. 仕上げ・送付 — Outlook でメール下書きを生成し、内容を確認して送信する

## 関連用語

- Microsoft Copilot
- Microsoft
- GitHub Copilot
- Azure

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- はっきり言って詐欺だと思いました。機能としてはあるけれど使えたものではないのに、「できます」と謳ってニュースケースを出しているのは企業として問題があると感じます。特に2023年から2025年にかけての状況は詐欺と言っても過言ではないと思いました。
- 
- 

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: これは詐欺ではないかと思いました。
- 👍 良い点: 特にないと思います。
- 👎 ダメな点: 問題が多すぎて全てかもしれませんが、はっきり言って時代遅れすぎます。
- 👥 誰向けか: AI リテラシーがほとんどない方向けかなと思います。


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Microsoft 365 Copilot」のロゴを置き、Word・Excel・PowerPoint・Teams の 4 つのアプリアイコンに矢印が伸びる放射状の構造図
- 登場人物（いれば）: オフィスワーカー風の人物が Excel 画面を見ながら Copilot を呼び出している
- 吹き出し・心の声: 「会議の要約まで自動でやってくれるの？」
- 中央に置くキーワード/ラベル: Microsoft 365 Copilot

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: マイク（会議・要約）
- Step 2 のアイコン/絵柄: グラフ（データ分析）
- Step 3 のアイコン/絵柄: スライド（資料作成）
- Step 4 のアイコン/絵柄: 封筒（メール送付）
- 矢印で示す流れの意図: 「集めて → 分析して → 資料化して → 送る」という業務フロー

## コミュニティ補完メモ

- B-15（Microsoft Copilot）との住み分け：B-15 は無償の汎用チャット版（Windows・Edge から使える）。B-16 は Word・Excel・Teams 等の Microsoft 365 アプリ内に統合された有料版（月額 $30 追加）。Microsoft Graph によるテナント内データ参照ができるかどうかが分かれ目
- B-5（GitHub Copilot）との住み分け：B-5 はコードエディタ内の補完特化。B-16 は Office 系アプリの業務タスク全般が対象
- B-25（Azure）との関係：B-16 の基盤インフラは Azure が担う。エンタープライズのデータ管理・セキュリティポリシーは Azure AD / Microsoft Entra と連動する
- C-8（Microsoft）との関係：企業・会社としての Microsoft のエントリ。B-16 はその主要 AI サービスの 1 製品

## 出典メモ

- <https://www.microsoft.com/ja-jp/microsoft-365/copilot/microsoft-365-copilot> — checked 2026-04-30
- <https://blogs.microsoft.com/blog/2023/11/01/introducing-microsoft-365-copilot-your-copilot-for-work/> — checked 2026-04-30

## 備考

- 2023-11: 企業向け（Microsoft 365 E3/E5 保有の 300 ユーザー以上）に提供開始
- 2024-01: 小規模事業者・個人事業主向けにも開放（最低ユーザー数制限の撤廃）
- 価格：ユーザーあたり月 $30（Microsoft 365 E3/E5 等の有償プランに追加で購入）（evaluation_date: 2026-04-30 時点の情報。変動可能性あり）
- Microsoft Graph 経由でテナント内のメール・予定表・ファイルにアクセスして回答を生成する点が無料版との最大の差分
- Copilot Studio によるカスタムエージェント拡張も可能だが、本エントリの範囲外
