students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

gryffindors1 = {student: "Gryffindor" for student in students}

print(gryffindors)
print(gryffindors1)