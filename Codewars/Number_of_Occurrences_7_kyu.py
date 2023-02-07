from typing import List
def number_of_occurrences(element: int, sample: List[int]) -> int:
    arr = sample.copy()
    return arr.count(element)

