def smallest_product(arr):
    numbers = []
    for i in arr:
        p = 1
        for j in i:
            p = p * j
        numbers.append(p)        
    return min(numbers)

# Alternative solution
from math import prod
def smallest_product2(arr):
    return min(map(prod, arr))

  
        
        
    
