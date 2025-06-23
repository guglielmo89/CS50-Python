def main():
    names = ["Mario", "Luigi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender):
    return f"""
    +-------------------------+
        Dear {receiver},

        You are invited to a ball at Peach's Castle
        this evening at 7 pm.

        Sincerly,
        {sender}
    +-------------------------+
    """

main()
