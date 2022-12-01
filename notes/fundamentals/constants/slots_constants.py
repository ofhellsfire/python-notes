"""
Example showing `__slots__` attribute for constants and it's memory consumption.
"""

class Constants:
    __slots__ = ()
    UNO = 1.2345
    DOS = 300


constants = Constants()


if __name__ == '__main__':
    print(constants.UNO)
    print(constants.DOS)
    constants.UNO = 3.14
