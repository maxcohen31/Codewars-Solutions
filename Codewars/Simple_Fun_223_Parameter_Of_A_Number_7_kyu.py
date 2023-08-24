from math import lcm

def parameter(n: int) -> int:
    n_to_str = [int(i) for i in str(n)]

    mult = 1 
    sum_ = sum(n_to_str)
    for i in n_to_str:
        mult *= i
    return lcm(sum_, mult)
