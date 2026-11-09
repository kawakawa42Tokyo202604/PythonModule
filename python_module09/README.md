# Python Module 09

## English

Python exercises that check whether space-station and crew data satisfy defined rules. Pydantic models specify field types and allowed value ranges.

For example, a space station accepts a crew size from 1 to 20. Valid data is accepted; values outside the range produce validation errors. Later exercises validate missions containing multiple related records.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Basic space-station model and value limits |
| [ex1](ex1/) | Enums and model-wide validation |
| [ex2](ex2/) | Nested crew and mission models |

### Run

Requires Python 3.10 or newer and Pydantic 2.x. Create a virtual environment in this module directory.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install 'pydantic>=2,<3'
.venv/bin/python ex0/space_station.py
.venv/bin/python ex1/alien_contact.py
.venv/bin/python ex2/space_crew.py
```

The demos display accepted data and validation errors for invalid values. `ex1` and `ex2` use `model_validator`.

`make` checks syntax; `make run` runs `ex0/space_station.py`. Use `ENTRY` and `ARGS` to select a script and arguments. To use the environment above, run `make run PYTHON=.venv/bin/python`.

## 日本語

宇宙ステーションや乗組員のデータが、決めた条件に合っているか検査するPython演習です。Pydanticというライブラリで、文字列・数値などの型や、値の範囲を定義します。

例えば宇宙ステーションの人数は1〜20人です。条件を満たすデータは受け付け、範囲外の数値などには検証エラーを表示します。複数のデータを組み合わせた任務の検証も扱います。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | 宇宙ステーションの基本モデルと値の範囲 |
| [ex1](ex1/) | 列挙型とモデル全体の検証 |
| [ex2](ex2/) | 乗組員・任務を組み合わせたモデル |

### 実行

Python 3.10以降と Pydantic 2系が必要です。モジュールのディレクトリで仮想環境を用意します。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install 'pydantic>=2,<3'
.venv/bin/python ex0/space_station.py
.venv/bin/python ex1/alien_contact.py
.venv/bin/python ex2/space_crew.py
```

正常なデータの生成と、不正な値に対する検証エラーを表示します。`ex1`・`ex2` は `model_validator` を使用します。

Make を使う場合、`make` で構文を確認し、`make run` で `ex0/space_station.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。

上の仮想環境で実行する場合は `make run PYTHON=.venv/bin/python` と指定します。
