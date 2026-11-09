# Python Module 08

## English

Exercises in preparing a Python runtime environment: isolating project packages with virtual environments, checking external dependencies, and passing runtime settings through environment variables.

The programs report environment status. One exercise uses additional packages to draw a scatter plot from random data; another inspects settings from a `.env` file.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Detect a virtual environment |
| [ex1](ex1/) | Check dependencies and visualize data |
| [ex2](ex2/) | Load configuration from .env |

### Run

Requires Python 3.10 or newer. Environment detection needs no additional packages.

```sh
python3 ex0/construct.py
```

Data visualization uses pandas, NumPy, and Matplotlib.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r ex1/requirements.txt
.venv/bin/python ex1/loading.py
```

The plot is saved as `matrix_analysis.png` in the working directory. Dependencies are defined in `ex1/requirements.txt` for pip and `ex1/pyproject.toml` for Poetry.

Run the configuration demonstration from `ex2`.

```sh
cd ex2
test -e .env || cp .env.example .env
python3 oracle.py
```

`.env.example` contains demonstration settings. `oracle.py` reads settings and displays status; it does not connect to a database or API.

`make` checks syntax; `make run` runs `ex0/construct.py`. Use `ENTRY` and `ARGS` to select a script and arguments. For the visualization in the virtual environment, use `make run PYTHON=.venv/bin/python ENTRY=ex1/loading.py`.

## 日本語

Pythonプログラムを動かす環境を整える演習です。プロジェクトごとにパッケージを分ける仮想環境、外部パッケージの有無の確認、実行時の設定を渡す環境変数を扱います。

実行すると環境の状態を表示します。追加パッケージを使う演習では、乱数データから散布図の画像を作り、別の演習では `.env` ファイルの設定値を確認します。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | 仮想環境の検出 |
| [ex1](ex1/) | 依存パッケージの確認とデータ可視化 |
| [ex2](ex2/) | .envからの設定読み込み |

### 実行

Python 3.10以降を使用します。仮想環境の検出は追加パッケージなしで実行できます。

```sh
python3 ex0/construct.py
```

データ可視化には pandas・NumPy・Matplotlib を使用します。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r ex1/requirements.txt
.venv/bin/python ex1/loading.py
```

`matrix_analysis.png` を実行したディレクトリに保存します。依存関係はpip用の `ex1/requirements.txt` と、Poetry用の `ex1/pyproject.toml` に定義しています。

設定読み込みのデモは `ex2` から実行します。

```sh
cd ex2
test -e .env || cp .env.example .env
python3 oracle.py
```

`.env.example` はデモ用の設定です。`oracle.py` は設定値を読み込んで状態を表示するプログラムで、DBやAPIへの接続処理は含みません。

Make を使う場合、`make` で構文を確認し、`make run` で `ex0/construct.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。

仮想環境のPythonを使う場合は、`make run PYTHON=.venv/bin/python ENTRY=ex1/loading.py` と指定します。
