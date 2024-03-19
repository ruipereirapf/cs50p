import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
        if matches := re.search(r"^([0-9][0-9]?):?([0-9]?[0-9]?) (AM|PM) (to) ([0-9][0-9]?):?([0-9]?[0-9]?) (AM|PM)$", s):

                # declare and validate start working hours schedule variables
                start_hour = int(matches.group(1))
                validate_hour(start_hour)

                if matches.group(2) != "":
                    start_min = int(matches.group(2))
                    validate_min(start_min)

                start_mediridem = matches.group(3).strip()
                if start_mediridem == "PM" and start_hour == 12:
                    start_hour = 12
                elif start_mediridem == "PM":
                    start_hour += 12
                elif start_mediridem == "AM" and start_hour == 12:
                    start_hour = 0

                #validates if 'to' is actually 'to' and not anything else
                validate_to(matches.group(4))

                # declare and validate finish working hours schedule variables
                end_hour = int(matches.group(5))
                validate_hour(end_hour)

                if matches.group(6) != "":
                    end_min = int(matches.group(6))
                    validate_min(end_min)

                end_mediridem = matches.group(7)
                if end_mediridem == "PM" and end_hour == 12:
                    end_hour = 12
                elif end_mediridem == "PM":
                    end_hour += 12
                elif end_mediridem == "AM" and end_hour == 12:
                    end_hour = 0

        else:
            raise ValueError

        if matches.group(2) == "" and matches.group(6) == "":
            return f"{start_hour:02}:00 to {end_hour:02}:00"
        elif matches.group(2) == "":
            return f"{start_hour:02}:00 to {end_hour:02}:{end_min:02}"
        elif matches.group(6) == "":
            return f"{start_hour:02}:{start_min:02} to {end_hour:02}:00"
        else:
            return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"


def validate_hour(hour):
    try:
        hour = int(hour)
        if 1 <= hour <= 12:
            return True
        else:
            raise ValueError
    except ValueError:
        raise ValueError

def validate_min(min):
    try:
        min = int(min)
        if 0 <= min <= 59:
            return True
        else:
            raise ValueError
    except ValueError:
        raise ValueError

def validate_to(to):
    if to == "to":
        return True
    else:
        raise ValueError


if __name__ == "__main__":
    main()
