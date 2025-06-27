from random import randint

def main():
    random = randint(1,user_level())
    guess = user_guess()
    if guess < random:
        print("Too small!")
        guess = user_guess()
    elif guess > random:
        print("Too large!")
        guess = user_guess()
    return print("Just right!")


def user_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1:
                return level
        except ValueError:
            pass

def user_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess >= 1:
                return guess
        except ValueError:
            pass

if __name__ == "__main__":
    main()
