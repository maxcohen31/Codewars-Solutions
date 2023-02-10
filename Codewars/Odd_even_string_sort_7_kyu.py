def sort_my_string(s: str) -> str:
    s = s[:]
    first = ""
    second = ""

    for idx, val in enumerate(s):
        if idx % 2 == 0:
            first += val
        elif idx % 2 != 0:
            second += val

    return f"{first} {second}"
    

print(sort_my_string("CodeWars"))
print(sort_my_string("YCOLUE'VREER"))