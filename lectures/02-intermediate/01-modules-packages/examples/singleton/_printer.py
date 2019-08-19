from time import time


class Printer:

    def __init__(self, msg=None):
        self.time_creation = time()
        self.msg = msg

    def print(self):
        print(self.msg)

    def rev_print(self):
        print(''.join(reversed(self.msg)))
