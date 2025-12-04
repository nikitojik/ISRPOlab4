import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    # Тесты для функции area (площадь)
    def test_area_zero_width(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_zero_height(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = area(5, 3)
        self.assertEqual(res, 15)

    def test_area_fractional(self):
        res = area(2.5, 4)
        self.assertEqual(res, 10.0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    # Тесты для функции perimeter (периметр)
    def test_perimeter_positive(self):
        res = perimeter(5, 3)
        self.assertEqual(res, 16)

    def test_perimeter_fractional(self):
        res = perimeter(2.5, 4)
        self.assertEqual(res, 13.0)

    def test_perimeter_zero_width(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_perimeter_zero_height(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    # Негативные тесты
    def test_area_negative_input(self):
        with self.assertRaises(TypeError):
            area(-5, 3)

    def test_perimeter_negative_input(self):
        with self.assertRaises(TypeError):
            perimeter(5, -3)


if __name__ == "__main__":
    unittest.main()