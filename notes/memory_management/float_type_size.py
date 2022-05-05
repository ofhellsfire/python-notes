"""
This example prints sizes of float type
"""

import sys

from pympler.asizeof import asizeof


def show_sizeof(x):
    print(f'`getsizeof`', x.__class__, sys.getsizeof(x), x)
    print(f'`asizeof`', x.__class__, asizeof(x), x)


if __name__ == '__main__':
    for i in range(1024):
        print(i)
        show_sizeof((2**i) * 1.0)
        print()
