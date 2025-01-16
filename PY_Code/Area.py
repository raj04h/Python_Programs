import math
def area_circle(radius):
    return math.pi*radius**2
radius =int(input('radius='))

print(f"area_circle= {area_circle(radius)}")


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(3)
print("Area:", circle.area())  # Output: Area: 28.27
print("Circumference:", circle.circumference())  # Output: Circumference: 18.85
