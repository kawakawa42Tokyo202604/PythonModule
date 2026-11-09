# Python Module 06

## English

Exercises in loading functions from separate Python files. A single file is a module; related modules can be grouped into packages.

Alchemy-themed functions demonstrate different import styles. The examples also show problems caused by circular imports, where modules import each other.

### Exercises

| Location | Exercise |
| --- | --- |
| `ft_alembic_*.py` | Import syntax and package exports |
| `ft_distillation_*.py` | Calls between modules |
| `ft_transmutation_*.py` | Absolute and relative imports |
| `ft_kaboom_*.py` | Working and failing circular imports |
| [alchemy/](alchemy/) | Implementation with subpackages |

### Run

Requires Python 3.10 or newer, with no additional packages. Run from this directory.

```sh
python3 ft_alembic_0.py
python3 ft_transmutation_0.py
```

`ft_kaboom_1.py` intentionally demonstrates an unhandled circular-import error.

With Make, `make` checks syntax and `make run` runs `ft_alembic_0.py`. Set `ENTRY` and `ARGS` to choose a script and its arguments.

## 日本語

複数のPythonファイルに分けた関数を、別のファイルから読み込んで使う演習です。1つのファイルをモジュール、関連するモジュールをまとめたものをパッケージとして扱います。

錬金術を題材にした関数を呼び出し、読み込み方による違いを表示します。互いに読み込み合う「循環インポート」で起きる問題もデモに含めています。

### 演習

| 場所 | 内容 |
| --- | --- |
| `ft_alembic_*.py` | import構文とパッケージからの公開 |
| `ft_distillation_*.py` | モジュール間の関数呼び出し |
| `ft_transmutation_*.py` | 絶対・相対インポート |
| `ft_kaboom_*.py` | 循環インポートの成功例・失敗例 |
| [alchemy/](alchemy/) | サブパッケージを含む実装 |

### 実行

Python 3.10以降を使用します。追加パッケージは不要です。このディレクトリで実行します。

```sh
python3 ft_alembic_0.py
python3 ft_transmutation_0.py
```

このディレクトリから実行します。`ft_kaboom_1.py` は循環インポートによる未処理の例外を示すためのデモです。

Make を使う場合、`make` で構文を確認し、`make run` で `ft_alembic_0.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。
