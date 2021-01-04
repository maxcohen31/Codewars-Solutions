import random

# Function to generate a random password

def pass_generator():

    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*£$%&@#'

    # Main loop

    try:
        passwd_choice = int(input('How long do you want your password to be? 8/16 '))
        if passwd_choice == 8:
            passwd_8 = ''
            for x in range(8):
                passwd_8 += random.choice(characters)
                print(passwd_8)

        elif passwd_choice == 16:
            passwd_16 = ''
            for x in range(16):
                passwd_16 += random.choice(characters)
                print(passwd_16)

        else:
            print('Try again')
            return pass_generator()

    except ValueError:
        print('Error!')

# Calling the function

pass_generator()