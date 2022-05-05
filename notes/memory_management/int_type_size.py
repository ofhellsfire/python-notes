"""
This example prints sizes of int type
"""

import sys

from pympler.asizeof import asizeof


def show_sizeof(x):
    print(f'`getsizeof`', x.__class__, sys.getsizeof(x), x)
    print(f'`asizeof`', x.__class__, asizeof(x), x)


if __name__ == '__main__':
    for i in range(122):
        print(i)
        show_sizeof(2**i)
        print()
