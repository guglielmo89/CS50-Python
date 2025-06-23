def main():
    string = input("Enter text: ")
    print(convert(string))


def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


main()
