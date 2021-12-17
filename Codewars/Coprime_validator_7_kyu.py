def are_coprime(n,m):
    n_divisors = [i for i in range(1, n+1) if n % i == 0]
    m_divisors = [i for i in range(1, m+1) if m % i == 0]
    for i in n_divisors[1:]:
        for j in m_divisors[1:]:
            if i % j == 0:
                return False
    return True        


# clever Solution: Euclid's Algorithm
def are_coprime2(n, m):
    while m > 0:
        n, m = m, n % m
    return n == 1
    
print(are_coprime(23, 45))