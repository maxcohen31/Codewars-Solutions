from collections import Counter
def count(string):
    return Counter(string)

# Second solution    
def count2(s):
    return {x:s.count(x) for x in set(s)}        

