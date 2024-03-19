name = input("Type name in camelCase: ")

for letter in range(len(name)):
    if name[letter].isupper():
        print("_", name[letter].lower(), sep="", end="")
    else:
        print(name[letter], end="")
        letter + 14