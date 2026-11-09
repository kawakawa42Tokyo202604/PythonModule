"""Demonstrate the execution-time decorator."""

from decorator_mastery import spell_timer


@spell_timer
def answer() -> int:
    return 42


def main() -> None:
    print(answer())


if __name__ == "__main__":
    main()
