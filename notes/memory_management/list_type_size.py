"""
This example prints sizes of float type
"""

from pprint import pp
import sys


def show_sizeof(x, level=0):
    print(f'\t' * level, x.__class__, sys.getsizeof(x), x[-5:])
    return sys.getsizeof(x)


if __name__ == '__main__':
    res = {}
    for i in range(102):
        temp_list = []
        for k in range(i):
            temp_list.append(k)
        print(len(temp_list), temp_list[-5:])
        size = show_sizeof(temp_list)
        res[i] = size
        print()
    pp(res)