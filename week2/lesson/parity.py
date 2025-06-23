def main():
    x = int(input("x: "))
    if parity(x):
        print("Even")
    else:
        print("Odd")
        
# version 1
def parity(num):
    if num % 2 == 0:
        return True

# version 2
def is_even(num):
    return True if num % 2 == 0 else False

# version 3
def other(num):
    return (num % 2 == 0)

main()
