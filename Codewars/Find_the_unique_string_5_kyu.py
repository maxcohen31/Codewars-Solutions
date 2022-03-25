from collections import Counter
def find_uniq(arr: list) -> str:
    result = []
    new_arr = Counter(''.join(arr)).most_common()
    
    for word in arr:
        if new_arr[-1][0] in word:
            result.append(word)
    return result[0]        

a = [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]
b = [ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]
print(find_uniq(a))