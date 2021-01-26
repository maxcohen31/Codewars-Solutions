# Rolling dice simulator

from random import randint

class Dice():
    def __init__(self, faces):
        self.faces = faces
        self.score = 0
        types_of_dice = [4, 6, 8, 12, 20]

        if self.faces in types_of_dice:
            print(f'A {self.faces} faces dice!')
        else:
            print('What kind of dice is that?')

    # Method to launch the dice and see the score

    def launch(self):
        self.score = randint(1, self.faces)
        return f'The score is {self.score}'

    # Method to sum the results of the dices

    def __add__(self, other):
        return self.score + other.score







d = Dice(5)
d2 = Dice(12)
print(d.launch())
print(d2.launch())
print(d + d2)
