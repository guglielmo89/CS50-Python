import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"(?:<iframe).+(?:https?://)?(?:www\.)?youtube\.com/embed/(?P<embed>[a-z0-9]{11})"
    if match := re.search(pattern, s, re.IGNORECASE):
        return f"https://youtu.be/{match.group("embed")}"

if __name__ == "__main__":
    main()
