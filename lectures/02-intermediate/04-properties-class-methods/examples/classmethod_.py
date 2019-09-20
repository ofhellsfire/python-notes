# Named constructors example

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'(x = {self.x}, y = {self.y})'


class Quadangle:

    def __init__(self, p1, p2, p3, p4):
        """ Constructs quadangle from points

        :param: p1 (Point) - First point
        :param: p2 (Point) - Second point
        :param: p3 (Point) - Third point
        :param: p4 (Point) - Fourth point
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def area(self):
        raise NotImplementedError()

    def __repr__(self):
        return f'p1 = {self.p1}, p2 = {self.p2}, p3 = {self.p3}, p4 = {self.p4}'

    @classmethod
    def from_values(cls, *values):
        """ Constructs quadangle from values
        """
        if len(values) != 8:
            raise Exception(f'Required coordinates mismatch. Want 8, got {len(values)}')
        points = [Point(values[val * 2], values[val * 2 + 1]) for val in range(len(values) // 2)]
        return cls(*points)

    @classmethod
    def create_empty(cls):
        return cls(None, None, None, None)

    @classmethod
    def from_lst(cls, lst):
        if not isinstance(lst, list):
            raise Exception(f'Want list. Got {type(lst)}')
        return cls.from_values(*lst)
        

if __name__ == '__main__':
    default_quadangle = Quadangle(Point(0, 0), Point(5, 5), Point(3, 6), Point(10, 13))
    print(f'Default quadangle: {default_quadangle}')
    vals_quadangle = Quadangle.from_values(0, 3, 10, 8, 8, 12, 16, 14)
    print(f'From values quadangle: {vals_quadangle}')
    empty_quadangle = Quadangle.create_empty()
    print(f'Create empty quadangle: {empty_quadangle}')
