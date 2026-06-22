---
id: J-83
title: vLLM
title_reading: ブイエルエルエム
category: term_general
subtype: inference
experience_level: research_only
reader_level: 6
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-06-22
related_terms:
  - KV Cache
  - バッチ推論
  - スループットとレイテンシ
  - ollama
  - LLM
status: drafting
---

# vLLM

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

LLM を高スループットで配信（サービング）するためのオープンソース推論エンジンです。KV キャッシュをページ単位で管理し、GPU を遊ばせず大量リクエストを捌きます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

vLLM は、学習済みの LLM（Large Language Model、大規模言語モデル）を「同時に大量のリクエストへ高速に応答するサーバ」に仕立てるための推論エンジンです。`vllm serve <モデル名>` の一行で OpenAI 互換 API のサーバが立ち上がり、アプリ側はエンドポイントの URL を差し替えるだけで自前ホストの LLM に切り替えられます。

価値の中心は「同じ GPU で、桁違いに多くのリクエストを捌けること」です。素朴に書いた推論サーバは、リクエストごとに KV キャッシュ（過去トークンの Key と Value を保存する領域）を連続したメモリ区画として確保します。最大長を見越して大きく取るため大半が未使用のまま遊び、しかも確保と解放を繰り返すうちにメモリが断片化して、空き合計はあるのに連続区画が取れず新しいリクエストを受けられなくなります。結果、GPU メモリが先に枯れて同時処理数（バッチサイズ）が伸びません。vLLM はこのメモリの無駄をなくし、空いた計算資源を埋め続けることで、ハードを増やさずスループットを底上げします。

## どこで出会うか

自社・自分の GPU で OSS の LLM（Llama、Qwen、gpt-oss など）をホストしようとした瞬間に、ほぼ必ず候補に挙がります。「ChatGPT の API では機密データを外に出せない」「推論コストを自前で握りたい」「同時アクセスが多くてレイテンシ（応答遅延）を詰めたい」——こうした要件で社内 LLM 基盤を組むときの定番です。

手元での出会い方は具体的で、`pip install vllm` → `vllm serve` で起動し、`gpu_memory_utilization`（GPU メモリをどこまで使うか）や `max_model_len`（扱う最大トークン長）、`tensor_parallel_size`（複数 GPU への分割数）といった設定を詰めていきます。リリースノートやベンチマーク記事では「PagedAttention」「continuous batching」「投機的デコード対応」「AWQ/GPTQ 量子化対応」といった語とセットで登場します。なお、手軽にローカルで 1 モデルを動かす用途は ollama（F-86）が担い、vLLM は「本番サービングで台数あたりの処理量を最大化する」側に立つ、という住み分けになります。

## メイン図

### 図の狙い

「リクエストごとに連続メモリを大きく確保して断片化する素朴版」と「KV キャッシュをページ単位で管理し空きスロットへ次々リクエストを詰める vLLM 版」を上下に並べ、なぜ同じ GPU で処理量が跳ね上がるのか——メモリの無駄を消す（PagedAttention）と GPU を遊ばせない（continuous batching）の二本柱——を一目で掴んでもらう。

### A. Before / After（GPU の遊びをどう消すか）

- Before（素朴なサービング）
  - 状況: リクエストごとに最大長ぶんの KV キャッシュを連続区画で予約。多くが未使用のまま占有され、確保／解放で断片化
  - 視覚要素（概念）: GPU メモリ帯にまだら模様の空白（断片化）。バッチは全リクエストが揃うのを待ち、短い応答が長い応答に足止めされる
  - つまずき: メモリが先に枯れて同時処理数が伸びず、待ち合わせで GPU が遊ぶ。スループットが頭打ちになる
- After（vLLM）
  - 状況: KV キャッシュを固定長ブロック（ページ）に分割して必要なぶんだけ割り当て（PagedAttention）。生成が終わったリクエストのスロットへ即座に次を投入（continuous batching）
  - 視覚要素: 隙間なく敷き詰められたページのタイル。ステップごとに完了したリクエストが抜け、空きへ新リクエストが流れ込む
  - うれしさ: メモリの無駄が消え、GPU が常に満稼働。同一ハードでスループットが大きく伸びる

## 会話での使い方例

「自前ホストで同時数が多いなら vLLM 一択で、PagedAttention と continuous batching が効くんですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM を OpenAI 互換 API で配信し、同じ GPU で捌けるスループットを最大化するサービングエンジンです。

