from string import ascii_lowercase

def switcher(arr: list[str]) -> str:
    result = ""
    reversed_alpha = f"{ascii_lowercase[::-1]}!? "
    number_range = list(range(1, 30))
    new_dict = dict(zip(reversed_alpha, number_range))
    
    for n in arr:
        for k,v in new_dict.items():
            if n == str(v):
                result += k
    return result

print(switcher(['24', '12', '23', '22', '4', '26', '9', '8']))
print(switcher(['12']))