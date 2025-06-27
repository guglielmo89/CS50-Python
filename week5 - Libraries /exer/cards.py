import random

cards = ["jack", "queen", "king"]

def main():
    random.seed(0) # For debug
    print(random.choice(cards))
    print(random.choices(cards, k=2))
    print(random.sample(cards, k=2))
    print(random.choices(cards, weights=[50, 25, 25], k=2))

main()
