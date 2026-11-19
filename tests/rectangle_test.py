import unittest
from src import rectangle
from src.geomath import create_rect
from src.vector import Vector

class RectangleTest(unittest.TestCase):
    def test_perimeter(self):
        res = rectangle.perimeter(4, 6)
        self.assertEqual(res, 20)
    def test_geomath_perimeter(self):
        rect = create_rect(Vector(), 4, 6)
        res = rectangle.perimeter(len(rect[1]-rect[0]), len(rect[2]-rect[1]))
        self.assertEqual(res, 20)
    def test_area(self):
        res = rectangle.area(4, 6)
        self.assertEqual(res, 24)
    def test_geomath_area(self):
        rect = create_rect(Vector(), 4, 6)
        res = rectangle.area(len(rect[1]-rect[0]), len(rect[2]-rect[1]))
        self.assertEqual(res, 24)