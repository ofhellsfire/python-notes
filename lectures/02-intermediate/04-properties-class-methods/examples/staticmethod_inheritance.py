class MyBase:

    @staticmethod
    def baz():
        return 'baz() from MyBase'


class Foo(MyBase):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


class Bar(MyBase):

    def __init__(self, c):
        self.c = c

    def multi(self, n):
        return pow(self.c, n)

    @staticmethod
    def baz():
        return 'baz() from Bar'


print(MyBase.baz())
print(Foo.baz())
foo = Foo(1, 2)
print(foo.baz())
print(Bar.baz())
bar = Bar(100)
print(bar.baz())
