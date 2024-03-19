import inflect

def main():
    p = inflect.engine()
    names_list = []

    #this cicle prompts the user for a input until a KeyboardInterrupt is inputed
    while True:
        try:
            user_input = get_user_input("Name: ")
            names_list.append(user_input)
        except KeyboardInterrupt:
            break
        except EOFError:
            break

    print(f"Adieu, adieu, to {p.join((names_list))}")


#prompts the user for a input
def get_user_input(prompt):
    user_input = input(prompt)
    return user_input

main()