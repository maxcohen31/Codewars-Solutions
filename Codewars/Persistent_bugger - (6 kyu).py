# Persistent bugger

def persistence(n):
    
    x = n
    counter = 0
    while x > 9:
        start = 1
        for num in str(x):
            start = start * int(num)
            x = start       
        counter += 1
    return counter
        
       



    