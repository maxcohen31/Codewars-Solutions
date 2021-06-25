def unique_in_order(iterable):
    
    result = []
    for x in iterable:
        if len(result) < 1 or not x == result[len(result) - 1]:
            result.append(x)
    return result

print(unique_in_order('AAAABBBCCDAABBB'))