class Student:
    def __init__(self, name, house=None):
        self.name = name
        self.house = house
#        self.patrunus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house = house

#    def charm(self):
#        match self.patronus:
#            case "Stag":
#                return "🦌"
#            case _ :
#                return "🦖"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
#    patronus = input("Patronus: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
