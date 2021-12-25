def median(array):
    array = sorted(array)
    if len(array) % 2 == 0:
        return (array[(len(array) - 1) // 2] + array[len(array) // 2]) / 2
    else:
        return array[len(array) // 2]
        
