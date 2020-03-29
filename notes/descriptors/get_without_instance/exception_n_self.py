# When descriptor is meant to be for instance-level, and descriptor is used
# from class-level instead.
# We may raise exception or return `self`

class DumbStdDescriptor:

    def __init__(self, arg):
        self.arg = arg

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.arg * instance.a


class DumbExcDescriptor:

    def __init__(self, arg):
        self.arg = arg

    def __get__(self, instance, owner):
        if instance is None:
            raise Exception('Invoking descriptor not from an instance-level')
        return self.arg * instance.a


class Foo:

    attrA = DumbStdDescriptor(3)
    attrB = DumbExcDescriptor(5)

    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    foo = Foo(100)
    print(foo.attrA)
    print(Foo.attrA)
    print(foo.attrB)
    print(Foo.attrB)
