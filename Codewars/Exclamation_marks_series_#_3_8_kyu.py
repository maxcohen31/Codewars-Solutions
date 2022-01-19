def remove(s: str) -> str:
    result = ''
    result2 = ''
    char = '!'
    for mark in s:
        if mark == '!':
            result += mark        
    for i in s:
        if i != char:
            result2 += i
    return result2 + result          
            

           