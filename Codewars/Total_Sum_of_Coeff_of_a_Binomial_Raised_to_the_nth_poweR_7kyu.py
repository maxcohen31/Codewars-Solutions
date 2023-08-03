from math import comb
from typing import List

# Poor performance
# This is the slution i came up with
def f(n: int) -> List[int]:

    result = []
    bin_coeff_sum = []    

    for i in range(n + 1):
        bin_coeff = []
        for j in range(n + 1):
            bin_coeff.append(comb(i, j))
        result.append(bin_coeff)
   
    for element in result:
        bin_coeff_sum.append(sum(element))

    return bin_coeff_sum + [sum(bin_coeff_sum)]

# Faster method
def f(n: int) -> List[int]:
    result = []
    
    for i in range(n + 1):
        result.append(pow(2, i))
    return result + [sum(result)]

