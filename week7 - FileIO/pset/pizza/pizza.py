import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(f"{sys.argv[1]}", "r") as file:
            reader = csv.DictReader(file)
            return print(tabulate(reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
