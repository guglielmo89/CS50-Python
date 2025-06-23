import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1]) as file:
            print(file)
    except FileNotFoundError:
        sys.exit("File not found") 

if __name__ == "__main":
    main()