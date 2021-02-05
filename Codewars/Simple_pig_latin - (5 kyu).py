# Simple pig latin

def pig_it(text):
    
    text = text.split()
    pig_text = ''
    
    for elements in text:
        if elements.isalpha():
            pig_text += elements[1:] + elements[0] + 'ay' + ' '
        else:
            pig_text += elements 
    return  pig_text[:-1]   
        
        
print(pig_it('Pig latin is cool'))    

           