def main():
    user_list = dict(sorted(grocery("").items()))
    for item in user_list:
        print(f"{user_list[item]} {item}")


def grocery(prompt):
    grocery_list = {}
    while True:
        try:
            groc_item = input(prompt).upper()
            grocery_list[groc_item] += 1
        except EOFError:
            return grocery_list
        except KeyError:
            grocery_list[groc_item] = 1


main()
