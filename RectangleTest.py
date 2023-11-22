import math
import unittest
from rectangle import area
from rectangle import perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(1, 1)
        self.assertEqual(res, 1)
        res = area(2, 2)
        self.assertEqual(res, 4)
        res = area(25, 22)
        self.assertEqual(res, 550)
        res = area(0, 1)
        self.assertEqual(res, float(0))

    def test_area_big(self):
        res = area(10 ** 10, 10 ** 5)
        self.assertEqual(res, 10 ** 15)
        res = area(10 ** 15, 10 ** 10)
        self.assertEqual(res, 10 ** 25)
        res = area(123123123123, 3)
        self.assertEqual(res, 369369369369)
        res = area(10 ** 25, 10 ** 20)
        self.assertEqual(res, 10 ** 45)

    def test_error_area(self):
        self.assertRaises(ValueError, area, -1, 3)
        self.assertRaises(ValueError, area, -35, -5)
        self.assertRaises(ValueError, area, -5454574574574747554, 2342342)
        self.assertRaises(ValueError, area, -45755, 3)
        self.assertRaises(ValueError, area, -10 ** 20, 0)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        res = perimeter(1, 2)
        self.assertEqual(res, 6)
        res = perimeter(2, 2)
        self.assertEqual(res, 8)
        res = perimeter(25, 25)
        self.assertEqual(res, 100)
        res = perimeter(0, 3)
        self.assertEqual(res, 0)

    def test_perimeter_big(self):
        res = perimeter(10 ** 10, 10 ** 10)
        self.assertEqual(res, (10 ** 10) * 4)
        res = perimeter(10 ** 15, 50)
        self.assertEqual(res, (10 ** 15) * 2 + 100)
        res = perimeter(12345678999999, 12345678999999)
        self.assertEqual(res, 49382715999996)
        res = perimeter(10 ** 25, (10 ** 24) * 5)
        self.assertEqual(res, (10 ** 25) * 3)

    def test_error_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1, 2)
        self.assertRaises(ValueError, perimeter, -35, -34)
        self.assertRaises(ValueError, perimeter, -5454574574574747554, 2343242342340000)
        self.assertRaises(ValueError, perimeter, -45755, 0)
        self.assertRaises(ValueError, perimeter, -10 ** 20, 10 ** 23)
