def gimme(input_array):
    middle_element = sorted(input_array)[1]
    return input_array.index(middle_element)
    


a = [2, 3, 1] # should return 0
print(gimme(a))