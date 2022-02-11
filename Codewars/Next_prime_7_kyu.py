from math import sqrt
def find_prime(n):
    if n < 2:
        return False
    else:
        first_prime = 2
        while first_prime <= sqrt(n):
            if n % first_prime == 0:
                return False
            first_prime += 1
        return True
    
def next_prime(n):
    n = n + 1
    while not find_prime(n):
        n += 1
    return n

print(next_prime(8))            