# Demonstrates traceback objects

import math
import traceback


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as ex:
        raise InclinationError('Slope cannot be vertical') from ex


def main():
    try:
        inclination(0, 5)
    except InclinationError as ex:
        traceback.print_tb(ex.__traceback__)  # printing directly
        s = traceback.format_tb(ex.__traceback__)  # saving to variable
        print(s)


main()
