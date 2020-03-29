# When descriptor is meant to be for instance-level, and descriptor is used
# from class-level instead, then
# we may use unbound attribute

class DumbUnboundAttr:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        if instance is None:
            def unboundattr(inst):
                return self.__get__(inst, owner)
            return unboundattr
        return self.value * instance.a


class UnboundAttribute:

    def __init__(self, descriptor, owner):
        self.descriptor = descriptor
        self.owner = owner

    def __call__(self, instance):
        return self.descriptor.__get__(instance, self.owner)


class Attr:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        if instance is None:
            return UnboundAttribute(self, owner)
        return self.value * instance.a


class Foo:

    attrA = DumbUnboundAttr(15)
    attrB = Attr(22)

    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    foo = Foo(10)
    print(foo.attrA)
    print(Foo.attrA)
    print(foo.attrB)
    print(Foo.attrB)

    print('-' * 32)

    inst1 = Foo(100)
    inst2 = Foo(200)
    inst3 = Foo(300)
    inst4 = Foo(400)
    data = [inst1, inst2, inst3, inst4]
    print(list(map(lambda c: c.attrA, data)))
    print(list(map(Foo.attrB, data)))