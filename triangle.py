def area(a, h):
    if a < 0 or h < 0:
        raise ValueError("Сторона и высота не могут быть отрицательными")
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a * h / 2


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a + b + c