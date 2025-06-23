import inflect

p = inflect.engine()

def main():
    list_of_names = []
    while True:
        try:
            name = input("Input: ").strip()
            list_of_names.append(name)
        except EOFError:
            print()
            return print("Adieu, adieu, to", p.join(list_of_names))

main()
