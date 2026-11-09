# Python Module 02

## English

Python exercises for reporting problems and handling invalid input or failed file reads. An exception signals that normal processing cannot continue.

The demos catch number-conversion errors, define custom errors, and perform cleanup even when an error occurs.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Catch conversion errors |
| [ex1](ex1/) | Raise errors for invalid conditions |
| [ex2](ex2/) | Handle multiple exception types |
| [ex3](ex3/) | Define custom exception classes |
| [ex4](ex4/) | Use finally for cleanup |

### Run

Requires Python 3.10 or newer, with no additional packages. Run from this directory.

```sh
python3 ex0/ft_first_exception.py
python3 ex4/ft_finally_block.py
```

Each file includes demonstrations with valid and invalid input. Error messages in the output illustrate handled exceptions.

With Make, `make` checks syntax and `make run` runs `ex0/ft_first_exception.py`. Set `ENTRY` and `ARGS` to choose a script and its arguments.

## 日本語

不正な入力やファイルの読み込み失敗が起きても、原因を知らせて処理を進めるためのPython演習です。例外とは、通常の処理を続けられないことをプログラムに知らせる仕組みです。

数値変換の失敗を捕まえる、独自のエラーを作る、エラーが起きても後片付けする、といった動作をデモで確認します。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | 型変換エラーの捕捉 |
| [ex1](ex1/) | 条件に応じた例外の送出 |
| [ex2](ex2/) | 複数の例外を処理 |
| [ex3](ex3/) | 独自の例外クラス |
| [ex4](ex4/) | finallyによる終了処理 |

### 実行

Python 3.10以降を使用します。追加パッケージは不要です。このディレクトリで実行します。

```sh
python3 ex0/ft_first_exception.py
python3 ex4/ft_finally_block.py
```

正常入力とエラー入力を使うデモを各ファイルに含めています。出力中のエラー表示は、例外を処理する動作例です。

Make を使う場合、`make` で構文を確認し、`make run` で `ex0/ft_first_exception.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。
