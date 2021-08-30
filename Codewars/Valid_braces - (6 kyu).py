def validBraces(s):
        stack, brace_map = [], {"(": ")", "{": "}", "[": "]"}
        for brace in s:
            if brace in brace_map:
                stack.append(brace)       
            elif len(stack) == 0 or brace_map[stack.pop()] != brace:
                return False
        return len(stack) == 0  

# Alternative solution
def validBraces2(string):
    while '()' in string or '{}' in string or '[]' in string:
        string = string.replace('()', '')
        string = string.replace('{}', '')
        string = string.replace('[]', '')
    return False if len(string) != 0 else True            

d = '[(])'
b = "(){}[]"     
x = '())({}}{()][]['

print(validBraces2(b))