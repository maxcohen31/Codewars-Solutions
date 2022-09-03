def ordered_count(inp):
    inp_d = {i:inp.count(i) for i in inp}
    return [(k, v) for k,v in inp_d.items()]
    


x = 'abracadabra'
# [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
print(ordered_count(x))

print(list(x))