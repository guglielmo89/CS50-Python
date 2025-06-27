DENOMINATIONS = (25, 10, 5)

def main():
    amount = 50
    while int(amount) > 0:
        print(f"Amount due: {amount}")
        user = int(input("Insert coint: "))
        if user not in DENOMINATIONS:
            continue
        amount = amount - user
    return print(f"Change owed: {amount * -1}")

main()
