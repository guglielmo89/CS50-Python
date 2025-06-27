# Constant
MEOWS = 3

for _ in range(MEOWS):
    print("meow")

class Cat:
    VAR = 3

    def meow(self):
        for _ in range(Cat.VAR):
            print("meow")

cat = Cat()
cat.meow()