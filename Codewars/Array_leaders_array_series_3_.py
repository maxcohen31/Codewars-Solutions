def array_leaders(numbers):
    result = []
    for n in range(0, len(numbers)):
        if numbers[n] > sum(numbers[n+1:]):
            result.append(numbers[n])    
    return result

# Better Solution
def array_leaders2(numbers):
    return [numbers[n] for n in range(0, len(numbers)) if numbers[n] > sum(numbers[n+1:])]

a = [1,2,3,4,0]
print(array_leaders2(a))