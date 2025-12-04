def area(a):
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")
    if not isinstance(a, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    return a * a


def perimeter(a):
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")
    if not isinstance(a, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    return 4 * a