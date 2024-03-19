import sys, os
from PIL import Image, ImageOps

def main():
    if check_arguments() == True:
        try:
            #opening images
            muppet_image = Image.open(sys.argv[1])
            shirt_image = Image.open("shirt.png")
        except (FileNotFoundError):
            sys.exit("Input does not exist")

        size = shirt_image.size

        final_image = ImageOps.fit(muppet_image, size)

        final_image.paste(shirt_image, mask=shirt_image)

        final_image.save(sys.argv[2])

def check_arguments():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        arg1 = os.path.splitext(sys.argv[1])
        arg2 = os.path.splitext(sys.argv[2])

        if check_extension(arg1[1]) == False or check_extension(arg2[1]) == False:
            sys.exit("Invalid output")
        elif arg1[1] != arg2[1]:
            sys.exit("Input and output have different extensions")

        return True


def check_extension(arg):
    extensions = [".jpg", ".jpeg", ".png"]

    if arg in extensions:
        return True
    else:
        return False

if __name__ == "__main__":
    main()