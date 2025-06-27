def main():
    t = input("What time is it? ").lstrip("0")
    ct = convert(t)
    if 7 <= ct <= 8:
        print("breakfast time")
    elif 12 <= ct <= 13:
        print("lunch time")
    elif 18 <= ct <= 19:
        print("dinner time")
    else:
        return

def convert(time):
    h, m = time.split(":")
    conv_time = float(h) + float(m)/60
    return conv_time


if __name__ == "__main__":
    main()
