*This project has been created as part of the 42 curriculum by hwakatsu.*

# Code Nexus

## Description / 説明

### English
Code Nexus is a Python project about method overriding and subtype polymorphism in data-processing systems. Its goal is to build several inheritance-based processing layers that share common interfaces while providing specialized behavior for different kinds of data.

This repository contains three progressive exercises:

- `ex0/stream_processor.py`: abstract processors for numeric, text, and log data
- `ex1/data_stream.py`: polymorphic stream classes for sensor, transaction, and event batches
- `ex2/nexus_pipeline.py`: a larger pipeline architecture with stages, adapters, and a manager

From the code in this repository, the project demonstrates:

- abstract base classes for shared processing contracts
- overridden methods that adapt behavior to numeric, text, log, sensor, transaction, and event data
- a stream manager that handles multiple stream subtypes through a common interface
- a pipeline system using `Protocol`, abstract classes, stage chaining, adapters, and recovery logic

### 日本語
Code Nexus は、データ処理システムにおける method overriding と subtype polymorphism を学ぶ Python プロジェクトです。目的は、共通インターフェースを保ちながら、異なるデータ種別に対して特化した振る舞いを提供する複数の継承ベース処理レイヤーを構築することです。

このリポジトリには、段階的な 3 つの exercise があります。

- `ex0/stream_processor.py`: 数値、テキスト、ログを扱う抽象プロセッサ
- `ex1/data_stream.py`: センサー、トランザクション、イベントのバッチを扱うポリモーフィックなストリームクラス
- `ex2/nexus_pipeline.py`: stage、adapter、manager を備えた大きめのパイプライン構成

このリポジトリの実装では、次の内容が確認できます。

- 共通処理契約を定義する抽象基底クラス
- 数値、テキスト、ログ、センサー、トランザクション、イベントごとに動作を変えるオーバーライド
- 共通インターフェースを通して複数のストリーム subtype を処理する stream manager
- `Protocol`、抽象クラス、stage 連結、adapter、復旧処理を使った pipeline システム

## Instructions / 実行方法

### English

Requirements:

- Python 3.10 or later
- No external dependencies

Run each exercise from the repository root:

```bash
python3 ex0/stream_processor.py
python3 ex1/data_stream.py
python3 ex2/nexus_pipeline.py
```

Optional lint check:

```bash
flake8 ex0 ex1 ex2
```

There is no installation or compilation step. The project uses only the Python standard library.

### 日本語

必要環境:

- Python 3.10 以上
- 外部依存関係なし

リポジトリのルートで、各 exercise は次のように実行できます。

```bash
python3 ex0/stream_processor.py
python3 ex1/data_stream.py
python3 ex2/nexus_pipeline.py
```

任意の lint チェック:

```bash
flake8 ex0 ex1 ex2
```

インストールやコンパイルは不要です。このプロジェクトは Python 標準ライブラリのみを使用します。

## Features / 主な内容

### English

- `DataProcessor` defines a shared interface with `process()`, `validate()`, and `format_output()`.
- `NumericProcessor`, `TextProcessor`, and `LogProcessor` override processing rules for different input types.
- `DataStream` provides shared batch and filtering behavior that subclasses specialize.
- `StreamProcessor` works with different stream types polymorphically.
- `ProcessingPipeline` and adapter subclasses demonstrate staged processing and recovery behavior.
- `NexusManager` orchestrates multiple pipelines and simulates multi-format processing.

### 日本語

- `DataProcessor` は `process()`、`validate()`、`format_output()` を持つ共通インターフェースを定義します。
- `NumericProcessor`、`TextProcessor`、`LogProcessor` は入力型ごとに処理ルールをオーバーライドします。
- `DataStream` は共有のバッチ処理とフィルタ動作を提供し、各 subclass がそれを特化します。
- `StreamProcessor` は異なる stream 型をポリモーフィックに扱います。
- `ProcessingPipeline` と adapter subclass は stage ベースの処理と復旧動作を示します。
- `NexusManager` は複数 pipeline を統括し、複数フォーマットの処理を模擬します。

## Usage Overview / 使い方の概要

### English

- `ex0` demonstrates the same processor interface applied to multiple data types.
- `ex1` demonstrates batch-oriented stream processing and domain-specific filtering.
- `ex2` demonstrates staged pipeline execution for JSON-like, CSV-like, and stream-style inputs.

### 日本語

- `ex0` では同じ processor インターフェースを複数データ型に適用する様子を示します。
- `ex1` ではバッチ単位の stream 処理とドメイン別フィルタリングを示します。
- `ex2` では JSON 風、CSV 風、リアルタイム stream 風の入力に対する段階的 pipeline 処理を示します。

## Resources / 参考資料

### English

Classic references related to the topic:

- [Python Documentation: abc](https://docs.python.org/3/library/abc.html)
- [Python Documentation: typing](https://docs.python.org/3/library/typing.html)
- [Python Documentation: collections](https://docs.python.org/3/library/collections.html)
- [Python Documentation: isinstance](https://docs.python.org/3/library/functions.html#isinstance)
- [Real Python: Polymorphism in Python](https://realpython.com/polymorphism-python/)
- [Real Python: Duck Typing and Protocols](https://realpython.com/duck-typing-python/)
- [flake8 Documentation](https://flake8.pycqa.org/)

AI usage in this project:

- AI was used for documentation support and README drafting.
- It was used to inspect the repository structure, summarize the implemented processing architecture, and produce bilingual English/Japanese wording.

### 日本語

この課題に関連する代表的な参考資料:

- [Python Documentation: abc](https://docs.python.org/3/library/abc.html)
- [Python Documentation: typing](https://docs.python.org/3/library/typing.html)
- [Python Documentation: collections](https://docs.python.org/3/library/collections.html)
- [Python Documentation: isinstance](https://docs.python.org/3/library/functions.html#isinstance)
- [Real Python: Polymorphism in Python](https://realpython.com/polymorphism-python/)
- [Real Python: Duck Typing and Protocols](https://realpython.com/duck-typing-python/)
- [flake8 Documentation](https://flake8.pycqa.org/)

このプロジェクトにおける AI の利用:

- AI はドキュメント補助と README 作成支援に使用しました。
- リポジトリ構造の確認、実装された処理アーキテクチャの要約、英語と日本語の文章作成に利用しました。

## Notes / 補足

### English
The project is centered on design clarity rather than production-scale data engineering. The important part is showing how common interfaces and overridden methods allow one system to process different data forms cleanly.

### 日本語
このプロジェクトは本格的な大規模データ処理よりも、設計の明確さを重視しています。重要なのは、共通インターフェースとオーバーライドされたメソッドによって、1 つの仕組みで異なるデータ形態をきれいに処理できることを示す点です。
