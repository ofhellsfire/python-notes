# Demonstrates customized exception

import io
import math
import sys

class TriangleError(Exception):

    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return f"'{self.args[0]}' for sides {self._sides}"

    def __repr__(self):
        return f'TriangleError({self.args[0]!r}, {self._sides!r})'

def triangle_area(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError('Illegal triangle', sides)
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a


def main():
    try:
        area = triangle_area(3, 4, 10)
        print(area)
    except TriangleError as ex:
        try:
            print(ex, file=sys.stdin)
        except io.UnsupportedOperation as f:
            print(ex)
            print(f)
            print(f.__context__ is ex)

main()

triangle_area(1, 1, 1)
triangle_area(1, 2, 100)  # raises the exception

