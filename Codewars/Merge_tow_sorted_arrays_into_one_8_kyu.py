def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))


def merge_arrays(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if j not in arr1:
                arr1.append(j)   
    
    for idx, val in enumerate(arr1):
        if arr1.count(val) > 1:
            arr1.remove(arr1[idx])

    return sorted(set(arr1))

print(merge_arrays([1,1,2,3,4], [5,6,7,8]))