### 2. うれしさ

メモリの無駄と待ち合わせを消し、ハードを増やさず同時処理数とスループットを大きく伸ばせます。

### 3. 注意点

スループット最適化が主眼で、単発の最小レイテンシや小規模ローカル用途は ollama 等のほうが手軽なことがあります。

### 4. どこで役立つか

社内 LLM 基盤・大量同時リクエストの API サーバなど、台数あたりの処理量が効いてくる本番運用で活きます。

### 5. はじめに

「PagedAttention でメモリの無駄を消し、continuous batching で GPU を遊ばせない」の二本柱を押さえれば芯は掴めます。

### 6. 深掘り先

PagedAttention、continuous batching、量子化（AWQ/GPTQ）、投機的デコード、tensor parallel

## 開発フローでの位置（必須）

1. モデル選定 — Llama・Qwen・gpt-oss など OSS の重みを選び、GPU メモリに載るサイズと量子化方式を決める
2. 起動 — `vllm serve <モデル>` で OpenAI 互換サーバを立てる。`gpu_memory_utilization`・`max_model_len` で容量を割り付ける
3. メモリ管理 — PagedAttention が KV キャッシュを固定長ページで割り当て、断片化と過剰確保をなくして同時収容数を増やす
4. スケジューリング — continuous batching が完了スロットへ次のリクエストを即投入し、GPU を遊ばせず満稼働を保つ
5. チューニング — バッチサイズ・量子化・投機的デコード・tensor parallel を調整し、スループットとレイテンシの折り合いを取る

## 関連用語

- KV Cache
- バッチ推論
- スループットとレイテンシ
- ollama
- LLM

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 上段「素朴なサービング」、下段「vLLM」の 2 段比較。上段は GPU メモリ帯を 1 本描き、リクエストごとに最大長ぶんの長い区画を予約 → 実際の使用は先頭だけで残りは灰色の遊び、確保／解放を繰り返した跡がまだらな空白（断片化）として残る。右側にバッチを並べ、短い応答が長い応答の完了を待って足止めされる「待ち合わせ」を点線で示す。下段は同じメモリ帯を均等な小タイル（ページ）で敷き詰め、各リクエストが必要なページだけを飛び石状に確保（連続でなくてよい）。タイムステップが進むと完了したリクエストのタイルが抜け、即座に新リクエストのタイルが空きへ流れ込む矢印を描く。
- 登場人物（いれば）: 推論サーバを運用するエンジニア 1 名（著者の分身）。GPU メモリ帯のダッシュボードを見ながら、下段の隙間なく埋まったタイルにうなずいている。
- 吹き出し・心の声: 「同じ GPU なのに捌ける数が段違い。メモリの遊びを消して、空いたら即詰める——それだけでここまで変わるのか」
- 中央に置くキーワード/ラベル: 「PagedAttention＝メモリの無駄を消す」「continuous batching＝GPU を遊ばせない」「同一ハードでスループット↑」
- Before / After の場合の対比ポイント: 上段＝まだらな空白（断片化）＋待ち合わせの足止め、下段＝隙間なきタイル＋流れ込む新リクエスト。「無駄なメモリ」と「遊ぶ GPU」の 2 つの損失が、2 つの工夫で消える対応を色で結ぶ。

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（① 配信サーバ箱、② 満タンに敷き詰まったメモリタイル、を差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 棚から OSS モデルの重みを選ぶ（量子化ラベル付き）
- Step 2 のアイコン/絵柄: `vllm serve` のターミナル＋OpenAI 互換 API の差込口
- Step 3 のアイコン/絵柄: 固定長ページに分割されたメモリブロック（PagedAttention）
- Step 4 のアイコン/絵柄: 完了スロットへ新リクエストが流れ込むベルトコンベア（continuous batching）
- Step 5 のアイコン/絵柄: スループットとレイテンシの天秤＋量子化／投機的デコード／tensor parallel のつまみ
- 矢印で示す流れの意図: モデル選定 → 起動 → メモリ管理 → スケジューリング → チューニング、という「自前 LLM 基盤を立てて処理量を最大化するまで」の縦の流れ

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: vLLM
- visual_subject: 同じ GPU メモリが Before では断片化でまだら・After では隙間なくタイル敷詰になり新リクエストが流れ込む対比
- supporting_subjects: 推論サーバを運用するエンジニア（著者の分身）、GPU メモリ帯のタイル図、完了スロットへ流れ込む矢印
- logo_subject: none
- excluded_subjects: カラフルなダッシュボード・UIスクリーン・グリーン/レッド/イエローの警告色・他社ロゴ・実在UIスクリーンショット

