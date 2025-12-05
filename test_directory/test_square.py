import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_fractional(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_area_large_number(self):
        res = area(100)
        self.assertEqual(res, 10000)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_fractional(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10.0)

    def test_perimeter_large_number(self):
        res = perimeter(100)
        self.assertEqual(res, 400)

    def test_area_negative_input(self):
        with self.assertRaises(TypeError):
            area(-5)

    def test_perimeter_negative_input(self):
        with self.assertRaises(TypeError):
            perimeter(-5)


if __name__ == "__main__":
    unittest.main()