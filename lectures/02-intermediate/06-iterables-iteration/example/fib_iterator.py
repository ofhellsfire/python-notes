# Fibonacci Iterator

class Fibonacci:

    def __init__(self, nmax=None):
        self.a = None
        self.b = None
        self.nmax = nmax
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.nmax is not None and self.nmax < self.index:
            raise StopIteration
        self.a, self.b = (self.b, self.a + self.b) if self.index != 0 else (0, 1)
        self.index += 1
        return self.a


if __name__ == '__main__':
    fib = Fibonacci(10)
    for i in fib:
        print(i)
