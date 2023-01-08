def create_dict(keys: list, values: list) -> dict:
    result = dict(zip(keys, values))
    
    if len(keys) > len(values):
        for k in keys:
            if k not in result:
                result[k] = None
    return result 
            

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]

print(create_dict(keys, values))