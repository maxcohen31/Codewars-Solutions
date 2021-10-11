def binary_array_to_number(arr):
    return int(''.join([str(i) for i in arr]), 2)
    
    
b = [0, 1, 0, 1]   
print(binary_array_to_number(b))