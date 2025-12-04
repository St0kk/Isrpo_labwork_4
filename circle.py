import math


def area(r):
    """
    Возвращает площадь круга радиуса r.

    Принимает:
        r (float): радиус круга

    Возвращает:
        area (float): площадь круга радиуса r

    """
    return math.pi * r * r


def perimeter(r):
    """
    Возвращает периметр круга радиуса r.

    Параметры:
        r (float): радиус круга

    Возвращает:
        perimeter (float): периметр круга радиуса r

    """
    return 2 * math.pi * r

# r = int(input())
# print("area:", area(r))
# print("perimeter:" , perimeter(r))