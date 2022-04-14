def string_merge(string1, string2, letter):
    string1 = [string1[0:i] for i, n in enumerate(string1) if n == letter]        
    string2 = [string2[i:] for i, n in enumerate(string2) if n == letter]
    return string1[0] + string2[0]



print(string_merge('hello', 'world', 'l')) 
print(string_merge('coding', 'anywhere', 'n'))
print(string_merge("wonderful", "people", "e"))
print(string_merge("jason", "samson", "s"))
