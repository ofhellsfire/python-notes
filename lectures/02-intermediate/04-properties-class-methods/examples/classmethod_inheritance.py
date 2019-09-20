from classmethod_ import Point, Quadangle


class Rectangle(Quadangle):

    def __init__(self, lt, rb, p2=None, p3=None):
        """ Constructs rectangle

        :param: lt (Point) - left top
        :param: rb (Point) - right bottom
        """
        super().__init__(lt, p2, p3, rb)

    def get_area(self):
        return abs((self.p4.x - self.p1.x) * (self.p4.y - self.p1.x))


default_rect = Rectangle(Point(0, 0), Point(5, 10))
print(f'Default Rectangle: {default_rect.get_area()}')

empty_rect = Rectangle.create_empty()
print(f'Empty Rectangle: {empty_rect}')

listed_rect = Rectangle.from_lst([1, 2, 3, 4, 5, 6, 7, 8])
print(f'Listed Rectangle: {listed_rect.get_area()}')
