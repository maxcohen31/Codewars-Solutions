def is_vow(inp):
    for vowel in range(len(inp)):
        if inp[vowel] == 'a':
            inp[vowel] = 97
        elif inp[vowel] == 'e':
            inp[vowel] = 101
        elif inp[vowel] == 'i':
            inp[vowel] = 105
        elif inp[vowel] == 'o':
            inp[vowel] = 111
        elif inp[vowel] == 'u':
            inp[vowel] = 117            
        elif inp[vowel] == 97:
            inp[vowel] = 'a'
        elif inp[vowel] == 101:
            inp[vowel] = 'e'
        elif inp[vowel] == 105:
            inp[vowel] = 'i'
        elif inp[vowel] == 111:
            inp[vowel] = 'o'
        elif inp[vowel] == 117:
            inp[vowel] = 'u'                  
    return inp        

# Better solution 
def is_vowe(inp):
    vowels = 'aeiou'
    for v in range(len(inp)):
        if chr(inp[v]) in vowels:
            inp[v] = chr(inp[v])
    return inp



c = [118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]
b = [100, 100, 116, 105, 117, 121]
print(is_vow(c))


