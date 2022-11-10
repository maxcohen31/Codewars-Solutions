from math import ceil
def new_avg(arr, newavg):
    # Simple math
    number_of_don = len(arr)
    total_donators = number_of_don + 1
    result = ceil((total_donators * newavg) - sum(arr))  

    if result > 0:
        return result
    else:
        raise ValueError