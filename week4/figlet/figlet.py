from pyfiglet import Figlet
import sys
import random

def main():

    figlet = Figlet()
    font = figlet.getFonts()

    try:
        check_command_line_arguments()
    except SystemExit as e:
        sys.exit(e)

    user_input = get_user_input()

    #if there is only 1 command line argument it will print the input in a random font
    if len(sys.argv) == 1:
        font_random = random.choice(font)
        figlet.setFont(font=font_random)
        print(figlet.renderText(user_input))
    #if there are 3 command line arguments it will set the font named in the command line argument and print in that font
    elif len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user_input))


#asks the user for input
def get_user_input():
    user_input = input("Input: ")
    return user_input

#checks if the arguments given in the command line are valid
def check_command_line_arguments():
    if len(sys.argv) == 2:
        raise SystemExit("Invalid usage")
    elif len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f":
            raise SystemExit("Invalid usage")
    else:
        pass

main()