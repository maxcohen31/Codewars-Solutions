def order_weight(strng):
    strng = strng.split(' ')
    fake_weights = {}
    for numbers in strng:
        sum_ = 0
        for dig in numbers:
            sum_ += int(dig)
        fake_weights[numbers] = sum_ 
    strng.sort()        
    strng.sort(key=lambda x: fake_weights[x])
    return ' '.join(strng)
    
    
s = "103 123 4444 99 2000"    
print(order_weight(s))