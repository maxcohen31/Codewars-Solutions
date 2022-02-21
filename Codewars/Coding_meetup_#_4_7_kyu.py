def get_first_python(users):
    result = []
    for element in users:
        if element['language'] == 'Python':
            result.append(element['first_name'])
            result.append(element['country'])
    if result == []:
        return 'There will be no Python developers'
    else:     
        return ', '.join(result[0:2])
    
    
print(get_first_python(list1))