def cakes(recipe, available):
    cakes = []
    for r in recipe.keys():
        if r not in available.keys():
            return 0
    for k, v in recipe.items():
        cakes.append(available[k] // v)     
    return min(cakes)
    
recipe = {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
available = {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}    

print(cakes(recipe3, available3))
