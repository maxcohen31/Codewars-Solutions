# One-liner
def get_larger_numbers(a, b):
    return [max(number1, number2) for number1, number2 in list(zip(a, b))]

    
    
# def get_larger_numbers(a, b):
#     result = []
#     compared = list(zip(a, b))
#     for number1, number2 in compared:
#         result.append(max(number1, number2))
#     return result
    
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
print(get_larger_numbers(arr1, arr2))