from collections.abc import Sequence
import datetime
import functools

from multipledispatch import dispatch


@functools.singledispatch
def format(arg):
    return arg


@format.register
def _(arg: datetime.date):
    return f'{arg.day}-{arg.month}-{arg.year}'


@format.register
def _(arg: datetime.datetime):
    return f'{arg.day}-{arg.month}-{arg.year} {arg.hour}:{arg.minute}:{arg.second}'


@format.register
def _(arg: datetime.time):
    return f'{arg.hour}:{arg.minute}:{arg.second}'


class Formatter:

    @functools.singledispatchmethod
    def format(self, arg):
        raise NotImplementedError(f'Cannot format value of type {type(arg)}')

    @format.register
    def _(self, arg: datetime.date):
        return f'{arg.day}-{arg.month}-{arg.year}'

    @format.register
    def _(self, arg: datetime.time):
        return f'{arg.hour}:{arg.minute}:{arg.second}'


@dispatch(list, str)
def concatenate(a, b):
    a.append(b)
    return a


@dispatch(str, str)
def concatenate(a, b):
    return a + b


@dispatch(str, int)
def concatenate(a, b):
    return a + str(b)


@dispatch((list, tuple), (str, int))
def concatenate(a, b):
    return list(a) + [b]


@dispatch(Sequence, tuple)
def concatenate(a, b):
    return list(a) + [b]


@dispatch(object, object)  # base implementation example
def concatenate(a, b):
    return f'Given argument types are not supported'


if __name__ == '__main__':
    # Singledispatch function
    print(format('today'))
    print(format(datetime.date(2021, 5, 26)))
    print(format(datetime.datetime(2021, 5, 26, 17, 25, 10)))
    print(format(datetime.time(19, 22, 15)))

    # Singledispatch method
    fmt = Formatter()
    print(fmt.format(datetime.date(2021, 6, 14)))
    print(fmt.format(datetime.time(22, 3, 53)))

    # Multipledispatch
    print(concatenate(['a', 'b'], 'c'))
    print(concatenate('Hello ', 'World'))
    print(concatenate('a', 1))
    print(concatenate((1, 3, 5), '7'))
    print(concatenate((1, 2), [3, 4]))
    print(concatenate([1, 2, 3], ('1', '1')))
