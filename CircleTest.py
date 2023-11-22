import math
import unittest
from circle import area
from circle import perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_area(self):
        res = area(1)
        self.assertEqual(res, math.pi)
        res = area(2)
        self.assertEqual(res, 4 * math.pi)
        res = area(25)
        self.assertEqual(res, 625 * math.pi)
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_big(self):
        res = area(10 ** 10)
        self.assertEqual(res, (10 ** 20) * math.pi)
        res = area(10 ** 15)
        self.assertEqual(res, (10 ** 30) * math.pi)
        res = area(12345678999999)
        self.assertEqual(res, 152415789971016308642000001 * math.pi)
        res = area(10 ** 25)
        self.assertEqual(res, (10 ** 50) * math.pi)

    def test_error_area(self):
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -35)
        self.assertRaises(ValueError, area, -5454574574574747554)
        self.assertRaises(ValueError, area, -45755)
        self.assertRaises(ValueError, area, -10**20)

class CirclePreimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 2 * math.pi)
        res = perimeter(2)
        self.assertEqual(res, 4 * math.pi)
        res = perimeter(25)
        self.assertEqual(res, 50 * math.pi)
        res = perimeter(0)
        self.assertEqual(res, float(0))

    def test_perimeter_big(self):
        res = perimeter(10 ** 10)
        self.assertEqual(res, (10 ** 10) * 2 * math.pi)
        res = perimeter(10 ** 15)
        self.assertEqual(res, (10 ** 15) * 2 * math.pi)
        res = perimeter(12345678999999)
        self.assertEqual(res, 24691357999998 * math.pi)
        res = perimeter(10 ** 25)
        self.assertEqual(res, (10 ** 25) * 2 * math.pi)

    def test_error_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -35)
        self.assertRaises(ValueError, perimeter, -5454574574574747554)
        self.assertRaises(ValueError, perimeter, -45755)
        self.assertRaises(ValueError, perimeter, -10**20)
