def stray(arr):
    number_dict = {i:arr.count(i) for i in arr}
    for k, v in number_dict.items():
        if v == 1:
            return k

a = [17, 17, 3, 17, 17, 17, 17] 
print(stray(a))