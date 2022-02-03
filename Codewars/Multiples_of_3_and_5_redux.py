def solution(number):
    mult_3 = (number - 1) // 3 
    mult_5 = (number - 1) // 5 
    mult_15 = (number -1) // 15
    sum_3 = ((mult_3 * (mult_3 + 1)) // 2) * 3
    sum_5 = ((mult_5 * (mult_5 + 1)) // 2) * 5
    sum_15 = ((mult_15 * (mult_15 + 1)) // 2) * 15
    return sum_3 + sum_5 - sum_15 # intersection

print(solution(50000000000000000000000000000000000000000000000))
