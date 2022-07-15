def solve(a, b):
    b_prime_factors = []
    start = 2
    while start <= b:
        if b % start == 0:
            b_prime_factors.append(start)
            b = b // start
        else:
            start += 1
    for prime in b_prime_factors:
        f = a % prime
        if f != 0:
            return False
    return True
            
print(solve(12, 15))