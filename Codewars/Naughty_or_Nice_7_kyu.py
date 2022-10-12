def get_nice_names(people):
    names = []
    for item in people:
        for v in item.values():
            if v == True:
                names.append(item['name'])
    return names

def get_naughty_names(people):
    names = []
    for item in people:
        for v in item.values():
            if v == False:
                names.append(item['name'])
    return names


people = [
    { 'name': 'Warrior reading this kata', 'was_nice': True },
    { 'name': 'xDranik', 'was_nice': False },
    { 'name': 'Santa', 'was_nice': True }
] 

print(get_nice_names(people))
print(get_naughty_names(people))