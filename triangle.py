def area(a, h):
    """
    Вычисляет площадь треугольника со стороной a и высотой проведенной к этой стороне h.

    Принимает:
        a (float): длинна стороны a треугольника
        h (float): высота h треугольника

    Возвращает:
        area (float): площадь треугольника со стороной a и высотой проведенной к этой стороне h

    """
    return (a * h) / 2


def perimeter(a, b, c):
    """
    Вычисляет периметр треугольника со сторонами a , b и c.

    Принимает:
        a (float): длина стороны a
        b (float): длина стороны b
        c (float): длина стороны c

    Возвращает:
        perimeter (float): периметр треугольника со сторонами a , b и c
        
    """
    return a + b + c

# a = int(input())
# h = int(input())
# b = int(input())
# c = int(input())
# print("area:", area(a, h))
# print("perimeter:" , perimeter(a, b, c))