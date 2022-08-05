def title_case(title, minor_words=''):
    if title == '':
        return ''
    
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    result = []
    
    for word in title:
        if word in minor_words:
            result.append(word)
        else:
            result.append(word.capitalize())
    return ' '.join(result)
    

print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox', 'The Quick Brown Fox'))