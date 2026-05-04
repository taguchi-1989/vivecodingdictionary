---
id: G-9
title: effort レベル
title_reading: エフォート レベル
category: term_llm
subtype: basic
experience_level: partial
reader_level: 3-4
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-04-30
related_terms:
  - Thinking モデル
  - reasoning_effort
  - Claude Code
  - o3
status: needs_review
---

# effort レベル

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

Thinking モデルに「どれだけ深く考えるか」を伝える設定で、low／medium／high の 3 段階があります。

## 何をしてくれるか

推論ステップ数を呼び出し側で調整できます。high は思考時間が伸び正答率が上がりやすい反面、料金と応答時間も増えます。軽い作業は low でコストを抑えます。

## どこで出会うか

Claude Code の `--effort high` フラグや settings.json での指定が代表例です。OpenAI API では `reasoning_effort` として登場し、「難しい調査は high、整形は low」と使い分けます。

## メイン図

### 図の狙い

low／medium／high の 3 段階を横に並べ、思考時間・料金・精度の変化を一目で示します。

### B. 登場シーン（figure_type: comparison）

- シーン1: 開発者が Claude Code で `--effort high` を指定して難解なバグを調査する
- シーン2: OpenAI API で `reasoning_effort: low` を渡して高速な整形タスクをこなす
- シーン3: settings.json にデフォルト値を書いておき、常に medium で動かす
- 並べる基準: effort 値が変わると何が変わるかを用途別に対比

## 会話での使い方例

「このバグ調査は effort を high にしないと答えが浅くなりがちです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Thinking モデルの内部推論量をパラメータで制御します。

### 2. うれしさ

タスクの難度に合わせてコストと精度のバランスを取れます。

### 3. 注意点

high でも正答を保証するものではなく、料金が増える点に注意が必要です。

### 4. どこで役立つか

複雑なバグ調査や設計レビューで high を選ぶと効果的です。

### 5. はじめに

low／medium／high の意味と、それぞれの料金差を把握することが出発点です。

### 6. 深掘り先

Thinking モデル、reasoning_effort、o3

## 開発フローでの位置（必須）

1. 難度の見極め — 整形か深い推論かを判断します
2. effort 値の選択 — low／medium／high から選びます
3. フラグや API で指定 — `--effort` や `reasoning_effort` に渡します
4. 結果と料金を確認 — 質とトークン消費を照合します
5. 既定値を固定 — settings.json に書いて毎回の指定を省きます

## 関連用語

- Thinking モデル
- reasoning_effort
- Claude Code
- o3


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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: low／medium／high の 3 列表。各列に「思考時間」「料金」「精度」の目安アイコンを並べる
- 登場人物: 開発者（男性または中性的シルエット）が high の列を指さしている
- 吹き出し・心の声: 「バグが難しいから今日は high にします」
- 中央に置くキーワード/ラベル: effort レベル比較

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（タスク確認）
- Step 2 のアイコン/絵柄: スライダー（レベル選択）
- Step 3 のアイコン/絵柄: ターミナル（フラグ入力）
- Step 4 のアイコン/絵柄: チェックリスト（結果確認）
- 矢印で示す流れの意図: 判断 → 設定 → 実行 → 検証の一方向フロー


## コミュニティ補完メモ

- G-14 Thinking モデルとのスコープ分担：Thinking モデルは「推論を段階的に見せるモデルの種類」、effort レベルは「そのモデルに渡すパラメータ値」。どちらが主体かで使い分ける
- D-22 o1 系・D-23 o3 系：OpenAI モデルにおける effort／reasoning_effort の具体的な動作はそちらへ詳細を委譲
- B-2 Claude：Claude 側の effort フラグの詳細は B-2 の補足欄を参照

## 出典メモ

- Anthropic Claude Code ドキュメント — checked 2026-04-30
- OpenAI API リファレンス（reasoning_effort パラメータ） — checked 2026-04-30

## 備考

- effort の段階は製品によって異なる（Claude Code: low/medium/high、OpenAI: low/medium/high、minimal を加える製品もある）。本エントリでは共通概念として 3 段階を基本に説明している
- 料金・レイテンシの具体値は製品バージョンで変わるため evaluation_date を参照すること
