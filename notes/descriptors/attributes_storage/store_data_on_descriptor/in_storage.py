"""Example of storing value for per-instance based class attribute, based on custom storage.
It helps to solve memory leak when the object is gone and attribute is GCed,
and it allows having unhashable object attributes as well

Drawbacks:

1. Slight processing overhead against simple alternatives 
"""

import weakref


class DescriptorStorage:  # TODO: complete object with dict methods

    def __init__(self, **kwargs):
        self.storage = {}
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __getitem__(self, key):
        return self.storage[id(key)]

    def __setitem__(self, key, value):
        self.storage[id(key)] = value
        weakref.finalize(key, self.storage.__delitem__, id(key))

    def __delitem__(self, key):
        del self.storage[id(key)]


class ClassAttr:

    def __init__(self):
        self.storage = DescriptorStorage()

    def __get__(self, instance, owner):
        if not instance:
            return self
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

    __hash__ = None


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
