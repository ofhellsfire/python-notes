# Demonstrates exception chaining

import math


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as ex:
        raise InclinationError('Slope cannot be vertical') from ex


try:
    inclination(0, 5)
except InclinationError as ex:
    print(ex)
    print(ex.__cause__)