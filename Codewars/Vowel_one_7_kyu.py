def vowel_one(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']    
    result = ""
    
    for i in range(len(s)):
        if s[i] in vowels:
            result += '1'
        else:
            result += '0'
    return result


s = "abceios"
print(vowel_one(s))
