from re import findall

def is_it_a_num(s: str) -> str:
    number = findall(r"\d", s)
    if len(number) == 0 or len(number) > 11 or len(number) < 11 or number[0] != '0': 
        return "Not a phone number"
    return "".join(number)

    

print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"))
print(is_it_a_num("call me"))