# A basic quadratic inequalities calculator
from math import sqrt
import cmath
def quadratic_inequality():
    a = int(input('Enter the coefficient for x^2 >> '))
    b = int(input('Enter the coefficient for x >> '))
    c = int(input('Enter the coefficient for the constant term >> '))
    delta = (b ** 2 - (4 * a * c))

    if delta > 0 and a > 0:
        x_1 = (-b + sqrt(delta)) / 2 * a
        x_2 = (-b - sqrt(delta)) / 2 * a
        print(f'Solutions are x < {x_2} and x > {x_1}')
        return x_1, x_2

    elif delta > 0 and a < 0:
        x_1 = (-b + sqrt(delta)) / 2 * a
        x_2 = (-b - sqrt(delta)) / 2 * a
        print(f'Solutions are {x_2} < x < {x_1}')
        return x_1, x_2

    elif delta == 0:
        x = -b / 2 * a
        print(f'Solutions are x = {x}')
        return x

    elif delta < 0 and a > 0:
        x_1 = (-b + cmath.sqrt(delta)) / 2 * a
        x_2 = (-b - cmath.sqrt(delta)) / 2 * a
        print(f'Complex Solutions are x < {x_2} and x > {x_1} ')
        return x_1, x_2

    elif delta < 0 and a < 0:
        x_1 = (-b + cmath.sqrt(delta)) / 2 * a
        x_2 = (-b - cmath.sqrt(delta)) / 2 * a
        print(f'Complex Solutions are {x_2} < x < {x_1}')
        return x_1, x_2



