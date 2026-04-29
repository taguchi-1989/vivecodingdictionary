---
id: F-14
title: three.js
title_reading: スリージェイエス
category: term_tool
subtype: framework
experience_level: hands_on
reader_level: 3-4
figure_type: before_after
page_layout: spread_v1
start_date: 2010-04-24
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - JavaScript
  - WebGL
  - React Three Fiber
  - Babylon.js
status: drafting
---

# three.js

## tagline

ブラウザで 3D を手軽に描けるライブラリです。WebGL（ウェブジーエル）の複雑さを隠す高レベル層として機能します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

3D モデルの読み込み・光源・カメラ・アニメーションを JavaScript（F-1）で操作できます。WebGL を直接書く場合に必要な行列計算やシェーダ言語の知識を省略でき、数行で立方体を画面に表示することができます。

## どこで出会うか

AI に「ブラウザで動く 3D デモを作って」と頼むと、Claude や ChatGPT は三行目で `import * as THREE from 'three'` と書き始めます。3D ビジュアライザやデータ可視化のコードが共有されたとき、読み始めの一行として目にすることが多いです。

## メイン図

### 図の狙い

WebGL を直書きした場合と three.js を使った場合の行数・難易度の対比を示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: WebGL をゼロから書く
  - 視覚要素（コード or 概念）: 行列計算・シェーダ宣言・バッファ操作が 50 行以上続く
  - つまずき: 何を書いているかわからないまま画面は真っ黒
- After
  - 状況: three.js を使う
  - 視覚要素: `new THREE.BoxGeometry()` の 10 行程度で回転する立方体が表示される
  - うれしさ: AI に頼んで動くコードがすぐ得られる

## 会話での使い方例

「three.js を Claude に書かせたら、ブラウザで動く 3D デモが 10 分で出ました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

WebGL の複雑な低レベル処理を包んで 3D 描画を簡潔にします。

### 2. うれしさ

AI が生成したコードがそのまま動く確率が高い定番ライブラリです。

### 3. 注意点

3D 全般の学習コストは残るため、座標やカメラ概念の理解が必要です。

### 4. どこで役立つか

3D データ可視化・製品デモ・インタラクティブな説明 UI で使われます。

### 5. はじめに

WebGL より先に three.js から入るのが現代的な学習順序です。

### 6. 深掘り先

WebGL、React Three Fiber、Babylon.js

## 開発フローでの位置（必須）

1. 要件整理 — ブラウザ上で 3D 表現が必要かどうかを確認する
2. ライブラリ導入 — npm または CDN で three.js を追加する
3. AI に生成依頼 — シーン・カメラ・光源のコードを Claude 等に書かせる
4. 動作確認 — ブラウザで回転・操作をチェックし、座標系を調整する
5. 連携 — React Three Fiber や物理演算ライブラリと組み合わせて拡張する

## 関連用語

- JavaScript
- WebGL
- React Three Fiber
- Babylon.js


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

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

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に「WebGL 直書き」のコード断片（難解な行列計算が何行も続く）、右に「three.js」のコード断片（BoxGeometry 数行）を並べる Before/After 対比
- 登場人物: 画面の前で頭を抱える開発者（Before）、スッキリした顔でブラウザを見ている開発者（After）
- 吹き出し・心の声: Before「なんで真っ黒なの…」/ After「動いた！ 10 分で出来た」
- 中央に置くキーワード/ラベル: `three.js で 3D を手軽に`
- Before / After の対比ポイント: 行数の多さ・専門知識の要否

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チェックリストのアイコン
- Step 2 のアイコン/絵柄: パッケージ箱のアイコン
- Step 3 のアイコン/絵柄: AI チャットの吹き出しアイコン
- Step 4 のアイコン/絵柄: ブラウザウィンドウに 3D 立方体
- 矢印で示す流れの意図: 要件確認 → 導入 → AI 生成 → 確認・拡張の一方向フロー


## コミュニティ補完メモ

- WebGL（F-181）との住み分け：WebGL はブラウザの低レベル 3D API そのもの。three.js はその上に立つラッパー。WebGL を理解したいなら F-181 へ
- Babylon.js との住み分け：Microsoft 系の競合ライブラリ。ゲームエンジン的な機能が豊富。three.js より重いが公式ドキュメントが充実している
- React Three Fiber との住み分け：React（F-11）のコンポーネント思考で three.js を書くためのラッパー。React を使うプロジェクトならセットで登場する

## 出典メモ

- <https://threejs.org/> — checked 2026-04-29
- <https://github.com/mrdoob/three.js> — checked 2026-04-29


## 備考

- 2010 年公開。Ricardo Cabello（mr.doob）が開発・現在もメンテナンス継続中
- glTF（ジーエルティーエフ）形式の 3D モデル読み込みに対応
- 物理演算は three.js 単体では提供せず、Cannon.js 等との連携が必要
- pricing_note: none（MIT ライセンス、無料）
