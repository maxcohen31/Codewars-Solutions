#Exes and Ohs

def xo(s):
    
    x = s.lower().count('x')
    o = s.lower().count('o')
    if x == o:
        return True
    else:
        return False
    
    

x = 'xxxoo'
print(xo(x))
        
        