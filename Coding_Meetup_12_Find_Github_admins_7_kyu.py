def find_admin(lst, lang): 
    return [i for i in lst if i['language'] == lang and i['githubAdmin'] == 'yes' ]