class Student:
    def __init__(self, name, house=None):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

#return an Object of the class Student, in this way I don't have to create
# a student object first
