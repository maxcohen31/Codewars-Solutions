def even_and_odd(n): 
    odd = ''
    even = ''
    new_n = str(n)
    for number in new_n:
        if int(number) % 2 == 0:
            even += str(number)
        elif int(number) % 2 != 0:
            odd += str(number)
            
    if odd == '':
        return int(even), 0
    elif even == '':
        return 0, int(odd)
    return int(even), int(odd)


    
a = 4628
print(even_and_odd(a))