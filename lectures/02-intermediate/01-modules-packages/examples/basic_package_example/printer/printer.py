class Printer:

    def __init__(self, message, decor_symbol='*'):
        self.message = message
        self.decor_symbol = decor_symbol * 3

    def print(self):
        print(f'{self.decor_symbol}{self.message}{self.decor_symbol}')
