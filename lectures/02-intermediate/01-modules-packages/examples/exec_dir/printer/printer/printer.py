class Printer:

    def __init__(self, msg):
        self.msg = msg

    def print(self):
        print(''.join(reversed(self.msg)))
