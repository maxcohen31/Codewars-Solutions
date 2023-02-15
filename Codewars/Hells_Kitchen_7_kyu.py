def gordon(a: str) -> str:
    result = ""
    a = list([l.upper() for l in a])
    
    for idx, val in enumerate(a):
        if val == 'A':
            val = '@'
        elif val == ' ':
            val = "!!!! "
        elif val in "EIOU":
            val = '*'
        result += val
    return f"{result}!!!!"

