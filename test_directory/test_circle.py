import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_unit_circle(self):
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_area_positive(self):
        res = area(2)
        self.assertEqual(res, math.pi * 4)

    def test_area_fractional(self):
        res = area(2.5)
        self.assertEqual(res, math.pi * 6.25)

    def test_area_large_radius(self):
        res = area(10)
        self.assertEqual(res, math.pi * 100)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_unit_circle(self):
        res = perimeter(1)
        self.assertEqual(res, 2 * math.pi)

    def test_perimeter_positive(self):
        res = perimeter(2)
        self.assertEqual(res, 4 * math.pi)

    def test_perimeter_fractional(self):
        res = perimeter(2.5)
        self.assertEqual(res, 5 * math.pi)

    def test_perimeter_large_radius(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * math.pi)

    def test_area_negative_input(self):
        with self.assertRaises(TypeError):
            area(-1)

    def test_perimeter_negative_input(self):
        with self.assertRaises(TypeError):
            perimeter(-5)


if __name__ == "__main__":
    unittest.main()