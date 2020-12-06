print("""
    ** WELCOME **
      """)
# Variables
name = input('What is your name? >> ')
print('Hello', name)
life_point = 10
age = int(input('Enter your age >> '))
# Main
if age > 21:

    while life_point > 0 and life_point <= 10:
        print('You are old enough to play')
        print("Let's get started")
        print('A cataclysm is approaching.Hurry! You have to save Jane.')
        run_for_your_life = input('Do you wanna run or take the car: R/C >> ')


        if run_for_your_life == 'R':
            print('Sorry, you got hit by a car. You died... Oh, Jane died too.')
            life_point -= 10

        else:
            print('Nice, you are driving your car')
            print('You are nearby a tower')
            climb_or_not_climb = input('Do you want to climb it? C/NC >> ')

            if climb_or_not_climb == 'C':
                print('You see Jane in her garden asking for help. She is well, though.')
                print('You are on your way to her')
                print('A thug is threatening you with a knife')
                fight_or_run_away = input('Do you want to fight him or run away? F/R >> ')

                if fight_or_run_away == 'F':
                    print('You got stabbed. You lose... Oh, and Jane died too')
                    life_point -= 10

                else:
                    print('You run away and the thug gets hit by a meteor')
                    print("You are almost to Jane's house")
                    print('All of a sudden you have to dodge a car')
                    dodge_or_not_dodge = input('Do you wanna dodge the car? D/ND >> ')

                    if dodge_or_not_dodge == 'D':
                        print('You saved Jane. You Win')
                        break
                    else:
                        print('You get hit by the car. You died.')
                        life_point -= 10
            else:
                print('You are watching your phone while driving. You hit a wall. You lose... Oh, Jane died too')
                life_point -= 10
else:
    print('Sorry, too young to play')
