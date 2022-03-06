def solution(digits):
    result = []
    str_digit = str(digits) 
    for i, a in enumerate(str_digit):   
        result.append(str_digit[i:i+5])
    return max([int(i) for i in result])

n = 1234567890
p = 1234567898765
print(solution(n))        