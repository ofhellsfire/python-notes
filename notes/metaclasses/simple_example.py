class Meta(type):

    def __new__(meta, name, bases, class_dict):
        print(f"{meta=}, {name=}, {bases=}, {class_dict=}")
        return type.__new__(meta, name, bases, class_dict)


class MyClass(metaclass=Meta):
    foo = 33

    def foo(self, a, b):
        return a + b
