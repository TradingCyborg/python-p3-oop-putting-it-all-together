#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, model, size, color):
        self.brand = brand
        self.model = model
        self.size = size
        self.color = color
        self.is_worn = False  # Assume the shoe is not worn initially

    def wear(self):
        if not self.is_worn:
            print(f"You are now wearing the {self.color} {self.brand} {self.model}.")
            self.is_worn = True
        else:
            print("The shoes are already worn.")

    def take_off(self):
        if self.is_worn:
            print("You have taken off the shoes.")
            self.is_worn = False
        else:
            print("The shoes are not currently worn.")

# Example usage:
shoe1 = Shoe("Nike", "Air Max", 10, "Blue")
shoe2 = Shoe("Adidas", "Superstar", 9, "White")

print(shoe1.brand)  # Output: Nike
print(shoe2.size)  # Output: 9

shoe1.wear()  # Output: You are now wearing the Blue Nike Air Max.
shoe1.take_off()  # Output: You have taken off the shoes.

shoe2.wear()  # Output: You are now wearing the White Adidas Superstar.
shoe2.wear()  # Output: The shoes are already worn.

    