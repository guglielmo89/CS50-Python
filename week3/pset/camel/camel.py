def main():
    camel = input("camelCase: ")
    print(f"snake_case: {snake(camel)}")

def snake(name):
    x = ""
    for n in name:
        if n.isupper():
            x += "_" + n.lower()
        else:
            x += n
    return x

main()


