import math
import unittest

def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):
    def test_SmallArea(self):
        res = area(6, 7)
        self.assertEqual(res, 42)

    def test_ZeroArea(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_Square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_Negative(self):
        res = area(-10, 3)
        self.assertEqual(res, -30)
    
    def test_BothNegativeArea(self):
        res = area(-10, -3)
        self.assertEqual(res, 30)

    def test_BigNumbers(self):
        res = area(2**32, 2**32)
        self.assertEqual(res, 2**64)

    def test_MinimalArea(self):
        res = area(1, 1)
        self.assertEqual(res, 1)
    
    def test_SmallPerimeter(self):
        res = perimeter(6, 7)
        self.assertEqual(res, 26)

    def test_ZeroPerimeter(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_NegativePerimeter(self):
        res = perimeter(5, -10)
        self.assertEqual(res, -10)

    def test_BothNegativePerimeter(self):
        res = perimeter(-5, -10)
        self.assertEqual(res, -30)

    def test_BigPerimeter(self):
        res = perimeter(2**32, 2**32)
        self.assertEqual(res, 2**34)

    def test_MinimalPerimeter(self):
        res = perimeter(0, 1)
        self.assertEqual(res, 2)