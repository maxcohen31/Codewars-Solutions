## A simple textual game ##
import random

def dice():
    # Variables
    print('You have chosen game number 1')
    count = 0
    count_limit = 5
    no_more_guesses = True
    faces = random.randint(1, 20)
    # Main loop
    while count < count_limit and no_more_guesses:
        guess = int(input('Try to guess the number of a d20. You have 5 tries. >> '))
        if guess != faces:
            print('Sorry, wrong number.')
            count += 1
        else:
            no_more_guesses = False
    if no_more_guesses:
        print('Sorry, you are unlucky.')
    else:
        print('Bravo! You win the game')



def rock_paper_scissors():
    print('You have chosen game number 2')
    print("""Enter your choise:
             1 - Rock
             2 - Paper
             3 - Scissors  
          """)
    # Variables
    count = 0
    count_limiter = 5
    # Main loop
    while count < count_limiter:
        your_move = int(input('Enter your choise >> '))
        computer_choice = random.randint(1, 3)

        if your_move == 1 and computer_choice == 1:
            print(f'Draw!')
            count += 1

        elif your_move == 1 and computer_choice == 2:
            print('You lose')
            count += 1

        elif your_move == 1 and computer_choice == 3:
            print('You win!')
            count += 1

        elif your_move == 2 and computer_choice == 1:
            print('You win')
            count += 1

        elif your_move == 2 and computer_choice == 2:
            print('Draw!')
            count += 1

        elif your_move == 2 and computer_choice == 3:
            print('You lose')
            count += 1

        elif your_move == 3  and computer_choice == 1:
            print('You lose')
            count += 1

        elif your_move ==  3 and computer_choice == 2:
            print('You win')
            count += 1

        elif your_move == 3 and computer_choice == 3:
            print('Draw!')
            count += 1
    print('Nice play')


def random_number_generator():
    print('You have chosen game number 3')
    random_number = random.randint(1, 100)
    count = 0
    count_limiter = 5
    # Main loop
    while count < count_limiter:
        print('Try to guess a number between 1 and 100')
        your_number = int(input('>> '))

        if your_number < random_number:
            print('Number too small')
            count += 1
        elif your_number > random_number:
            print('Number too large')
            count += 1
        elif your_number == random_number:
            print('Bravo! You win the game')
            break

    print('You are unlucky. Nice try though')



print("""
        WELCOME TO THIS SIMPLE GAME. PLEASE CHOOSE AN OPTION:
        1 - DICE
        2 - ROCK, PAPER, SCISSORS
        3 - GUESS THE NUMBER   
     """)
game = int(input('Please enter the number of the game you want to play to >> '))
if game == 1:
    dice()

elif game == 2:
     rock_paper_scissors()

elif game == 3:
    random_number_generator()
















