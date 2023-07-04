def shorter_reverse_longer(a: str, b: str) -> str:
    result = ""

    if len(a) < len(b):
        result = a + b[::-1] + a
    elif len(a) == len(b) or len(a) > len(b):  
        result =  b + a[::-1] + b  
        
    return result

print((shorter_reverse_longer("first", "abcde")))