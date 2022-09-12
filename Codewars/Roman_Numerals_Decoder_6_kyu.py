def solution(roman):
    
    result = 0
    numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    for i in range(len(roman)):
        val = numbers[roman[i]]
        # if the next number is greater than value, subtract it
        if i+1 < len(roman) and numbers[roman[i+1]] > val:
            result -= val
        else:
            result += val
    return result

print(solution('CDXLIII')) # 443
print(solution('IX')) # 443