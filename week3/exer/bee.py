WORDS = {
    "PAIR": 4,
    "HAIR": 4,
    "CHAIR": 5,
    "GRAPHIC": 7,
}

def main():
    print("Welcome to spelling Bee!")
    print("Your letters are: A I P C R H G")

    for word, points in WORDS.items():
        print(f"{word} have {points} points")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You won!")
        if guess in WORDS.keys():
            points = WORDS.pop(guess)   #pop() return the value and remove the key
            print(f"Good job! You scored {points} points")


    print("That's the game!")

main()
