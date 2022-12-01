"""
Note: only for 3.10+
"""

from enum import Enum
from typing import NoReturn


class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"


"""
It will work, but the better solution is to use static type checker like `mypy`
"""
def exhaustiveness_check(value: NoReturn) -> NoReturn:
    assert False, f'This code should never be reached, got: {value}'


def foo(color: Color) -> str:
    match color:
        case Color.RED:
            return "Color is red"
        case Color.GREEN:
            return "Color is green"
    exhaustiveness_check(color)


foo(Color.RED)
foo(Color.BLUE)
