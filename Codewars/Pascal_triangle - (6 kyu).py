import functools
import operator
def pascals_triangle(n):
    start = [[1]]
    for row in range(2, n+1):
        end = [1]
        for column in range(1, row-1):
            end.append(start[-1][column] + start[-1][column-1])
        end.append(1)
        start.append(end)
    return functools.reduce(operator.iconcat, start, [])       
 
# Alternative Solution 
def pascal_triangle_2(n):
    start = [1]
    for i in range(1, n+1):
        start.append(start[i - 1] * (n - i + 1) // i)
    return start   

# Alternative Solution 
from scipy.special import comb
def pascal_triangle_3(n):
    return [comb(a, b, exact=True) for a in range(n) for b in range(a+1)]
    
    
print(pascal_triangle_3(5))    