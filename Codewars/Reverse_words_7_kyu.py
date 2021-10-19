def reverse_words(text): # 7 kyu
    reverse = []
    words = text.split(' ')
    for word in words:
        reverse.append(word[::-1])
    return ' '.join(reverse)  
    
    
t = "This is an example!"    
print(reverse_words(t))