def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    lowercased= [word.lower() for word in words]
    print(*uppercased, *lowercased)

if __name__ == "__main__":
    main()