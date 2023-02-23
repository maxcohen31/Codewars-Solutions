from typing import Tuple
from itertools import groupby
def longest_repetition(chars: str) -> Tuple[str, int]:
    if chars == "":
        return ("", 0)
    elif len(chars) == 2:
        return chars[0], chars.count(chars[0])

    groups = []
    result = []
    for k, g in groupby(chars):
        groups.append(list(g))
    
    lenghts = [len(group) for group in groups]
    zipping = list(zip(groups, lenghts))
    result = sorted(zipping, key= lambda x: x[1], reverse=True)[0]
    return result[0][1], result[1]


def longest_repetition2(chars):
    count = 0
    char = ''

    for c in chars:
        if c == char:
            count += 1
        else:
            char = c
            count = 1
    return char, count

s = "cbdeuuu900"
b = "bbbaaabaaaa"
a = "ba"
x = "22222sadfsafkkkkk"
print(longest_repetition2(x))