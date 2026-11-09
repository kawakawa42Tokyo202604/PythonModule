# Python Module 04

## English

Python exercises for reading, displaying, transforming, and saving text files. They also cover terminal input and separate streams for normal output and error messages.

The demos handle missing files and use `with` statements to ensure files are closed after use.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Read a text file |
| [ex1](ex1/) | Transform and save file contents |
| [ex2](ex2/) | Use standard input, output, and error |
| [ex3](ex3/) | Handle file errors with context managers |

### Run

Requires Python 3.10 or newer, with no additional packages. Run from this directory.

```sh
printf 'Hello, archives!\n' > sample.txt
python3 ex0/ft_ancient_text.py sample.txt
python3 ex3/ft_vault_security.py
```

`ex1` and `ex2` take an input filename as an argument and ask for an output path interactively. Leaving it blank skips writing a file.

With Make, `make` checks syntax and `make run` runs `ex3/ft_vault_security.py`. Set `ENTRY` and `ARGS` to choose a script and its arguments.

## 日本語

テキストファイルを読み、内容を表示・加工・保存するPython演習です。端末から入力を受け取り、通常の結果とエラーメッセージの出力先を分ける方法も扱います。

ファイルが見つからない場合の対応や、処理後にファイルを確実に閉じる `with` 文を、付属のデモで確認できます。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | テキストファイルの読み込み |
| [ex1](ex1/) | 読み込んだ内容を加工して保存 |
| [ex2](ex2/) | 標準入力・標準出力・標準エラー出力 |
| [ex3](ex3/) | with文とファイル処理の例外対応 |

### 実行

Python 3.10以降を使用します。追加パッケージは不要です。このディレクトリで実行します。

```sh
printf 'Hello, archives!\n' > sample.txt
python3 ex0/ft_ancient_text.py sample.txt
python3 ex3/ft_vault_security.py
```

`ex1` と `ex2` は入力ファイル名を引数に取り、加工後の保存先を対話入力します。保存先を空欄にすると、ファイルへは書き込みません。

Make を使う場合、`make` で構文を確認し、`make run` で `ex3/ft_vault_security.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。
