def longest_consec(strarr, k):
    new_arr = []
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    for i in range(len(strarr)):
        new_arr.append(''.join(strarr[i:i+k]))
        lenght = max(new_arr, key=lambda x: len(x))
    return lenght  

    







strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
print(longest_consec(strarr, 2))