students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])


students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter",
    } ,
        {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag",
    }
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
