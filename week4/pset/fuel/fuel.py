def main():
    z = convert("Input: ") * 100
    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(f"{round(z)}%")


def convert(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            if (x / y) <= 1:
                return (x / y)
        except (ValueError, ZeroDivisionError):
            pass


main()
