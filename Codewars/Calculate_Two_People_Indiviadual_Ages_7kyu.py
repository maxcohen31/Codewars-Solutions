from typing import Tuple

def get_ages(sum_: int, difference: int) -> Tuple[int]:
    result = []
    
    if sum_ < 0 or difference < 0:
        return None
    else:
        """
        x + y = sum_
        x - y = difference

        """
    
        y = (sum_ - difference) / 2
        x = difference + y
    
        if x < 0 or y < 0:
            return None
    
        result.append(x)
        result.append(y)
        result = sorted(result, reverse=True)
    
    
    return tuple(result) 
