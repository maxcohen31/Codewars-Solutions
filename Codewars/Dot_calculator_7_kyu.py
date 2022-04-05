def calculator(txt):
    # This is the place to code!
    new_text = txt.split()
    dot1 = len(new_text[0])
    dot2 = len(new_text[2])
    operator = new_text[1]
    
    result = 0
    
    if operator == '+':
        result = dot1 + dot2
    elif operator == '-':
        result = dot1 - dot2
    elif operator == '*':
        result = dot1 * dot2
    elif operator == '//':
        result = dot1 // dot2
    
    return '.' * result
    
    
    
    
a = "..... + ..............."
print(calculator(a))