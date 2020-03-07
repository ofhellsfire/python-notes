from functools import partial


class CustomClassmethod:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print('inside custom getter')
        return partial(self.func, owner)


class Sum:

    def __init__(self, *args):
        self.items = args

    @CustomClassmethod
    def from_list(cls, lst):
        return cls(*lst)

    def __call__(self):
        return sum(self.items)

    def _from_dict(cls, d):
        return cls(*d.values())

    from_dict = CustomClassmethod(_from_dict)


if __name__ == '__main__':
    foo = Sum(5, 15, 23, -20, -43)
    print(foo())
    other_foo = Sum.from_list([5, -44, 23, -20, 16])
    print(other_foo())
    another_foo = Sum.from_dict(dict(a=5, b=10, c=15, d=33))
    print(another_foo())
