---
id: J-11
title: Deep Learning
title_reading: ディープラーニング
category: term_general
subtype: ml_basic
experience_level: research_only
reader_level: 3
importance: B
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-04-29
related_terms:
  - Machine Learning
  - Neural Network
  - Transformer
  - LLM
  - GPU
status: ready
---

# Deep Learning

## tagline

多層のニューラルネットワークによる機械学習の手法で、現代の LLM の土台です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

大量のデータからパターンを自動で学習します。人間が特徴を設計しなくても、層を重ねた Neural Network が画像・音声・テキストの特徴を段階的に抽出します。

## どこで出会うか

AI ツールや研究紹介記事で「Deep Learning モデルを使っています」という形で頻出します。LLM（J-14）や画像生成 AI の仕組みを調べると必ず登場します。

## メイン図

### 図の狙い

Machine Learning という大きな枠の中に Deep Learning があり、その中核に Neural Network の多層構造があることを入れ子の図で示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Neural Network の多層構造（入力層 → 隠れ層 × 複数 → 出力層）
- 周辺の要素: Machine Learning（包含の外枠）、Deep Learning（中間枠）、LLM / 画像認識（応用例）、GPU（計算基盤）
- 関係の描き方: 同心の入れ子円（Machine Learning ⊃ Deep Learning ⊃ Neural Network）と右側に応用例の矢印

## 会話での使い方例

「LLM も Deep Learning の一種で、多層の Neural Network が言語を学びます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Machine Learning の中で、多層構造により複雑なパターンを学ぶ手法です。

### 2. うれしさ

特徴量の設計を人間が行わなくて済み、精度が大幅に上がります。

### 3. 注意点

大量のデータと GPU 計算資源が要り、学習コストが高めです。

### 4. どこで役立つか

LLM・画像認識・音声認識など、現代 AI の主要タスクに広く使われます。

### 5. はじめに

「層を重ねるほど複雑な特徴を掴める」という直感だけで十分です。

### 6. 深掘り先

Neural Network（J-12）、Transformer（J-13）、GPU（J-77）

## 開発フローでの位置（必須）

1. データを集める — 画像・テキスト・音声など大量の学習データを用意します。
2. モデル構造を選ぶ — 層数やアーキテクチャを目的に合わせて決めます。
3. GPU で学習する — Neural Network の重みをデータから繰り返し更新します。
4. 評価・調整する — 精度を測り、層の深さや学習率を調整します。
5. 推論に使う — 学習済みモデルを LLM や画像認識ツールとして呼び出します。

## 関連用語

- Machine Learning
- Neural Network
- Transformer
- LLM
- GPU

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- 多層化で重み調整が難しく、説明不可能性が残る点が悩ましくもあり魅力でもあります

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: AlphaGo のあたりで初めて存在を認識しました
- 👍 良い点: 人間のバイアスを超えていける場面が出てくる点が面白いです
- 👎 ダメな点: 説明不可能性が残り、標準業務での再現性・説明性に不安があります
- 👥 誰向けか: 強モデルを目指す人や AI 史の主軸として押さえたい人向けです

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 同心の入れ子円。最外円に「Machine Learning」、中円に「Deep Learning」、内円に「Neural Network（多層）」。右側に LLM・画像認識・音声認識の応用例アイコンを矢印で接続。
- 登場人物: 非エンジニアの人物が入れ子図を指差し「層を重ねるほど賢くなるんだ」と驚くシーン
- 吹き出し・心の声: 「特徴を自分で設計しなくていいの？」「層が深いほどパターンが細かく掴める」
- 中央に置くキーワード/ラベル: Neural Network（多層構造）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: データの山（学習データ収集）
- Step 2 のアイコン/絵柄: 積み重なった層のアイコン（モデル構造選択）
- Step 3 のアイコン/絵柄: GPU チップアイコン（学習）
- Step 4 のアイコン/絵柄: チューニングダイヤル（評価・調整）
- Step 5 のアイコン/絵柄: API コールの矢印（推論利用）
- 矢印で示す流れの意図: データ → 設計 → 学習 → 改善 → 活用のサイクル

## コミュニティ補完メモ

- Machine Learning（J-10）との住み分け：J-10 は機械学習全体の概念。J-11 は「多層ニューラルネット」という具体手法に絞る。
- Neural Network（J-12）との住み分け：J-12 はニューラルネットの構造そのもの。J-11 は「それを深く積んだ手法」という位置づけ。
- Transformer（J-13）との住み分け：J-13 は Deep Learning の特定アーキテクチャ（2017 年以降の主流）。J-11 はその土台概念として、Transformer が Deep Learning の一形態であることを示す。
- LLM（J-14）との住み分け：J-14 は応用サービス視点。J-11 は「LLM が Deep Learning の産物」という概念説明に徹する。
- 「2012 ImageNet 革命（AlexNet）」「2017 Transformer 論文」などのマイルストーンは本文には入れず、深掘り先や備考に留める。

## 出典メモ

- Goodfellow et al., "Deep Learning", MIT Press (2016) — checked 2026-04-29
- DeepMind, "What is deep learning?", deepmind.google — checked 2026-04-29
- LeCun, Bengio, Hinton, "Deep learning", Nature 521 (2015) — checked 2026-04-29

## 備考

- 2012 年 ImageNet コンペでの AlexNet の躍進が Deep Learning ブームの起点とされますが、本エントリでは技術史の細部には踏み込まず「層を重ねる手法」の概念紹介に徹しています。歴史的経緯は J-10 または timeline 系エントリへ参照。
- 「深層学習」という日本語訳も広く使われますが、業界では "Deep Learning" のカタカナ表記が主流のため本エントリでは英語表記を title とし、title_reading に「ディープラーニング」を入れています。
