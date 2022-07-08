def number_of_pairs(gloves):
    pa = []
    tot_gloves = {glove:gloves.count(glove) for glove in gloves}    
    pairs = 0
    for v in tot_gloves.values():
        pa.append(divmod(v, 2))
    
    for i, j in pa:
        pairs += i 
    return pairs

x = ["gray","black","purple","purple","gray","black", 'black']
print(number_of_pairs(x))