# Moving zeros to the end

def move_zeros(arr):
    zero = 0
    for elements in range(len(arr)):
        if arr[elements] != 0 or arr[elements] is False:
            arr[elements], arr[zero] = arr[zero], arr[elements]
            zero += 1
    return arr




x = [0, 1, 0, 3, False, 12, 5, 7, 0 ,12, 2, 3, 4]
print(move_zeros(x))
