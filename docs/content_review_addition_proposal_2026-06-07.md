# 著者コメント違和感チェックと追加語彙案

*2026-06-07 作成。対象は `## 私のコメント` の公開時リスク、A章/前付け/あとがきの語り口、Zod など追加したほうがよい周辺語彙。本文を直接直す前のレビュー案。*

## 目的

- 著者の感想は残しつつ、読者に「事実」と誤読される断定を減らす
- 「知らない人のつまずき」として価値がある違和感を、本文側の補足に変換する
- Zod のように、AI開発・TypeScript開発の会話で出やすいが現行目次に薄い語彙を追加候補化する

## 先に守る方針

- `## 私のコメント` は著者本人の声なので、AIが本文へ直接書き換えない
- 修正する場合も「本人の言い方を薄める」のではなく、横に事実補足・評価日・用途条件を足す
- サービス評価は時変が激しいため、「2026年5月時点」「私の用途では」「未使用・評判ベース」を明示する

## 違和感・誤解の出やすい型

| 型 | 例 | リスク | 直し方の案 |
|:--|:--|:--|:--|
| 時点が強い断定 | 「一番使いやすい」「今は不要」 | 数か月で古くなる | `2026年5月時点の私の用途では` を足す |
| 未使用なのに評価が強い | 「今更感」「難しい印象」 | 読者が実体験レビューとして読む | `未使用なので判断保留` を明記する |
| セキュリティ不安の断定 | 「会社では使いにくい」 | 根拠不明の否定に見える | `業務利用では利用規約・データ保持の確認が必要` に寄せる |
| 技術概念の混同 | YAML の「型の厳密さ」 | YAML自体と検証ツールが混ざる | `YAMLは記法。型検証はスキーマ/validator側` と補足 |
| 魔法っぽい理解 | Prisma の「入れておけば DB 周りがうまく回る」 | ORM/DB/マイグレーション責務が曖昧になる | `DB操作の型付き窓口。設計と運用は別に必要` と補足 |
| 主観が本文化しすぎる | 「すべての人が使うべき」 | 読者像を狭める | `ChatGPT課金済みで開発も触る人には第一候補` のように条件化 |

## 個別に気になった箇所

### TypeScript

現行コメントの「必要性も分からず辛かったですが、必須の道でした」は良いです。非エンジニア読者の入り口として強い。

ただし、TypeScriptは実行時のデータを自動で検証するものではありません。Zodを追加するなら、TypeScript欄には「型は開発中の安全網、外から来たデータの確認はZod/JSON Schemaの仕事」という補足があると理解が締まります。

### JSON

「人間が直接読み書きするより AI や設計者が扱うもの」は少し狭いです。JSONは機械間データ交換が主役ですが、人間もAPIレスポンスや設定確認で普通に読みます。

直すなら「人間が長文として読むものではなく、機械と人が同じ構造を確認するための形式」くらいが自然です。

### YAML

「JSONに比べると型の厳密さが完璧ではない」は、理解として少しズレます。YAMLはデータ表記で、型の厳密さはYAMLそのものより、読み取る側のスキーマやvalidatorに依存します。

提案文:

> 👎 ダメな点: 読みやすい反面、インデントや解釈差で壊れやすく、スキーマ検証なしでは安心しづらいです。

### Prisma

「入れておけば DB 周りがうまく回るらしい」は、読者の正直な感覚としては有効です。ただし、PrismaはDBそのものではなく、スキーマ・マイグレーション・型付きクライアントをつなぐ層です。

本文側に「PrismaはDBを置き換えるものではない。DBとの付き合い方をTypeScript側に引き寄せる道具」と足すと誤解が減ります。

### Tool Use / Function Calling

「AIがパソコンでできることを事実上すべて担えるようになり得る」は、方向性としては良いですが、権限・ツール定義・ホスト実装・実行環境に依存します。

補足案:

> ただし、AIが直接動かすのではなく、許可されたツールをホスト側が実行する、という責任分界が大事です。

### サービス評価系

Microsoft Copilot / v0 / Bolt.new / Devin などは、率直な温度感が出ていて魅力があります。一方で、未使用・時点依存・用途依存の評価が混ざります。

改善案は、コメント本文を丸めるより、A-6「評価日・時変情報の見方」に以下を足すほうが良いです。

> 本書の著者コメントは、評価日時点の著者の用途に基づく体感です。サービスは数週間で変わるため、料金・性能・UIは必ず現在の公式情報で確認してください。

## 追加候補パック

Zodだけを単独で足すより、「型・スキーマ・API契約」の小パックとして足すのが自然です。Zodはこのパックの中心に置けます。

### 優先度A

| 提案ID | 見出し | 置き場 | 理由 |
|:--|:--|:--|:--|
| F-210 | JSON Schema | F 従来コーディング / 型・スキーマ | JSON、Function Calling、Structured Outputs、OpenAPI の土台になる |
| F-211 | Zod | F 従来コーディング / 型・スキーマ | TypeScriptの型と実行時バリデーションの間を埋める重要語 |
| F-212 | OpenAPI | F 従来コーディング / API契約 | YAML/JSONでAPI仕様を書く代表。API連携・SDK生成・AIツール定義にも近い |
| G-48 | Structured Outputs | G バイブコーディング特有 | LLMにJSON Schemaで出力形を守らせる話。Function Callingと隣接 |

### 優先度B

