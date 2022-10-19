def sort_dict(d):
    'return a sorted list of tuples from the dictionary'
    new_d = sorted(d.items(), reverse=True, key=lambda x: x[1])
    return new_d




dictionary = {3:1, 2:2, 1:3}
d2 = {1:2, 2:4, 3:6}
print(sort_dict(dictionary))
print(sort_dict(d2))