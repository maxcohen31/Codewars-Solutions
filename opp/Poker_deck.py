import random

# Initializing Card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
       return str(self.value) + " of " + str(self.suit)

# Initializing Deck class
class Deck(list):
    def __init__(self):
        super().__init__()
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["♠", "♥", "♦", "♣"]
        for v in values:
            for s in suits:
                self.append(Card(v, s))

    # Method to shuffle the deck
    def shuffling_the_deck(self):
        print('Shuffled deck: ')
        random.shuffle(self)

    # Method to draw the first card from the deck
    def deal_a_card(self):
         return self.pop(0)

# Initializing the player class
class Player(Deck):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hand_card = []

    # method to count the cards in hand
    def counting_cards(self):
        print(len(self.hand_card))


