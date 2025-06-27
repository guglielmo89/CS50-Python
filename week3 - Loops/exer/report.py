def main():
    spacecraft = {
        "name": "Voyager 1",
        "distance": 163
    }
    spacecraft.update({
        "orbit": "Sun"
    })
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ======= REPORT =======

    Name: {spacecraft["name"]}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ====================== """

main()

# get() retrieve the Value associated to the Key,
# if key doesn t exits --> default Unknown
