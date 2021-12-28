from math import log
def compare_powers(n1,n2):
    if (n1[1] * log(n1[0])) > (n2[1] * log(n2[0])):
        return -1
    elif (n1[1] * log(n1[0])) < (n2[1] * log(n2[0])):
        return 1    
    elif (n1[1] * log(n1[0])) == (n2[1] * log(n2[0])):
        return 0
    
