from typing import List
def capitalize(s:str, ind: List[int]) -> str:
    result = ""
    new_str = list(filter(lambda x: x in s, s))
    
    for idx, val in enumerate(new_str):
        if idx in ind:
            result += val.upper()
        else:
            result += val
    return result



c = "abcdef"
l = [1,2,5]
print(capitalize(c, l))
