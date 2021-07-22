def sort_array(source_array):
    odds = sorted([item for item in source_array if item % 2 != 0])
    odd_int = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odds[odd_int]
            odd_int += 1
    return source_array

x = [5, 8, 6, 3, 4] # Should return [3, 8, 6, 5, 4]
# print(sort_array(x))    
j = [5, 1, 6] # Should return [1, 5, 6]
odd = sorted([x for x in j if x % 2 != 0])
# print(od)
oddd_ind = 0
for n in range(len(j)):
    if j[n] % 2 != 0:
        j[n] = odd[oddd_ind]
        oddd_ind += 1 
           
      




x = [5, 8, 6, 3, 4] # Should return [3, 8, 6, 5, 4]    