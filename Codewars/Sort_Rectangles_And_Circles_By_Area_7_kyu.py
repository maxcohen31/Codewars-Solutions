from typing import List, Tuple
from math import pi
def sort_by_area(seq: List[Tuple[float, float]|float]) -> List[Tuple[float, float]|float]: 
    result_area = []
    for data in seq:
        if isinstance(data, tuple):
            result_area.append(data[0]*data[1])
        else:
            result_area.append(pi*(data**2))
    
    return [i[1] for i in sorted(list(zip(result_area, seq)))]
    
    

x = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ]
print(sort_by_area(x)) # [ (1.342, 3.212), 1.23, (4.23, 6.43), 3.444 ]