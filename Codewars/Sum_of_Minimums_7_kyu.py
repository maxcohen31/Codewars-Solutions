def sum_of_minimums(numbers):
    min_sum = 0
    for row in numbers:
        min_sum += min(row)
    return min_sum





a = [ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]
v = [ [11,12,14,54], [67,89,90,56], [7,9,4,3], [9,8,6,7]]
# print(sum_of_minimums(a))

