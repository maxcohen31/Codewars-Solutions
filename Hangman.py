# Hangman Game #


# List of words to choose from
import random
words = ['Mathematics', 'Arch', 'illegal', 'illustrious', 'Cypherpunk', 'Algebra', 'Topology']

# Variables
word = random.choice(words)
guesses = []
hp = 5
play = True

# Main loop
while play:
    for letters in word.lower():
        if letters.lower() in guesses:
            print(letters, end = '')
        else:
            print('_', end = '')


    guess = input('Try to guess the word: ')
    guesses.append(guess.lower())

    if guess.lower() in word.lower():
        print('Bravo! You guessed')
    elif guess not in word.lower():
        print(f'Wrong letter! {hp} health point remained.')
        hp -= 1
        if hp == 0:
            break

    play = False
    for letters in word:
        if letters.lower() not in guesses:
            play = True

if play == False:
    print(f'Bravo! You found the word. >> {word}')
else:
    print(f'You lose. The word was {word}')

