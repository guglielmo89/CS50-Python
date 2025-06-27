from validator_collection import validators, checkers, errors

def main():
    print(validate(input("What's your email address? ")))

def validate(s):
    try:
        validators.email(s)
        return f"Valid"
    except errors.EmptyValueError:
        return f"Field can't be empy"
    except errors.InvalidEmailError:
        return f"Invalid"


if __name__ == "__main__":
    main()
