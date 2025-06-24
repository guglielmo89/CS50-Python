"""names = []
for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"Hello, {name}")"""


name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

"""with open("names.txt", "r") as file:
    names = []
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")"""

with open("names.txt", "r") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")
