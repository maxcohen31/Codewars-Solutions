def sum_dig_pow(a: int, b: int) -> list:
    result = []
    for i in range(a, b + 1):
        numbers = []
        power = 0
        for j in str(i):
            numbers.append(int(j) ** (power + 1))
            power += 1
        if i == sum(numbers):    
            result.append(i)
    return result


# Alternative Solution
def sum_dig_pow(a, b):
    result = []
    for n in range(a, b+1):
        digits = [int(i) for i in str(n)]
        dig_sum = sum([pow(d, i+1) for i, d in enumerate(digits)])
        if dig_sum == n: 
            result.append(n)
    return result
