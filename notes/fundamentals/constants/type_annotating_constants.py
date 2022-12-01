from typing import Final


MAX_SPEED: Final[int] = 300
DEFAULT_COLOR: Final[str] = "\033[1;34m"
ALLOWED_BUILTINS: Final[tuple[str, ...]] = ("sum", "max", "min", "abs")


if __name__ == "__main__":
    MAX_SPEED = 450  # static type checker must give an error here
