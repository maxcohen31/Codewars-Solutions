def alternate_case(s):
    result = []
    for letter in s:
        if letter.isupper():
           result.append(letter.lower())
        elif letter == ' ':
            result.append(' ')   
        elif letter.islower():
            result.append(letter.capitalize())
    return ''.join(result)

# Solution 2
def alternate_case2(s):
   return s.swapcase()
       
  