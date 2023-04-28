from typing import List
from math import sqrt
from itertools import filterfalse
from timeit import default_timer

def is_prime(n: int) -> bool:
    first_prime = 2
    if n < 2:
        return False
    while first_prime <= sqrt(n):
        if n % first_prime == 0:
            return False
        first_prime += 1
    return True
    
    """
    # Neal Holtschulte
    if n in primes:
        return True
    for p in primes:
        if n % p == 0:
            return False

    upper_limit = int(sqrt(n) + 1)
    divisor = primes[len(primes)-1] + 2
    while divisor < upper_limit:
        if prime(divisor):
            primes.append(divisor)
        if n % divisor == 0:
            return False
        divisor += 2
    return True
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    """

def prime_factors(n: int) -> int:
    result = 0
    first_divisor = 2
    while n > 1:
        if n % first_divisor == 0:
            result += first_divisor
            n //= first_divisor
        else:
            first_divisor += 1
    return result


def mult_primefactor_sum(a: int, b: int) -> List[int]: # [a, b] range of numbers included a and b
    numbers = list(range(a, b+1))
    filter_primes = list(filterfalse(is_prime, numbers))
    return [n for n in filter_primes if n % prime_factors(n) == 0]
    
    
if __name__ == "__main__":

    print(mult_primefactor_sum(80, 150))
    print(mult_primefactor_sum(10, 100))
    start = default_timer()
    print(mult_primefactor_sum(1500, 3002))
    end = default_timer()
    print(end - start)

