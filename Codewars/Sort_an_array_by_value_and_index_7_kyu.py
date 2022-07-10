def sort_by_value_and_index(arr):
    molt = [val * idx for idx,val in enumerate(arr, start=1)]
    zipped_molt_arr = list(zip(molt, arr))
    zipping =  sorted(zipped_molt_arr, key=lambda x: x[0])
    return [j[1] for j in zipping]
        


def sort_by_value_and_index2(arr):
    return [y[1] for y in sorted(enumerate(arr, start=1),key=lambda x:x[0] * x[1])]

a = [23, 2, 3, 4, 5]
x =  [63, 70, 21, 20, 7, 50, 20, 44, 94, 23, 84] # [7, 63, 21, 20, 70, 20, 23, 50, 44, 94, 84]
print(sort_by_value_and_index(x))