def main():
    q = input("Greeting: ").lower().strip()
    if q.startswith("hello"):
        print("$0")
    elif q.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
