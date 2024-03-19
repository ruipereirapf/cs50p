def main():
    word = input("Input: ")
    message = shorten(word)
    print(message)


def shorten(word):
    vowels = ["a","e","i","o","u"] #missing uppercase vowels

    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()