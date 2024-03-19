def main():
    division = check_input("Fraction: ")
    percent = division * 100
    percent_rounded = round(percent)

    if percent_rounded >= 99:
        print("F")
    elif percent_rounded <= 1:
        print("E")
    else:
        print(f"{percent_rounded}%")

def check_input(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            division = x / y

        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        if x > y:
            continue
        else:
            return division

main()