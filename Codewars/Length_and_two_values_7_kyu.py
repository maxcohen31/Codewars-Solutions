def alternate(n: int, first_value, second_value) -> list:
    result = []
    for _ in range(n+1):
        result.append(first_value)
        result.append(second_value)
    return result[:n]



print(alternate(5, True, False))
