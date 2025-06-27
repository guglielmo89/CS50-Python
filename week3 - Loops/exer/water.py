from soil import sample

def main():
    moisture = sample()
    days = 0
    print(f"Day: {day}: Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Day: {day}: Moisture is {moisture}%")

    print("It's time to water the plant")

main()
