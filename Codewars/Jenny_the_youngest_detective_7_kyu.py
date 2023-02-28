from typing import List
def missing(nums: List[int], s: str) -> str:
    new_s = s.replace(" ", "")
    new_s = ''.join([i.lower() for i in new_s])
    result = ""

    try:
        for n in sorted(nums, reverse=False):
            result += new_s[new_s.find(new_s[n])]
    except IndexError:
        return "No mission today"
    return result