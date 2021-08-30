def vaporcode(s):
    return '  '.join(s.upper().replace(' ', ''))
    
    
    
mess = "Lets go to the movies"    
print(vaporcode(mess))