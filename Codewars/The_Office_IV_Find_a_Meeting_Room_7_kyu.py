def meeting(rooms):
    
    if rooms == []:
        return 'None available!'
    for idx, val in enumerate(rooms):
        if val == 'O':
            return idx
        elif 'O' not in rooms:
            return 'None available!'

print(meeting(['X', 'O', 'X']))

