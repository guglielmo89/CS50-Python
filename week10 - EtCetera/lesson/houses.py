# Set() 
students = [
    {"name": "Hermione", "house": "Gryffindor",},
    {"name": "Harry", "house": "Gryffindor",},
    {"name": "Ron", "house": "Gryffindor",},
    {"name": "Draco", "house": "Slytherin",},
    {"name": "Padma", "house": "Ravenclaw",},
]

houses = set() # List of item without duplicates
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)