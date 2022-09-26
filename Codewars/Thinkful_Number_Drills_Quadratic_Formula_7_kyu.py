from math import sqrt
def quadratic_formula(a, b, c):
    
    dis = b * b - (4 * a * c)

    root1 = (-b + sqrt(dis)) / (2 * a)
    
    root2 = (-b - sqrt(dis)) / (2 * a)
    
    return [root1, root2]

print(quadratic_formula(1, 10, -24))
print(quadratic_formula(2, 16, 1))