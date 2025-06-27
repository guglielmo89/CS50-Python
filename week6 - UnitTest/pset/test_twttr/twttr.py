def main():
    word = input("Input: ").strip()
    print(shorten(word))

def shorten(word):
    try:
        word = str(word)
    except:
        ValueError
    twt = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            twt += char
    return f"{twt}"



if __name__ == "__main__":
    main()
