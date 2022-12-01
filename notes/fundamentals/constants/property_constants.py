"""
Example showing `@property` decorator for constants.
"""

class Constants:

    @property
    def UNO(self):
        return 1.2345

    @property
    def DOS(self):
        return 300


constants = Constants()


if __name__ == '__main__':
    print(constants.UNO)
    print(constants.DOS)
    constants.UNO = 3.14
