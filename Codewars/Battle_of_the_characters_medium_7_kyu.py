from string import ascii_lowercase
def battle(x: str, y: str) -> str:
    upper_case = {chr(i+64):i for i in range(1,27)}
    lower_case = {chr(i+96):(i/2) for i in range(1, 27)} 
    full_dict = {**upper_case, **lower_case}
    power_1 = 0
    power_2 = 0
    
    for k, v in full_dict.items():
        if k in x:
            power_1 += (full_dict[k] * x.count(k))
    
    for k, v in full_dict.items():
        if k in y:
            power_2 += (full_dict[k] * y.count(k))
    
    if power_1 == power_2:
        return 'Tie!'
    elif power_1 > power_2:
        return x
    else:
        return y
    
print(battle('Foo', 'BAR'))