def quarter_of(month):
        if month == 1 or month == 2 or month == 3:
            return 1
        elif  month == 4 or month == 5 or month == 6:
            return 2
        elif month == 7 or month == 8 or month == 9:
            return 3
        elif month == 10 or month == 11 or month == 12:
            return 4
     
        
# Clever solution  
def quarter_of2(month):
    return (month + 2) // 3      
        
print(quarter_of2(5))        