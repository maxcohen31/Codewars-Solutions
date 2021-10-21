def adjacent_element_product(array):
    return max(array[number] * array[number+1] for number in range(len(array) - 1))
    

l = [1, 2]    
print(adjacent_element_product(l))