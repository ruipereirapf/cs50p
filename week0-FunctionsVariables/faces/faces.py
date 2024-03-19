def main():
    message = input("Say hello with a smile face: ")
    convert(message)



#This function converts happy and sad smiles to emojis
def convert(message):

    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    print(message)

main()