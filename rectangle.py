def area(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a * b


def perimeter(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return 2 * (a + b)