from collections import Counter
def sum_no_duplicates(l):
    
    list_ = Counter(l)
    new_list = []
    for k, v in list_.items():
        if v == 1:
            new_list.append(k)
    return sum(new_list)





x = [1, 1, 2, 3] # 5
v = [1, 1, 2, 2, 3] # 3
print(sum_no_duplicates(v))