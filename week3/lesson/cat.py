
i = 3
while i != 0 :
    print("meow")
    i -= 1

for j in range(3):
    print("meow")

print("meow\n" * 3, end="")

while True:
    n = int(input("How many times? "))
    if n < 0:
        continue
    else:
        break

def main():
    num = get_number()
    meow(num)

def get_number():
    while True:
        n = int(input("n: "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")
