from math import pi

def circle_area(r):
    
    try:
        area = round(pi * r ** 2, 2)
        if r <= 0:
            return False
        else:
            return area
        
    except TypeError:
        return False


print(circle_area(43.2673))
print(circle_area(0))
print(circle_area('number'))
