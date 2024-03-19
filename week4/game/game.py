import random
import sys

def main():
    while True:
        try:
            #asks for a level and checks if its valid input
            level = get_input("Level: ")
            level = level_check(level)

            #asks for a level guess to the user and checks if its a valid input
            guess = get_input("Guess: ")
            guess = level_check(guess)

            break

        except ValueError:
            continue

    level = random.randrange(1, level)

    while True:
        try:
            if guess < level:
                print("Too small!")

                #asks for a level guess to the user and checks if its a valid input
                guess = get_input("Guess: ")
                guess = level_check(guess)
            elif guess > level:
                print("Too large!")

                #asks for a level guess to the user and checks if its a valid input
                guess = get_input("Guess: ")
                guess = level_check(guess)
            else:
                print("Just right!")
                sys.exit()

        except ValueError:
            continue


#checks in the variable is a digit and returns as int, if not raises ValueError
def level_check(level):
    if level.isdigit():
        level = int(level)
        if level > 0:
            return level
        else:
            raise ValueError
    else:
        raise ValueError

#asks user for a input and returns the input
def get_input(prompt):
    inputed_level = input(prompt)
    return inputed_level


main()