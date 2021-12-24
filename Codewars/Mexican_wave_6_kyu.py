def wave(people):
    result = []
    for i, p in enumerate(people):
        if p == " ":
            continue
        result.append(people[:i] + people[i].upper() + people[i+1:])
    return result
    
print(wave('two words'))        