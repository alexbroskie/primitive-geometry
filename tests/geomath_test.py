import unittest
import src.geomath as geomath
from src.vector import Vector

class CreateTest(unittest.TestCase):
    def test_rect_create(self):
        res = geomath.create_rect(Vector(), 4, 6)
        a_side = res[1]-res[0]
        b_side = res[2]-res[1]
        c_side = res[3]-res[2]
        d_side = res[0]-res[3]

        self.assertAlmostEqual(a_side*b_side, 0, msg=f"Non-perpendicular A and B sides: {a_side}, {b_side}, {a_side*b_side}")
        self.assertAlmostEqual(c_side*d_side, 0, msg=f"Non-perpendicular C and D sides: {c_side}, {d_side}, {c_side*d_side}")
        self.assertTrue(len(a_side) == len(c_side) == 4, f"Height must be 4!: {a_side}={len(a_side)}, {c_side}={len(c_side)}")
        self.assertTrue(len(b_side) == len(d_side) == 6, f"Height must be 6!: {a_side}={len(a_side)}, {c_side}={len(c_side)}")

    def test_square_create(self):
        res = geomath.create_square(Vector(), 4)
        a_side = len(res[1]-res[0])
        b_side = len(res[2]-res[1])
        c_side = len(res[3]-res[2])
        d_side = len(res[0]-res[3])
        return self.assertTrue(
            a_side == b_side == c_side == d_side == 4,
            f"Unequal sides for square:\nSides: {a_side}, {b_side}, {c_side}, {d_side}\nPoints: {res[0]}, {res[1]}, {res[2]}, {res[3]}"
        )

class MoveTest(unittest.TestCase):
    def test_rect_move(self):
        rect = geomath.create_rect(Vector(), 4, 6)
        res = geomath.move(rect, Vector(1, 0), 4)

        self.assertTrue(
            len(rect[0]-res[0]) == 4 and
            len(rect[1]-res[1]) == 4 and
            len(rect[2]-res[2]) == 4 and
            len(rect[3]-res[3]) == 4,
            f"Rect move failed:\nbefore: {rect}\nafter: {res}"
        )
    def test_square_move(self):
        sqrt = geomath.create_square(Vector(), 4)
        res = geomath.move(sqrt, Vector(1, 0), 4)
        
        a_delta = len(sqrt[0]-res[0])
        b_delta = len(sqrt[1]-res[1])
        c_delta = len(sqrt[2]-res[2])
        d_delta = len(sqrt[3]-res[3])

        self.assertTrue(
            a_delta ==
            b_delta ==
            c_delta ==
            d_delta == 4,
            f"Square move by 4 failed:\nbefore: {sqrt}\nafter: {res}\nDeltas: {a_delta}, {b_delta}, {c_delta}, {d_delta}"
        )
    def test_zero_move(self):
        sqrt = geomath.create_square(Vector(), 4)
        res = geomath.move(sqrt, Vector(1, 0), 0)
        
        a_delta = len(sqrt[0]-res[0])
        b_delta = len(sqrt[1]-res[1])
        c_delta = len(sqrt[2]-res[2])
        d_delta = len(sqrt[3]-res[3])

        self.assertTrue(
            a_delta ==
            b_delta ==
            c_delta ==
            d_delta == 0,
            f"Square move by 0 failed:\nbefore: {sqrt}\nafter: {res}\nDeltas: {a_delta}, {b_delta}, {c_delta}, {d_delta}"
        )
    def test_zero_dir_move(self):
        sqrt = geomath.create_square(Vector(), 4)
        res = geomath.move(sqrt, Vector(0, 0), 999)
        
        a_delta = len(sqrt[0]-res[0])
        b_delta = len(sqrt[1]-res[1])
        c_delta = len(sqrt[2]-res[2])
        d_delta = len(sqrt[3]-res[3])

        self.assertTrue(
            a_delta ==
            b_delta ==
            c_delta ==
            d_delta == 0,
            f"Square move by zero direction vector failed:\nbefore: {sqrt}\nafter: {res}\nDeltas: {a_delta}, {b_delta}, {c_delta}, {d_delta}"
        )