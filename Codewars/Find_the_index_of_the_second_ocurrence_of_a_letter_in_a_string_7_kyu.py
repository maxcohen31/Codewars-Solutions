def second_symbol(s: str, symbol: str) -> int:
    if symbol not in s:
        return -1

    string_indexes = [idx for idx, char in enumerate(s) if char == symbol]
    if len(string_indexes) == 1:
        return -1
    elif len(string_indexes) == 2:
        return string_indexes[1]
    elif len(string_indexes) % 2 != 0 and len(string_indexes) > 2:
        return string_indexes[len(string_indexes)//2]
    return string_indexes[len(string_indexes)//2-1]
   
print(second_symbol('Hello world!!!','l'))

