def arr_adder(arr):
    words = []
    result = ''
    new_arr = list(zip(*arr))
    
    for arr in new_arr:
        words.append(''.join(arr))
    for word in words:
        result += f"{word} "
    return result[0:-1]


print(arr_adder([['J','L','L','M'], ['u','i','i','a'], ['s','v','f','n'], ['t','e','e','' ]]))