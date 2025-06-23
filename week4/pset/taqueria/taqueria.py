MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    order("Item: ")


def order(prompt):
    total = 0
    while True:
        try:
            ord = input(prompt).lower().title()
            total += MENU[ord]
            print(f"${total:.2f}")
        except EOFError:
            return print()
        except KeyError:
            pass


main()
