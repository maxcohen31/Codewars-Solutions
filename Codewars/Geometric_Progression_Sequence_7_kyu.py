def geometric_sequence_elements(a, r, n):
    result = []
    for i in range(n):
        result.append(a * pow(r, i))
    return ', '.join(str(i) for i in result)
    
print(geometric_sequence_elements(2, 3, 5))