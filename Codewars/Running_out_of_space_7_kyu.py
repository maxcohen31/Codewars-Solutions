from typing import List

def spacey(array: List[str]) -> List[str]:
    first = [array[0]]
    return first + ["".join(array[:i+1]) for i in range(1, len(array))]


# Alternative Solution

def spacey(array: List[str]) -> List[str]:
    result = []
    s = ""

    for word in array:
        s += word
        result.append(s)
    return result
