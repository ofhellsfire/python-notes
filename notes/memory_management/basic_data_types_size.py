"""
This example prints sizes of different basic data types
"""

import sys
from array import array


def show_sizeof(x, level=0):
    print(f'\t' * level, x.__class__, sys.getsizeof(x), x)

    if not isinstance(x, str) and hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)


class Foo:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def bar(self):
        return self.a * self.b - self.a


def baz():
    return 100


def qux():
    return 'alala'


def rut(a, b, c):
    return a + b + c


if __name__ == '__main__':
    types = (
        None,   # None
        53,     # int
        2**63,  # big int
        3.14159265358979,  # float
        "",  # empty string
        "some random string",  # string
        b"",  # empty bytes
        b"some random bytes",  # bytes
        # list
        [],  # empty list
        [1],  # uno
        [1, 2],  # dos
        [1, 2, 3],  # tres
        [1, 2, 3, 4],  # cuatro
        [1, 2, 3, 4, 5],  # sinco
        [1, 2, 3, 4, 5, 6],  # seis
        [3, "ololo", 123.45],  # various types list
        # tuple
        tuple(),               # empty tuple
        (1,),  # uno
        (1, 2),  # dos
        (1, 2, 3),  # tres
        (1, 2, 3, 4),  # cuatro
        (1, 2, 3, 4, 5),  # sinco
        (1, 2, 3, 4, 5, 6),  # seis
        (3, "ololo", 123.45),  # various types tuple
        # dict
        {},  # empty dict
        {'a': 1},  # uno
        {'a': 1, 'b': 2},  # dos
        {'a': 123, 'b': 456, 'c': 789},  # tres
        {'a': 123, 'b': 'alala', 'c': 834.91},  # various types dict
        # set
        set(),  # empty set
        {1},  # uno
        {1, 2},  # dos
        {1, 2, 3},  # tres
        {1, "alala", 456.123},  # various types set
        # array
        array('i', []),  # empty array
        array('i', [1]),  # uno
        array('i', [1, 2]),  # dos
        array('i', [1, 2, 3]),  # tres
        # class
        Foo,  # class itself
        Foo(1, 2),  # instance
        baz,  # simple function
        qux,  # simple function
        rut,  # function with parameters
    )
    for t in types:
        show_sizeof(t)
