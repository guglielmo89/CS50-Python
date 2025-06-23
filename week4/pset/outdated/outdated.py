MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        s = input("Date: ").strip()
        try:
            month, day, year = s.split("/")
            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                return print(f"{year}-{int(month):02}-{int(day):02}")
        except:
            try:
                m_d, year = s.split(", ")
                month, day = m_d.split(" ")
                if month in MONTHS and (1 <= int(day) <= 31):
                    month = MONTHS.index(month) + 1
                    return print(f"{year}-{month:02}-{int(day):02}")
            except:
                pass


main()
