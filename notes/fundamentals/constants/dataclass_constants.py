"""
Example showing `@dataclass` decorator for constants.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Constants:
    UNO = 1.2345
    DOS = 300


constants = Constants()


if __name__ == '__main__':
    print(constants.UNO)
    print(constants.DOS)
    constants.UNO = 3.14
