from typing import List

def convert_palindromes(numbers: List[int]) -> List[int]:
    result = []
    for idx, val in enumerate(numbers):
        if str(val) == str(val)[::-1]:
            result.append(1)
        else:
            result.append(0)
    return result



print(convert_palindromes([101, 2, 85, 33, 14014]))