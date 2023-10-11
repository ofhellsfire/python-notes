from dataclasses import dataclass
import enum


class RectRelation(enum.IntEnum):

    SEPARATE = 0
    PARTIAL_OVERLAPPING = 1
    FULLY_OVERLAPPING = 2
    INSCRIBED = 3
    ADJACENT = 4


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Projection:
    p1: float
    p2: float

    def __lt__(self, other: "Projection") -> bool:
        return self.p1 < other.p1

    def __gt__(self, other: "Projection") -> bool:
        return self.p2 > other.p2
    
    def intersects(self, other: "Projection") -> bool:
        if self < other:
            return self.p1 <= other.p1 and self.p2 > other.p1
        else:
            return other.p1 <= self.p1 and other.p2 > self.p1
    
    def includes(self, other: "Projection") -> bool:
        if self < other:
            return self.p1 <= other.p1 and self.p2 > other.p2
        else:
            return other.p1 <= self.p1 and other.p2 > self.p2
    
    def adjoins(self, other: "Projection") -> bool:
        if self < other:
            return self.p1 < other.p1 and self.p2 == other.p1
        else:
            return other.p1 < self.p1 and other.p2 == self.p1


class Rectangle:

    def __init__(
        self,
        top_left: Point,
        width: float,
        height: float,
        angle: float = 0,
    ):
        self.top_left = top_left
        self.width = width
        self.height = height
        self.angle = angle
        self.proj_x, self.proj_y = self._get_projections()
    
    def get_relation(self, other: "Rectangle") -> RectRelation:
        if not isinstance(other, Rectangle):
            raise TypeError(f"Cannot compare {type(self)} and {type(other)}")
        if self._is_fully_overlapping(other):
            return RectRelation.FULLY_OVERLAPPING
        elif self._is_inscribed(other):
            return RectRelation.INSCRIBED
        elif self._is_partially_overlapping(other):
            return RectRelation.PARTIAL_OVERLAPPING
        elif self._is_adjacent(other):
            return RectRelation.ADJACENT
        else:
            return RectRelation.SEPARATE

    def _is_fully_overlapping(self, other: "Rectangle") -> bool:
        return (
            self.proj_x == other.proj_x and
            self.proj_y == other.proj_y
        )

    def _is_inscribed(self, other: "Rectangle") -> bool:
        return (
            self.proj_x.includes(other.proj_x) and
            self.proj_y.includes(other.proj_y)
        )

    def _is_partially_overlapping(self, other: "Rectangle") -> bool:
        return (
            self.proj_x.intersects(other.proj_x) and
            self.proj_y.intersects(other.proj_y)
        )

    def _is_adjacent(self, other: "Rectangle") -> bool:
        return (
            self.proj_x.adjoins(other.proj_x) or
            self.proj_y.adjoins(other.proj_y)
        )
    
    def _get_projections(self) -> tuple[Projection, Projection]:
        proj_x = Projection(self.top_left.x, self.top_left.x + self.width)
        proj_y = Projection(self.top_left.y, self.top_left.y + self.height)
        return proj_x, proj_y
