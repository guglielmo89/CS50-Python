def main():
    x = float(input("X: "))
    y = float(input("Y: "))
    print(f"{x} elevated to {y} is", elevate(x, y))

def elevate(a, b):
    return a ** b

main()
