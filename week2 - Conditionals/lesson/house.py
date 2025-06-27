name = input("Name: ")

#version 1
if name == "Harry":
    print("Griffindor")
elif name == "Hermione":
    print("Griffindor")
elif name == "Draco":
    print("Slythiren")
else :
    print("Who ?")

# version 1
if name == "Harry" or name == "Hermione":
    print("Griffindor")
elif name == "Draco":
    print("Slythiren")
else :
    print("Who ?")

# version 2
match name:
    case "Harry":
        print("griff")
    case "Hermione":
        print("griff")
    case "Draco":
        print("sly")
    case _ :
        print("who ?")

# version 3
match name:
    case "Harry" | "Hermione" | "Ron":
        print("gryff")
    case _:
        print("who ?")
