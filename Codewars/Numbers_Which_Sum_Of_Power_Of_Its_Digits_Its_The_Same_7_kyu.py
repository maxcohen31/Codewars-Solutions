def eq_sum_powdig(hMax: int, exp: int) ->list:
    
    result = []

    for n in range(hMax+1):
        new = str(n)
        numb = sum(pow(int(i), exp) for i in new)
        if numb == n:
            result.append(n)
    return result[2:]

print(eq_sum_powdig(200, 3))