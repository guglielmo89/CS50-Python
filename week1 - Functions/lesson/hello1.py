def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="world"):      #default value if no arg is passed to function
    print("hello,", to)     #side-effect

main()
