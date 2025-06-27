def main():
    t, s = input("What time is it? ").lstrip("0").split()
    ct = convert(t)
    if s == "am" and 7 <= ct <= 8:
        print("breakfast time")
    elif s == "pm" and 0 <= ct <= 1:
        print("lunch time")
    elif s == "pm" and 6 <= ct <= 7:
        print("dinner time")
    else:
        return

def convert(time):
    h, m = time.split(":")
    if float(h) == 12:
        h = 0
    conv_time = float(h) + float(m)/60
    return conv_time


if __name__ == "__main__":
    main()
