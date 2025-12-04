import math


def area(r):
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    if not isinstance(r, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    if not isinstance(r, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    return 2 * math.pi * r