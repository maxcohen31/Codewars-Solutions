from typing import List
def closest(lst: List[int]) -> int:
    result = min(lst, key=lambda x: abs(x))
    if -result not in lst or not result:
        return result

        
    


print(closest([2, 4, -1, -3]))
print(closest([5, 2, 2]))
print(closest([5, 2, -2]))