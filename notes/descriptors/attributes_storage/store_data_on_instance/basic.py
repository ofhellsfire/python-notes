"""It's better to store data on the instance instead of on descriptor.

This example stores data on the instance by keeping it in instance __dict__
using hardcoded location.

Issues:
1. No __slots__ support
2. No support for multiple attribues of the same type
"""

class ClassAttr:

    location = 'descriptor_storage'

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.location]

    def __set__(self, instance, value):
        instance.__dict__[self.location] = value

    def __delete__(self, instance):
        del instance.__dict__[self.location]


class Foo:  # hashable object will work fine with this

    attr = ClassAttr()

    def __init__(self, value):
        self.attr = value


class Bar:  # unhashable object

    attr = ClassAttr()

    def __init__(self, value):
        self.attr = value

    __hash__ = None


class Baz:  # class with __slots__

    __slots__ = ()
    attr = ClassAttr()

    def __init__(self, value):
        self.attr = value


class Qux:  # class with multiple attrs

    attr_a = ClassAttr()
    attr_b = ClassAttr()

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
    print(qux.attr_a)  # this attribute value is overriden by the 'attr_b'
    print(qux.attr_b)

    print('----')

    baz1 = Baz(500)
    baz2 = Baz(600)
    print(baz1.attr)
    print(baz2.attr)
