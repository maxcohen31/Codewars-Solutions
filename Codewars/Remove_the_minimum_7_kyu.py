def remove_smallest(numbers):
    n = numbers.copy()
    if len(numbers) < 1 :
	    return numbers
    else:
	    n.remove(min(numbers))
    return n



print(remove_smallest([1, 2, 3, 1, 1]))
print(remove_smallest([2, 1, 3, 4, 5]))