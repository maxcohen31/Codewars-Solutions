def prime_factors(n: int) -> list:
    factors = []
    first_fact = 2
    while first_fact <= n:
        if n % first_fact == 0:
            factors.append(first_fact)
            n = n // first_fact
        else:
            first_fact += 1
    return factors    
        
print(prime_factors(1234567890))         
