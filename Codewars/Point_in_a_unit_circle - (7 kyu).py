import math
def point_in_circle(x, y):
    return True if math.sqrt(x**2 + y**2) < 1 else False