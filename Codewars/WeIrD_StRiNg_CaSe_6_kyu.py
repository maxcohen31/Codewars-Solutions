def to_weird_case(string):
    result = []
    empty = ' '
    new_string = string.split()
    
    if len(new_string) == 1:
        for word in new_string:
            for idx, letter in enumerate(word):
                if idx % 2 == 0:
                    letter = letter.upper()
                elif idx % 2 != 0:
                    letter = letter.lower()
                result.append(letter)
        return ''.join(result)
    
    elif len(new_string) > 1:
        for word in new_string:
            for idx, letter in enumerate(word):
                if idx % 2 == 0:
                    letter = letter.upper()
                elif idx % 2 != 0:
                    letter = letter.lower()
                result.append(letter)
            result.append(list(string).index(' '))
        
        for idx, numb in enumerate(result):
            if isinstance(result[idx], int):
                result[idx] = empty
        return ''.join(result[:-1])

