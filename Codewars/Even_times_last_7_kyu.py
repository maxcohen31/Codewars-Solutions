def even_last(numbers):
    if len(numbers) > 0:
        summ = 0 
        for i, n in enumerate(numbers):
            if i % 2 == 0:
                summ += numbers[i] 
        return summ * numbers[-1]
    else:
        return 0

arr = [2, 3, 4, 5]
print(even_last(arr))