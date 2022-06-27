def alphabet_position(text):
    result = []
    text = text.split()
    alpha = {chr(i+96):i for i in range(1,27)}
    for i in ''.join(text):
        for k, v in alpha.items():
            if k == i or k.upper() == i:
                result.append(' '.join(str(v)))
    new_result = [i.replace(' ', '') for i in result]
    return ' '.join(new_result)


    
    
print(alphabet_position("Five o' clock"))
    
    