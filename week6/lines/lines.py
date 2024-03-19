import sys

def main():
    file_data = []

    try:
        if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
            with open (sys.argv[1]) as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("#") or line == "":
                        continue
                    else:
                        file_data.append(line)
            print(len(file_data))
        elif len(sys.argv) == 1:
            sys.exit("Too few command-line argument")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()