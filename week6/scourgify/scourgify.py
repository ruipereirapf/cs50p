import sys
import csv


def main():
    file_data = []
    if check_arguments() == True:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)

                for row in reader:
                    last, first = row["name"].split(", ")
                    file_data.append({"first": first, "last": last, "house": row["house"]})

                with open(sys.argv[2], "w", newline="") as newfile:
                    writer = csv.DictWriter(
                        newfile, fieldnames=["first", "last", "house"]
                    )
                    writer.writeheader()
                    for line in file_data:
                        writer.writerow(line)
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

def check_arguments():
    if len(sys.argv) == 3:
        return True
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()