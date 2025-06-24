def main():
    fuel = input("Input: ")
    return print(gauge(convert(fuel)))


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    if not isinstance(int(x), int) or not isinstance(int(y), int) or int(x) > int(y) :
        raise ValueError
    return round(int(x)/int(y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{str(percentage)}%"




if __name__ == "__main__":
    main()
