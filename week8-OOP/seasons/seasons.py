# from datetime import date, datetime
# import inflect
# import sys

# p = inflect.engine()

# class Date:
#     ...


# def main():
#     birth_date_str = get_birth_date()
#     current_date = get_current_date()
#     birth_date = convert_to_data_type(birth_date_str)
#     subbed_date = subtract_dates(current_date, birth_date)
#     subtraction_in_minutes = subbed_date_to_min(subbed_date)
#     print(f"{int_to_alpha(subtraction_in_minutes)} minutes")


# #asks and returns the user for the birth date
# def get_birth_date():
#     birth_date_str = input("Birth Date: ")
#     return birth_date_str


# #gets and returns system current date
# def get_current_date():
#     return date.today()
#     #probably datetime.today()

# #converts to date data type
# def convert_to_data_type(date):
#     try:
#         birth_date = datetime.strptime(date, "%Y-%m-%d").date()
#         return birth_date
#     except ValueError:
#         sys.exit("Invalid date")

# #subtracts current date with birth date
# def subtract_dates(current_date, birth_date):
#     subbed_date = current_date - birth_date
#     return subbed_date

# #gets the date in minutes
# def subbed_date_to_min(subbed_date):
#     subtraction_in_minutes = int(subbed_date.total_seconds() / 60)
#     return subtraction_in_minutes

# #transforms minutes int to minutes alpha and removes the 'and' word
# def int_to_alpha(subtraction_in_minutes):
#     in_words = p.number_to_words(subtraction_in_minutes, andword="")
#     return in_words.capitalize()


# if __name__ == "__main__":
#     main()


#--------------------------------------------------------------------------------------



from datetime import date, datetime
import inflect
import sys

p = inflect.engine()

def main():
    birth_date_str = get_birth_date()
    current_date = get_current_date()
    birth_date = convert_to_data_type(birth_date_str)
    subbed_date = subtract_dates(current_date, birth_date)
    subtraction_in_minutes = subbed_date_to_min(subbed_date)
    print(f"{int_to_alpha(subtraction_in_minutes)} minutes")


#asks and returns the user for the birth date
def get_birth_date():
    birth_date_str = input("Birth Date: ")
    return birth_date_str


#gets and returns system current date
def get_current_date():
    return date.today()

#converts a date string to date data type
def convert_to_data_type(date):
    try:
        birth_date = datetime.strptime(date, "%Y-%m-%d").date()
        return birth_date
    except ValueError:
        sys.exit("Invalid date")

#subtracts current date with birth date
def subtract_dates(current_date, birth_date):
    subbed_date = current_date - birth_date
    return subbed_date

#gets the date in minutes
def subbed_date_to_min(subbed_date):
    subtraction_in_minutes = int(subbed_date.total_seconds() / 60)
    return subtraction_in_minutes

#transforms minutes int to minutes alpha and removes the 'and' word
def int_to_alpha(subtraction_in_minutes):
    in_words = p.number_to_words(subtraction_in_minutes, andword="")
    return in_words.capitalize()


if __name__ == "__main__":
    main()
