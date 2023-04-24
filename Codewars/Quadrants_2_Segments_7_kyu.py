from typing import List

def quadrant_segment(A: List[int], B: List[int]) -> bool:
    # First sector
    if A[0] > 0 and B[0] > 0 and A[1] > 0 and B[1] > 0:
        return False
    # Third sector
    elif A[0] < 0 and B[0] < 0 and A[1] < 0 and B[1] < 0:
        return False
    # Second sector
    elif A[0] < 0 and A[1] > 0 and B[0] < 0  and B[1] > 0:
        return False
    # Fourth sector
    elif A[0] > 0 and A[1] < 0 and B[0] > 0 and B[1] < 0:
        return False
    else:
        return True
    



print(quadrant_segment((1, 2), (3, 4)))
print(quadrant_segment((9, 3), (-1, 6)))