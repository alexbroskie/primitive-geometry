import unittest
from src.vector import Vector

class VectorCreate(unittest.TestCase):
    def test_create(self):
        v = Vector(67, 67)
        self.assertTrue(v.x == 67 and v.y == 67)
    def test_zero_vector(self):
        v1 = Vector(0, 0)
        v2 = Vector()
        self.assertTrue(v1.x == v2.x and v1.y == v2.y)
    def test_vector_reassign(self):
        v1 = Vector(0, 0)
        v2 = Vector(67, 67)
        v1.x = 67
        v1.y = 67
        self.assertTrue(v1.x == v2.x and v1.y == v2.y)

class VectorArithmetic(unittest.TestCase):
    def test_vector_eq(self):
            v1 = Vector(234, 346)
            v2 = Vector(234, 346)
            self.assertEqual(v1 == v2, True)
    def test_add(self):
        res = Vector(2, 5) + Vector(5, 2)
        self.assertEqual(res, Vector(7, 7))
    def test_add_zero(self):
        res = Vector() + Vector(5, 5)
        self.assertEqual(res, Vector(5, 5))
    def test_sub(self):
            res = Vector(2, 5) - Vector(5, 2)
            self.assertEqual(res, Vector(-3, 3))
    def test_sub_zero(self):
        res = Vector(5, 5) - Vector()
        self.assertEqual(res, Vector(5, 5))
    def test_mul_scale(self):
        res = Vector(5, 5) * 2
        self.assertEqual(res, Vector(10, 10))
    def test_mul_vec(self):
        res = Vector(2, 5) * Vector(5, 2)
        self.assertEqual(res, 20)
    def test_div_scale(self):
        res = Vector(10, 10) / 2
        self.assertEqual(res, Vector(5, 5))

class VectorFuncs(unittest.TestCase):
    def test_len(self):
        res = len(Vector(4, 3))
        self.assertEqual(res, 5)
    def test_len_zero(self):
        res = len(Vector())
        self.assertEqual(res, 0)
    def test_str(self):
        res = str(Vector(67, 67))
        self.assertEqual(res, "(67, 67)")
    def test_unit(self):
        res = Vector(67, 0).unit()
        self.assertEqual(res, Vector(1, 0))
    def test_zero_unit(self):
        res = Vector(0, 0).unit()
        self.assertEqual(res, Vector())