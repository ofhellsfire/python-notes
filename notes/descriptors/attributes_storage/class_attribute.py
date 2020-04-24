"""
Pretty dumb class attribute example, which returns value from both: class and instance level.
The major problem here is inability to set value for class level attribute,
so class level attribue gets rewritten, because __set__() operates on instance level only.
"""

class ClassAttr:
    """Class Attribute"""

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('inside descriptor')
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Foo:

    attr1 = ClassAttr(100)
    attr2 = ClassAttr(200)

    def __init__(self):
        pass


if __name__ == '__main__':
    foo = Foo()
    print(Foo.attr1)
    print(Foo.attr2)
    print(foo.attr1)
    print(foo.attr2)

    print('----')

    Foo.attr1 = 400   # This will overwrite original descriptor
    print(Foo.attr1)  # This will be affected
    print(Foo.attr2)
    print(foo.attr1)  # This will be affected as well
    print(foo.attr2)

    print('----')

    foo.attr2 = 500
    print(Foo.attr1)
    print(Foo.attr2)
    print(foo.attr1)
    print(foo.attr2)
