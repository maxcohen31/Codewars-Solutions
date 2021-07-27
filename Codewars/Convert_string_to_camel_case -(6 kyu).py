def to_camel_case(text):
    if text == '':
        return ''
    else:
        camel = ''
        new_text = text.replace('-', ' ').replace('_', ' ')
        new_text = new_text.split()
        for word in new_text:
            return word[0:] + camel.join(word.capitalize() for word in new_text[1:])
    


    
t = "the_stealth_warrior"
print(to_camel_case(t))