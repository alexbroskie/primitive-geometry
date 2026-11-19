import unittest
from src import square
from src.geomath import create_square
from src.vector import Vector

class SquareTest(unittest.TestCase):
    def test_perimeter(self):
        res = square.perimeter(4)
        self.assertEqual(res, 16)
    def test_geomath_perimeter(self):
        rect = create_square(Vector(), 4)
        res = square.perimeter(len(rect[1]-rect[0]))
        self.assertEqual(res, 16)
    def test_area(self):
        res = square.area(4)
        self.assertEqual(res, 16)
    def test_geomath_area(self):
        rect = create_square(Vector(), 4)
        res = square.area(len(rect[1]-rect[0]))
        self.assertEqual(res, 16)