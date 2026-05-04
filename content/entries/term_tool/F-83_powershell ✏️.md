---
id: F-83
title: PowerShell
title_reading: パワーシェル
category: term_tool
subtype: shell
experience_level: partial
reader_level: 2-4
importance: D
figure_type: comparison
page_layout: spread_v1
start_date: 2006-11-14
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - bash
  - WSL
  - git
  - Azure
status: drafting
---

# PowerShell

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

Microsoft が 2006 年に公開したシェル兼スクリプト言語です。Windows 標準搭載で、現行の PowerShell 7 は macOS/Linux でも動きます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

コマンドを対話入力するシェルとして OS を操作しながら、スクリプトとして繰り返し処理を自動化できます。bash（F-81）がテキストを流すのに対し、PowerShell は .NET オブジェクトをパイプで扱うため、属性でのフィルタが直感的です。

## どこで出会うか

Windows の「ターミナル」や「スタートメニュー」から起動できます。Claude Code を Windows ネイティブで使うとき、Bash ツールではなく PowerShell ツールが呼ばれる環境があり、bash と書式が違うためコマンドの解釈に注意が必要です。

## メイン図

### 図の狙い

bash と PowerShell のパイプ操作を短いコマンド対比で示し、「テキスト vs オブジェクト」の違いを掴んでもらう。

### A. Before / After（figure_type: comparison）

- Before
  - 状況: bash でプロセスを CPU 使用率でフィルタしたい
  - 視覚要素（コード）: `ps aux | awk '$3 > 10'`（テキスト解析が必要）
  - つまずき: 列番号を数えて awk で切り出す手間がかかる
- After
  - 状況: PowerShell でオブジェクト属性を直接フィルタ
  - 視覚要素: `Get-Process | Where-Object {$_.CPU -gt 10}`
  - うれしさ: `.CPU` というプロパティ名で意図が明確になる

## 会話での使い方例

「Claude Code を Windows で使うときは PowerShell の制約を伝えると安全です。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Windows 標準のシェルとスクリプト実行環境です。

### 2. うれしさ

動詞-名詞形式のコマンド名で操作の意図が読みやすくなります。

### 3. 注意点

bash の `&&` は PowerShell 5.1 では使えず、7 以降で対応します。

### 4. どこで役立つか

Windows 管理・Azure 操作・CI/CD の Windows ランナーで使われます。

### 5. はじめに

bash との構文差異と、バージョン 5.1/7 の違いを押さえましょう。

### 6. 深掘り先

bash、WSL、Azure

## 開発フローでの位置（必須）

1. 環境確認 — `$PSVersionTable` でバージョンと OS を確認します
2. スクリプト作成 — `.ps1` ファイルに動詞-名詞コマンドを組み合わせて書きます
3. 実行ポリシー確認 — `Set-ExecutionPolicy` でスクリプト実行が許可されているか確かめます
4. パイプ活用 — オブジェクトをパイプで渡し、`Where-Object` や `Select-Object` でフィルタします
5. CI/CD 連携 — GitHub Actions 等の Windows ランナーで `.ps1` スクリプトを呼び出します

## 関連用語

- bash
- WSL
- git
- Azure

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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: bash と PowerShell のコマンド対比。左に `ps aux | awk` の bash コマンド、右に `Get-Process | Where-Object` の PowerShell コマンドを並べる
- 登場人物: Windows PC に向かう人物（男女どちらでも可）
- 吹き出し・心の声: 「bash のコマンドがそのまま動かない…」→「PowerShell は .CPU って書けるんだ」
- 中央に置くキーワード/ラベル: テキスト vs オブジェクト
- Before / After の対比ポイント: 列番号で切り出す bash vs プロパティ名で読む PowerShell

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: バージョン確認アイコン（虫眼鏡 + ターミナル）
- Step 2 のアイコン/絵柄: スクリプトファイル（.ps1 拡張子のファイルアイコン）
- Step 3 のアイコン/絵柄: 鍵マーク（実行ポリシー）
- Step 4 のアイコン/絵柄: パイプ記号（|）を中央に配置
- Step 5 のアイコン/絵柄: CI/CD サーバアイコン
- 矢印で示す流れの意図: 確認 → 作成 → 許可 → 実行 → 自動化の順で進む

## コミュニティ補完メモ

- bash（F-81）との住み分け：bash は Unix 系でテキストパイプ、PowerShell は Windows 標準でオブジェクトパイプ。どちらを使うかは OS と実行環境で決まる
- WSL（F-82）との住み分け：Windows 上で bash を使いたい場合は WSL 経由が現実的。Claude Code を Windows で使う場合は PowerShell か WSL かで動作が変わるため、環境に注意が必要
- PowerShell 5.1（Windows PowerShell）と PowerShell 7（cross-platform）は別物。バージョン差異でスクリプトが動かないケースがある

## 出典メモ

- [PowerShell Overview](https://learn.microsoft.com/ja-jp/powershell/scripting/overview) — checked 2026-04-29
- [What's New in PowerShell 7.5](https://learn.microsoft.com/ja-jp/powershell/scripting/whats-new/what-s-new-in-powershell-75) — checked 2026-04-29

## 備考

- PowerShell 5.1（Windows 同梱）と PowerShell 7（クロスプラットフォーム版、別途インストール）でコマンド互換性が異なる。`&&` 演算子は 7 以降のみ対応
- Claude Code が Windows ネイティブ環境で動く場合、bash ツールではなく PowerShell ツールが呼ばれる場面がある。AI へのプロンプトで環境（PowerShell バージョン）を明示すると誤爆が減る
