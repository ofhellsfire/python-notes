import unittest

from solution import Point, Rectangle, RectRelation


class TestRectRelations(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle(Point(1, 1), width=10, height=5)

    def test_non_rectangle(self):
        other = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.rect.get_relation(other)

    def test_separate_by_x_axis(self):
        other = Rectangle(Point(15, 1), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.SEPARATE)

    def test_separate_by_y_axis(self):
        other = Rectangle(Point(1, 15), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.SEPARATE)

    def test_separate_by_both_axis(self):
        other = Rectangle(Point(15, 15), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.SEPARATE)

    def test_inscribed(self):
        other = Rectangle(Point(2, 2), width=8.5, height=3.14)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.INSCRIBED)

    def test_full_overlap(self):
        other = Rectangle(Point(1, 1), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.FULLY_OVERLAPPING)

    def test_partial_overlap_top_right(self):
        other = Rectangle(Point(7.5, 0.5), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.PARTIAL_OVERLAPPING)

    def test_partial_overlap_top_left(self):
        other = Rectangle(Point(0, 0), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.PARTIAL_OVERLAPPING)

    def test_partial_overlap_botom_right(self):
        other = Rectangle(Point(8, 3), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.PARTIAL_OVERLAPPING)

    def test_partial_overlap_botom_left(self):
        other = Rectangle(Point(0, 3), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.PARTIAL_OVERLAPPING)

    def test_partial_overlap_top(self):
        other = Rectangle(Point(1, 0), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.PARTIAL_OVERLAPPING)

    def test_partial_overlap_right(self):
        other = Rectangle(Point(4, 1), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.PARTIAL_OVERLAPPING)

    def test_partial_overlap_bottom(self):
        other = Rectangle(Point(1, 3), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.PARTIAL_OVERLAPPING)

    def test_partial_overlap_left(self):
        other = Rectangle(Point(0, 1), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.PARTIAL_OVERLAPPING)

    def test_adjacent(self):
        other = Rectangle(Point(1, 6), width=10, height=5)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.ADJACENT)

    def test_partial_overlap_cross(self):
        other = Rectangle(Point(4, 0), width=3, height=6)
        rel = self.rect.get_relation(other)
        self.assertTrue(rel == RectRelation.PARTIAL_OVERLAPPING)

if __name__ == '__main__':
    unittest.main()
