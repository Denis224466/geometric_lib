import math
import unittest
from square import area
from square import perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(1)
        self.assertEqual(res, 1)
        res = area(2)
        self.assertEqual(res, 4)
        res = area(25)
        self.assertEqual(res, 625)
        res = area(0)
        self.assertEqual(res, float(0))

    def test_area_big(self):
        res = area(10 ** 10)
        self.assertEqual(res, 10 ** 20)
        res = area(10 ** 15)
        self.assertEqual(res, 10 ** 30)
        res = area(12345678999999)
        self.assertEqual(res, 152415789971016308642000001)
        res = area(10 ** 25)
        self.assertEqual(res, 10 ** 50)

    def test_error_area(self):
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -35)
        self.assertRaises(ValueError, area, -5454574574574747554)
        self.assertRaises(ValueError, area, -45755)
        self.assertRaises(ValueError, area, -10**20)

class SquarePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
        res = perimeter(2)
        self.assertEqual(res, 8)
        res = perimeter(25)
        self.assertEqual(res, 100)
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_big(self):
        res = perimeter(10 ** 10)
        self.assertEqual(res, (10 ** 10) * 4)
        res = perimeter(10 ** 15)
        self.assertEqual(res, (10 ** 15) * 4)
        res = perimeter(12345678999999)
        self.assertEqual(res, 49382715999996)
        res = perimeter(10 ** 25)
        self.assertEqual(res, (10 ** 25) * 4)

    def test_error_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -35)
        self.assertRaises(ValueError, perimeter, -5454574574574747554)
        self.assertRaises(ValueError, perimeter, -45755)
        self.assertRaises(ValueError, perimeter, -10**20)