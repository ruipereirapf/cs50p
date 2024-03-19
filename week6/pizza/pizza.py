import sys
import csv
from tabulate import tabulate


def main():

    menu = []

    if check_arguments() == True:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for pizza, small, large in reader:
                    menu.append(
                        {
                            "pizza": pizza,
                            "small": small,
                            "large": large,
                        }
                    )
                print(menu)
                print(tabulate(menu, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exit")

    else:
        sys.exit()


def check_arguments():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        return True
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
