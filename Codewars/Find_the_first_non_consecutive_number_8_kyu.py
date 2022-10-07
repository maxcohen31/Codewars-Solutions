def first_non_consecutive(arr):
    arr2 = list(range(arr[0],arr[-1]))
    for i in arr2:
        if i not in arr:
            return i+1

a = [1,2,3,4,6,7,8]
print(first_non_consecutive(a))