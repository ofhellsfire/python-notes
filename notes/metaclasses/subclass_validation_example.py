"""
Example of subclass validation on poligon class creation.
"""

class MetaPolygon(type):

    def __new__(mcs, name, bases, class_dict):
        # don't validate the abstract class
        if bases not in ((), (object,)):
            if class_dict["sides"] < 3:
                raise ValueError("Polygons need 3+ sides")
        return type.__new__(mcs, name, bases, class_dict)


class Polygon(metaclass=MetaPolygon):

    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


# NOTE: comment this out to avoid an exception
class Line(Polygon):
    sides = 1
