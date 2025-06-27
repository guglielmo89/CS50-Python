#print hello, world
print("hello, world")

#get user input
name = input("what's your name? ")  # the = is the assigment operator (RIGHT to LEFT ) - input() return a string

#remove blank spaces (or a character) from string from left or right - default value is blank space
name = name.strip()

#capitalize the first letter
name = name.capitalize()

#capitalize the first letter of every word
name = name.title()

#split name
first, last = name.split(" ")

#short hand name = input("what s your name? ").strip().title()

#print a greet
print(f"hello, {first}")

print("hello, ", end="")
print(name)

print("hello, " + name)

print("hello,", name)

print("hello,", name, sep="???")

#positional parameter vs named parameters (optional, i.e. sep or end)
