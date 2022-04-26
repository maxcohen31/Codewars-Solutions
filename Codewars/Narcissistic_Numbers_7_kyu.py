def is_narcissistic(i):
    result = 0
    str_i = list(str(i))
    for idx, n in enumerate(str_i):
        result += pow(int(n), len(str_i))
    return result == i


print(is_narcissistic(1634))