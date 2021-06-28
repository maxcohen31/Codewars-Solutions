def filter_list(l):
    n = filter(lambda x: isinstance(x, int), l)
    return list(n)

lis = [1,2,'a','b']

# Alternative method
def filter_list_2(l):
    numbers = []
    for n in l:
        if type(n) == int:
            numbers.append(n)
    return numbers


lis = [1,2,'a','b']
        
