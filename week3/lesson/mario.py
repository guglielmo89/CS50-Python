def main():
    print_col(3)
    print_row(5)


def print_col(h):
    for _ in range(h):
        print("#")

def print_row(n):
    print("?" * n)

main()
