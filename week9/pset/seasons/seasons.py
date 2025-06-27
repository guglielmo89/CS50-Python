from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        birth = get_date(input("Date of birth: "))
    except ValueError:
        sys.exit("Invalid date")
    time_minutes = (date.today() - birth).days * (24 * 60)
    print(convert(time_minutes), "minutes")

def get_date(prompt):
    return date.fromisoformat(prompt)

def convert(n):
     return f"{p.number_to_words(n, andword="").capitalize()}"

if __name__ == "__main__":
    main()
