distances = {
    "Voyager 1": "163",
    "Voyager 2": "162",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44",
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print("Can't find the spacecraft")
        return
    except ValueError:
        print("Can't covert to a float")
        return
    m = convert(au)
    print(f"{distances[spacecraft]} AU is {m:,} m ")

def convert(au):
    return au * 149597870700

main()
