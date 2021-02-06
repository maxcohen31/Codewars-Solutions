# You'are a square!

import math

def is_square(n):
    
    if n <= -1:
        return False
    else:    
        numb = math.sqrt(n)
        return numb.is_integer()  

