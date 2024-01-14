"""
    Write a function which reduces fractions to their simplest form! 
    Fractions will be presented as an array/tuple (depending on the language) 
    of strictly positive integers, 
    and the reduced fraction must be returned as an array/tuple:

"""

def gcd(a, b):
    if(b == 0):
        return a

    return gcd(b, a%b)

def reduce_fraction(fraction):
    # your code here
    assert fraction[1] > 0, "Zero division error" 

    simpl_num = fraction[0] // gcd(fraction[0], fraction[1])
    simpl_den = fraction[1] // gcd(fraction[0], fraction[1])

    return (simpl_num, simpl_den)
    
    
    
    

if "__main__" == __name__:
    print(reduce_fraction((20, 60)))
    print(gcd(10, 15))

