def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    return start(plate) and length(plate) and zero(plate)

##########


def start(plate):
    return plate[:2].isalpha() and plate[:].isalnum()


def length(plate):
    return 2 <= len(plate) <= 6


def zero(plate):
    x = []
    if plate[:].isalpha():
        return True
    else:
        for i in range(len(plate)-1):
            if plate[i].isalpha() and plate[i+1].isdigit():
                x.append(i+1)
        if plate[x[0]:].isdigit() and plate[x[0]] != "0":
            return True
        else:
            return False


main()
