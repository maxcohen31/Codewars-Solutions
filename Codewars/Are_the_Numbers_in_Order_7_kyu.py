def in_asc_order(arr):
    # random_ is not allowed
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True