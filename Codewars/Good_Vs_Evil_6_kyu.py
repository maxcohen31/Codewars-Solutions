def good_vs_evil(good, evil):
    new_good = good.split()
    new_evil = evil.split()

    good_ = {
        'Hoobit': 1,
        'Men': 2,
        'Elves': 3,
        'Dwarves': 3,
        'Eagles': 4,
        'Wizard': 10
        }
    
    evil_ = {
        'Orcs': 1,
        'Men': 2,
        'Wargs': 2,
        'Goblins': 2,
        'Uruk Hai': 3,
        'Trolls': 5,
        'Wizard': 10
    }
    
    good_index = 0
    evil_index = 0
    good_army = 0
    evil_army = 0
    
    for v in good_.values():
        good_army += v * int(new_good[good_index])
        good_index += 1     
        
    for v in evil_.values():
        evil_army += v * int(new_evil[evil_index])
        evil_index += 1    
    
    if good_army < evil_army:
        return "Battle Result: Evil eradicates all trace of Good"
    elif evil_army < good_army:
        return "Battle Result: Good triumphs over Evil"
    elif good_army == evil_army:
        return "Battle Result: No victor on this battle field"

print(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))
