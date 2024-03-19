import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)$", ip):

        g1 = int(matches.group(1))
        g2 = int(matches.group(2))
        g3 = int(matches.group(3))
        g4 = int(matches.group(4))

        if g1 <= 255 and g2 <= 255 and g3 <= 255 and g4 <= 255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()