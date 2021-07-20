Position = {'high': 'h', 'low': 'l'}  #don't change this!

class Warrior():
    def __init__(self, name):
        # each warrior should be created with a name and 100 health points
        self.name = name
        self.health = 100
        # default guard is "", that is unguarded
        self.block = ""
        self.zombie = False
        self.deceased = False
        
    def attack(self, enemy, position):
        self.damage = 0
        # attacking high deals 10 damage, low 5
        # 0 damage if the enemy blocks in the same position
        if enemy.block != position: self.damage += 10 if position == Position['high'] else 5
        # and even more damage if the enemy is not blocking at all
        if enemy.block == "": self.damage += 5
        enemy.set_health(enemy.health - self.damage)
    
    def set_health(self, new_health):
        # health cannot have negative values
        self.health = max(0, new_health)
        # if a warrior is set to 0 health he is dead
        if self.health == 0:
            self.deceased = True
            self.zombie = False
        # he would be a zombie only if he was already dead
        if self.health < 0 and self.deceased == True:
            self.zombie = True
            
    
    
ninja = Warrior('Hanzo Hattori')
samurai = Warrior('Ryōma Sakamoto') 
samurai.block = 'l'
ninja.attack(samurai, 'h')
print(samurai.health)
