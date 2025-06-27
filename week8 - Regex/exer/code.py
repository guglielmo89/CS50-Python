import re

def main():
    code = input("Hexadecimal color code: ")

    pattern = r"^#{1}[a-f0-9]{6}$"

    match = re.search(pattern, code, re.IGNORECASE)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print(f"Invalid.")

main()