| 提案ID | 見出し | 置き場 | 理由 |
|:--|:--|:--|:--|
| F-213 | tRPC | F 従来コーディング / API契約 | TypeScriptだけでAPIの型をつなぐ代表。Zodとの連携が多い |
| F-214 | React Hook Form | F 従来コーディング / フォーム | Zodをフォーム検証で見る読者向け |
| F-215 | Ajv | F 従来コーディング / 型・スキーマ | JSON Schema validatorの代表。Zodとの住み分けに使える |
| F-216 | Valibot | F 従来コーディング / 型・スキーマ | Zod代替として出るが、本書では関連語止まりでもよい |
| F-217 | Drizzle ORM | F 従来コーディング / ORM | Prismaと比較されやすいTypeScript ORM。必要ならPrismaの隣に追加 |

## Zod を入れるなら同時に入れたい説明

### 一文定義

Zodは、TypeScriptでデータの形を定義し、その形どおりか実行時に検証できるライブラリです。

### TypeScriptとの住み分け

- TypeScript: 書いているコードの型を開発中に見る
- Zod: API・フォーム・AI出力など、外から来たデータが本当に期待どおりか実行時に見る

この住み分けを入れないと、「TypeScriptがあるのにZodがなぜ要るのか」が読者に残ります。

### JSON Schemaとの住み分け

- JSON Schema: JSONの形を標準的な仕様として表す
- Zod: TypeScriptコードとしてスキーマを書き、型推論と実行時検証を同時に使う

Zod 4ではJSON Schema変換が公式に扱われています。ただし `z.fromJSONSchema()` は実験的扱いなので、本文では「変換できるが万能ではない」程度に留めるのが安全です。

### 図案

左ページは「外から来たJSON」をZodの検査ゲートに通し、右側でTypeScriptの型付きデータとして使う図が合います。

```text
API / フォーム / AI出力
        ↓
    unknown data
        ↓
   Zod schema gate
        ↓
  validated + typed data
        ↓
 TypeScript app code
```

### 関連語

- TypeScript
- JSON
- JSON Schema
- OpenAPI
- Function Calling
- Structured Outputs
- React Hook Form
- tRPC

## 追加候補の最小スケルトン

### F-210 JSON Schema

- tagline: JSONの形を機械が検査できるように書くためのルール表です。
- どこで出会うか: API仕様、LLMの構造化出力、Function Callingの引数定義。
- 注意点: JSON Schema自体は実装ではなく仕様。検証にはAjvなどのvalidatorが必要。
- 図: JSONデータと、その形を定義するSchemaを左右に並べる。

### F-211 Zod

- tagline: TypeScriptでデータの形を書き、実行時に検証できるライブラリです。
- どこで出会うか: Next.js、フォーム、API入力、AI出力の検証。
- 注意点: TypeScriptの代替ではなく、TypeScriptだけでは見られない外部入力を確認する。
- 図: unknown dataがZod gateを通ってtyped dataになる。

### F-212 OpenAPI

- tagline: APIのURL、入力、出力、認証方法をYAML/JSONで書くための仕様です。
- どこで出会うか: Swagger UI、API docs、SDK生成、外部サービス連携。
- 注意点: REST APIの説明書であり、APIそのものではない。
- 図: API仕様書からドキュメント、SDK、テスト、AI連携が枝分かれする。

### G-48 Structured Outputs

- tagline: LLMの返答を決まったJSONの形に寄せるための出力制御です。
- どこで出会うか: OpenAI API、AIからJSONを安定して受け取りたい場面。
- 注意点: 形は守れても、中身の事実性までは保証しない。
- 図: 自由文の回答と、schemaで整形されたJSON回答のBefore/After。

### F-213 tRPC

- tagline: TypeScriptだけでフロントエンドとバックエンドの型をつなぐAPI開発手法です。
- どこで出会うか: Next.js + TypeScriptの個人開発/業務アプリ。
- 注意点: TS中心の世界では便利だが、外部公開APIや多言語連携ではOpenAPIのほうが自然な場合もある。
- 図: フロントとサーバーが同じ型でつながる橋。

## 既存エントリへの補足提案

| 既存ID | 補足 |
|:--|:--|
| F-2 TypeScript | `Zod` と `JSON Schema` を related_terms に追加候補 |
| F-8 JSON | `JSON Schema` を単独エントリ化したら深掘り先としてリンク |
| F-7 YAML | `OpenAPI` を単独エントリ化したら「仕様を書く形式」としてリンク |
| F-122 Prisma | `Zod` はDB前ではなくAPI/入力検証側として関連づける |
| G-30 Tool Use | `JSON Schema` / `Structured Outputs` を関連候補に追加 |
| G-33 Function Calling | `JSON Schema` / `Structured Outputs` を関連候補に追加 |
| A-6 評価日 | サービス評価・著者コメントの時点依存ルールを追記 |

## 実装順

1. この案をレビューして、追加する語をA/B/Cに分ける
2. 優先度Aは `ledgers/entry_candidates.md` に F-210〜F-212 / G-48 を候補として追記
3. `ledgers/entries.csv` に採用分だけ追加
4. Zod / JSON Schema / OpenAPI の3件からスケルトンを作る
5. F-2 / F-7 / F-8 / G-30 / G-33 の related_terms を調整
6. A-6 に「著者コメントは評価日時点の体感」という注記を足す

## 参照メモ

- Zod docs: <https://zod.dev/> — Zod 4 stable、TypeScript-first validation、static type inference、JSON Schema conversion
- Zod JSON Schema docs: <https://zod.dev/json-schema> — `z.toJSONSchema()`、`z.fromJSONSchema()` は experimental
- OpenAPI Learn: <https://learn.openapis.org/specification/structure.html> — OpenAPI Descriptionの構造
- OpenAPI Specification: <https://spec.openapis.org/oas/v3.0.4.html> — OAS文書はJSON/YAMLで表現可能
