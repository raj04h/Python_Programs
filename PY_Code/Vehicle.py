class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_vehicle(self):
        return f"Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_car(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

# Creating instances
vehicle = Vehicle("Toyota", "Camry")
car = Car("Ford", "Mustang", 2023)

print(vehicle.display_vehicle())   # Output: Make: Toyota, Model: Camry
print(car.display_car())           # Output: Make: Ford, Model: Mustang, Year: 2023
