from typing import List

def get_dividers(values: List[int], powers: List[int]) -> List[int]:
    
    x = 1
    divisors = []
    raise_to_powers = [pow(val1, val2) for val1, val2 in zip(values, powers)]
    for i in raise_to_powers:
        x *= i
    
    divisors = [d for d in range(1, x + 1) if x % d == 0]
    return divisors
    

l1 = [1, 11, 5]
l2 = [1, 1, 3]

print(get_dividers(l1, l2))