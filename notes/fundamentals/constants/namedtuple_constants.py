"""
Example showing `namedtuple()` factory function for constants.
"""

from collections import namedtuple


Constants = namedtuple(
    "Constants",
    ["UNO", "DOS"],
)


constants = Constants(
    UNO=1.2345,
    DOS=300
)


if __name__ == '__main__':
    print(constants.UNO)
    print(constants.DOS)
    constants.UNO = 3.14
