import math
import unittest
from triangle import area
from triangle import perimeter


class TriangleAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(1, 2)
        self.assertEqual(res, 1)
        res = area(2, 4)
        self.assertEqual(res, 4)
        res = area(25, 4)
        self.assertEqual(res, 50)
        res = area(0, 1)
        self.assertEqual(res, 0.0)

    def test_area_big(self):
        res = area(10 ** 5, 10 ** 10)
        self.assertEqual(res, 10 ** 15 / 2)
        res = area(10 ** 4, 10 ** 15)
        self.assertEqual(res, 10 ** 19 / 2)
        res = area(12345678999999, 234)
        self.assertEqual(res, 1444444442999883.0)
        res = area(10 ** 25, 10 ** 15)
        self.assertEqual(res, 10 ** 40 / 2)

    def test_error_area(self):
        self.assertRaises(ValueError, area, -1, 4)
        self.assertRaises(ValueError, area, -35, 34)
        self.assertRaises(ValueError, area, -5454574574574747554, 4)
        self.assertRaises(ValueError, area, -45755, -2)
        self.assertRaises(ValueError, area, -10 ** 20, -4098789)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        res = perimeter(1, 3, 3)
        self.assertEqual(res, 7)
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
        res = perimeter(25, 25, 20)
        self.assertEqual(res, 70)
        res = perimeter(0, 0, 0)
        self.assertEqual(res, float(0))

    def test_perimeter_big(self):
        res = perimeter(10 ** 10, 10 ** 10, 10 ** 10)
        self.assertEqual(res, (10 ** 10) * 3)
        res = perimeter(10 ** 15, 10 ** 15, 1234)
        self.assertEqual(res, (10 ** 15) * 2 + 1234)
        res = perimeter(10 ** 5, (10 ** 4) * 7, (10 ** 4) * 6)
        self.assertEqual(res, (10 ** 4) * 23)
        res = perimeter(10 ** 25, (10 ** 24) * 6, (10 ** 24) * 9)
        self.assertEqual(res, (10 ** 24) * 25)

    def test_error_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1, 23, 234)
        self.assertRaises(ValueError, perimeter, -35, 35, 35)
        self.assertRaises(ValueError, perimeter, 10 ** 12, 10 ** 14, 10 ** 13)
        self.assertRaises(ValueError, perimeter, 1, 13, 6)
        self.assertRaises(ValueError, perimeter, -10 ** 20, 0, 1)
