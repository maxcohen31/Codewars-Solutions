def min_sum(arr: list) -> int:
    sum_ = 0
    arr = sorted(arr)
    
    for i in range(0, len(arr)//2):
        sum_ += arr[i] * arr[-1-i]
    return sum_

# Clever Solution
def min_sum(arr: list) -> int:
    arr.sort()
    return sum(i * arr.pop() for i in arr)


# Another solution
def min_sum3(arr):
    arr = sorted(arr)
    result = 0
    
    for numb in arr:
        result += max(arr) * min(arr)
        arr.remove(max(arr))
        arr.remove(min(arr))
    return result

        

x = [5,4,2,3]
print(min_sum3(x))


