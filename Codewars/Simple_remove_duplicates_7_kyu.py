def solve(arr):
    result = []
    new_arr = arr[::-1]
    for i, a in enumerate(new_arr):
        if new_arr[i] not in result:
            result.append(new_arr[i])
    return result[::-1] 
   
a = [3, 4, 4, 3, 6, 3]    
# print(solve(a))

from string import ascii_lowercase
num = []
alpha = {i:ord(i) for i in ascii_lowercase}
numbers = str(list(range(97, 123)))
a = '10197115121'
for k, v in alpha.items():
    if str(v) in a:
        num.append(k)
print(num)