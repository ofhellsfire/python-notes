"""It's better to store data on the instance instead of on descriptor.

This example stores data on the instance by keeping it in instance __dict__
using named location.

Issues:
1. No __slots__ support
2. Require setting location name explicitly
"""

class ClassAttr:

    def __init__(self, location):
        self.location = location

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.location]

    def __set__(self, instance, value):
        instance.__dict__[self.location] = value

    def __delete__(self, instance):
        del instance.__dict__[self.location]


class Foo:  # hashable object will work fine with this

    attr = ClassAttr('Foo')

    def __init__(self, value):
        self.attr = value


class Bar:  # unhashable object

    attr = ClassAttr('Bar')

    def __init__(self, value):
        self.attr = value

    __hash__ = None


class Baz:  # class with __slots__

    __slots__ = ()
    attr = ClassAttr('Baz')

    def __init__(self, value):
        self.attr = value


class Qux:  # class with multiple attrs

    attr_a = ClassAttr('a')
    attr_b = ClassAttr('b')

    def __init__(self, a, b):
        self.attr_a = a
        self.attr_b = b


if __name__ == '__main__':
    foo1 = Foo(100)
    foo2 = Foo(200)
    print(foo1.attr)
    print(foo2.attr)

    del foo1  # check Foo class contents after this line to make sure you don't get a leakage

    print('----')

    bar1 = Bar(300)
    bar2 = Bar(400)
    print(bar1.attr)
    print(bar2.attr)

    print('----')

    qux = Qux('ololo', 'alala')
    print(qux.attr_a)
    print(qux.attr_b)

    print('----')

    baz1 = Baz(500)
    baz2 = Baz(600)
    print(baz1.attr)
    print(baz2.attr)
