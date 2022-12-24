def solution(number: int) -> list:    
    mult_5 = []
    mult_3 = []
    mult_3_5 = []

    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            mult_3_5.append(i)
        elif i % 3 == 0:
            mult_3.append(i)
        elif i % 5 == 0:
            mult_5.append(i)
       
    return [len(mult_3), len(mult_5), len(mult_3_5)]

print(solution(141))