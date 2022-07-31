def remove_rotten(bag_of_fruits: list) -> list:
    
    fruit = []
    if bag_of_fruits == [] or bag_of_fruits == None:
        return []
    for f in bag_of_fruits:
        if 'rotten' in f:
            fruit.append(f.replace('rotten', '').lower())
        else:
            fruit.append(f.lower())
    return fruit

f = ["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi"]
x = ['apple', 'banana', 'kiwi', 'melone', 'orange']
print(remove_rotten(x))