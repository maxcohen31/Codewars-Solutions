# find the divisors!

def divisors(n):
    
    divisor_array = []
    
    for div in range(2, n - 1):
        if n % div == 0:
            divisor_array.append(div)
    if len(divisor_array) == 0:
        return f'{str(n)} is prime'     
    else:
        return divisor_array  
    
print(divisors(25))    
