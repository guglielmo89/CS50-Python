class Package:
# Object instance (properties of the Object) initialization
    def __init__(self, number, sender, recipient, weight):
        self.number = number      # Instance variable
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"""
        -------------------------------------------
        Package: {self.number}: {self.sender} to {self.recipient}, {self.weight}kg
        Shipping cost = {self.calculate_cost(cost_per_kg=2)} USD
        -------------------------------------------"""

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg

def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]

    for package in packages:
        print(package)

main()
