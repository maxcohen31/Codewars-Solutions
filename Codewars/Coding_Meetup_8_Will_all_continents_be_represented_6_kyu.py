def all_continents(lst): 
    cont = {'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'}
    continets = set([person['continent'] for person in lst])
    if continets == cont:
        return True
    return False
