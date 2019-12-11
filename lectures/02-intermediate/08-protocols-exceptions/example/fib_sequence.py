# Demonstrates simple sequence protocol implementation by Fibonacci Sequence

# NOTE: Don't use it on production, for demo purpose only

from collections.abc import Sequence


class Fibonacci(Sequence):

    def __init__(self, nmax):
        self.length = nmax
        self._items = []
        self._calculate()

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def _calculate(self, a=0, b=1):
        if self.length == len(self):
            return
        self._items.append(a)
        self._calculate(b, a + b)


fibseq = Fibonacci(10)
print(f'The 6th Fibonacci number is: {fibseq[5]}')

print('Iterating through Fibonacci sequence...')
for index, number in enumerate(fibseq, 1):
    print(f'{index} is {number}')

# The following implementation we get for free
print(f'Check if 27 in Fibonacci sequence: {27 in fibseq}')
print(f'Check if 13 in Fibonacci sequence: {13 in fibseq}')

print('Iterating through reversed Fibonacci sequence...')
for index, number in enumerate(reversed(fibseq), 1):
    print(f'{index} is {number}')
