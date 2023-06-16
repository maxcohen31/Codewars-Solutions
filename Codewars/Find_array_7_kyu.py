from typing import List
def find_array(arr1: List[int|str], arr2: List[int|str]) -> List[int|str]:
    if arr1 == [] or arr2 == []:
        return []

    new_indexes = []
    for i in arr2:
        if i < len(arr1):
            new_indexes.append(i)
    return [arr1[i] for i in new_indexes]



