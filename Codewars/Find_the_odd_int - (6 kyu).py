# Find the odd integer

def find_it(list):
    for i in list:
        if list.count(i) % 2 != 0:
            return i


x = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(x))
