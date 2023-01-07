def find_even_index(arr: list[int]) -> int:
    index = []

    for i in range(len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i+1:])
        if left == right:
            index.append(i)

    if len(index) > 0:
        return index[0]
    elif len(index) == 1:
        return index
    return -1



x = [1, 2, 3, 4, 3, 2, 1]
c = [-100, -1]
z = [0, 0, 0, 0, 0]
print(find_even_index(z))