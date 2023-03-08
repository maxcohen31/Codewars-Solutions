from typing import Type

class Fighter(object):
    def __init__(self, name: str, health: int, damage_per_attack: int):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1: Type[Fighter], fighter2: Type[Fighter], first_attacker: str) -> str:
    h1 = fighter1.health
    h2 = fighter2.health
    turn = fighter1.name == first_attacker
    while(h1 > 0 and h2 > 0):
        if(turn):
            h2 -= fighter1.damage_per_attack
        else:
            h1 -= fighter2.damage_per_attack
        if(turn):
            turn = True
        else:
            turn = False
    if(h2 < h1):
        return fighter1.name
    else:
        return fighter2.name

if __name__ == "__main__":

    f1 = Fighter("Lew", 10, 2)
    f2 = Fighter("Harry", 5, 4)
    f3 = Fighter("Harald", 20, 5)
    
    print(declare_winner(f1, f2, f1.name))
    print(declare_winner(f3, f2, f3.name))