# スマホ雑コメント運用

*スマホでは正しい Markdown を書かず、Claude Code Web などのチャットに雑に話す。PC 側で `mobile_inbox` 形式へ整えて取り込むための軽量運用です。*

## 目的

外出先で、著者本人の感想・つまずき・本文への指摘を止めずに残す。

スマホでは、次のことをしない。

- `content/entries/**/*.md` を直接編集しない
- `mobile_inbox` の厳密な見出し形式を毎回手で書かない
- Git / Obsidian / validator を意識しない

スマホでは、思ったことをチャットに雑に書く。整形と反映は PC 側で行う。

## 基本フロー

1. スマホで Claude Code Web などのチャットを開く
2. 「VibeCoding 図鑑の著者コメントを書きたい」と伝える
3. AI に、今日コメントしやすい項目を 1〜3 件出してもらう
4. AI が 1 項目ずつ質問する
5. 著者は雑に答える
6. AI が最後に `mobile_inbox` 形式へ整える
7. PC に戻ったら、その整形結果を Codex / Claude Code に貼って取り込む

## スマホで最初に送る定型文

```text
VibeCoding図鑑の著者コメントを書きたい。
今日コメントしやすい項目を3つ出して。
1つずつ質問して。
私は雑に答えるので、最後に mobile_inbox 形式でまとめて。

整理先は次のどれかにして。
- 第一印象
- 良い点
- ダメな点
- 誰向けか
- 非エンジニアのつまずき
- 本文への指摘
```

## AI 側の質問の仕方

AI は、1 回に 1 エントリだけ聞く。

良い聞き方:

```text
B-2 Claude について。
第一印象、良い点、ダメな点、誰向けか、つまずきのうち、思いつくものだけ雑に書いてください。
箇条書きでも話し言葉でも大丈夫です。
```

悪い聞き方:

```text
B-2 / my_comment / first_impression の形式で書いてください。
```

スマホでは形式を守らせない。形式はあとで AI が整える。

## 著者の雑な回答例

```text
Claudeは入口が多いのが最初わかりにくい
でも文章作るのはかなり便利
Claude.aiとClaude Codeの違いが最初混ざった
料金とモデル名は覚えにくい
```

## AI が整える形式

上の雑コメントは、最後に次の形へ整える。

```markdown
## B-2 / my_comment / first_impression
入口が多く、最初は全体像がつかみにくかった。

## B-2 / my_comment / good
文章を作る用途ではかなり便利に感じた。

## B-2 / my_comment / bad
料金とモデル名の関係が覚えにくい。

## B-2 / stumble
Claude.ai と Claude Code の違いが最初は混ざった。
```

## 種類の対応

| 著者が言った内容 | 変換先 |
| :-- | :-- |
| 第一印象、最初に思ったこと | `my_comment / first_impression` |
| 良かった点、便利だった点 | `my_comment / good` |
| ダメな点、嫌だった点、使いにくさ | `my_comment / bad` |
| 誰に向いていそうか | `my_comment / target` |
| 最初わからなかったこと、詰まったこと | `stumble` |
| 本文が古い、説明が違う、直したい節 | `ai_feedback / 対象節名` |

## PC 側での取り込み

PC に戻ったら、Codex / Claude Code に次のように貼る。

```text
以下を mobile_inbox に入れて import-comments して。
日付は今日で。

（ここに整形済み markdown）
```

PC 側の AI は、次を行う。

1. `mobile_inbox/YYYY-MM-DD.md` に追記する
2. `skills/import-comments.md` のルールに従って反映する
3. 正常に反映できたら `processed/` へ移動する

## 守ること

- 著者のコメントは要約しすぎない
- 文体を整えるのはよいが、意味を足さない
- `my_comment` と `stumble` は著者の声なので、勝手に立派な文章にしすぎない
- `ai_feedback` は本文へ直接反映しない。まず備考へ積む
- スマホ側で ID が曖昧な場合は、PC 側で確認してから取り込む

## 位置づけ

この運用は、Obsidian Mobile + Git の正式運用より軽い。

- きちんと同期して書ける日は `mobile_inbox/YYYY-MM-DD.md` に直接書いてよい
- 面倒な日は、この雑コメント運用でよい
- どちらも最終的には `mobile_inbox` に集約する

