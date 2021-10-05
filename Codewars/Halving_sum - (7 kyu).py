def halving_sum(n):
    summ = n
    current_value = n
    while current_value > 1:
        if n == 1 or n == 0:
            return False
        else:
            current_value = int(current_value/2)
            summ = summ + current_value
    return summ    
        
# Alternative Solution        
def halving_sum(n):
    result = n
    while n >= 1:
        n //= 2
        result += n
    return result
    
print(halving_sum(25))    

