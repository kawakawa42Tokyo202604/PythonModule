# Python Module 05

## English

Python exercises that put numeric, text, and log processing into classes with a common calling interface. Different data types can follow a shared processing flow.

Starting with individual processors, the exercises build pipelines and CSV/JSON output plugins. Each demo displays the results of processing sample data.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Numeric, text, and log processors |
| [ex1](ex1/) | Data streams using processing classes |
| [ex2](ex2/) | CSV and JSON output plugins |

### Run

Requires Python 3.10 or newer, with no additional packages. Run from this directory.

```sh
python3 ex0/data_processor.py
python3 ex2/data_pipeline.py
```

With Make, `make` checks syntax and `make run` runs `ex0/data_processor.py`. Set `ENTRY` and `ARGS` to choose a script and its arguments.

## 日本語

数値・文字列・ログに対する処理をクラスに分け、同じ呼び出し方で使うPython演習です。処理対象が変わっても、集計・変換などの共通した流れを組み立てられる設計を学びます。

数値用・テキスト用の処理クラスから始め、複数の処理をつなぐパイプラインや、CSV・JSON形式の出力へ広げます。各デモはサンプルデータの処理結果を表示します。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | 数値・テキスト・ログの処理クラス |
| [ex1](ex1/) | 処理クラスを使うデータストリーム |
| [ex2](ex2/) | CSV・JSON形式の出力プラグイン |

### 実行

Python 3.10以降を使用します。追加パッケージは不要です。このディレクトリで実行します。

```sh
python3 ex0/data_processor.py
python3 ex2/data_pipeline.py
```

Make を使う場合、`make` で構文を確認し、`make run` で `ex0/data_processor.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。
