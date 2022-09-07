def arithmetic_sequence_elements(a, d, n):
	return ', '.join([str(a + (d * i)) for i in range(n)])

    
print(arithmetic_sequence_elements(1, 2, 5))