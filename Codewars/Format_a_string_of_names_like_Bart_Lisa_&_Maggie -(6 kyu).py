# Stupid way

def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return names[0]['name'] + ' & ' + names[1]['name']
    elif len(names) == 3:
        return names[0]['name'] + ', ' + names[1]['name'] + ' & ' + names[2]['name']
    elif len(names) == 4:
        return names[0]['name'] + ', ' + names[1]['name'] + ', ' + names[2]['name'] + ' & ' + names[3]['name'] 
    elif len(names) == 5:
        return names[0]['name'] + ', ' + names[1]['name'] + ', ' + names[2]['name'] + ', ' + names[3]['name'] + ' & ' + names[4]['name']
    elif len(names) == 6:
        return names[0]['name'] + ', ' + names[1]['name'] + ', ' + names[2]['name'] + ', ' + names[3]['name'] + ', ' + names[4]['name'] + ' & ' +  names[5]['name']
    elif len(names) == 7:
        return names[0]['name'] + ', ' + names[1]['name'] + ', ' + names[2]['name'] + ', ' + names[3]['name'] + ', ' + names[4]['name'] + ', ' +  names[5]['name'] +  ' & ' + names[6]['name'] 
    elif len(names) == 8:
        return names[0]['name'] + ', ' + names[1]['name'] + ', ' + names[2]['name'] + ', ' + names[3]['name'] + ', ' + names[4]['name'] + ', ' +  names[5]['name'] +  ', ' + names[6]['name'] + ' & ' + names[7]['name']    
    elif len(names) == 9:
        return names[0]['name'] + ', ' + names[1]['name'] + ', ' + names[2]['name'] + ', ' + names[3]['name'] + ', ' + names[4]['name'] + ', ' +  names[5]['name'] +  ', ' + names[6]['name'] + ', ' + names[7]['name'] + ' & ' + names[8]['name']
    
# Clever way
def namelist2(names):
    if len(names) == 0: 
        return ''
    elif len(names) == 1: 
        return names[0]['name']
    elif len(names) > 1:
        return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']

x = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
print(namelist2(x))