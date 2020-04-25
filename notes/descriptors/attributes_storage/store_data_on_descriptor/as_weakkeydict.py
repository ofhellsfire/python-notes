"""
Example of storing value for per-instance based class attribute, based on weak key dictionary.
It helps to solve memory leak when the object is gone and attribute is GCed

Issues:
1. No support for unhashable objects (like lists, sets, custom unhashable, etc..)
"""

from weakref import WeakKeyDictionary


class ClassAttr:

    def __init__(self):
        self.storage = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if not instance:
            return self  # or unbound attribute may be returned
        print('inside descriptor')
        return self.storage[instance]

    def __set__(self, instance, value):
        self.storage[instance] = value

    def __delete__(self, instance):
        del self.storage[instance]


class Foo:  # hashable object will work fine with this

    attr = ClassAttr()

    def __init__(self, value):
        self.attr = value


class Bar:  # unhashable object

    attr = ClassAttr()

    def __init__(self, value):
        self.attr = value

    __hash__ = None  # if we removed this, then solution would be fine


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
