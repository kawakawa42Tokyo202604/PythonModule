# Python Module 03

## English

Python lists, tuples, sets, and dictionaries applied to game scores, coordinates, achievements, and inventory. Store multiple values, calculate summaries, remove duplicates, and retrieve relevant data.

For example, passing scores `10 20 30` displays a total of `60` and average of `20.0`. Generators demonstrate producing values as needed instead of creating them all at once.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Read command-line arguments |
| [ex1](ex1/) | Analyze scores with lists |
| [ex2](ex2/) | Represent coordinates with tuples |
| [ex3](ex3/) | Manage achievements with sets |
| [ex4](ex4/) | Manage inventory with dictionaries |
| [ex5](ex5/) | Generate events lazily |
| [ex6](ex6/) | Transform data with comprehensions |

### Run

Requires Python 3.10 or newer, with no additional packages. Run from this directory.

```sh
python3 ex0/ft_command_quest.py hello world
python3 ex1/ft_score_analytics.py 10 20 30
```

With Make, `make` checks syntax and `make run` runs `ex0/ft_command_quest.py`. Set `ENTRY` and `ARGS` to choose a script and its arguments.

## 日本語

ゲームのスコア・座標・実績・在庫などのデータを、Pythonのリスト・タプル・集合・辞書で扱う演習です。複数の値をまとめて保存し、集計や重複の除去、必要な値の取り出しを行います。

例えばスコア集計に `10 20 30` を渡すと、合計 `60` や平均 `20.0` を表示します。大量の値を一度に作らず、必要な分ずつ生成するジェネレータも扱います。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | コマンドライン引数 |
| [ex1](ex1/) | リストによるスコア集計 |
| [ex2](ex2/) | 座標とタプル |
| [ex3](ex3/) | 集合による実績の管理 |
| [ex4](ex4/) | 辞書による在庫管理 |
| [ex5](ex5/) | ジェネレータによるイベント生成 |
| [ex6](ex6/) | 内包表記によるデータ加工 |

### 実行

Python 3.10以降を使用します。追加パッケージは不要です。このディレクトリで実行します。

```sh
python3 ex0/ft_command_quest.py hello world
python3 ex1/ft_score_analytics.py 10 20 30
```

Make を使う場合、`make` で構文を確認し、`make run` で `ex0/ft_command_quest.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。
