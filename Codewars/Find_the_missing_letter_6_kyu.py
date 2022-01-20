def find_missing_letter(chars):
    result = ""
    for i in range(1, len(chars)):
        if ord(chars[i]) - ord(chars[i-1]) != 1:
            result += chr(ord(chars[i]) - 1)               
    return result
    
# List comprehension
# def find_missing_letter(chars): 
#     return [chr(ord(chars[i]) - 1) for i in range(1, len(chars)) if ord(chars[i]) - ord(chars[i-1]) != 1][0]
    
                       
a = ["a","b","c","d","f"]
print(find_missing_letter(a))
