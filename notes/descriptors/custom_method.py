from functools import partial


class CustomMethod:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return partial(self, instance)


def add(self):
    return self.a + self.b


class Foo:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    add = CustomMethod(add)


if __name__ == '__main__':
    foo = Foo(100, 115)
    print(foo.add())
