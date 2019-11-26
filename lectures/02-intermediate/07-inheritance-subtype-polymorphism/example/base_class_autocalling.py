# Demonstrates base class autocalling

class Base:

    def __init__(self):
        print('inside BASE class')


class Foo(Base):

    def __init__(self):
        print('inside init Foo class')


class Bar(Base):

    def do_something(self):
        print('do something from Bar class')


f = Foo()  # Will print: inside init Foo class
b = Bar()  # Will print: inside BASE class
