from typing import Type

class Warrior:
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        
    def strike(self, enemy: Type, swings: int) -> int:
        #health cannot go below zero
        enemy.health = max([0, enemy.health-(swings*10)])



if __name__ == "__main__":
    n = Warrior("Ninja")
    s = Warrior("Samurai")
    s.strike(n, 3)
    print(n.health)