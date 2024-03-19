def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # test_check(s)

    if start_two_letters(s) == True and min_max_char(s) == True and numbers_at_end(s) == True and is_first_number_zero(s) == False and has_punctuation(s) == False:
        return True
    else:
        return False

#Checks functions returns
# def test_check(z):
#     print("\nstart_two_letters:", start_two_letters(z))
#     print("min_max_char:", min_max_char(z))
#     print("numbers_at_end:", numbers_at_end(z))
#     print("is_first_number_zero:", is_first_number_zero(z))
#     print("has_punctuation:", has_punctuation(z), "\n")

# Checks if string starts with ATLEAST 2 letters
def start_two_letters(a):
    a_substring = a[0:2]

    for character in a_substring:
        if character.isalpha():
            continue
        else:
            return False
    return True

# Checks if string contains minimum of 2 letter and maximum of 6 letters
def min_max_char(b):
    if len(b) >= 2 and len(b) <= 6:
        return True
    else:
        return False

# Checks if string contains LAST characters has numbers in a row and first number isnt 0
def numbers_at_end(c):
    numbers_have_started = False

    for character in c:
        if character.isalpha():
            if numbers_have_started is False:
                continue
            else:
                return False
        else:
            numbers_have_started = True
    return True

# Checks if the first number of the string is 0
def is_first_number_zero(d):
    for character in d:
        if character.isdigit():
            if character == "0":
                return True
            else:
                return False
        else:
            continue
    return False

## Checks if there are no periods, spaces or any kind of punctuation
def has_punctuation(e):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for char in e:
        if char in punctuation:
            return True
    return False

main()