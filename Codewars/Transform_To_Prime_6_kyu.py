from math import sqrt
from typing import List

def is_prime(n: int) -> bool:
    first_prime = 2

    if n < first_prime:
        return False

    while sqrt(n) > first_prime:
        if n % first_prime == 0:
            return False
        first_prime += 1
    return True

def next_prime(p: int) -> int:
    while not is_prime(p):
        p += 1
    return p 


def minimum_number(numbers: List[int]) -> int:
    number_sum = sum(numbers)
    return next_prime(number_sum) - number_sum

