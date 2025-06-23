def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            pass # or print(......)
        else:
            break
    return x # it's possible to return directly after the try statement

main()
