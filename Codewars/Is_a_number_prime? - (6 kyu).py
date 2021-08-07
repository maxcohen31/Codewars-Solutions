from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    index = 2 # primes start from 2
    while index <= sqrt(num):
        if num % index == 0:
            return False       
        index += 1
    return True

print(is_prime(75))    


    