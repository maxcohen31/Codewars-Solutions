# Solution
def itemgetter(item):
    return item['name']
    
def get_names(data):
    return list(map(itemgetter,data))

# Solution 2    
def get_names(data):
    names = []
    for d in data:
        for k, v in d.items():
            if k == 'name':
                names.append(v)
    return names


data = [
    {'name': 'Joe', 'age': 20},
    {'name': 'Bill', 'age': 30},
    {'name': 'Kate', 'age': 23}
]


print(get_names(data))