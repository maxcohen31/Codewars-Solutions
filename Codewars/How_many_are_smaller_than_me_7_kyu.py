def smaller(arr: list) -> list:
    result = [0] * len(arr)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[i]):
                result[i] += 1
    return result  
        






print(smaller([5, 4, 3, 2, 1]))
print(smaller([1, 2, 1]))