class Food:

    base_hearts = 1   # Class variables

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)

    @classmethod    # a Class method is applied to the entire class not to the single object
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])
        food.hearts = hearts
        return food

def main():
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushrrom"])
    print(f"This skewer increase to {mushroom_skewer.hearts}!")

    mushroom_skewer = Food.from_nothing(hearts=2)

main()
