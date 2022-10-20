"""
    - accepts two integer arrays of equal length
    - compares the value each member in one array to the corresponding member in the other
    - squares the absolute value difference between those two values
    - and returns the average of those squared absolute value difference between each member pair.

"""

def solution(array_a, array_b):
    result_comparison = []
    for i in range(len(array_a)):
            result_comparison.append(array_b[i] - array_a[i])
    return sum([i**2 for i in result_comparison]) / len(array_a)








a1 = [1,2,3]
a2 = [4,5,6]
b1 = [10, 20, 10, 2]
b2 = [10, 25, 5, -2]
c1 = [-3, 4, 5, 919, 666, -69]
c2 = [12, 3, 55, 911, 555, 44]
print(solution(c1, c2))