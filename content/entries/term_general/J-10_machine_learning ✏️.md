---
id: J-10
title: Machine Learning
title_reading: マシンラーニング
category: term_general
subtype: ml_basic
experience_level: research_only
reader_level: 2
importance: B
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-04-29
related_terms:
  - Deep Learning
  - Neural Network
  - LLM
  - AI
  - 教師あり学習
status: needs_review
---

# Machine Learning

## tagline

データからパターンを自動で学ぶ AI の手法で、ルールを人が書かない点が特徴です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

データを与えると、コンピューターが統計的なパターンを自動で見つけます。画像識別・スパム分類・価格予測など、ルールを書かなくても「経験から学ぶ」仕組みです。

## どこで出会うか

「AI を導入した」という話の多くが Machine Learning の応用です。Deep Learning（J-11）や LLM（J-14）は下位概念にあたり、「AI > Machine Learning > Deep Learning > LLM」の入れ子で整理すると全体像が見えます。

## メイン図

### 図の狙い

「AI > Machine Learning > Deep Learning > LLM」の入れ子構造を 1 枚で示し、Machine Learning が AI 全体の中でどの層に位置するかを掴んでもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Machine Learning（データから自動学習する手法の総称）
- 周辺の要素: AI（外枠）/ Machine Learning（中枠）/ Deep Learning（内枠）/ LLM（最内枠）/ 教師あり・教師なし・強化学習（Machine Learning 内に分類ラベル）
- 関係の描き方: 入れ子の同心四角形で包含関係を表現。外側が広義、内側が特化

## 会話での使い方例

「Machine Learning はデータから学ぶ手法で、Deep Learning もその一種です」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

データからパターンを学び、新しい入力に対して予測や分類を行います。

### 2. うれしさ

ルールを手書きしなくても、データさえあれば自動でモデルが育ちます。

### 3. 注意点

学習データの質と量が結果を左右し、偏ったデータでは偏った予測になります。

### 4. どこで役立つか

画像認識・需要予測・スパム検出など、パターンが複雑なタスクに向いています。

### 5. はじめに

「ルールベースとの違い」と AI の入れ子構造の中の位置づけが出発点です。

### 6. 深掘り先

Deep Learning（J-11）、Neural Network（J-12）、LLM（J-14）

## 開発フローでの位置（必須）

1. 課題の定義 — 何を予測・分類したいかを決め、必要なデータを洗い出します。
2. データの準備 — 収集・クリーニングを行い、学習用と検証用に分けます。
3. モデルの選択と学習 — アルゴリズムを選び、データを与えてパターンを学ばせます。
4. 評価と改善 — 精度を測り、データ追加やパラメータ調整でモデルを磨きます。

## 関連用語

- Deep Learning
- Neural Network
- LLM
- AI
- 教師あり学習

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

-
-
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:
- 👍 良い点:
- 👎 ダメな点:
- 👥 誰向けか:

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 同心四角形で「AI（最外）> Machine Learning > Deep Learning > LLM（最内）」の入れ子。Machine Learning の枠内には「教師あり学習」「教師なし学習」「強化学習」の 3 ラベルを小さく配置
- 登場人物: 図の横に非エンジニアの人物が指さして「LLM ってここにいるんだ」と気づくシーン
- 吹き出し・心の声: 「データを渡すだけで勝手に学んでくれるの？」
- 中央に置くキーワード/ラベル: Machine Learning（データから自動で学ぶ）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 的（ターゲット）アイコン（課題定義）
- Step 2 のアイコン/絵柄: データベース・表アイコン（データ準備）
- Step 3 のアイコン/絵柄: 歯車＋グラフアイコン（学習）
- Step 4 のアイコン/絵柄: 目盛り・チェックアイコン（評価と改善）
- 矢印で示す流れの意図: 課題 → データ → 学習 → 評価のサイクル

## コミュニティ補完メモ

- AI（J-1 スケルトン）との住み分け：J-1 は AI 全般の概念。J-10 は「データから自動学習する手法」に絞り、「ルールベースとの違い」に重点を置く。
- Deep Learning（J-11）との住み分け：J-11 は Neural Network を多層化した特定手法。J-10 は教師あり・教師なし・強化学習を含む上位概念として扱う。
- Neural Network（J-12）との住み分け：J-12 は神経回路模倣モデルの仕組み説明。J-10 はそれを包む手法の総称。
- LLM（J-14）との住み分け：J-14 はテキスト生成の応用視点。J-10 はその土台となる学習パラダイムの説明。
- 教師あり / 教師なし / 強化学習の詳細分類は J-10 では概念の名前出しに留め、個別エントリ（未定）で深堀りする。

## 出典メモ

- Bishop, "Pattern Recognition and Machine Learning", Springer (2006) — checked 2026-04-29
- Mitchell, "Machine Learning", McGraw-Hill (1997) — checked 2026-04-29
- Google Machine Learning Crash Course, developers.google.com/machine-learning/crash-course — checked 2026-04-29

## 備考

- Machine Learning は略称・ヌメロニムではないため、tagline 冒頭に略称展開は不要。title_reading は「マシンラーニング」（英単語をカタカナで並べた読み）。
- 「教師あり学習」「教師なし学習」「強化学習」の 3 分類は誌面に名前だけ出し、詳細は別エントリへ委ねる。
- ルールベースシステムとの比較（if-then ルールを手書きする方法との対比）は「何をしてくれるか」の「ルールを人が書かない」という一句に圧縮した。詳細はコミュニティ補完メモ参照。
