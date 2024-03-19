from validator_collection import validators

def main():
    email = input("What's your email? ")

    print(validate_email(email))

def validate_email(email):
    try:
        validators.email(email)
        return "Valid"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()
