from re import findall

def solve(s:str) -> int:
    numbers = findall(r"\d+", s)
    return max([int(i) for i in numbers])


