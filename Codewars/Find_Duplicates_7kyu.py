from typing import List

def duplicates(arr: List[int,str]) -> List[int,str]:
    result = []
    seen = set()
    for i in arr:
        if i in seen:
            result.append(i)
        else:
            seen.add(i)
    return list(dict.fromkeys(result))

