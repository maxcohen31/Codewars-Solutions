def generate_hashtag(s):
    hashtag = '#' + s.title().replace(' ', '')
    if len(hashtag) > 140:
        return False
    elif hashtag == '#':
        return False
    else:
        return hashtag


    
 


    

