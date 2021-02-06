# Sum of positive

def positive_sum(arr):
    pos_sum = sum(a for a in arr if a > 0)
    return pos_sum


# Another solution

def positive_sum2(arr):
    initial_sum = 0
    for elements in arr:
        if elements > 0:
            initial_sum = initial_sum + elements
    return initial_sum        
    
    
    
a = []
print(positive_sum2(a)) 