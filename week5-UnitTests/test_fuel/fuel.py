import sys

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x <= y:
        percentage = (x / y) * 100
        return round(percentage)
    elif y == 0:
        raise ZeroDivisionError
    else:
        raise ValueError


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <=1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()