def center(strng, width, fill=' '):
    if len(strng) >= width:
        return strng    
    
    result = ""
    if strng == '':
        result = fill * width
    
    elif width % 2 != 0:
        result += strng.center(width, fill)
    elif width % 2 == 0:
        new_result = strng.center(width, fill).split(strng)
        result = new_result[1] + strng + new_result[0]
    elif strng == '':
        result = fill * width
    return result
    
print(center("abc", 10, '_'))   
print(center('' , 2, '$')) 