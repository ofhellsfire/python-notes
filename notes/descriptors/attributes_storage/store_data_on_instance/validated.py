"""Example of 'validated' descriptor that stores data on instance using named location.

Issues:
1. No __slots__ support
2. Require setting location name explicitly
"""

class Validated:

    def __init__(self, location, validator):
        self.location = location
        self.validator = validator

    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.location] = value
        else:
            raise ValueError(f'Invalid value for "{self.location}"')


def validate(value):
    if isinstance(value, (int, float)):
        return True
    return False


class Foo:  # hashable object will work fine with this

    attr = Validated('attr', validate)

    def __init__(self, value):
        self.attr = value


class Bar:  # unhashable object

    attr = Validated('attr', validate)

    def __init__(self, value):
        self.attr = value

    __hash__ = None


class Baz:  # class with __slots__

    __slots__ = ()
    attr = Validated('attr', validate)

    def __init__(self, value):
        self.attr = value


class Qux:  # class with multiple attrs

    attr_a = Validated('attr_a', validate)
    attr_b = Validated('attr_b', validate)

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

    qux = Qux(3.14, 9.8)
    print(qux.attr_a)
    print(qux.attr_b)
    print('----')

    qux = Qux('ololo', 'alala')
    print(qux.attr_a)
    print(qux.attr_b)

    print('----')

    baz1 = Baz(500)
    baz2 = Baz(600)
    print(baz1.attr)
    print(baz2.attr)
