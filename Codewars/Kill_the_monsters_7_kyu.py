def kill_monsters(health, monsters, damage):
    if monsters % 3 == 0:
        numb_of_hits = (monsters // 3) - 1
        health = health - (numb_of_hits * damage)   
        result = f"hits: {numb_of_hits}, damage: {numb_of_hits*damage}, health: {health}" 
    elif monsters % 3 != 0:
        numb_of_hits = monsters // 3
        health = health - (numb_of_hits * damage)   
        result = f"hits: {numb_of_hits}, damage: {numb_of_hits*damage}, health: {health}" 
    elif health < 0:
        return 'hero died'  
    return result
        
print(kill_monsters(84, 6, 5))
print(kill_monsters(50, 7, 10))
