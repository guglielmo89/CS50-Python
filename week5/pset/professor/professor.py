import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for j in range(3):
            solution = input(f"{x} + {y} = ").strip()
            try:
                if int(solution) != (x + y):
                    print("EEE")
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")
            if j == 2:
                print(f"{x} + {y} = {x + y}")

    return print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case _:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
