def squares(x, n):
    power = 2
    result = [x, pow(x, 2)]
    if n <= 0:
        return []
    for i in range(n-2):
        result.append(pow(x, 2 * power))
        power *= 2
    return result[0:n]