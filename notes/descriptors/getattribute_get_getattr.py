"""
Order Priority

1. First __getattribute__() is called (if defined)
2. Then data descriptors
3. Then instance attributes
4. Then nondata descriptors and class attributes
5. Finally __getattr__() is called (if defined)

`__getattr__()` is only invoked if the attribute wasn't found the usual ways.
It's good for implementing a fallback for missing attributes.

If `__getattribute__()` method is defined, then Python invokes this method for
every attribute access regardless whether it exists or not.
One good usage is that it can prevent access to attributes and make
them more secure.
In order to avoid infinite recursion in `__getattribute__()` method,
its implementation should always call the base class method with the same
name to access any attributes it needs.
"""

class DumbDescriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('inside dumb descriptor')
        return self.value


class Foo:

    c = DumbDescriptor(100)

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __getattribute__(self, name):
        if name in ('c', 'd'):
            print(f'inside "getattribute" method: {name}')
        if name == 'd':
            raise AttributeError
        return super().__getattribute__(name)

    def __getattr__(self, name):
        if name in ('c', 'd'):
            print(f'inside "getattr" method: {name}')
        return 0


if __name__ == '__main__':
    foo = Foo(10, 20)
    print(foo.c)
    print(foo.d)
    print(foo.a)
