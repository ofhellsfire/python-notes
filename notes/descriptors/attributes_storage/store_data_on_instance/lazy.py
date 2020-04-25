"""Example of lazy descriptor (set it and forget it descriptor).
It allows initializing attribute in a lazy manner: attribute is setup during its access.
"""

from random import randint


class Lazy:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        instance.__dict__[self.func.__name__] = value
        print('attribute value is set up')
        return value


def generate_value(_):  # TODO: pick up better example
    return randint(0, 100)


class Foo:

    attr = Lazy(generate_value)

    def __init__(self):
        pass


if __name__ == '__main__':
    print('before instance creation')
    foo1 = Foo()
    print('after instance creation')
    print('before attribute access')
    print(foo1.attr)
    print('after attribute access')
