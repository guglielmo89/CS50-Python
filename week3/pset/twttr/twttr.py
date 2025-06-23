VOWELS = ("a", "e", "i", "o", "u")

def main():
    s = input("Input: ")
    o = twitter(s)
    print(f"Output: {o}")


def twitter(text):
    x = ""
    for t in text:
        if t.lower() in VOWELS:
            x += ""
        else:
            x += t
    return x

main()

