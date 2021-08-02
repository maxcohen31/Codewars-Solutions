def dig_pow(n, p):  
    dig = [int(i) for i in str(n)]
    digits_power = []
    for digits in dig:
        digits_power.append(pow(digits, p))
        p += 1
    sum_ = sum(digits_power)
    if sum_ % n == 0:
        return sum_ // n
    else:
        return -1
        
    
    
    
print(dig_pow(695, 2))    
        