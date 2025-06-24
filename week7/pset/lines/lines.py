import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(f"{sys.argv[1]}", "r") as file:
            print(read_lines(file))
    except FileNotFoundError:
        sys.exit("File not found")


def read_lines(filename):
    rows = 0
    for row in filename.readlines():
        if not row.lstrip().startswith("#") and row.strip() != "":
            rows += 1
    return rows

if __name__ == "__main__":
    main()
