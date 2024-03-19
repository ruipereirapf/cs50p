message = input("Input: ")
vowels =["a","e","i","o","u","A","E","I","O","U"]

for letter in message:
    if letter in vowels:
        message = message.replace(letter, "")

print(message)