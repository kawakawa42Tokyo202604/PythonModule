# Matrix Loader

## English

A Python program that checks for required packages and creates a scatter plot from random numeric data. It saves the plot as `matrix_analysis.png`.

pandas handles tabular data, NumPy supplies numeric data, and Matplotlib draws the plot. Missing packages are reported with installation instructions.

### Run

Requires Python 3.10 or newer. Create a virtual environment and prepare dependencies in this directory.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
make
make run PYTHON=.venv/bin/python
```

If the packages are available, the program saves `matrix_analysis.png`. Otherwise, it lists the missing packages and how to install them.

### Files

| File | Purpose |
| --- | --- |
| [requirements.txt](requirements.txt) | Dependencies for pip |
| [pyproject.toml](pyproject.toml) | Project definition for Poetry |
| [loading.py](loading.py) | Dependency checks, data generation, and plot output |

## 日本語

必要な外部パッケージが揃っているかを調べ、ランダムな数値データから散布図を作るPythonプログラムです。グラフは `matrix_analysis.png` に保存します。

pandasは表形式のデータ、NumPyは数値データ、Matplotlibは描画に使います。足りないパッケージがある場合は、その名前と導入方法を表示します。

### 実行

Python 3.10以降を使います。このディレクトリで仮想環境を作り、依存パッケージを準備します。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
make
make run PYTHON=.venv/bin/python
```

依存パッケージが揃っていれば `matrix_analysis.png` を保存し、不足していれば該当パッケージと導入方法を表示します。

### ファイル

| ファイル | 用途 |
| --- | --- |
| [requirements.txt](requirements.txt) | pip用の依存関係 |
| [pyproject.toml](pyproject.toml) | Poetry用のプロジェクト定義 |
| [loading.py](loading.py) | 依存確認・データ生成・グラフ保存 |
