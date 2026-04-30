---
id: G-18
title: Chain of Thought
title_reading: チェーン オブ ソート
category: term_llm
subtype: technique
experience_level: partial
reader_level: 3-4
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Prompt Engineering
  - Few-shot Learning
  - Thinking モデル
  - Zero-shot
status: drafting
---

# Chain of Thought

## tagline

LLM に「答えの前にステップを示して」と促す推論技法です。思考過程を見せることで正答率が上がります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

数学・論理問題など、一段飛ばしにすると誤る問いに対し、LLM が中間ステップを順番に書き出してから結論を出せるようにします。2022 年に Google の Wei らが論文で効果を実証しました。

## どこで出会うか

Prompt Engineering（G-10）の解説記事で必ず登場します。「Let's think step by step.」の一文を末尾に添えるだけの Zero-shot CoT が有名で、Few-shot Learning（G-13）と組み合わせた例示付き版も広く使われます。


## メイン図

### 図の狙い

「直接回答」と「思考ステップ付き回答」の差を並べて、CoT が推論の精度を上げる仕組みを直感で掴んでもらう。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: プロンプトに「答えを教えて」とだけ書いた状態
  - 視覚要素（コード or 概念）: 問題 → LLM → 誤答
  - つまずき: 複数ステップが必要な問題で一発回答が外れる
- After
  - 状況: 「ステップを順に示してから答えて」と添えた状態
  - 視覚要素: 問題 → ステップ 1 → ステップ 2 → ステップ 3 → 正答
  - うれしさ: 中間推論が見えるので誤りの箇所も確認できる


## 会話での使い方例

「Thinking モデルが普及したので、CoT のおまじないを書く頻度は減りました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

プロンプトで LLM に推論の中間ステップを明示させる技法です。

### 2. うれしさ

数学・論理問題の正答率が大きく上がることがあります。

### 3. 注意点

Thinking モデルでは CoT が自動化され、手書きの必要性は減ります。

### 4. どこで役立つか

非 Thinking モデルを使う予算制約のある場面で今も有効です。

### 5. はじめに

Zero-shot CoT の一文（Let's think step by step.）を試すと体感できます。

### 6. 深掘り先

Prompt Engineering, Thinking モデル, Self-Consistency


## 開発フローでの位置（必須）

1. 問題の選定 — 多段推論が必要か確認し、CoT 適用を判断します
2. プロンプト設計 — Zero-shot CoT か Few-shot CoT かを選んで記述します
3. 出力の検証 — 中間ステップが正しいか順に確認します
4. モデル選択の再考 — 精度不足なら Thinking モデルへの切り替えを検討します


## 関連用語

- Prompt Engineering
- Few-shot Learning
- Thinking モデル
- Zero-shot


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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左に「直接回答モデル（問題→誤答）」、右に「CoT モデル（問題→ステップ 1→2→3→正答）」を対比する 2 列図
- 登場人物: 人物（ユーザー）がプロンプトを打ち込み、吹き出しで LLM が思考を展開する
- 吹き出し・心の声: 「まず…、次に…、したがって答えは…」のステップを小さいボックスで流れとして示す
- 中央に置くキーワード/ラベル: 「思考ステップ」「CoT」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（問題を見極めるイメージ）
- Step 2 のアイコン/絵柄: ペン・メモ（プロンプトを書くイメージ）
- Step 3 のアイコン/絵柄: チェックリスト（中間ステップを確認するイメージ）
- Step 4 のアイコン/絵柄: 上位モデルへの矢印（Thinking モデルへの移行イメージ）


## コミュニティ補完メモ

- Prompt Engineering（G-10）との住み分け：G-10 はプロンプト設計の総論。G-18 はその中の推論強化テクニック 1 つ。
- Thinking モデル（G-14）との住み分け：G-14 は CoT をモデル内部に自動組み込んだ進化形。G-18 はその原点となる手法側を扱う。
- Few-shot Learning（G-13）との住み分け：G-13 は例示プロンプト一般。G-18 は「思考過程の例を示す」という Few-shot CoT として交差するが、CoT の本質は推論可視化にある。
- Self-Consistency（複数の思考経路を多数決で集約）は G-18 の派生手法で、現時点では独立エントリなし。備考として本エントリに記載。


## 出典メモ

- Wei et al. 2022 "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (arXiv:2201.11903) — checked 2026-04-30
- Google Blog: "Language Models Perform Reasoning via Chain of Thought" — checked 2026-04-30


## 備考

- CoT の派生に Self-Consistency（複数の思考経路を生成し多数決で集約する手法）がある。独立エントリは未設定。
- Thinking モデル（o1 系・Claude 4.5 Thinking・Gemini 2.5 Thinking）は CoT を内部展開するため、プロンプトでの手書き CoT は不要になりつつある。用途に応じた使い分けを読者に示すことが重要。
- GSM8K（E-23）・MATH（E-24）ベンチマークで CoT の効果が実証されているが、これらのベンチエントリはスコープ外。
