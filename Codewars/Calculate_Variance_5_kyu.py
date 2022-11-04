def variance(numbers): 
    mean = sum(numbers) / len(numbers)
    variance = 0

    for n in numbers:
        variance += pow((n - mean), 2)
    
    return variance / len(numbers)



x = [12, 23, 65, 89, 94, 200]
print(variance(x))