def max_pizza(cuts):
    pieces = 1 # Entire pizza :)
    if cuts >= 0:
        for i in range(cuts + 1):
            pieces += i    
        return pieces
    else:
        return -1
    
print(max_pizza(6))