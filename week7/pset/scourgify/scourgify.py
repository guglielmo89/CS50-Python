import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")


    try:
        with open(f"{sys.argv[1]}", "r") as input, open(f"{sys.argv[2]}", "w") as output:
            reader = csv.DictReader(input)
            writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
