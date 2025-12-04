import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_height(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = area(10, 5)
        self.assertEqual(res, 25.0)

    def test_area_fractional(self):
        res = area(3, 4)
        self.assertEqual(res, 6.0)

    def test_area_decimal(self):
        res = area(0.5, 4)
        self.assertEqual(res, 1.0)

    def test_perimeter_equilateral(self):
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)

    def test_perimeter_right_triangle(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_fractional(self):
        res = perimeter(1.5, 2.5, 3.5)
        self.assertEqual(res, 7.5)

    def test_area_negative_input(self):
        with self.assertRaises(TypeError):
            area(-10, 5)

    def test_perimeter_negative_input(self):
        with self.assertRaises(TypeError):
            perimeter(-3, 4, 5)


if __name__ == "__main__":
    unittest.main()