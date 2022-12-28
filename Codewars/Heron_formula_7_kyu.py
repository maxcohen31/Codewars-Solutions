from math import sqrt
def heron(a: int, b: int, c: int) -> float:
    semi_perimeter = (a + b + c) / 2
    x = semi_perimeter - a
    y = semi_perimeter - b
    z = semi_perimeter - c
    return round(sqrt(semi_perimeter * x * y * z), 2)