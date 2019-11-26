# Demonstrates simple example of multiple inheritance

class Base1:

    def __init__(self):
        print('Base 1 init')

    def foo(self):
        print('foo')


class Base2:

    def __init__(self):
        print('Base 2 init')
        
    def bar(self):
        print('bar')


class Sub(Base1, Base2):
    def baz(self):
        print('baz')


sub = Sub()           # Will print: Base 1 init
sub.bar()             # Will print: bar
sub.foo()             # Will print: foo
print(Sub.__bases__)
