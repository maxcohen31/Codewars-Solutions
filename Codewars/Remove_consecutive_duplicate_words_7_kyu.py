from itertools import groupby
def remove_consecutive_duplicates(s):
    s = s.split()
    new_s = [i[0] for i in groupby(s)] 
    return ' '.join(new_s)
    
    
# Alternative Solution
def remove_consecutive_duplicates2(s):
    s = s.split()
    first = [s[0]]
    for word in s[1:]:
        if word != first:
            first.append(word) 
    return first    

x = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
print(remove_consecutive_duplicates(x))