### scene brief（日本語）
上段「素朴なサービング」／下段「vLLM」の2段比較図を中心に据える。上段は GPU メモリ帯にまだらな灰色の空白（断片化）が残り、短い応答が長い応答の完了を点線で待つ様子を描く。下段は同じ帯が均等な小タイルで隙間なく埋まり、完了したスロットへ新リクエストの矢印が即座に流れ込む。画面右端にエンジニア（著者の分身）を小さく立たせ、下段のタイルを指差しながら吹き出し「同じ GPU なのに段違い——メモリの遊びを消して、空いたら即詰める」を添える。キーラベルは「PagedAttention＝メモリの無駄を消す」「continuous batching＝GPU を遊ばせない」の2本のみ。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration, 2:1 horizontal composition (1254x627); monochrome plus blue palette only (#1A1A1A linework, neutral grays #6B7280, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background. Two stacked panels comparing naive GPU memory layout (top: fragmented gray patches scattered across the memory band, dashed wait-line showing short response blocked by long one) versus vLLM layout (bottom: uniform fixed-size tiles filling the memory band with no gaps, curved arrows showing new requests flowing into completed slots). A single male engineer character stands at the right edge of the lower panel, pointing at the filled tiles, with a speech bubble reading the key idea. Two label banners only: "PagedAttention" and "continuous batching". Flat, clean, consistent series style; minimal text, only the two key labels; no yellow, green, red, purple, orange, rainbow, colorful UI, or brand marks.

## コミュニティ補完メモ

- 同じ Lv6 シェルフの近接語との住み分け:
  - KV Cache（J-29）: 「何を保存するか・なぜ効くか」の概念。vLLM はその KV キャッシュを OS のページングに倣って固定長ブロックで管理する実装（PagedAttention）。本エントリは KV Cache の「メモリ管理」ステップを実装に落とした道具、という位置。
  - バッチ推論（J-84）: 複数リクエストをまとめて GPU に通す概念。vLLM の continuous batching は「揃うまで待つ静的バッチ」を「空きスロットへ動的に詰める」へ発展させた実装。概念は J-84、実装の妙は本エントリ。
  - スループットとレイテンシ（J-85）: vLLM が最適化する対象の指標そのもの。指標の定義・トレードオフは J-85、それを稼ぐエンジンが本エントリ。
  - ollama（F-86）: ローカルで手軽に 1 モデルを動かす用途。vLLM は本番サービングで台数あたりの処理量を最大化する側。手軽さ vs スループットで住み分け。
  - LLM（J-14）: vLLM が配信する対象。J-14 は一般読者向けの入口、本エントリは「その LLM をどう速く配るか」の裏側。
- スコープ境界: 本エントリは「vLLM とは何か・なぜ速いか（二本柱）・どこで使うか」までを担う。PagedAttention の内部アルゴリズムや量子化の数理は各深掘りエントリに譲る。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (vLLM, 2023) https://arxiv.org/abs/2309.06180 — checked 2026-06-22（PagedAttention と continuous batching の一次出典。KV キャッシュ断片化の問題提起とスループット向上の評価）
- vLLM 公式ドキュメント https://docs.vllm.ai/ — checked 2026-06-22（`vllm serve`、OpenAI 互換 API、`gpu_memory_utilization`・`max_model_len`・`tensor_parallel_size` 等の設定、量子化・投機的デコード対応の確認）
- vLLM GitHub リポジトリ https://github.com/vllm-project/vllm — checked 2026-06-22（OSS であること・対応モデル・active な開発状況の確認）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- version_status: active（2026-06 時点で活発に開発・リリースが続く OSS）。対応モデルや設定項目はバージョンで変わるため、設定名・対応量子化は時変情報として扱う。
- 用語の整理: 「PagedAttention＝メモリ効率（KV キャッシュの断片化・過剰確保を消す）」と「continuous batching＝スケジューリング効率（GPU の遊びを消す）」は直交する二本柱。両者が揃って初めて素朴版から桁違いのスループットが出る、という関係を本文・図で崩さないこと。
