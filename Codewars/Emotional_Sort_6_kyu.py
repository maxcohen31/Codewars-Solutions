from typing import List
def sort_emotions(arr: List[str], order: bool) -> List[str]:
    # (ง •̀_•́)ง
    emotions = {
        ':D': 0,
        ':)': 1,
        ':|': 2,
        ':(': 3,
        'T_T': 4,
    }

    if len(arr) == 0:
        return arr

    indexes = []
    result = []
    for k, v in emotions.items():
        for e in arr:
            if k == e:
                indexes.append(v)

    for idx, val in enumerate(indexes):
        for k, v in emotions.items():
            if val == v:
                result.append(k)
    if order:
        return result
    return result[::-1]

# Alternative Sol
def sort_emotions(arr: List[str], order: bool) -> List[str]:
    emotions = {
        ":D"  : 1, 
        ":)"  : 2, 
        ":|"  : 3, 
        ":("  : 4, 
        "T_T" : 5
        }

    return sorted(arr, key=lambda x: emotions[x], reverse=not order)
