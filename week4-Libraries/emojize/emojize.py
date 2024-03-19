import emoji

def main():
    text = input("Input: ")
    print(emoji.emojize(text, language="alias"))

main()