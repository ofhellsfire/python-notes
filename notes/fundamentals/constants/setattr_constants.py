"""
Example showing `__setattr__()` special method for constants.
"""

class Constants:

    UNO = 1.2345
    DOS = 300

    def __setattr__(self, name, value):
        raise AttributeError(f"can't reassign constant '{name}'")


constants = Constants()


if __name__ == '__main__':
    print(constants.UNO)
    print(constants.DOS)
    constants.UNO = 3.14
