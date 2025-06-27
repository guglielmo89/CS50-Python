# Type hint (test with mypip)

def meow(n: int) -> str:
    """
    Meow n times
    
    :param n: number of times to meow
    :type n: int
    :raise: TypeError: if n not an int
    :return: string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: ").strip())
meows: str = meow(number)
print(meows, end="")