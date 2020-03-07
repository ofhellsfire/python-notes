class CustomStaticmethod:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func


class Foo:

    @CustomStaticmethod
    def static_foo():
        return 'hello from "static_foo()"'

    def _static_mul(a, b, c):
        return a * b * c

    static_mul = CustomStaticmethod(_static_mul)


if __name__ == '__main__':
    print(Foo.static_foo())
    print(Foo.static_mul(10, 20, 30))