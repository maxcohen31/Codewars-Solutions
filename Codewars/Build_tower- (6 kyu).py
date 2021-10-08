def tower_builder(n_floors):
    tower = []
    d = '*'
    for i in range(1, 2 * n_floors + 1 , 2):
        tower.append((d * i).center(2 * i - 1))
    return tower


print(tower_builder(3))    
