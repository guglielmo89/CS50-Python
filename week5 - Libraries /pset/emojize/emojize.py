from emoji import emojize


def main():
    user = input("Input: ")
    print(emojize(user, language="alias"))

main()
